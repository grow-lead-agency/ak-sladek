# DirectCase: limity a volba nástroje

> Jediné místo, kde plugin drží čísla limitů DirectCase. Skilly na tento soubor odkazují a čísla
> neopakují, protože se mění (mezi červencem a říjnem 2026 se zvýšily dvakrát).
> Stav ověřen 2026-10-16 z oficiální dokumentace: https://www.directcase.ai/gb/en/docs/mcp/
> Aktuální stav účtu vždy vrátí `get_entitlements`. Rozhoduje to, co vrátí, ne tato tabulka.

## Tvrdá pravidla (platí pro všechny tiery)

1. **AI search** (`search_caselaw_parallel`, `search_law_parallel`, `search_regulatory_parallel`)
   lze zavolat jen **1× za konverzaci**. Víc dotazů slouč do pole `queries[]` jednoho volání.
2. **Ověření spisové značky, ECLI nebo č. j.** = `search_identifier` (parametr `identifiers[]`),
   pak `get_document` pro plný text. Je to nejlevnější cesta (na Basic 1000 volání) a výchozí
   způsob ověření každé citované judikatury.
3. **Firma podle IČO nebo názvu** = `search_company` (`ico` nebo `nazev`), vrací i stav insolvence.
   Sbírka listin = `search_company_documents` (jen `ico`). `search_identifier` na IČO **nepoužívej**,
   hledá spisové značky.
4. **`get_entitlements`** volej nejvýš **1× za konverzaci** a jen když potřebuješ znát tier
   (např. zda si můžeš dovolit AI search). Na Basic se počítá do limitu 20 volání, takže
   opakované volání v Kroku 0 by kvótu vyčerpalo a skill by mylně usoudil, že konektor chybí.
5. **Lhůty a data**: aktuální datum ber z `get_current_time`, ne z paměti modelu.

## Limity k 2026-10-16 (den / měsíc, rolling 24 h a 30 dní)

| Nástroje | Basic (free) | Pro | Premium | Enterprise |
|---|---|---|---|---|
| AI search (3 parallel nástroje) | 20 | 60 / 400 | 200 / 1000 | 400 / 3000 |
| `search_identifier` | 1000 | 200 / 1200 | 500 / 3000 | 1500 / 9000 |
| `search_keyword`, `search_similar`, `get_document`, `get_law_detail`, `convert_file_to_markdown`, `search_company`, `search_company_documents`, `currency_conversion` | 20 | 200 / 1200 | 500 / 3000 | 1500 / 9000 |
| `track_legislation`, `legislation_changes`, `get_current_time`, `get_entitlements` | 20 | 100 / 600 | 300 / 1800 | 800 / 4800 |

Basic = jedno dlouhé zkušební okno se společným stropem, ne denní limit.

## Úspora volání (pořadí preference)

1. Citace známé sp. zn. → `search_identifier` + `get_document`
2. Znění paragrafu → `get_law_detail` (s parametrem `date` k rozhodnému dni)
3. Doplňující dotaz k už nalezenému → `search_keyword` / `search_similar`
4. Nová rešerše tématu → jeden AI search s polem `queries[]`

`convert_file_to_markdown` čte jen důvěryhodné právní domény (justice.cz, gov.cz, e-sbirka.cz,
soudy, europa.eu, echr) a nově umí OCR skenovaných PDF (např. starší listiny ze Sbírky listin).
Soubory odjinud převáděj lokálně.
