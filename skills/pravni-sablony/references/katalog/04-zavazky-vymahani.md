# Katalog úloh 04: Závazky a vymáhání pohledávek (Z-)

Druhá noha praxe vedle nemovitostí: dostat od dlužníka peníze co nejlevněji a bez procesní chyby. Karty jdou v pořadí, v jakém věc obvykle běží: výzva, uznání nebo narovnání, platební rozkaz, žaloba, obrana dlužníka; k tomu zajištění dluhu ručením, postoupení a hlídání promlčení. Čísla (úrok, poplatek, odměna, konce lhůt) počítá vždy `/pravni-vypocty`, nikdy model z hlavy.

Ustanovení v řádcích „Klíčová ustanovení" jsou ověřena v plném znění na zakonyprolidi.cz ke dni 16. 10. 2026. Do podání je cituj až po ověření znění k rozhodnému dni přes DirectCase. Eskalace: [`references/eskalace.md`](../../../../references/eskalace.md). Kontroly podání: [`references/kontroly-podani.md`](../../../../references/kontroly-podani.md).

Zkratky: OZ = zák. č. 89/2012 Sb.; o. s. ř. = zák. č. 99/1963 Sb.; NV 351/2013 = nařízení vlády č. 351/2013 Sb.; EŘ = zák. č. 120/2001 Sb.; IZ = zák. č. 182/2006 Sb.; ZSP = zák. č. 549/1991 Sb., o soudních poplatcích.

## Obsah
- Z-01 Předžalobní výzva
- Z-02 Uznání dluhu
- Z-03 Dohoda o narovnání
- Z-04 Návrh na vydání platebního rozkazu a elektronického platebního rozkazu
- Z-05 Žaloba o zaplacení
- Z-06 Odpor proti platebnímu rozkazu
- Z-07 Smluvní pokuta
- Z-08 Úroky z prodlení
- Z-09 Postoupení pohledávky
- Z-10 Ručení
- Z-11 Bezdůvodné obohacení
- Z-12 Promlčení: hlídání a obrana
- Z-13 Započtení

---

### Z-01 Předžalobní výzva
- **Kdy:** před každou žalobou nebo návrhem na platební rozkaz na splnění povinnosti; zároveň poslední mimosoudní pokus.
- **Klíčová ustanovení (ověřeno):** § 142a o. s. ř.; § 1968, § 1970 a § 648 OZ; § 2 a § 3 NV 351/2013.
- **Co nesmí chybět:** věřitel a dlužník; dluh přesně (titul, faktury, splatnost, jistina); příslušenství (úrok z prodlení; u vzájemného závazku podnikatelů a u dodávky zboží nebo služby podnikatele veřejnému zadavateli minimální náklady 1 200 Kč za každou pohledávku podle § 3 NV 351/2013); lhůta k plnění a účet; upozornění na soudní vymáhání; adresa pro doručování, případně poslední známá adresa.
- **Lhůty a rizika:** výzva musí odejít nejméně 7 dnů před podáním návrhu, jinak žalobce i při úspěchu zpravidla nedostane náhradu nákladů řízení (§ 142a odst. 1); výjimka jen z důvodů hodných zvláštního zřetele (odst. 2). Výzva běh promlčení nezastaví, to udělá až uplatnění práva u soudu (§ 648 OZ).
- **Časté chyby:** výzva e-mailem bez důkazu o odeslání; nezaznamenaný den odeslání; ve výzvě jiná částka než v žalobě; úrok počítaný ručně.
- **Nástroj:** `/generuj-smlouvu` vzor `predzalobni-vyzva` (gate: lhůta pod 7 dnů, chybí doručovací adresa); úrok `/pravni-vypocty urok`.
- **Eskalace:** dluh blízko promlčení (Z-12), dlužník v insolvenci (místo žaloby přihláška, E-10) = advokát.

