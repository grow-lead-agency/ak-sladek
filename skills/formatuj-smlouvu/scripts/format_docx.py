#!/usr/bin/env python3
"""
Formátovač: JSON model dokumentu -> .docx v jednotném rukopisu kanceláře AK Sládek.

Použití:
    python format_docx.py <model.json> <vystup.docx>

Rukopis kanceláře (odvozeno z reálných vzorů):
- Tahoma 10,5 pt, blokové zarovnání (justify)
- Titul + články centrovaně bold; číslo článku (I.) a název na samostatných řádcích
- Body článků: SKUTEČNÉ Word číslování (decimal %1., odsazení 360/360 twips),
  restart číslování v každém článku
- **text** v modelu = bold run (definované pojmy, částky)

Model JSON:
{
  "titul": "DOHODA O NAROVNÁNÍ",
  "nazev_listiny": "Dohoda o narovnání",   (volitelné, do patičky; jinak se odvodí z titulu)
  "pravni_hlavicka": "(dále jen „**Dohoda**“) uzavřená podle ... mezi smluvními stranami:",
  "strany": [
    {"radky": ["**Jméno, r.č. ...**", "trvale bytem ..."], "dale_jen": "(dále jen „**X**“)"},
    ...
  ],
  "uvod": "v tomto znění:",
  "clanky": [
    {"cislo": "I.", "nazev": "Skutkový stav", "cislovane": true, "body": ["text bodu 1", ...]},
    ...
  ],
  "misto_datum": "V ________________ dne ________ 2026",
  "podpisy": {
    "leva":  {"jmeno": "...", "role": "...", "zastupce": null},
    "prava": {"jmeno": "...", "role": "...", "zastupce": "Jméno, jednatel"}
  }
}
"""
import json
import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml
from docx.oxml.ns import qn
from docx.shared import Pt

FONT = "Tahoma"
SIZE = Pt(10.5)
BASE_TPL = Path(__file__).resolve().parent.parent / "base" / "kancelar-base.docx"

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

# Patička kanceláře = číslo stránky + název listiny. Šablona ho nese z kupní smlouvy,
# proto ho každý dokument přepíše na svůj název (mění se jen text, formát zůstává).
FOOTER_TITLE_BASE = "Kupní smlouva"


def set_footer_title(doc, title: str) -> int:
    """Nahradí název listiny v patičkách šablony. Vrací počet nahrazení (0 = patička bez názvu)."""
    from docx.opc.constants import RELATIONSHIP_TYPE as RT
    n = 0
    for rel in doc.part.rels.values():
        if rel.reltype == RT.FOOTER:
            for t in rel.target_part.element.iter(qn("w:t")):
                if (t.text or "").strip() == FOOTER_TITLE_BASE:
                    t.text = f"{title} "
                    n += 1
    return n


def footer_title_from(titul: str) -> str:
    """„DOHODA O NAROVNÁNÍ" -> „Dohoda o narovnání" (název listiny do patičky)."""
    s = " ".join(titul.replace("*", "").split())
    return s[:1].upper() + s[1:].lower()


# ---------- numbering (skutečné, per-článek restart) ----------

ABSTRACT_ID = 100

ABSTRACT_XML = f'''<w:abstractNum xmlns:w="{W}" w:abstractNumId="{ABSTRACT_ID}">
  <w:multiLevelType w:val="singleLevel"/>
  <w:lvl w:ilvl="0">
    <w:start w:val="1"/>
    <w:numFmt w:val="decimal"/>
    <w:lvlText w:val="%1."/>
    <w:lvlJc w:val="left"/>
    <w:pPr><w:ind w:left="360" w:hanging="360"/></w:pPr>
    <w:rPr><w:rFonts w:ascii="{FONT}" w:hAnsi="{FONT}"/><w:sz w:val="21"/><w:szCs w:val="21"/></w:rPr>
  </w:lvl>
</w:abstractNum>'''


def ensure_numbering(doc: Document) -> "NumberingAllocator":
    part = doc.part.numbering_part
    return NumberingAllocator(part.element)


class NumberingAllocator:
    """Přidá kancelářský abstractNum a vydává nové numId (restart per článek)."""

    def __init__(self, numbering_el):
        self.el = numbering_el
        existing = [int(n.get(qn("w:numId"))) for n in numbering_el.findall(qn("w:num"))]
        self.next_id = max(existing, default=0) + 1
        # abstractNum musí být před všemi <w:num>
        abstract = parse_xml(ABSTRACT_XML)
        nums = numbering_el.findall(qn("w:num"))
        if nums:
            nums[0].addprevious(abstract)
        else:
            numbering_el.append(abstract)

    def new_num(self) -> int:
        nid = self.next_id
        self.next_id += 1
        num_xml = f'''<w:num xmlns:w="{W}" w:numId="{nid}">
  <w:abstractNumId w:val="{ABSTRACT_ID}"/>
  <w:lvlOverride w:ilvl="0"><w:startOverride w:val="1"/></w:lvlOverride>
</w:num>'''
        self.el.append(parse_xml(num_xml))
        return nid


