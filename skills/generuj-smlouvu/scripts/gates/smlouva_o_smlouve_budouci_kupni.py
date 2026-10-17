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
        data, "§ 1785 až 1788 OZ", ("prodavajici", "kupujici"))
    warnings = [
        "FORMA (§ 560 OZ): písemná forma je nutná pro právní jednání převádějící věcné právo k nemovitosti. § 1785 OZ sám písemnou formu smlouvy o smlouvě budoucí nestanoví; tento vzor je písemný pro průkaznost. Advokát ověří formu navazující kupní smlouvy.",
        "LHŮTY (§ 1785, § 1786 a § 1788 OZ): zákon při chybějícím ujednání počítá s jedním rokem a po výzvě s uzavřením bez zbytečného odkladu. Tento vzor záměrně vyžaduje výslovné datum výzvy i podpisu; nejde o tvrzení, že bez nich zákonná smlouva nemůže vzniknout. Advokát ověří dostatečný odstup a doručení výzvy.",
        "PŘEDMĚT (§ 1785 OZ): porovnejte úplný popis, podíly, vlastnictví a omezení s aktuálním LV; gate ověřuje vyplnění, nikoli obsah katastru.",
    ]
    price = amount("cena.celkem")
    text("cena.uhrada")
    call = date("lhuta.vyzva_do")
    close = date("lhuta.uzavreni_do")
    text("lhuta.doruceni")
    text("predani")
    if call and close and call >= close:
        error("Datum výzvy musí v tomto vzoru předcházet nejzazšímu datu uzavření kupní smlouvy.")
    escrow = flag("uschova.pouzita")
    if escrow is True:
        text("uschova.podminky")
        warnings.append("ÚSCHOVA (§ 1785 OZ): podmínky úhrady a vrácení slaďte se samostatnou smlouvou o advokátní úschově; tato Smlouva advokáta nezavazuje.")
    deposit = get("zaloha.typ")
    if deposit not in ("zaloha", "zavdavek", "zadna"):
        error('zaloha.typ musí být "zaloha", "zavdavek" nebo "zadna" (§ 1807 a 1808 OZ).')
    if deposit in ("zaloha", "zavdavek"):
        paid = amount("zaloha.castka")
        text("zaloha.prijemce")
        text("zaloha.ucet")
        if price is not None and paid is not None and paid > price:
            error("Záloha či závdavek započítávané na cenu nesmějí v tomto vzoru překročit kupní cenu.")
    if deposit == "zaloha":
        text("zaloha.splatnost")
        warnings.append("ZÁLOHA (§ 1807 OZ): doporučeno složit zálohu do advokátní úschovy a výslovně sjednat její výplatu a vrácení. Samotné neuzavření koupě neznamená propadnutí zálohy.")
    if deposit == "zavdavek":
        if get("zaloha.odevzdani_potvrzeno") is not True:
            error("§ 1808 odst. 1 OZ: bez ověřeného odevzdání závdavku nejpozději při podpisu nelze vložit potvrzení o jeho přijetí; vyžaduje se zaloha.odevzdani_potvrzeno=true.")
        if get("zaloha.prijemce") != get("prodavajici.podpis"):
            error("§ 1808 OZ: tato varianta potvrzuje přímé přijetí závdavku prodávajícím; zaloha.prijemce musí odpovídat prodavajici.podpis.")
        warnings.append("ZÁVDAVEK (§ 1808 odst. 2 OZ): vysvětlete oběma stranám ponechání při příčině na straně dávajícího a při příčině na straně příjemce alternativu dvojnásobku, splnění nebo při nemožnosti splnění náhrady škody. Zkontrolujte důkaz skutečného odevzdání, samotný příkaz k platbě nestačí.")
        warnings.append("ODSTOUPENÍ (§ 1809 OZ): doplnění smluvního práva odstoupit může změnit režim závdavku na odstupné; tento vzor právo odstoupit za závdavek nesjednává.")
    penalty = flag("pokuta.sjednana")
    if penalty is True:
        amount("pokuta.castka")
        if deposit == "zavdavek":
            error("§ 1808 a § 2048 OZ: tento vzor nepodporuje souběh závdavku a smluvní pokuty. Vyžaduje individuální ujednání advokáta, nikoli automatické sčítání sankcí.")
        warnings.append("SANKCE (§ 2048 až 2051 OZ): ověřte přiměřenost smluvní pokuty; vzor ponechává zákonný režim náhrady škody podle § 2050 OZ.")
    warnings.append("PODMÍNKY (§ 1785 OZ): cena.uhrada musí zohlednit vybraný typ i částku platby a úschovu. Lhůty v textových polích zapisujte slovy i číslem. Financování a spotřebitelské postavení stran posoudí advokát.")
    return errors, warnings

# <!-- Origin: GrowLead, návrh pro AK Sládek | Inspiration: https://www.zakonyprolidi.cz/cs/2012-89, https://www.zakonyprolidi.cz/cs/2020-39 -->
