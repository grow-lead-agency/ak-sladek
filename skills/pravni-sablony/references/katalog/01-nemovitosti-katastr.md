# Katalog úloh 01: Nemovitosti a katastr (N-)

Jádro praxe kanceláře: převody nemovitostí, prověrka listu vlastnictví a vše, co se kolem vkladu do katastru typicky pokazí. Každá karta říká, co připravit, podle čeho, kde bývá chyba a kdy přestat a předat věc advokátovi. Karta není text smlouvy; text dodá vzor kanceláře (`/generuj-smlouvu`) nebo šablona (`/pravni-sablony`) a vždy jde o návrh ke kontrole advokátem.

Ustanovení v řádcích „Klíčová ustanovení" jsou ověřena v plném znění na zakonyprolidi.cz ke dni 16. 10. 2026. Do podání je cituj až po ověření znění k rozhodnému dni přes DirectCase (`get_law_detail`). Eskalační pravidla: [`references/eskalace.md`](../../../../references/eskalace.md). Kontroly podání: [`references/kontroly-podani.md`](../../../../references/kontroly-podani.md).

Zkratky: OZ = zák. č. 89/2012 Sb.; kat. z. = zák. č. 256/2013 Sb., katastrální zákon; kat. vyhl. = vyhl. č. 357/2013 Sb.; o. s. ř. = zák. č. 99/1963 Sb.; ZRZ = zák. č. 39/2020 Sb., o realitním zprostředkování.

## Obsah
- N-01 Kupní smlouva k nemovitosti (převod s úschovou)
- N-02 Prověrka listu vlastnictví (části A až F)
- N-03 Smlouva o smlouvě budoucí kupní (nemovitost)
- N-04 Rezervační smlouva
- N-05 Návrh na vklad a jeho náležitosti
- N-06 Výmaz zástavního práva
- N-07 Služebnosti: služebnost bytu, užívací a požívací právo
- N-08 Darování nemovitosti s výhradou věcného břemene
- N-09 Spoluvlastnictví: zrušení a vypořádání
- N-10 Společné jmění manželů při převodu
- N-11 Vady při koupi nové jednotky od developera
- N-12 Realitní zprostředkování
- N-13 Poznámka spornosti a žaloba o odstranění nesouladu zápisu
- N-14 Předkupní práva při prodeji
- N-15 Prodej bytové jednotky v domě se SVJ

---

### N-01 Kupní smlouva k nemovitosti (převod s úschovou)
- **Kdy:** prodej bytu, domu nebo pozemku, kupní cena (nebo doplatek) jde přes advokátní úschovu kanceláře.
- **Klíčová ustanovení (ověřeno):** § 2079, § 2128 odst. 1 ve spojení s § 560, § 1105, § 2129, § 2130 OZ; § 8 a § 10 kat. z.
- **Co nesmí chybět:** strany přesně podle dokladů (u manželů oba, u PO způsob jednání); nemovitost označená údaji katastru podle § 8 kat. z. (parcela s k. ú., jednotka včetně podílu na společných částech); cena a způsob platby navázaný na smlouvu o úschově; kdo a kdy podá návrh na vklad; stav zástav a jejich výmaz; ujednaný den převzetí (od něj plody, užitky a nebezpečí škody, § 2130 OZ).
- **Lhůty a rizika:** vlastnictví přechází až zápisem do katastru (§ 1105 OZ) s účinky ke dni, kdy návrh došel katastrálnímu úřadu (§ 10 kat. z.). Skrytou vadu stavby musí kupující vytknout do 5 let od nabytí (§ 2129 odst. 2 OZ); u spotřebitele platí dvouletá domněnka vady (§ 2129 odst. 3 OZ).
- **Časté chyby:** záloha v hotovosti nad limit 270 000 Kč (zák. č. 254/2004 Sb., § 4, viz U-11); nemovitost opsaná z inzerátu místo z LV; nepromyšlená výměra pozemku: na slevu má kupující právo, nemá-li pozemek výměru určenou ve smlouvě, a u výměry, která není zapsaná ve veřejném seznamu, jen bylo-li to ujednáno (§ 2129 odst. 1 OZ); chybí souhlas manžela; LV starší než den podpisu.
- **Nástroj:** `/generuj-smlouvu` vzor `prevod-nemovitosti` (kupní smlouva + úschova z jednoho zadání); prověrka LV N-02; strany `/kontrola-podpis`; formát `/formatuj-smlouvu`.
- **Eskalace:** exekuce nebo insolvence na LV, poznámka spornosti, cizinec, rozvod či zúžení SJM, PO jednající dvěma jednateli společně, financování hypotékou nebo více výplat z úschovy (vzor v0.1 je nepokrývá) = STOP, shrnout advokátovi (references/eskalace.md).

