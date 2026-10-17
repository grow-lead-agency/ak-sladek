#!/usr/bin/env python3
"""
Render páru dokumentů (kupní smlouva + smlouva o úschově) z docxtpl šablon.

Použití:
    python render.py <vzor-dir> <data.json> <out-dir>

- <vzor-dir>: složka se šablonami (kupni-smlouva.docx, smlouva-o-uschove.docx, schema.json)
- <data.json>: data případu dle schema.json
- <out-dir>: kam uložit vygenerované dokumenty

Vyžaduje: pip install docxtpl
Konstanty kanceláře se čtou z config/kancelar.json v rootu pluginu.
"""
import json
import re
import sys
from decimal import Decimal
from pathlib import Path

from docxtpl import DocxTemplate

def _find_config() -> Path:
    """kancelar.json: nejdřív skill-lokální (samostatný skill upload), pak plugin root."""
    here = Path(__file__).resolve()
    for cand in (here.parents[1] / "config" / "kancelar.json",
                 here.parents[3] / "config" / "kancelar.json"):
        if cand.exists():
            return cand
    raise FileNotFoundError("config/kancelar.json nenalezen (skill ani plugin root)")


CONFIG = _find_config()

# tvrdé validace nad rámec JSON schématu (konzistence páru)
HOTOVOST_LIMIT = Decimal("270000")
_CASTKA = re.compile(r"^\d{1,3}(\.\d{3})*,\d{2}$")


def _castka(value) -> Decimal | None:
    """'100.000,00' -> Decimal; jiný formát, záporná, NaN nebo prázdná hodnota -> None."""
    if not isinstance(value, str) or not _CASTKA.match(value.strip()):
        return None
    return Decimal(value.strip().replace(".", "").replace(",", "."))


def _gate_hotovost(data: dict) -> list[str]:
    """Zákon č. 254/2004 Sb., § 4: hotovost nad 270.000,00 Kč zakázána, platby téže osobě
    za jeden kalendářní den se sčítají. Vzor kupní smlouvy popisuje zálohu V HOTOVOSTI."""
    cena = data.get("cena", {})
    zaloha = _castka(cena.get("zaloha"))
    if zaloha is None:
        return [f"cena.zaloha ({cena.get('zaloha')!r}) chybí nebo není částka ve formátu '100.000,00'"]
    jine = cena.get("hotovost_tentyz_den", "0,00")
    jine_kc = _castka(jine)
    if jine_kc is None:
        return [f"cena.hotovost_tentyz_den ({jine!r}) není částka ve formátu '100.000,00'"]
    if zaloha + jine_kc > HOTOVOST_LIMIT:
        return [f"GATE hotovost: záloha {cena.get('zaloha')} Kč v hotovosti"
                + (f" + další hotovost téhož dne {jine} Kč" if jine_kc else "")
                + " překračuje 270.000,00 Kč. Zákon č. 254/2004 Sb., § 4 zakazuje takovou platbu "
                "v hotovosti (platby téže osobě za jeden den se sčítají). Vyšší zálohu platit "
                "bezhotovostně nebo do úschovy; změnu textu kupní smlouvy posoudí advokát."]
    return []


def validate(data: dict) -> list[str]:
    errors = []
    for strana in ("prodavajici", "kupujici"):
        s = data.get(strana, {})
        for req in ("radek1", "radek2", "podpis", "email"):
            if not s.get(req):
                errors.append(f"{strana}.{req} chybí")
    # výplatní účet příjemce (prodávající) je v SÚ povinný
    prod = data.get("prodavajici", {})
    radky = " ".join(str(prod.get(k) or "") for k in ("radek3", "radek4", "radek5"))
    if "č.ú." not in radky and "č. ú." not in radky:
        errors.append("prodavajici: chybí řádek s č.ú. (výplatní účet úschovy — povinný v SÚ)")
    # konzistence částek
    if data.get("cena", {}).get("doplatek") != data.get("uschova", {}).get("castka"):
        errors.append(f"cena.doplatek ({data.get('cena',{}).get('doplatek')}) != uschova.castka ({data.get('uschova',{}).get('castka')})")
    errors.extend(_gate_hotovost(data))
    if not data.get("nemovitost", {}).get("polozky"):
        errors.append("nemovitost.polozky prázdné")
    return errors


def build_context(data: dict, cfg: dict, doc_key: str) -> dict:
    ctx = dict(data)
    ctx["advokat"] = cfg["advokat"]
    uschova = dict(cfg["uschova_default"])
    uschova.update(data.get("uschova", {}))
    ctx["uschova"] = uschova
    lhuty = dict(cfg["lhuty_default"])
    lhuty.update(data.get("lhuty", {}))
    ctx["lhuty"] = lhuty
    ctx["stejnopisy"] = data.get("stejnopisy", {}).get(doc_key) if isinstance(data.get("stejnopisy"), dict) \
        else cfg["stejnopisy_default"][doc_key]
    return ctx


def main() -> int:
    if len(sys.argv) != 4:
        print(__doc__)
        return 2
    vzor_dir, data_path, out_dir = (Path(a) for a in sys.argv[1:4])
    data = json.loads(data_path.read_text(encoding="utf-8"))
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))

    errors = validate(data)
    if errors:
        print("VALIDACE SELHALA — dokumenty NEBYLY vygenerovány:")
        for e in errors:
            print(f"  ✗ {e}")
        return 1

    out_dir.mkdir(parents=True, exist_ok=True)
    generated = []
    for tpl_name in ("kupni-smlouva", "smlouva-o-uschove"):
        tpl_path = vzor_dir / f"{tpl_name}.docx"
        if not tpl_path.exists():
            print(f"  ! šablona {tpl_path} neexistuje, přeskakuji")
            continue
        tpl = DocxTemplate(str(tpl_path))
        tpl.render(build_context(data, cfg, tpl_name))
        out = out_dir / f"{tpl_name}-navrh.docx"
        tpl.save(str(out))
        generated.append(out)
        print(f"  ✓ {out}")

    if "hotovost_tentyz_den" not in data.get("cena", {}):
        print("  ⚠ HOTOVOST: ověř, že stejná osoba téhož dne nezaplatila v hotovosti další částku (§ 4 odst. 4 zák. 254/2004 Sb.); jinak ji uveď v cena.hotovost_tentyz_den.")
    print(f"\nHOTOVO — {len(generated)} dokumenty. UPOZORNĚNÍ: Jde o návrhy ke kontrole advokátem, ne finální dokumenty.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
