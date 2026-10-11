"""Khung chung cho bài giảng: giao diện, giọng đọc (edge-tts) đồng bộ với hình, phụ đề."""
import asyncio
import hashlib
import json
import os
import re
from contextlib import contextmanager
from pathlib import Path

import edge_tts
from manim import *
from mutagen.mp3 import MP3

ROOT = Path(__file__).resolve().parent
VOICE_DIR = ROOT / "voice_cache"
SUB_DIR = ROOT / "subs"
VOICE = os.environ.get("LECTURE_VOICE", "vi-VN-NamMinhNeural")
RATE = os.environ.get("LECTURE_RATE", "-4%")

FONT = "Noto Sans"
BG = "#0E1726"
PANEL = "#16233A"
FG = "#E8EEF6"
MUTED = "#9AAAC0"
ACCENT = "#4FD1C5"   # xanh ngọc: tiêu đề, nhấn
GOLD = "#F6C453"     # vàng: điểm quan trọng
RED = "#FF7A7A"
GREEN = "#7BE495"
BLUE = "#6CB4FF"
PURPLE = "#C39BFF"

config.background_color = BG
MathTex.set_default(color=FG)
Tex.set_default(color=FG)


def synth(text: str) -> Path:
    VOICE_DIR.mkdir(exist_ok=True)
    key = hashlib.sha1(f"{VOICE}|{RATE}|{text}".encode()).hexdigest()[:16]
    path = VOICE_DIR / f"{key}.mp3"
    if not path.exists() or path.stat().st_size == 0:
        async def run():
            await edge_tts.Communicate(text, VOICE, rate=RATE).save(str(path))
        for attempt in range(4):
            try:
                asyncio.run(run())
                break
            except Exception:
                if attempt == 3:
                    raise
                import time
                time.sleep(3 * (attempt + 1))
    return path


def vt(text, size=30, color=FG, weight=NORMAL, align=LEFT, **kw):
    """Chữ tiếng Việt (Pango). Nhiều dòng ('\\n') được dựng từng dòng để giãn dòng thoáng."""
    if "\n" in text:
        lines = [Text(t, font=FONT, font_size=size, color=color, weight=weight, **kw)
                 for t in text.split("\n")]
        return VGroup(*lines).arrange(DOWN, buff=size / 100 * 0.22, aligned_edge=align)
    return Text(text, font=FONT, font_size=size, color=color, weight=weight, **kw)


def mt(*tex, size=40, color=FG, **kw):
    return MathTex(*tex, font_size=size, color=color, **kw)


def mix(*parts, size=28, color=FG, buff=0.14):
    """Ghép chữ và công thức trên một dòng: phần tử bắt đầu bằng '$' là công thức."""
    mobs = []
    for p in parts:
        if isinstance(p, Mobject):
            mobs.append(p)
        elif p.startswith("$"):
            mobs.append(MathTex(p.strip("$"), font_size=size * 1.35, color=color))
        else:
            mobs.append(Text(p, font=FONT, font_size=size, color=color))
    return VGroup(*mobs).arrange(RIGHT, buff=buff)


def bullet_list(items, size=28, gap=0.32, width=12.2, color=FG, dot_color=ACCENT):
    rows = VGroup()
    for it in items:
        if isinstance(it, Mobject):
            body = it
        else:
            body = vt(it, size=size, color=color)
            if body.width > width:
                body.scale_to_fit_width(width)
        dot = Dot(radius=0.06, color=dot_color)
        row = VGroup(dot, body).arrange(RIGHT, buff=0.25)
        if isinstance(it, str) and "\n" in it:
            dot.set_y(body[0].get_y())
        rows.add(row)
    rows.arrange(DOWN, buff=gap, aligned_edge=LEFT)
    return rows


def box(mob, color=ACCENT, buff=0.22, fill=PANEL, opacity=0.9, corner=0.12):
    return SurroundingRectangle(mob, color=color, buff=buff, corner_radius=corner,
                                fill_color=fill, fill_opacity=opacity, stroke_width=2)


def boxed(mob, **kw):
    r = box(mob, **kw)
    return VGroup(r, mob)


