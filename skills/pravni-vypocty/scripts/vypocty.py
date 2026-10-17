#!/usr/bin/env python3
"""Právní výpočty pro ak-sladek (úrok z prodlení, lhůty, promlčení, poplatek, tarif).

Pouze standardní knihovna Pythonu 3.10+. Bez sítě. Sazby jsou data ve skriptu.
"""

from __future__ import annotations

import argparse
import calendar
import json
import sys
from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP
from typing import Any

# ---------------------------------------------------------------------------
# Stav k 2026-10-16
# Zdroje: NV 351/2013 Sb. (zakonyprolidi.cz/cs/2013-351),
# ČNB repo https://www.cnb.cz/cs/casto-kladene-dotazy/Jak-se-vyvijela-dvoutydenni-repo-sazba-CNB/,
# o. s. ř. § 57, OZ § 605-607 a § 629/636/638/639/641,
# zák. 245/2000 Sb., zák. 549/1991 Sb. položka 1 a 2,
# vyhl. 177/1996 Sb. § 7, § 8, § 11, § 13 odst. 4,
# zák. 235/2004 Sb. § 47 odst. 1 písm. a).
# ---------------------------------------------------------------------------

STAV_K = date(2026, 10, 16)

# (platná_od, repo v %). Tabulka od 2. 11. 2012 (sazba k 1. 1. 2014) po 19. 6. 2026.
REPO_ZMENY: list[tuple[date, Decimal]] = [
    (date(2012, 11, 2), Decimal("0.05")),
    (date(2017, 8, 4), Decimal("0.25")),
    (date(2017, 11, 3), Decimal("0.50")),
    (date(2018, 2, 2), Decimal("0.75")),
    (date(2018, 6, 28), Decimal("1.00")),
    (date(2018, 8, 3), Decimal("1.25")),
    (date(2018, 9, 27), Decimal("1.50")),
    (date(2018, 11, 2), Decimal("1.75")),
    (date(2019, 5, 3), Decimal("2.00")),
    (date(2020, 2, 7), Decimal("2.25")),
    (date(2020, 3, 17), Decimal("1.75")),
    (date(2020, 3, 27), Decimal("1.00")),
    (date(2020, 5, 11), Decimal("0.25")),
    (date(2021, 6, 24), Decimal("0.50")),
    (date(2021, 8, 6), Decimal("0.75")),
    (date(2021, 10, 1), Decimal("1.50")),
    (date(2021, 11, 5), Decimal("2.75")),
    (date(2021, 12, 23), Decimal("3.75")),
    (date(2022, 2, 4), Decimal("4.50")),
    (date(2022, 4, 1), Decimal("5.00")),
    (date(2022, 5, 6), Decimal("5.75")),
    (date(2022, 6, 23), Decimal("7.00")),
    (date(2023, 12, 22), Decimal("6.75")),
    (date(2024, 2, 9), Decimal("6.25")),
    (date(2024, 3, 21), Decimal("5.75")),
    (date(2024, 5, 3), Decimal("5.25")),
    (date(2024, 6, 28), Decimal("4.75")),
    (date(2024, 8, 2), Decimal("4.50")),
    (date(2024, 9, 26), Decimal("4.25")),
    (date(2024, 11, 8), Decimal("4.00")),
    (date(2025, 2, 7), Decimal("3.75")),
    (date(2025, 5, 9), Decimal("3.50")),
    (date(2026, 6, 19), Decimal("3.75")),
]

UROK_PRIRAZEK_PB = Decimal("8")
PAUSAL_PODNIKATELE = Decimal("1200")
DENIK = Decimal("365")
NV_351_UCINNOST = date(2014, 1, 1)

# Pevné svátky (měsíc, den) podle zák. 245/2000 Sb. § 1 a § 2. Velikonoce algoritmem.
SVATKY_PEVNE: tuple[tuple[int, int], ...] = (
    (1, 1),
    (5, 1),
    (5, 8),
    (7, 5),
    (7, 6),
    (9, 28),
    (10, 28),
    (11, 17),
    (12, 24),
    (12, 25),
    (12, 26),
)

