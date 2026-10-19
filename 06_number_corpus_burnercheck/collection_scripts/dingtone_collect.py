import subprocess, re, time, os, csv, sys

ADB = os.path.expanduser("~/AppData/Local/Android/Sdk/platform-tools/adb.exe")
DEV = "emulator-5554"
OUT = r"C:/Phd/Research/Burner-Paper/dingtone_numbers"
SHOTS = os.path.join(OUT, "screenshots")
CSV = os.path.join(OUT, "dingtone_burner_numbers.csv")
LOG = os.path.join(OUT, "collect.log")
TARGET = int(sys.argv[1]) if len(sys.argv) > 1 else 500
os.makedirs(SHOTS, exist_ok=True)
NUM_RE = re.compile(r"\((\d{3})\) (\d{3})-(\d{4})")

AREA = [
 ("212","New York"),("315","New York"),("585","New York"),("716","New York"),("914","New York"),
 ("213","California"),("310","California"),("408","California"),("415","California"),("510","California"),
 ("619","California"),("650","California"),("714","California"),("818","California"),("916","California"),
 ("210","Texas"),("214","Texas"),("281","Texas"),("512","Texas"),("713","Texas"),("806","Texas"),("915","Texas"),
 ("305","Florida"),("321","Florida"),("407","Florida"),("561","Florida"),("813","Florida"),("904","Florida"),("954","Florida"),
 ("312","Illinois"),("309","Illinois"),("618","Illinois"),("815","Illinois"),
 ("206","Washington"),("253","Washington"),("509","Washington"),
 ("413","Massachusetts"),("508","Massachusetts"),("617","Massachusetts"),("781","Massachusetts"),
 ("404","Georgia"),("470","Georgia"),("678","Georgia"),("912","Georgia"),
 ("215","Pennsylvania"),("412","Pennsylvania"),("610","Pennsylvania"),("717","Pennsylvania"),("814","Pennsylvania"),
 ("216","Ohio"),("330","Ohio"),("419","Ohio"),("513","Ohio"),("614","Ohio"),("937","Ohio"),
 ("303","Colorado"),("719","Colorado"),("970","Colorado"),
 ("480","Arizona"),("520","Arizona"),("602","Arizona"),
 ("704","North Carolina"),("828","North Carolina"),("919","North Carolina"),
 ("313","Michigan"),("248","Michigan"),("616","Michigan"),
 ("612","Minnesota"),("651","Minnesota"),("507","Minnesota"),
 ("503","Oregon"),("541","Oregon"),("702","Nevada"),("775","Nevada"),
 ("615","Tennessee"),("901","Tennessee"),("703","Virginia"),("757","Virginia"),("804","Virginia"),
]

def sh(*a):
    try:
        return subprocess.run([ADB, "-s", DEV, *a], capture_output=True, text=True, timeout=40)
    except Exception:
        return None

