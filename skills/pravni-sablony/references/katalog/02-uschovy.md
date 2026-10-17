# Katalog úloh 02: Advokátní úschovy (U-)

Úschova je místo, kde v realitní praxi nejvíc hrozí ztráta peněz klienta i kárná odpovědnost advokáta. Karty proto drží jen standardní postupy a u všeho mimo vzor kanceláře (více výplat, hypotéka, spor, cizinec) vedou k eskalaci. AI úschovu nikdy neprovádí ani nehlásí; připravuje smlouvy, kontrolní seznamy a podklady pro advokáta.

**Pozor na stará znění:** dřívější § 56a zákona o advokacii je zrušen. Úschovu upravuje od 1. 4. 2025 část desátá, § 52e až § 52n zákona č. 85/1996 Sb. ve znění zák. č. 73/2025 Sb.; Garanční fond (§ 29a) a hlášení identifikačních údajů stran do Elektronické knihy úschov platí od 1. 1. 2026. Stavovský předpis: usnesení představenstva ČAK č. 7/2004 Věstníku ve znění usnesení č. 7/2026 Věstníku (účinné od 30. 8. 2026). Vše ověřeno 16. 10. 2026 na zakonyprolidi.cz a cak.cz; před použitím zkontroluj, zda ČAK mezitím nevydala další změnu (cak.cz/advokatni-uschovy).

Eskalace: [`references/eskalace.md`](../../../../references/eskalace.md) (nestandardní úschova = okamžitá eskalace). Zkratky: ZA = zák. č. 85/1996 Sb., o advokacii; usnesení 7/2004 = usnesení představenstva ČAK č. 7/2004 Věstníku v platném znění; usnesení sněmu 5/2025 = usnesení sněmu ČAK č. 5/2025 Věstníku, o Garančním fondu; EKÚ = Elektronická kniha úschov; AML = zák. č. 253/2008 Sb.; ZRZ = zák. č. 39/2020 Sb.; NŘ = zák. č. 358/1992 Sb., notářský řád; ZŘS = zák. č. 292/2013 Sb.

## Obsah
- U-01 Smlouva o advokátní úschově kupní ceny
- U-02 Povinnosti před přijetím peněz do úschovy
- U-03 Výplatní podmínky vázané na list vlastnictví
- U-04 Úschova s výplatou zástavnímu věřiteli prodávajícího
- U-05 Úschova při financování hypotékou kupujícího
- U-06 Vrácení úschovy při nesplnění podmínek
- U-07 Rozporné pokyny stran a spor o vydání úschovy
- U-08 Úschova zálohy, rezervačního poplatku nebo závdavku
- U-09 Úschova listin
- U-10 Hlášení do EKÚ, Garanční fond a ukončení úschovy
- U-11 Zákaz hotovosti a platby mimo úschovu
- U-12 Notářská a soudní úschova, úschova přes realitní kancelář
- U-13 Protistrana v exekuci nebo insolvenci během úschovy
- U-14 Úschova s cizincem nebo platbou ze zahraničí

---

