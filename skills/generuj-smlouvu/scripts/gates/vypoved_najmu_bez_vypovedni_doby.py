"""Kontroly vstupů a právních podmínek návrhu. Pouze standardní knihovna."""
import json
import re
from datetime import date, datetime, timedelta
from decimal import Decimal
from pathlib import Path


def _validate(value, rule, root, path="data"):
    """Omezený validátor pouze klíčových slov použitých v místním schema.json."""
    errors = []
    if "$ref" in rule:
        target = root
        for key in rule["$ref"].split("/")[1:]:
            target = target[key]
        errors.extend(_validate(value, target, root, path))
    for sub in rule.get("allOf", []):
        errors.extend(_validate(value, sub, root, path))
    if "if" in rule:
        branch = "else" if _validate(value, rule["if"], root, path) else "then"
        errors.extend(_validate(value, rule.get(branch, {}), root, path))
    if "not" in rule and not _validate(value, rule["not"], root, path):
        errors.append(f"{path}: nepovolená hodnota.")
    if "const" in rule and (value != rule["const"] or type(value) is not type(rule["const"])):
        errors.append(f"{path}: musí být {rule['const']}.")
    if "enum" in rule and value not in rule["enum"]:
        errors.append(f"{path}: nepovolená hodnota.")
    kinds = {"object": isinstance(value, dict), "array": isinstance(value, list),
             "string": isinstance(value, str), "integer": type(value) is int,
             "boolean": type(value) is bool, "null": value is None}
    expected = rule.get("type")
    if expected and not any(kinds.get(t, False) for t in (expected if isinstance(expected, list) else [expected])):
        return errors + [f"{path}: chybný datový typ."]
    if isinstance(value, dict):
        for key in rule.get("required", []):
            if key not in value:
                errors.append(f"{path}.{key}: chybí povinný údaj.")
        for key, sub in rule.get("properties", {}).items():
            if key in value:
                errors.extend(_validate(value[key], sub, root, f"{path}.{key}"))
        for key, deps in rule.get("dependentRequired", {}).items():
            if key in value:
                for dep in deps:
                    if dep not in value:
                        errors.append(f"{path}.{dep}: chybí související údaj k {key}.")
    elif isinstance(value, list):
        if len(value) < rule.get("minItems", 0):
            errors.append(f"{path}: seznam je prázdný nebo neúplný.")
        for i, item in enumerate(value):
            errors.extend(_validate(item, rule.get("items", {}), root, f"{path}[{i}]"))
    elif isinstance(value, str):
        if len(value.strip()) < rule.get("minLength", 0) or ("pattern" in rule and not re.search(rule["pattern"], value)):
            errors.append(f"{path}: prázdný údaj nebo chybný formát.")
        if rule.get("format") == "cz-date":
            try:
                _date(value)
            except ValueError:
                errors.append(f"{path}: neplatné kalendářní datum.")
        if "\u2013" in value or "\u2014" in value:
            errors.append(f"{path}: použijte spojovník místo dlouhé pomlčky (pravidlo kanceláře).")
    elif type(value) is int:
        if value < rule.get("minimum", value) or value > rule.get("maximum", value):
            errors.append(f"{path}: hodnota mimo povolený rozsah.")
    return errors


def _date(value):
    return datetime.strptime(value, "%d.%m.%Y").date()


def _money(value):
    return Decimal(value.replace(".", "").replace(",", "."))


def _inputs(data, slug, section):
    schema_path = Path(__file__).resolve().parents[2] / "vzory" / slug / "schema.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    return [f"GATE {section}: {e}" for e in _validate(data, schema, schema)]


def _parties(data, errors, section):
    if " ".join(data["pronajimatel"]["radek1"].casefold().split()) == " ".join(data["najemce"]["radek1"].casefold().split()):
        errors.append(f"GATE {section}: pronajímatel a nájemce mají stejnou identifikaci, ověřte strany.")


def _debts(data, asof, errors):
    rows = data["dluhy"]
    months = [row["mesic"] for row in rows]
    if len(months) != len(set(months)):
        errors.append("GATE § 2291 OZ: duplicitní dlužný měsíc, položky téhož měsíce slučte.")
    total = Decimal(0)
    for row in rows:
        amount = _money(row["najemne"]) + _money(row["sluzby"])
        total += amount
        if row["mesic"] < _date(data["smlouva_datum"]).strftime("%Y-%m"):
            errors.append("GATE § 2291 OZ: dlužné období předchází měsíci uzavření označené smlouvy; ověřte právní titul dluhu.")
        if amount <= 0:
            errors.append("GATE § 2291 OZ: každý uvedený měsíc musí obsahovat skutečný kladný dluh.")
        if _date(row["splatnost"]) >= asof:
            errors.append("GATE § 2291 OZ: dluh dosud není po splatnosti k datu listiny.")
        if row["mesic"] > asof.strftime("%Y-%m"):
            errors.append("GATE § 2291 OZ: dlužný měsíc leží v budoucnu.")
    if _money(data["dluh_celkem"]) != total:
        errors.append("GATE § 2291 OZ: dluh_celkem neodpovídá součtu položek.")
    return len(set(months))