### N-02 Prověrka listu vlastnictví (části A až F)
- **Kdy:** před každou smlouvou o převodu, zástavě nebo služebnosti, znovu těsně před podpisem a před podáním návrhu na vklad.
- **Klíčová ustanovení (ověřeno):** § 23 odst. 2 a § 23a odst. 5 kat. vyhl. (členění LV); § 9 odst. 1, § 23, § 24 a § 25 kat. z.; § 980 a § 984 OZ.
- **Co nesmí chybět:** A vlastník a podíly (sedí na strany smlouvy?); B nemovitosti a plomba „P" (běží řízení, § 9 odst. 1 kat. z.: co je v něm?); B1 práva ve prospěch nemovitosti; C věcná práva zatěžující nemovitost (zástavy včetně soudcovských a exekutorských, služebnosti, předkupní práva, zákaz zcizení) a poznámky k nim; D poznámky k osobě nebo nemovitosti (exekuce, insolvence, předběžné opatření, spornost); E nabývací listiny; F údaje pro daňové účely. U jednotky v D informace o SVJ (§ 23a odst. 5 kat. vyhl.).
- **Lhůty a rizika:** LV je fotografie k jednomu okamžiku; co přijde po výpisu, uvidíš až z plomby. Neznalost zapsaného údaje nikoho neomlouvá (§ 980 odst. 1 OZ); kdo nabyl za úplatu v dobré víře od osoby oprávněné podle zápisu, je chráněn (§ 984 odst. 1 OZ).
- **Časté chyby:** kontrola jen části C a přehlédnutí exekuce nebo insolvence v části D (nebo naopak); plomba bez dohledání, jaké řízení běží; prověrka nemovitosti bez prověrky osoby prodávajícího v insolvenčním rejstříku.
- **Nástroj:** `/pravni-sablony` (checklist LV, výstup tabulka nálezů + co musí řešit smlouva nebo výplatní podmínky úschovy); osoba a firma `/hloubkovy-research firma`.
- **Eskalace:** jakýkoli zápis exekuce, insolvence, poznámky spornosti nebo předběžného opatření; nesoulad vlastníka na LV a strany smlouvy = STOP (references/eskalace.md).

### N-03 Smlouva o smlouvě budoucí kupní (nemovitost)
- **Kdy:** strany se dohodly na prodeji, ale kupní smlouvu ještě nelze uzavřít (dokončení stavby, vyřízení hypotéky, výmaz zástavy, vznik jednotky).
- **Klíčová ustanovení (ověřeno):** § 1785 až § 1788 a § 1808 OZ; u spotřebitele § 1813 a § 1814 OZ; § 14 ZRZ.
- **Co nesmí chybět:** obsah budoucí kupní smlouvy alespoň obecně (předmět podle LV, cena, způsob placení); lhůta, ve které lze vyzvat k uzavření, a kdo smí vyzvat; zda jde o zálohu, nebo závdavek (závdavek musí být odevzdán nejpozději při uzavření smlouvy, § 1808 odst. 1 OZ); kam jde záloha (doporučeně do úschovy); osud plateb, když se kupní smlouva neuzavře.
- **Lhůty a rizika:** bez ujednané lhůty platí jeden rok (§ 1785 OZ); nevyzve-li oprávněná strana včas, povinnost zaniká (§ 1788 odst. 1 OZ). Při podstatné změně okolností povinnost zaniká, ale zavázaná strana ji musí bez zbytečného odkladu oznámit (§ 1788 odst. 2 OZ). Když druhá strana neuzavře, obsah určí soud (§ 1787 OZ).
- **Časté chyby:** „záloha" i „závdavek" v jednom textu; propadnutí plnění jen v neprospěch spotřebitele bez reciprocity (zneužívající ujednání, § 1814 písm. c) a e) OZ); povinnost spotřebitele uzavřít budoucí smlouvu vtělená do smlouvy s realitkou (§ 14 ZRZ).
- **Nástroj:** `/generuj-smlouvu` vzor `smlouva-o-smlouve-budouci-kupni` (gate: předmět dle LV, cena, termín výzvy, typ a výše zálohy či závdavku); úschova zálohy U-08.
- **Eskalace:** developerský projekt s postupnými platbami, budoucí jednotka bez prohlášení vlastníka, cizinec, nestandardní úschova (references/eskalace.md).

