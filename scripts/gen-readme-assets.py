#!/usr/bin/env python3
"""README visuals for dsh-scaffold — hero (Pillow) + structure (hand SVG).

Everything drawn here is read out of the shipped package, not invented:

  package.json   exports map: `.` / `./seam` / `./gates` / `./shared` /
                 `./verify` (a root barrel re-exports all four subpaths);
                 `dependencies` is `{}`; every `@deepseek-ai/*` peer is
                 optional; `dsh.bundle.patch` points at cordis.patch.yml.
  cordis.patch.yml  an intentionally EMPTY array: a consuming plugin adds its
                 `insert:` row here, this package mounts none.
  src/seam/provider.ts       ProviderRegistry<T>: register() returns a
                 disposer and throws on a duplicate name; use() resolves the
                 named impl or the default.
  src/gates/approval.ts      applyFailClosed(verdict | null): no verdict ->
                 fallback, DEFAULT_FALLBACK 'rejected' (deny); the only grant
                 path is an explicit 'allow-once'.
  src/gates/session-event.ts makeEventGate / maybeAppendSessionEvent: append
                 known types directly, append unknown ones only when the host
                 stamps the ignorable envelope, otherwise skip (never retry).
  src/shared/*               sanitize (placeholder table), pricing (cost /
                 carbon / latency), judge (VERDICT_SCHEMA, parseVerdict).
  src/verify/*               verify-license / verify-readme-languages /
                 verify-seam -> VerifyReport, CLI exits non-zero on failure.
  template/                  a three-role plugin skeleton (Service Definition
                 / Service Provider / Consumer).

  hero  (1440x576, zh/en x light/dark) — package anatomy. Left column is the
        prose seven: kicker / title / two value lines / subtitle / two meta
        lines / footer. Right column is the package itself: a header with the
        export map and `deps {}`, four surface tiles (seam / gates / shared /
        verify) each with the exact entry token and its posture, then a dashed
        `cordis.patch.yml` rail carrying a large 0 (plugin rows mounted) beside
        the `template/` three-role skeleton. Nothing on the right is a promise
        the code does not keep.

  flow  (1100x660, light/dark) — a SWIMLANE, not a row of nodes: three actor
        lanes (CONSUMER / LIBRARY / HOST · CI) across four phases (SETUP /
        CALL / DISPOSE / CI GATE). Reading a column shows what each actor does
        in that phase; the HOST · CI SETUP cell is a dashed empty slot with 0
        plugin rows, and the CI lane ends in the only process exit this
        library can cause. All labels are command/config tokens in English, so
        one light/dark pair serves all five README languages.

Every SVG label is measured with the same TTF Chrome resolves locally
(Consolas / Segoe UI) and a label that would leave its box aborts the run
instead of shipping clipped text. Hero text is measured with the TTF that
draws it (msyh / msyhbd / Consolas / Segoe UI).

Outputs (idempotent overwrite):
  docs/assets/dsh-scaffold-hero-{zh,en}-{light,dark}.webp
  docs/assets/dsh-scaffold-flow-v5-{light,dark}.svg

Run once:  python scripts/gen-readme-assets.py
Requires:  Pillow, plus msyh.ttc / msyhbd.ttc / consola.ttf (CJK must never
           render as tofu boxes; missing fonts abort the run).
"""
from __future__ import annotations

import os
import re
import sys
from html import escape

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "assets")

HERO_W, HERO_H = 1440, 576
FLOW_W, FLOW_H = 1100, 660
S = 2  # hero shapes composite at 2x and are downsampled once

FONT_CJK = r"C:\Windows\Fonts\msyh.ttc"
FONT_CJK_BOLD = r"C:\Windows\Fonts\msyhbd.ttc"
FONT_MONO = r"C:\Windows\Fonts\consola.ttf"
FONT_MONO_BOLD = r"C:\Windows\Fonts\consolab.ttf"
FONT_EN = r"C:\Windows\Fonts\segoeui.ttf"
FONT_EN_BOLD = r"C:\Windows\Fonts\segoeuib.ttf"
for _p in (FONT_CJK, FONT_CJK_BOLD, FONT_MONO):
    if not os.path.exists(_p):
        sys.exit(f"FATAL: font missing: {_p} — refusing to draw (a CJK font "
                 "is mandatory; Chinese must never render as tofu boxes)")
