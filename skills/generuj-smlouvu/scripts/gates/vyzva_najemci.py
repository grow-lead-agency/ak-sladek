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

def gate(data):
    errors = _inputs(data, "vyzva-najemci", "§ 2291 odst. 3 OZ")
    warnings = [
        "§ 2291 odst. 3 OZ: výzva musí předcházet doručení výpovědi; doručte ji prokazatelně a uschovejte důkaz o dojití i její obsah.",
        "§ 2291 odst. 3 OZ nestanoví pevnou minimální lhůtu. Advokát musí posoudit přiměřenost lhůty podle dluhu a požadované nápravy.",
        "§ 2291 odst. 1 a 2 OZ: neuhrazení ve lhůtě samo nestačí; před výpovědí ověřte trvající zvlášť závažné porušení a všechny následné platby."
    ]
    if errors:
        return errors, warnings
    _parties(data, errors, "§ 2291 OZ")
    issue = _date(data["datum_vyzvy"])
    if _date(data["smlouva_datum"]) > issue:
        errors.append("GATE § 2291 OZ: datum nájemní smlouvy následuje po výzvě.")
    if data["rok"] != str(issue.year):
        errors.append("GATE § 2291 OZ: rok podpisu neodpovídá datu výzvy.")
    _debts(data, issue, errors)
    # Jediný zdroj lhůty je číslo. Text pro dokument se odvodí, nikoli přebírá od LLM.
    small = {1:"jednoho",2:"dvou",3:"tří",4:"čtyř",5:"pěti",6:"šesti",7:"sedmi",8:"osmi",9:"devíti",10:"deseti",11:"jedenácti",12:"dvanácti",13:"třinácti",14:"čtrnácti",15:"patnácti",16:"šestnácti",17:"sedmnácti",18:"osmnácti",19:"devatenácti"}
    tens = {20:"dvaceti",30:"třiceti",40:"čtyřiceti",50:"padesáti",60:"šedesáti",70:"sedmdesáti",80:"osmdesáti",90:"devadesáti"}
    n = data["lhuta_dny"]
    words = small[n] if n < 20 else tens[n // 10 * 10] + (" " + ("jedna" if n % 10 == 1 else small[n % 10]) if n % 10 else "")
    data["lhuta_slovy"] = f"{words} ({n}) " + ("dne" if n == 1 else "dnů")
    return errors, warnings
