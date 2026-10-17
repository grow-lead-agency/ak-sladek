---
name: pravni-sablony
description: Knihovna právních úloh — žaloba, vyjádření k žalobě, odvolání, dovolání, právní stanovisko, memorandum, upomínka, dodatek ke smlouvě, uznání dluhu, porovnání verzí dokumentu, shrnutí pro klienta, anonymizace, překlad, posudek, FAQ, checklist procesu a další. Upgrade šablon ze semináře AI pro právníky (11/2025) — stejná struktura, ale s ochranou proti halucinaci citací a formátem kanceláře. Použij když advokát potřebuje sepsat či zpracovat právní dokument, který nemá vlastní specializovaný skill.
argument-hint: "<typ dokumentu/úlohy + fakta>"
---

# /pravni-sablony — Knihovna právních úloh

**Důležité**: Výstupy jsou návrhy ke kontrole advokátem (zák. č. 85/1996 Sb.). Nikdy je nepředávej klientovi bez advokátní kontroly.

## Nejdřív routing — má úloha specializovaný skill?

| Úloha | → Použij místo šablony |
|---|---|
| Kupní smlouva + úschova (nemovitost) | `/generuj-smlouvu` (vzory kanceláře) |
| Plná moc, předžalobní výzva, uznání dluhu se splátkami, dohoda o narovnání | `/generuj-smlouvu` (vzory s kódovými gates) |
| Smlouva o smlouvě budoucí kupní, rezervační smlouva, zástavní smlouva k nemovitosti | `/generuj-smlouvu` |
| Nájemní smlouva k bytu, výzva nájemci, výpověď nájmu bez výpovědní doby | `/generuj-smlouvu` |
| Smlouva o poskytování právních služeb (s AI doložkou) | `/generuj-smlouvu` |
| Úrok z prodlení, konec lhůty, promlčení, soudní poplatek, odměna dle tarifu | `/pravni-vypocty` (skript, nikdy z hlavy) |
| Kontrola citací v hotovém dokumentu | `/hloubkovy-research citace` |
| Odpověď klientovi „kolik to bude stát", newsletter, odborný příspěvek | `references/klientska-komunikace.md` (etický kodex ČAK) |
| Přeformátovat dokument do stylu kanceláře | `/formatuj-smlouvu` |
| Revize/analýza smlouvy na rizika | `/revize-smlouvy` |
| NDA posouzení | `/triage-nda` |
| Kontrola podpisových práv, KYC | `/kontrola-podpis`, `/kontrola-dodavatele` |
| GDPR/compliance check | `/kontrola-souladu` |
| Judikatura, rešerše, prověrka čehokoli | `/hloubkovy-research` |
| Riziko, jednání, šablonové odpovědi, přehled | `/posouzeni-rizika`, `/priprava-jednani`, `/pravni-odpoved`, `/prehled-pravni` |

Nic z toho? → pokračuj šablonou níže.

## Katalog úloh (karty)

Než začneš psát, najdi kartu úlohy v [`references/katalog/00-index.md`](references/katalog/00-index.md) (212 karet, 12 oblastí). Advokát může úlohu zadat i číslem karty („úloha N-03", „karta Z-05").
Karta říká, co dokument musí obsahovat, podle jakých ustanovení (ověřeno k 16. 10. 2026), jaké lhůty běží, jaké jsou časté chyby, který vzor nebo skill použít a kdy STOP a eskalovat. Karty 01 až 05 jsou hlavní praxe kanceláře (nemovitosti, úschovy, nájem a SVJ, vymáhání, zajištění a exekuce), karty 06 až 12 ostatní oblasti: tam vždy ověř znění přes DirectCase a častěji eskaluj.
Karta je podklad, ne hotový text: dokument dál vzniká přes vzor (`/generuj-smlouvu`) nebo šablonu níže s upgrade vrstvou.

## Upgrade vrstva (platí pro VŠECHNY šablony — neobcházet)