def log(m):
    print(m, flush=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(m + "\n")

def activity():
    r = sh("shell", "dumpsys", "activity", "activities")
    if not r:
        return "?"
    m = re.search(r'ResumedActivity[^\n]*?me\.number\.app\.im/([\w./]+)', r.stdout)
    return m.group(1) if m else (r.stdout and re.search(r'ResumedActivity[^\n]*?([\w./]+/[\w./]+)', r.stdout).group(1)) or "?"

def dump():
    sh("shell", "uiautomator", "dump", "/sdcard/d.xml")
    sh("pull", "/sdcard/d.xml", os.path.join(OUT, "_d.xml"))
    try:
        return open(os.path.join(OUT, "_d.xml"), encoding="utf-8", errors="replace").read()
    except Exception:
        return ""

def screenshot(name):
    sh("shell", "screencap", "-p", "/sdcard/d.png")
    sh("pull", "/sdcard/d.png", os.path.join(SHOTS, name))

def tap(x, y): sh("shell", "input", "tap", str(x), str(y))
def key(*c): sh("shell", "input", "keyevent", *[str(i) for i in c])

def bounds(xml, rid=None, text_prefix=None):
    for m in re.finditer(r'<node[^>]*>', xml):
        n = m.group(0)
        if rid and not re.search(r'resource-id="[^"/]*/%s"' % re.escape(rid), n):
            continue
        if text_prefix:
            tm = re.search(r'text="([^"]*)"', n)
            if not tm or not tm.group(1).startswith(text_prefix):
                continue
        bm = re.search(r'bounds="\[(\d+),(\d+)\]\[(\d+),(\d+)\]"', n)
        if bm:
            x1, y1, x2, y2 = map(int, bm.groups())
            return ((x1 + x2) // 2, (y1 + y2) // 2)
    return None

PURCHASE = ("PackagePurchase", "Purchase", "Package")

def is_purchase(a): return any(k in a for k in PURCHASE)
def is_input(a): return "AdBuyPhoneNumberInputAreaCode" in a
def is_choose(a): return "AdBuyPhoneNumberChooseWithUS" in a

def panic_back():
    # never confirm anything; just navigate back off any purchase/selection screen
    key(4); time.sleep(1.5)

def nav_to_input():
    for _ in range(12):
        a = activity()
        if is_input(a):
            return True
        if is_purchase(a):
            panic_back(); continue
        if is_choose(a):
            key(4); time.sleep(1.3); continue
        if "CountryListOfPhoneNumber" in a:
            xml = dump(); us = bounds(xml, text_prefix="United States")
            if us: tap(*us); time.sleep(1.8)
            continue
        if "NumberMainActivity" in a:
            xml = dump()
            add = bounds(xml, rid="rl_add_phone") or bounds(xml, text_prefix="Add a New Phone")
            if add: tap(*add); time.sleep(1.8)
            continue
        if "NumberSplashActivity" in a or "PrivatePhoneSetting" in a:
            key(4); time.sleep(1.3); continue
        # unknown: try launching, else back
        if a == "?" or "Launcher" in a:
            sh("shell", "monkey", "-p", "me.number.app.im", "-c", "android.intent.category.LAUNCHER", "1"); time.sleep(3)
        else:
            key(4); time.sleep(1.2)
    return is_input(activity())

def enter_areacode(code):
    """Only runs when verified on the InputAreaCode screen. Element-based taps only."""
    xml = dump()
    field = bounds(xml, rid="edit_text_view")
    submit = bounds(xml, rid="btn_submit")
    if not field or not submit:
        return False
    tap(*field); time.sleep(0.6)
    key(67, 67, 67, 67, 67)                 # clear
    key(*[7 + int(d) for d in code])        # digits (KEYCODE_0=7)
    time.sleep(0.5)
    tap(*submit); time.sleep(2.2)
    return True

collected = {}
if os.path.exists(CSV):
    try:
        for r in csv.DictReader(open(CSV, encoding="utf-8")):
            collected[r["phone_number"]] = (r["formatted"], r["area_code"], r["region_state"], r["screenshot"])
    except Exception:
        pass

def save():
    tmp = CSV + ".tmp"
    for _ in range(4):
        try:
            with open(tmp, "w", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                w.writerow(["phone_number", "formatted", "area_code", "region_state", "screenshot"])
                for p, (fm, ac, st, ss) in collected.items():
                    w.writerow([p, fm, ac, st, ss])
            os.replace(tmp, CSV); return
        except PermissionError:
            log("WARN: CSV locked (close Excel?); retry 3s"); time.sleep(3)
    log("WARN: CSV not written this round; kept in memory")

log(f"start; have {len(collected)}, target {TARGET}")
shot_idx = len([f for f in os.listdir(SHOTS) if f.endswith('.png')]) if os.path.isdir(SHOTS) else 0
done_ac = set(v[1] for v in collected.values())

for code, state in AREA:
    if len(collected) >= TARGET:
        break
    if code in done_ac:
        continue
    if not nav_to_input():
        log(f"{code}: could not reach area-code input safely; skipping")
        continue
    if not enter_areacode(code):
        log(f"{code}: could not enter area code; skipping")
        continue
    a = activity()
    if is_purchase(a):
        log(f"{code}: hit a purchase screen unexpectedly; backing out, skipping")
        panic_back(); continue
    if not is_choose(a):
        log(f"{code}: no number list appeared (act={a}); skipping")
        continue
    # ON THE NUMBER LIST: read + screenshot ONLY. No taps here except system Back afterwards.
    xml = dump()
    got = [(f"+1{x}{y}{z}", f"+1 ({x}) {y}-{z}", x) for x, y, z in NUM_RE.findall(xml)]
    new = [g for g in got if g[0] not in collected]
    before = len(collected)
    if new:
        shot_idx += 1
        shot = f"{shot_idx:03d}_ac{code}.png"
        screenshot(shot)
        for p, fm, x in new:
            collected[p] = (fm, x, state, shot)
    done_ac.add(code)
    save()
    log(f"ac {code} ({state}): +{len(collected)-before}  total={len(collected)}  (list had {len(got)})")
    key(4); time.sleep(1.3)   # system Back -> area-code input for next

save()
log(f"DONE: {len(collected)} numbers from {len(done_ac)} area codes; screenshots in {SHOTS}")
