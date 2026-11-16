"""Sidebar width: the default is not cut down while the window is not shown yet."""
import os, sys
from types import SimpleNamespace as NS
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import stub  # noqa: F401
from katiecad.ui import sidebar as S

ok = 0
def check(c, m):
    global ok
    assert c, "FEHLER: " + m
    ok += 1

def fake(fensterbreite):
    return NS(winfo_toplevel=lambda: NS(winfo_width=lambda: fensterbreite))

b = S.Seitenleiste._begrenzen
check(b(fake(1), S.BREITE_STANDARD) == S.BREITE_STANDARD, "Fenster noch nicht angezeigt (Breite 1): Standard bleibt")
check(S.BREITE_STANDARD >= 300, "Standard ist breit")
check(b(fake(1400), S.BREITE_STANDARD) == S.BREITE_STANDARD, "normales Fenster")
check(b(fake(1400), 5000) == 620, "Maximum")
check(b(fake(1000), 900) == 600, "hoechstens 60 % des Fensters")
check(b(fake(1400), 50) == S.BREITE_MIN, "Minimum 170 (vom Nutzer einstellbar)")
check(b(fake(1), 200) == 200, "gespeicherte kleine Breite bleibt")
print(f"test_sidebar_breite - OK ({ok} Pruefungen)")