1. **Doptej se před psaním** — každá šablona končí „zeptej se mě na vše, co potřebuješ" — MYSLÍ SE TO VÁŽNĚ. Chybí-li fakta, ptej se, nevymýšlej. Zadání si nech dát (nebo ho sám sestav a nech potvrdit) ve 4 řádcích:
   ```
   CO PŘIPRAVIT: druh podání nebo smlouvy
   FAKTA: strany a rozhodné události s daty a částkami
   PODKLADY: listiny k dispozici (smlouva, faktury, korespondence, výzva s dokladem o odeslání)
   CÍL KLIENTA: jakého výsledku chce dosáhnout
   ```
   Chybějící údaje ponech v dokumentu jako `[DOPLNIT: …]` a vypiš je na konci jako seznam „Údaje k potvrzení". Nikdy je nevymýšlej.
2. **Citace jen ověřené** — §, judikatura, sp. zn. VÝHRADNĚ přes DirectCase (`get_law_detail` k rozhodnému dni, `search_identifier` + `get_document` u rozhodnutí) nebo primární zdroj. Bez ověření → `[neověřeno]`. Nikdy nevydávej neověřenou citaci za fakt. AI search (`search_*_parallel`) lze zavolat jen 1× za konverzaci (víc dotazů → pole `queries[]`); limity a volba nástroje viz [`references/directcase-limity.md`](../../references/directcase-limity.md). Před předáním advokátovi projdi hotový text `/hloubkovy-research citace`.
3. **Formát kanceláře** — finální dokument protáhni `/formatuj-smlouvu` house rules (Tahoma 10,5, bez mezer, částky s haléři, podpisy ve sloupcích).
4. **Playbook kanceláře** — existuje-li `legal.local.md`, respektuj jeho pozice a eskalační pravidla.
5. **Eskalace** — před draftem zkontroluj `references/eskalace.md`; červený trigger = STOP a shrnutí advokátovi.
6. **Osobní údaje** — do dokumentů jen údaje dodané advokátem; při anonymizaci konzistentní náhrady (Osoba 1, Společnost A).
7. **Podání na soud nebo úřad** — u každé žaloby, návrhu, odporu, vyjádření, odvolání či dovolání projdi [`references/kontroly-podani.md`](../../references/kontroly-podani.md) (příslušnost, § 142a, lhůty a promlčení, poplatky, forma) a tabulku výsledku připoj pro advokáta mimo text podání.

## Šablony (struktura: Role · Rozsah · Formát · Účel)

Každou spouštěj vzorem: *„[Role]. [Rozsah]. Formát: [formát]. Účel: [účel]. Zeptej se mě na všechno, co potřebuješ vědět."*

