# Katalog úloh 03: Nájem a společenství vlastníků (NJ-)

Nájem bytu je ve prospěch nájemce z velké části kogentní, a proto se v něm nejčastěji chybuje formou: chybějící poučení, výpověď bez předchozí výzvy, jistota nad limit. Karty pokrývají nájem bytu i prostoru sloužícího podnikání, ukončení nájmu a navazující spory a k tomu správu domu přes SVJ. U podání vždy projdi kontroly podání; výpočty lhůt a úroků dělá skript, ne model.

Ustanovení v řádcích „Klíčová ustanovení" jsou ověřena v plném znění na zakonyprolidi.cz ke dni 16. 10. 2026. Do podání je cituj až po ověření znění k rozhodnému dni přes DirectCase. Eskalace: [`references/eskalace.md`](../../../../references/eskalace.md). Kontroly podání: [`references/kontroly-podani.md`](../../../../references/kontroly-podani.md).

Zkratky: OZ = zák. č. 89/2012 Sb.; zák. 67/2013 = zák. č. 67/2013 Sb., o službách spojených s užíváním bytů; o. s. ř. = zák. č. 99/1963 Sb.; EŘ = zák. č. 120/2001 Sb.; IZ = zák. č. 182/2006 Sb.

## Obsah
- NJ-01 Nájemní smlouva k bytu
- NJ-02 Nájem prostoru sloužícího podnikání
- NJ-03 Výzva nájemci
- NJ-04 Výpověď nájmu bytu pronajímatelem s výpovědní dobou
- NJ-05 Výpověď nájmu bytu bez výpovědní doby
- NJ-06 Návrh nájemce na přezkoumání výpovědi
- NJ-07 Jistota u nájmu bytu
- NJ-08 Nájemné a služby: zvýšení a vyúčtování
- NJ-09 Vyklizení bytu a dluhy po skončení nájmu
- NJ-10 Konec nájmu na dobu určitou a výpověď nájemce
- NJ-11 SVJ: příspěvky, zálohy a vymáhání dluhů
- NJ-12 SVJ: shromáždění a rozhodování
- NJ-13 SVJ: napadení rozhodnutí shromáždění přehlasovaným vlastníkem

---

### NJ-01 Nájemní smlouva k bytu
- **Kdy:** pronájem bytu nebo domu k zajištění bytových potřeb (ne k rekreaci nebo jinému zjevně krátkodobému účelu, § 2235 odst. 2 OZ).
- **Klíčová ustanovení (ověřeno):** § 2235, § 2236, § 2237, § 2239, § 2248, § 2249, § 2251, § 2254, § 2285 OZ; zák. 67/2013.
- **Co nesmí chybět:** písemná forma (§ 2237; neplatnost pro vadu formy nemůže namítnout pronajímatel); přesné označení bytu a příslušenství; doba (určitá s konečným dnem, nebo neurčitá); nájemné a splatnost (předem, nejpozději do 5. dne platebního období, § 2251 odst. 1); služby, zálohy a způsob rozúčtování; zda se sjednává každoroční zvyšování (§ 2248), jinak jen postup § 2249; jistota a smluvní pokuty; předávací protokol.
- **Lhůty a rizika:** k ujednáním zkracujícím práva nájemce se nepřihlíží (§ 2235 odst. 1), stejně jako ke zjevně nepřiměřeným povinnostem (§ 2239). Jistota a smluvní pokuty dohromady nesmí přesáhnout trojnásobek měsíčního nájemného (§ 2254 odst. 1). Jiná plnění než nájemné a služby, ani ve formě „vkladu", pronajímatel požadovat nesmí (§ 2251 odst. 2).
- **Časté chyby:** jistota v limitu, ale smluvní pokuty limit přetáhnou; „vratný poplatek" mimo jistotu; doba určitá bez konečného data; přehlédnutá obnova nájmu podle § 2285 (NJ-10).
- **Nástroj:** `/generuj-smlouvu` vzor `najemni-smlouva-byt` + předávací protokol (gate: jistota nad 3 násobek nájemného, doba určitá bez konce, chybí nájemné); cizí smlouvu `/revize-smlouvy`.
- **Eskalace:** služební byt (§ 2297 OZ), cizinecký prvek, nezletilý nebo opatrovanec jako strana = advokát (references/eskalace.md).

