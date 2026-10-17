"""Hard gates dohody o narovnání, včetně podmíněných peněžitých plnění."""
import re
from datetime import datetime


def _text(value):
    return isinstance(value, str) and bool(value.strip())


def _positive_money(value):
    if not isinstance(value, str) or not re.fullmatch(r"(?:0|[1-9][0-9]{0,2}(?:\.[0-9]{3})*),[0-9]{2}", value):
        return False
    return int(value.replace(".", "").replace(",", "")) > 0


def _date(value):
    if not isinstance(value, str) or not re.fullmatch(r"[0-9]{2}\.[0-9]{2}\.[0-9]{4}", value):
        return False
    try:
        datetime.strptime(value, "%d.%m.%Y")
        return True
    except ValueError:
        return False


def gate(data):
    errors, warnings = [], []
    if not isinstance(data, dict):
        return ["GATE § 1903 OZ: data musí být objekt."], []
    for key in ("strana1", "strana2"):
        party = data.get(key)
        if not isinstance(party, dict):
            errors.append(f"GATE § 1903 OZ: chybí řádná identifikace strany {key}.")
            continue
        for field in ("radek1", "radek2", "podpis"):
            if not _text(party.get(field)):
                errors.append(f"GATE § 1903 OZ: chybí {key}.{field}.")
        if party.get("typ") not in ("FO", "PO"):
            errors.append(f"GATE § 1903 OZ: {key}.typ musí být FO nebo PO.")
        for field in ("radek3", "radek4", "radek5", "podpis_zastupce"):
            if party.get(field) is not None and not isinstance(party[field], str):
                errors.append(f"GATE § 1903 OZ: {key}.{field} musí být text nebo null.")
        if party.get("typ") == "PO" and not _text(party.get("podpis_zastupce")):
            errors.append(f"GATE § 1903 OZ: u PO chybí {key}.podpis_zastupce; ověřte oprávnění jednat.")
    rights = data.get("sporna_prava")
    if not isinstance(rights, list) or not rights or any(not _text(x) for x in rights):
        errors.append("GATE § 1903 odst. 1 OZ: chybí určitý popis alespoň jednoho sporného či pochybného práva; sporna_prava musí být neprázdný seznam textů.")
    for key in ("ustupky_strana1", "ustupky_strana2", "rozsah_narovnani"):
        if not _text(data.get(key)):
            errors.append(f"GATE § 1903 OZ: chybí {key}; doplňte ústupky a přesný rozsah nahrazovaných práv.")
    obligations = data.get("plneni")
    if not isinstance(obligations, list) or not obligations:
        errors.append("GATE § 1903 OZ: chybí nové uspořádání práv a povinností (plneni).")
    else:
        for i, item in enumerate(obligations, 1):
            if not isinstance(item, dict):
                errors.append(f"GATE § 1903 OZ: plnění {i} musí být objekt.")
                continue
            if item.get("typ") not in ("penezite", "nepenezite"):
                errors.append(f"GATE § 1903 OZ: plnění {i} má neplatný typ.")
            if item.get("povinna_strana") not in ("strana1", "strana2"):
                errors.append(f"GATE § 1903 OZ: u plnění {i} určete povinnou stranu (strana1 nebo strana2).")
            if not _text(item.get("popis")):
                errors.append(f"GATE § 1903 OZ: plnění {i} nemá popis nového uspořádání.")
            if not _date(item.get("splatnost")):
                errors.append(f"GATE § 1903 OZ: plnění {i} nemá platnou splatnost či termín ve formátu DD.MM.RRRR.")
            if item.get("typ") == "penezite":
                if not _positive_money(item.get("castka")):
                    errors.append(f"GATE § 1903 OZ: peněžité plnění {i} nemá kladnou částku ve formátu N.NNN,00.")
                if not _text(item.get("ucet")):
                    errors.append(f"GATE § 1903 OZ: peněžité plnění {i} nemá účet příjemce.")
            if item.get("typ") == "nepenezite" and not _text(item.get("zpusob")):
                errors.append(f"GATE § 1903 OZ: nepeněžité plnění {i} nemá místo a způsob splnění (zpusob).")
            if item.get("vs") is not None and (not isinstance(item["vs"], str) or not re.fullmatch(r"[0-9]{0,10}", item["vs"])):
                errors.append(f"GATE § 1903 OZ: plnění {i} má neplatný vs; nejvýše deset číslic jako text nebo null.")
    for key in ("konecne_vyporadani", "prevod_nemovitosti"):
        if not isinstance(data.setdefault(key, False), bool):
            errors.append(f"GATE § 1903 OZ: {key} musí být boolean true nebo false.")
    if data.get("konecne_vyporadani") is True and not _text(data.get("rozsah_vyporadani")):
        errors.append("GATE § 1905 OZ: konečné vypořádání vyžaduje výslovný rozsah (rozsah_vyporadani).")
    if data.get("rozsah_vyporadani") is not None and not isinstance(data["rozsah_vyporadani"], str):
        errors.append("GATE § 1905 OZ: rozsah_vyporadani musí být text nebo null.")
    if not isinstance(data.get("rok"), str) or not re.fullmatch(r"[0-9]{4}", data["rok"]):
        errors.append("GATE § 1906 OZ: rok musí obsahovat čtyři číslice.")
    if isinstance(obligations, list) and isinstance(data.get("rok"), str) and re.fullmatch(r"[0-9]{4}", data["rok"]):
        if any(isinstance(p, dict) and _date(p.get("splatnost")) and int(p["splatnost"][-4:]) < int(data["rok"]) for p in obligations):
            warnings.append("§ 1903 OZ: termín nového plnění předchází roku podpisu. Před podpisem ověřte zamýšlenou splatnost a případné prodlení.")
    warnings.extend([
        "§ 1903 odst. 2 OZ: narovnání nelze odporovat pouze pro nepoměr vzájemného plnění. § 1904 OZ: omyl ve sporné či pochybné otázce nevadí, vyjma omylu vyvolaného lstí; při dobré víře nevadí ani později zjištěná neexistence pohledávky. Jiné důvody napadení tím nejsou obecně vyloučeny.",
        "§ 1905 OZ: konečné vypořádání nepokrývá vyloučená práva ani práva, která strany zřejmě nemohly mít na mysli. Ověřte soulad rozsahu narovnání, ústupků a nového plnění.",
        "§ 1906 a § 561 odst. 1 OZ: písemná forma je povinná, byl-li původní závazek písemný nebo jde-li o již promlčené právo. Tento vzor podepisují obě strany; ověřte oprávnění zástupců.",
        "§ 1903 a § 1907 OZ: zkontrolujte okamžik nahrazení původních práv, návaznost zajištění a postavení třetích osob. Posuďte následky neplnění a případného odstoupení od narovnání.",
    ])
    if data.get("prevod_nemovitosti") is True:
        warnings.append("ESKALACE ADVOKÁTOVI: převod nemovitosti zapsané v katastru vyžaduje vklad (§ 1903 odst. 1 a § 1105 OZ, § 11 zákona č. 256/2013 Sb.), písemnou listinu a projevy stran na téže listině (§ 560 a § 561 odst. 2 OZ). Zajistěte úředně ověřené podpisy; § 7 odst. 2 zákona č. 256/2013 Sb. připouští také jiné prokázání pravosti. Obecný vzor není hotovou vkladovou listinou: advokát musí doplnit přesnou identifikaci nemovitosti a celý převodní mechanismus před podpisem či podáním.")
    return errors, warnings

# Origin: GrowLead, ak-sladek v0.9 | Inspiration: https://www.zakonyprolidi.cz/cs/2012-89