def labeled_matrix(rows, size=32, color=FG, h_buff=0.9, v_buff=0.6):
    m = Matrix(rows, h_buff=h_buff, v_buff=v_buff,
               element_to_mobject=lambda s: MathTex(str(s), font_size=size, color=color),
               bracket_h_buff=0.12)
    m.get_brackets().set_color(MUTED)
    return m


class Lecture(Scene):
    """Scene có giọng đọc: dùng `with self.say("..."):` rồi chạy hoạt ảnh bên trong."""

    section_label = ""

    def setup(self):
        self._subs = []
        self.title_mob = None
        self.tag = None
        if self.section_label:
            self.tag = vt(self.section_label, size=18, color=MUTED).to_corner(DR, buff=0.25)
            self.add(self.tag)

    @contextmanager
    def say(self, text, pad=0.35):
        text = " ".join(text.split())
        path = synth(text)
        dur = MP3(str(path)).info.length
        start = self.renderer.time
        self.add_sound(str(path))
        self._subs.append({"start": start, "end": start + dur, "text": text})
        yield dur
        elapsed = self.renderer.time - start
        if elapsed < dur + pad:
            self.wait(dur + pad - elapsed)

    def narrate(self, text, *anims, run_time=None, pad=0.35):
        with self.say(text, pad=pad) as d:
            if anims:
                self.play(*anims, run_time=run_time or min(2.0, d * 0.5))

    def tear_down(self):
        SUB_DIR.mkdir(exist_ok=True)
        with open(SUB_DIR / f"{type(self).__name__}.json", "w", encoding="utf-8") as f:
            json.dump({"subs": self._subs, "duration": self.renderer.time}, f,
                      ensure_ascii=False, indent=1)

    # ---------- bố cục ----------
    def set_title(self, text, sub=None, color=ACCENT):
        t = vt(text, size=38, color=color, weight=BOLD)
        if t.width > 12.8:
            t.scale_to_fit_width(12.8)
        grp = VGroup(t)
        if sub:
            s = vt(sub, size=22, color=MUTED)
            grp.add(s)
            grp.arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        grp.to_corner(UL, buff=0.45)
        line = Line(LEFT * 7, RIGHT * 7, color=color, stroke_width=1.5, stroke_opacity=0.5)
        line.next_to(grp, DOWN, buff=0.18).set_x(0)
        new = VGroup(grp, line)
        if self.title_mob is None:
            self.play(FadeIn(grp, shift=RIGHT * 0.3), Create(line), run_time=0.8)
            self.remove(grp, line)
            self.add(new)
        else:
            self.play(FadeOut(self.title_mob, shift=UP * 0.2), FadeIn(new, shift=UP * 0.2),
                      run_time=0.7)
        self.title_mob = new
        return new

    def fit(self, mob, top_buff=0.35, bottom=-3.25, max_width=13.2, grow=1.0):
        """Đặt nhóm nội dung ngay dưới tiêu đề, co lại nếu tràn khung (hoặc phóng to tới `grow` lần)."""
        top = self.title_mob.get_bottom()[1] - top_buff if self.title_mob else 3.6
        avail = top - bottom
        k = min(avail / mob.height, max_width / mob.width, grow)
        if k != 1:
            mob.scale(k)
        mob.set_x(0)
        mob.set_y(top - mob.height / 2)
        return mob

    def content_mobs(self):
        keep = {self.title_mob, self.tag}
        return [m for m in self.mobjects if m not in keep]

    def clear_content(self, run_time=0.6):
        mobs = self.content_mobs()
        if mobs:
            self.play(*[FadeOut(m) for m in mobs], run_time=run_time)

    def clear_all(self, run_time=0.6):
        mobs = [m for m in self.mobjects if m is not self.tag]
        if mobs:
            self.play(*[FadeOut(m) for m in mobs], run_time=run_time)
        self.title_mob = None

    def section_card(self, number, title, subtitle=""):
        num = vt(number, size=30, color=ACCENT, weight=BOLD)
        t = vt(title, size=50, color=FG, weight=BOLD)
        if t.width > 12:
            t.scale_to_fit_width(12)
        grp = VGroup(num, t)
        if subtitle:
            grp.add(vt(subtitle, size=26, color=MUTED))
        grp.arrange(DOWN, buff=0.35)
        bar = Rectangle(width=0.12, height=grp.height + 0.4, fill_color=ACCENT,
                        fill_opacity=1, stroke_width=0).next_to(grp, LEFT, buff=0.5)
        return VGroup(bar, grp).move_to(ORIGIN)


