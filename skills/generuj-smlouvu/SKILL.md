---
name: generuj-smlouvu
description: Vygeneruje smlouvy z vlastních vzorů kanceláře — kupní smlouva na nemovitost + smlouva o advokátní úschově jako propojený pár z jednoho zadání. Uživatel nadiktuje fakta případu (strany, nemovitost dle LV, cena, platby), AI je namapuje na strukturovaná data, deterministický šablonovací engine vyplní schválený vzor kanceláře. Použij při přípravě dokumentů k převodu nemovitosti, prodeji bytu/pozemku s úschovou kupní ceny, nebo když uživatel řekne „připrav kupní smlouvu a úschovu".
argument-hint: "<fakta případu: strany, nemovitost, cena, platby>"
---

# /generuj-smlouvu — Generování smluv ze vzorů kanceláře

**Důležité**: Tento skill pomáhá s právními workflow, ale neposkytuje právní poradenství ve smyslu zákona č. 85/1996 Sb., o advokacii. Výstup je NÁVRH ke kontrole advokátem — nikdy ho nepředávej klientovi bez advokátní kontroly.

## Jak to funguje (princip)

**AI text smlouvy NEPÍŠE.** Text pochází ze schválených vzorů kanceláře (docxtpl šablony). AI pouze:
1. vytěží fakta případu ze zadání uživatele (přirozený jazyk, LV, rezervační smlouva…),
2. namapuje je na JSON dle `vzory/prevod-nemovitosti/schema.json`,
3. zvaliduje (chybějící pole = STOP a doptat se, ne hádat),
4. spustí deterministický render (`scripts/render.py`) → hotové .docx v jednotném formátu kanceláře.

Tím je vyloučena halucinace klauzulí — každá věta v dokumentu je z odsouhlaseného vzoru.

## Pracovní postup

### Krok 1 — Převzetí faktů
Uživatel dodá fakta případu volným textem, nebo přiloží podklady (výpis LV, rezervační smlouvu, e-mail s dohodou). Vytěž:
- **Strany**: jméno/název, r.č. nebo IČ, adresa; u PO rejstříkový zápis + zástupce; u manželů oba (SJM)
- **Nemovitost**: přesný popis dle LV (jednotka/pozemky/stavba, podíly, k.ú., katastrální pracoviště)
- **Cena a platby**: celková cena, záloha (hotovost/už uhrazená), doplatek do úschovy
- **Kontakty**: e-maily obou stran (notifikace o pohybech na účtu úschovy)
- **Výplatní účet prodávajícího** (č.ú.) — POVINNÝ, bez něj úschovu nelze sestavit

### Krok 2 — KYC ověření (s DirectCase konektorem)
Pokud je připojen DirectCase MCP, ověř strany v obchodním rejstříku (`search_company` podle IČO nebo názvu):
existence, sídlo, statutární orgán, **způsob jednání** (samostatně × společně!), insolvence.
Nesoulad → upozorni PŘED generováním. Bez konektoru výslovně uveď, že údaje nebyly nezávisle ověřeny.

### Krok 3 — Mapování na schéma
Sestav JSON dle `vzory/prevod-nemovitosti/schema.json`. Řádky stran (`radek1`–`radek5`) skládej dle vzorů v schema description. Částky formátuj `3.500.000,00`, lhůty `deseti (10)`.
- prodávající v úschově = **Strana příjemce** (musí mít č.ú.)
- kupující v úschově = **Strana uschovatele**
- `cena.doplatek` MUSÍ = `uschova.castka`

### Krok 4 — Kontrola s uživatelem
Před generováním ukaž **přehlednou rekapitulaci** (strany, nemovitost, částky, účty, lhůty) a nech ji potvrdit. Netriviální odchylky od standardu (jiná banka úschovy, nestandardní lhůty) výslovně zvýrazni.

### Krok 5 — Render
```
python skills/generuj-smlouvu/scripts/render.py \
  skills/generuj-smlouvu/vzory/prevod-nemovitosti  data-pripadu.json  vystup/
```
Vyžaduje `pip install docxtpl`. Validace ve skriptu při chybě generování ZASTAVÍ (exit 1) — chybu vyřeš doptáním, nikdy ji neobcházej vymyšlenou hodnotou.

### Krok 6 — Předání
Vrať uživateli oba dokumenty + shrnutí: co bylo vygenerováno, jaké hodnoty byly použity z defaultů kanceláře (účet úschovy, lhůty, stejnopisy), co zbývá doplnit ručně (datum a místo podpisu). Připomeň kontrolu advokátem.

## Další vzory (render_doc.py — jednotlivé dokumenty s gates)

Postup u všech: fakta → JSON podle `vzory/<vzor>/schema.json` → `python scripts/render_doc.py vzory/<vzor> data.json out/`.
Gate při chybě (chybějící povinný údaj, porušení zákonné podmínky) generování ZASTAVÍ a vypíše proč; varování (⚠) předej advokátovi. Data piš klidně ISO (`2026-11-30`), do textu se převedou na `30. 11. 2026`.