### NJ-02 Nájem prostoru sloužícího podnikání
- **Kdy:** kancelář, obchod, sklad nebo provozovna, kde prostor slouží alespoň převážně podnikání (§ 2302 odst. 1 OZ).
- **Klíčová ustanovení (ověřeno):** § 1 odst. 2, § 2227, § 2228, § 2229, § 2232, § 2302, § 2303, § 2305, § 2307, § 2308, § 2309, § 2310, § 2312, § 2314, § 2315 OZ.
- **Co nesmí chybět:** účel nájmu; doba; nájemné a služby (pravidla služeb u bytů platí obdobně, § 2303); označení provozovny štíty (§ 2305: mlčí-li pronajímatel měsíc po písemné žádosti, souhlas je dán); převod nájmu se souhlasem v písemné formě (§ 2307 odst. 1); smluvní výpovědní důvody a výpovědní doby (jinak nájem na dobu určitou smluvně vypovědět nelze, § 2229).
- **Lhůty a rizika:** u výpovědi postupuj v pořadí: nejdřív smlouva (ujednané důvody a doby, § 2229, § 1 odst. 2), pak zvláštní zákonné důvody pro dobu určitou podle § 2308 (nájemce) a § 2309 (pronajímatel, mimo jiné prodlení s nájemným nebo službami delší než měsíc), u nichž musí být důvod ve výpovědi a výpovědní doba je tříměsíční (§ 2310), a nakonec obecné důvody výpovědi bez výpovědní doby (nepoužitelnost věci § 2227, marná výzva podle § 2228, zvlášť závažné porušení se značnou újmou § 2232). Tříměsíční dobu podle § 2310 nezobecňuj na smluvní výpovědi. Na dobu neurčitou 6 měsíců, s vážným důvodem 3 měsíce, po nájmu delším než 5 let za podmínek § 2312 vždy 6. Námitky do 1 měsíce od doručení výpovědi, jinak právo na přezkum zaniká; soudní přezkum do 2 měsíců od marného uplynutí lhůty ke zpětvzetí (§ 2314). Při výpovědi pronajímatelem náleží nájemci náhrada za převzetí zákaznické základny, ne při hrubém porušení (§ 2315).
- **Časté chyby:** použití pravidel nájmu bytu; výpověď doby určité bez smluvního i zákonného důvodu; tříměsíční výpovědní doba použitá tam, kde smlouva určuje jinou; zmeškané měsíční námitky.
- **Nástroj:** `/pravni-sablony` (smlouva, výpověď, námitky); `/revize-smlouvy`; lhůty `/pravni-vypocty lhuta`.
- **Kontroly:** references/kontroly-podani.md (u návrhu na přezkum výpovědi)
- **Eskalace:** spor o náhradu za zákaznickou základnu, převod nájmu spolu s převodem podnikání = advokát.

### NJ-03 Výzva nájemci
- **Kdy:** nájemce dluží nájemné nebo služby, poškozuje byt, obtěžuje ostatní nebo užívá byt jinak, než bylo ujednáno.
- **Klíčová ustanovení (ověřeno):** § 2251, § 2288 odst. 1 písm. a), § 2291 odst. 2 a 3 OZ.
- **Co nesmí chybět:** přesný popis porušení (u dluhu měsíce, částky a součet); přiměřená lhůta k nápravě; upozornění na možnost výpovědi; způsob doručení, který půjde prokázat.
- **Lhůty a rizika:** k výpovědi bez výpovědní doby, které nepředcházela výzva k odstranění závadného chování nebo protiprávního stavu, se nepřihlíží (§ 2291 odst. 3). Výpověď posílej až po marném uplynutí lhůty z výzvy.
- **Časté chyby:** výzva bez dokladu o doručení; nepřiměřeně krátká lhůta; výzva a výpověď v jednom dopise.
- **Nástroj:** `/generuj-smlouvu` vzor `vyzva-najemci` (gate: výčet dluhu, součet, lhůta); úrok z prodlení `/pravni-vypocty urok`.
- **Eskalace:** spor o výši dluhu, nájemce v insolvenci (E-12) = advokát.

