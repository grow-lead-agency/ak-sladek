---
name: nastaveni-kancelare
description: Vstupní nastavení pluginu — 15minutový řízený rozhovor, který z advokáta vytáhne playbook kanceláře (standardní pozice u klauzulí, eskalační pravidla, house style) a zapíše ho do legal.local.md + zkontroluje kancelar.json. Spusť PŘED prvním ostrým použitím ostatních skillů, při onboardingu nového kolegy, nebo když advokát řekne "nastav si moji kancelář" / "výstupy jsou moc generické".
argument-hint: "(bez argumentů — interview)"
---

# /nastaveni-kancelare — Cold-start interview

> Anthropic pattern: *„Přeskočení setupu je nejčastější důvod, proč skill produkuje generický výstup."*
> Bez playbooku revidují skilly proti obecným standardům — s playbookem proti VAŠIM pozicím.

## Co uděláš (AI)

Veď řízený rozhovor (max 15 min, po blocích, netahej vše najednou). Odpovědi průběžně zapisuj. Na konci vytvoř/aktualizuj **`legal.local.md`** (podle `legal.local.example.md` v rootu pluginu) a zkontroluj **`config/kancelar.json`**.

### Blok 1 — Kancelář a defaults (ověř kancelar.json)
- Sedí konstanty? (advokát, ev. č. ČAK, IČO, sídlo, účet úschovy, banka)
- Výchozí lhůty (úhrada, výplata úschovy, předání) — nechat, nebo upravit?
- Kolik stejnopisů standardně u KS / SÚ / ostatních?

### Blok 2 — Playbook pozic (pro revize-smlouvy, triage-nda…)
Pro každou oblast: **standardní pozice → přijatelný rozsah → eskalace** (stačí realitní core):
- Limit odpovědnosti, smluvní pokuty (výše, moderace)
- Úschovní podmínky: výplatní podmínky z LV (co musí/nesmí být v části C a D), lhůty vrácení
- Lhůty: složení kupní ceny, předání nemovitosti, podání na katastr
- NDA: vzájemnost, doba trvání, co je ČERVENÁ
- Rozhodné právo/sudiště preference

### Blok 3 — Eskalační triggery
Co VŽDY eskalovat (návrhy: spor > X Kč, cizinecký prvek, insolvence protistrany, nestandardní úschova, více spoluvlastníků, jednání za s.r.o. „dva jednatelé společně")?

### Blok 4 — House style a komunikace
- Formát dokumentů: potvrdit house rules (`references/house-rules.md`) — něco změnit?
- Tón klientské komunikace (formální/přátelský), podpis e-mailů
- Šablonové odpovědi, které kancelář používá často (→ pravni-odpoved)

### Blok 5 — Vzory a priority
- Které dokumenty píše nejčastěji? (fronta pro nové vzory generátoru — plná moc, předžalobní výzva, uznání dluhu, narovnání…)
- Kde drží vzory (OneDrive?) — pro budoucí napojení

## Výstup
1. **`legal.local.md`** vyplněný odpověďmi (struktura dle example).
2. Změny v `config/kancelar.json` — vypiš je advokátovi k potvrzení PŘED zápisem.
3. Shrnutí: co je nastaveno + co zbývá (nezodpovězené bloky → příště).
4. Připomeň: playbook je živý — „řekněte kdykoli *změň pravidlo X* a zapíšu to".

**Neptej se na vše najednou** — bloky po jednom, advokát může kdykoli říct „zbytek přeskočíme".

<!-- Origin: Anthropic claude-for-legal cold-start-interview pattern (github.com/anthropics/claude-for-legal) | Adaptace: 2026-07-14 pro AK Sládek (realitní právo, úschovy) -->
