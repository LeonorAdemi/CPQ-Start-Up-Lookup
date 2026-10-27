"""Erzeugt das Quoro-Logo als SVG: Bildmarke und Schriftzug (Manrope SemiBold, in Pfade umgewandelt).

Bildmarke: ein „Q“, dessen Schweif aus drei parallelen Linien unterschiedlicher Länge besteht,
den parallel arbeitenden KI-Agenten.

Aufruf: python3 build_logo.py <Pfad zu Manrope-SemiBold.ttf> <Ausgabeordner>
"""
import math
import sys
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

FONT, OUT = sys.argv[1], Path(sys.argv[2])
OUT.mkdir(parents=True, exist_ok=True)

NAVY, PETROL = "#0C1824", ["#3F7275", "#548484", "#609090"]
NAVY_DARK_BG, LIGHT = "#FFFFFF", ["#9FC4C4", "#B7D3D3", "#CFE0E0"]


def mark(ring, tails, x0=0.0, y0=0.0, s=1.0):
    """Bildmarke im 48er-Raster, verschoben um (x0, y0) und skaliert um s."""
    cx, cy, r = 22, 22, 15

    def pt(deg, rad=r):
        a = math.radians(deg)
        return x0 + s * (cx + rad * math.cos(a)), y0 + s * (cy + rad * math.sin(a))

    (ax, ay), (bx, by) = pt(72), pt(18)
    parts = [f'<path d="M{ax:.2f} {ay:.2f}A{r * s:.2f} {r * s:.2f} 0 1 1 {bx:.2f} {by:.2f}" '
             f'fill="none" stroke="{ring}" stroke-width="{4.4 * s:.2f}" stroke-linecap="round"/>']
    d = (math.sqrt(.5), math.sqrt(.5))      # Schweif-Richtung 45°
    p = (math.sqrt(.5), -math.sqrt(.5))     # quer dazu
    for k, length, color in [(-1, 11, tails[2]), (0, 19, tails[0]), (1, 15, tails[1])]:
        sx = cx + 8.5 * d[0] + k * 3.9 * p[0]
        sy = cy + 8.5 * d[1] + k * 3.9 * p[1]
        ex, ey = sx + length * d[0], sy + length * d[1]
        parts.append(f'<path d="M{x0 + s * sx:.2f} {y0 + s * sy:.2f}L{x0 + s * ex:.2f} {y0 + s * ey:.2f}" '
                     f'stroke="{color}" stroke-width="{3.4 * s:.2f}" stroke-linecap="round"/>')
    return "\n  ".join(parts)


def wordmark(text, x, baseline, size, color, tracking=-0.02):
    """Schriftzug als Pfade. size = Schriftgröße in SVG-Einheiten."""
    font = TTFont(FONT)
    glyphs, cmap = font.getGlyphSet(), font.getBestCmap()
    upm = font["head"].unitsPerEm
    scale = size / upm
    paths, cursor = [], x
    for ch in text:
        name = cmap[ord(ch)]
        pen = SVGPathPen(glyphs)
        glyphs[name].draw(TransformPen(pen, (scale, 0, 0, -scale, cursor, baseline)))
        paths.append(pen.getCommands())
        cursor += glyphs[name].width * scale + tracking * size
    return f'<path d="{" ".join(paths)}" fill="{color}"/>', cursor - tracking * size


def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" width="{w:.0f}" height="{h:.0f}" '
            f'role="img" aria-label="{title}">\n  <title>{title}</title>\n  {body}\n</svg>\n')


# Bildmarke allein
(OUT / "quoro-mark.svg").write_text(svg(48, 48, mark(NAVY, PETROL), "Quoro"))
(OUT / "quoro-mark-dark.svg").write_text(svg(48, 48, mark(NAVY_DARK_BG, LIGHT), "Quoro"))

# Horizontales Logo: Bildmarke + Schriftzug
for name, ring, tails, text_color in [("quoro-logo.svg", NAVY, PETROL, NAVY),
                                      ("quoro-logo-dark.svg", NAVY_DARK_BG, LIGHT, "#FFFFFF")]:
    word, end = wordmark("quoro", 58, 34, 38, text_color)
    (OUT / name).write_text(svg(end + 2, 48, mark(ring, tails) + "\n  " + word, "Quoro"))

print("ok", sorted(p.name for p in OUT.glob("*.svg")))
