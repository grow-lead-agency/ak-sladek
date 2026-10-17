"""Kontrola dat konkrétního návrhu smlouvy; výchozí AI doložka je zapnutá."""
import re

MONEY = re.compile(r'(?:0|[1-9]\d{0,2}(?:\.\d{3})*),\d{2}\Z')


def _text(value):
    return isinstance(value, str) and bool(value.strip())


def _money(value, zero=False):
    if not _text(value) or not MONEY.fullmatch(value):
        return False
    amount = float(value.replace('.', '').replace(',', '.'))
    return amount >= 0 if zero else amount > 0


def gate(data):
    errors, warnings = [], []
    if not isinstance(data, dict):
        return ['GATE § 2430 OZ: data musí být objekt.'], []
    if not _text(data.get('predmet_sluzeb')):
        errors.append('GATE § 2430 OZ: chybí určitý předmět právních služeb.')
    fee = data.get('odmena') if isinstance(data.get('odmena'), dict) else {}
    if fee.get('zpusob') not in ('hodinova', 'pausalni', 'ukonova'):
        errors.append('GATE odměny (§ 22 ZA, § 1 a § 3 vyhlášky č. 177/1996 Sb.): chybí podporovaný způsob odměny. Tento vzor vyžaduje výslovné vymezení.')
    if not _money(fee.get('vyse')):
        errors.append('GATE odměny (§ 22 ZA, § 3 a § 6 vyhlášky č. 177/1996 Sb.): chybí kladná výše/sazba odměny ve formátu 1.000,00. Bezplatnou pomoc tento vzor nepokrývá.')
    if fee.get('zpusob') == 'ukonova':
        if not _text(fee.get('tarifni_zaklad')):
            errors.append('GATE § 6 vyhlášky č. 177/1996 Sb.: chybí tarifní hodnota nebo jiný rozhodný podklad a výpočet sazby odměny.')
        warnings.append('§ 6 a § 11 vyhlášky č. 177/1996 Sb.: advokát ověří tarifní podklad, aktuální sazbu, zvláštní pravidla a plné či poloviční úkony. Gate sazbu sám nepočítá.')
    for field in ('dph_text', 'fakturace'):
        if not _text(fee.get(field)):
            errors.append(f'GATE určitosti odměny (§ 3 vyhlášky č. 177/1996 Sb.): chybí odmena.{field}.')
    for key, fields in [('klient', ('radek1', 'radek2', 'podpis')), ('advokat', ('jmeno', 'cak', 'ico', 'sidlo'))]:
        obj = data.get(key) if isinstance(data.get(key), dict) else {}
        for field in fields:
            if not _text(obj.get(field)):
                errors.append(f'GATE úplnosti smlouvy (§ 2430 OZ): chybí {key}.{field}. Advokáta načítá renderer z konfigurace kanceláře.')
    if not _money(data.get('zaloha'), zero=True):
        errors.append('GATE § 22 ZA: záloha musí být částka ve formátu 1.000,00, případně 0,00.')
    if type(data.get('spotrebitel')) is not bool:
        errors.append('GATE § 14 zákona č. 634/1992 Sb.: určete spotrebitel jako true nebo false.')
    elif data['spotrebitel']:
        warnings.append('§ 14 zákona č. 634/1992 Sb.: spotřebitel musí dostat informaci o ADR u ČAK, která je obsažena v článku VI. Zkontrolujte také zveřejnění na webu a v případných obchodních podmínkách a předání na trvalém nosiči při nevyřešeném sporu.')
        warnings.append('Spotřebitelská smlouva: před použitím ověřte způsob uzavření. Pro smlouvu na dálku nebo mimo obchodní prostory tento základní vzor vyžaduje doplnění poučení a případné žádosti o zahájení plnění podle spotřebitelských ustanovení OZ.')
    data.setdefault('ai_dolozka', True)
    if type(data['ai_dolozka']) is not bool:
        errors.append('GATE § 21 ZA: ai_dolozka musí být true nebo false, nikoliv text.')
    elif not data['ai_dolozka']:
        warnings.append('§ 21 ZA: AI doložka je vypnuta. Advokát výslovně rozhodne o použití AI a odpovídajícím informování klienta; vypnutí doložky neodstraňuje mlčenlivost ani povinnosti GDPR.')
    for field in ('gdpr_informace', 'rok'):
        if not _text(data.get(field)):
            errors.append(f'GATE úplnosti vzoru: chybí {field}.')
    warnings.append('§ 20 odst. 6 ZA: po skončení zastoupení zkontrolujte neodkladné úkony v patnáctidenní době a zákonné výjimky.')
    return errors, warnings
