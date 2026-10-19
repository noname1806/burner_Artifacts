import frida, sys, time
dev = frida.get_device("emulator-5556", timeout=10)
pkg = "com.textmeinc.textme"
print("[*] spawning", pkg, flush=True)
pid = dev.spawn([pkg])
sess = dev.attach(pid)
with open(r"C:\Phd\Research\Burner-Paper\captures\textme_api33\pairip_bypass.js","r",encoding="utf-8") as f:
    src = f.read()
script = sess.create_script(src)
def on_msg(m, d):
    if m.get("type") == "send":
        print("JS:", m.get("payload"), flush=True)
    elif m.get("type") == "error":
        print("JSERR:", m.get("stack") or m.get("description"), flush=True)
script.on("message", on_msg)
script.load()
dev.resume(pid)
print("[*] resumed pid", pid, flush=True)
# keep session alive and watch liveness
dur = int(sys.argv[1]) if len(sys.argv) > 1 else 90
t0 = time.time()
while time.time() - t0 < dur:
    time.sleep(5)
    try:
        procs = [p.pid for p in dev.enumerate_processes() if p.name == pkg or p.pid == pid]
        alive = pid in procs
        print("[*] t=%ds alive=%s" % (int(time.time()-t0), alive), flush=True)
        if not alive:
            print("[!] target process gone (likely killed by PairIP native or exit path)", flush=True)
            break
    except Exception as e:
        print("[*] enum err", e, flush=True)
print("[*] done; detaching (app stays running if alive)", flush=True)