def table(rows, col_widths, row_h=0.62, header_color=ACCENT, size=26, line_color=MUTED):
    """Bảng đơn giản: rows là list các list mobject hoặc chuỗi (chuỗi -> Text)."""
    grp = VGroup()
    y = 0
    heights = []
    built = []
    for i, row in enumerate(rows):
        cells = []
        for j, c in enumerate(row):
            if isinstance(c, str):
                c = vt(c, size=size, color=header_color if i == 0 else FG,
                       weight=BOLD if i == 0 else NORMAL)
            if c.width > col_widths[j] - 0.2:
                c.scale_to_fit_width(col_widths[j] - 0.2)
            cells.append(c)
        h = max(row_h, max(c.height for c in cells) + 0.25)
        heights.append(h)
        built.append(cells)
    total_w = sum(col_widths)
    for i, cells in enumerate(built):
        h = heights[i]
        x = -total_w / 2
        for j, c in enumerate(cells):
            c.move_to([x + col_widths[j] / 2, y - h / 2, 0])
            x += col_widths[j]
        grp.add(VGroup(*cells))
        y -= h
    lines = VGroup()
    top = 0
    lines.add(Line([-total_w / 2, top, 0], [total_w / 2, top, 0], color=line_color, stroke_width=2))
    yy = -heights[0]
    lines.add(Line([-total_w / 2, yy, 0], [total_w / 2, yy, 0], color=line_color, stroke_width=1.5))
    lines.add(Line([-total_w / 2, y, 0], [total_w / 2, y, 0], color=line_color, stroke_width=2))
    out = VGroup(lines, grp)
    out.rows = grp
    out.lines = lines
    out.heights = heights
    out.move_to(ORIGIN)
    return out


def row_highlight(tbl, i, color=GOLD, opacity=0.18):
    r = tbl.rows[i]
    w = tbl.lines[0].get_length()
    h = tbl.heights[i]
    rect = Rectangle(width=w, height=h, fill_color=color, fill_opacity=opacity, stroke_width=0)
    top = tbl.lines[0].get_y() - sum(tbl.heights[:i])
    rect.move_to([tbl.lines[0].get_center()[0], top - h / 2, 0])
    return rect


def legend(eq, idxs, labels, size=24, cols=2, col_gap=1.0):
    """Chú giải ký hiệu: gạch chân từng phần của công thức và liệt kê 'ký hiệu — ý nghĩa'."""
    unders = VGroup()
    items = VGroup()
    for i, lab in zip(idxs, labels):
        part = eq[i]
        col = part.get_color()
        unders.add(Line(part.get_corner(DL) + DOWN * 0.1, part.get_corner(DR) + DOWN * 0.1,
                        color=col, stroke_width=3))
        sym = part.copy().scale(0.75)
        txt = Text(lab, font=FONT, font_size=size, color=col)
        items.add(VGroup(sym, Text(":", font=FONT, font_size=size, color=MUTED), txt).arrange(RIGHT, buff=0.15))
    grid = VGroup()
    rows = [items[k:k + cols] for k in range(0, len(items), cols)]
    widths = [max(r[c].width for r in rows if c < len(r)) for c in range(cols)]
    for r in rows:
        line = VGroup()
        x = 0
        for c, it in enumerate(r):
            it.move_to([x + it.width / 2, 0, 0])
            x += widths[c] + col_gap
            line.add(it)
        grid.add(line)
    grid.arrange(DOWN, buff=0.28, aligned_edge=LEFT)
    grid.next_to(eq, DOWN, buff=0.6)
    return unders, grid
