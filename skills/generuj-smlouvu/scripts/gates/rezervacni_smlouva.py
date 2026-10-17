"""Hard gate před renderem; bez externích závislostí a bez změny vstupních dat."""
import re
from datetime import datetime
from decimal import Decimal


def _checks(data, legal, parties):
    errors = []
    def get(path):
        value = data
        for key in path.split("."):
            if not isinstance(value, dict):
                return None
            value = value.get(key)
        return value
    def error(text):
        errors.append(f"GATE {legal}: {text}")
    def text(path):
        value = get(path)
        if not isinstance(value, str) or not value.strip():
            error(f"Chybí nebo není vyplněn text {path}.")
            return None
        if any(marker in value for marker in ("{{", "{%", "[ověřit]")):
            error(f"{path} obsahuje nevyplněnou proměnnou nebo údaj k ověření.")
            return None
        return value
    def flag(path):
        value = get(path)
        if type(value) is not bool:
            error(f"{path} musí být výslovně true nebo false.")
            return None
        return value
    def amount(path, positive=True):
        value = text(path)
        if value is None:
            return None
        if not re.fullmatch(r"(?:0|[1-9]\d{0,2}(?:\.\d{3})*),\d{2}", value):
            error(f"{path} musí být částka ve formátu N.NNN,00 bez Kč.")
            return None
        result = Decimal(value.replace(".", "").replace(",", "."))
        if positive and result <= 0:
            error(f"{path} musí být kladná částka.")
        return result
    def date(path):
        value = text(path)
        if value is None:
            return None
        try:
            if not re.fullmatch(r"\d{2}\.\d{2}\.\d{4}", value):
                raise ValueError
            return datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            error(f"{path} musí být platné datum DD.MM.RRRR.")
            return None
    if not isinstance(data, dict):
        error("Vstup musí být objekt JSON.")
    for party in parties:
        for field in ("radek1", "radek2", "podpis"):
            text(party + "." + field)
        for field in ("radek3", "radek4", "radek5", "podpis_zastupce", "email"):
            value = get(party + "." + field)
            if value is not None and not isinstance(value, str):
                error(f"{party}.{field} musí být text nebo null.")
            elif isinstance(value, str) and any(marker in value for marker in ("{{", "{%", "[ověřit]")):
                error(f"{party}.{field} obsahuje nevyplněnou proměnnou nebo údaj k ověření.")
    year = text("rok")
    if year is not None and not re.fullmatch(r"\d{4}", year):
        error("rok musí obsahovat čtyři číslice.")
    for field in ("ku_text", "urad_kraj", "pracoviste"):
        text("nemovitost." + field)
    items = get("nemovitost.polozky")
    if not isinstance(items, list) or not items:
        error("Chybí předmět dle LV: nemovitost.polozky musí obsahovat alespoň jednu položku.")
    else:
        for index, item in enumerate(items):
            if not isinstance(item, dict):
                error(f"nemovitost.polozky[{index}] musí být objekt s text a odrazka.")
                continue
            value = item.get("text")
            if not isinstance(value, str) or not value.strip() or any(marker in value for marker in ("{{", "{%", "[ověřit]")):
                error(f"Chybí úplný text předmětu dle LV v položce {index + 1}.")
            if type(item.get("odrazka")) is not bool:
                error(f"V položce {index + 1} musí být odrazka true nebo false.")
        if isinstance(items[0], dict) and items[0].get("odrazka") is not True:
            error("První položka nemovitosti musí začínat samostatnou odrážkou.")
    return errors, get, text, flag, amount, date, error


def gate(data):
    errors, get, text, flag, amount, date, error = _checks(
        data, "§ 1746 odst. 2 OZ", ("vlastnik", "zajemce"))
    warnings = ["PŘEDMĚT (§ 1746 odst. 2 OZ): ověřte aktuální LV a oprávnění vlastníka; tento vzor je dvoustranná rezervace, bez závazku Zájemce koupit Nemovitost."]
    start = date("rezervace.od")
    end = date("rezervace.do")
    price = amount("rezervace.nabidkova_cena")
    fee = amount("poplatek.castka", positive=False)
    due = date("poplatek.splatnost")
    text("poplatek.prijemce")
    text("poplatek.ucet")
    text("poplatek.ucet_vraceni")
    if start and end and start > end:
        error("Začátek rezervace nesmí být pozdější než její konec.")
    if due and start and end and not start <= due <= end:
        error("Splatnost poplatku musí ležet v době rezervace.")
    fate = get("poplatek.osud")
    if fate not in ("zapocteni", "vraceni", "propadnuti"):
        error('Chybí osud poplatku: poplatek.osud musí být "zapocteni", "vraceni" nebo "propadnuti".')
    if fate in ("zapocteni", "propadnuti") and fee is not None and price is not None and fee > price:
        error("Poplatek započítávaný na cenu nesmí v tomto vzoru převyšovat nabídkovou cenu.")
    if get("poplatek.prijemce") != get("vlastnik.podpis"):
        error("Tento dvoustranný vzor připouští platbu pouze vlastníkovi; poplatek.prijemce musí odpovídat vlastnik.podpis. Jiný příjemce vyžaduje úpravu smlouvy advokátem.")
    consumer = flag("spotrebitel")
    business = flag("vlastnik_podnikatel")
    broker = flag("zprostredkovani.pouzito")
    if consumer is True and business is True:
        warnings.append("SPOTŘEBITEL (§ 1813, § 1814 odst. 1 písm. c) a l), § 1815 OZ): ujednání o propadnutí poplatku, vyváženost náhrad a přiměřenost sankcí musí posoudit advokát; ke zneužívajícímu ujednání se nepřihlíží, ledaže se jej spotřebitel dovolá. Samotná vzájemnost sankcí nestačí.")
    if fate == "propadnuti":
        if fee is not None and fee <= 0:
            error("§ 2048 OZ: pro variantu propadnuti musí být sjednána kladná výše poplatku a pokuty.")
        warnings.append("POPLATEK (§ 2048 až 2051 a § 1982, § 1987 OZ): propadnuti znamená jen přesně vymezenou pokutu za úmyslné nepravdivé údaje, nikdy sankci za nekoupení nebo nezískání úvěru. Advokát posoudí její přiměřenost a podmínky započtení; nejistou nebo neurčitou pohledávku započíst nelze.")
    if broker is True:
        text("zprostredkovani.zprostredkovatel")
        text("zprostredkovani.smlouva")
        warnings.append("ZPROSTŘEDKOVATEL (§ 9 až 12 zákona č. 39/2020 Sb.): advokát ověří písemnou samostatnou smlouvu, předmět, cenu a provizi, aktuálnost výpisu z veřejného seznamu a informační povinnosti. Rozhoduje skutečný obsah vztahu, nikoli označení rezervace.")
        warnings.append("SPOTŘEBITEL A ZPROSTŘEDKOVÁNÍ (§ 14 zákona č. 39/2020 Sb.): spotřebiteli nelze ve zprostředkovatelské smlouvě uložit povinnost uzavřít realitní ani budoucí realitní smlouvu. Tento vzor zprostředkovateli nepřiznává poplatek ani provizi.")
    return errors, warnings

# <!-- Origin: GrowLead, návrh pro AK Sládek | Inspiration: https://www.zakonyprolidi.cz/cs/2012-89, https://www.zakonyprolidi.cz/cs/2020-39 -->