### U-01 Smlouva o advokátní úschově kupní ceny
- **Kdy:** převod nemovitosti, kupující skládá kupní cenu nebo doplatek na účet úschovy kanceláře, výplata prodávajícímu po vkladu.
- **Klíčová ustanovení (ověřeno):** § 52e, § 52g, § 52h odst. 2, § 52i ZA; čl. 1 odst. 1 a 3, čl. 2 odst. 2 usnesení 7/2004; § 2402 OZ.
- **Co nesmí chybět:** písemná forma (§ 52g odst. 1 ZA); jednoznačná identifikace složitele, výše a měna (čl. 1 odst. 3 usnesení 7/2004); číslo účtu označeného „advokátní úschova" (§ 52g odst. 2); výplatní podmínky (U-03) a lhůta výplaty; podmínky a účet pro vrácení (U-06); komu náleží úroky a na jaký účet (§ 52h odst. 2 písm. b)); kontaktní údaje stran pro notifikace banky a ČAK; odměna za úschovu (vždy smluvní, advokátní tarif ji neupravuje, cak.cz).
- **Lhůty a rizika:** bez jiného ujednání se vyplácí okamžitě nebo v nejbližším termínu banky (čl. 2 odst. 2). Advokát nakládá s penězi jen podle smlouvy (§ 52i odst. 1); odměnu si z úschovy smí vzít jen se souhlasem klienta, podle smlouvy nebo rozhodnutí (cak.cz). Jeden účet = jedna úschova, nová až po úplném vypořádání předchozí (§ 52g odst. 4, § 52i odst. 2). Úschova ve vlastní věci je zakázaná (§ 52g odst. 5).
- **Časté chyby:** výplata „po podpisu kupní smlouvy"; chybí účet pro vrácení; částka v úschově nesedí s doplatkem v kupní smlouvě (vzor to hlídá: `cena.doplatek` = `uschova.castka`).
- **Nástroj:** `/generuj-smlouvu` vzor `prevod-nemovitosti` (kupní smlouva a smlouva o úschově jako propojený pár).
- **Eskalace:** jiná struktura než vzor (hypotéka, více výplat, více složitelů, výplata třetí osobě) = nestandardní úschova, STOP (references/eskalace.md).

### U-02 Povinnosti před přijetím peněz do úschovy
- **Kdy:** od první schůzky do okamžiku, kdy kupující pošle peníze (AML identifikace podle steplistu ČAK předchází podpisu smlouvy o úschově).
- **Klíčová ustanovení (ověřeno):** § 52h, § 52j odst. 1 a 2 ZA; čl. 1 odst. 4, čl. 2 odst. 3, čl. 2b odst. 1 a 3, čl. 4 odst. 2 usnesení 7/2004; § 2 odst. 1 písm. g) AML; steplist ČAK (cak.cz/dokumenty-a-formulare/319).
- **Co nesmí chybět (v tomto pořadí):** (1) identifikace a kontrola klienta podle AML, kopie dokladů do spisu; (2) písemná informace složiteli a oprávněnému o povinnosti přijmout peníze jen na účet úschovy, o omezeních nakládání, o potvrzeních banky a o změně údajů (§ 52h odst. 1); (3) elektronické sdělení bance: kontakty stran a účty pro úroky (§ 52h odst. 2); (4) spotřebiteli údaje podle § 1811 odst. 2 OZ, případně § 1820 odst. 1 a § 1826 OZ, a poučení, že peníze kryje Fond pojištění vkladů, ne pojištění advokáta, a že spotřebitelské spory řeší ČAK (čl. 4 odst. 2); (5) hlášení úschovy do EKÚ včetně identifikačních údajů složitele i oprávněného (čl. 2b odst. 1), potvrzení do spisu; (6) po připsání identifikace skutečného vlastníka peněz vůči bance (čl. 2 odst. 3).
- **Lhůty a rizika:** banka pošle stranám potvrzení o vedení účtu (§ 52j odst. 1 a 2); nedostane-li ho klient, je to varovný signál. Složí-li kupující dřív, než advokát úschovu nahlásí, hlásí se bez zbytečného odkladu dodatečně včetně data přijetí (čl. 2b odst. 3). Bez nahlášených identifikačních údajů nemá klient nárok na náhradu z Garančního fondu (čl. 4 odst. 1 usnesení sněmu 5/2025).
- **Časté chyby:** překlep v kontaktu strany (notifikace jdou jinam); v EKÚ chybí údaje oprávněného; informace podle § 52h odeslaná až po připsání peněz.
- **Nástroj:** `/pravni-sablony` (písemná informace stranám, kontrolní seznam); KYC `/kontrola-podpis`, `/hloubkovy-research firma`.
- **Eskalace:** pochybnost o původu peněz nebo skutečném vlastníkovi, platba z účtu třetí osoby, politicky exponovaná osoba = STOP, advokát (AML).