### NJ-04 Výpověď nájmu bytu pronajímatelem s výpovědní dobou
- **Kdy:** pronajímatel má důvod podle § 2288 OZ (hrubé porušení, odsouzení za úmyslný trestný čin vůči pronajímateli nebo v domě, veřejný zájem, jiný obdobně závažný důvod; u doby neurčité i potřeba bytu pro sebe nebo příbuzné).
- **Klíčová ustanovení (ověřeno):** § 2286, § 2288, § 2290, § 605 a § 607 OZ.
- **Co nesmí chybět:** písemná forma a dojití výpovědi (§ 2286 odst. 1); konkrétní výpovědní důvod ve výpovědi (§ 2288 odst. 3); poučení o právu vznést námitky a navrhnout soudní přezkum, jinak je výpověď neplatná (§ 2286 odst. 2).
- **Lhůty a rizika:** výpovědní doba 3 měsíce běží od prvního dne měsíce následujícího po dojití (§ 2286 odst. 1, § 2288 odst. 1). Je to doba, ne lhůta: posun konce ze soboty, neděle nebo svátku se podle § 607 OZ týká jen lhůt. Důvody podle § 2288 odst. 2 jen u nájmu na dobu neurčitou. Nájemce má 2 měsíce od dojití na návrh soudu (§ 2290).
- **Časté chyby:** chybějící poučení; důvod opsaný ze zákona bez skutkového popisu; výpověď odeslaná, ale nedoručená.
- **Nástroj:** `/pravni-sablony` (výpověď s poučením). Konec výpovědní doby urči ručně (poslední den třetího měsíce běhu) a nech potvrdit advokátem; `/pravni-vypocty lhuta` počítá lhůty, ne doby.
- **Eskalace:** výpověď pro „jiný obdobně závažný důvod" (§ 2288 odst. 1 písm. d)) = vždy úvaha advokáta.

### NJ-05 Výpověď nájmu bytu bez výpovědní doby
- **Kdy:** nájemce porušuje povinnost zvlášť závažně: zejména dluh na nájemném a službách za alespoň 3 měsíce, závažné poškozování bytu nebo domu, závažné obtíže ostatním, neoprávněné užívání k jinému účelu (§ 2291 odst. 2 OZ).
- **Klíčová ustanovení (ověřeno):** § 2286, § 2290, § 2291 OZ.
- **Co nesmí chybět:** předchozí výzva a marné uplynutí lhůty v ní (NJ-03); ve výpovědi, v čem je zvlášť závažné porušení; požadavek odevzdat byt; poučení o námitkách a soudním přezkumu (§ 2286 odst. 2); písemná forma a doručení.
- **Lhůty a rizika:** nájem končí, jakmile výpověď dojde (§ 2286 odst. 1 ve spojení s § 2291 odst. 1); byt má nájemce odevzdat bez zbytečného odkladu, nejpozději do 1 měsíce od skončení nájmu (§ 2291 odst. 1). Bez výzvy nebo bez uvedení porušení se k výpovědi nepřihlíží (§ 2291 odst. 3). Nájemce může do 2 měsíců navrhnout přezkum (§ 2290).
- **Časté chyby:** dluh kratší než 3 měsíce; výpověď odeslaná před uplynutím lhůty z výzvy; chybí poučení.
- **Nástroj:** `/generuj-smlouvu` vzor `vypoved-najmu-bez-vypovedni-doby` (gate: dluh pod 3 měsíce, chybí výzva nebo její dojití, lhůta z výzvy neuplynula; poučení podle § 2286 a § 2290 je v textu vždy).
- **Eskalace:** spor o doručení výzvy nebo výši dluhu, nájemce odmítá byt vyklidit (NJ-09) = advokát.