FONT_PATHS = {
    "cjk": FONT_CJK,
    "cjk_bold": FONT_CJK_BOLD,
    "mono": FONT_MONO,
    "mono_bold": FONT_MONO_BOLD if os.path.exists(FONT_MONO_BOLD) else FONT_MONO,
    "en": FONT_EN if os.path.exists(FONT_EN) else FONT_CJK,
    "en_bold": FONT_EN_BOLD if os.path.exists(FONT_EN_BOLD) else FONT_CJK_BOLD,
}

_MEASURE = ImageDraw.Draw(Image.new("RGB", (8, 8)))

SKIN = {
    "light": dict(
        bg_from="#f9f6fd", bg_to="#e4eaf8", card="#ffffff",
        zone="#f7f5fc", zone_alt="#f1eef9", edge="#e4e1ee", rule="#e9e5f2",
        text="#141419", sub="#4d5261", faint="#8f94a4",
        accent="#4B67B4", accent_soft="#eceffb", green="#16a34a",
        green_soft="#e7f5ec", red="#cf222e", pill="#ece7f9",
        shadow=(34, 27, 66), shadow_a=30, glow_a=26, dash="#a9a2c4",
        lane_tint="#f3eff9", lane_actor="#ece7f8",
    ),
    "dark": dict(
        bg_from="#131a2a", bg_to="#0c1016", card="#1b2231",
        zone="#202839", zone_alt="#1d2534", edge="#2e374b", rule="#2a3345",
        text="#f0f3f9", sub="#a8b1c4", faint="#828da3",
        accent="#8496f5", accent_soft="#232c42", green="#3fb950",
        green_soft="#16281f", red="#f87171", pill="#242d42",
        shadow=(0, 0, 0), shadow_a=120, glow_a=40, dash="#4a5468",
        lane_tint="#171f2e", lane_actor="#1c2536",
    ),
}

# --- the package's own words ------------------------------------------------
COPY = {
    "zh": dict(
        kicker="DSH 家族共享工具包 · 零依赖 · 不挂插件行",
        value=[
            "Provider seam、审批门、脱敏与裁决：",
            "每个插件重写一遍的，这里只有一份。",
        ],
        sub=[
            "可插拔 Provider seam、fail-closed 审批门，",
            "与会话事件门、sanitize/pricing/judge 纯函数、",
            "机械校验脚本，外加 template/ 三角色骨架。",
        ],
        meta=[
            "ESM + TypeScript · dependencies {} · optional peers",
            "Node ^22.19 || >=24 · Apache-2.0",
        ],
        foot="github.com/PerryLink/dsh-scaffold",
        head_meta="exports · 4 subpaths + root barrel",
        head_meta_r="deps {} · peers optional",
        tiles=[
            dict(label="./seam", chip="可撤销", token="ProviderRegistry<T>",
                 note="重名抛错，注册可撤销"),
            dict(label="./gates", chip="fail-closed", token="applyFailClosed",
                 note="默认拒绝，仅 allow-once 放行"),
            dict(label="./shared", chip="纯函数", token="sanitize · pricing · judge",
                 note="无 I/O，浏览器安全"),
            dict(label="./verify", chip="非零即失败",
                 token="verify-license · readme · seam",
                 note="非零退出码即失败"),
        ],
        rail_title="cordis.patch.yml",
        rail_token="insert: []",
        rail_big="0",
        rail_label="plugin rows mounted",
        tpl_title="template/",
        tpl_note="三角色骨架",
        tpl_tokens="Definition / Provider / Consumer",
        tpl_contents="cordis.yml · test · README",
    ),
    "en": dict(
        kicker="SHARED TOOLKIT FOR DSH PLUGINS · ZERO DEPS",
        value=[
            "Provider seam, gates, pure modules:",
            "written once here, not in every plugin.",
        ],
        sub=[
            "A pluggable Provider seam, fail-closed approval and",
            "session-event gates, pure sanitize/pricing/judge",
            "modules, mechanical verify, and a template/ skeleton.",
        ],
        meta=[
            "ESM + TypeScript · dependencies {} · optional peers",
            "Node ^22.19 || >=24 · Apache-2.0",
        ],
        foot="github.com/PerryLink/dsh-scaffold",
        head_meta="exports · 4 subpaths + root barrel",
        head_meta_r="deps {} · peers optional",
        tiles=[
            dict(label="./seam", chip="reversible", token="ProviderRegistry<T>",
                 note="duplicate name throws; undoable"),
            dict(label="./gates", chip="fail-closed", token="applyFailClosed",
                 note="rejected by default; allow-once only"),
            dict(label="./shared", chip="pure", token="sanitize · pricing · judge",
                 note="no I/O; browser-safe"),
            dict(label="./verify", chip="non-zero fails",
                 token="verify-license · readme · seam",
                 note="exit 0 / 1, straight into CI"),
        ],
        rail_title="cordis.patch.yml",
        rail_token="insert: []",
        rail_big="0",
        rail_label="plugin rows mounted",
        tpl_title="template/",
        tpl_note="three-role skeleton",
        tpl_tokens="Definition / Provider / Consumer",
        tpl_contents="cordis.yml · test · README",
    ),
}

