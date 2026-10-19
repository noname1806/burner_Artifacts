"""Static API-endpoint extractor for the Dingtone / 2ndLine APK (me.number.app.im).

Scans all classes*.dex for printable ASCII strings, then pulls out:
  - hostnames (FQDNs, esp. *.dt-pn1.com and other backends)
  - REST-style path fragments (/plan/..., /config/..., /telosWeb/..., etc.)
No decompiler needed: Retrofit/OkHttp endpoints live as literal strings in the
string pool, so a raw string scan recovers the full declared API surface.
"""
import re, sys, glob, os, collections

BASE = os.path.dirname(os.path.abspath(__file__))
DEX = sorted(glob.glob(os.path.join(BASE, "xapk_extract", "base", "classes*.dex")))

# printable ASCII runs, length >= 4
STR_RE = re.compile(rb'[\x20-\x7e]{4,}')
HOST_RE = re.compile(r'^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,}$', re.I)
# path fragments that look like API routes
PATH_RE = re.compile(r'^/(?:[A-Za-z0-9_\-.]+/)*[A-Za-z0-9_\-.{}]+/?$')
API_HINT = re.compile(r'(?:^/(?:api|v\d|plan|config|telos|report|number|user|account|'
                      r'sms|call|message|conversation|sub|subscription|device|login|'
                      r'auth|token|register|profile|contact|balance|credit|order|pay|'
                      r'product|upgrade|burn|block|dt|log|feed|ad)\b)', re.I)

def strings_from(path):
    with open(path, 'rb') as f:
        blob = f.read()
    for m in STR_RE.finditer(blob):
        try:
            yield m.group().decode('ascii')
        except Exception:
            pass

hosts = collections.Counter()
paths = collections.Counter()
full_urls = collections.Counter()
url_re = re.compile(r'https?://[^\s"\'<>]+')

for dx in DEX:
    for s in strings_from(dx):
        for u in url_re.findall(s):
            full_urls[u] += 1
        # candidate whole-string host
        if HOST_RE.match(s) and '.' in s and not s.endswith(('.png', '.jpg', '.java',
                '.xml', '.so', '.gif', '.webp', '.json', '.html', '.css', '.js', '.ttf',
                '.txt', '.dex', '.kt', '.properties', '.class')):
            hosts[s.lower()] += 1
        if s.startswith('/') and PATH_RE.match(s) and 2 <= len(s) <= 120:
            paths[s] += 1

def dump(title, counter, filt=None, limit=400):
    print(f"\n{'='*70}\n{title}  ({len(counter)} unique)\n{'='*70}")
    items = [(k, v) for k, v in counter.items() if (filt is None or filt(k))]
    for k, v in sorted(items, key=lambda x: (-x[1], x[0]))[:limit]:
        print(f"  {v:5d}  {k}")
    return items

# backend hosts of interest (skip google/android/facebook noise for the headline)
NOISE = re.compile(r'(google|gstatic|android|facebook|fbcdn|crashlytics|firebase|'
                   r'youtube|schemas|w3\.org|apache|example|localhost|'
                   r'gpc\.|doubleclick|googleapis|googletagmanager|adjust\.|'
                   r'unity3d|applovin|mopub|inmobi|vungle|admob)', re.I)

dump("ALL FULL URLs (literal https?:// strings)", full_urls)
dump("BACKEND HOSTS (app-specific, noise filtered)", hosts, lambda h: not NOISE.search(h))
dump("API PATH FRAGMENTS (endpoint-like)", paths, lambda p: bool(API_HINT.search(p)))
