---
name: formatuj-smlouvu
description: Převede cizí nebo špatně naformátovaný právní dokument (Word/PDF/text) do jednotného formátu kanceláře — Tahoma 10,5, články římskými číslicemi centrovaně, skutečné Word číslování bodů, strukturované bloky stran, podpisové bloky. NEMĚNÍ text, jen vzhled a strukturu. Použij když uživatel dostane dokument od protistrany, z AI generátoru, nebo starý dokument v rozbitém formátu a chce ho "učesat" do formátu kanceláře.
argument-hint: "<dokument k přeformátování>"
---

# /formatuj-smlouvu — Jednotný formát kanceláře

**Důležité**: Tento skill mění POUZE formát a strukturu, nikdy právní text. Neposkytuje právní poradenství ve smyslu zákona č. 85/1996 Sb., o advokacii. Výstup je návrh ke kontrole advokátem.

## House rules (závazné)

Formát kanceláře je definován v [`references/house-rules.md`](../../references/house-rules.md) (root pluginu) — Tahoma 10,5 vč. čísel odrážek, „Bez mezer", částky s haléři na 2 místa, „v tomto znění:" střed bez boldu, „a" mezi stranami doleva, enter pod hlavním nadpisem, podpisy 2 zarovnané sloupce. Implementace v `scripts/format_docx.py`. Nový feedback advokáta → aktualizuj house-rules.md + kód, ne jednotlivý dokument.

## Princip: rebuild-and-restyle (ne patchování)

Rozbité Word dokumenty se NEopravují po kouskách — staré formátování se zahodí a obsah se znovu postaví na čistém formátovém nosiči kanceláře (`base/kancelar-base.docx`, odvozený z reálných vzorů). AI dokument rozparsuje na strukturovaný model, deterministický skript ho vysází.

## Pracovní postup

### Krok 1 — Převzetí a diagnostika
Přijmi dokument (.docx, PDF, text). U .docx krátce diagnostikuj co je špatně (pro report):
falešné číslování psané v textu („1. 2. 3." v jednom odstavci), defaultní Word styly, mix fontů, strany slité do jedné věty, chybějící podpisové linky.

### Krok 2 — Parse na model dokumentu (AI krok)
Rozparsuj dokument na JSON model (struktura viz docstring `scripts/format_docx.py`):
- **titul** + **pravni_hlavicka** (věta „uzavřená podle ustanovení § …")
- **strany** — každá jako blok řádků + `(dále jen „X")`; jméno/název a definované pojmy označ `**bold**`
- **clanky** — číslo (I., II., …), název, body. Slité body „1. … 2. …" rozděl na položky pole. `cislovane: false` pro jednobodové články.
- **podpisy** — levá/pravá strana, role, případný zástupce (jednatel)

**ŽELEZNÉ PRAVIDLO: text bodů přepisuj DOSLOVNĚ.** Nic neopravuj, nevylepšuj, nedoplňuj — ani překlepy, ani právní vady. Jediné povolené úpravy: (a) spojka do hlavičky („mezi smluvními stranami:") při vytažení stran do bloků, (b) house-style datumová linka, (c) `**bold**` na částky a definované pojmy. Každou takovou úpravu vyjmenuj v reportu.

### Krok 3 — Render
```
python skills/formatuj-smlouvu/scripts/format_docx.py model.json vystup.docx
```
Vyžaduje `pip install python-docx`. Vysází: Tahoma 10,5, blokové zarovnání, články centrovaně bold (číslo + název na samostatných řádcích), **skutečné Word číslování** (decimal, restart per článek, odsazení 360/360), podpisový blok se sloupci.

### Krok 4 — Verifikace (povinná)
Po renderu ověř integritu: každá věta originálu musí být ve výstupu doslovně (viz kontrolní pattern — rozbij inline číslování, porovnej po větách). Chybějící věta = STOP, oprava modelu, nikdy neodevzdat děravý dokument.

### Krok 5 — Report
Vrať uživateli:
1. **Dokument** v novém formátu
2. **Co bylo změněno** (jen forma): rozbité číslování → skutečné, strany do bloků, fonty sjednoceny…
3. **Advisory poznámky (obsah NEMĚNIT, jen upozornit)** — co formátovači padlo do oka: chybějící obvyklá ustanovení proti vzorům kanceláře (prohlášení o exekucích/insolvenci, doložka o změnách dodatky, ověřené podpisy…), nekonzistence. Rozhodnutí je na advokátovi.

## Omezení v0.2
- Tabulky, obrázky a vícesloupcové layouty se nepřenáší (flag „vyžaduje ruční zpracování").
- Vnořené podúrovně číslování (a, b, c) zatím ne — bod s podvýčtem nech jako jeden odstavec a upozorni.
- PDF vstup: nejdřív extrahuj text lokálně, strukturu rekonstruuj a označ nejistá místa.

<!-- Origin: GrowLead sladek-pravo plugin (interní house style kanceláře JUDr. Sládka) | Vytvořeno: 2026-07-14 | Inspiration: interní house-rules.md + kancelar-base.docx vzory -->