# --- flow copy (token English, shared by all five README languages) ---------
PHASES = [
    ("01", "SETUP", "add / import"),
    ("02", "CALL", "every call"),
    ("03", "DISPOSE", "stop / update"),
    ("04", "CI GATE", "exit code"),
]
LANES = [
    ("CONSUMER", ["plugin halves", "Host / Client"]),
    ("dsh-scaffold", ["zero-dep core", "no host import"]),
    ("HOST · CI", ["session · CI"]),
]
# cell = (title, [notes...], special) — special is None, 'zero' or 'exit'
CELLS = [
    [
        ("pnpm add", ["dsh-scaffold", "or profile channel", "import only"], None),
        ("applyFailClosed", ["registry.use · append", "strip · parseVerdict"], None),
        ("ctx.effect", ["disposer runs on", "stop / update"], None),
        ("cli.js all .", ["node lib/verify/cli.js"], None),
    ],
    [
        ("exports: 5", ["seam · gates · shared · verify", "deps {} · peers optional"], None),
        ("EffectiveDecision", ["impl · text · cost", "verdict"], None),
        ("Map.delete(name)", ["registration is undone", "no global state"], None),
        ("VerifyReport", ["license · readmes · seam", "PASS / FAIL text"], None),
    ],
    [
        ("0", ["plugin rows mounted", "insert: []"], "zero"),
        ("session.append", ["unknown type → skip", "never retried"], None),
        ("uninstall", ["= install, reversed", "nothing left over"], None),
        ("PASS / FAIL", ["printed by each gate", "exit 0 / 1"], "exit"),
    ],
]

UNIT = re.compile(r"[A-Za-z0-9_@][A-Za-z0-9_@./:+#<>=-]*| +|.", re.S)
DASHES = re.compile(r"(—|–|——|、|，|。|；|：)+")


def rgb(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return tuple(int(value[i:i + 2], 16) for i in (0, 2, 4))


def font(size: float, kind: str) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_PATHS[kind], max(1, int(round(size * S))))


_MEASURE_CACHE: dict[tuple[str, float, str], float] = {}


def measure(text: str, size: float, kind: str) -> float:
    """Logical px width using the real TTF at 2x, divided back down."""
    key = (text, size, kind)
    if key not in _MEASURE_CACHE:
        _MEASURE_CACHE[key] = _MEASURE.textlength(text, font=font(size, kind)) / S
    return _MEASURE_CACHE[key]


def wrap(text: str, size: float, kind: str, maxw: float) -> list[str]:
    lines: list[str] = []
    line = ""
    for unit in UNIT.findall(text):
        if unit == " ":
            if line:
                line += " "
            continue
        trial = line + unit
        if line and measure(trial.rstrip(), size, kind) > maxw:
            lines.append(line.rstrip())
            line = unit
        else:
            line = trial
    if line:
        lines.append(line.rstrip())
    return lines


def must_fit(text: str, size: float, kind: str, maxw: float, where: str) -> None:
    if measure(text, size, kind) > maxw:
        sys.exit(f"FATAL: {where} overflows: {measure(text, size, kind):.1f}px > "
                 f"{maxw:.1f}px — {text!r}")


def fit_size(text: str, base: float, kind: str, maxw: float, floor: float,
             where: str) -> float:
    size = base
    while size > floor and measure(text, size, kind) > maxw:
        size -= 0.5
    if measure(text, size, kind) > maxw:
        sys.exit(f"FATAL: {where} cannot fit: {text!r}")
    return size