### Podání a spory
Pro všechny položky této sekce platí bod 7 upgrade vrstvy (kontroly před podáním).
- **Žaloba** — procesní právník; kompletní žaloba: účastníci, rozhodující skutečnosti, důkazy, právní posouzení, petit; náležitosti dle o.s.ř., číslované odstavce. Před psaním ověř přes DirectCase aktuální judikaturu k nároku.
- **Návrh na vydání (elektronického) platebního rozkazu** — peněžitý nárok doložený listinami; u elektronického předepsaný formulář a uznávaný podpis; v návrhu tvrzení o odeslání předžalobní výzvy.
- **Odpor proti platebnímu rozkazu** — lhůta od doručení (ověř datum doručení a zákonnou lhůtu, ne odhad). Odpor nemusí být odůvodněn (§ 174 odst. 3 o. s. ř.), ale soud po něm může uložit kvalifikovanou výzvu k vyjádření (§ 114b o. s. ř.) a její nesplnění má tvrdé následky. Proto odpor, následné vyjádření a jeho lhůtu hlídej jako tři samostatné kroky. Věcné námitky: promlčení, zaplacení či započtení, vady plnění. Chybějící předžalobní výzva je argument proti náhradě nákladů (§ 142a), ne proti samotnému dluhu.
- **Vyjádření k žalobě** — obhajoba: procesní námitky, věcná obrana, důkazní návrhy, návrh na zamítnutí; strukturováno podle bodů žaloby.
- **Odvolání** — vady prvostupňového rozhodnutí (hmotné i procesní), rozsah napadení, odvolací důvody, petit; citace z napadeného rozhodnutí.
- **Dovolání** — přípustnost, právní otázka zásadního významu, judikatura NS (POUZE ověřená přes DirectCase!).
- **Upomínka / předžalobní výzva** — specifikace dluhu, výzva s lhůtou, důsledky. ⚠️ HARD GATE: nárok na náhradu nákladů řízení vyžaduje výzvu **min. 7 dnů před podáním žaloby** na doručovací adresu (§ 142a o.s.ř.) — vždy zkontroluj a upozorni. Pro výpočet lhůty ověř aktuální datum přes DirectCase `get_current_time`, nespoléhej na paměť modelu.
- **Uznání dluhu** — identifikace stran, specifikace dluhu co do důvodu i výše, písemná forma (§ 2053 OZ), splátkový kalendář a ztráta výhody splátek. Účinek na promlčení: od uznání běží nová desetiletá promlčecí lhůta, resp. od posledního dne doby, do které dlužník slíbil plnit (§ 639 OZ); u splátek běží pro každou splátku od její dospělosti (§ 641 OZ). Výraz „přerušení promlčení" je terminologie starého OZ, nepoužívat. Standardní případ jde přes `/generuj-smlouvu` vzor `uznani-dluhu` (gate hlídá součet splátek); šablonou jen nestandardní varianty.

### Smlouvy a korporátní (mimo vzory kanceláře)
- **Nájemní smlouva** — prostory, nájemné, služby, údržba, ukončení; dle NOZ.
- **Darovací smlouva** — specifikace daru, prohlášení dárce, podmínky, odvolání daru; u nemovitostí vkladové řízení (KEP + časové razítko — viz katastr gate).
- **Pracovní smlouva** — povinné náležitosti (druh, místo, nástup), mzda, konkurenční doložka; kogentní ustanovení ZP.
- **Smlouva o dílo / společenská smlouva / konkurenční doložka / dohoda o narovnání** — dle seminárních šablon; u narovnání: sporné vztahy → ústupky → nové uspořádání → konečnost vypořádání.
- **Dodatek ke smlouvě** — přesná identifikace původní smlouvy, číslování, co se ruší a čím nahrazuje, účinnost.

