# Research Sources — hloubkovy-research

## 2026-10-16 — režim citace, search_company pro IČO, limity
- https://www.directcase.ai/gb/en/docs/mcp/ — search_identifier = sp. zn./ECLI/č. j. (ne IČO), Basic 1000; get_entitlements Basic 20
- https://www.directcase.ai/cz/cs/news/find-decisions-by-case-number — vyhledání podle sp. zn. zdarma (27. 7. 2026)
- https://github.com/anthropics/claude-for-legal/pull/127 — cite-check (existence + obsah, nenalezeno = FAIL), myšlenka převzata, text vlastní

## 2026-07-14 — vznik (fork)
Fork interního GrowLead agenta `research-loop` (agents-and-skills/skills/research/research-loop/agent.md).
Adaptace: CLI agent → Cowork SKILL.md; tool routing Exa (mcp.exa.ai) + Firecrawl (mcp.firecrawl.dev hosted) + DirectCase (mcp.directcase.ai); přidána právní anti-halucinační vrstva (citace § jen z DirectCase/primárních zdrojů — kontext: sankce za AI halucinace, viz skills/legal/research/03).
Externí reference: https://docs.firecrawl.dev (hosted MCP URL pattern), https://docs.exa.ai (MCP endpoint), https://www.directcase.ai/gb/en/docs/mcp/
