---
name: pravni-vypocty
description: Deterministické právní výpočty skriptem, nikdy z hlavy modelu. Úrok z prodlení, výpočet lhůty, konec lhůty, promlčení, soudní poplatek, advokátní tarif, odměna advokáta, náklady řízení. Použij když je potřeba spočítat dny prodlení a sazbu úroku, konec procesní nebo hmotněprávní lhůty, orientační promlčení, soudní poplatek z peněžitého plnění včetně EPR, nebo mimosmluvní odměnu a režijní paušál.
argument-hint: "urok|lhuta|promlceni|poplatek|odmena + parametry"
---

# /pravni-vypocty: Právní výpočty skriptem

**Důležité**: Výstup je orientační podklad ke kontrole advokátem (zák. č. 85/1996 Sb.). Nepředávej ho klientovi ani do podání bez ověření. Sazby ve skriptu mají razítko data, před podáním je porovnej s primárním zdrojem.

## Železné pravidlo

**Čísla nikdy nepočítej z hlavy ani z paměti modelu.** Vždy spusť `scripts/vypocty.py`. Model smí jen sestavit příkaz z faktů uživatele, spustit skript a přečíst výstup. Halucinovaná sazba, špatné pololetí nebo posun lhůty ze svátku je kárné riziko.

Sazby a paragrafy: `references/sazby.md`. URL zdrojů: `references/sources.md`. Před podáním projdi [`references/kontroly-podani.md`](../../references/kontroly-podani.md).

## Pracovní postup

1. Zjisti, co se počítá (úrok, lhůta, promlčení, poplatek, odměna). Chybí-li datum nebo částka, doptaj se. Nic nedoplňuj odhadem.
2. Sestav příkaz níže. Datumy `RRRR-MM-DD`, částky v Kč.
3. Spusť skript (Python 3.10+, jen standardní knihovna, bez sítě):
   ```
   python skills/pravni-vypocty/scripts/vypocty.py <prikaz> [parametry]
   ```
   Volitelně `--json` na konci (stejné údaje strojově).
4. Uživateli vrať výstup skriptu plus upozornění ze skriptu. Nesnaž se čísla „vylepšit".
5. U podání připoj tabulku z `kontroly-podani.md`.

## Příkazy

### Úrok z prodlení

```
python skills/pravni-vypocty/scripts/vypocty.py urok --castka 85000 --splatnost 2026-03-31 --do 2026-10-16
python skills/pravni-vypocty/scripts/vypocty.py urok --castka 85000 --splatnost 2026-03-31 --do 2026-10-16 --podnikatele
```

Prodlení začíná dnem po splatnosti. Sazba = repo ČNB k 1. dni pololetí vzniku prodlení + 8 p. b. a platí po celou dobu prodlení (NV č. 351/2013 Sb. § 2). `--podnikatele` připočte paušál 1 200 Kč podle § 3 (jen kde náleží). `--do` se počítá včetně.

### Lhůta / konec lhůty

```
python skills/pravni-vypocty/scripts/vypocty.py lhuta --od 2026-10-16 --delka 15 --jednotka dny
python skills/pravni-vypocty/scripts/vypocty.py lhuta --od 2026-10-16 --delka 15 --jednotka dny --hmotnepravni
```

`--jednotka` je `dny`, `tydny`, `mesice` nebo `roky`. Konec podle § 57 o. s. ř. (den rozhodné skutečnosti se do dnů nepočítá, u týdnů/měsíců/let stejné číslo dne, posun ze soboty, neděle a svátku). `--hmotnepravni`: podání musí soudu poslední den dojít, odeslání nestačí.

### Promlčení

```
python skills/pravni-vypocty/scripts/vypocty.py promlceni --pocatek 2026-01-10
python skills/pravni-vypocty/scripts/vypocty.py promlceni --pocatek 2026-01-10 --typ uznani
```

`--typ`: `obecna` (výchozí), `uznani`, `skoda`, `obohaceni`. Jen orientační konec podle OZ § 629, § 636, § 638, § 639, § 641. Stavění běhu skript neřeší.

### Soudní poplatek

```
python skills/pravni-vypocty/scripts/vypocty.py poplatek --castka 85000
python skills/pravni-vypocty/scripts/vypocty.py poplatek --castka 85000 --epr
```

Položka 1 sazebníku zák. č. 549/1991 Sb. (peněžité plnění). `--epr` položka 2 (elektronický platební rozkaz, nižší sazba jen při podání přes určenou aplikaci).

### Odměna advokáta / náklady řízení

```
python skills/pravni-vypocty/scripts/vypocty.py odmena --tarifni-hodnota 85000 --ukony 3
python skills/pravni-vypocty/scripts/vypocty.py odmena --tarifni-hodnota 85000 --ukony 3 --dph
```

Sazba za úkon § 7, paušál 450 Kč § 13 odst. 4, `--dph` základní sazba 21 %. `--ukony` je počet úkonů v plné sazbě (§ 11 odst. 1).

## Jak číst výstup

- Částky v Kč s haléři, data česky.
- Blok „Upozornění" patří do odpovědi advokátovi, ne do textu podání.
- `--json` má stejná pole (`urok`, `konec`, `poplatek`, `celkem`, `upozorneni`, `stav_k`).
- `stav_k` je datum, ke kterému skript drží sazby. Nesedí-li se dneškem o víc než pár týdnů, zkontroluj ČNB a zakonyprolidi.cz podle `references/sazby.md` (sekce Jak aktualizovat).

## Omezení

- Orientační aritmetika, ne právní posouzení. Rozhodný počátek, stavění lhůty, osvobození od poplatku, poloviční úkony a smluvní odměna skript neřeší.
- Sazby jsou snapshot (stav k datu ve skriptu). Před podáním ověř repo sazbu, sazebník poplatků, tarif a svátky.
- Úrok z výživného nezletilého (§ 2 odst. 2 NV 351/2013 Sb.) skript nepočítá.
- Velikonoce bere algoritmem, pevné svátky ze zák. č. 245/2000 Sb. Významné dny jsou dny pracovní.

<!-- Origin: GrowLead ak-sladek | Vytvořeno: 2026-10-16 | Inspiration: https://www.zakonyprolidi.cz/cs/2013-351, https://www.cnb.cz/cs/casto-kladene-dotazy/Jak-se-vyvijela-dvoutydenni-repo-sazba-CNB/, https://www.zakonyprolidi.cz/cs/1963-99, https://www.zakonyprolidi.cz/cs/1991-549, https://www.zakonyprolidi.cz/cs/1996-177, https://www.zakonyprolidi.cz/cs/2000-245 -->
