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
| Jiný dokument (žaloba, stanovisko, memorandum, dodatek, uznání dluhu…) | `/pravni-sablony` |

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

---
**Zlaté pravidlo:** Všechno, co z pluginu vyleze, je NÁVRH — finální slovo má vždy advokát. AI nikdy neposílá nic klientovi.
**Když si nejste jistí:** prostě napište, co řešíte — Claude vybere skill sám.
