"""Kontroly vstupů a právních podmínek návrhu. Pouze standardní knihovna."""
import json
import re
from datetime import datetime
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


def gate(data):
    errors = _inputs(data, "najemni-smlouva-byt", "§ 2235, § 2246, § 2251 a § 2254 OZ")
    warnings = [
        "§ 2235 odst. 1 OZ: k ujednáním zkracujícím práva nájemce se nepřihlíží; § 2239 odst. 1 OZ vylučuje zjevně nepřiměřené povinnosti.",
        "§ 7 zákona č. 67/2013 Sb.: vyúčtování doručit do čtyř (4) měsíců po skončení zúčtovacího období; finanční vypořádání nejpozději do čtyř (4) měsíců od doručení vyúčtování.",
        "§ 2254 OZ: jistota a právo na smluvní pokuty mají společný limit trojnásobku měsíčního nájemného bez služeb. Tento vzor smluvní pokutu nesjednává; prověřte případné jiné dohody a úročení jistoty.",
        "§ 2257 OZ a NV č. 308/2015 Sb.: od 1. 1. 2026 činí limit v § 5 částku 1.500,00 Kč, roční hranice podle § 6 činí 150,00 Kč/m². Nejde o univerzální limit každé opravy podle věcného vymezení v § 4.",
        "§ 2247 OZ, § 3 až § 6 zákona č. 67/2013 Sb.: ověřte úplnost služeb a pravidla rozúčtování podle konkrétního domu; zúčtovací období smí mít nejvýše dvanáct (12) měsíců (§ 2 písm. c)).",
        "Předávací protokol potvrďte až podle skutečného stavu při předání; podpis smlouvy sám nenahrazuje předání (§ 2292 a § 2293 OZ)."
    ]
    if errors:
        return errors, warnings
    _parties(data, errors, "§ 2235 OZ")
    rent = _money(data["najemne"])
    deposit = _money(data["jistota"])
    if rent <= 0:
        errors.append("GATE § 2246 OZ: nájemné musí být kladné; bezplatné užívání vyžaduje jiný vzor.")
    if deposit > 3 * rent:
        errors.append("GATE § 2254 odst. 1 OZ: jistota přesahuje trojnásobek měsíčního nájemného bez služeb.")
    if _money(data["zalohy_celkem"]) != sum((_money(s["zaloha"]) for s in data["sluzby"]), Decimal(0)):
        errors.append("GATE § 2247 a § 2251 OZ: součet záloh neodpovídá rozpisu služeb.")
    period = data["doba"]
    if period["typ"] == "urcita" and _date(period["konec"]) < _date(period["zacatek"]):
        errors.append("GATE § 2235 OZ: konec doby určité předchází začátku nájmu.")
    if period["typ"] == "neurcita" and period.get("konec"):
        errors.append("GATE § 2235 OZ: doba neurčitá nesmí současně uvádět datum skončení.")
    if _date(data["predani"]) != _date(data["protokol"]["datum"]):
        errors.append("GATE § 2235 OZ: datum předání a datum protokolu si odporují.")
    days = ["pátého", "šestého", "sedmého", "osmého", "devátého", "desátého", "jedenáctého", "dvanáctého", "třináctého", "čtrnáctého", "patnáctého", "šestnáctého", "sedmnáctého", "osmnáctého", "devatenáctého", "dvacátého", "dvacátého prvního", "dvacátého druhého", "dvacátého třetího", "dvacátého čtvrtého", "dvacátého pátého", "dvacátého šestého", "dvacátého sedmého", "dvacátého osmého"]
    data["splatnost_slovy"] = days[data["splatnost_den"] - 5]
    data["slozit_jistotu"] = deposit > 0
    data["rok_predani"] = str(_date(data["protokol"]["datum"]).year)
    if period["typ"] == "urcita" and _date(data["predani"]) > _date(period["konec"]):
        errors.append("GATE § 2235 OZ: předání Bytu je až po konci sjednaného nájmu.")
    if _date(data["predani"]) != _date(period["zacatek"]):
        warnings.append("§ 2242 OZ: datum předání se liší od začátku nájmu. Ověřte důvod a vypořádání nájemného za první období.")
    return errors, warnings