### N-04 Rezervační smlouva
- **Kdy:** zájemce chce nemovitost „podržet" po dobu vyřízení financování; typicky s realitní kanceláří nebo developerem.
- **Klíčová ustanovení (ověřeno):** § 1746 odst. 2 OZ (nepojmenovaná smlouva); § 1813 a § 1814 písm. c) a e) OZ; § 4, § 15 a § 19 ZRZ.
- **Co nesmí chybět:** předmět rezervace podle LV; doba rezervace a co se během ní nesmí (nabízet třetím osobám); výše rezervačního poplatku a jeho osud ve všech třech scénářích (započtení na cenu, vrácení, propadnutí) s důvody; kdo poplatek drží.
- **Lhůty a rizika:** rezervační poplatek, který propadá jen spotřebiteli, zatímco podnikatel nic nevrací, je typické zneužívající ujednání (§ 1814 písm. c) OZ). Realitní zprostředkovatel nesmí nabízet úschovu (výjimka jen na písemnou žádost a za podmínek § 4 odst. 2 ZRZ).
- **Časté chyby:** smlouva o realitním zprostředkování a realitní smlouva v jedné listině (§ 15 ZRZ zakazuje právě spojení těchto dvou smluv, ne každé spojení s rezervací); poplatek ve skutečnosti skrývá provizi splatnou před uzavřením realitní smlouvy (§ 19 ZRZ).
- **Nástroj:** `/generuj-smlouvu` vzor `rezervacni-smlouva` (gate: doba, poplatek a jeho osud); cizí rezervační smlouvu `/revize-smlouvy`.
- **Eskalace:** spor o vrácení poplatku vůči realitní kanceláři s hrozbou žaloby přejde na Z- karty; pochybnost o spotřebitelském charakteru = advokát posoudí.

### N-05 Návrh na vklad a jeho náležitosti
- **Kdy:** po podpisu vkladové listiny (kupní, darovací, zástavní smlouva, smlouva o zřízení služebnosti, souhlas s výmazem).
- **Klíčová ustanovení (ověřeno):** § 6, § 7, § 8, § 9, § 10, § 11, § 14 až § 18 kat. z.; položka 120 písm. a) sazebníku zák. č. 634/2004 Sb.
- **Co nesmí chybět:** návrh na stanoveném formuláři s náležitostmi § 14 odst. 1 kat. z.; vkladová listina (bez ní se k návrhu nepřihlíží, § 15 odst. 2); plná moc s úředně ověřeným podpisem, je-li účastník zastoupen (§ 15 odst. 1 písm. b)); výpis z OR, nelze-li ho získat bezplatně dálkově; geometrický plán, týká-li se právo části pozemku (§ 7 odst. 3); správní poplatek 2 000 Kč za návrh.
- **Lhůty a rizika:** pořadí a účinky zápisu se řídí okamžikem doručení návrhu (§ 9 odst. 2, § 10 kat. z.). Vklad lze povolit nejdříve 20 dnů od odeslání informace vlastníkovi (§ 18 odst. 1 ve spojení s § 16 odst. 1). Neověřené podpisy na soukromé listině = prokázat pravost do 30 dnů, jinak zastavení (§ 7 odst. 2). Proti zamítnutí jen žaloba podle o. s. ř. do 30 dnů od doručení (§ 18 odst. 5). Zpětvzetí návrhu vyžaduje souhlas všech účastníků (§ 16 odst. 2).
- **Časté chyby:** elektronická listina bez uznávaného elektronického podpisu a kvalifikovaného časového razítka (§ 7 odst. 1); sken podepsané listiny místo originálu; označení nemovitosti mimo § 8 kat. z.; nenávazný řetězec zápisů (§ 17 odst. 1 písm. g)).
- **Nástroj:** `/pravni-sablony` (návrh na vklad); plná moc `/generuj-smlouvu` vzor `plna-moc` (vynutí ověřený podpis pro katastr).
- **Kontroly:** references/kontroly-podani.md
- **Eskalace:** zamítnutí nebo zastavení vkladového řízení, výzva katastru k doplnění u nestandardní listiny = advokát.