# Soudní poplatek, položka 1 a 2 sazebníku zák. 549/1991 Sb.
POPLATEK_P1_PEVNA_DO = Decimal("20000")
POPLATEK_P1_PEVNA = Decimal("1000")
POPLATEK_P1_PCT = Decimal("0.05")
POPLATEK_P1_HORNI = Decimal("40000000")
POPLATEK_P1_CAST = Decimal("2000000")
POPLATEK_P1_PCT_NAD = Decimal("0.01")
POPLATEK_P1_STROP_ZAKLADU = Decimal("250000000")
POPLATEK_STROP = Decimal("2000000")  # § 6a odst. 7, neplatí u položky 1c

POPLATEK_EPR_A_DO = Decimal("10000")
POPLATEK_EPR_A = Decimal("400")
POPLATEK_EPR_B_DO = Decimal("20000")
POPLATEK_EPR_B = Decimal("800")
POPLATEK_EPR_PCT = Decimal("0.04")

# Advokátní tarif vyhl. 177/1996 Sb. § 7 a § 13 odst. 4
PAUSAL_UKON = Decimal("450")
DPH_SAZBA = Decimal("0.21")

# (horní mez včetně, nebo None = bez stropu, funkce sazby)
# Pásma § 7: implementace v sazba_ukon().

PROMLCENI_TYPY = ("obecna", "uznani", "skoda", "obohaceni")
JEDNOTKY = ("dny", "tydny", "mesice", "roky")


# ---------------------------------------------------------------------------
# Pomocné formátování a kalendář
# ---------------------------------------------------------------------------

def _kc(amount: Decimal) -> Decimal:
    return amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def format_kc(amount: Decimal) -> str:
    q = _kc(amount)
    sign = "-" if q < 0 else ""
    q = abs(q)
    whole, frac = f"{q:.2f}".split(".")
    groups: list[str] = []
    while whole:
        groups.append(whole[-3:])
        whole = whole[:-3]
    return f"{sign}{' '.join(reversed(groups))},{frac} Kč"


def format_pct(value: Decimal) -> str:
    q = value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    text = f"{q:.2f}".replace(".", ",")
    if text.endswith(",00"):
        text = text[:-3]
    elif text.endswith("0"):
        text = text[:-1]
    return f"{text} %"


def format_date(d: date) -> str:
    return f"{d.day}. {d.month}. {d.year}"


def parse_date(text: str) -> date:
    try:
        return date.fromisoformat(text)
    except ValueError as exc:
        raise SystemExit(f"Neplatné datum {text!r}, očekáván formát RRRR-MM-DD.") from exc


def parse_castka(text: str) -> Decimal:
    normalized = text.strip().replace(" ", "").replace(",", ".")
    try:
        value = Decimal(normalized)
    except Exception as exc:
        raise SystemExit(f"Neplatná částka {text!r}.") from exc
    if value <= 0:
        raise SystemExit("Částka musí být kladná.")
    return value


def easter_sunday(year: int) -> date:
    """Velikonoční neděle, anonymní gregoriánský algoritmus (Meeus/Jones/Butcher)."""
    a = year % 19
    b, c = divmod(year, 100)
    d, e = divmod(b, 4)
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = divmod(c, 4)
    el = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * el) // 451
    month = (h + el - 7 * m + 114) // 31
    day = ((h + el - 7 * m + 114) % 31) + 1
    return date(year, month, day)


def je_svatek(d: date) -> bool:
    if (d.month, d.day) in SVATKY_PEVNE:
        return True
    nedele = easter_sunday(d.year)
    return d in (nedele - timedelta(days=2), nedele + timedelta(days=1))


def je_pracovni_den(d: date) -> bool:
    return d.weekday() < 5 and not je_svatek(d)


def posun_na_pracovni(d: date) -> date:
    while not je_pracovni_den(d):
        d += timedelta(days=1)
    return d


def pridat_mesice(d: date, mesice: int) -> date:
    month_index = d.month - 1 + mesice
    year = d.year + month_index // 12
    month = month_index % 12 + 1
    last = calendar.monthrange(year, month)[1]
    return date(year, month, min(d.day, last))


def pridat_roky(d: date, roky: int) -> date:
    return pridat_mesice(d, roky * 12)


def nazev_dne(d: date) -> str:
    return ("pondělí", "úterý", "středa", "čtvrtek", "pátek", "sobota", "neděle")[d.weekday()]


def duvod_posunu(d: date) -> str:
    if d.weekday() == 5:
        return "sobotu"
    if d.weekday() == 6:
        return "neděli"
    if je_svatek(d):
        return "svátek"
    return "nepracovní den"


