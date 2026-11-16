"""Menu bar (canvas version): row geometry, hover/click, colours - with fake Tk objects."""
import sys, types
sys.path.insert(0, ".")
fake = types.ModuleType("tkinter")
class TclError(Exception): pass
class _W:
    def __init__(self, *a, **k): self.k = k; self.items = []; self.b = {}
    def pack(self, *a, **k): pass
    def withdraw(self): pass
    def overrideredirect(self, *a): pass
    def attributes(self, *a): pass
    def update_idletasks(self): pass
    def destroy(self): pass
    def bind(self, ev, fn): self.b[ev] = fn
    def create_rectangle(self, *a, **k): self.items.append(dict(k)); return len(self.items)
    def create_text(self, *a, **k): self.items.append(dict(k)); return len(self.items)
    def create_line(self, *a, **k): self.items.append(dict(k)); return len(self.items)
    def itemconfigure(self, i, **k): self.items[i-1].update(k); self.n = getattr(self, "n", 0) + 1
fake.TclError, fake.Frame, fake.Toplevel, fake.Canvas, fake.Label = TclError, _W, _W, _W, _W
fake.LEFT = fake.BOTH = fake.X = fake.RIGHT = None
sys.modules["tkinter"] = fake
font = types.ModuleType("tkinter.font"); sys.modules["tkinter.font"] = font; fake.font = font
from katiecad.ui import menuleiste as ml
class Menu:
    def __init__(self, e): self.e = e; self.tk = types.SimpleNamespace(globalgetvar=lambda v: 1)
    def index(self, _): return len(self.e) - 1
    def type(self, i): return self.e[i]["t"]
    def entrycget(self, i, o):
        if o in self.e[i]: return self.e[i][o]
        raise TclError
class F:
    def metrics(self, _): return 16
    def measure(self, t): return 7 * len(t)
m = Menu([{"t": "command", "label": "Neu", "accelerator": "Ctrl+N"},
          {"t": "separator"},
          {"t": "command", "label": "Aus", "state": "disabled"},
          {"t": "checkbutton", "label": "Raster", "variable": "v", "onvalue": 1}])
b = object.__new__(ml.MenuLeiste)
b._bg, b._fg, b._abg, b._afg, b._sperr, b._font = "w", "k", "b", "w", "g", F()
b._stapel = []; b._cache = {}; b._subcache = {}; b._offen = None
p = b._pop_bauen(m, 0)
assert len(p.zeilen) == 3 and p.ys == [(0, 22), (29, 51), (51, 73)], p.ys
assert b._zeile_bei(p, 25) is None and b._zeile_bei(p, 30) == 1 and b._zeile_bei(p, 5) == 0
b._maus(p, 5); assert p.aktiv == 0 and p.cv.items[0]["fill"] == "b"   # highlight
n = p.cv.n
b._maus(p, 6); assert p.cv.n == n                                    # same row: nothing sent to Tk
b._maus(p, 60); assert p.aktiv == 2 and p.cv.items[0]["fill"] == "w"  # disabled row, old one reset
b._auffrischen(p)
assert p.cv.items[10]["text"] == "✓"                # check mark of the checkbutton
b._maus(p, 5); b._markierung_loeschen(p)
assert p.aktiv is None and p.cv.items[0]["fill"] == "w"
print("OK     test_menuleiste_canvas - OK")
