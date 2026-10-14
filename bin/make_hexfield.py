#!/usr/bin/env python3
"""Generate _includes/hexfield.svg: the hexagon density field behind the homepage hero.

A pointy-top hexagon grid (the shape of Uber's H3 cells, which Luning's mobility
datasets use) shaded by a smooth density surface with two activity centres, so it
reads like an aggregated mobility heat map. Colours come from CSS classes d1–d4.
Re-run after changing parameters: python3 bin/make_hexfield.py
"""
import math
import pathlib
import random

random.seed(7)
R = 13  # hex radius in px
W, H = 620, 440
w = math.sqrt(3) * R
centres = [(470, 150, 150, 1.0), (300, 300, 95, 0.55), (560, 360, 70, 0.45)]


def density(x, y):
    return sum(a * math.exp(-((x - cx) ** 2 + (y - cy) ** 2) / (2 * s * s)) for cx, cy, s, a in centres)


cells = []
row = 0
y = R
while y < H + R:
    x = (w / 2 if row % 2 else 0) + w / 2
    while x < W + w:
        edge = min(1.0, x / 160, (W - x) / 110, (H - y) / 110, (y + 20) / 60)
        d = density(x, y) * max(edge, 0) * (0.85 + 0.3 * random.random())
        level = 4 if d > 0.78 else 3 if d > 0.5 else 2 if d > 0.28 else 1 if d > 0.12 else 0
        if level:
            pts = " ".join(
                f"{x + (R - 1.4) * math.cos(math.radians(60 * k - 30)):.1f},{y + (R - 1.4) * math.sin(math.radians(60 * k - 30)):.1f}"
                for k in range(6)
            )
            cells.append(f'<polygon class="d{level}" points="{pts}"/>')
        x += w
    y += 1.5 * R
    row += 1

svg = (
    f'<svg class="hexfield" viewBox="0 0 {W} {H}" aria-hidden="true" focusable="false" '
    f'xmlns="http://www.w3.org/2000/svg">' + "".join(cells) + "</svg>\n"
)
out = pathlib.Path(__file__).resolve().parent.parent / "_includes" / "hexfield.svg"
out.write_text(svg)
print(f"wrote {out} ({len(cells)} cells)")