### N-06 Výmaz zástavního práva
- **Kdy:** prodávající splácí hypotéku z kupní ceny, nebo byl zajištěný dluh zaplacen a zástava v LV zůstala.
- **Klíčová ustanovení (ověřeno):** § 1376, § 1377, § 1379, § 1949 OZ; § 11 odst. 1 písm. d), § 14 a § 15 kat. z.
- **Co nesmí chybět:** vyčíslení zůstatku dluhu zástavním věřitelem k datu výplaty (číslo účtu, variabilní symbol, denní úrok); závazek věřitele vydat po zaplacení listinu potvrzující zánik zástavního práva (§ 1379 odst. 2 OZ) nebo kvitanci (§ 1949 OZ); kdo návrh na výmaz podá a kdy; u více zástav jejich pořadí (§ 1371 OZ).
- **Lhůty a rizika:** zánikem dluhu zástavní právo zaniká (§ 1376 OZ), ale z LV zmizí až výmazem. Věřitel má požádat o výmaz bez zbytečného odkladu (§ 1379 odst. 1); když zánik nepotvrdí, odpovídá za škodu (§ 1379 odst. 2). Výmaz je zápis vkladem (§ 11 odst. 1 kat. z.), tedy běží stejné vkladové řízení jako v N-05.
- **Časté chyby:** výplata bance bez písemného příslibu souhlasu s výmazem; vyčíslení k jinému dni, než kdy peníze dojdou; přehlédnuté zákazy zcizení a zatížení zapsané s hypotékou.
- **Nástroj:** `/pravni-sablony` (návrh na výmaz, žádost věřiteli o potvrzení zániku); výplata z úschovy U-04.
- **Kontroly:** references/kontroly-podani.md
- **Eskalace:** úschova, z níž se vyplácí bance i prodávajícímu, je úschova s více výplatami = nestandardní, draftuje advokát (references/eskalace.md). Soudcovské nebo exekutorské zástavní právo = vždy advokát.

### N-07 Služebnosti: služebnost bytu, užívací a požívací právo
- **Kdy:** zřízení práva cesty, inženýrských sítí, doživotního bydlení rodičů, užívání části pozemku; zrušení staré služebnosti.
- **Klíčová ustanovení (ověřeno):** § 1257, § 1260, § 1262, § 1283, § 1285, § 1297, § 1299, § 1300, § 560 OZ; § 7 odst. 3 a § 11 odst. 1 písm. c) kat. z.
- **Co nesmí chybět:** panující pozemek nebo oprávněná osoba; přesný rozsah (které místnosti, jaká část pozemku, při části pozemku geometrický plán); zda jde o užívací (§ 1283), nebo požívací právo s právem na plody a užitky (§ 1285); úplata, nebo bezúplatnost; doba (dožití, určitá doba, dosažení věku jiné osoby podle § 1300 odst. 2); kdo nese náklady údržby.
- **Lhůty a rizika:** služebnost k zapsané věci vzniká až zápisem (§ 1262 odst. 1 OZ). Služebnost bytu se bez dalšího vykládá jako užívání (§ 1297), ne požívání. Zrušení dohodou působí až výmazem (§ 1300 odst. 1).
- **Časté chyby:** „věcné břemeno bydlení" bez rozsahu a bez rozlišení užívání a požívání; chybí ujednání o nákladech; služebnost zřízená bez geometrického plánu na část pozemku.
- **Nástroj:** `/pravni-sablony` (smlouva o zřízení služebnosti, návrh na vklad N-05).
- **Eskalace:** služebnost jako součást darování v rodině (N-08) nebo spor o vydržení služebnosti = advokát.