# ===========================================================================
# hero — package anatomy (Pillow, 2x supersampled)
# ===========================================================================
def gradient(w: int, h: int, top: str, bottom: str) -> Image.Image:
    strip = Image.new("RGB", (1, h))
    px = strip.load()
    c1, c2 = rgb(top), rgb(bottom)
    for y in range(h):
        t = y / max(1, h - 1)
        px[0, y] = tuple(round(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))
    return strip.resize((w, h), Image.BILINEAR)


def soft_glow(img: Image.Image, cx: float, cy: float, radius: float,
              color: str, alpha: int) -> Image.Image:
    d = int(radius * 2 * S)
    mask = Image.radial_gradient("L").resize((d, d), Image.BILINEAR)
    mask = mask.point(lambda v: max(0, int((128 - v) / 128 * alpha)))
    layer = Image.new("RGBA", img.size, rgb(color) + (0,))
    glow = Image.new("RGBA", (d, d), rgb(color) + (255,))
    glow.putalpha(mask)
    layer.alpha_composite(glow, (int(cx * S - d / 2), int(cy * S - d / 2)))
    return Image.alpha_composite(img, layer)


def dash_segments(points: list[tuple[float, float]], dash: float,
                  gap: float) -> list[tuple[tuple[float, float], tuple[float, float]]]:
    out = []
    on, phase = True, 0.0
    for (x1, y1), (x2, y2) in zip(points, points[1:]):
        length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        t = 0.0
        while t < length:
            step = (dash if on else gap) - phase
            take = min(step, length - t)
            if on and take > 0.15:
                a = t / length
                b = (t + take) / length
                out.append(((x1 + (x2 - x1) * a, y1 + (y2 - y1) * a),
                            (x1 + (x2 - x1) * b, y1 + (y2 - y1) * b)))
            t += take
            phase += take
            if phase >= (dash if on else gap) - 1e-6:
                phase = 0.0
                on = not on
    return out


def rounded_points(x0: float, y0: float, x1: float, y1: float, r: float,
                   step: float = 2.0) -> list[tuple[float, float]]:
    import math
    pts: list[tuple[float, float]] = []

    def line(ax, ay, bx, by):
        n = max(1, int(((bx - ax) ** 2 + (by - ay) ** 2) ** 0.5 / step))
        for i in range(n + 1):
            pts.append((ax + (bx - ax) * i / n, ay + (by - ay) * i / n))

    def arc(cx, cy, a0, a1):
        n = max(2, int(abs(a1 - a0) / 6))
        for i in range(n + 1):
            a = math.radians(a0 + (a1 - a0) * i / n)
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))

    line(x0 + r, y0, x1 - r, y0)
    arc(x1 - r, y0 + r, -90, 0)
    line(x1, y0 + r, x1, y1 - r)
    arc(x1 - r, y1 - r, 0, 90)
    line(x1 - r, y1, x0 + r, y1)
    arc(x0 + r, y1 - r, 90, 180)
    line(x0, y1 - r, x0, y0 + r)
    arc(x0 + r, y0 + r, 180, 270)
    return pts


