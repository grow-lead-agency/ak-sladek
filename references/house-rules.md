# House rules — formát dokumentů AK Sládek

> Zdroj pravdy pro formátování všech dokumentů kanceláře. Odvozeno z reálných vzorů
> + živý feedback JUDr. Sládka (session 2026-07-14, diktováno osobně).
> Implementováno v `skills/formatuj-smlouvu/scripts/format_docx.py` — při změně pravidla
> změň KÓD + tento soubor. Konzumují: formatuj-smlouvu, generuj-smlouvu (šablony), AI vrstva.

## Písmo a odstavce
- **Font: Tahoma 10,5 pt** — VŠE včetně čísel odrážek (sz=21 v definici číslování).
- **Řádkování: „Bez mezer"** (No Spacing) — space_after=0, space_before=0, line=1.0. Žádné velké mezery, zejména mezi řádky jmen stran.
- Tělo textu: blokové zarovnání (justify).

## Struktura dokumentu
- **Hlavní nadpis**: VELKÝM, centrovaně, bold + **prázdný řádek pod ním** (Sládek 14.7.).
- Právní hlavička: „(dále jen „X") uzavřená podle ustanovení § … mezi smluvními stranami:" — justify.
- **Bloky stran**: jméno/název + identifikace bold na 1. řádku; adresa a další řádky normal; prázdný řádek; „(dále jen „X")" s bold pojmem.
- **„a" mezi stranami: DOLEVA**, bold (Sládek 14.7. — ne na střed).
- **„v tomto znění:" — NA STŘED, BEZ boldu, vždy** (Sládek 14.7.).
- **Články**: římská číslice (I.) centrovaně bold; název článku na dalším řádku centrovaně bold.
- **Body**: skutečné Word číslování (decimal `%1.`, odsazení 360/360 twips, restart per článek). NIKDY čísla psaná v textu.

## Patička
- **Číslo stránky + název listiny** (Tahoma 10 pt), převzato z patičky kupní smlouvy kanceláře.
- Název listiny odpovídá dokumentu (např. „Plná moc", „Dohoda o narovnání"), nikdy nezůstává
  „Kupní smlouva" ze šablony. Formátovač i buildery vzorů ho nastavují automaticky (oprava 2026-10-16).

## Částky a lhůty
- **Částky: `N.NNN.NNN,00 Kč` — haléře VŽDY na dvě místa** (Sládek 14.7.). Formátovač normalizuje automaticky.
- Lhůty slovy + číslem: `deseti (10) pracovních dnů`.

## Podpisový blok
- **Dva zarovnané sloupce (tabulka bez ohraničení)** — podtržítko, jméno (bold), případný zástupce (jednatel), role — **přesně pod sebou** (Sládek 14.7.).
- Datumová linka: `V ________________ dne ________ RRRR`.

## Proces
- Formátovač NIKDY nemění právní text — jen vzhled a strukturu (výjimky vyjmenované v reportu).
- Každý nový Sládkův feedback: zapsat SEM + do kódu formátovače + přegenerovat šablony. Pravidlo platí od té chvíle pro všechny dokumenty automaticky.
