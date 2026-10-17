# Sazby a parametry právních výpočtů

Stav k 2026-10-16. Každá hodnota níže pochází z primárního zdroje (URL). Před podáním ověř aktuální znění.

Skript `scripts/vypocty.py` drží stejná data ve vlastním bloku. Při aktualizaci změň obojí a spusť testy.

## 1. Úrok z prodlení

Předpis: nařízení vlády č. 351/2013 Sb., aktuální znění 1. 1. 2026 (verze 6).
URL: https://www.zakonyprolidi.cz/cs/2013-351

### § 2 výše sazby

Výše úroku z prodlení odpovídá ročně výši repo sazby ČNB pro první den kalendářního pololetí, v němž došlo k prodlení, zvýšené o 8 procentních bodů.

Sazba se určí jednou, k okamžiku vzniku prodlení, a platí po celou dobu prodlení (nemění se s pozdějšími změnami repo sazby).

Prodlení vzniká dnem následujícím po splatnosti.

Pololetí: 1. 1. až 30. 6., 1. 7. až 31. 12. Rozhodný je první den toho pololetí, do kterého spadá první den prodlení.

Zvláštní sazba u výživného pro nezletilé dítě (§ 2 odst. 2) skript nepočítá.

### § 3 paušál nákladů 1 200 Kč

Minimální výše nákladů spojených s uplatněním každé pohledávky činí 1 200 Kč, jde-li o vzájemný závazek podnikatelů, nebo o závazek mezi podnikatelem a veřejným zadavatelem podle zákona o veřejných zakázkách, jehož obsahem je dodání zboží nebo poskytnutí služby za úplatu veřejnému zadavateli.

Skript paušál připočte jen s příznakem `--podnikatele`.

### Repo sazba ČNB (dvoutýdenní)

Zdroj celé tabulky: https://www.cnb.cz/cs/casto-kladene-dotazy/Jak-se-vyvijela-dvoutydenni-repo-sazba-CNB/
Soubor ke stažení: https://www.cnb.cz/cs/casto-kladene-dotazy/.galleries/vyvoj_repo_historie.txt

Změny od 1. 1. 2014 (k 1. 1. 2014 platila sazba 0,05 % od 2. 11. 2012):

| Platná od | Repo % |
| --- | --- |
| 2. 11. 2012 | 0,05 |
| 4. 8. 2017 | 0,25 |
| 3. 11. 2017 | 0,50 |
| 2. 2. 2018 | 0,75 |
| 28. 6. 2018 | 1,00 |
| 3. 8. 2018 | 1,25 |
| 27. 9. 2018 | 1,50 |
| 2. 11. 2018 | 1,75 |
| 3. 5. 2019 | 2,00 |
| 7. 2. 2020 | 2,25 |
| 17. 3. 2020 | 1,75 |
| 27. 3. 2020 | 1,00 |
| 11. 5. 2020 | 0,25 |
| 24. 6. 2021 | 0,50 |
| 6. 8. 2021 | 0,75 |
| 1. 10. 2021 | 1,50 |
| 5. 11. 2021 | 2,75 |
| 23. 12. 2021 | 3,75 |
| 4. 2. 2022 | 4,50 |
| 1. 4. 2022 | 5,00 |
| 6. 5. 2022 | 5,75 |
| 23. 6. 2022 | 7,00 |
| 22. 12. 2023 | 6,75 |
| 9. 2. 2024 | 6,25 |
| 21. 3. 2024 | 5,75 |
| 3. 5. 2024 | 5,25 |
| 28. 6. 2024 | 4,75 |
| 2. 8. 2024 | 4,50 |
| 26. 9. 2024 | 4,25 |
| 8. 11. 2024 | 4,00 |
| 7. 2. 2025 | 3,75 |
| 9. 5. 2025 | 3,50 |
| 19. 6. 2026 | 3,75 |

Příklady rozhodné sazby úroku z prodlení (repo k 1. dni pololetí + 8 p. b.):

| Pololetí | Repo k 1. dni | Úrok z prodlení |
| --- | --- | --- |
| 2. pol. 2024 | 4,75 % (28. 6. 2024) | 12,75 % |
| 1. pol. 2025 | 4,00 % (8. 11. 2024) | 12,00 % |
| 2. pol. 2025 | 3,50 % (9. 5. 2025) | 11,50 % |
| 1. pol. 2026 | 3,50 % (9. 5. 2025) | 11,50 % |
| 2. pol. 2026 | 3,75 % (19. 6. 2026) | 11,75 % |