# ---------------------------------------------------------------------------
# Úrok z prodlení
# ---------------------------------------------------------------------------

def repo_k(d: date) -> Decimal:
    platna: Decimal | None = None
    for od, sazba in REPO_ZMENY:
        if od <= d:
            platna = sazba
        else:
            break
    if platna is None:
        raise SystemExit(
            f"Chybí repo sazba ČNB k {format_date(d)}. Tabulka ve skriptu začíná "
            f"{format_date(REPO_ZMENY[0][0])}."
        )
    return platna


def zacatek_pololeti(d: date) -> date:
    if d.month <= 6:
        return date(d.year, 1, 1)
    return date(d.year, 7, 1)


def sazba_uroku_z_prodleni(prvni_den: date) -> tuple[Decimal, Decimal, date]:
    """Vrátí (sazba v %, repo v %, první den pololetí)."""
    polo = zacatek_pololeti(prvni_den)
    repo = repo_k(polo)
    return repo + UROK_PRIRAZEK_PB, repo, polo


def dny_prodleni(splatnost: date, do: date) -> tuple[int, date]:
    prvni = splatnost + timedelta(days=1)
    if do < prvni:
        raise SystemExit(
            f"K datu {format_date(do)} prodlení ještě netrvalo "
            f"(první den prodlení je {format_date(prvni)})."
        )
    return (do - prvni).days + 1, prvni


def spocitej_urok(
    castka: Decimal,
    splatnost: date,
    do: date,
    podnikatele: bool,
) -> dict[str, Any]:
    dny, prvni = dny_prodleni(splatnost, do)
    sazba_pct, repo, polo = sazba_uroku_z_prodleni(prvni)
    urok = _kc(castka * (sazba_pct / Decimal("100")) * Decimal(dny) / DENIK)
    pausal = PAUSAL_PODNIKATELE if podnikatele else Decimal("0")
    prislusenstvi = _kc(urok + pausal)
    upozorneni = [
        "Sazba platí po celou dobu prodlení ve výši určené k prvnímu dni pololetí, "
        "v němž prodlení vzniklo (NV č. 351/2013 Sb. § 2 odst. 1).",
        "Výpočet je orientační (jistina × sazba × dny / 365, haléře ROUND_HALF_UP). "
        "Před podáním ověřte splatnost, dny a aktuální repo sazbu na cnb.cz.",
    ]
    if prvni < NV_351_UCINNOST:
        upozorneni.append(
            "Prodlení vzniklo před 1. 1. 2014. Výši tehdy určovalo nařízení vlády "
            "č. 142/1994 Sb. Tento výpočet podle NV 351/2013 Sb. nepoužívejte bez ověření."
        )
    if not podnikatele:
        upozorneni.append(
            "Paušál 1 200 Kč podle § 3 NV 351/2013 Sb. se připočítává jen u vzájemného "
            "závazku podnikatelů (nebo podnikatel a veřejný zadavatel). Zapněte --podnikatele, "
            "pokud náleží."
        )
    pololeti_label = f"{'1' if polo.month == 1 else '2'}. pololetí {polo.year}"
    return {
        "prikaz": "urok",
        "jistina": str(_kc(castka)),
        "splatnost": splatnost.isoformat(),
        "prvni_den_prodleni": prvni.isoformat(),
        "do": do.isoformat(),
        "dny_prodleni": dny,
        "pololeti": pololeti_label,
        "pololeti_od": polo.isoformat(),
        "repo_sazba_pct": str(repo),
        "sazba_pct": str(sazba_pct),
        "urok": str(urok),
        "pausal": str(_kc(pausal)),
        "pausal_nalezi": podnikatele,
        "celkem_prislusenstvi": str(prislusenstvi),
        "celkem_s_jistinou": str(_kc(castka + prislusenstvi)),
        "upozorneni": upozorneni,
        "stav_k": STAV_K.isoformat(),
    }