### N-08 Darování nemovitosti s výhradou věcného břemene
- **Kdy:** rodiče převádějí byt nebo dům na děti a vyhrazují si doživotní bydlení.
- **Klíčová ustanovení (ověřeno):** § 2055, § 2057, § 2068, § 2072, § 1642, § 1660 odst. 2 OZ; § 591 OZ.
- **Co nesmí chybět:** písemná forma (§ 2057 odst. 1 OZ); přesné vymezení služebnosti podle N-07 ve stejné listině nebo souběžně; kdo platí energie, opravy a daň z nemovitých věcí; jak se má dar započítat mezi sourozenci (výslovné ujednání nebo pokyn zůstavitele).
- **Lhůty a rizika:** dárce může dar odvolat pro nouzi (§ 2068) nebo od smlouvy odstoupit pro nevděk (§ 2072). Dar nepominutelnému dědici v posledních třech letech před smrtí se započte na povinný díl (§ 1660 odst. 2). Je-li dárce dlužník, věřitel může bezúplatnému převodu z posledních dvou let odporovat (§ 591 OZ, viz E-13).
- **Časté chyby:** darování „aby to nepropadlo exekuci"; nevyřešené vztahy k ostatním dětem; služebnost zapsaná až po převodu, kdy nový vlastník už může jednat sám.
- **Nástroj:** `/pravni-sablony` (darovací smlouva s výhradou služebnosti, návrh na vklad).
- **Eskalace:** dárce má dluhy nebo exekuce, je nezletilý obdarovaný, nebo jde o dědické plánování (nepominutelní dědici) = STOP, advokát posoudí (references/eskalace.md).

### N-09 Spoluvlastnictví: zrušení a vypořádání
- **Kdy:** spoluvlastníci (sourozenci po dědictví, bývalí partneři) se chtějí rozejít, dohodou nebo soudem.
- **Klíčová ustanovení (ověřeno):** § 1140, § 1141, § 1143, § 1144, § 1147, § 1124 OZ; § 88 písm. b) o. s. ř.
- **Co nesmí chybět:** u dohody písemná forma a ujednání o způsobu vypořádání (§ 1141 OZ): rozdělení, prodej s rozdělením výtěžku, nebo převod na jednoho s vyplacením ostatních; výše a splatnost náhrady; zajištění náhrady (úschova); kdo nese poplatky a vklad. U žaloby návrh na konkrétní způsob vypořádání.
- **Lhůty a rizika:** nikdo nemůže být nucen ve spoluvlastnictví setrvat, ale nelze žádat v nevhodnou dobu nebo jen k újmě jiného (§ 1140 odst. 2). Soud věc dělí jen bez podstatného snížení hodnoty (§ 1144), jinak ji přikáže za náhradu nebo nařídí dražbu (§ 1147). Řízení o právech k nemovitosti patří soudu podle místa nemovitosti (§ 88 písm. b) o. s. ř.).
- **Časté chyby:** dohoda bez vypořádání (neúplná); náhrada splatná až po vkladu bez zajištění; přehlédnuté zástavy na podílech.
- **Nástroj:** `/pravni-sablony` (dohoda o zrušení a vypořádání, žaloba); výpočet poplatku a odměny `/pravni-vypocty`.
- **Kontroly:** references/kontroly-podani.md (u žaloby)
- **Eskalace:** spoluvlastník v exekuci nebo insolvenci, nezletilý spoluvlastník, sporná výše podílů = advokát.

### N-10 Společné jmění manželů při převodu
- **Kdy:** prodávající nebo kupující je ženatý či vdaná; převod po rozvodu; nemovitost koupená jedním manželem.
- **Klíčová ustanovení (ověřeno):** § 708, § 709, § 713, § 714, § 716, § 736, § 740, § 741, § 747 OZ.
- **Co nesmí chybět:** zjištění, zda nemovitost patří do SJM (nabytí za trvání manželství, výjimky § 709 odst. 1 OZ jako dar nebo dědictví jen jednoho); u prodeje z SJM jednají oba, nebo jeden se souhlasem druhého (§ 714 odst. 1); zda je v bytě nebo domě rodinná domácnost, a to i u výlučného vlastnictví jednoho manžela (§ 747); u koupě jedním manželem poučení, že věc zpravidla spadne do SJM; existence smlouvy o manželském majetkovém režimu (veřejná listina, § 716 odst. 2).
- **Lhůty a rizika:** jednání bez potřebného souhlasu je relativně neplatné, dovolat se může druhý manžel (§ 714 odst. 2). Dům nebo byt s rodinnou domácností, kterého je k bydlení rodiny nezbytně třeba, nesmí manžel ani jako jediný vlastník bez souhlasu druhého zcizit ani zatížit právem neslučitelným s bydlením, ledaže zajistí obdobné bydlení; jinak se druhý manžel může dovolat neplatnosti (§ 747 OZ). Po rozvodu se nevypořádané SJM řídí přiměřeně pravidly SJM (§ 736); nedojde-li do tří let k vypořádání ani k podání návrhu, nemovitosti jsou v podílovém spoluvlastnictví se stejnými podíly (§ 741 písm. b)).
- **Časté chyby:** v LV „SJM", ale ve smlouvě jen jeden manžel; prodej po rozvodu bez vypořádání; přehlédnutá smlouva o zúžení SJM.
- **Nástroj:** `/generuj-smlouvu` vzor `prevod-nemovitosti` (manželé jen omezeně, výstup zkontrolovat); jinak `/pravni-sablony`.
- **Eskalace:** rozvod, zúžení nebo zrušení SJM, nevypořádané SJM, nesouhlas manžela = STOP (references/eskalace.md: SJM komplikace).