Výpočet: `jistina × sazba × počet dnů prodlení / 365`, zaokrouhlení na haléře (ROUND_HALF_UP). Dny se počítají včetně prvního dne prodlení i včetně dne `--do` (k tomuto dni se předpokládá, že dluh trvá).

## 2. Lhůty

### Procesní počítání (§ 57 o. s. ř.)

Zdroj: zákon č. 99/1963 Sb., občanský soudní řád.
URL: https://www.zakonyprolidi.cz/cs/1963-99

§ 57:

1. Do běhu lhůty se nezapočítává den, kdy došlo ke skutečnosti určující počátek lhůty (neplatí u lhůty podle hodin).
2. Lhůty podle týdnů, měsíců nebo let končí dnem, který se označením shoduje se dnem rozhodné skutečnosti. Není-li takový den v měsíci, končí lhůta posledním dnem měsíce. Připadne-li konec na sobotu, neděli nebo svátek, je posledním dnem nejblíže následující pracovní den.
3. Lhůta je zachována, je-li posledního dne učiněn úkon u soudu nebo podání odevzdáno orgánu, který má povinnost je doručit.

Hmotněprávní (prekluzivní) lhůty: návrh musí soudu poslední den dojít, odeslání nestačí. Skript s `--hmotnepravni` na to upozorní. Počítání konce (včetně posunu ze so/ne/svátku) bere podle § 57, protože OZ § 605 a § 607 jsou obsahově stejné.

OZ § 605 až § 607: https://www.zakonyprolidi.cz/cs/2012-89

### Státní a ostatní svátky (zákon č. 245/2000 Sb.)

URL: https://www.zakonyprolidi.cz/cs/2000-245
Aktuální znění 13. 5. 2026 (verze 12). Významné dny podle § 4 jsou dny pracovní.

Státní svátky (§ 1):

| Den | Název |
| --- | --- |
| 1. 1. | Den obnovy samostatného českého státu |
| 8. 5. | Den vítězství |
| 5. 7. | Den slovanských věrozvěstů Cyrila a Metoděje |
| 6. 7. | Den upálení mistra Jana Husa |
| 28. 9. | Den české státnosti |
| 28. 10. | Den vzniku samostatného československého státu |
| 17. 11. | Den boje za svobodu a demokracii a Mezinárodní den studentstva |

Ostatní svátky (§ 2): 1. 1. Nový rok, Velký pátek, Velikonoční pondělí, 1. 5. Svátek práce, 24. 12. Štědrý den, 25. 12. 1. svátek vánoční, 26. 12. 2. svátek vánoční.

Velikonoce skript počítá anonymním gregoriánským algoritmem (Meeus/Jones/Butcher). Velký pátek = neděle minus 2 dny, velikonoční pondělí = neděle plus 1 den.

Ověřené Velikonoce: 2026 neděle 5. 4. (Velký pátek 3. 4., pondělí 6. 4.).

## 3. Promlčení (orientačně)

Zdroj: zákon č. 89/2012 Sb., občanský zákoník.
URL: https://www.zakonyprolidi.cz/cs/2012-89

| Typ | Lhůta | Ustanovení |
| --- | --- | --- |
| obecna | 3 roky (subjektivní). Majetkové právo nejpozději 10 let od dospělosti. | § 629, počátek § 619 |
| uznani | 10 let od uznání, nebo od posledního dne určené doby plnění | § 639 (splátky § 641) |
| skoda | subjektivní 3 roky, objektivně 10 let od vzniku škody (úmysl 15 let, újma na svobodě/životě/zdraví bez objektivní lhůty) | § 636, počátek § 620 |
| obohaceni | subjektivní 3 roky, objektivně 10 let od obohacení (úmysl 15 let) | § 638, počátek § 621 |

Konec lhůty podle let: stejné číslo dne jako rozhodná skutečnost (§ 605 odst. 2 OZ). Posun ze so/ne/svátku podle § 607 OZ.

Skript neřeší stavění běhu, uplatnění u soudu, dílčí plnění ani úmysl. Výraz „přerušení promlčení" je stará terminologie, nepoužívat.

## 4. Soudní poplatek (peněžité plnění)

Předpis: zákon č. 549/1991 Sb., o soudních poplatcích.
URL: https://www.zakonyprolidi.cz/cs/1991-549

Základ procentního poplatku se zaokrouhluje na celé desítky Kč nahoru (§ 6 odst. 7). Poplatek podle sazebníku nejvýše 2 000 000 Kč, ledaže sazebník stanoví jinak (§ 6a odst. 7). Položka 1 bod 1 písm. c) stanoví jinak.

### Položka 1 (návrh na zahájení řízení o peněžité plnění)

