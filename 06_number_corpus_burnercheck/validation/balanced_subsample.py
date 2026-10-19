"""Stratified subsample: 100 numbers per app (seed 2026) + the 372 negatives.
Also repeats the draw 1,000 times to show how much the result depends on the draw.
Hushed is drawn only from the 450 numbers documented in the collection log
(hushed_documented_450.record_ids.txt).
Usage: python -I balanced_subsample.py <public_masked_dir>
"""
import csv, os, random, sys
from math import sqrt
D = sys.argv[1]
pos = list(csv.DictReader(open(os.path.join(D, 'app_numbers_2508.masked.csv'), encoding='utf-8')))
NEG = set(open(os.path.join(D, 'negatives_known_contacts_372.record_ids.txt')).read().split())
neg = [r for r in csv.DictReader(open(os.path.join(D, 'labeled_611_with_negatives.masked.csv'), encoding='utf-8'))
       if r['record_id'] in NEG]
DOC = set(open(os.path.join(D, 'hushed_documented_450.record_ids.txt')).read().split())
pos = [r for r in pos if r['source_app'] != 'hushed' or r['record_id'] in DOC]
APPS = sorted({r['source_app'] for r in pos})
lt = lambda r: r['twilio_line_type'] == 'nonFixedVoip'
car = lambda r: lt(r) or (r['twilio_line_type'] == 'mobile' and r['twilio_carrier'].lower().startswith('onvoy'))
pre_p = lambda r: r['nanpa_classification'] == 'BURNER/VoIP'
pre_n = lambda r: r['nanpa_pred'] == 'True'

def wilson(k, n, z=1.96):
    p = k / n; d = 1 + z*z/n; c = (p + z*z/(2*n))/d; h = z*sqrt(p*(1-p)/n + z*z/(4*n*n))/d
    return f'{p:.3f} [{max(0,c-h):.3f}, {min(1,c+h):.3f}]'

def draw(seed):
    rnd = random.Random(seed)
    return [r for a in APPS for r in rnd.sample([x for x in pos if x['source_app'] == a], 100)]

def scores(P, rp, rn):
    tp = sum(map(rp, P)); fp = sum(map(rn, neg)); fn = len(P)-tp; tn = len(neg)-fp
    return tp, fn, fp, tn

S = draw(2026)
print(f'Seed 2026: positives={len(S)} (100 per app), negatives={len(neg)}')
for name, rp, rn in (('Line type', lt, lt), ('Line type + carrier', car, car), ('NANPA prefix', pre_p, pre_n)):
    tp, fn, fp, tn = scores(S, rp, rn); p = tp/(tp+fp); rc = tp/len(S)
    print(f'  {name:<20} TP={tp:<4} FN={fn:<4} FP={fp:<4} TN={tn:<4} P={wilson(tp,tp+fp)} R={wilson(tp,len(S))} '
          f'Spec={wilson(tn,len(neg))} F1={2*p*rc/(p+rc):.3f}')
print('  Recall by app (line type):', {a: sum(map(lt, [r for r in S if r['source_app']==a]))/100 for a in APPS})

print('\nRecall by app on all documented positives (n=%d):' % len(pos))
for a in APPS:
    g = [r for r in pos if r['source_app'] == a]
    print(f'  {a:<9} n={len(g):<4} line type={wilson(sum(map(lt, g)), len(g))}  '
          f'+carrier={wilson(sum(map(car, g)), len(g))}  prefix={wilson(sum(map(pre_p, g)), len(g))}')

print('\n1,000 random draws (seeds 0-999): 2.5th-97.5th percentile across draws')
for name, rp, rn in (('Line type', lt, lt), ('Line type + carrier', car, car), ('NANPA prefix', pre_p, pre_n)):
    P_, R_, F_ = [], [], []
    for s in range(1000):
        tp, fn, fp, tn = scores(draw(s), rp, rn); p = tp/(tp+fp); rc = tp/500
        P_.append(p); R_.append(rc); F_.append(2*p*rc/(p+rc))
    q = lambda v: f'{sorted(v)[25]:.3f}-{sorted(v)[974]:.3f}'
    print(f'  {name:<20} precision {q(P_)}  recall {q(R_)}  F1 {q(F_)}')