### N-11 Vady při koupi nové jednotky od developera
- **Kdy:** klient převzal nový byt nebo dům a objevil vady; nebo připomínkuje developerskou smlouvu před podpisem.
- **Klíčová ustanovení (ověřeno):** § 2099, § 2106, § 2107, § 2112, § 2129 odst. 2 a 3 OZ; § 1814 písm. a) OZ.
- **Co nesmí chybět:** předávací protokol s vadami a výhradami; přesný popis každé vady a datum jejího zjištění; zvolené právo (oprava, sleva, odstoupení) a lhůta k odstranění; fotodokumentace; u revize smlouvy kontrola, zda developer neomezuje práva z vad.
- **Lhůty a rizika:** vadu oznamuj bez zbytečného odkladu (§ 2112 odst. 1); skrytou vadu stavby do 5 let od nabytí (§ 2129 odst. 2). U spotřebitele se vada projevená do dvou let považuje za existující při přechodu nebezpečí (§ 2129 odst. 3). Podstatné porušení dává volbu práv (§ 2106), nepodstatné jen opravu nebo slevu (§ 2107). Ujednání, které spotřebiteli práva z vad vylučuje nebo omezuje, je zneužívající (§ 1814 písm. a)).
- **Časté chyby:** reklamace bez volby práva; čekání na „výzvu developera"; podpis protokolu „bez vad" pod tlakem termínu.
- **Nástroj:** `/revize-smlouvy` (developerská smlouva); `/pravni-sablony` (oznámení vad, výzva); lhůty `/pravni-vypocty lhuta`; žaloba přes Z-05.
- **Eskalace:** konstrukční vady vyžadující znalce, odstoupení od smlouvy u financované koupě, developer v insolvenci = advokát.

### N-12 Realitní zprostředkování
- **Kdy:** klient podepisuje nebo podepsal smlouvu s realitní kanceláří, řeší provizi, výhradnost nebo výpověď.
- **Klíčová ustanovení (ověřeno):** § 2445, § 2446, § 2448, § 2450 OZ; § 4, § 9 až § 12, § 14 až § 19 ZRZ.
- **Co nesmí chybět:** písemná forma (§ 9 ZRZ); předmět, cena a provize (bez nich neplatnost, kterou může namítnout jen zájemce, § 10); výpis z KN ne starší 3 pracovních dnů ke dni uzavření (§ 11); informace o závadách (§ 12).
- **Lhůty a rizika:** bez předaného výpisu může zájemce do 14 dnů odstoupit (§ 11 odst. 3 ZRZ). U spotřebitele výpovědní doba nejvýše 1 měsíc (§ 18), zákaz směnky a šeku (§ 16), zákaz povinnosti uzavřít realitní smlouvu (§ 14). Provize je splatná nejdříve uzavřením realitní smlouvy (§ 19 odst. 1); dřívější splatnost jen s výslovným poučením ve smlouvě a nejdříve obstaráním příležitosti k uzavření realitní smlouvy (§ 19 odst. 2); záloha na provizi spotřebitele nejvýše dvě třetiny ujednané provize (§ 19 odst. 3). Zprostředkovatel činný v rozporu se smlouvou i pro druhou stranu ztrácí provizi (§ 2450 OZ).
- **Časté chyby:** realitní smlouva a smlouva o zprostředkování v jedné listině (§ 15 ZRZ); úschova nabízená realitkou (§ 4); klient tlačený k „advokátovi realitky" (ČAK výslovně uvádí právo svobodné volby advokáta, cak.cz/advokatni-uschovy).
- **Nástroj:** `/revize-smlouvy` (smlouva s RK); `/pravni-sablony` (výpověď, odstoupení, odpověď na výzvu k provizi).
- **Eskalace:** žaloba realitky o provizi nebo smluvní pokutu = Z- karty a advokát.