### U-03 Výplatní podmínky vázané na list vlastnictví
- **Kdy:** sepisuješ nebo kontroluješ, kdy se kupní cena z úschovy uvolní prodávajícímu.
- **Klíčová ustanovení (ověřeno):** § 52i odst. 1 ZA; § 9, § 10, § 16 odst. 1, § 18 odst. 1 a 3 kat. z. (zák. č. 256/2013 Sb.); § 23 odst. 2 kat. vyhl. (vyhl. č. 357/2013 Sb.).
- **Co nesmí chybět:** rozhodný doklad (výpis z LV nebo vyrozumění katastru o provedeném vkladu, § 18 odst. 3 kat. z.) a kdo ho opatří; co musí výpis ukazovat: kupující v části A ve správném podílu, v částech C a D jen zápisy, se kterými smlouva počítá (typicky zástava banky kupujícího), zástavy prodávajícího vymazané nebo vypořádané podle U-04, žádná nevysvětlená plomba; lhůta k výplatě po splnění (v pracovních dnech); účet prodávajícího.
- **Lhůty a rizika:** vklad lze povolit nejdříve 20 dnů od odeslání informace vlastníkovi (§ 18 odst. 1 ve spojení s § 16 odst. 1 kat. z.); s tím počítej v termínech. Účinky zápisu se vážou k doručení návrhu (§ 10), výplata se ale váže na provedený zápis, ne na podání. Stranám doporuč službu sledování změn v katastru (§ 16 odst. 1).
- **Časté chyby:** výplata „po podání návrhu na vklad" (riziko zamítnutí); podmínka „LV bez jakéhokoli zatížení", když kupující zastavuje bance (podmínka se nikdy nesplní); chybí pravidlo pro zamítnutí vkladu (U-06).
- **Nástroj:** `/generuj-smlouvu` vzor `prevod-nemovitosti`; cizí smlouvu o úschově `/revize-smlouvy`; termíny `/pravni-vypocty lhuta`.
- **Eskalace:** podmínky mimo LV standard (kolaudace, souhlas třetí osoby, postupné výplaty) = nestandardní úschova (references/eskalace.md).

### U-04 Úschova s výplatou zástavnímu věřiteli prodávajícího
- **Kdy:** na prodávané nemovitosti vázne hypotéka a z kupní ceny se nejdřív splácí banka prodávajícího.
- **Klíčová ustanovení (ověřeno):** § 52i odst. 1 ZA; § 1376, § 1379, § 1949 OZ; § 11 odst. 1 kat. z.
- **Co nesmí chybět:** vyčíslení zůstatku dluhu k datu výplaty s pravidlem pro denní navýšení; účet a variabilní symbol banky; písemný závazek banky vydat po zaplacení potvrzení o zániku zástavního práva nebo souhlas s výmazem (§ 1379 odst. 2 OZ); pořadí výplat (banka, pak zbytek prodávajícímu); kdo a kdy podá návrh na výmaz (N-06); co když vyčíslení převýší kupní cenu.
- **Lhůty a rizika:** zástava zaniká zánikem dluhu (§ 1376 OZ), z LV ale zmizí až výmazem, který je vkladem (§ 11 odst. 1 kat. z.); věřitel má o výmaz požádat bez zbytečného odkladu (§ 1379 odst. 1 OZ). Riziko zapsané zástavy nesmí nést kupující: zbytek ceny prodávajícímu až po doložení souhlasu s výmazem nebo po výmazu.
- **Časté chyby:** celá cena prodávajícímu s ujištěním, že hypotéku doplatí sám; vyčíslení bez úroku do dne připsání; chybí kvitance (§ 1949 OZ).
- **Nástroj:** AI připraví jen podklad (rekapitulace částek, pořadí výplat, seznam listin); smlouvu sestaví advokát. Návrh na výmaz `/pravni-sablony`.
- **Eskalace:** více výplat z jedné úschovy = nestandardní úschova podle references/eskalace.md, AI nedraftuje.