### Z-02 Uznání dluhu
- **Kdy:** dlužník dluh nepopírá a chce splácet, nebo věřitel potřebuje novou promlčecí lhůtu.
- **Klíčová ustanovení (ověřeno):** § 2053, § 2054, § 639, § 641 OZ; § 40 odst. 1 písm. d) EŘ.
- **Co nesmí chybět:** písemná forma a podpis dlužníka; dluh co do důvodu i výše (§ 2053); u splátek kalendář, jehož součet odpovídá dluhu, a ujednání o ztrátě výhody splátek; doba, do které dlužník splní.
- **Lhůty a rizika:** uznání zakládá domněnku, že dluh v rozsahu uznání trvá (§ 2053), a desetiletou promlčecí lhůtu od uznání, nebo od posledního dne doby, do které dlužník slíbil plnit (§ 639). U splátek běží pro každou splátku od její dospělosti; dospěje-li celý dluh nesplněním splátky, od dospělosti nesplněné splátky (§ 641). Placení úroků a částečné plnění mohou mít účinky uznání, ne však u promlčené pohledávky (§ 2054). Uznání není exekučním titulem; přímo vykonatelný je notářský zápis se svolením k vykonatelnosti (§ 40 odst. 1 písm. d) EŘ).
- **Časté chyby:** „přerušení promlčení" (pojem starého OZ, nepoužívat); uznání bez výše; součet splátek nesedí; souhlas e-mailem bez podpisu.
- **Nástroj:** `/generuj-smlouvu` vzor `uznani-dluhu` (gate: důvod a výše, součet splátek = dluh, pořadí splátek); promlčení `/pravni-vypocty promlceni --typ uznani`.
- **Eskalace:** spotřebitel s výraznými sankcemi za nesplacení, požadavek na zajištění nemovitostí = advokát.

### Z-03 Dohoda o narovnání
- **Kdy:** strany chtějí spor nebo nejistotu ukončit dohodou se vzájemnými ústupky.
- **Klíčová ustanovení (ověřeno):** § 1903, § 1904, § 1905, § 1906, § 647 OZ.
- **Co nesmí chybět:** popis sporných nebo pochybných práv; ústupky; nové uspořádání (kdo co plní a kdy); rozsah konečnosti (která práva se vypořádávají a která výslovně ne); procesní důsledky (zpětvzetí žaloby, náklady řízení).
- **Lhůty a rizika:** písemná forma je nutná, byl-li původní závazek písemný nebo jde o promlčené právo (§ 1906). Narovnání „všech práv" se nevztahuje na práva vyloučená ani na ta, na která strany zřejmě nemohly myslet (§ 1905). Týká-li se věcného práva k zapsané nemovitosti, účinky nastanou až zápisem (§ 1903 odst. 1). Omyl ve sporné věci platnost neruší, ledaže byl vyvolán lstí (§ 1904). Během dohodnutého mimosoudního jednání promlčecí lhůta neběží, dokud jedna strana výslovně neodmítne pokračovat (§ 647).
- **Časté chyby:** chybí výčet narovnávaných práv; plnění bez splatnosti; zapomenuté náklady řízení.
- **Nástroj:** `/generuj-smlouvu` vzor `dohoda-o-narovnani` (gate: sporné právo, nové plnění, částka, splatnost); u nemovitostí návrh na vklad N-05.
- **Eskalace:** narovnání v běžícím řízení (soudní smír), nemovitost nebo částka nad práh v `legal.local.md` = advokát.

### Z-04 Návrh na vydání platebního rozkazu a elektronického platebního rozkazu
- **Kdy:** peněžitý nárok doložený listinami a dlužník se známým pobytem v ČR.
- **Klíčová ustanovení (ověřeno):** § 79, § 142a, § 172, § 173, § 174, § 174a o. s. ř.; položky 1 a 2 sazebníku ZSP.
- **Co nesmí chybět:** náležitosti žaloby (§ 79 o. s. ř.) a skutečnosti, ze kterých nárok vyplývá (§ 172 odst. 1); listinné důkazy; u EPR elektronický formulář podepsaný žalobcem a datum narození nebo IČO (§ 174a odst. 1 a 2); zaplacený poplatek; tvrzení a doklad o předžalobní výzvě.
- **Lhůty a rizika:** platební rozkaz nelze vydat při neznámém pobytu žalovaného, doručování do ciziny nebo proti nezletilému bez plné svéprávnosti (§ 172 odst. 2). Doručuje se do vlastních rukou bez náhradního doručení, ledaže do datové schránky (§ 173 odst. 1); nelze-li doručit i jen jednomu ze žalovaných, soud rozkaz zruší (§ 173 odst. 2). Neúplný návrh na EPR soud odmítne bez výzvy k opravě (§ 174a odst. 4); bez zaplaceného poplatku EPR nevydá (§ 174a odst. 5 písm. b)). Nižší poplatek za EPR jen při podání přes určenou aplikaci, jinak položka 1; když soud EPR nevydá a pokračuje, poplatek doměří (položka 2 body 2 a 3 ZSP).
- **Časté chyby:** EPR mimo předepsaný formulář; nezaplacený poplatek; příslušenství nevyčíslené nebo se špatnou sazbou.
- **Nástroj:** `/pravni-sablony` (návrh); poplatek `/pravni-vypocty poplatek --castka X --epr`; úrok `/pravni-vypocty urok`.
- **Kontroly:** references/kontroly-podani.md
- **Eskalace:** dlužník v cizině (jiný procesní režim) nebo v insolvenci = advokát.