### N-13 Poznámka spornosti a žaloba o odstranění nesouladu zápisu
- **Kdy:** v katastru je zapsán stav, který neodpovídá skutečnosti (neplatná smlouva, podvodný převod), a klient potřebuje ochránit své právo.
- **Klíčová ustanovení (ověřeno):** § 985 a § 986 OZ; § 23 odst. 1 písm. o) a § 24 kat. z.; § 80 a § 88 písm. b) o. s. ř.
- **Co nesmí chybět:** tvrzení, proč zápis neodpovídá skutečnému stavu; volba cesty: podle § 985 OZ (a § 24 odst. 1 věty první kat. z.) se zápis provede, prokáže-li dotčený, že právo už uplatnil u soudu; podle § 986 OZ (zápis bez právního důvodu ve prospěch jiného, § 24 odst. 1 věta druhá kat. z.) stačí žádost o poznámku spornosti a uplatnění práva u soudu se doloží dodatečně; u určovací žaloby naléhavý právní zájem (§ 80 o. s. ř.).
- **Lhůty a rizika:** požádá-li dotčený o poznámku spornosti do 1 měsíce od dozvědění o zápisu, působí jeho právo vůči každému; později jen vůči tomu, kdo nebyl v dobré víře (§ 986 odst. 2 OZ). Katastr poznámku vymaže, nedoloží-li žadatel do 2 měsíců od doručení žádosti, že své právo uplatnil u soudu (§ 986 odst. 1). Při nevyrozumění se lhůta prodlužuje na 3 roky od zápisu (§ 986 odst. 3). Lhůty počítej jako hmotněprávní a žádost podávej s rezervou.
- **Časté chyby:** záměna § 985 a § 986 OZ (u § 985 musí být žaloba podána předem, u § 986 ji lze doložit do 2 měsíců); zmeškaná měsíční lhůta; zmeškaná dvouměsíční lhůta k doložení žaloby; žaloba u nesprávného soudu (výlučná příslušnost § 88 písm. b)).
- **Nástroj:** AI připraví jen podklad: chronologii, přehled zápisů a lhůt (`/pravni-vypocty lhuta --hmotnepravni`); rešerše `/hloubkovy-research`.
- **Kontroly:** references/kontroly-podani.md
- **Eskalace:** vždy. Sporná vlastnická struktura = STOP, nedraftovat (references/eskalace.md).

### N-14 Předkupní práva při prodeji
- **Kdy:** prodává se podíl, stavba na cizím pozemku, pozemek pod cizí stavbou, nebo je v LV zapsané předkupní právo.
- **Klíčová ustanovení (ověřeno):** § 1124, § 2128, § 2140, § 2143, § 2144, § 2147, § 2148, § 3056 OZ; § 11 odst. 1 písm. g) kat. z.
- **Co nesmí chybět:** zjištění zapsaných předkupních práv (část C LV); u podílu, jak spoluvlastnictví vzniklo (zákonné předkupní právo spoluvlastníka jen u spoluvlastnictví vzniklého bez vlivu stran, po dobu 6 měsíců od vzniku, § 1124 odst. 1); u staveb, které nejsou součástí pozemku, vzájemné předkupní právo vlastníka pozemku a stavby (§ 3056 odst. 1); nabídka předkupníkovi s ohlášením všech podmínek a obsahu smlouvy s kupujícím, u nemovitosti písemně (§ 2147 odst. 1).
- **Lhůty a rizika:** povinnost nabídnout dospívá uzavřením smlouvy s koupěchtivým (§ 2143), ne až převodem: nejdřív smlouva s kupujícím, pak nabídka, vklad až po vyjasnění, zda předkupník právo využije (jak smlouvu s kupujícím podmínit, posoudí advokát). Přijme-li předkupník nabídku, koupě se uskuteční za stejných podmínek (§ 2147 odst. 2); u nemovitosti zaplatí do 3 měsíců po nabídce, není-li ujednáno jinak, jinak předkupní právo zanikne (§ 2148 odst. 1). Věcné předkupní právo vzniká až zápisem (§ 2128 odst. 2) a působí i vůči nástupci (§ 2144 odst. 1). K ujednáním vylučujícím předkupní právo podle § 3056 se nepřihlíží; podle § 1124 odst. 2 se předkupní právo uplatní i při bezúplatném převodu za obvyklou cenu. Zda a jak se postup § 2143 až § 2148 použije u zákonného předkupního práva, potvrdí advokát.
- **Časté chyby:** prodej stavby bez nabídky vlastníkovi pozemku; nabídka bez obsahu smlouvy s kupujícím; vklad podaný dřív, než uplynula lhůta předkupníka; spoléhání na staré znění § 1124 (předkupní právo všech spoluvlastníků).
- **Nástroj:** `/pravni-sablony` (nabídka předkupního práva, prohlášení o jeho nevyužití); prověrka N-02.
- **Eskalace:** předkupní právo bylo opomenuto a převod už proběhl = advokát.