### U-05 Úschova při financování hypotékou kupujícího
- **Kdy:** část ceny platí banka kupujícího z úvěru a zástavní právo pro ni se zapisuje souběžně s převodem.
- **Klíčová ustanovení (ověřeno):** § 1341, § 1371 odst. 1 OZ; § 9 odst. 2 a § 10 kat. z.; § 52g odst. 3 a § 52i ZA.
- **Co nesmí chybět:** podmínky čerpání banky (obvykle smlouva o úschově, podaný návrh na vklad zástavy, výpis z LV) sladěné s výplatními podmínkami úschovy; dva zdroje (vlastní prostředky kupujícího a úvěr) a osud každého při nezdaru obchodu; zástavní smlouva k věci, kterou zástavce teprve nabude (budoucí zástavní právo, § 1341 OZ); pořadí podání návrhů na vklad převodu a zástavy.
- **Lhůty a rizika:** budoucí zástavní právo vznikne nabytím vlastnictví zástavcem (§ 1341 odst. 2 OZ). Pořadí zástav určuje okamžik podání návrhu (§ 1371 odst. 1 OZ, § 9 odst. 2 kat. z.). Prodlení banky s čerpáním posouvá výplatu prodávajícímu.
- **Časté chyby:** výplatní podmínka bez místa pro zástavu banky kupujícího v části C; vrácení úvěrových peněz na účet kupujícího místo bance.
- **Nástroj:** vzor `prevod-nemovitosti` v0.1 hypoteční variantu nepokrývá (omezení uvedená v `/generuj-smlouvu`); zástavní smlouvu `/generuj-smlouvu` vzor `zastavni-smlouva-nemovitost` jen tam, kde ji nepřipravuje banka.
- **Eskalace:** vždy nestandardní úschova (více složitelů, podmínky banky) = STOP, advokát.

### U-06 Vrácení úschovy při nesplnění podmínek
- **Kdy:** vklad byl zamítnut, strana odstoupila, uplynula lhůta, kupní smlouva se neuzavřela.
- **Klíčová ustanovení (ověřeno):** § 52i odst. 1, § 52j odst. 3 a 4, § 52k odst. 4 ZA; § 16 odst. 2 a § 18 odst. 1 a 5 kat. z.; § 2993 OZ.
- **Co nesmí chybět (ve smlouvě předem):** výčet spouštěčů vrácení; jakým dokladem se prokazují (rozhodnutí o zamítnutí, doručené odstoupení, marné uplynutí data); účet pro vrácení; lhůta; osud úroků a nákladů; zda je třeba společný pokyn stran.
- **Lhůty a rizika:** vrací se jen podle smlouvy (§ 52i odst. 1), nikdy hotově (§ 52j odst. 3); banka stranám potvrdí převod (§ 52j odst. 4); po posledním převodu hlášení do EKÚ (§ 52k odst. 4). Proti zamítnutí vkladu lze do 30 dnů od doručení podat žalobu (§ 18 odst. 5 kat. z.); váže-li smlouva vrácení na zamítnutí, musí s touto lhůtou počítat. Zpětvzetí návrhu na vklad vyžaduje souhlas všech účastníků (§ 16 odst. 2 kat. z.). Plnění z odpadlého důvodu se vrací (§ 2993 OZ).
- **Časté chyby:** vrácení na pokyn jedné strany tam, kde smlouva chce obě; vrácení na jiný účet, než ze kterého peníze přišly, bez opory ve smlouvě.
- **Nástroj:** `/pravni-sablony` (oznámení stranám, výzva); termíny `/pravni-vypocty lhuta`.
- **Eskalace:** strany se přou, zda spouštěč nastal = U-07, STOP.

