# Kontroly před podáním (soud, úřad)

> Sdílený kontrolní seznam pro všechna podání: žaloba, návrh na (elektronický) platební rozkaz,
> odpor, vyjádření, odvolání, dovolání, návrhy v katastru a ve správním řízení.
> Skill, který podání připravuje, projde všech 5 bloků a **výsledek vypíše advokátovi** jako
> tabulku (blok | stav | co ověřit). Nesplněný blok = výrazné upozornění, ne tichá oprava.
> Paragrafy níže jsou orientační. Do podání je cituj až po ověření přes DirectCase
> `get_law_detail` k rozhodnému dni (viz `directcase-limity.md`). Datum dneška ber z `get_current_time`.

## 1. Příslušnost a druh řízení
- Věcná příslušnost: okresní, nebo krajský soud jako soud prvního stupně (§ 9 o. s. ř.).
- Místní příslušnost: obecný soud žalovaného (§ 84 a násl. o. s. ř.); u práv k nemovitostem
  výlučně soud podle místa nemovitosti (§ 88 o. s. ř.); dohoda podnikatelů o místní příslušnosti
  (§ 89a o. s. ř.).
- Druh řízení: platební rozkaz, elektronický platební rozkaz, směnečný platební rozkaz, evropský
  platební rozkaz, běžné sporné řízení, nesporné řízení (z. ř. s.), správní řízení nebo správní
  žaloba. Zvol a zdůvodni jednou větou. **Nejdřív urči procesní režim**: pravidla výše platí pro
  civilní řízení. Ve správním soudnictví je věcně příslušný krajský soud a místně soud podle sídla
  správního orgánu, který rozhodl v prvním stupni (§ 7 s. ř. s.).

## 2. Předžalobní výzva (§ 142a o. s. ř.)
- U žaloby na splnění povinnosti: výzva odeslaná **nejméně 7 dní před podáním žaloby** na adresu
  pro doručování, nebo na poslední známou adresu.
- Bez výzvy soud zpravidla nepřizná náhradu nákladů řízení.
- Vyžádej si datum odeslání a doklad o odeslání. Chybí-li, upozorni a nenech podání odejít mlčky.
- Výzvu samotnou generuj přes `/generuj-smlouvu` (vzor předžalobní výzvy má kódový gate na 7 dní).

## 3. Lhůty a promlčení
- Počítání lhůt: lhůta začíná dnem následujícím po události; připadne-li konec na sobotu, neděli
  nebo svátek, končí nejbližší pracovní den (§ 57 o. s. ř.).
- **Procesní lhůty** (zachovány i podáním na poštu nebo do datové schránky poslední den,
  § 57 odst. 3 o. s. ř.): odvolání 15 dnů od doručení písemného vyhotovení (§ 204 o. s. ř.);
  odpor proti platebnímu rozkazu 15 dnů od doručení (§ 172 odst. 1 o. s. ř.); odvolání ve
  správním řízení 15 dnů od oznámení (§ 83 správního řádu); správní žaloba proti rozhodnutí
  2 měsíce (§ 72 s. ř. s.), proti nečinnosti nejpozději 1 rok (§ 80 s. ř. s.), jiné typy podle
  zvláštní úpravy.
- **Hmotněprávní (prekluzivní) lhůty**: návrh musí soudu poslední den **dojít**, odeslání
  nestačí. Typicky návrh na přezkoumání výpovědi z nájmu bytu 2 měsíce od doby, kdy výpověď
  došla (§ 2290 OZ). U těchto lhůt doporuč podání nejpozději den předem.
- Promlčení: subjektivní lhůta 3 roky (§ 629 odst. 1 a § 619 OZ), objektivní nejpozději 10 let
  od dospělosti majetkového práva (§ 629 odst. 2 OZ), zvláštní objektivní lhůty u náhrady škody
  (§ 636 OZ) a u bezdůvodného obohacení (§ 638 OZ). Písemné uznání dluhu co do důvodu i výše (§ 2053 OZ) zakládá
  desetiletou promlčecí lhůtu od uznání, resp. od posledního dne určené doby (§ 639 OZ),
  u splátek § 641 OZ.
- Lhůta, která končí do 14 dnů, nebo nárok blízko promlčení = **výrazné upozornění nahoře**,
  ne poznámka pod čarou. Výpočet nech advokáta potvrdit.

## 4. Doručení, poplatky, náklady
- Podání a doručování přes datovou schránku (zákon č. 300/2008 Sb.); ověř ID datové schránky
  protistrany, pokud ji má.
- Soudní poplatek podle sazebníku zákona č. 549/1991 Sb. (splatnost, případné osvobození).
- Náhrada nákladů: advokátní tarif (vyhláška č. 177/1996 Sb.) a režijní paušály.
- U peněžitých pohledávek: zákonný úrok z prodlení = repo sazba ČNB platná k prvnímu dni
  kalendářního pololetí, v němž prodlení vzniklo, + 8 p. b. (nařízení vlády č. 351/2013 Sb.);
  mezi podnikateli minimální paušál 1 200 Kč za uplatnění pohledávky. Sazbu ověř na cnb.cz,
  nepočítej z paměti.

## 5. Forma podání
- Předepsaný formulář (elektronický platební rozkaz), uznávaný elektronický podpis, nebo podání
  datovou schránkou.
- Povinné zastoupení advokátem: dovolání (§ 241 o. s. ř.), kasační stížnost (§ 105 s. ř. s.),
  ústavní stížnost (§ 30 zákona č. 182/1993 Sb.).
- Katastr: vkladová listina s úředně ověřenými podpisy (viz katastr gate v `/generuj-smlouvu`).
- Přílohy: plná moc, listinné důkazy, doklad o odeslání předžalobní výzvy, doklad o zaplacení
  poplatku.

## Výstup pro advokáta (vždy na konec podání, mimo text podání)

| Blok | Stav | Co ověřit před odesláním |
|---|---|---|
| 1 Příslušnost a druh řízení | ✅ / ⚠️ | … |
| 2 Předžalobní výzva | ✅ / ⚠️ / n/a | … |
| 3 Lhůty a promlčení | ✅ / ⚠️ | … |
| 4 Doručení, poplatky, náklady | ✅ / ⚠️ | … |
| 5 Forma podání | ✅ / ⚠️ | … |

Pak spusť `/hloubkovy-research citace` na hotový text (kontrola každé citace).

<!-- Origin: GrowLead ak-sladek | Vytvořeno: 2026-10-16 | Inspiration: myšlenka „5 kontrol" z externí knihovny právních úloh (text nepřebírán, detail v interním research/08); ustanovení ověřena na zakonyprolidi.cz 2026-10-16: o. s. ř. § 9, 57, 84, 88, 89a, 114b, 142a, 172, 174, 204, 241; s. ř. s. § 7, 72, 80, 105; zák. 182/1993 § 30; správní řád § 83; OZ § 619, 629, 636, 638, 639, 641, 1761, 2053, 2290; katastrální vyhláška 357/2013 § 23 | Review: Codex cross-family 2026-10-16 (10 nálezů zapracováno) -->
