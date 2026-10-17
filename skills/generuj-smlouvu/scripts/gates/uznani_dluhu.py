"""Hard gates uznání dluhu. Částky se sčítají v celých haléřích."""
import re
from datetime import datetime

MONEY = re.compile(r"(?:0|[1-9][0-9]{0,2}(?:\.[0-9]{3})*),[0-9]{2}")


def _text(value):
    return isinstance(value, str) and bool(value.strip())


def _money(value):
    if not isinstance(value, str) or not MONEY.fullmatch(value):
        return None
    whole, cents = value.replace(".", "").split(",")
    return int(whole) * 100 + int(cents)


def _date(value):
    if not isinstance(value, str) or not re.fullmatch(r"[0-9]{2}\.[0-9]{2}\.[0-9]{4}", value):
        return None
    try:
        return datetime.strptime(value, "%d.%m.%Y").date()
    except ValueError:
        return None


def gate(data):
    errors, warnings = [], []
    if not isinstance(data, dict):
        return ["GATE § 2053 OZ: data musí být objekt."], []
    for key in ("veritel", "dluznik"):
        party = data.get(key)
        if not isinstance(party, dict):
            errors.append(f"GATE § 2053 OZ: chybí řádná identifikace strany {key}.")
            continue
        for field in ("radek1", "radek2", "podpis"):
            if not _text(party.get(field)):
                errors.append(f"GATE § 2053 OZ: chybí {key}.{field}.")
        if party.get("typ") not in ("FO", "PO"):
            errors.append(f"GATE § 2053 OZ: {key}.typ musí být FO nebo PO.")
        for field in ("radek3", "radek4", "radek5", "podpis_zastupce"):
            if party.get(field) is not None and not isinstance(party[field], str):
                errors.append(f"GATE § 2053 OZ: {key}.{field} musí být text nebo null.")
        if party.get("typ") == "PO" and not _text(party.get("podpis_zastupce")):
            errors.append(f"GATE § 2053 OZ: u PO chybí {key}.podpis_zastupce; ověřte oprávnění jednat.")
    if not _text(data.get("duvod")):
        errors.append("GATE § 2053 OZ: chybí určitý právní důvod dluhu (duvod).")
    total = _money(data.get("castka"))
    principal = _money(data.get("jistina"))
    if total is None or total <= 0:
        errors.append("GATE § 2053 OZ: chybí výše dluhu nebo castka není kladná částka ve formátu N.NNN,00.")
    if principal is None:
        errors.append("GATE § 2053 OZ: jistina musí být nezáporná částka ve formátu N.NNN,00.")
    accessories = data.setdefault("prislusenstvi", [])
    accessory_total = 0
    valid_accessories = isinstance(accessories, list)
    if not valid_accessories:
        errors.append("GATE § 2053 OZ: prislusenstvi musí být seznam vyčíslených nároků.")
    else:
        for i, item in enumerate(accessories, 1):
            if not isinstance(item, dict):
                errors.append(f"GATE § 2053 OZ: příslušenství {i} musí být objekt.")
                valid_accessories = False
                continue
            amount = _money(item.get("castka"))
            if not _text(item.get("duvod")) or amount is None or amount <= 0:
                errors.append(f"GATE § 2053 OZ: příslušenství {i} musí mít určitý důvod a kladnou vyčíslenou částku.")
                valid_accessories = False
            else:
                accessory_total += amount
    if valid_accessories and principal is not None and total is not None and principal + accessory_total != total:
        errors.append("GATE § 2053 OZ: součet jistiny a vyčísleného příslušenství se nerovná uznané částce (kontrola v haléřích).")
    installments = data.get("splatky")
    if not isinstance(installments, list) or not installments:
        errors.append("GATE § 641 OZ: chybí splátkový kalendář a splatnost první splátky.")
    else:
        installment_total, valid_amounts, previous = 0, True, None
        for i, installment in enumerate(installments, 1):
            if not isinstance(installment, dict):
                errors.append(f"GATE § 641 OZ: splátka {i} musí být objekt s částkou a splatností.")
                valid_amounts = False
                continue
            amount = _money(installment.get("castka"))
            due = _date(installment.get("splatnost"))
            if amount is None or amount <= 0:
                errors.append(f"GATE § 2053 OZ: splátka {i} nemá kladnou částku ve formátu N.NNN,00.")
                valid_amounts = False
            else:
                installment_total += amount
            if due is None:
                errors.append(f"GATE § 641 OZ: chybí nebo je neplatná splatnost {'první splátky' if i == 1 else f'splátky {i}'}; použijte DD.MM.RRRR.")
            else:
                if previous is not None and due <= previous:
                    errors.append("GATE § 641 OZ: splátky musí být přísně chronologicky, bez shodných dat splatnosti.")
                previous = due
        if valid_amounts and total is not None and installment_total != total:
            errors.append("GATE § 2053 OZ: součet splátek se nerovná uznané částce (kontrola v haléřích).")
    if not _text(data.get("ucet")):
        errors.append("GATE § 2053 OZ: chybí účet pro plnění uznaného dluhu (ucet).")
    if data.get("vs") is not None and (not isinstance(data["vs"], str) or not re.fullmatch(r"[0-9]{0,10}", data["vs"])):
        errors.append("GATE § 2053 OZ: vs musí být řetězec nejvýše deseti číslic nebo null.")
    if not isinstance(data.get("rok"), str) or not re.fullmatch(r"[0-9]{4}", data["rok"]):
        errors.append("GATE § 2053 OZ: rok musí obsahovat čtyři číslice.")
    for key, default in (("ztrata_vyhody_splatek", True), ("urok_z_prodleni", True), ("notarsky_zapis", False)):
        if not isinstance(data.setdefault(key, default), bool):
            errors.append(f"GATE § 2053 OZ: {key} musí být boolean true nebo false.")
    if isinstance(installments, list) and len(installments) == 1:
        warnings.append("§ 639 OZ: při jediném plnění se použije lhůta od sjednané splatnosti; doložka ztráty výhody splátek se nevkládá, protože není další splátka.")
    if isinstance(installments, list) and isinstance(data.get("rok"), str) and re.fullmatch(r"[0-9]{4}", data["rok"]):
        if any(isinstance(s, dict) and _date(s.get("splatnost")) is not None and _date(s["splatnost"]).year < int(data["rok"]) for s in installments):
            warnings.append("§ 639 a § 641 OZ: splatnost předchází roku podpisu. Ověřte, zda jde o vědomě sjednané již splatné plnění, nebo chybu data, a dopady na prodlení a promlčení.")
    warnings.extend([
        "§ 2053 a § 561 odst. 1 OZ: uznání musí být písemné a podepsané Dlužníkem; Věřitel podepisuje dohodu o splátkách. Ověřte doručení uznání Věřiteli a oprávnění zástupců.",
        "§ 639 OZ: poučte Dlužníka o desetileté promlčecí lhůtě a jejím počátku dle sjednané splatnosti. Výjimku pro později dospělé úroky a opětující se plnění stanoví § 642 OZ.",
        "§ 2054 OZ: placení úroků může znamenat uznání příslušné jistiny; částečné plnění uznává zbytek jen podle okolností. Tyto účinky nenastávají u již promlčené pohledávky. Nenahrazujte jimi podpis tohoto písemného uznání.",
        "§ 1970 a § 1973 OZ: vzor nepředpokládá další úročení z titulu dosavadního prodlení po dobu řádného splácení. Ověřte vyčíslení dosavadního příslušenství, jeho rozsah a zamýšlené úročení. Vypnutí urok_z_prodleni pouze vynechá poučení, není prominutím zákonného nároku.",
    ])
    if isinstance(installments, list) and len(installments) > 1:
        warnings.append("§ 641 OZ: desetiletá promlčecí lhůta běží samostatně od splatnosti každé splátky; při zesplatnění od splatnosti nesplněné splátky, která zesplatnění vyvolala.")
    if data.get("ztrata_vyhody_splatek") is True and isinstance(installments, list) and len(installments) > 1:
        warnings.append("§ 1931 OZ: zesplatnění vyžaduje včasné uplatnění práva nejpozději do splatnosti nejblíže příští splátky. Vzor vyžaduje doručení písemné výzvy, ne automatické zesplatnění.")
    if data.get("notarsky_zapis") is True:
        warnings.append("PŘÍMÁ VYKONATELNOST: tento vzor nenahrazuje notářský ani exekutorský zápis se svolením k vykonatelnosti. Pro nové uznání použijte notářský zápis podle § 71a odst. 2 nebo § 71b zákona č. 358/1992 Sb. a § 40 odst. 1 písm. d) zákona č. 120/2001 Sb. Exekutorské zápisy zůstávají titulem pouze v historickém režimu čl. IV bodu 4 zákona č. 396/2012 Sb.; nejde o současnou alternativu nového notářského zápisu.")
    return errors, warnings

# Origin: GrowLead, ak-sladek v0.9 | Inspiration: https://www.zakonyprolidi.cz/cs/2012-89