### U-07 Rozporné pokyny stran a spor o vydání úschovy
- **Kdy:** prodávající tvrdí splnění podmínek, kupující výplatu blokuje (nebo naopak), případně se k penězům hlásí třetí osoba.
- **Klíčová ustanovení (ověřeno):** § 52i odst. 1 ZA; § 1953 OZ; § 290, § 291, § 298 ZŘS; § 88 písm. d) o. s. ř.
- **Co nesmí chybět:** chronologie a doklady ke každé výplatní podmínce; doslovná citace podmínek ze smlouvy; korespondence stran; stav účtu. AI připraví jen tento podklad.
- **Lhůty a rizika:** advokát nesmí spor rozhodnout sám mimo smlouvu (§ 52i odst. 1). Zákon zná soudní úschovu, je-li dlužník bez své viny v nejistotě, kdo je věřitelem (§ 1953 odst. 1 OZ, řízení podle § 290 a násl. ZŘS); vydání pak vyžaduje souhlas všech dotčených nebo rozhodnutí (§ 298 odst. 1 ZŘS), spor o souhlas patří soudu, u něhož běží řízení o úschovách (§ 88 písm. d) o. s. ř.). Zda a jak tento postup použít u advokátní úschovy, posoudí advokát.
- **Časté chyby:** výplata podle toho, kdo naléhá víc; mlčení vůči stranám bez písemného stanoviska.
- **Nástroj:** `/posouzeni-rizika`, `/priprava-jednani`; rešerše `/hloubkovy-research`.
- **Eskalace:** vždy a okamžitě.

### U-08 Úschova zálohy, rezervačního poplatku nebo závdavku
- **Kdy:** předkupní fáze: rezervace, smlouva o smlouvě budoucí, záloha developerovi.
- **Klíčová ustanovení (ověřeno):** § 52g a § 52k ZA; § 1808 OZ; § 4 ZRZ; čl. 3 odst. 2 usnesení sněmu 5/2025.
- **Co nesmí chybět:** vazba na hlavní smlouvu (označení, datum, strany); osud zálohy ve všech scénářích a její započtení na cenu; rozlišení zálohy a závdavku; samostatný účet i pro malou částku (jeden účet = jedna úschova).
- **Lhůty a rizika:** závdavek musí být odevzdán nejpozději při uzavření smlouvy (§ 1808 odst. 1 OZ); zda složení do úschovy je „odevzdáním" závdavku, posoudí advokát. Každá úschova se hlásí do EKÚ a nese odvod 500 Kč do Garančního fondu (čl. 3 odst. 2 usnesení sněmu 5/2025). Realitní zprostředkovatel úschovu nabízet nesmí a zprostředkovat ji smí jen u banky (i pobočky zahraniční banky), notáře nebo advokáta; soudní exekutor připadá v úvahu jen v souvislosti s exekučním, soudním nebo jiným řízením, ne jako běžná alternativa (§ 4 odst. 1 ZRZ).
- **Časté chyby:** převod zálohy z jedné úschovy do druhé bez ujednání; závdavek splatný až po podpisu.
- **Nástroj:** `/generuj-smlouvu` vzory `smlouva-o-smlouve-budouci-kupni` (gate na typ a výši zálohy či závdavku) a `rezervacni-smlouva`; smlouva o úschově zálohy obdobně podle U-01.
- **Eskalace:** postupné platby developerovi z jedné úschovy = nestandardní úschova.

