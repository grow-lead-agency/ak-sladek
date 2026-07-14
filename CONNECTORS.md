# Konektory

## Jak fungují odkazy na nástroje

Soubory pluginu používají `~~kategorie` jako zástupný symbol pro nástroj, který si v dané kategorii připojíte. Například `~~email` může znamenat Outlook nebo Gmail — plugin si vybere připojený MCP server v kategorii.

Pluginy jsou **nezávislé na konkrétním nástroji** — popisují workflow v pojmech kategorií (e-mail, cloud storage, elektronický podpis atd.), nikoli konkrétních produktů. Co reálně funguje, závisí na tom, které MCP servery si v Claude / Cowork připojíte.

---

## Doporučený stack pro českého advokáta a inhouse právníka

Plugin je vyladěný pro typický stack právní praxe v ČR. Pokud chcete plnou funkčnost, doporučujeme tyto konektory:

| Kategorie | Zástupný symbol | Doporučené (CZ stack) | Alternativy |
|---|---|---|---|
| **Právní zdroje ČR / EU** | `~~pravni-zdroje` | **DirectCase MCP** (judikatura, zákony, regulatorika, OR) | vlastní právní databáze |
| **E-mail** | `~~email` | **Outlook** (M365), **Gmail** | jiný IMAP klient |
| **Cloud storage** | `~~cloud-storage` | **Google Drive**, **OneDrive** (M365) | Dropbox, Box, SharePoint |
| **Kancelářský balík** | `~~office-suite` | **Microsoft 365** (Word, Excel, PowerPoint), **Google Workspace** | LibreOffice |
| **Elektronický podpis** | `~~e-signature` | **Signi** (česká služba, eIDAS-kompatibilní) | DocuSign, Adobe Sign |
| **Datová schránka** | `~~datova-schranka` | **ISDS** (Informační systém datových schránek) | Czech POINT |
| **Týmová komunikace** | `~~chat` | **Microsoft Teams**, **Slack** | jiný team chat |
| **Kalendář** | `~~calendar` | **Outlook Calendar**, **Google Calendar** | jiný kalendář |
| **CLM** (správa smluv) | `~~CLM` | (v ČR málo rozšířené) | Ironclad, ContractBook, Agiloft |
| **CRM** | `~~CRM` | **HubSpot**, **Pipedrive** | Salesforce |
| **Řízení projektů a úkolů** | `~~project-tracker` | **Asana**, **Trello**, **Jira** | Linear, Monday |

---

## Nejdůležitější tři konektory

Pokud máte rozpočet jen na pár MCP serverů, doporučujeme **v tomto pořadí**:

### 1. DirectCase MCP — bez něj plugin ztrácí ~60 % funkčnosti

`DirectCase` je MCP server specializovaný na české a evropské právo. Obsahuje cca 1,4 milionu ověřených právních zdrojů:

- **Judikatura** českých soudů (NS, ÚS, NSS, vrchní a krajské soudy).
- **Právní předpisy ČR** (zákony, nařízení vlády, vyhlášky) ve znění platném ke dni dotazu.
- **Regulatorní dokumenty** (stanoviska ČNB, ÚOOÚ, ÚOHS, ČTÚ, SÚKL, NÚKIB atd.).
- **Dokumenty obchodního rejstříku** a veřejných rejstříků (insolvenční, živnostenský).

**Návod k instalaci:** <https://www.directcase.ai/cs/news/prvni-v-cesku-pravo-primo-ve-vasem-ai-prostredi-pres-mcp>

**Aktuální seznam indexovaných zdrojů:** <https://www.directcase.ai/>

### 2. Microsoft 365 nebo Google Workspace

Pro práci s reálnými dokumenty:

- **Word / Docs** — skill `/revize-smlouvy` generuje Word výstup s barevnými komentáři.
- **Excel / Sheets** — vhodné pro registr rizik (`/posouzeni-rizika`).
- **Outlook / Gmail** — skilly `/prehled-pravni`, `/pravni-odpoved`, `/kontrola-dodavatele` prohledávají e-mail kvůli kontextu.
- **OneDrive / Drive** — úložiště smluv a interních memorand.

### 3. Datová schránka (ISDS) — klíčová pro ČR

V českém právním prostředí je **datová schránka klíčová pro doručování právních úkonů** — jak vůči orgánům veřejné moci, tak mezi podnikateli s povinně zřízenou DS (zák. č. 300/2008 Sb., od 2023 rozšířený okruh povinných subjektů).

Pokud existuje MCP konektor pro ISDS, doporučujeme ho připojit — skill `/kontrola-podpis` ho využije pro doručování formálních úkonů a `/pravni-odpoved` pro formální odpovědi.

---

## Elektronický podpis: Signi vs. DocuSign

V českém kontextu je důležité rozlišit dvě hlavní platformy:

- **Signi** (česká služba) — eIDAS-kompatibilní elektronický podpis (zaručený nebo kvalifikovaný). Preferovaná pro **české subjekty a úkony vůči veřejné správě**. Levnější pro běžnou agendu, nativně podporuje českou identitu (BankID, NIA).
- **DocuSign** — globální. Vhodný pro **mezinárodní smlouvy** a americké / britské protistrany. V ČR funguje, ale pro úkony vůči veřejné správě často nepostačuje (kvalifikovaný podpis vyžaduje další kroky).

Skill `/kontrola-podpis` umí pracovat s oběma; pokud chcete podpis u kvalifikovaného úkonu, skill upozorní, jaká forma je nutná (viz § 560 a násl. OZ, zák. č. 297/2016 Sb., nař. eIDAS).

---

## Co se stane, pokud konektor není připojený

Plugin pracuje **s tím, co je dostupné**. Pokud daný konektor (`~~email`, `~~CLM`, `~~chat` atd.) připojený není, skill v hlavičce výstupu jasně označí, **které zdroje nebyly prohledány**, a doporučí uživateli buď konektor připojit, nebo si chybějící zdroje dohledat ručně.

Bez DirectCase MCP plugin funguje, ale ztrácí citace judikatury, KYC z OR a ověřená znění zákonů. Pro plnou funkci silně doporučujeme alespoň DirectCase + jednu kancelářskou platformu (M365 nebo Workspace).