def text_urok(data: dict[str, Any]) -> str:
    pausal = Decimal(data["pausal"])
    if data["pausal_nalezi"]:
        pausal_radek = format_kc(pausal) + " (§ 3 NV 351/2013 Sb.)"
    else:
        pausal_radek = "nenáleží (chybí --podnikatele)"
    lines = [
        "Úrok z prodlení (orientační výpočet)",
        f"Stav sazeb k {format_date(STAV_K)}",
        "",
        f"Jistina:                 {format_kc(Decimal(data['jistina']))}",
        f"Splatnost:               {format_date(date.fromisoformat(data['splatnost']))}",
        f"První den prodlení:      {format_date(date.fromisoformat(data['prvni_den_prodleni']))}",
        f"Počítáno do:             {format_date(date.fromisoformat(data['do']))} (včetně)",
        f"Dny prodlení:            {data['dny_prodleni']}",
        f"Rozhodné pololetí:       {data['pololeti']} (repo k {format_date(date.fromisoformat(data['pololeti_od']))})",
        f"Repo sazba ČNB:          {format_pct(Decimal(data['repo_sazba_pct']))}",
        f"Sazba úroku z prodlení:  {format_pct(Decimal(data['sazba_pct']))} ročně (repo + 8 p. b.)",
        f"Úrok z prodlení:         {format_kc(Decimal(data['urok']))}",
        f"Paušál nákladů:          {pausal_radek}",
        f"Příslušenství celkem:    {format_kc(Decimal(data['celkem_prislusenstvi']))}",
        f"Celkem s jistinou:       {format_kc(Decimal(data['celkem_s_jistinou']))}",
        "",
        "Upozornění:",
    ]
    lines.extend(f"- {u}" for u in data["upozorneni"])
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Lhůty
# ---------------------------------------------------------------------------

def neposunuty_konec(od: date, delka: int, jednotka: str) -> date:
    if delka < 1:
        raise SystemExit("Délka lhůty musí být alespoň 1.")
    if jednotka == "dny":
        return od + timedelta(days=delka)
    if jednotka == "tydny":
        return od + timedelta(weeks=delka)
    if jednotka == "mesice":
        return pridat_mesice(od, delka)
    if jednotka == "roky":
        return pridat_roky(od, delka)
    raise SystemExit(f"Neznámá jednotka {jednotka!r}. Povoleno: {', '.join(JEDNOTKY)}.")


def konec_lhuty(od: date, delka: int, jednotka: str) -> tuple[date, date]:
    raw = neposunuty_konec(od, delka, jednotka)
    return posun_na_pracovni(raw), raw


def spocitej_lhutu(od: date, delka: int, jednotka: str, hmotnepravni: bool) -> dict[str, Any]:
    konec, raw = konec_lhuty(od, delka, jednotka)
    posunuto = konec != raw
    if hmotnepravni:
        upozorneni = [
            "Hmotněprávní lhůta: podání musí soudu poslední den DOJÍT, odeslání nestačí. "
            "Doporučeno podat nejpozději den předem.",
        ]
    else:
        upozorneni = [
            "Procesní lhůta: je zachována, je-li posledního dne učiněn úkon u soudu "
            "nebo podání odevzdáno orgánu, který má povinnost je doručit (§ 57 odst. 3 o. s. ř.).",
        ]
    upozorneni.append(
        "Výpočet je orientační podle § 57 o. s. ř. a svátků zák. č. 245/2000 Sb. "
        "Před podáním ověřte rozhodný počátek a doručení."
    )
    jednotka_label = {
        "dny": "dnů" if delka != 1 else "den",
        "tydny": "týdnů" if delka != 1 else "týden",
        "mesice": "měsíců" if delka != 1 else "měsíc",
        "roky": "let" if delka != 1 else "rok",
    }[jednotka]
    return {
        "prikaz": "lhuta",
        "od": od.isoformat(),
        "delka": delka,
        "jednotka": jednotka,
        "delka_label": f"{delka} {jednotka_label}",
        "neposunuty_konec": raw.isoformat(),
        "konec": konec.isoformat(),
        "posunuto": posunuto,
        "duvod_posunu": duvod_posunu(raw) if posunuto else None,
        "hmotnepravni": hmotnepravni,
        "upozorneni": upozorneni,
        "stav_k": STAV_K.isoformat(),
    }


def text_lhuta(data: dict[str, Any]) -> str:
    raw = date.fromisoformat(data["neposunuty_konec"])
    konec = date.fromisoformat(data["konec"])
    lines = [
        "Konec lhůty (orientační, § 57 o. s. ř.)",
        f"Stav svátků k {format_date(STAV_K)}",
        "",
        f"Počátek (rozhodná skutečnost): {format_date(date.fromisoformat(data['od']))} ({nazev_dne(date.fromisoformat(data['od']))})",
        f"Délka:                         {data['delka_label']}",
        f"Nepřesunutý konec:             {format_date(raw)} ({nazev_dne(raw)})",
        f"Konec lhůty:                   {format_date(konec)} ({nazev_dne(konec)})",
    ]
    if data["posunuto"]:
        lines.append(
            f"Posun: konec připadl na {data['duvod_posunu']}, "
            "posunuto na nejbližší pracovní den."
        )
    lines.append("")
    lines.append("Upozornění:")
    lines.extend(f"- {u}" for u in data["upozorneni"])
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Promlčení
# ---------------------------------------------------------------------------