### U-09 Úschova listin
- **Kdy:** podepsané vkladové listiny nemají odejít na katastr, dokud kupující nesloží cenu; banka svěřuje souhlas s výmazem do rukou advokáta.
- **Klíčová ustanovení (ověřeno):** čl. 3 a čl. 4 odst. 1 usnesení 7/2004; § 2402 a § 2403 OZ; § 84 NŘ (srovnání s notářskou úschovou listin).
- **Co nesmí chybět:** soupis listin (stejnopisy, ověřené podpisy); podmínky použití (podání návrhu na vklad advokátem) nebo vydání; komu se vydávají (bez jiného ujednání jen klientovi nebo jeho zástupci, čl. 3 odst. 2); uložení v bezpečnostní schránce nebo jinak přiměřeně bezpečně (čl. 3 odst. 1); plná moc k podání návrhu na vklad.
- **Lhůty a rizika:** hlášení do EKÚ se týká peněžních prostředků (§ 52k ZA), dokumentaci o nakládání ale vést musíš (čl. 4 odst. 1). Uschovatel může podle OZ žádat vrácení i před uplynutím doby (§ 2403 odst. 2 OZ); kdy má být úschova pro stranu nevratná, musí výslovně říct smlouva a posoudit advokát.
- **Časté chyby:** listiny „leží u advokáta" bez písemných podmínek; chybí plná moc k podání návrhu.
- **Nástroj:** `/pravni-sablony` (smlouva o úschově listin, protokol o převzetí); `/generuj-smlouvu` vzor `plna-moc`.
- **Eskalace:** požadavek jedné strany vydat listiny proti vůli druhé = U-07.

### U-10 Hlášení do EKÚ, Garanční fond a ukončení úschovy
- **Kdy:** u každé peněžní úschovy, od založení po uzavření spisu.
- **Klíčová ustanovení (ověřeno):** § 29a a § 52k ZA; § 52g odst. 1 ve spojení s § 52f odst. 3 ZA; čl. 2a a čl. 2b usnesení 7/2004; čl. 3, čl. 4, čl. 5 a čl. 9 odst. 3 usnesení sněmu 5/2025.
- **Co nesmí chybět:** tři kroky v EKÚ: (1) před přijetím peněz údaje podle § 52k odst. 3 písm. a), b), d) ZA, spisová značka a identifikační údaje složitele i oprávněného (čl. 2b odst. 1); (2) po přijetí datum přijetí, u opakovaných plateb jen první (§ 52k odst. 3 písm. c) ZA, čl. 2b odst. 2); (3) po ukončení datum posledního převodu (§ 52k odst. 4). Potvrzení EKÚ do spisu.
- **Lhůty a rizika:** hlášení po přijetí i po ukončení „bez zbytečného odkladu". Komora posílá stranám potvrzení o záznamu, změně a ukončení (§ 52k odst. 5). Garanční fond hradí škodu z trestné činnosti advokáta do 2,5 mil. Kč na úschovu, u kupní ceny nemovitosti sloužící k bydlení podle katastru do 5 mil. Kč (§ 29a odst. 2 ZA, čl. 5 odst. 1 usnesení sněmu 5/2025); jen u úschov přijatých po 31. 12. 2025 (čl. 9 odst. 3) a jen když advokát nahlásil identifikační údaje (čl. 4 odst. 1). Odvod 500 Kč za každou nahlášenou úschovu (čl. 3 odst. 2). Úschovu, na kterou nic nepřišlo, advokát v EKÚ zruší bez odvodu (cak.cz). Smlouvu a listiny uchovej 10 let od ukončení (§ 52f odst. 3 ZA).
- **Časté chyby:** hlášení až po připsání peněz; hlášení každé dílčí platby; v EKÚ neukončená úschova, přestože účet je prázdný.
- **Nástroj:** kontrolní seznam `/pravni-sablony`; EKÚ se obsluhuje přes Portál ČAK, AI do něj nezasahuje.
- **Eskalace:** zpětně zjištěná nenahlášená nebo neukončená úschova = advokát (kárné riziko).

