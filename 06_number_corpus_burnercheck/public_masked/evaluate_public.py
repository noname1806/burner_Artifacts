"""Reproduce the BurnerCheck evaluation (paper Section 5.1) from the masked public corpus.

Ground truth is by provenance, never by classifier output:
  Positives: app_numbers_2508.masked.csv, restricted to numbers with a collection record
             (all Burner, 2ndLine, TextMe and TextFree rows; the 450 Hushed rows listed in
             hushed_documented_450.record_ids.txt). 2,458 numbers.
  Negatives: the 372 known contacts of the research team listed in
             negatives_known_contacts_372.record_ids.txt (rows of labeled_611_with_negatives.masked.csv).
Main table: stratified random sample of 100 positives per app (seed 2026) + all 372 negatives.
Per-app recall: all 2,458 documented positives. CIs are 95% Wilson intervals.
Writes confusion_matrices.json next to this script.
Usage: python evaluate_public.py
"""
import csv, os, json, random
from math import sqrt

HERE = os.path.dirname(os.path.abspath(__file__))
SEED, PER_APP = 2026, 100


def ids(name):
    return set(open(os.path.join(HERE, name), encoding='utf-8').read().split())


hushed_doc = ids('hushed_documented_450.record_ids.txt')
neg_ids = ids('negatives_known_contacts_372.record_ids.txt')
pos = [r for r in csv.DictReader(open(os.path.join(HERE, 'app_numbers_2508.masked.csv'), encoding='utf-8'))
       if r['source_app'] != 'hushed' or r['record_id'] in hushed_doc]
neg = [r for r in csv.DictReader(open(os.path.join(HERE, 'labeled_611_with_negatives.masked.csv'), encoding='utf-8'))
       if r['record_id'] in neg_ids]
APPS = sorted({r['source_app'] for r in pos})


def lt_rule(r):        # high-confidence flag: Twilio line type
    return r['twilio_line_type'] == 'nonFixedVoip'


def carrier_rule(r):   # lead: line type + carrier metadata
    return lt_rule(r) or (r['twilio_line_type'] == 'mobile' and (r['twilio_carrier'] or '').lower().startswith('onvoy'))


def prefix_pos(r): return r['nanpa_classification'] == 'BURNER/VoIP'   # column name in the 2508 file
def prefix_neg(r): return r['nanpa_pred'] == 'True'                    # same rule, column name in the 611 file


SIGNALS = (('Line type', lt_rule, lt_rule),
           ('Line type + carrier', carrier_rule, carrier_rule),
           ('NANPA prefix', prefix_pos, prefix_neg))


def wilson(k, n, z=1.96):
    if n == 0:
        return [0.0, 0.0]
    p = k / n; d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return [round(max(0.0, c - h), 3), round(min(1.0, c + h), 3)]


def metrics(P, rp, rn):
    tp = sum(map(rp, P)); fp = sum(map(rn, neg)); fn = len(P) - tp; tn = len(neg) - fp
    p = tp / (tp + fp) if tp + fp else 0.0
    rc = tp / (tp + fn) if tp + fn else 0.0
    return dict(TP=tp, FN=fn, FP=fp, TN=tn,
                precision=round(p, 3), precision_ci=wilson(tp, tp + fp),
                recall=round(rc, 3), recall_ci=wilson(tp, tp + fn),
                specificity=round(tn / (tn + fp), 3), specificity_ci=wilson(tn, tn + fp),
                f1=round(2 * p * rc / (p + rc), 3) if p + rc else 0.0)


rnd = random.Random(SEED)
sample = [r for a in APPS for r in rnd.sample([x for x in pos if x['source_app'] == a], PER_APP)]

results = {'corpus': {'documented_positives': len(pos), 'negatives_known_contacts': len(neg),
                      'sample': f'{PER_APP} per app, seed {SEED}', 'sample_positives': len(sample)}}
print(f'Main table: {len(sample)} positives ({PER_APP} per app, seed {SEED}) + {len(neg)} known-contact negatives')
results['main_table'] = {}
for name, rp, rn in SIGNALS:
    m = metrics(sample, rp, rn); results['main_table'][name] = m
    print(f'  {name:<20} TP={m["TP"]:<4} FN={m["FN"]:<4} FP={m["FP"]:<4} TN={m["TN"]:<4} '
          f'P={m["precision"]:.3f} {m["precision_ci"]}  R={m["recall"]:.3f} {m["recall_ci"]}  '
          f'Spec={m["specificity"]:.3f} {m["specificity_ci"]}  F1={m["f1"]:.3f}')

print(f'\nRecall per issuing app (all {len(pos)} documented positives):')
results['recall_per_app'] = {}
for a in APPS:
    g = [r for r in pos if r['source_app'] == a]
    rec = {'n': len(g)}
    for name, rp, _ in SIGNALS:
        k = sum(map(rp, g)); rec[name] = {'recall': round(k / len(g), 3), 'ci': wilson(k, len(g))}
    results['recall_per_app'][a] = rec
    print(f'  {a:<9} n={len(g):<4} ' + '  '.join(f'{n}={rec[n]["recall"]:.3f} {rec[n]["ci"]}' for n, _, _ in SIGNALS))

out = os.path.join(HERE, 'confusion_matrices.json')
json.dump(results, open(out, 'w', encoding='utf-8'), indent=2)
print(f'\nwrote {out}')
