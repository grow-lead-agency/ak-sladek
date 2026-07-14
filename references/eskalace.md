# Eskalační pravidla (Escalation-Router)

> Sdílená pravidla pro VŠECHNY skilly pluginu — kdy smí AI pracovat samostatně (s následnou
> kontrolou advokáta) a kdy MUSÍ okamžitě eskalovat na advokáta a nepokračovat v draftu.
> Konkrétní prahy doplní /nastaveni-kancelare do legal.local.md (sekce Eskalační triggery).

## 🟢 AI může draftovat (advokát kontroluje výstup)
- Standardní převod bytu/pozemku FO↔FO/PO dle vzorů kanceláře
- Formátování dokumentů, rešerše, KYC, triage NDA, šablonové odpovědi
- Předžalobní výzva / plná moc / uznání dluhu dle vzoru s kompletními fakty

## 🔴 OKAMŽITÁ eskalace — AI nedraftuje, jen shrne situaci advokátovi
- **Nestandardní úschova** (jiná struktura než vzor, více výplat, podmínky mimo LV standard)
- **Sporná vlastnická struktura** (poznámka spornosti, probíhající řízení, duplicitní zápis, exekuce/insolvence na LV)
- **Cizinecký prvek** (zahraniční strana, cizí právo, přeshraniční platba)
- **Insolvence/likvidace protistrany** (z KYC)
- **Jednání za PO „dva jednatelé společně"** s jediným podpisem
- **Nezletilí, opatrovnictví, SJM komplikace** (rozvod, zúžení SJM)
- Cokoliv, kde si AI není jistá právní kvalifikací — **nejistota = eskalace, ne odhad**
- Prahy z legal.local.md (spor > X Kč, sankční riziko regulátora…)

## Jak eskalovat
1. STOP draftu. 2. Shrň fakta + co je nestandardní + možné směry (bez závěru). 3. Explicitně: „Toto vyžaduje posouzení advokátem — nedraftuju."