### U-11 Zákaz hotovosti a platby mimo úschovu
- **Kdy:** klient chce část ceny „na ruku", zálohu v hotovosti nebo vložit hotovost na účet úschovy.
- **Klíčová ustanovení (ověřeno):** § 52g odst. 3 a § 52j odst. 3 ZA; § 3 odst. 1 a § 4 zák. č. 254/2004 Sb., o omezení plateb v hotovosti.
- **Co nesmí chybět:** platby do úschovy jen bezhotovostně nebo vkladem u banky, který provádí vždy klient, nikdy advokát (§ 52g odst. 3 ZA, cak.cz); u plateb mimo úschovu kontrola limitu a jejich promítnutí do kupní smlouvy.
- **Lhůty a rizika:** banka neumožní vklad ani výběr hotovosti advokátem (§ 52j odst. 3 ZA). Platbu přesahující 270 000 Kč nelze provést ani přijmout v hotovosti (§ 4 odst. 1 a 2 zák. č. 254/2004 Sb.); platby téhož plátce téže osobě v jednom dni se sčítají (§ 4 odst. 4). Hotovost ve větším rozsahu je i AML signál.
- **Časté chyby:** struktura vzoru „záloha v hotovosti před podpisem" použitá i pro zálohu nad limit; dělení hotovosti do více dnů (zda jde o obcházení zákona, posoudí advokát).
- **Nástroj:** kontrola při `/generuj-smlouvu` vzor `prevod-nemovitosti` (výši hotovostní zálohy porovnej s limitem ručně).
- **Eskalace:** požadavek na hotovost nad limit nebo platby přes třetí osoby = STOP, advokát.

### U-12 Notářská a soudní úschova, úschova přes realitní kancelář
- **Kdy:** protistrana nebo realitka navrhuje jiného schovatele, nebo klient srovnává možnosti.
- **Klíčová ustanovení (ověřeno):** § 86, § 87, § 89a NŘ; § 1953 OZ a § 290 až § 298 ZŘS; § 4 ZRZ; § 29a ZA.
- **Co nesmí chybět (srovnání pro advokáta):** notářská úschova peněz vzniká na žádost s identifikací složitele a příjemce a sepisuje se o ní protokol (§ 86, § 87 NŘ); do vydání peníze náleží složiteli, není-li v protokolu jinak (§ 89a odst. 1 NŘ). Soudní úschova je náhradní splnění z důvodů na straně věřitele (§ 1953 OZ, § 291 odst. 2 ZŘS) a jen pro peníze, cenné papíry a movité věci (§ 290 ZŘS); pro převod se nehodí. Realitní zprostředkovatel smí úschovu poskytnout jen na písemnou žádost zájemce na samostatné listině, na samostatném účtu a s evidencí úschov (§ 4 odst. 2 ZRZ).
- **Lhůty a rizika:** Garanční fond ČAK kryje jen úschovy advokátů (§ 29a ZA); u realitní úschovy tato ochrana není.
- **Časté chyby:** realitka „zařídí úschovu" bez písemné žádosti na samostatné listině; klient tlačený k advokátovi realitky (ČAK zdůrazňuje svobodnou volbu advokáta, cak.cz).
- **Nástroj:** `/revize-smlouvy` (cizí smlouva o úschově); `/pravni-sablony` (srovnání pro klienta).
- **Eskalace:** protistrana trvá na úschově mimo advokáta s nestandardními podmínkami = advokát.

### U-13 Protistrana v exekuci nebo insolvenci během úschovy
- **Kdy:** nová prověrka nebo notifikace ukáže exekuci či insolvenci prodávajícího nebo kupujícího mezi podpisem a výplatou.
- **Klíčová ustanovení (ověřeno):** § 44a odst. 1 zák. č. 120/2001 Sb. (EŘ); § 109 odst. 1, § 111 odst. 1 a § 419 odst. 3 zák. č. 182/2006 Sb. (IZ); § 25 kat. z.
- **Co nesmí chybět:** přesné časy (doručení vyrozumění o zahájení exekuce, zahájení insolvenčního řízení, rozhodnutí o úpadku) proti datům podpisu, složení peněz a podání návrhu na vklad; výpis z insolvenčního rejstříku (veřejný, § 419 odst. 3 IZ); poznámky k osobě v LV (§ 25 kat. z.).
- **Lhůty a rizika:** po doručení vyrozumění o zahájení exekuce povinný nesmí nakládat s majetkem; jednání je neplatné, namítne-li to exekutor, oprávněný nebo přihlášený věřitel (§ 44a odst. 1 EŘ). Od zahájení insolvenčního řízení se dlužník musí zdržet podstatných dispozic s majetkovou podstatou (§ 111 odst. 1 IZ). Výplata podle smlouvy může v takové situaci škodit klientovi i advokátovi.
- **Časté chyby:** výplata bez nové prověrky těsně před výplatou.
- **Nástroj:** prověrka `/hloubkovy-research firma` a N-02; AI jen shrne situaci.
- **Eskalace:** vždy STOP (references/eskalace.md: exekuce nebo insolvence na LV, insolvence protistrany).