| Vzor | Kódový gate (STOP) | Hlavní varování |
|---|---|---|
| `plna-moc` | chybí rozsah zmocnění | katastr → vynucen úředně ověřený podpis |
| `predzalobni-vyzva` | **§ 142a: lhůta < 7 dnů**, chybí doručovací adresa | odeslat ≥ 7 dnů před žalobou |
| `uznani-dluhu` | chybí důvod či výše dluhu, **součet splátek ≠ dluh**, splátky mimo pořadí | písemnost a podpis dlužníka (§ 2053), promlčení § 639/§ 641, není exekučním titulem |
| `dohoda-o-narovnani` | chybí sporné právo, nové plnění, částka či splatnost | rozsah konečného vypořádání (§ 1905), forma (§ 1906), nemovitost → vklad |
| `smlouva-o-smlouve-budouci-kupni` | chybí předmět dle LV, cena, termín výzvy či podpisu, typ a výše zálohy/závdavku | záloha do úschovy, závdavek (§ 1808), § 1788 |
| `rezervacni-smlouva` | chybí doba, poplatek nebo jeho osud | spotřebitel a propadnutí poplatku, zprostředkování (zák. 39/2020) |
| `najemni-smlouva-byt` (+ předávací protokol) | **jistota > 3× nájemné (§ 2254)**, doba určitá bez konce, chybí nájemné | ujednání v neprospěch nájemce, vyúčtování služeb (zák. 67/2013) |
| `vyzva-najemci` | chybí výčet dluhu, součet nebo lhůta | prokazatelné doručení, přiměřenost lhůty |
| `vypoved-najmu-bez-vypovedni-doby` | **dluh < 3 měsíce**, chybí předchozí výzva nebo její dojití, lhůta k nápravě neuplynula | poučení § 2286 a § 2290 vždy v textu, hmotněprávní lhůta |
| `zastavni-smlouva-nemovitost` | chybí zajišťovaný dluh, zástava dle LV, strany | vklad + ověřené podpisy, zástavce ≠ dlužník, zákaz zcizení (§ 1761) |
| `smlouva-o-pravnich-sluzbach` | chybí předmět nebo odměna | ADR u ČAK pro spotřebitele, AI doložka, smlouva na dálku |

**Stav vzorů:** plná moc a předžalobní výzva i vzory od v0.9 jsou návrh GrowLead v house stylu (`vzory/<vzor>/meta.json`, `stav: navrh-growlead`). Render u nich vždy připomene „vzor dosud neschválen kanceláří". Po revizi JUDr. Sládkem se stav přepne na `schvaleno-kanceari` a od té chvíle jsou to vzory kanceláře. Formát (písmo, číslování, patička s názvem listiny, podpisy) se dědí ze šablony kanceláře a hlídá ho zámek formátu při každém nasazení.

## Eskalace (Escalation-Router)

PŘED draftováním zkontroluj [`references/eskalace.md`](../../references/eskalace.md) (root pluginu): sporná vlastnická struktura (poznámka spornosti, exekuce na LV), nestandardní úschova, cizinecký prvek, insolvence protistrany, „dva jednatelé společně" → **STOP, nedraftuj, shrň advokátovi**. Nejistota = eskalace, ne odhad.

## Hard gates (neobcházet)

- **Advokátní úschova**: zákaz hotovostních vkladů/výběrů z účtu úschovy; jeden účet = jedna úschova; úschova se hlásí do Elektronické knihy úschov ČAK (před přijetím, po přijetí, po vyplacení). Připomeň uživateli EKÚ hlášení.
- **Katastr**: k elektronickému vkladu je nutná vkladová listina s úředně ověřenými podpisy; prosté skeny katastr zamítá.
- **Hotovost max. 270.000,00 Kč** (zákon č. 254/2004 Sb., § 4; sčítají se platby téže osobě za jeden den): kupní smlouva počítá se zálohou v hotovosti, vyšší záloha = render STOP. Vyšší záloha jde bezhotovostně nebo do úschovy, úpravu textu posoudí advokát.
- Chybí-li povinný údaj → **zeptej se, nikdy nedopĺňuj odhadem** (jde o právní dokument).
- Judikaturu/§ cituj jen s ověřeným identifikátorem z DirectCase; bez konektoru citace označ jako neověřené.
- **Datum-disciplína**: u znění zákonů přes DirectCase používej `date` parametr (temporal validity) a do výstupu uveď, ke kterému dni znění platí — legislativa úschov/advokacie se v 2026 měnila. Pro výpočet lhůt (§142a předžalobní výzva, lhůty úschovy) ověř aktuální datum přes DirectCase `get_current_time`, nespoléhej na paměť modelu.

## Konfigurace kanceláře

`config/kancelar.json` v rootu pluginu — konstanty advokáta (jméno, ČAK, sídlo), účet úschovy, výchozí lhůty, počty stejnopisů. Data případu je mohou přepsat (`uschova.ucet`, `lhuty.*`).

## Omezení verze 0.1 (řekni uživateli, když narazí)

- Pokrytá struktura obchodu: záloha uhrazená v hotovosti před podpisem + doplatek do advokátní úschovy. Varianty (hypoteční financování, provize zprostředkovatele z první části, bez zálohy) zatím nejsou — vyžadují úpravu šablony, ne improvizaci v datech.
- Prodávající = 1 osoba (FO/PO). Manželé (SJM) a více spoluvlastníků zatím jen na straně kupující omezeně — ověř výstup.
- Podpisový blok se zástupcem podporuje jen kupující stranu (PO prodávající = zkontroluj podpisy ručně).

<!-- Origin: GrowLead ak-sladek plugin (interní vzory kanceláře JUDr. Sládka) | Vytvořeno: 2026-07-14 | Inspiration: interní docxtpl vzory kanceláře (kupní smlouva, smlouva o úschově, plná moc, předžalobní výzva) -->
