# Instalace ak-sladek do Claude (pro JUDr. Sládka)

Plugin funguje v **Claude Cowork** (desktop aplikace Claude s režimem práce se soubory). Potřebuje prostředí, kde Claude umí spouštět kód (generování Wordu).

## Krok 0 — ZAPNOUT code execution (bez toho se Skills sekce vůbec nezobrazí!)
**Settings → Capabilities → zapnout „Code execution and file creation".**
(Ověřeno z oficiálních docs: dokud je vypnuté, Skills/upload v menu nejsou vidět.)

## Krok 1 — Nahrát skilly (ověřený postup, garantovaný na Pro plánu)
K dispozici je složka `ak-sladek-skills/` se **14 samostatnými ZIPy** (jeden skill = jeden ZIP):
1. V Claude appce: levý sidebar → **Customize** → záložka **Skills**.
2. Tlačítko **+** → **„Create skill"** → **„Upload a skill"** → vybrat ZIP.
3. Opakovat pro všechny skilly (start: nastaveni-kancelare, formatuj-smlouvu, generuj-smlouvu, hloubkovy-research — zbytek lze donahrát později).
4. Nahrané skilly se zapínají přepínačem a objeví se po napsání „/" v chatu.

> Alternativa (pokud vaše verze appky nabízí v Customize → Plugins volbu „upload custom plugin file"): nahrát rovnou celý `ak-sladek.zip` — jeden krok místo čtrnácti. Obě cesty vedou ke stejnému výsledku.

## Krok 2 — Připojit konektory (Settings → Connectors)

| Konektor | Jak | Povinné? |
|---|---|---|
| **DirectCase** | přidat URL `https://mcp.directcase.ai` + přihlásit se účtem directcase.ai (free = 10 dotazů na zkoušku) | Doporučené — právo, OR, citace |
| **Exa** (vyhledávání) | přidat URL `https://mcp.exa.ai/mcp` + přihlásit se účtem exa.ai | Pro research |
| **Firecrawl** (čtení webu) | účet na firecrawl.dev → API klíč → přidat URL `https://mcp.firecrawl.dev/VÁŠ-KLÍČ/v2/mcp` | Pro research |
| **Microsoft 365** | standardní M365 konektor Claude + přihlášení účtem kanceláře | Doporučené — Outlook/OneDrive/Word |

> S účty a klíči pomůže Petr (GrowLead) — zabere to ~10 minut najednou.

## Krok 3 — Ověřit funkčnost
Zkuste postupně:
1. *„Naformátuj mi tuhle smlouvu do formátu kanceláře"* + přiložit .docx → `/formatuj-smlouvu`
2. *„Připrav kupní smlouvu a úschovu: prodávající …, kupující …, byt … v k.ú. …, cena …"* → `/generuj-smlouvu`
3. *„Prověř mi firmu XY s.r.o."* → `/hloubkovy-research` (OR + web + média)
4. *„Zkontroluj podpisová práva na téhle smlouvě vůči OR"* → `/kontrola-podpis` (DirectCase skill)

Claude skilly rozpozná sám podle popisu úkolu; slash-command psát nemusíte.

## Co plugin obsahuje (v0.4 — 12 skillů)

**Na míru kanceláři (GrowLead):**
- `/generuj-smlouvu` — kupní smlouva + úschova jako pár z vašich vzorů
- `/formatuj-smlouvu` — jednotný formát kanceláře (7 house rules dle vašeho diktátu)
- `/hloubkovy-research` — top research na COKOLIV (právo i neprávní: dodavatelé, produkty, konkurence) — vždy s citacemi reálně otevřených zdrojů, nikdy z paměti AI

**Právní workflow (DirectCase, upraveno pro ČR):**
revize smlouvy · triage NDA · kontrola podpisu · kontrola dodavatele · compliance check · příprava jednání · posouzení rizika · právní odpovědi · denní přehled

## Doporučené první kroky po instalaci
1. **Spustit `/nastaveni-kancelare`** — 15minutový řízený rozhovor, který nastaví playbook kanceláře (standardní pozice u klauzulí, eskalační pravidla, styl). Bez něj jsou výstupy generické — tohle je nejdůležitější krok.
2. Vyzkoušet research: *„Co je nového v pravidlech advokátních úschov 2026?"*
3. Vaše šablony ze semináře (11/2025) najdete upgradované v `/pravni-sablony` — stejná logika, ale s ověřenými citacemi a formátem kanceláře.

## Tahák
Vytiskněte si [TAHAK.md](TAHAK.md) — jedna stránka „situace → skill" podle fází práce advokáta.

## Důležité upozornění
Výstupy jsou **návrhy ke kontrole advokátem**. Plugin neposkytuje právní poradenství ve smyslu zák. č. 85/1996 Sb. Dokumenty nikdy neposílejte klientům bez vaší kontroly. Research skill označuje neověřená tvrzení — berte je vážně.

---
Správu a údržbu zajišťuje Petr Rohan (GrowLead). Nové typy dokumentů (plná moc, předžalobní výzva, rezervační smlouva) přidáme z vašich vzorů na požádání. Formátovací připomínky se zapisují jako trvalá pravidla — stačí je nadiktovat.
