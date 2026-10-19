import pytesseract, re, os, csv, glob
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Autopsy-4.20.0/autopsy/Tesseract-OCR/tesseract.exe"
BASE = r"C:/Phd/Research/Burner-Paper/text_free_numbers"
CSV = os.path.join(BASE, "textfree_numbers.csv")
# TextFree renders numbers as (AAA) BBB-CCCC in a scrolling list, ~16/screen with overlap.
NUM_RE = re.compile(r'\(?(\d{3})\)?[-.\s]*(\d{3})[-.\s]*(\d{4})')

shots = sorted(glob.glob(os.path.join(BASE, "**", "*.png"), recursive=True))
print(f"{len(shots)} screenshots found", flush=True)

collected = {}   # phone -> (formatted, area_code, screenshot)
order = []
per_shot = []

for sp in shots:
    name = os.path.basename(sp)
    try:
        txt = pytesseract.image_to_string(Image.open(sp))
    except Exception as e:
        per_shot.append((name, f"OCR error: {e}")); continue
    n_new = 0
    for a, b, c in NUM_RE.findall(txt):
        # NANP: area code and exchange cannot start with 0 or 1
        if a[0] in "01" or b[0] in "01":
            continue
        phone = f"+1{a}{b}{c}"
        if phone not in collected:
            collected[phone] = (f"+1 {a}-{b}-{c}", a, name)
            order.append(phone); n_new += 1
    per_shot.append((name, f"{n_new} new unique"))

with open(CSV, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["phone_number", "formatted", "area_code", "region_state", "screenshot"])
    for p in order:
        fm, a, ss = collected[p]
        w.writerow([p, fm, a, "", ss])

print(f"unique numbers: {len(collected)}", flush=True)
print(f"distinct area codes: {sorted(set(v[1] for v in collected.values()))}", flush=True)
print("\nper-screenshot new-unique counts:", flush=True)
for n, why in per_shot:
    print(f"   {n}: {why}", flush=True)
print(f"\nCSV -> {CSV}", flush=True)