### NJ-06 Návrh nájemce na přezkoumání výpovědi
- **Kdy:** klient je nájemce bytu a dostal výpověď.
- **Klíčová ustanovení (ověřeno):** § 2286 odst. 2, § 2288 odst. 3, § 2290, § 2291 odst. 3, § 607 OZ; § 79 o. s. ř.
- **Co nesmí chybět:** výpověď a doklad, kdy došla; argumenty: chybí poučení (neplatnost, § 2286 odst. 2), chybí nebo je neurčitý důvod (§ 2288 odst. 3, § 2291 odst. 3), nepředcházela výzva, tvrzený důvod nenastal; důkazy; petit (přesné znění posoudí advokát).
- **Lhůty a rizika:** 2 měsíce ode dne, kdy výpověď došla (§ 2290). Lhůta je hmotněprávní: návrh musí soudu dojít, odeslání nestačí (kontroly-podani.md, blok 3); podávej s rezervou. Konec lhůty na sobotu, neděli nebo svátek se posouvá na nejbližší pracovní den (§ 607 OZ).
- **Časté chyby:** počítání od data na výpovědi místo od dojití; čekání na výsledek jednání s pronajímatelem.
- **Nástroj:** `/pravni-sablony` (návrh); lhůta `/pravni-vypocty lhuta --jednotka mesice --hmotnepravni`; judikaturu jen ověřenou přes `/hloubkovy-research`.
- **Kontroly:** references/kontroly-podani.md
- **Eskalace:** lhůta končí do 14 dnů = výrazné upozornění nahoře a advokát hned.

### NJ-07 Jistota u nájmu bytu
- **Kdy:** sjednání, vrácení nebo započtení jistoty; spor o odečty při skončení nájmu.
- **Klíčová ustanovení (ověřeno):** § 2254, § 1982, § 1987 OZ; § 140 odst. 2 IZ.
- **Co nesmí chybět:** výše (spolu se smluvními pokutami nejvýše trojnásobek měsíčního nájemného, § 2254 odst. 1); kdy a na jaký účet se vrací; jaké pohledávky z nájmu se započtou a jak se doloží; úroky z jistoty.
- **Lhůty a rizika:** při skončení nájmu pronajímatel jistotu vrátí a započte si, co mu nájemce z nájmu dluží (§ 2254 odst. 2); započíst nelze pohledávku nejistou nebo neurčitou (§ 1987 odst. 2). Nájemce má právo na úroky z jistoty od jejího poskytnutí alespoň ve výši zákonné sazby (§ 2254 odst. 2); kterou sazbu použít, nech potvrdit advokátem. V insolvenci nájemce je započtení jistoty přípustné za podmínek § 140 odst. 2 IZ.
- **Časté chyby:** jistota zadržená „na budoucí vyúčtování" bez vyčíslení; úroky se nepřipočtou; jistota nad limit vybraná jako „záloha na škody".
- **Nástroj:** vzor `najemni-smlouva-byt` (gate na limit); vyúčtování jistoty `/pravni-sablony`; úroky `/pravni-vypocty`.
- **Eskalace:** nájemce v insolvenci, nárok na škody přesahující jistotu = advokát.