# ---------- text helpers ----------

def normalize_amounts(text: str) -> str:
    """'200.000 Kč' -> '200.000,00 Kč' (haléře na 2 místa, house style).
    Částky s already-present ',NN' nechává být."""
    return re.sub(r"(\d(?:[\d.]*\d)?)(?<!,\d\d)(\s?Kč)",
                  lambda m: (m.group(1) if "," in m.group(1) else m.group(1) + ",00") + m.group(2),
                  text)


def add_runs(p, text: str) -> None:
    """Rozparsuje **bold** markup na runy, Tahoma 10.5 všude."""
    for i, seg in enumerate(re.split(r"\*\*", text)):
        if not seg:
            continue
        r = p.add_run(seg)
        r.font.name = FONT
        r.font.size = SIZE
        r.bold = (i % 2 == 1)


def _tight(p) -> None:
    """House style: bez mezer, jednoduché řádkování (jako vzor 'Bez mezer')."""
    try:
        p.style = p.part.document.styles["No Spacing"]
    except (KeyError, AttributeError):
        pass
    p.paragraph_format.space_after = 0
    p.paragraph_format.space_before = 0
    p.paragraph_format.line_spacing = 1.0


def para(doc, text="", align=None, bold=False, numbered_id=None):
    p = doc.add_paragraph()
    _tight(p)
    if align:
        p.alignment = align
    if numbered_id is not None:
        numpr = parse_xml(
            f'<w:numPr xmlns:w="{W}"><w:ilvl w:val="0"/><w:numId w:val="{numbered_id}"/></w:numPr>')
        p._p.get_or_add_pPr().append(numpr)
    if text:
        if bold and "**" not in text:
            text = f"**{text}**"
        add_runs(p, normalize_amounts(text))
    return p


# ---------- builder ----------

def build(model: dict, out_path: Path) -> None:
    doc = Document(str(BASE_TPL))
    set_footer_title(doc, model.get("nazev_listiny") or footer_title_from(model["titul"]))
    alloc = ensure_numbering(doc)
    C, J = WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.JUSTIFY

    # titul + právní hlavička (house rule: prázdný řádek pod hlavním nadpisem)
    para(doc, model["titul"], align=C, bold=True)
    para(doc)
    if model.get("pravni_hlavicka"):
        para(doc, model["pravni_hlavicka"], align=J)
    para(doc)

    # strany
    strany = model.get("strany", [])
    for idx, s in enumerate(strany):
        for r in s["radky"]:
            para(doc, r)
        para(doc)
        para(doc, s["dale_jen"])
        if idx < len(strany) - 1:
            para(doc)
            # house rule (Sládek 2026-07-14): "a" mezi stranami doleva
            para(doc, "a", bold=True)
            para(doc)
    para(doc)
    if model.get("uvod"):
        # house rule (Sládek 2026-07-14): "v tomto znění:" vždy na střed, bez boldu
        para(doc, model["uvod"], align=C)
        para(doc)

    # články
    for cl in model["clanky"]:
        para(doc, cl["cislo"], align=C, bold=True)
        if cl.get("nazev"):
            para(doc, cl["nazev"], align=C, bold=True)
        nid = alloc.new_num() if cl.get("cislovane", True) and len(cl["body"]) > 1 else None
        for bod in cl["body"]:
            para(doc, bod, align=J, numbered_id=nid)
        para(doc)

    # místo/datum + podpisy (2 zarovnané sloupce přes tabulku bez ohraničení —
    # podtržítko, jméno i role vždy přesně pod sebou)
    para(doc)
    para(doc, model.get("misto_datum", "V ________________ dne ________"))
    for _ in range(4):
        para(doc)
    pods = model["podpisy"]
    leva, prava = pods["leva"], pods["prava"]
    table = doc.add_table(rows=1, cols=2)
    table.autofit = True
    for col, strana in ((0, leva), (1, prava)):
        cell = table.rows[0].cells[col]
        cell.paragraphs[0].text = ""
        rows = ["_______________________", f"**{strana['jmeno']}**"]
        if strana.get("zastupce"):
            rows.append(strana["zastupce"])
        rows.append(strana.get("role", ""))
        if model.get("overene_podpisy"):
            rows.append("(ověřený podpis)")
        first = True
        for line in rows:
            p = cell.paragraphs[0] if first else cell.add_paragraph()
            first = False
            _tight(p)
            add_runs(p, line)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(out_path))
    print(f"  ✓ {out_path}")


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    model = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    build(model, Path(sys.argv[2]))
    print("\nHOTOVO — návrh v jednotném formátu kanceláře. Zkontroluj obsah — formátovač NEMĚNÍ text, jen vzhled a strukturu.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
