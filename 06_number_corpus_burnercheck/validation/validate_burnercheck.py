"""Validity checks on the BurnerCheck evaluation (R1 precision/recall, error rates).

1. Reproduces evaluate_public.py and adds 95% Wilson intervals.
2. Line types and carriers of the known-contact negatives.
3. Leave-one-app-out test of the carrier rule: the carrier list is learned only
   from the other four apps, then applied to the held-out app.
4. Sensitivity: exact carrier name "Onvoy Spectrum" instead of any "Onvoy*".

Positives: documented numbers only (Hushed 450). Negatives: known-contact ID list.
Usage: python -I validate_burnercheck.py <corpus_dir>
"""
import csv, os, sys
from collections import Counter
from math import sqrt

D = sys.argv[1]
pos = list(csv.DictReader(open(os.path.join(D, 'app_numbers_2508.masked.csv'), encoding='utf-8')))
lab = list(csv.DictReader(open(os.path.join(D, 'labeled_611_with_negatives.masked.csv'), encoding='utf-8')))
neg_ids = set(open(os.path.join(D, 'negatives_known_contacts_372.record_ids.txt')).read().split())
neg = [r for r in lab if r['record_id'] in neg_ids]
doc = set(open(os.path.join(D, 'hushed_documented_450.record_ids.txt')).read().split())
pos = [r for r in pos if r['source_app'] != 'hushed' or r['record_id'] in doc]
APPS = sorted({r['source_app'] for r in pos})


def wilson(k, n, z=1.96):
    if n == 0:
        return 'n/a'
    p = k / n; d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return f'{p:.3f} [{max(0, c - h):.3f}, {min(1, c + h):.3f}]'


def norm(carrier):
    return (carrier or '').lower().replace(', llc', '').replace(' llc', '').strip()


def lt_rule(r): return r['twilio_line_type'] == 'nonFixedVoip'
def onvoy_rule(r): return lt_rule(r) or (r['twilio_line_type'] == 'mobile' and norm(r['twilio_carrier']).startswith('onvoy'))
def spectrum_rule(r): return lt_rule(r) or (r['twilio_line_type'] == 'mobile' and norm(r['twilio_carrier']) == 'onvoy spectrum')


def row(name, rule):
    tp = sum(map(rule, pos)); fp = sum(map(rule, neg))
    fn = len(pos) - tp; tn = len(neg) - fp
    p = tp / (tp + fp); rc = tp / len(pos)
    print(f'{name:<28} TP={tp:<5} FN={fn:<5} FP={fp:<4} TN={tn:<4} '
          f'P={wilson(tp, tp + fp)}  R={wilson(tp, len(pos))}  Spec={wilson(tn, len(neg))}  F1={2*p*rc/(p+rc):.3f}')


print(f'== 1. Reproduction (positives={len(pos)}, negatives={len(neg)})')
row('Line type', lt_rule)
row('Line type + Onvoy*', onvoy_rule)
tp = sum(r['nanpa_classification'] == 'BURNER/VoIP' for r in pos); fp = sum(r['nanpa_pred'] == 'True' for r in neg)
print(f'{"NANPA prefix":<28} TP={tp:<5} FN={len(pos)-tp:<5} FP={fp:<4} TN={len(neg)-fp:<4} '
      f'P={wilson(tp, tp + fp)}  R={wilson(tp, len(pos))}  Spec={wilson(len(neg) - fp, len(neg))}')
print('Recall by app (line type):', {a: wilson(sum(map(lt_rule, g)), len(g)) for a in APPS
                                      for g in [[r for r in pos if r['source_app'] == a]]})
print('Twilio returned no line type: 2508-set', sum(r['twilio_success'] != 'True' for r in pos),
      '| 611-set', sum(r['twilio_line_type'] == '' for r in lab))

print('\n== 2. Known-contact negatives: line types and carriers')
print('Line types among 611-set positives:', Counter(r['twilio_line_type'] for r in lab if r['ground_truth_burner'] == 'True'))
print('Line types among 611-set negatives:', Counter(r['twilio_line_type'] for r in neg))
print('Negative "real mobile" carriers:', Counter(r['twilio_carrier'] for r in neg if r['twilio_line_type'] == 'mobile').most_common())
print('-> Negatives are read from the known-contact ID list, not derived from line type.')

print('\n== 3. Leave-one-app-out carrier rule (carrier list learned from the other apps; carriers with >=5 mobile numbers)')
for held in APPS:
    train = [r for r in pos if r['source_app'] != held and r['twilio_line_type'] == 'mobile']
    learned = {c for c, k in Counter(norm(r['twilio_carrier']) for r in train).items() if k >= 5}
    rule = lambda r: lt_rule(r) or (r['twilio_line_type'] == 'mobile' and norm(r['twilio_carrier']) in learned)
    test = [r for r in pos if r['source_app'] == held]
    print(f'  held out {held:<9} learned={sorted(learned)}  recall={wilson(sum(map(rule, test)), len(test))}  '
          f'FP on negatives={sum(map(rule, neg))}/{len(neg)}')

print('\n== 4. Sensitivity: exact "Onvoy Spectrum" carrier')
row('Line type + Onvoy Spectrum', spectrum_rule)