### Nemovitosti a zajištění (mimo vzory kanceláře)
Kupní smlouvu a úschovu dělá `/generuj-smlouvu`. Tady jsou navazující úlohy realitní praxe. U všech zkontroluj `references/eskalace.md` (sporná vlastnická struktura, exekuce či insolvence na LV, cizinecký prvek = STOP).
- **Prověrka listu vlastnictví (checklist)** — LV k aktuálnímu datu. A: vlastník a podíly. B: nemovitosti (pozemky, stavby, jednotky), **písmeno „P" = plomba, probíhá řízení**. B1: práva ve prospěch nemovitosti. **C: věcná práva zatěžující nemovitost** (zástavní práva včetně exekutorského a soudcovského, služebnosti a věcná břemena, věcná předkupní práva) a poznámky k nim. **D: poznámky k vlastníkovi nebo nemovitosti** (spornost, exekuce, insolvence, zákazy nakládání), plomby, upozornění. E: nabývací listiny. Kontroluj **C i D vždy obě**, exekuce a insolvence se mohou objevit v obou. Výstup: tabulka nálezů + co musí řešit smlouva nebo úschova (výplatní podmínky).
- **Checklist koupě nemovitosti** — LV, nabývací titul a jeho platnost, SJM a souhlas manžela, zástavy a jejich výmaz z kupní ceny, PENB, předání a měřidla, daňové dopady (daň z nabytí nemovitých věcí je od roku 2020 zrušena; DPH u nových staveb a daň z příjmů prodávajícího ověř podle aktuální úpravy), lhůty návrhu na vklad.
- **Smlouva o smlouvě budoucí kupní** — určení podstatných náležitostí budoucí smlouvy, lhůta k uzavření, záloha nebo závdavek (rozlišit!), důsledky, když se budoucí smlouva neuzavře; vazba na rezervační smlouvu developera. Standardně `/generuj-smlouvu` vzor `smlouva-o-smlouve-budouci-kupni`.
- **Rezervační smlouva** — předmět, rezervační poplatek a jeho osud (započtení, vrácení, propadnutí), doba rezervace, výhrady. Standardně `/generuj-smlouvu` vzor `rezervacni-smlouva`.
- **Zástavní smlouva k nemovitosti** — zajišťovaný dluh (i budoucí), označení nemovitosti dle LV, případný zákaz zcizení či zatížení (jeho účinky vůči třetím osobám posuď podle § 1761 OZ), vklad do katastru, úředně ověřené podpisy. Standardně `/generuj-smlouvu` vzor `zastavni-smlouva-nemovitost`.
- **Návrh na vklad / návrh na výmaz zástavního práva** — formulář katastru, vkladová listina s ověřenými podpisy, kvitance nebo souhlas zástavního věřitele s výmazem, správní poplatek.
- **Služebnost bytu, požívací právo, darování s výhradou věcného břemene** — rozsah služebnosti, bezúplatnost či úplata, doba (dožití), vklad; u darování vztah k dědickým nárokům (nepominutelní dědici) označ jako bod k posouzení advokátem.
- **Návrh na zápis poznámky spornosti** — vazba na probíhající řízení a lhůty, které ji podmiňují; vždy eskalace, AI připraví jen podklad.

### Analytické a klientské výstupy
- **Právní stanovisko / posudek** — definice problému → analýza legislativy a judikatury (DirectCase!) → interpretační varianty → rizika → doporučení; executive summary na začátek.
- **Klientské memorandum** — 1 strana shrnutí + možnosti s výhodami/nevýhodami + doporučený postup s harmonogramem a náklady; srozumitelný jazyk.
- **Shrnutí složitého dokumentu** — klíčové body, práva/povinnosti, lhůty, rizika; laickým jazykem, tabulka + časová osa.
- **Porovnání verzí dokumentu** — tabulka změn (přidáno/odebráno/upraveno), právní dopad každé změny, doporučení akceptovat/odmítnout.
- **Překlad právního dokumentu** — zachovat právní význam a strukturu; termíny bez ekvivalentu označit s vysvětlením.
- **Anonymizace** — odstranit osobní/identifikační/důvěrné údaje, konzistentní náhrady, zachovat právní podstatu.
- **Due diligence report / kontrola úplnosti dokumentace** — struktura dle právních oblastí, risk matrix, red flags, chybějící dokumenty.
- **Interní směrnice / FAQ / prezentace / checklist procesu** — dle seminárních šablon; checklist vždy s lhůtami a odpovědnostmi.

## Poznámka k původu
Šablony vychází ze semináře „AI pro právníky" (4.11.2025), který JUDr. Sládek absolvoval — stejná logika Role/Rozsah/Formát/Účel, kterou zná, ale upgradovaná: trvalé skilly místo copy-paste promptů, ověřené citace místo halucinací, formát kanceláře místo generického výstupu.

<!-- Origin: upgrade seminárních šablon (AI seminář pro právníky 4.11.2025, PDF od JUDr. Sládka) | Vytvořeno: 2026-07-14 | Updated: 2026-10-16 (zadání ve 4 řádcích, kontroly před podáním, kontrola citací, sekce Nemovitosti a zajištění, oprava § 639 u uznání dluhu) | Inspiration: interní PDF "ŠABLONY PROMPTŮ PRO PRÁVNÍ DOKUMENTY", externí katalog právních úloh (jen pokrytí, text vlastní, detail v interním research/08), https://github.com/anthropics/claude-for-legal/pull/127 (myšlenka cite-check) -->