### Z-05 Žaloba o zaplacení
- **Kdy:** platební rozkaz nepřichází v úvahu nebo padl odporem; skutkový spor.
- **Klíčová ustanovení (ověřeno):** § 9, § 42, § 79, § 84, § 85, § 87, § 89a, § 142a o. s. ř.; § 648 OZ.
- **Co nesmí chybět:** soud; účastníci s identifikací podle § 79 odst. 1; rozhodující skutečnosti; označené důkazy a připojené listiny (§ 79 odst. 2); petit; doklad o předžalobní výzvě; vyčíslení jistiny a příslušenství; plná moc.
- **Lhůty a rizika:** v prvním stupni zpravidla okresní soud (§ 9 odst. 1); místně obecný soud žalovaného (§ 84, § 85), na výběr i soud podle § 87; podnikatelé se mohou písemně dohodnout na jiném soudu, není-li příslušnost výlučná (§ 89a). Podání žaloby a řádné pokračování v řízení staví běh promlčecí lhůty (§ 648 OZ). Návrh ve věci samé podaný elektronicky bez podpisu s účinky vlastnoručního podpisu je třeba do 3 dnů doplnit originálem (§ 42 odst. 2 a 3).
- **Časté chyby:** chyba v částce nebo v počátku úroku v petitu; chybí doklad o výzvě; důkazy jen označené, nepřiložené.
- **Nástroj:** `/pravni-sablony` (žaloba); poplatek, úrok, odměna `/pravni-vypocty`; kontrola citací `/hloubkovy-research citace`.
- **Kontroly:** references/kontroly-podani.md
- **Eskalace:** protinárok nebo započtení žalovaného, spor nad práh v `legal.local.md`, cizinec = advokát.

### Z-06 Odpor proti platebnímu rozkazu
- **Kdy:** klientovi byl doručen platební rozkaz nebo elektronický platební rozkaz.
- **Klíčová ustanovení (ověřeno):** § 114b, § 172 odst. 1, § 174, § 174a odst. 6, § 175 o. s. ř.
- **Co nesmí chybět:** den doručení (doručenka, datová schránka); odpor podaný u soudu, který rozkaz vydal; u EPR i na elektronickém formuláři (§ 174a odst. 6); věcná obrana připravená pro další krok (zaplacení, započtení, promlčení, vady plnění).
- **Lhůty a rizika:** odpor do 15 dnů od doručení (§ 172 odst. 1); včasný odpor i jen jednoho žalovaného ruší rozkaz celý (§ 174 odst. 2); opožděný odpor soud odmítne, pro nedostatek odůvodnění odmítnout nelze (§ 174 odst. 3). Následovat může výzva k vyjádření s lhůtou nejméně 30 dnů, počítanou až od uplynutí lhůty k odporu (§ 114b odst. 1 a 2); když se žalovaný bez vážného důvodu nevyjádří, má se za to, že nárok uznává (§ 114b odst. 5). Hlídej tři samostatné kroky: odpor, výzva, vyjádření.
- **Časté chyby:** brojení jen proti nákladům (proti výroku o nákladech je odvolání, § 174 odst. 2); lhůta počítaná od data vydání; přehlédnutá výzva podle § 114b; záměna se směnečným rozkazem, kde se podávají odůvodněné námitky (§ 175).
- **Nástroj:** `/pravni-sablony` (odpor, vyjádření); lhůta `/pravni-vypocty lhuta --delka 15 --jednotka dny`.
- **Kontroly:** references/kontroly-podani.md
- **Eskalace:** lhůta končí do 14 dnů = výrazné upozornění a advokát hned; směnečný platební rozkaz = vždy advokát.