### N-15 Prodej bytové jednotky v domě se SVJ
- **Kdy:** převod bytu v domě rozděleném na jednotky; kupující se ptá na dluhy a fond oprav.
- **Klíčová ustanovení (ověřeno):** § 1186 OZ; § 23a odst. 5 kat. vyhl.; § 8 kat. z.
- **Co nesmí chybět:** potvrzení osoby odpovědné za správu domu (SVJ) o dluzích převodce na příspěvcích a zálohách, nebo že dluhy nejsou (§ 1186 odst. 3); prokazatelná žádost o potvrzení a doklad o jejím doručení; označení jednotky včetně podílu na společných částech; ujednání, kdo hradí příspěvky do dne převzetí; vazba výplaty z úschovy na doložení potvrzení.
- **Lhůty a rizika:** s jednotkou přecházejí na nabyvatele dluhy, které měl a mohl zjistit; převodce za ně SVJ ručí (§ 1186 odst. 2). SVJ nemá povinnost příspěvky při převodu vypořádat (§ 1186 odst. 1). Domněnka, že nabyvatel dluhy zjistit nemohl, platí jen tehdy, nešly-li zjistit z potvrzení, nebo když je osoba odpovědná za správu domu nevydala bez zbytečného odkladu, ač o ně byla požádána (§ 1186 odst. 3); samotné nedoložení potvrzení kupujícího nechrání.
- **Časté chyby:** smlouva podepsána bez potvrzení SVJ a bez dokladu o žádosti; ujednání o „vypořádání fondu oprav" s SVJ, které k tomu nemá povinnost.
- **Nástroj:** `/generuj-smlouvu` vzor `prevod-nemovitosti`; žádost o potvrzení `/pravni-sablony`; SVJ obecně viz katalog 03 (NJ-11 až NJ-13).
- **Eskalace:** spor s SVJ o výši dluhu, nevzniklé SVJ v nové výstavbě = advokát.

<!-- Origin: GrowLead ak-sladek v0.9, vlastní text katalogu úloh | Vytvořeno: 2026-10-16 | Ověřeno na zakonyprolidi.cz 2026-10-16: OZ § 560, 591, 708, 709, 713, 714, 716, 736, 740, 741, 980, 984, 985, 986, 1105, 1124, 1140, 1141, 1143, 1144, 1147, 1186, 1257, 1260, 1262, 1283, 1285, 1297, 1299, 1300, 1371, 1376, 1377, 1379, 1642, 1660, 1746, 1785, 1786, 1787, 1788, 1808, 1813, 1814, 1949, 2055, 2057, 2068, 2072, 2079, 2099, 2106, 2107, 2112, 2128, 2129, 2130, 2445, 2446, 2448, 2450, 3056; kat. z. § 6 až 11, 14 až 18, 23, 24, 25; kat. vyhl. § 23, 23a; o. s. ř. § 80, 88; ZRZ § 4, 9 až 12, 14 až 19; zák. 634/2004 položka 120; zák. 254/2004 § 4 | Review: Codex cross-family 2026-10-16, nálezy ověřeny v plném znění a zapracovány (N-01, N-04, N-10, N-12, N-13, N-14, N-15): OZ § 747, 2140, 2143, 2144, 2147, 2148, ZRZ § 19 | Inspiration: externí katalog právních úloh jen jako kontrolní seznam pokrytí (názvy), text vlastní; https://www.cak.cz/advokatni-uschovy -->