def spocitej_promlceni(pocatek: date, typ: str) -> dict[str, Any]:
    if typ not in PROMLCENI_TYPY:
        raise SystemExit(f"Neznámý typ {typ!r}. Povoleno: {', '.join(PROMLCENI_TYPY)}.")
    raw_3 = pridat_roky(pocatek, 3)
    raw_10 = pridat_roky(pocatek, 10)
    raw_15 = pridat_roky(pocatek, 15)
    konec_3 = posun_na_pracovni(raw_3)
    konec_10 = posun_na_pracovni(raw_10)
    konec_15 = posun_na_pracovni(raw_15)
    if typ == "obecna":
        hlavni_raw, hlavni = raw_3, konec_3
        popis = (
            "Obecná promlčecí lhůta 3 roky (§ 629 odst. 1 OZ). "
            "Majetkové právo se promlčí nejpozději uplynutím 10 let ode dne dospělosti "
            "(§ 629 odst. 2 OZ), pokud zákon nestanoví jinou lhůtu."
        )
    elif typ == "uznani":
        hlavni_raw, hlavni = raw_10, konec_10
        popis = (
            "Uznání dluhu: 10 let ode dne uznání. Určí-li dlužník i dobu, do které splní, "
            "10 let od posledního dne té doby (§ 639 OZ). U splátek § 641 OZ."
        )
    elif typ == "skoda":
        hlavni_raw, hlavni = raw_3, konec_3
        popis = (
            "Náhrada škody: subjektivní 3 roky od vědomosti o škodě a škůdci (§ 619, § 620, § 629 OZ). "
            "Objektivně nejpozději 10 let od vzniku škody, při úmyslu 15 let. "
            "Újma na svobodě, životě nebo zdraví: objektivní lhůta se nepoužije (§ 636 OZ)."
        )
    else:
        hlavni_raw, hlavni = raw_3, konec_3
        popis = (
            "Bezdůvodné obohacení: subjektivní 3 roky od vědomosti (§ 619, § 621, § 629 OZ). "
            "Objektivně nejpozději 10 let od obohacení, při úmyslu 15 let (§ 638 OZ)."
        )
    upozorneni = [
        "Orientační výpočet. Skript neřeší stavění běhu lhůty, uplatnění práva u soudu, "
        "dílčí plnění, úmysl ani odlišný počátek objektivní lhůty.",
        "Zadané --pocatek se bere jako den rozhodné skutečnosti (§ 605 OZ). "
        "Před podáním ověřte počátek a aktuální znění OZ.",
        "Terminologie NOZ: nepoužívat spojení 'přerušení promlčení' (starý OZ).",
    ]
    return {
        "prikaz": "promlceni",
        "pocatek": pocatek.isoformat(),
        "typ": typ,
        "popis": popis,
        "konec": hlavni.isoformat(),
        "neposunuty_konec": hlavni_raw.isoformat(),
        "subjektivni_3r": konec_3.isoformat(),
        "objektivni_10l": konec_10.isoformat(),
        "objektivni_15l_umysl": konec_15.isoformat(),
        "posunuto": hlavni != hlavni_raw,
        "upozorneni": upozorneni,
        "stav_k": STAV_K.isoformat(),
    }


def text_promlceni(data: dict[str, Any]) -> str:
    pocatek = date.fromisoformat(data["pocatek"])
    konec = date.fromisoformat(data["konec"])
    lines = [
        "Orientační promlčení",
        f"Stav k {format_date(STAV_K)}",
        "",
        f"Typ:                 {data['typ']}",
        f"Počátek (zadaný):    {format_date(pocatek)} ({nazev_dne(pocatek)})",
        f"Orientační konec:    {format_date(konec)} ({nazev_dne(konec)})",
        "",
        data["popis"],
        "",
        f"Subjektivní 3 roky:           {format_date(date.fromisoformat(data['subjektivni_3r']))}",
        f"Objektivní 10 let:            {format_date(date.fromisoformat(data['objektivni_10l']))}",
        f"Objektivní 15 let (úmysl):    {format_date(date.fromisoformat(data['objektivni_15l_umysl']))}",
        "",
        "Upozornění:",
    ]
    lines.extend(f"- {u}" for u in data["upozorneni"])
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Soudní poplatek
# ---------------------------------------------------------------------------

