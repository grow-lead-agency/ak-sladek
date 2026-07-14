# Research Sources — formatuj-smlouvu

## 2026-07-14 — vznik skillu (research fáze legal vertikály)
Kompletní research: `skills/legal/research/02-document-automation-word-format.md`.

Klíčové zdroje (reálně otevřené):
- https://lawvudraft.com/articles/microsoft-word-numbering-lawyers-guide/ — 3vrstvá architektura Word číslování, patologie, fixy
- https://support.litera.com/article/DocXtools-Fixing-Documents-494046 — Litera rebuild-and-restyle pipeline (Discover→AutoFix→Rebuild)
- https://intellek.io/blog/legal-document-numbering/ — named List Styles linked to Paragraph Styles
- https://www.athennian.com/post/field-merge-vs-document-assembly-legal-document-automation — field merge vs assembly
- https://codegive.com/blog/python_docx_numbering_lists_and_multilevel_lists.php — programové numbering XML (abstractNum/num/numPr)
- https://github.com/4teamwork/docxcompose — merge docs se styly

Testovací vstup: Dohoda o narovnání (AI-generovaný draft, falešné číslování) — `_podklady/vzory-sladek/spatne/` (gitignored, PII).
Formátový nosič: kancelar-base.docx odvozený z reálné KS AK Sládek (styly + sectPr, PII stripped).
