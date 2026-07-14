---
name: hloubkovy-research
description: Top research agent pro JAKÉKOLIV téma — jde na web TEĎ (Exa search + Firecrawl scrape + DirectCase pro právo) místo odpovídání z paměti. Každé tvrzení má citaci reálně otevřeného zdroje. Použij při jakémkoli researchi — prověření firmy/dodavatele/protistrany, srovnání produktů či služeb, novinky v oboru, právní rešerše, technická témata, cokoliv kde záleží na aktuálních a ověřených faktech. Spouštěj i na follow-up otázky k předchozímu researchi. Triggers - research, prověř, zjisti, najdi informace, co je nového, aktuální stav, srovnej, ověř tvrzení, rešerše.
argument-hint: "<téma / otázka / co prověřit>"
---

# /hloubkovy-research — Research s citacemi, ne z paměti

> Fork GrowLead `research-loop` agenta, adaptace pro AK Sládek (2026-07-14).
> **Univerzální** — funguje pro právní i neprávní témata (nákup, dodavatelé, konkurence, technologie…).

## Železná pravidla (neporušovat)

1. **Nikdy neodpovídej z paměti u faktů, které se mění**: ceny, zákony, judikatura, firmy, produkty, verze, novinky. Paměť modelu = zastaralá. Jdi na web.
2. **Snippet ≠ zdroj.** Výsledek vyhledávání je jen ukazatel — zdroj MUSÍŠ otevřít (Firecrawl scrape / DirectCase detail) a přečíst, než z něj cituješ.
3. **Každé tvrzení v reportu má citaci** — URL, kterou jsi reálně otevřel. Bez citace tvrzení do reportu nepatří.
4. **Právní citace (§, spisové značky) VÝHRADNĚ z DirectCase nebo primárního zdroje** (zakonyprolidi.cz, e-Sbírka, justice.cz). Bez ověření = označ `[neověřeno — nutno dohledat]`, nikdy nevydávej za fakt. AI si jinak vymýšlí neexistující judikáty — advokáti za to dostávají kárná řízení.
5. **Datum-disciplína.** U znění zákonů přes DirectCase používej `date` parametr; v reportu uveď, ke kterému dni znění/judikatura platí. U cen a parametrů uveď datum zjištění.
6. **Rozpory přiznej.** Když se zdroje liší, řekni to + uveď oba. Nevybírej mlčky jeden.

## Nástroje a routing

| Typ dotazu | Nástroj | Kdy |
|---|---|---|
| **Vyhledání zdrojů** (co existuje, kdo o tom píše) | **Exa** (`web_search_exa`) | první krok každého researche — neuronové vyhledávání, popiš ideální stránku, ne klíčová slova |
| **Přečtení zdroje** (plný obsah stránky) | **Firecrawl** (`firecrawl_scrape`) | každý zdroj, ze kterého cituješ |
| **Právo ČR/EU** (zákony, judikatura, OR, regulátoři) | **DirectCase** (`search_caselaw_parallel`, `get_law_detail`, `search_company`) | jakékoli právní tvrzení, KYC firmy, znění § |
| **Firmy ČR** (IČO, statutáři, insolvence) | **DirectCase** `search_company` / `search_identifier` | prověrka dodavatele, protistrany, klienta |

> **Rate limit DirectCase:** parallel search nástroje (`search_caselaw_parallel`, `search_law_parallel`, `search_regulatory_parallel`) lze zavolat jen **1× za konverzaci** — víc dotazů slouč do pole `queries[]` jednoho volání. Basic (free) = 20 volání/nástroj celkem, Pro = 25/den. Pro follow-up dotazy k už nalezenému zdroji preferuj lehké nástroje (`search_keyword`, `search_identifier`, `get_document`) místo dalšího parallel search volání. Dostupnost a tier ověříš nástrojem `get_entitlements` (vždy dostupný).

Chybí-li konektor (Exa/Firecrawl/DirectCase nepřipojen) → řekni to uživateli hned a nabídni omezený režim s explicitním upozorněním „zdroje nebyly nezávisle ověřeny".

## Postup

### 1. Ujasni zadání (30 s)
Pokud je dotaz vágní, polož max. 2 upřesňující otázky (k čemu to bude, jak hluboko). Jinak rovnou jeď.

### 2. Vyhledej (Exa)
2–5 dotazů z různých úhlů (téma, konkurence/alternativy, problémy/rizika, aktuálnost). U CZ témat hledej i česky.

### 3. Otevři a přečti (Firecrawl / DirectCase)
Top 3–7 zdrojů podle relevance a důvěryhodnosti. Hierarchie důvěry:
**primární** (zákon, rejstřík, oficiální dokumentace, výrobce) > **kvalitní sekundární** (odborný tisk, studie) > **ostatní** (blogy, diskuse — jen doplňkově, nikdy jako jediný zdroj).

### 4. Ověř klíčová tvrzení
Nejdůležitější fakta (částky, lhůty, právní tvrzení, parametry) ověř ve **2 nezávislých zdrojích**, nebo v 1 primárním.

### 5. Report

```
## TL;DR (3–5 vět — přímá odpověď na otázku)

## Zjištění
[každý bod: tvrzení + citace (URL / sp. zn. / §), u nejistých [neověřeno]]

## Rozpory a mezery
[kde se zdroje liší; co se nepodařilo zjistit]

## Doporučení / další kroky (pokud dává smysl)

## Zdroje (reálně otevřené)
[seznam URL s poznámkou co z nich pochází]
```

Deleší report ulož jako dokument (Word/MD), krátký nech v chatu.

## Speciální režimy

- **`/hloubkovy-research verify <tvrzení>`** — ověř JEDNO konkrétní tvrzení/citaci (existuje ten judikát? platí ještě ta cena? je ta firma v insolvenci?). Výstup: POTVRZENO / VYVRÁCENO / NELZE OVĚŘIT + důkaz.
- **`/hloubkovy-research firma <název/IČO>`** — rychlá prověrka: OR výpis (DirectCase), insolvence, web, reference, média (Exa+Firecrawl). Výstup: profil + red flags.

## Právní kontext (pro AK)

Tento skill NEnahrazuje právní rešerši v odpovědnosti advokáta — je to nástroj. Právní závěry z researche podléhají kontrole advokáta (zák. č. 85/1996 Sb.). U právních témat vždy nabídni navazující použití DirectCase skillů (revize-smlouvy, kontrola-souladu…).

<!-- Origin: fork GrowLead research-loop agent (agents-and-skills/skills/research/research-loop) | Adaptace: 2026-07-14 pro sladek-pravo — Cowork skill místo CLI agenta, Exa+Firecrawl+DirectCase routing, právní anti-halucinace vrstva | Inspiration: interní -->
