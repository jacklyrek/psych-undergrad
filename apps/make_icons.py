#!/usr/bin/env python3
"""Generate the PWA's home-screen icons. Stdlib only — no Pillow on this machine, and adding a
binary dependency to a repo that is otherwise `python file.py`-runnable isn't worth an icon.

So: a tiny PNG writer (zlib + struct is all a PNG needs) drawing four rising bars — the widening
review intervals SM-2 produces. Rendered at 4x and box-downsampled for antialiased edges.

iOS needs a real PNG for apple-touch-icon (it ignores SVG), which is why this exists at all.
Full-bleed square with no rounded corners of its own: iOS masks icons to its own squircle, and a
pre-rounded icon shows pale corners inside that mask.

Run:  python apps/make_icons.py
"""
from __future__ import annotations

import struct
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "docs" / "icons"

SS = 4  # supersample factor

# Matches --accent-deep / --accent in docs/style.css.
BG = (23, 61, 58)
BAR = (122, 199, 189)
BAR_LEAD = (233, 246, 243)   # the tallest bar, brightest — reads as "where you're heading"


def draw(size: int) -> list[bytearray]:
    """Render one icon at `size` px. Returns RGB rows (no alpha — the icon is opaque)."""
    w = size * SS
    canvas = [bytearray(BG * w) for _ in range(w)]

    # Four bars on a 20-unit grid: equal widths, rising heights, sitting on a common baseline.
    unit = w / 20.0
    bar_w = unit * 2.6
    gap = unit * 1.6
    baseline = w - unit * 4.2
    heights = [unit * 4.0, unit * 6.4, unit * 8.8, unit * 11.6]
    total = len(heights) * bar_w + (len(heights) - 1) * gap
    x = (w - total) / 2.0
    radius = bar_w / 2.0

    for n, h in enumerate(heights):
        color = BAR_LEAD if n == len(heights) - 1 else BAR
        x0, x1 = x, x + bar_w
        y0, y1 = baseline - h, baseline
        _rounded_rect(canvas, x0, y0, x1, y1, radius, color, w)
        x = x1 + gap

    return _downsample(canvas, size)


def _rounded_rect(canvas, x0, y0, x1, y1, r, color, w) -> None:
    """Fill a rect whose top end is a semicircular cap (the bars read better with a soft top)."""
    cx = (x0 + x1) / 2.0
    cy_top = y0 + r
    for y in range(max(0, int(y0)), min(w, int(y1) + 1)):
        for x in range(max(0, int(x0)), min(w, int(x1) + 1)):
            if y < cy_top:
                # inside the cap only if within the circle
                if (x + 0.5 - cx) ** 2 + (y + 0.5 - cy_top) ** 2 > r * r:
                    continue
            i = x * 3
            canvas[y][i:i + 3] = bytes(color)


def _downsample(canvas: list[bytearray], size: int) -> list[bytearray]:
    """Box filter SS x SS back to `size` — this is what antialiases the curved bar tops."""
    rows: list[bytearray] = []
    n = SS * SS
    for y in range(size):
        row = bytearray(size * 3)
        for x in range(size):
            r = g = b = 0
            for dy in range(SS):
                src = canvas[y * SS + dy]
                base = (x * SS) * 3
                for dx in range(SS):
                    i = base + dx * 3
                    r += src[i]
                    g += src[i + 1]
                    b += src[i + 2]
            o = x * 3
            row[o] = r // n
            row[o + 1] = g // n
            row[o + 2] = b // n
        rows.append(row)
    return rows


def write_png(path: Path, rows: list[bytearray]) -> int:
    """Minimal PNG: IHDR + IDAT + IEND, 8-bit truecolour, filter type 0 on every scanline."""
    height = len(rows)
    width = len(rows[0]) // 3

    def chunk(kind: bytes, data: bytes) -> bytes:
        return (struct.pack(">I", len(data)) + kind + data
                + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF))

    ihdr = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)  # colour type 2 = RGB
    raw = b"".join(b"\x00" + bytes(row) for row in rows)
    png = (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr)
           + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b""))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(png)
    return len(png)


def main() -> None:
    # 192/512 for the web manifest, 180 for iOS's apple-touch-icon, 32 for the browser tab.
    targets = {"icon-192.png": 192, "icon-512.png": 512, "apple-touch-icon.png": 180,
               "favicon-32.png": 32}
    for name, size in targets.items():
        n = write_png(OUT_DIR / name, draw(size))
        print(f"  {name:<22} {size}x{size}  {n / 1024:.1f} KB")
    print(f"Wrote {len(targets)} icons to {OUT_DIR.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