### NJ-08 Nájemné a služby: zvýšení a vyúčtování
- **Kdy:** pronajímatel chce zvýšit nájemné; spor o vyúčtování služeb (teplo, voda, výtah, úklid); obdobně mezi SVJ a vlastníkem jednotky.
- **Klíčová ustanovení (ověřeno):** § 2248, § 2249, § 2251, § 2252 OZ; § 7, § 8, § 13 zák. 67/2013.
- **Co nesmí chybět:** u zvýšení podle § 2249 písemný návrh s novou výší a doložením podmínek (srovnatelné nájemné); u vyúčtování členění podle služeb, celkové přijaté zálohy a rozdíl (§ 7 odst. 2 zák. 67/2013).
- **Lhůty a rizika:** bez ujednání o zvyšování lze navrhnout zvýšení nejvýše do srovnatelného nájemného obvyklého v místě a o nejvýše 20 % za 3 roky, ne dříve než po 12 měsících bez zvýšení; jinak se k návrhu nepřihlíží (§ 2249 odst. 1). Souhlas platí od třetího měsíce po dojití; nesouhlasí-li nájemce do 2 měsíců, může pronajímatel do dalších 3 měsíců navrhnout soudu (§ 2249 odst. 3). Vyúčtování do 4 měsíců od konce zúčtovacího období, finanční vyrovnání nejpozději do 4 měsíců od doručení (§ 7 odst. 1 a 3 zák. 67/2013); námitky do 30 dnů, jinak se má za to, že příjemce souhlasí (§ 8 odst. 2); pokuta za prodlení podle § 13 nejvýše 50 Kč za každý započatý den. Vztah splatnosti podle § 2252 odst. 2 OZ a § 7 odst. 3 zák. 67/2013 posoudí advokát.
- **Časté chyby:** návrh na zvýšení bez doložení podmínek; vyúčtování bez členění; zmeškané třicetidenní námitky.
- **Nástroj:** `/pravni-sablony` (návrh na zvýšení, námitky k vyúčtování); lhůty a úroky `/pravni-vypocty`.
- **Eskalace:** návrh na soudní určení nájemného = advokát.

### NJ-09 Vyklizení bytu a dluhy po skončení nájmu
- **Kdy:** nájem skončil a nájemce byt neodevzdal nebo nezaplatil.
- **Klíčová ustanovení (ověřeno):** § 570, § 2225, § 2285, § 2291 odst. 1, § 2295 OZ; § 40 odst. 2 EŘ; § 79 a § 142a o. s. ř.
- **Co nesmí chybět:** doklad o skončení nájmu (výpověď a její dojití, nebo uplynutí doby a písemná výzva k opuštění bytu, která nájemci došla v době podle § 2285 a § 570 odst. 1); vyčíslení dlužného nájemného a služeb po měsících; za dobu od skončení nájmu do skutečného odevzdání bytu náhrada ve výši ujednaného nájemného (§ 2295 OZ; bezdůvodné obohacení jen pro jiné situace); předžalobní výzva.
- **Lhůty a rizika:** odevzdáním se rozumí i předání vyklizené nemovitosti (§ 2225 odst. 1). Neobsahuje-li rozhodnutí lhůtu, má se za to, že byt je třeba vyklidit do 15 dnů od právní moci (§ 40 odst. 2 EŘ). Před žalobou na plnění výzva alespoň 7 dní předem kvůli nákladům řízení (§ 142a o. s. ř.).
- **Časté chyby:** výměna zámků svépomocí; žaloba bez prokázaného skončení nájmu; přehlédnutá obnova nájmu na dobu určitou (§ 2285).
- **Nástroj:** `/pravni-sablony` (žaloba na vyklizení a zaplacení); `/generuj-smlouvu` vzor `predzalobni-vyzva`; úroky, poplatek, odměna `/pravni-vypocty`.
- **Kontroly:** references/kontroly-podani.md
- **Eskalace:** nájemce napadl výpověď (NJ-06) nebo tvrdí obnovu nájmu = advokát.

### NJ-10 Konec nájmu na dobu určitou a výpověď nájemce
- **Kdy:** blíží se konec sjednané doby, nebo chce nájemce odejít dřív.
- **Klíčová ustanovení (ověřeno):** § 570, § 2285, § 2286, § 2287 OZ.
- **Co nesmí chybět:** pronajímatel, který nechce pokračovat: písemná výzva nájemci, aby byt opustil, která mu musí v době 3 měsíců po skončení nájmu dojít, odeslání nestačí (§ 2285 ve spojení s § 570 odst. 1); kontrola, zda smlouva obnovu nájmu nevylučuje nebo neupravuje jinak (§ 2285 věta první, část za středníkem); nájemce na dobu určitou: popis změny okolností, kvůli níž po něm nelze rozumně chtít pokračování (§ 2287); písemná forma a dojití výpovědi (§ 2286 odst. 1).
- **Lhůty a rizika:** pokračuje-li nájemce v užívání aspoň 3 měsíce po skončení a výzva mu v této době nedojde, nájem se obnoví na stejnou dobu, nejvýše na 2 roky, ledaže si strany ujednaly něco jiného (§ 2285). Výzvu proto posílej včas a s doručením, které půjde prokázat. Výpovědní doba běží od prvního dne měsíce následujícího po dojití výpovědi (§ 2286 odst. 1).
- **Časté chyby:** pronajímatel po konci doby jen čeká; výzva odeslaná na konci tříměsíční doby, která dojde pozdě; nájemce odejde bez výpovědi a nájemné dál běží.
- **Nástroj:** `/pravni-sablony` (výzva k opuštění bytu, výpověď nájemce).
- **Eskalace:** spor o to, zda se nájem obnovil = advokát.

