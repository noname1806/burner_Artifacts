import subprocess, re, time, os, csv, sys, json

ADB = os.path.expanduser("~/AppData/Local/Android/Sdk/platform-tools/adb.exe")
DEV = "emulator-5554"
OUT = r"C:/Phd/Research/Burner-Paper/hushed_numbers"
SHOTS = os.path.join(OUT, "screenshots")
CSV = os.path.join(OUT, "hushed_burner_numbers.csv")
LOG = os.path.join(OUT, "collect.log")
TARGET = int(sys.argv[1]) if len(sys.argv) > 1 else 450
os.makedirs(SHOTS, exist_ok=True)

NUM_RE = re.compile(r"\+1 \((\d{3})\) (\d{3})-(\d{4})")

def sh(*args):
    return subprocess.run([ADB, "-s", DEV, *args], capture_output=True, text=True, timeout=60)

def log(m):
    line = f"[{int(time.time())}] {m}"
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def dump():
    sh("shell", "uiautomator", "dump", "/sdcard/ui.xml")
    sh("pull", "/sdcard/ui.xml", os.path.join(OUT, "_ui.xml"))
    try:
        return open(os.path.join(OUT, "_ui.xml"), encoding="utf-8", errors="replace").read()
    except Exception:
        return ""

def screenshot(name):
    sh("shell", "screencap", "-p", "/sdcard/s.png")
    sh("pull", "/sdcard/s.png", os.path.join(SHOTS, name))

def tap(x, y):
    sh("shell", "input", "tap", str(x), str(y))

def swipe_up():
    sh("shell", "input", "swipe", "540", "1700", "540", "700", "400")

def back():
    sh("shell", "input", "keyevent", "4")

def screen_kind(xml):
    if "Select a Region" in xml or "selectRegion_listItemWrapper" in xml:
        return "region"
    if "number_row" in xml or "Select Your Number" in xml:
        return "numbers"
    return "other"

def numbers_in(xml):
    out = []
    for a, b, c in NUM_RE.findall(xml):
        out.append((f"+1{a}{b}{c}", f"+1 ({a}) {b}-{c}", a))
    return out

def bounds_center(node):
    m = re.search(r'bounds="\[(\d+),(\d+)\]\[(\d+),(\d+)\]"', node)
    if not m:
        return None
    x1, y1, x2, y2 = map(int, m.groups())
    return (x1 + x2) // 2, (y1 + y2) // 2

def region_rows(xml):
    """Return list of (areacode, state, x, y) for visible area-code rows."""
    rows = []
    for m in re.finditer(r'<node[^>]*selectRegion_tvAreaCode[^>]*>', xml):
        n = m.group(0)
        t = (re.search(r'text="\((\d{3})\)"', n) or [None, None])[1]
        c = bounds_center(n)
        if t and c:
            rows.append((t, c[0], c[1]))
    # attach nearest state name
    names = []
    for m in re.finditer(r'<node[^>]*selectRegion_tvName[^>]*>', xml):
        n = m.group(0)
        t = (re.search(r'text="([^"]*)"', n) or [None, ""])[1]
        c = bounds_center(n)
        if c:
            names.append((c[1], t))
    res = []
    for ac, x, y in rows:
        state = min(names, key=lambda z: abs(z[0] - y))[1] if names else ""
        res.append((ac, state, 400, y))
    return res

def ensure_region():
    for _ in range(4):
        xml = dump()
        k = screen_kind(xml)
        if k == "region":
            return xml
        back(); time.sleep(1.2)
    return dump()

# main
collected = {}   # phone -> (formatted, areacode, state, first_screenshot)
done_ac = set()
if os.path.exists(CSV):
    try:
        for r in csv.DictReader(open(CSV, encoding="utf-8")):
            collected[r["phone_number"]] = (r["formatted"], r["area_code"], r["region_state"], r["screenshot"])
            done_ac.add(r["area_code"])
    except Exception:
        pass

def save():
    tmp = CSV + ".tmp"
    for attempt in range(4):
        try:
            with open(tmp, "w", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                w.writerow(["phone_number", "formatted", "area_code", "region_state", "screenshot"])
                for p, (fm, ac, st, ss) in collected.items():
                    w.writerow([p, fm, ac, st, ss])
            os.replace(tmp, CSV)
            return
        except PermissionError:
            log("WARN: CSV is locked (is it open in Excel?); retrying in 3s")
            time.sleep(3)
    log("WARN: could not write CSV this round; kept data in memory, will retry next round")

log(f"start; have {len(collected)} numbers, target {TARGET}")
region_scrolls = 0
shot_idx = len([n for n in os.listdir(SHOTS)]) if os.path.isdir(SHOTS) else 0

while len(collected) < TARGET:
    xml = ensure_region()
    rows = region_rows(xml)
    # pick first area code not yet done
    pick = next((r for r in rows if r[0] not in done_ac), None)
    if pick is None:
        # scroll region list for more area codes
        swipe_up(); time.sleep(1.0); region_scrolls += 1
        if region_scrolls > 60:
            log("no new area codes after 60 consecutive scrolls; stopping")
            break
        continue
    ac, state, x, y = pick
    done_ac.add(ac)
    region_scrolls = 0  # reset: only count consecutive fruitless region swipes
    tap(x, y); time.sleep(1.8)
    before = len(collected)
    no_new = 0
    for s in range(5):  # up to 5 scroll positions per area code
        xml = dump()
        if screen_kind(xml) != "numbers":
            break
        got = numbers_in(xml)
        new = [(p, fm, a) for p, fm, a in got if p not in collected]
        if new:
            shot_idx += 1
            shot = f"{shot_idx:03d}_ac{ac}_{s}.png"
            screenshot(shot)
            for p, fm, a in new:
                collected[p] = (fm, a, state, shot)
            no_new = 0
        else:
            no_new += 1
        if no_new >= 2 or len(collected) >= TARGET:
            break
        swipe_up(); time.sleep(1.0)
    save()
    log(f"ac {ac} ({state}): +{len(collected)-before}  total={len(collected)}")
    back(); time.sleep(1.2)

save()
log(f"DONE: {len(collected)} numbers from {len(done_ac)} area codes; screenshots in {SHOTS}")
