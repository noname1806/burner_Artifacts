import subprocess, re, time, os, csv, sys

ADB = os.path.expanduser("~/AppData/Local/Android/Sdk/platform-tools/adb.exe")
DEV = "emulator-5554"
OUT = r"C:/Phd/Research/Burner-Paper/burner_app_numbers"
SHOTS = os.path.join(OUT, "screenshots")
CSV = os.path.join(OUT, "burner_numbers.csv")
LOG = os.path.join(OUT, "collect.log")
TARGET = int(sys.argv[1]) if len(sys.argv) > 1 else 500
os.makedirs(SHOTS, exist_ok=True)
NUM_RE = re.compile(r"\((\d{3})\) (\d{3})-(\d{4})")

# ~110 US area codes across many states (Burner shows ~5 numbers each)
AREA = [
 ("212","NY"),("315","NY"),("585","NY"),("716","NY"),("914","NY"),("631","NY"),("845","NY"),("929","NY"),
 ("213","CA"),("310","CA"),("408","CA"),("415","CA"),("510","CA"),("619","CA"),("650","CA"),("714","CA"),
 ("818","CA"),("916","CA"),("323","CA"),("559","CA"),("707","CA"),("760","CA"),("805","CA"),("909","CA"),
 ("210","TX"),("214","TX"),("281","TX"),("512","TX"),("713","TX"),("806","TX"),("915","TX"),("817","TX"),("972","TX"),("936","TX"),
 ("305","FL"),("321","FL"),("407","FL"),("561","FL"),("813","FL"),("904","FL"),("954","FL"),("352","FL"),("386","FL"),("727","FL"),
 ("312","IL"),("309","IL"),("618","IL"),("815","IL"),("847","IL"),("630","IL"),
 ("206","WA"),("253","WA"),("509","WA"),("360","WA"),("425","WA"),
 ("413","MA"),("508","MA"),("617","MA"),("781","MA"),("978","MA"),
 ("404","GA"),("470","GA"),("678","GA"),("912","GA"),("706","GA"),("770","GA"),
 ("215","PA"),("412","PA"),("610","PA"),("717","PA"),("814","PA"),("484","PA"),("724","PA"),
 ("216","OH"),("330","OH"),("419","OH"),("513","OH"),("614","OH"),("937","OH"),("440","OH"),
 ("303","CO"),("719","CO"),("970","CO"),("720","CO"),
 ("480","AZ"),("520","AZ"),("602","AZ"),("623","AZ"),("928","AZ"),
 ("704","NC"),("828","NC"),("919","NC"),("336","NC"),("910","NC"),
 ("313","MI"),("248","MI"),("616","MI"),("517","MI"),("734","MI"),("906","MI"),
 ("612","MN"),("651","MN"),("507","MN"),("218","MN"),("320","MN"),
 ("503","OR"),("541","OR"),("971","OR"),
 ("702","NV"),("775","NV"),
 ("615","TN"),("901","TN"),("865","TN"),("423","TN"),("931","TN"),
 ("703","VA"),("757","VA"),("804","VA"),("540","VA"),("434","VA"),
 ("317","IN"),("219","IN"),("812","IN"),
 ("314","MO"),("816","MO"),("417","MO"),
 ("225","LA"),("504","LA"),("337","LA"),("318","LA"),
 ("205","AL"),("251","AL"),("334","AL"),
 ("601","MS"),("228","MS"),("662","MS"),
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

def dump():
    sh("shell", "uiautomator", "dump", "/sdcard/b.xml")
    sh("pull", "/sdcard/b.xml", os.path.join(OUT, "_b.xml"))
    try:
        return open(os.path.join(OUT, "_b.xml"), encoding="utf-8", errors="replace").read()
    except Exception:
        return ""

def screenshot(name):
    sh("shell", "screencap", "-p", "/sdcard/b.png")
    sh("pull", "/sdcard/b.png", os.path.join(SHOTS, name))

def tap(x, y): sh("shell", "input", "tap", str(x), str(y))
def key(*c): sh("shell", "input", "keyevent", *[str(i) for i in c])
def text(s): sh("shell", "input", "text", s)

def kind(xml):
    if "Pick a different area code" in xml: return "LIST"
    if "Enter area code" in xml: return "ENTRY"
    if any(k in xml.lower() for k in ("subscrib", "purchase", "checkout", "free trial", "per month", "/mo")): return "PURCHASE"
    return "OTHER"

def to_entry():
    for _ in range(6):
        k = kind(dump())
        if k == "ENTRY": return True
        if k == "LIST": tap(540, 2149); time.sleep(2); continue      # Pick a different area code
        if k == "PURCHASE": key(4); time.sleep(1.5); continue        # never confirm; back out
        key(4); time.sleep(1.3)
    return kind(dump()) == "ENTRY"

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
    if len(collected) >= TARGET: break
    if code in done_ac: continue
    if not to_entry():
        log(f"{code}: could not reach entry; skip"); continue
    key(67, 67, 67, 67, 67)      # clear field
    text(code)                    # type 3 digits -> auto-advances
    time.sleep(2.3)
    xml = dump()
    k = kind(xml)
    if k == "PURCHASE":
        log(f"{code}: hit purchase screen; backing out"); key(4); time.sleep(1.5); continue
    if k != "LIST":
        log(f"{code}: no list appeared (kind={k}); skip"); continue
    got = [(f"+1{x}{y}{z}", f"+1 ({x}) {y}-{z}", x) for x, y, z in NUM_RE.findall(xml)]
    # keep only numbers matching the requested area code (avoid stale screen)
    got = [g for g in got if g[2] == code]
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

save()
log(f"DONE: {len(collected)} numbers from {len(done_ac)} area codes; screenshots in {SHOTS}")