### NJ-11 SVJ: příspěvky, zálohy a vymáhání dluhů
- **Kdy:** vlastník jednotky neplatí příspěvky na správu domu nebo zálohy na služby; klient je SVJ nebo dlužící vlastník.
- **Klíčová ustanovení (ověřeno):** § 1180, § 1181, § 1186, § 1208 písm. c) a d) OZ; § 7 a § 8 zák. 67/2013; § 142a o. s. ř.
- **Co nesmí chybět:** rozhodnutí shromáždění o celkové výši příspěvků a o způsobu rozúčtování služeb (§ 1208 písm. c) a d)); předpis plateb pro jednotku; vyúčtování záloh (§ 1181); vyčíslení dluhu po měsících a odděleně příspěvky a zálohy; předžalobní výzva.
- **Lhůty a rizika:** příspěvky se rozvrhují podle podílu na společných částech, nestanoví-li prohlášení jinak; náklady vlastní správní činnosti stejně na každou jednotku (§ 1180). Při převodu jednotky přecházejí zjistitelné dluhy na nabyvatele a převodce za ně ručí (§ 1186 odst. 2), viz N-15. Promlčení hlídej podle Z-12.
- **Časté chyby:** vymáhání příspěvků bez rozhodnutí shromáždění o jejich výši; směšování příspěvků na správu a záloh na služby.
- **Nástroj:** `/generuj-smlouvu` vzor `predzalobni-vyzva`; platební rozkaz Z-04; výpočty `/pravni-vypocty`.
- **Kontroly:** references/kontroly-podani.md (u návrhu)
- **Eskalace:** dlužník v insolvenci nebo exekuci (E-10, E-12) = advokát.

### NJ-12 SVJ: shromáždění a rozhodování
- **Kdy:** pozvánka, návrh usnesení, zápis, hlasování per rollam; kontrola, zda bylo usnesení přijato platně.
- **Klíčová ustanovení (ověřeno):** § 1206, § 1207, § 1208, § 1210, § 1211, § 1212, § 1214, § 1221 OZ.
- **Co nesmí chybět:** svolání statutárním orgánem alespoň jednou ročně, na podnět vlastníků s více než čtvrtinou hlasů (nejméně dvou) povinně (§ 1207 odst. 1); pořad a podklady nebo možnost se s nimi seznámit (§ 1207 odst. 2); kontrola usnášeníschopnosti (přítomní s většinou všech hlasů) a potřebné většiny podle zákona a stanov (§ 1206 odst. 2); u per rollam návrh rozhodnutí, podklady a lhůta, bez stanov 15 dnů (§ 1211 odst. 3), a hlas s datem podepsaný vlastní rukou na listině s plným zněním návrhu (§ 1212).
- **Lhůty a rizika:** náhradní shromáždění jen připouštějí-li to stanovy, usnáší se při 40 % všech hlasů (§ 1210). Mimo zasedání lze rozhodnout po nezpůsobilém shromáždění, jinak jen připouštějí-li to stanovy (§ 1211 odst. 1); většina se tu počítá ze všech hlasů (§ 1214). Vyžaduje-li se veřejná listina, podpis na hlasu musí být úředně ověřen (§ 1212).
- **Časté chyby:** hlas per rollam e-mailem bez vlastnoručního podpisu; usnesení mimo pořad; pozvánka bez podkladů.
- **Nástroj:** `/pravni-sablony` (pozvánka, usnesení, zápis, hlasovací listina); stanovy `/revize-smlouvy`.
- **Eskalace:** změna prohlášení vlastníka nebo podílů, rozhodnutí osvědčované veřejnou listinou, úvěr SVJ = advokát.