### Z-07 Smluvní pokuta
- **Kdy:** sjednání pokuty, její uplatnění, nebo obrana proti nepřiměřené pokutě.
- **Klíčová ustanovení (ověřeno):** § 1 odst. 2, § 2048, § 2049, § 2050, § 2051, § 2052, § 1813, § 2254 OZ.
- **Co nesmí chybět:** přesná povinnost, jejíž porušení pokutu spouští; výše nebo způsob jejího určení (§ 2048 odst. 1); splatnost; vztah k náhradě škody.
- **Lhůty a rizika:** pokuta náleží bez ohledu na vznik škody (§ 2048 odst. 1) a dluh zaplacením pokuty nezaniká (§ 2049); náhradu škody ze stejného porušení věřitel vedle pokuty nemá (§ 2050), není-li ujednáno jinak (ustanovení je dispozitivní, § 1 odst. 2). Nepřiměřeně vysokou pokutu může soud na návrh dlužníka snížit až do výše škody (§ 2051). U spotřebitele hrozí zneužívající ujednání (§ 1813), u nájmu bytu platí strop spolu s jistotou (§ 2254 odst. 1). Pravidla platí i pro zákonné penále (§ 2052).
- **Časté chyby:** pokuta bez vymezené povinnosti; denní pokuta bez stropu; požadavek na pokutu i plnou náhradu škody ze stejného porušení bez ujednání, které souběh připouští.
- **Nástroj:** sepsání `/pravni-sablony` nebo ve vzorech `/generuj-smlouvu`; posouzení cizí smlouvy `/revize-smlouvy`. Výši pokuty za dny prodlení skript nepočítá: spočítej s rozpisem a nech potvrdit advokátem.
- **Eskalace:** spor o moderaci, spotřebitelské smlouvy ve velkém objemu = advokát.

### Z-08 Úroky z prodlení
- **Kdy:** vyčíslení příslušenství do výzvy, žaloby, přihlášky nebo uznání dluhu.
- **Klíčová ustanovení (ověřeno):** § 1968, § 1970 OZ; § 2 a § 3 NV 351/2013.
- **Co nesmí chybět:** jistina; den splatnosti; první den prodlení; sazba (ujednaná, jinak zákonná); konec výpočtu; u vzájemného závazku podnikatelů a u dodávky zboží nebo služby podnikatele veřejnému zadavateli minimální náklady 1 200 Kč za každou pohledávku (§ 3 NV 351/2013).
- **Lhůty a rizika:** zákonná sazba = repo sazba ČNB pro první den kalendářního pololetí, v němž prodlení nastalo, plus 8 procentních bodů (§ 2 odst. 1 NV 351/2013); neujednají-li strany jinou výši, platí tato (§ 1970 OZ). Úrok může žádat jen věřitel, který řádně splnil své povinnosti, a nenáleží, není-li dlužník za prodlení odpovědný (§ 1970).
- **Časté chyby:** sazba z aktuálního pololetí místo z pololetí vzniku prodlení; úrok od dne splatnosti místo ode dne následujícího; paušál 1 200 Kč uplatněný mimo vztahy podle § 3 NV 351/2013, nebo naopak zapomenutý u dodávky veřejnému zadavateli.
- **Nástroj:** `/pravni-vypocty urok --castka X --splatnost RRRR-MM-DD --do RRRR-MM-DD` (ve vztazích podle § 3 NV 351/2013 `--podnikatele`); nikdy z hlavy.
- **Eskalace:** smluvní úrok zjevně nepřiměřený, úrok z výživného (skript ho nepočítá) = advokát.

### Z-09 Postoupení pohledávky
- **Kdy:** klient pohledávku prodává nebo kupuje, nebo je dlužníkem postoupené pohledávky.
- **Klíčová ustanovení (ověřeno):** § 1879 až § 1887 OZ; § 107a o. s. ř.; § 177 odst. 2 IZ.
- **Co nesmí chybět:** přesná identifikace pohledávky (titul, výše, příslušenství, zajištění); kontrola, zda postoupení nevylučuje ujednání s dlužníkem (§ 1881 odst. 1); úplata a odpovědnost za trvání a dobytnost (§ 1885); předání dokladů (§ 1880 odst. 2); vyrozumění dlužníka a osob, které dluh zajistily (§ 1882, § 1883).
- **Lhůty a rizika:** dokud postupitel dlužníka nevyrozumí nebo postupník postoupení neprokáže, dlužník se zprostí plněním postupiteli (§ 1882 odst. 1). Vůči ručiteli nebo zástavci postoupení působí až po vyrozumění (§ 1883). Dlužníkovi zůstávají námitky a může započíst i své pohledávky vůči postupiteli, oznámí-li je bez zbytečného odkladu (§ 1884 odst. 1). Za úplatu postupitel odpovídá za trvání a ručí za dobytnost do výše úplaty, ledaže postupník věděl o nejistotě (§ 1885 odst. 1). V běžícím řízení vstup postupníka návrhem podle § 107a o. s. ř. V insolvenci přikládá postupník, který pohledávku nabyl po zahájení řízení nebo v posledních 6 měsících před ním, čestné prohlášení o skutečném majiteli (§ 177 odst. 2 IZ).
- **Časté chyby:** dlužník nevyrozuměn; zajištění neoznámeno ručiteli; postoupení přes smluvní zákaz.
- **Nástroj:** `/pravni-sablony` (smlouva o postoupení, vyrozumění dlužníka); `/revize-smlouvy`.
- **Eskalace:** soubor pohledávek (§ 1887), pohledávky vůči spotřebitelům ve velkém, pohledávka zajištěná nemovitostí = advokát.