| Pásmo | Sazba |
| --- | --- |
| do 20 000 Kč | 1 000 Kč |
| vyšší než 20 000 Kč do 40 000 000 Kč | 5 % z částky |
| vyšší než 40 000 000 Kč | 2 000 000 Kč + 1 % z částky přesahující 40 000 000 Kč; nad 250 000 000 Kč se nezapočítává |

### Položka 2 (návrh na vydání elektronického platebního rozkazu)

Skript s `--epr`. Pokud návrh není podán přes určenou aplikaci, vybere se položka 1 (bod 3 položky 2).

| Pásmo | Sazba |
| --- | --- |
| do 10 000 Kč včetně | 400 Kč |
| vyšší než 10 000 do 20 000 Kč včetně | 800 Kč |
| vyšší než 20 000 Kč | 4 % z částky |

Nevydá-li soud EPR a pokračuje v řízení, doměří se do položky 1 (bod 2). Skript to nepočítá, jen upozorní.

Příklady (stav k 2026-10-16): 85 000 Kč položka 1 = 4 250 Kč, EPR = 3 400 Kč. 20 000 Kč = 1 000 Kč. 20 001 Kč = 5 % z 20 010 = 1 000,50 Kč.

## 5. Advokátní tarif

Předpis: vyhláška č. 177/1996 Sb.
URL: https://www.zakonyprolidi.cz/cs/1996-177

### § 7 sazba mimosmluvní odměny za jeden úkon

| Tarifní hodnota | Sazba za úkon |
| --- | --- |
| do 500 Kč | 300 Kč |
| přes 500 do 1 000 Kč | 500 Kč |
| přes 1 000 do 5 000 Kč | 1 000 Kč |
| přes 5 000 do 10 000 Kč | 1 500 Kč |
| přes 10 000 do 200 000 Kč | 1 500 Kč + 40 Kč za každých započatých 1 000 Kč nad 10 000 Kč |
| přes 200 000 do 10 000 000 Kč | 9 100 Kč + 40 Kč za každých započatých 10 000 Kč nad 200 000 Kč |
| přes 10 000 000 Kč | 48 300 Kč + 40 Kč za každých započatých 100 000 Kč nad 10 000 000 Kč |

Příklad: tarifní hodnota 85 000 Kč = 1 500 + 40 × 75 = 4 500 Kč za úkon.

### § 8 tarifní hodnota u peněžitého plnění

Tarifní hodnotou je výše peněžitého plnění v době započetí úkonu. K příslušenství se nepřihlíží, ledaže je samostatným nárokem.

### § 11 úkony (přehled)

Plná odměna mimo jiné: převzetí a příprava zastoupení, písemné podání nebo návrh ve věci samé, výzva k plnění se základním rozborem, účast na jednání (každé započaté 2 hodiny), odvolání a dovolání.

Polovina mimo jiné: jednoduchá výzva k plnění, účast při vyhlášení rozhodnutí, některé návrhy po zahájení řízení.

Skript bere `--ukony` jako počet úkonů v plné sazbě. Poloviční úkony zadej jako počet plných (např. dva poloviční = 1).

### § 13 odst. 4 režijní paušál

Nedohodl-li se advokát s klientem na jiné paušální částce jako náhradě výdajů na vnitrostátní poštovné, místní hovorné a přepravné, činí tato částka 450 Kč na jeden úkon právní služby.

### DPH

Základní sazba 21 % (§ 47 odst. 1 písm. a) zákona č. 235/2004 Sb.).
URL: https://www.zakonyprolidi.cz/cs/2004-235#p47
Právní služby: základní sazba. Skript DPH připočte jen s `--dph` (plátce).

Příklad: 3 úkony při 85 000 Kč: odměna 13 500 Kč + paušál 1 350 Kč = 14 850 Kč, DPH 3 118,50 Kč, celkem 17 968,50 Kč.

## Jak aktualizovat

1. Otevři ČNB tabulku repo sazby. Přibyla-li změna, doplň řádek do této tabulky i do `REPO_ZMENY` v `scripts/vypocty.py`.
2. Na zakonyprolidi.cz zkontroluj znění 351/2013, 549/1991 (položka 1 a 2 sazebníku), 177/1996 (§ 7, § 8, § 11, § 13 odst. 4), 245/2000 a 235/2004 § 47. Změnu přenes do tabulek i do dat ve skriptu.
3. Přepiš „Stav k" v tomto souboru, v `sources.md` a v komentáři ve skriptu.
4. Spusť `python -m pytest _tools/tests/test_vypocty.py -q`. Testy s ručně spočtenými očekáváními musí projít. Změní-li se zákonná částka, uprav očekávání v testu podle nového primárního zdroje, ne podle skriptu.