def zaokrouhli_zaklad(castka: Decimal) -> Decimal:
    """§ 6 odst. 7 zák. 549/1991 Sb.: základ na celé desítky Kč nahoru."""
    return (castka / Decimal("10")).quantize(Decimal("1"), rounding=ROUND_UP) * Decimal("10")


def soudni_poplatek(castka: Decimal, epr: bool) -> tuple[Decimal, str, Decimal]:
    zaklad = zaokrouhli_zaklad(castka)
    if epr:
        if castka <= POPLATEK_EPR_A_DO:
            return POPLATEK_EPR_A, "položka 2 písm. a) sazebníku (EPR do 10 000 Kč včetně)", zaklad
        if castka <= POPLATEK_EPR_B_DO:
            return POPLATEK_EPR_B, "položka 2 písm. b) sazebníku (EPR nad 10 000 do 20 000 Kč včetně)", zaklad
        fee = _kc(zaklad * POPLATEK_EPR_PCT)
        if fee > POPLATEK_STROP:
            fee = POPLATEK_STROP
        return fee, "položka 2 písm. c) sazebníku (EPR nad 20 000 Kč, 4 %)", zaklad
    if castka <= POPLATEK_P1_PEVNA_DO:
        return POPLATEK_P1_PEVNA, "položka 1 bod 1 písm. a) sazebníku (do 20 000 Kč)", zaklad
    if castka <= POPLATEK_P1_HORNI:
        fee = _kc(zaklad * POPLATEK_P1_PCT)
        if fee > POPLATEK_STROP:
            fee = POPLATEK_STROP
        return fee, "položka 1 bod 1 písm. b) sazebníku (nad 20 000 do 40 000 000 Kč, 5 %)", zaklad
    zapocitat = min(zaklad, POPLATEK_P1_STROP_ZAKLADU)
    presah = max(zapocitat - POPLATEK_P1_HORNI, Decimal("0"))
    fee = _kc(POPLATEK_P1_CAST + presah * POPLATEK_P1_PCT_NAD)
    return (
        fee,
        "položka 1 bod 1 písm. c) sazebníku (nad 40 000 000 Kč, 2 000 000 Kč + 1 % z přesahu, "
        "nad 250 000 000 Kč se nezapočítává)",
        zaklad,
    )


def spocitej_poplatek(castka: Decimal, epr: bool) -> dict[str, Any]:
    fee, pasmo, zaklad = soudni_poplatek(castka, epr)
    upozorneni = [
        "Základ procentního poplatku se zaokrouhluje na celé desítky Kč nahoru (§ 6 odst. 7 zák. č. 549/1991 Sb.).",
        "Výpočet je orientační pro peněžité plnění v prvním stupni. Osvobození, odvolání a dovolání neřeší.",
    ]
    if epr:
        upozorneni.append(
            "EPR: poplatek podle položky 2 jen při podání přes určenou aplikaci. "
            "Jinak položka 1. Nevydá-li soud EPR, doměří se do položky 1."
        )
    return {
        "prikaz": "poplatek",
        "castka": str(_kc(castka)),
        "zaklad": str(zaklad),
        "epr": epr,
        "poplatek": str(_kc(fee)),
        "pasmo": pasmo,
        "upozorneni": upozorneni,
        "stav_k": STAV_K.isoformat(),
    }


def text_poplatek(data: dict[str, Any]) -> str:
    rezim = "elektronický platební rozkaz (položka 2)" if data["epr"] else "návrh na zahájení řízení (položka 1)"
    lines = [
        "Soudní poplatek (orientační výpočet)",
        f"Stav sazebníku k {format_date(STAV_K)}",
        "",
        f"Předmět (peněžité plnění): {format_kc(Decimal(data['castka']))}",
        f"Režim:                     {rezim}",
        f"Základ po zaokrouhlení:    {format_kc(Decimal(data['zaklad']))}",
        f"Pásmo:                     {data['pasmo']}",
        f"Poplatek:                  {format_kc(Decimal(data['poplatek']))}",
        "",
        "Upozornění:",
    ]
    lines.extend(f"- {u}" for u in data["upozorneni"])
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Advokátní tarif
# ---------------------------------------------------------------------------