### Z-10 Ručení
- **Kdy:** zajištění dluhu třetí osobou (jednatel za společnost, rodič za dítě), nebo uplatnění práva vůči ručiteli.
- **Klíčová ustanovení (ověřeno):** § 2018, § 2019, § 2020, § 2021, § 2022, § 2023, § 2026, § 2029, § 1883 OZ.
- **Co nesmí chybět:** písemné ručitelské prohlášení vůči věřiteli (§ 2018 odst. 2) a jeho přijetí věřitelem (§ 2018 odst. 1); zajištěný dluh, i budoucí nebo soubor dluhů (§ 2019 odst. 1); rozsah, případně jen část dluhu (§ 2020); doba ručení.
- **Lhůty a rizika:** po ručiteli lze plnění žádat, až dlužník nesplnil v přiměřené lhůtě po písemné výzvě, ledaže výzvu nelze uskutečnit nebo je nesplnění nepochybné (§ 2021 odst. 1); u ručení na dobu určitou musí věřitel ručitele v této době vyzvat (§ 2021 odst. 2). Ručitel má všechny námitky dlužníka (§ 2023 odst. 1) a může plnění odepřít, zavinil-li věřitel nedobytnost u dlužníka (§ 2022). Ručení zaniká se zajištěným dluhem, ne však při zániku právnické osoby dlužníka (§ 2026 odst. 2).
- **Časté chyby:** ručení ústní nebo e-mailem bez podpisu; uplatnění u ručitele bez předchozí písemné výzvy dlužníkovi; záměna s finanční zárukou, která vzniká záruční listinou (§ 2029).
- **Nástroj:** `/pravni-sablony` (ručitelské prohlášení, výzva dlužníkovi a ručiteli); žaloba Z-05.
- **Eskalace:** ručitel spotřebitel za podnikatelský dluh, ručení manžela (SJM, N-10) = advokát.

### Z-11 Bezdůvodné obohacení
- **Kdy:** plnění bez právního důvodu, z neplatné nebo zrušené smlouvy, užívání cizí věci bez titulu, platba omylem. Neodevzdá-li nájemce byt po skončení nájmu, uplatni přednostně náhradu ve výši nájemného podle § 2295 OZ (NJ-09), ne bezdůvodné obohacení.
- **Klíčová ustanovení (ověřeno):** § 2991, § 2993, § 2999, § 3000, § 3004, § 610 odst. 2, § 619, § 629, § 638 OZ.
- **Co nesmí chybět:** skutečnosti zakládající obohacení a jeho výši; zda šlo o plnění bez platného nebo ze zrušeného závazku (§ 2993); dobrá, nebo zlá víra obohaceného (§ 3000, § 3004); výpočet peněžité náhrady, nelze-li vydat věc (§ 2999 odst. 1).
- **Lhůty a rizika:** subjektivní lhůta 3 roky (§ 629 odst. 1, § 619), objektivní 10 let od obohacení, při úmyslném obohacení 15 let (§ 638). U vzájemného vracení z neplatné smlouvy soud přihlédne k promlčení, jen mohla-li ho namítnout i druhá strana (§ 610 odst. 2). Poctivý příjemce vydá, jen co při uplatnění práva trvá (§ 3000); nepoctivý vydá vše včetně plodů a užitků (§ 3004 odst. 1).
- **Časté chyby:** obohacení uplatněné tam, kde existuje smluvní nárok; chybí tvrzení o dobré nebo zlé víře.
- **Nástroj:** `/pravni-sablony` (výzva, žaloba); promlčení `/pravni-vypocty promlceni --typ obohaceni`.
- **Kontroly:** references/kontroly-podani.md (u žaloby)
- **Eskalace:** obohacení trestným činem, souběh s nárokem na náhradu škody = advokát.

