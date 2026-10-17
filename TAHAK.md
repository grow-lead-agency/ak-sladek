# TAHÁK — kdy použít který skill

> Jedna stránka na nástěnku. Nemusíte si pamatovat příkazy — stačí popsat situaci vlastními slovy, Claude skill pozná sám. Příkazy jsou zkratka.

## 🏁 Začínám s pluginem
| Situace | Skill |
|---|---|
| První spuštění / výstupy jsou moc obecné | `/nastaveni-kancelare` — 15 min rozhovor, nastaví vaše standardy |

## 📄 Tvorba dokumentů
| Situace | Skill |
|---|---|
| Prodej nemovitosti — potřebuju kupní smlouvu + úschovu | `/generuj-smlouvu` (jeden diktát → oba dokumenty z vašich vzorů) |
| Potřebuju plnou moc | `/generuj-smlouvu` (vzor plná moc) |
| Dlužník neplatí — předžalobní výzva | `/generuj-smlouvu` (vzor; hlídá lhůtu 7 dnů dle § 142a) |
| Dlužník uzná dluh a bude splácet | `/generuj-smlouvu` (uznání dluhu; hlídá, že splátky dají dohromady celý dluh) |
| Spor chceme ukončit dohodou | `/generuj-smlouvu` (dohoda o narovnání) |
| Před prodejem: smlouva o smlouvě budoucí, rezervace, zástava | `/generuj-smlouvu` (záloha nebo závdavek, osud rezervačního poplatku, vklad zástavy) |
| Pronájem bytu: smlouva, výzva nájemci, výpověď bez výpovědní doby | `/generuj-smlouvu` (hlídá jistotu max. 3× nájemné, předchozí výzvu a 3 měsíce dluhu, poučení nájemce) |
| Nový klient: smlouva o právních službách | `/generuj-smlouvu` (včetně doložky o AI a informace o ČAK pro spotřebitele) |
| Kolik je úrok z prodlení, kdy končí lhůta, soudní poplatek, odměna dle tarifu | `/pravni-vypocty` (počítá skript, ne AI; svátky i víkendy) |
| Jiný dokument (žaloba, stanovisko, memorandum, dodatek, uznání dluhu…) | `/pravni-sablony` |
| Žaloba, odpor, odvolání: ať nic nechybí | `/pravni-sablony` (sám projde 5 kontrol: příslušnost, výzva dle § 142a, lhůty a promlčení, poplatky, forma podání) |
| Prověrka LV, checklist koupě, smlouva o smlouvě budoucí, zástavní smlouva, výmaz zástavy | `/pravni-sablony` (sekce Nemovitosti a zajištění) |

## 🎨 Formát a úprava
| Situace | Skill |
|---|---|
| Dostal jsem smlouvu v rozbitém/cizím formátu → chci formát kanceláře | `/formatuj-smlouvu` (text se nemění, jen vzhled) |
| Připomínka k formátu („tohle chci jinak") | nadiktovat Petrovi (GrowLead) → stane se trvalým pravidlem |

## 🔍 Kontrola a revize (než něco podepíšu/pošlu)
| Situace | Skill |
|---|---|
| Protistrana poslala smlouvu — co je v ní špatně? | `/revize-smlouvy` (rizika + návrhy úprav + Word s komentáři) |
| Přišla NDA — podepsat, nebo pozor? | `/triage-nda` (zelená/žlutá/červená za pár minut) |
| Kdo za firmu smí podepsat? Sedí podpisy? | `/kontrola-podpis` (ověří v obchodním rejstříku) |
| Je tenhle záměr v souladu s GDPR/regulací? | `/kontrola-souladu` |
| Mám hotové podání nebo stanovisko: existují všechny citované judikáty a sedí citace? | `/hloubkovy-research citace` (každou spisovou značku dohledá v DirectCase, co nenajde, označí) |

## 🕵️ Prověrky a rešerše
| Situace | Skill |
|---|---|
| Prověřit firmu/protistranu (OR, insolvence, média, web) | `/hloubkovy-research firma <název/IČO>` |
| Zjistit COKOLIV aktuálního (právo i neprávní — dodavatel, produkt, novinka) | `/hloubkovy-research` (vždy s ověřenými zdroji, ne z hlavy AI) |
| Ověřit konkrétní tvrzení / existuje ten judikát? | `/hloubkovy-research verify <tvrzení>` |
| Co všechno máme podepsáno s dodavatelem X? | `/kontrola-dodavatele` |

## ⚖️ Spory, rizika, jednání
| Situace | Skill |
|---|---|
| Přišla výzva/stížnost/incident — jak vážné to je? | `/posouzeni-rizika` (skóre + doporučený postup) |
| Zítra jednání — potřebuju podklady a strategii | `/priprava-jednani` |
| Rutinní právní odpověď (výmaz údajů, dotaz dodavatele…) | `/pravni-odpoved` |
| Ranní přehled / rešerše tématu / krizový režim | `/prehled-pravni` |

## 🔒 Bezpečné používání AI v kanceláři
- **Mlčenlivost (§ 21 zákona o advokacii):** do Clauda dávejte údaje klientů jen v rozsahu nutném pro úkol. Rešerše a obecné dotazy pište anonymně („klient", „společnost A").
- **Trénování:** záleží na typu účtu. U osobního plánu (Claude Pro, Max) vypněte v nastavení soukromí použití konverzací ke zlepšování modelu. Firemní plány (Team, Enterprise) data k trénování podle podmínek Anthropic standardně nepoužívají.
- **Klienti:** ve smlouvě o poskytování právních služeb je vhodné jednou větou uvést, že kancelář používá nástroje AI pod dohledem advokáta (text doložky připraví `/pravni-sablony`).
- **Judikatura:** rozhodnutí, které jste neviděli v DirectCase nebo na webu soudu, do podání nepatří. Na kontrolu je `/hloubkovy-research citace`.

---
**Zlaté pravidlo:** Všechno, co z pluginu vyleze, je NÁVRH — finální slovo má vždy advokát. AI nikdy neposílá nic klientovi.
**Když si nejste jistí:** prostě napište, co řešíte — Claude vybere skill sám.
