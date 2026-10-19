import pytesseract, re, os, csv, glob
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Autopsy-4.20.0/autopsy/Tesseract-OCR/tesseract.exe"
BASE = r"C:/Phd/Research/Burner-Paper/text_me_numbers"
CSV = os.path.join(BASE, "textme_numbers.csv")
NUM_RE = re.compile(r'\+?1?\s*(\d{3})[-.\s]?(\d{3})[-.\s]?(\d{4})')

shots = sorted(glob.glob(os.path.join(BASE, "**", "*.png"), recursive=True))
print(f"{len(shots)} screenshots found", flush=True)

collected = {}   # phone -> (formatted, area_code, screenshot)
order = []
bad = []         # screenshots that did not yield exactly 5 valid numbers

for sp in shots:
    name = os.path.basename(sp)
    try:
        txt = pytesseract.image_to_string(Image.open(sp))
    except Exception as e:
        bad.append((name, f"OCR error: {e}")); continue
    found = []
    for a, b, c in NUM_RE.findall(txt):
        # sanity: NANP area code and exchange cannot start with 0 or 1
        if a[0] in "01" or b[0] in "01":
            continue
        phone = f"+1{a}{b}{c}"
        found.append((phone, f"+1 {a}-{b}-{c}", a))
    # dedupe within the screenshot, preserve order
    seen = set(); uniq = []
    for p, fm, a in found:
        if p not in seen:
            seen.add(p); uniq.append((p, fm, a))
    if len(uniq) != 5:
        bad.append((name, f"{len(uniq)} numbers parsed"))
    for p, fm, a in uniq:
        if p not in collected:
            collected[p] = (fm, a, name); order.append(p)

with open(CSV, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["phone_number", "formatted", "area_code", "region_state", "screenshot"])
    for p in order:
        fm, a, ss = collected[p]
        w.writerow([p, fm, a, "", ss])

print(f"unique numbers: {len(collected)}", flush=True)
print(f"distinct area codes: {len(set(v[1] for v in collected.values()))}", flush=True)
if bad:
    print(f"\n{len(bad)} screenshots not yielding exactly 5 unique numbers (review these):", flush=True)
    for n, why in bad[:40]:
        print(f"   {n}: {why}", flush=True)
print(f"\nCSV -> {CSV}", flush=True)