### Z-12 Promlčení: hlídání a obrana
- **Kdy:** před každou výzvou, žalobou a přihláškou; při obraně proti staré pohledávce.
- **Klíčová ustanovení (ověřeno):** § 609, § 610, § 619, § 629, § 636, § 638, § 639, § 641, § 647, § 648, § 2054 odst. 3 OZ; § 173 odst. 4 IZ.
- **Co nesmí chybět:** den, kdy právo mohlo být uplatněno poprvé, tedy dospělost a vědomost o rozhodných okolnostech (§ 619); případné uznání (§ 639, § 641); dohodnuté mimosoudní jednání (§ 647); dříve zahájená řízení (§ 648).
- **Lhůty a rizika:** subjektivně 3 roky (§ 629 odst. 1), objektivně nejpozději 10 let od dospělosti majetkového práva (§ 629 odst. 2); náhrada škody nejpozději 10 let, při úmyslu 15 let od vzniku škody (§ 636); bezdůvodné obohacení obdobně (§ 638). Promlčené právo dlužník plnit nemusí, ale plnil-li, zpět nic nežádá (§ 609); soud přihlédne jen k námitce dlužníka (§ 610 odst. 1). Uplatnění u soudu nebo návrh na exekuci běh staví (§ 648); přihláška do insolvence má stejné účinky jako žaloba (§ 173 odst. 4 IZ).
- **Časté chyby:** „přerušení promlčení"; spoléhání na uznání placením úroků u už promlčené pohledávky (§ 2054 odst. 3); zapomenutá objektivní lhůta.
- **Nástroj:** `/pravni-vypocty promlceni --pocatek RRRR-MM-DD --typ obecna|uznani|skoda|obohaceni` (stavění běhu skript neřeší, doplní advokát).
- **Eskalace:** nárok blízko promlčení = výrazné upozornění nahoře a advokát hned (kontroly-podani.md, blok 3).

### Z-13 Započtení
- **Kdy:** strany si vzájemně dluží peníze; dlužník chce dluh umořit svou pohledávkou; obrana v řízení.
- **Klíčová ustanovení (ověřeno):** § 1982, § 1987, § 1884 OZ; § 140 odst. 2 IZ.
- **Co nesmí chybět:** projev započtení vůči druhé straně (§ 1982 odst. 1); přesná identifikace obou pohledávek a započítávané částky; den, kdy se pohledávky staly způsobilými k započtení.
- **Lhůty a rizika:** započíst lze, jakmile lze žádat uspokojení vlastní pohledávky a plnit vlastní dluh (§ 1982 odst. 1); pohledávky zanikají v rozsahu, v jakém se kryjí, k okamžiku, kdy se staly způsobilými k započtení (§ 1982 odst. 2). K započtení jsou způsobilé jen pohledávky uplatnitelné u soudu; nejistou nebo neurčitou započíst nelze (§ 1987). Proti postupníkovi lze započíst i pohledávky vůči postupiteli při včasném oznámení (§ 1884 odst. 1). Po rozhodnutí o úpadku jen za podmínek § 140 odst. 2 IZ.
- **Časté chyby:** „započítáváme" bez vyčíslení; projev započtení nedoručený druhé straně.
- **Nástroj:** `/pravni-sablony` (prohlášení o započtení, námitka započtení ve vyjádření).
- **Eskalace:** započtení v insolvenci, spor o existenci protipohledávky = advokát.

<!-- Origin: GrowLead ak-sladek v0.9, vlastní text katalogu úloh | Vytvořeno: 2026-10-16 | Ověřeno na zakonyprolidi.cz 2026-10-16: OZ § 609, 610, 619, 629, 636, 638, 639, 641, 647, 648, 1813, 1879 až 1887, 1903 až 1906, 1968, 1970, 1982, 1987, 2018 až 2024, 2026, 2029, 2048 až 2054, 2254, 2991, 2993, 2999, 3000, 3004; o. s. ř. § 9, 42, 79, 84, 85, 87, 89a, 107a, 114b, 142a, 172 až 175; NV 351/2013 § 2, 3; EŘ § 40; IZ § 140, 173, 177; ZSP sazebník položky 1 a 2 | Review: Codex cross-family 2026-10-16, nálezy ověřeny a zapracovány (Z-01, Z-07, Z-08, Z-11): OZ § 1, 2295, NV 351/2013 § 3 | Inspiration: externí katalog právních úloh jen jako kontrolní seznam pokrytí (názvy), text vlastní -->
