# ak-sladek — AI plugin pro AK Sládek

Plugin pro Claude (Cowork / Claude Code) na míru advokátní kanceláři **JUDr. Petr Sládek** (realitní právo, advokátní úschovy). Kompletní balík: generování a formátování dokumentů z vlastních vzorů kanceláře + 9 právních workflow skillů (DirectCase, MIT) + top research agent.

## Skilly (14)

**Taxonomie podle použití** (plná mapa situace → skill: [TAHAK.md](TAHAK.md)):

| Fáze práce | Skilly |
|---|---|
| 🏁 Nastavení | nastaveni-kancelare |
| 📄 Tvorba | generuj-smlouvu · pravni-sablony |
| 🎨 Formát | formatuj-smlouvu |
| 🔍 Kontrola | revize-smlouvy · triage-nda · kontrola-podpis · kontrola-souladu |
| 🕵️ Prověrky | hloubkovy-research · kontrola-dodavatele |
| ⚖️ Spory & provoz | posouzeni-rizika · pravni-odpoved · priprava-jednani · prehled-pravni |

### GrowLead — na míru kanceláři
| Skill | Command | Co dělá |
|---|---|---|
| Nastavení kanceláře | `/nastaveni-kancelare` | **Spustit první.** Cold-start interview (15 min) → playbook kanceláře do `legal.local.md`. Bez něj jsou výstupy generické. |
| Právní šablony | `/pravni-sablony` | Knihovna úloh (žaloba, stanovisko, memorandum, dodatek, anonymizace…) — upgrade šablon ze semináře AI pro právníky (11/2025) + routing na specializované skilly. |
| Generuj smlouvu | `/generuj-smlouvu` | Kupní smlouva + úschova (pár) · plná moc · předžalobní výzva (kódový §142a gate). Fakta → JSON → deterministický render ze vzoru. AI nikdy nepíše právní text. |
| Formátuj smlouvu | `/formatuj-smlouvu` | Cizí/rozbitý dokument → jednotný formát kanceláře (rebuild-and-restyle, text doslovně zachován, house rules dle diktátu JUDr. Sládka). |
| Hloubkový research | `/hloubkovy-research` | **Univerzální research agent** (fork GrowLead research-loop) — Exa search + Firecrawl scrape + DirectCase pro právo. Každé tvrzení s citací reálně otevřeného zdroje. Režimy: research / verify / firma. Pro právní i neprávní témata. |

### DirectCase pravo-skills v1.1.0 (import, MIT — viz LICENSE-directcase-pravo-skills)
| Skill | Command | Co dělá |
|---|---|---|
| Revize smlouvy | `/revize-smlouvy` | Revize proti playbooku, redlines, Word s barevnými komentáři, KYC protistrany |
| Triage NDA | `/triage-nda` | Klasifikace NDA: ZELENÁ / ŽLUTÁ / ČERVENÁ |
| Kontrola podpisu | `/kontrola-podpis` | Ověření podpisových práv v OR + checklist před podpisem |
| Kontrola dodavatele | `/kontrola-dodavatele` | Konsolidovaný přehled smluv s dodavatelem + KYC |
| Kontrola souladu | `/kontrola-souladu` | Compliance check (GDPR, NIS2, DORA, AI Act…) |
| Příprava jednání | `/priprava-jednani` | Briefing na jednání + profil protistrany |
| Posouzení rizika | `/posouzeni-rizika` | Matice závažnost × pravděpodobnost + memorandum |
| Právní odpověď | `/pravni-odpoved` | Šablonové odpovědi (DSR, litigation hold, předvolání…) |
| Přehled právní | `/prehled-pravni` | Denní / tematický / krizový přehled |

## Konektory (`.mcp.json`)

| Konektor | K čemu | Auth |
|---|---|---|
| **DirectCase** | Právo ČR/EU: judikatura, zákony, OR, regulátoři | OAuth (účet directcase.ai) |
| **Firecrawl** | Čtení webu pro research | API klíč (firecrawl.dev) |
| **Exa** | Neuronové vyhledávání pro research | OAuth (exa.ai) |
| **Microsoft 365** | Outlook, OneDrive, Word | OAuth (účet kanceláře) |
| **DocuSign** | E-podpis (volitelné) | OAuth |

## Princip: AI = plnič dat a orchestrátor, ne autor

1. Advokát nadiktuje fakta / přiloží dokument.
2. AI vytěží data, zvaliduje (chybí pole → STOP a doptá se), u práva groundinguje přes DirectCase.
3. Deterministické skripty (`scripts/`) vyplní **schválené vzory kanceláře** → hotové .docx.
4. Výstup = vždy **návrh ke kontrole advokátem** (zák. č. 85/1996 Sb.). Nikdy přímo klientovi.

## Konfigurace

- `config/kancelar.json` — konstanty kanceláře (advokát, účet úschovy, lhůty, stejnopisy). Změna zde = všude.
- `references/house-rules.md` — 7 formátovacích pravidel kanceláře (diktát JUDr. Sládka 14. 7. 2026).
- `legal.local.example.md` — šablona playbooku pro DirectCase review skilly (zkopírovat jako `legal.local.md` + doplnit pozice kanceláře).
- `CONNECTORS.md` — jak fungují `~~kategorie` zástupné symboly v DirectCase skillech.

## Údržba

Plugin spravuje GrowLead (Petr Rohan). Zdroj: repo `agents-and-skills`, `skills/legal/`.
Instalace: viz [INSTALL.md](INSTALL.md).

---
*Verze 0.6.1 (2026-07-14) — audit skill-and-agent-master: 30 oprav (MCP tool reference vs. oficiální DirectCase API, rate-limit logika 1×/konverzaci, get_entitlements/get_current_time). Předchozí: + vzory plná moc a předžalobní výzva (kódové gates §142a/katastr), + references/eskalace.md (Escalation-Router), + datum-disciplína DirectCase; + nastaveni-kancelare (cold-start interview, Anthropic pattern), + pravni-sablony (upgrade Sládkových seminárních šablon); + hloubkovy-research (fork research-loop), + 9 DirectCase pravo-skills (MIT, origin-tracked, review OK), + Firecrawl/Exa konektory. House rules v0.3 zachovány. Pokrytí generátoru: převod nemovitosti (KS+SÚ pár); varianty (hypotéka, zprostředkovatel, SJM) viz Omezení v SKILL.md.*