class Hero:
    def __init__(self, skin: str, lang: str):
        self.s = SKIN[skin]
        self.c = COPY[lang]
        self.zh = lang == "zh"
        self.img = gradient(HERO_W * S, HERO_H * S, self.s["bg_from"],
                            self.s["bg_to"]).convert("RGBA")
        self.img = soft_glow(self.img, 1190, 40, 430, self.s["accent"],
                             self.s["glow_a"])
        self.img = soft_glow(self.img, 120, 580, 300, self.s["accent"],
                             max(10, self.s["glow_a"] // 2))
        self.d = ImageDraw.Draw(self.img)

    def sc(self, box):
        return tuple(int(round(v * S)) for v in box)

    def text(self, x, y, text, size, color, kind="cjk", anchor=None,
             bold=False):
        self.d.text((x * S, y * S), text,
                    font=font(size, kind if not bold else kind),
                    fill=color, anchor=anchor)

    def chip(self, x_right, y, text, color, fill, size=12.0):
        w = measure(text, size, "cjk_bold" if self.zh else "en_bold") + 18
        self.d.rounded_rectangle(self.sc((x_right - w, y, x_right, y + 21)),
                                 radius=10 * S, fill=fill)
        self.text(x_right - w + 9, y + 15.5, text, size, color,
                  "cjk_bold" if self.zh else "en_bold")

    def build(self) -> Image.Image:
        s, c = self.s, self.c
        # card shadow
        shadow = Image.new("RGBA", self.img.size, (0, 0, 0, 0))
        sd = ImageDraw.Draw(shadow)
        sd.rounded_rectangle(self.sc((716, 46, 1372, 536)), radius=22 * S,
                             fill=s["shadow"] + (s["shadow_a"],))
        shadow = shadow.filter(ImageFilter.GaussianBlur(16 * S))
        self.img = Image.alpha_composite(self.img, shadow)
        self.d = ImageDraw.Draw(self.img)

        # package card
        self.d.rounded_rectangle(self.sc((716, 46, 1372, 536)), radius=22 * S,
                                 fill=s["card"], outline=s["edge"],
                                 width=max(1, int(1.2 * S)))

        # header
        self.text(744, 88, "dsh-scaffold", 20, s["text"], "mono_bold")
        self.text(1344, 88, "v0.2.1", 12, s["faint"], "mono", anchor="rs")
        self.text(744, 111, c["head_meta"], 12, s["faint"], "mono")
        self.text(1344, 111, c["head_meta_r"], 12, s["faint"], "mono",
                  anchor="rs")
        self.d.line(self.sc((744, 122, 1344, 122)), fill=s["rule"],
                    width=max(1, int(1.2 * S)))

        # four surface tiles
        tiles = c["tiles"]
        for i, tile in enumerate(tiles):
            col, row = i % 2, i // 2
            x, y = 744 + col * 308, 132 + row * 148
            w, h = 292, 140
            stripe = s["green"] if tile["label"] == "./verify" else s["accent"]
            self.d.rounded_rectangle(self.sc((x, y, x + w, y + h)),
                                     radius=15 * S, fill=s["zone"],
                                     outline=s["edge"], width=max(1, int(1.1 * S)))
            self.d.rounded_rectangle(self.sc((x + 1, y + 14, x + 5, y + h - 14)),
                                     radius=2 * S, fill=stripe)
            self.text(x + 17, y + 40, tile["label"], 18, s["text"], "mono_bold")
            self.chip(x + w - 14, y + 14, tile["chip"], s["accent"],
                      s["pill"], 12.0)
            self.text(x + 17, y + 86, tile["token"], 15, s["text"], "mono")
            self.text(x + 17, y + 122, tile["note"], 14, s["sub"],
                      "cjk" if self.zh else "en")
            must_fit(tile["label"], 18, "mono_bold", 190, "hero tile label")
            must_fit(tile["token"], 15, "mono", 258, "hero tile token")
            must_fit(tile["note"], 14, "cjk" if self.zh else "en", 258,
                     "hero tile note")

        # dashed patch rail: the package mounts nothing
        pts = rounded_points(744, 434, 1074, 526, 16)
        for (ax, ay), (bx, by) in dash_segments(pts + [pts[0]], 7, 5):
            self.d.line((ax * S, ay * S, bx * S, by * S), fill=s["dash"],
                        width=max(1, int(1.3 * S)))
        self.text(760, 458, c["rail_title"], 15, s["text"], "mono")
        self.text(760, 486, c["rail_token"], 13, s["accent"], "mono_bold")
        self.text(1058, 491, c["rail_big"], 36, s["accent"], "mono_bold",
                  anchor="rs")
        self.text(1058, 514, c["rail_label"], 13, s["faint"],
                  "cjk" if self.zh else "en", anchor="rs")

        # template card
        self.d.rounded_rectangle(self.sc((1090, 434, 1344, 526)), radius=16 * S,
                                 fill=s["green_soft"], outline=s["green"],
                                 width=max(1, int(1.1 * S)))
        self.text(1106, 458, c["tpl_title"], 15, s["text"], "mono_bold")
        self.text(1330, 458, c["tpl_note"], 11.5, s["green"],
                  "cjk" if self.zh else "en_bold", anchor="rs")
        self.text(1106, 484, c["tpl_tokens"], 12, s["sub"], "mono")
        self.text(1106, 506, c["tpl_contents"], 12, s["faint"], "mono")

        # ---- left column: the prose seven --------------------------------
        ksize = 16 if self.zh else 14.5
        kkind = "cjk_bold" if self.zh else "en_bold"
        kw = measure(c["kicker"], ksize, kkind) + 44
        self.d.rounded_rectangle(self.sc((64, 46, 64 + kw, 78)), radius=16 * S,
                                 fill=s["pill"])
        self.d.ellipse(self.sc((80, 58, 88, 66)), fill=s["accent"])
        self.text(96, 68.5, c["kicker"], ksize, s["accent"], kkind)

        title_size = fit_size("dsh-scaffold", 86, "mono_bold", 620, 60,
                              "hero title")
        self.text(62, 180, "dsh-scaffold", title_size, s["text"], "mono_bold")

        vkind = "cjk_bold" if self.zh else "en_bold"
        vsize = min(fit_size(line, 33, vkind, 620, 27, "hero value")
                    for line in c["value"])
        y = 252
        for line in c["value"]:
            self.text(64, y, line, vsize, s["text"], vkind)
            y += int(round(vsize * 1.38))

        skind = "cjk" if self.zh else "en"
        ssize = 25.5
        sub_lines = c["sub"]
        for line in sub_lines:
            must_fit(line, ssize, skind, 620, "hero subtitle line")
        y = 356
        for line in sub_lines:
            self.text(64, y, line, ssize, s["sub"], skind)
            y += 38

        for i, line in enumerate(c["meta"]):
            must_fit(line, 20, "mono", 620, "hero meta")
            self.text(64, 488 + i * 28, line, 20, s["faint"], "mono")
        self.text(64, 552, c["foot"], 17, s["faint"], "mono")

        return self.img.convert("RGB").resize((HERO_W, HERO_H), Image.LANCZOS)


# ===========================================================================
# flow — swimlane SVG (1100x660, light/dark, no raster)
# ===========================================================================
MONO = ("ui-monospace, 'Cascadia Code', Consolas, 'SF Mono', "
        "'Liberation Mono', monospace")
SANS = ("ui-sans-serif, system-ui, -apple-system, 'Segoe UI', "
        "'Helvetica Neue', Arial, sans-serif")
MONO_MEASURE = "mono"
SANS_MEASURE = "en"

FLOW = {
    "light": dict(
        bg_from="#f9f6fd", bg_to="#e4eaf8", card="#ffffff", zone="#f5f2fc",
        lane="#faf8fe", actor="#efeaf9", edge="#e3dfee", rule="#e6e2f0",
        text="#141419", sub="#4d5261", faint="#8f94a4", accent="#4B67B4",
        accent_soft="#eceffb", green="#16a34a", green_soft="#e8f5ec",
        red="#cf222e", dash="#a9a2c4", step="#b9b3cd",
    ),
    "dark": dict(
        bg_from="#131a2a", bg_to="#0c1016", card="#1b2231", zone="#171e2d",
        lane="#1a2231", actor="#212b3f", edge="#2e374b", rule="#2a3345",
        text="#f0f3f9", sub="#a8b1c4", faint="#737b8d", accent="#8496f5",
        accent_soft="#232c42", green="#3fb950", green_soft="#16281f",
        red="#f87171", dash="#4a5468", step="#5b657c",
    ),
}


class Svg:
    def __init__(self, skin: str):
        self.s = FLOW[skin]
        self.parts: list[str] = []
        self.checks: list[str] = []

    def raw(self, text: str):
        self.parts.append(text)

    def text(self, x, y, text, size, fill, kind="mono", weight=400,
             anchor="start", opacity=1.0):
        if opacity != 1.0:
            fill = fill
        body = escape(text)
        extra = f' opacity="{opacity}"' if opacity != 1.0 else ""
        self.parts.append(
            f'<text x="{x:g}" y="{y:g}" fill="{fill}"{extra} '
            f'font-family="{MONO if kind == "mono" else SANS}" '
            f'font-size="{size:g}"' +
            (f' font-weight="{weight}"' if weight != 400 else "") +
            (f' text-anchor="{anchor}"' if anchor != "start" else "") +
            f'>{body}</text>')

    def fit(self, text, size, kind, maxw, where, weight=400):
        width = measure(text, size, kind)
        if width > maxw:
            sys.exit(f"FATAL: SVG {where} overflows: {width:.1f}px > "
                     f"{maxw:.1f}px — {text!r}")
        self.checks.append(f"{where}: {width:.1f}/{maxw:.1f}")

    def cell(self, x, y, w, h, phase, title, notes, special, kind_fill=None):
        s = self.s
        dashed = special == "zero"
        self.parts.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" '
            f'fill="{s["card"]}" stroke="{s["accent"] if dashed else s["edge"]}" '
            f'stroke-width="{1.6 if dashed else 1.2}"' +
            (' stroke-dasharray="7 5"' if dashed else "") + "/>")
        # step number
        self.text(x + w - 12, y + 22, phase, 11, s["step"], "mono",
                  anchor="end")

        if special == "zero":
            self.text(x + 16, y + 74, "0", 40, s["accent"], "mono", weight=700)
            self.text(x + 52, y + 74, notes[0], 14, s["sub"], "en")
            self.fit(notes[0], 14, SANS_MEASURE, 154, "cell zero note")
            self.text(x + 16, y + 106, notes[1], 14, s["accent"], "mono",
                      weight=700)
            self.fit(notes[1], 14, MONO_MEASURE, 194, "cell zero mono")
            return

        tsize = 17
        self.fit(title, tsize, MONO_MEASURE, 194, "cell title", weight=700)
        self.text(x + 16, y + 46, title, tsize, s["text"], "mono", weight=700)
        if special == "exit":
            # recolour the two words: PASS / FAIL
            self.parts.pop()
            self.parts.append(
                f'<text x="{x + 16}" y="{y + 46}" font-family="{MONO}" '
                f'font-size="17" font-weight="700">'
                f'<tspan fill="{s["green"]}">PASS</tspan>'
                f'<tspan fill="{s["faint"]}"> / </tspan>'
                f'<tspan fill="{s["red"]}">FAIL</tspan></text>')
        ny = y + 78
        for note in notes:
            self.fit(note, 14, SANS_MEASURE, 194, "cell note")
            self.text(x + 16, ny, note, 14, s["sub"], "en")
            ny += 20

    def build(self) -> str:
        s = self.s
        self.raw(f'<svg xmlns="http://www.w3.org/2000/svg" width="{FLOW_W}" '
                 f'height="{FLOW_H}" viewBox="0 0 {FLOW_W} {FLOW_H}" '
                 f'role="img" aria-labelledby="t d">')
        self.raw('<title id="t">dsh-scaffold structure: three actor lanes '
                 '(consumer / library / host · CI) across four phases — setup, '
                 'call, dispose, CI gate</title>')
        self.raw('<desc id="d">The package exports four subpaths; setup mounts '
                 'zero plugin rows in the host, calls use the pure helpers, '
                 'stop runs the disposer, and the CI gate turns the verify '
                 'report into one exit code.</desc>')
        self.raw('<defs>')
        self.raw(f'<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">'
                 f'<stop offset="0" stop-color="{s["bg_from"]}"/>'
                 f'<stop offset="1" stop-color="{s["bg_to"]}"/></linearGradient>')
        self.raw(f'<radialGradient id="glow" cx="0.5" cy="0.5" r="0.5">'
                 f'<stop offset="0" stop-color="{s["accent"]}" stop-opacity="0.16"/>'
                 f'<stop offset="1" stop-color="{s["accent"]}" stop-opacity="0"/>'
                 f'</radialGradient>')
        self.raw('</defs>')
        self.raw(f'<rect width="{FLOW_W}" height="{FLOW_H}" rx="20" '
                 f'fill="url(#bg)"/>')
        self.raw(f'<circle cx="985" cy="30" r="300" fill="url(#glow)"/>')

        # header
        self.text(30, 48, "dsh-scaffold structure", 28, s["text"], "mono",
                  weight=700)
        self.fit("dsh-scaffold structure", 28, MONO_MEASURE, 520, "flow title",
                 weight=700)
        sub = ("three actors × four phases — import, call, dispose, verify; "
               "the package starts no I/O of its own")
        self.fit(sub, 14.5, SANS_MEASURE, 700, "flow subtitle")
        self.text(30, 73, sub, 14.5, s["sub"], "en")
        meta_r = "0 runtime deps · 0 plugin rows"
        meta_r2 = "4 subpaths + root barrel · v0.2.1"
        self.fit(meta_r, 14, MONO_MEASURE, 330, "flow meta right")
        self.fit(meta_r2, 14, MONO_MEASURE, 330, "flow meta right 2")
        self.text(1068, 48, meta_r, 14, s["faint"], "mono", anchor="end")
        self.text(1068, 69, meta_r2, 14, s["faint"], "mono", anchor="end")
        self.raw(f'<line x1="30" y1="88" x2="1068" y2="88" '
                 f'stroke="{s["rule"]}" stroke-width="1.2"/>')

        # phase headers
        self.text(30, 126, "ACTOR / PHASE", 14, s["faint"], "mono")
        for i, (num, label, note) in enumerate(PHASES):
            x = 172 + i * 226
            accent = s["green"] if i == 3 else s["accent"]
            soft = s["green_soft"] if i == 3 else s["accent_soft"]
            self.raw(f'<rect x="{x}" y="100" width="218" height="38" rx="12" '
                     f'fill="{soft}" stroke="{accent}" stroke-opacity="0.45"/>')
            self.raw(f'<circle cx="{x + 24}" cy="119" r="11" '
                     f'fill="{s["card"]}" stroke="{accent}" stroke-opacity="0.5"/>')
            self.text(x + 24, 123.5, num, 11, accent, "mono", anchor="middle")
            self.text(x + 43, 125, label, 15, s["text"], "mono", weight=700)
            self.fit(label, 15, MONO_MEASURE, 90, "phase label", weight=700)
            self.text(x + 206, 125, note, 14, accent, "en", anchor="end")
            self.fit(note, 14, SANS_MEASURE, 96, "phase note")

        # lanes + cells
        for lane_i, (lane_name, lane_notes) in enumerate(LANES):
            ly = 144 + lane_i * 164
            self.raw(f'<rect x="30" y="{ly}" width="1038" height="156" rx="16" '
                     f'fill="{s["lane"]}" stroke="{s["rule"]}"/>')
            self.raw(f'<rect x="30" y="{ly}" width="132" height="156" rx="16" '
                     f'fill="{s["actor"]}"/>')
            self.raw(f'<rect x="30" y="{ly + 16}" width="4" height="124" rx="2" '
                     f'fill="{s["accent"] if lane_i < 2 else s["green"]}"/>')
            self.text(50, ly + 56, lane_name, 15, s["text"],
                      "mono" if lane_i == 1 else "en", weight=700)
            self.fit(lane_name, 15, MONO_MEASURE if lane_i == 1 else SANS_MEASURE,
                     104, "lane name")
            for j, note in enumerate(lane_notes):
                self.fit(note, 14, SANS_MEASURE, 104, "lane note")
                self.text(50, ly + 80 + j * 20, note, 14, s["sub"], "en")
            for col in range(4):
                cx = 172 + col * 226
                title, notes, special = CELLS[lane_i][col]
                self.cell(cx, ly + 10, 218, 136, PHASES[col][0], title, notes,
                          special)

        # footer
        foot_l = ("dashed cell: no plugin row mounted · phase 04 runs in CI "
                  "on the same package")
        foot_r = "a refused append is a skip, never a retry"
        self.fit(foot_l, 14, SANS_MEASURE, 720, "flow footer left")
        self.fit(foot_r, 14, SANS_MEASURE, 300, "flow footer right")
        self.text(30, 648, foot_l, 14, s["sub"], "en")
        self.text(1068, 648, foot_r, 14, s["sub"], "en", anchor="end")
        self.raw("</svg>")
        return "\n".join(self.parts) + "\n"


def main() -> None:
    os.makedirs(OUT, exist_ok=True)
    for lang in ("zh", "en"):
        for skin in ("light", "dark"):
            img = Hero(skin, lang).build()
            path = os.path.join(OUT, f"dsh-scaffold-hero-{lang}-{skin}.webp")
            img.save(path, "WEBP", quality=90, method=6)
            print(f"wrote {path}  {img.size[0]}x{img.size[1]}")

    for skin in ("light", "dark"):
        svg = Svg(skin).build()
        path = os.path.join(OUT, f"dsh-scaffold-flow-v5-{skin}.svg")
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(svg)
        print(f"wrote {path}  {FLOW_W}x{FLOW_H}")
    print("done: 4 hero webp + 2 flow svg (no evidence chart: no benchmark "
          "data in this repo)")


if __name__ == "__main__":
    main()