### U-14 Úschova s cizincem nebo platbou ze zahraničí
- **Kdy:** složitel nebo oprávněný je zahraniční osoba, peníze přicházejí z ciziny nebo v cizí měně, výplata míří do zahraničí.
- **Klíčová ustanovení (ověřeno):** § 2 odst. 1 písm. g) AML; čl. 1 odst. 3 a 4 a čl. 2b odst. 1 písm. c) usnesení 7/2004; § 3 odst. 1 písm. b) a § 4 odst. 3 zák. č. 254/2004 Sb.
- **Co nesmí chybět:** identifikace podle AML; pro EKÚ u osoby bez rodného čísla datum a místo narození, pobyt a státní občanství (čl. 2b odst. 1 písm. c) bod 1); měna úschovy (čl. 1 odst. 3); kdo nese kurzové riziko a bankovní poplatky; doklad o původu prostředků.
- **Lhůty a rizika:** cizí prvek může přinést cizí právo, sankční a devizová omezení a delší AML kontrolu; vše posoudí advokát.
- **Časté chyby:** úschova v CZK, platba v EUR bez ujednání o kurzu; výplata na zahraniční účet bez ověření majitele.
- **Nástroj:** AI připraví jen seznam potřebných údajů a dokladů; prověrka `/hloubkovy-research`.
- **Eskalace:** cizinecký prvek = STOP (references/eskalace.md).

<!-- Origin: GrowLead ak-sladek v0.9, vlastní text katalogu úloh | Vytvořeno: 2026-10-16 | Ověřeno 2026-10-16: zák. 85/1996 ve znění k 1. 1. 2026 (verze 36) § 21, 29a, 52e až 52n, přechodná ustanovení zák. 73/2025 (účinnost 1. 4. 2025, § 29a od 1. 1. 2026), https://www.zakonyprolidi.cz/cs/1996-85, https://www.zakonyprolidi.cz/cs/2025-73; usnesení představenstva ČAK č. 7/2004 Věstníku ve znění č. 7/2026 (čl. 1, 2, 2a, 2b, 3, 4), https://www.cak.cz/dokumenty-a-formulare/352; usnesení sněmu ČAK č. 5/2025 Věstníku o Garančním fondu (čl. 3, 4, 5, 9), https://www.cak.cz/cs/download/Garan%C4%8Dn%C3%AD%20fond.pdf; steplist ČAK https://www.cak.cz/dokumenty-a-formulare/319; https://www.cak.cz/advokatni-uschovy; https://advokatnidenik.cz/2026/01/13/povinnosti-advokata-pri-provadeni-uschov-podle-nove-pravni-a-stavovske-upravy/; OZ § 1341, 1371, 1376, 1379, 1808, 1949, 1953, 2402, 2403, 2993; kat. z. § 9, 10, 11, 16, 18, 25; kat. vyhl. § 23; ZRZ § 4; NŘ § 84, 86, 87, 89a; ZŘS § 290 až 298; o. s. ř. § 88; EŘ § 44a; IZ § 109, 111, 419; AML § 2; zák. 254/2004 § 3, 4 | Review: Codex cross-family 2026-10-16, zapracováno U-08 (ZRZ § 4 odst. 1 písm. b)) | Inspiration: externí katalog právních úloh jen jako kontrolní seznam pokrytí (názvy), text vlastní -->
