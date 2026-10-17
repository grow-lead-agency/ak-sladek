"""Tvrdé podmínky konkrétního vzoru, nenahrazují právní přezkum LV."""
import re
from datetime import date

MONEY = re.compile(r'(?:0|[1-9]\d{0,2}(?:\.\d{3})*),\d{2}\Z')


def _text(value):
    return isinstance(value, str) and bool(value.strip())


def _money(value):
    return _text(value) and bool(MONEY.fullmatch(value)) and float(value.replace('.', '').replace(',', '.')) > 0


def _obj(value):
    return value if isinstance(value, dict) else {}


def gate(data):
    errors, warnings = [], []
    if not isinstance(data, dict):
        return ['GATE § 1312 OZ: data musí být objekt.'], []
    for key in ('veritel', 'zastavce'):
        side = _obj(data.get(key))
        for field in ('radek1', 'radek2', 'podpis'):
            if not _text(side.get(field)):
                errors.append(f'GATE § 1312 OZ: chybí identifikace či podpis {key}.{field}.')
    if type(data.get('zastavce_je_dluznik')) is not bool:
        errors.append('GATE § 1312 OZ: určete zastavce_je_dluznik jako true nebo false.')
    elif not data['zastavce_je_dluznik']:
        debtor = _obj(data.get('dluznik'))
        if not all(_text(debtor.get(k)) for k in ('radek1', 'radek2')):
            errors.append('GATE § 1312 OZ: Zástavce není Dlužník, chybí úplná identifikace Dlužníka.')
        warnings.append('§ 1309 a § 1312 OZ: Zástavce není osobním Dlužníkem. Advokát ověří jeho poučení, rozsah majetkového rizika a případný střet zájmů.')
    debt = _obj(data.get('dluh'))
    mode = debt.get('rezim')
    if mode not in ('existujici', 'budouci'):
        errors.append('GATE § 1311 a § 1312 OZ: chybí nebo není znám režim dluh.rezim.')
    if not _text(debt.get('duvod')):
        errors.append('GATE § 1312 OZ: chybí určitý právní důvod a vymezení zajišťovaného dluhu.')
    amount = 'nejvyssi_castka' if mode == 'budouci' else 'vyse'
    if not _money(debt.get(amount)):
        errors.append(f'GATE § 1312 OZ: dluh.{amount} musí být kladná částka ve formátu 1.000,00; bez výše či limitu zajištění nelze pokračovat.')
    for field in ('splatnost', 'prislusenstvi'):
        if not _text(debt.get(field)):
            errors.append(f'GATE § 1312 OZ: chybí dluh.{field}; u příslušenství uveďte výslovně i vyloučení, není-li zajištěno.')
    if mode == 'budouci':
        try:
            start = date.fromisoformat(debt.get('obdobi_od', ''))
            end = date.fromisoformat(debt.get('obdobi_do', ''))
            if start > end:
                raise ValueError
        except (ValueError, TypeError):
            errors.append('GATE § 1311 OZ: budoucí dluhy vyžadují platné období vzniku od/do ve formátu RRRR-MM-DD v časovém pořadí.')
    prop = _obj(data.get('nemovitost'))
    for field in ('ku_text', 'urad_kraj', 'pracoviste', 'lv', 'zatizeni'):
        if not _text(prop.get(field)):
            errors.append(f'GATE § 1312 OZ a § 8 zákona č. 256/2013 Sb.: chybí nemovitost.{field}.')
    items = prop.get('polozky')
    if not isinstance(items, list) or not items or any(not isinstance(i, dict) or not _text(i.get('text')) or type(i.get('odrazka')) is not bool for i in items):
        errors.append('GATE § 1312 OZ a § 8 zákona č. 256/2013 Sb.: chybí úplný popis Zástavy dle LV v nemovitost.polozky[].')
    ban = data.setdefault('zakaz', {'zapnut': False})
    if not isinstance(ban, dict) or type(ban.get('zapnut')) is not bool:
        errors.append('GATE § 1761 OZ: zakaz.zapnut musí být true nebo false.')
    elif ban['zapnut']:
        try:
            date.fromisoformat(ban.get('do', ''))
        except (ValueError, TypeError):
            errors.append('GATE § 1761 OZ: zákaz musí mít určitý konec zakaz.do (RRRR-MM-DD).')
        if not _text(ban.get('zajem')):
            errors.append('GATE § 1761 OZ: chybí zájem hodný právní ochrany a zdůvodnění přiměřenosti doby zákazu.')
        warnings.append('§ 1761 OZ a § 11 odst. 1 písm. n) zákona č. 256/2013 Sb.: zákaz působí vůči třetím osobám jako věcné právo vzniklé vkladem. Advokát ověří přiměřenost doby a chráněný zájem; samotný smluvní zákaz dle § 1761 zavazuje jen strany. Zvláštní účinky zákazu zřídit zástavní právo viz § 1309 odst. 2 OZ.')
    for field in ('pojisteni', 'vklad_zajisti', 'rok'):
        if not _text(data.get(field)):
            errors.append(f'GATE úplnosti vzoru (§ 1312 OZ): chybí {field}.')
    warnings.extend([
        '§ 1316 OZ a § 11 zákona č. 256/2013 Sb.: zástavní právo vznikne až vkladem. Ověřte aktuální LV, vlastnictví, oprávnění zatížit věc, potřebné souhlasy a pořadí práv.',
        '§ 7 odst. 2 zákona č. 256/2013 Sb.: pro vklad připravte soukromou vkladovou listinu s úředně ověřenými podpisy. Bez ověření je nutné prokázat pravost podpisů zákonným postupem; samotný prostý sken není řádnou elektronickou vkladovou listinou.',
    ])
    return errors, warnings