### NJ-13 SVJ: napadení rozhodnutí shromáždění přehlasovaným vlastníkem
- **Kdy:** vlastník jednotky byl přehlasován a s rozhodnutím shromáždění nesouhlasí (rozpor se zákonem nebo stanovami, nebo jiný důležitý důvod u záležitosti správy domu).
- **Klíčová ustanovení (ověřeno):** § 1209, § 1221, § 258 OZ; usnesení NS sp. zn. 26 Cdo 2201/2023 ze dne 20. 11. 2024 (ECLI:CZ:NS:2024:26.CDO.2201.2023.1, ověřeno v plném textu; před citací v podání znovu přes DirectCase).
- **Co nesmí chybět:** usnesení, zápis, pozvánka a stanovy; doklad, že klient byl přehlasován; důležitý důvod; den, kdy se o rozhodnutí dozvěděl nebo dozvědět mohl; návrh podle § 1209 odst. 1 ve spojení s § 258 OZ: primárně vyslovení neplatnosti rozhodnutí, případně uspořádání poměrů podle slušného uvážení (§ 1209 odst. 2) a dočasný zákaz jednat podle napadeného rozhodnutí (§ 1209 odst. 1).
- **Lhůty a rizika:** rozhodná je jen subjektivní lhůta 3 měsíců ode dne, kdy se vlastník o rozhodnutí dozvěděl nebo dozvědět mohl; po ní právo zaniká (§ 1209 odst. 1). Podle NS 26 Cdo 2201/2023 se vyslovení neplatnosti usnesení shromáždění řeší cestou § 1209 odst. 1 ve spojení s § 258, roční objektivní doba podle § 259 se neuplatní a bez přehlasování nebo důležitého důvodu soud rozhodnutí věcně nepřezkoumá. Lhůta je prekluzivní: návrh musí soudu dojít.
- **Časté chyby:** návrh jen podle § 258 a § 259 jako u spolku s představou roční lhůty; zmeškání tří měsíců kvůli jednání s výborem; chybí tvrzení o přehlasování a důležitém důvodu.
- **Nástroj:** `/pravni-sablony` (návrh); lhůta `/pravni-vypocty lhuta --jednotka mesice --hmotnepravni`.
- **Kontroly:** references/kontroly-podani.md
- **Eskalace:** lhůta končí do 14 dnů, nebo rozhodnutí s velkým finančním dopadem (úvěr, rekonstrukce) = advokát hned.

<!-- Origin: GrowLead ak-sladek v0.9, vlastní text katalogu úloh | Vytvořeno: 2026-10-16 | Ověřeno na zakonyprolidi.cz 2026-10-16: OZ § 258, 259, 260, 605, 607, 1180, 1181, 1186, 1206 až 1212, 1214, 1221, 1982, 1987, 2225, 2235, 2236, 2237, 2239, 2248, 2249, 2251, 2252, 2254, 2285 až 2288, 2290, 2291, 2297, 2302, 2303, 2305, 2307 až 2310, 2312, 2314, 2315, 2991; zák. 67/2013 § 7, 8, 13; o. s. ř. § 79, 142a; EŘ § 40; IZ § 140 | Review: Codex cross-family 2026-10-16, nálezy ověřeny a zapracovány (NJ-02, NJ-09, NJ-10, NJ-13): OZ § 1, 570, 2227, 2228, 2229, 2232, 2295; NS 26 Cdo 2201/2023 ze dne 20. 11. 2024 (ECLI:CZ:NS:2024:26.CDO.2201.2023.1), plný text https://www.zakonyprolidi.cz/judikat/nscr/26-cdo-2201-2023; NJ-13 už necituje § 259 a § 260 | Inspiration: externí katalog právních úloh jen jako kontrolní seznam pokrytí (názvy), text vlastní -->
