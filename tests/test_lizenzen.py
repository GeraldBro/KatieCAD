"""Third-party notices: every requirement is named in the notices, the collector tool works."""
import os, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import stub  # noqa: F401
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
import lizenzen_sammeln as L
from katiecad.ui import dialogs

ok = 0
def check(c, m):
    global ok
    assert c, "FEHLER: " + m
    ok += 1

wurzel = L.WURZEL
notices = open(os.path.join(wurzel, "THIRD_PARTY_NOTICES.txt"), encoding="utf-8").read().lower()
for n in L.requirements_namen():
    check(n.lower() in notices, f"{n} steht in THIRD_PARTY_NOTICES.txt")
    check(n.lower() in dialogs.THIRD_PARTY_TEXT.lower(), f"{n} steht im Lizenzfenster")
check("libredwg" in notices and "gpl" in notices, "LibreDWG (GPL, nicht ausgeliefert) erwaehnt")
check("pyinstaller" in notices, "PyInstaller erwaehnt")
check(os.path.getsize(os.path.join(wurzel, "LICENSE")) > 500, "LICENSE vorhanden")

# collector: with whatever is installed here (at least pypdf / Pillow)
with tempfile.TemporaryDirectory() as td:
    ziel = os.path.join(td, "lic")
    pakete, fehlend, ohne = L.sammeln(ziel, ["pypdf"])
    check("pypdf" in pakete, "pypdf gefunden")
    ordner = [d for d in os.listdir(ziel) if d.lower().startswith("pypdf")]
    check(ordner and "INFO.txt" in os.listdir(os.path.join(ziel, ordner[0])), "INFO.txt geschrieben")
    check(any(f.upper().startswith("LICENSE") for f in os.listdir(os.path.join(ziel, ordner[0]))),
          "Lizenzdatei kopiert")
    p2, f2, o2 = L.sammeln(ziel, ["gibt-es-nicht-xyz"])
    check(f2 == ["gibt-es-nicht-xyz"], "fehlendes Paket wird gemeldet")
print(f"test_lizenzen - OK ({ok} Pruefungen)")