def _easter(year):
    """Gregoriánský výpočet Velikonoční neděle (Meeus/Jones/Butcher)."""
    a = year % 19
    b, c = divmod(year, 100)
    d, e = divmod(b, 4)
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = divmod(c, 4)
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month, remainder = divmod(h + l - 7 * m + 114, 31)
    return date(year, month, remainder + 1)


def _deadline(received, days):
    """§ 605 odst. 1 a § 607 OZ; svátky podle § 1 a § 2 zákona č. 245/2000 Sb."""
    end = received + timedelta(days=days)
    fixed = {(1, 1), (5, 1), (5, 8), (7, 5), (7, 6), (9, 28), (10, 28), (11, 17), (12, 24), (12, 25), (12, 26)}
    while True:
        easter = _easter(end.year)
        holiday = (end.month, end.day) in fixed or end in (easter - timedelta(days=2), easter + timedelta(days=1))
        if end.weekday() < 5 and not holiday:
            return end
        end += timedelta(days=1)


def gate(data):
    errors = _inputs(data, "vypoved-najmu-bez-vypovedni-doby", "§ 2286, § 2290 a § 2291 OZ")
    warnings = [
        "§ 2286 odst. 1 OZ: výpověď musí být písemná a musí nájemci dojít; doložte dojití každému adresátovi, včetně případných společných nájemců.",
        "§ 605 a § 607 OZ: počet dnů a doručení přepište přesně z předchozí výzvy; lhuta_do se kontroluje včetně českých svátků. Vzor podporuje lhůtu v kalendářních dnech od dojití.",
        "§ 2291 odst. 3 OZ: bez předchozí výzvy k nápravě v přiměřené době nebo bez konkretizace důvodu se k výpovědi nepřihlíží. Prověřte shodu důvodu s výzvou, přiměřenost lhůty a trvání porušení i při dojití výpovědi.",
        "§ 2286 odst. 2 a § 2290 OZ: poučení o námitkách i soudním přezkumu je vždy vloženo. Dvouměsíční lhůta pro soudní přezkum je hmotněprávní; návrh musí včas dojít soudu, nestačí jej poslední den odeslat.",
        "§ 2291 odst. 1 OZ: požadujte odevzdání bez zbytečného odkladu, nejpozději do jednoho (1) měsíce od skončení nájmu. Výpověď sama neopravňuje ke svémocnému vyklizení; případný soudní postup posoudí advokát.",
        "§ 2291 odst. 2 OZ: počet měsíců nenahrazuje právní posouzení intenzity porušení, zejména u částečných úhrad, bagatelních zbytků nebo sporných služeb."
    ]
    if errors:
        return errors, warnings
    _parties(data, errors, "§ 2291 OZ")
    issue = _date(data["datum_vypovedi"])
    prior = data["predchozi_vyzva"]
    sent, received, limit = (_date(prior[k]) for k in ("datum", "doruceni", "lhuta_do"))
    if not (_date(data["smlouva_datum"]) <= sent <= received < limit < issue):
        errors.append("GATE § 2291 odst. 3 OZ: ověřte pořadí smlouva, výzva, její dojití, konec přiměřené lhůty a následná výpověď. Náprava musí mít skutečný časový prostor.")
    try:
        expected_limit = _deadline(received, prior["lhuta_dny"])
        if limit != expected_limit:
            errors.append(f"GATE § 605 a § 607 OZ: lhuta_do neodpovídá počtu dnů od dojití a posunu na pracovní den; správně {expected_limit:%d.%m.%Y}.")
    except (OverflowError, ValueError):
        errors.append("GATE § 605 a § 607 OZ: lhůta přesahuje podporovaný kalendářní rozsah.")
    if data["rok"] != str(issue.year):
        errors.append("GATE § 2286 OZ: rok podpisu neodpovídá datu výpovědi.")
    if data["duvod_typ"] == "neplaceni":
        months = _debts(data, issue, errors)
        if not any(_date(row["splatnost"]) < sent for row in data["dluhy"]):
            errors.append("GATE § 2291 odst. 3 OZ: žádný uvedený dluh nebyl po splatnosti již při předchozí výzvě.")
        if months < 3:
            errors.append("GATE § 2291 odst. 2 OZ: neplacení je doloženo za méně než tři (3) různé měsíce.")
    elif "dluhy" in data or "dluh_celkem" in data:
        errors.append("GATE § 2291 OZ: u jiného důvodu neuvádějte skrytý rozpis dluhu; rozhodné skutky popište v duvod_popis.")
    return errors, warnings