def sazba_ukon(tarifni: Decimal) -> Decimal:
    """Mimosmluvní odměna za jeden úkon, vyhl. 177/1996 Sb. § 7."""
    if tarifni <= Decimal("500"):
        return Decimal("300")
    if tarifni <= Decimal("1000"):
        return Decimal("500")
    if tarifni <= Decimal("5000"):
        return Decimal("1000")
    if tarifni <= Decimal("10000"):
        return Decimal("1500")
    if tarifni <= Decimal("200000"):
        presah = tarifni - Decimal("10000")
        jednotek = (presah / Decimal("1000")).to_integral_value(rounding=ROUND_UP)
        return Decimal("1500") + Decimal("40") * jednotek
    if tarifni <= Decimal("10000000"):
        presah = tarifni - Decimal("200000")
        jednotek = (presah / Decimal("10000")).to_integral_value(rounding=ROUND_UP)
        return Decimal("9100") + Decimal("40") * jednotek
    presah = tarifni - Decimal("10000000")
    jednotek = (presah / Decimal("100000")).to_integral_value(rounding=ROUND_UP)
    return Decimal("48300") + Decimal("40") * jednotek


def spocitej_odmenu(tarifni: Decimal, ukony: int, dph: bool) -> dict[str, Any]:
    if ukony < 1:
        raise SystemExit("Počet úkonů musí být alespoň 1 (plná sazba podle § 7).")
    za_ukon = sazba_ukon(tarifni)
    odmena = za_ukon * ukony
    pausal = PAUSAL_UKON * ukony
    zaklad = odmena + pausal
    if dph:
        dph_castka = _kc(zaklad * DPH_SAZBA)
        celkem = _kc(zaklad + dph_castka)
    else:
        dph_castka = Decimal("0.00")
        celkem = zaklad
    upozorneni = [
        "Odměna podle § 7 vyhl. č. 177/1996 Sb. za úkon v plné sazbě. "
        "Poloviční úkony (§ 11 odst. 2) zadejte přepočtené na plné.",
        "Paušál 450 Kč na úkon (§ 13 odst. 4), není-li dohodnuto jinak.",
        "Tarifní hodnota u peněžitého plnění je jistina bez příslušenství, "
        "ledaže je příslušenství samostatným nárokem (§ 8).",
        "Výpočet je orientační pro náhradu nákladů řízení. Před podáním ověřte tarif a plátcovství DPH.",
    ]
    return {
        "prikaz": "odmena",
        "tarifni_hodnota": str(_kc(tarifni)),
        "ukony": ukony,
        "sazba_ukon": str(za_ukon),
        "odmena": str(odmena),
        "pausal_ukon": str(PAUSAL_UKON),
        "pausal": str(pausal),
        "zaklad": str(zaklad),
        "dph_sazba_pct": "21",
        "dph": str(dph_castka),
        "dph_zapnuto": dph,
        "celkem": str(celkem),
        "upozorneni": upozorneni,
        "stav_k": STAV_K.isoformat(),
    }


def text_odmena(data: dict[str, Any]) -> str:
    lines = [
        "Odměna advokáta podle tarifu (orientační výpočet)",
        f"Stav tarifu k {format_date(STAV_K)}",
        "",
        f"Tarifní hodnota:     {format_kc(Decimal(data['tarifni_hodnota']))}",
        f"Počet úkonů:         {data['ukony']} (plná sazba § 7)",
        f"Sazba za úkon:       {format_kc(Decimal(data['sazba_ukon']))}",
        f"Odměna celkem:       {format_kc(Decimal(data['odmena']))}",
        f"Paušál § 13 odst. 4: {format_kc(Decimal(data['pausal']))} ({format_kc(Decimal(data['pausal_ukon']))} × {data['ukony']})",
        f"Základ:              {format_kc(Decimal(data['zaklad']))}",
    ]
    if data["dph_zapnuto"]:
        lines.append(f"DPH 21 %:            {format_kc(Decimal(data['dph']))}")
    else:
        lines.append("DPH:                 nepočítáno (zapněte --dph u plátce)")
    lines.extend(
        [
            f"Celkem:              {format_kc(Decimal(data['celkem']))}",
            "",
            "Upozornění:",
        ]
    )
    lines.extend(f"- {u}" for u in data["upozorneni"])
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _emit(data: dict[str, Any], text: str, as_json: bool) -> None:
    if as_json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        print(text)


