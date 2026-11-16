"""Zoom Extents in a layout always fits the sheet (also when it is empty)."""
import os, sys
from types import SimpleNamespace as NS
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import stub  # noqa: F401
import katiecad.ui.app as A
from katiecad.model.core import Linie

ok = 0
def check(c, m):
    global ok
    assert c, "FEHLER: " + m
    ok += 1

def fake(layout, elemente, fmt="A4 (297x210)"):
    return NS(elemente=[], layout_elemente=elemente, _ist_layout=lambda: layout, layers={},
              layout_format=fmt, view={"zoom": 1.5, "ox": 0.0, "oy": 0.0},
              canvas=NS(winfo_width=lambda: 1200, winfo_height=lambda: 700),
              redraw=lambda: None, _zeichne_raster=lambda: None, status=NS(set=lambda t: None))

b, h = A.ZEICHNUNGSFORMATE["A4 (297x210)"]
for name, els in (("leer", []), ("mit Inhalt auf dem Blatt", [Linie(10, 10, 50, 50)])):
    s = fake(True, els)
    A.CadApp.zoom_grenzen(s)
    z, ox, oy = s.view["zoom"], s.view["ox"], s.view["oy"]
    x1, x2 = ox, ox + b * z                      # sheet in pixels
    y1, y2 = oy - h * z, oy
    check(x1 >= 0 and x2 <= 1200 and y1 >= 0 and y2 <= 700, f"Blatt passt ins Fenster ({name})")
    check(abs((x1 + x2) / 2 - 600) < 1 and abs((y1 + y2) / 2 - 350) < 1, f"Blatt zentriert ({name})")
    check(max((x2 - x1) / 1200, (y2 - y1) / 700) > 0.8, f"Blatt fuellt das Fenster ({name})")
# an element far outside the sheet is included as well
s = fake(True, [Linie(0, 0, 1000, 0)])
A.CadApp.zoom_grenzen(s)
check(s.view["zoom"] < 1200 / b, "Element ausserhalb des Blatts wird mit eingerechnet")
# model view unchanged: empty -> fixed zoom
s = fake(False, [])
A.CadApp.zoom_grenzen(s)
check(s.view["zoom"] == 1.5, "leeres Modell wie bisher")
print(f"test_zoom_layout - OK ({ok} Pruefungen)")
