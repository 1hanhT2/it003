import subprocess, re, sys, os

WORK = os.path.dirname(os.path.abspath(__file__))
EXE = {"ex1": "ex1.exe", "ex2": "ex2.exe", "ex3": "ex3.exe", "ex4": "ex4.exe"}
PASS = FAIL = 0

def run(exe, inp):
    p = subprocess.run([os.path.join(WORK, EXE[exe])], input=inp,
                       capture_output=True, text=True, timeout=10)
    return p.stdout.strip()

def floats(s):
    return [float(x) for x in re.findall(r"-?\d+(?:\.\d+)?", s)]

def check(name, inp, cond, actual):
    global PASS, FAIL
    ok = cond(actual)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | in={inp!r} -> {actual!r}")
    PASS, FAIL = PASS + ok, FAIL + (not ok)

def approx(a, b, tol=0.02):
    return abs(a - b) <= tol




print("== build ==")
r = subprocess.run(["g++", "-O2", "-o", "ex1.exe", "ex1.cpp"], cwd=WORK, capture_output=True, text=True)
print("ex1:", "OK" if r.returncode == 0 else r.stderr[:300])
r = subprocess.run(["g++", "-O2", "-o", "ex2.exe", "ex2.cpp"], cwd=WORK, capture_output=True, text=True)
print("ex2:", "OK" if r.returncode == 0 else r.stderr[:300])
r = subprocess.run(["g++", "-O2", "-o", "ex3.exe", "ex3.cpp"], cwd=WORK, capture_output=True, text=True)
print("ex3:", "OK" if r.returncode == 0 else r.stderr[:300])
r = subprocess.run(["g++", "-O2", "-o", "ex4.exe", "ex4.cpp"], cwd=WORK, capture_output=True, text=True)
print("ex4:", "OK" if r.returncode == 0 else r.stderr[:300])

print("== C1: avg ==")
for inp, ec, en in [("3 4 5", 4.0, 3.9149), ("1 2 3", 2.0, 1.8171),
                    ("0 4 9", 4.3333, 0.0), ("2.5 3.5 4", 3.3333, 3.2711)]:
    out = run("ex1", inp)
    nums = floats(out)
    check(f"C1 {inp}", inp, lambda o, n=nums: len(n) >= 2 and approx(n[0], ec) and approx(n[1], en), out)

print("== C2: max ==")
for inp, exp in [("3 1 2", 3), ("-5 -2 -9", -2), ("5 5 3", 5), ("7 7 7", 7)]:
    out = run("ex2", inp)
    nums = floats(out)
    check(f"C2 {inp}", inp, lambda o, n=nums: len(n) >= 1 and n[-1] == exp, out)

print("== C3: classify ==")
def norm(s):
    return s.lower().replace("a la", "a").replace("so", "").replace("  ", " ").strip()
for inp, keys in [("0", ["0"]), ("7", ["duong", "le"]),
                  ("-4", ["am", "chan"]), ("-3", ["am", "le"])]:
    out = run("ex3", inp)
    n = norm(out)
    check(f"C3 {inp}", inp, lambda o, k=keys: all(x in norm(o) for x in k), out)

print("== C4: poly func ==")
for inp, exp in [("1 2 1\n2", 9), ("0 3 4\n5", 19), ("2 -3 5\n0", 5), ("1.5 2.5 -1\n2", 10)]:
    out = run("ex4", inp)
    nums = floats(out)
    check(f"C4 {inp!r}", inp, lambda o, n=nums: any(approx(x, exp) for x in n), out)

print(f"\nTOTAL: {PASS} pass, {FAIL} fail")
sys.exit(1 if FAIL else 0)