def build_parser() -> argparse.ArgumentParser:
    json_flag = argparse.ArgumentParser(add_help=False)
    json_flag.add_argument("--json", action="store_true", help="výstup JSON místo češtiny")
    parser = argparse.ArgumentParser(
        prog="vypocty.py",
        parents=[json_flag],
        description=(
            "Deterministické právní výpočty (úrok z prodlení, lhůta, promlčení, "
            "soudní poplatek, advokátní tarif). Sazby ve skriptu, stav k "
            f"{STAV_K.isoformat()}."
        ),
    )
    sub = parser.add_subparsers(dest="prikaz", required=True)

    p_urok = sub.add_parser("urok", parents=[json_flag], help="úrok z prodlení (NV 351/2013 Sb.)")
    p_urok.add_argument("--castka", required=True, help="jistina v Kč")
    p_urok.add_argument("--splatnost", required=True, help="datum splatnosti RRRR-MM-DD")
    p_urok.add_argument("--do", required=True, dest="do_", help="počítat do dne RRRR-MM-DD včetně")
    p_urok.add_argument(
        "--podnikatele",
        action="store_true",
        help="připočíst paušál 1 200 Kč podle § 3 (závazek mezi podnikateli)",
    )

    p_lhuta = sub.add_parser("lhuta", parents=[json_flag], help="konec lhůty podle § 57 o. s. ř.")
    p_lhuta.add_argument("--od", required=True, dest="od_", help="den rozhodné skutečnosti RRRR-MM-DD")
    p_lhuta.add_argument("--delka", required=True, type=int, help="délka lhůty (celé číslo)")
    p_lhuta.add_argument("--jednotka", required=True, choices=JEDNOTKY, help="dny, tydny, mesice, roky")
    p_lhuta.add_argument(
        "--hmotnepravni",
        action="store_true",
        help="upozornit, že podání musí soudu dojít (hmotněprávní lhůta)",
    )

    p_prom = sub.add_parser("promlceni", parents=[json_flag], help="orientační konec promlčecí lhůty")
    p_prom.add_argument("--pocatek", required=True, help="den rozhodné skutečnosti RRRR-MM-DD")
    p_prom.add_argument("--typ", default="obecna", choices=PROMLCENI_TYPY)

    p_pop = sub.add_parser("poplatek", parents=[json_flag], help="soudní poplatek z peněžitého plnění")
    p_pop.add_argument("--castka", required=True, help="předmět řízení v Kč")
    p_pop.add_argument("--epr", action="store_true", help="návrh na elektronický platební rozkaz")

    p_odm = sub.add_parser("odmena", parents=[json_flag], help="mimosmluvní odměna a paušál podle tarifu")
    p_odm.add_argument("--tarifni-hodnota", required=True, dest="tarifni_hodnota")
    p_odm.add_argument("--ukony", required=True, type=int, help="počet úkonů v plné sazbě")
    p_odm.add_argument(
        "--dph",
        action="store_true",
        help="připočíst DPH u plátce, základní sazba 21 procent",
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    as_json = bool(getattr(args, "json", False))
    if args.prikaz == "urok":
        data = spocitej_urok(
            parse_castka(args.castka),
            parse_date(args.splatnost),
            parse_date(args.do_),
            args.podnikatele,
        )
        _emit(data, text_urok(data), as_json)
    elif args.prikaz == "lhuta":
        data = spocitej_lhutu(parse_date(args.od_), args.delka, args.jednotka, args.hmotnepravni)
        _emit(data, text_lhuta(data), as_json)
    elif args.prikaz == "promlceni":
        data = spocitej_promlceni(parse_date(args.pocatek), args.typ)
        _emit(data, text_promlceni(data), as_json)
    elif args.prikaz == "poplatek":
        data = spocitej_poplatek(parse_castka(args.castka), args.epr)
        _emit(data, text_poplatek(data), as_json)
    elif args.prikaz == "odmena":
        data = spocitej_odmenu(parse_castka(args.tarifni_hodnota), args.ukony, args.dph)
        _emit(data, text_odmena(data), as_json)
    else:
        parser.error("Neznámý příkaz.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
