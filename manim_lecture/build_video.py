"""Dựng toàn bộ bài giảng: render các scene, ghép video, tạo phụ đề tiếng Việt.

Cách dùng (trong thư mục manim_lecture):
    python build_video.py            # 1080p30, ghép + phụ đề
    python build_video.py --quality l  # bản nháp 480p
    python build_video.py --skip-render  # chỉ ghép lại từ các file đã render
"""
import argparse
import json
import os
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FFMPEG = str(ROOT.parent / ".menv" / "bin" / "ffmpeg")
FFPROBE = str(ROOT.parent / ".menv" / "bin" / "ffprobe")
MANIM = str(ROOT.parent / ".menv" / "bin" / "manim")

SCENES = [
    ("part1_anova", "S00_Intro"),
    ("part1_anova", "S01_AnovaModel"),
    ("part1_anova", "S02_AnovaExample"),
    ("part2_terms", "S03_Terms"),
    ("part3_oneway", "S04_OneWayModel"),
    ("part3_oneway", "S05_Example69"),
    ("part3_oneway", "S06_Example610"),
    ("part4_twoway", "S07_TwoWayUni"),
    ("part4_twoway", "S08_TwoWayMulti"),
    ("part5_example613", "S09_Example613"),
    ("part5_example613", "S10_Summary"),
]
QDIR = {"l": "480p15", "m": "720p30", "h": "1080p30"}
QFLAGS = {"l": ["-ql"], "m": ["-qm"], "h": ["-qh", "--fps", "30"]}


def duration(path):
    out = subprocess.check_output([FFPROBE, "-v", "error", "-show_entries", "format=duration",
                                   "-of", "csv=p=0", str(path)])
    return float(out)


def chunks(text, limit=80):
    """Cắt lời giảng thành các dòng phụ đề ngắn theo câu / dấu phẩy."""
    parts = re.split(r"(?<=[.?!:;])\s+", text)
    out = []
    for p in parts:
        while len(p) > limit:
            cut = p.rfind(", ", 0, limit)
            if cut < limit * 0.4:
                cut = p.rfind(" ", 0, limit)
            out.append(p[:cut + 1].strip())
            p = p[cut + 1:].strip()
        if p:
            out.append(p)
    return out


def ts(t):
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int(round((s - int(s)) * 1000)) % 1000:03d}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quality", default="h", choices=list(QDIR))
    ap.add_argument("--skip-render", action="store_true")
    ap.add_argument("--jobs", type=int, default=2)
    ap.add_argument("--out", default=str(ROOT.parent / "BaiGiang_MANOVA_6.4_6.7"))
    args = ap.parse_args()
    env = dict(os.environ)
    env["PATH"] = str(Path.home() / ".TinyTeX/bin/x86_64-linux") + os.pathsep + env["PATH"]

    if not args.skip_render:
        from concurrent.futures import ThreadPoolExecutor
        mods = {}
        for mod, scene in SCENES:
            mods.setdefault(mod, []).append(scene)

        def render(item):
            mod, scenes = item
            print("render", mod, *scenes, flush=True)
            r = subprocess.run([MANIM, *QFLAGS[args.quality], f"{mod}.py", *scenes], cwd=ROOT, env=env,
                               capture_output=True, text=True)
            if r.returncode:
                print(r.stdout[-3000:], r.stderr[-3000:])
                raise SystemExit(f"Lỗi render {mod}")

        with ThreadPoolExecutor(args.jobs) as ex:
            list(ex.map(render, mods.items()))

    files = [ROOT / "media" / "videos" / mod / QDIR[args.quality] / f"{scene}.mp4" for mod, scene in SCENES]
    missing = [str(f) for f in files if not f.exists()]
    if missing:
        raise SystemExit("Thiếu file:\n" + "\n".join(missing))

    # phụ đề
    srt, offset, n = [], 0.0, 1
    chapters = []
    for (mod, scene), f in zip(SCENES, files):
        data = json.load(open(ROOT / "subs" / f"{scene}.json", encoding="utf-8"))
        chapters.append((offset, scene))
        for s in data["subs"]:
            pieces = chunks(s["text"])
            total = sum(len(p) for p in pieces)
            t = s["start"]
            span = s["end"] - s["start"]
            for p in pieces:
                d = span * len(p) / total
                srt.append(f"{n}\n{ts(offset + t)} --> {ts(offset + t + d)}\n{p}\n")
                n += 1
                t += d
        offset += duration(f)
    out = Path(args.out)
    srt_path = out.with_suffix(".srt")
    srt_path.write_text("\n".join(srt), encoding="utf-8")

    # ghép video
    lst = ROOT / "concat_list.txt"
    lst.write_text("".join(f"file '{f}'\n" for f in files))
    joined = ROOT / "joined.mp4"
    subprocess.run([FFMPEG, "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst),
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", str(joined)], check=True)

    # chương (metadata) để tua nhanh
    titles = {
        "S00_Intro": "Mở đầu", "S01_AnovaModel": "Phần 1 - Tổng quan ANOVA", "S02_AnovaExample": "Ví dụ 6.7 & 6.8",
        "S03_Terms": "Phần 2 - Thuật ngữ", "S04_OneWayModel": "Phần 3 - Mục 6.4 One-way MANOVA",
        "S05_Example69": "Ví dụ 6.9", "S06_Example610": "Ví dụ 6.10", "S07_TwoWayUni": "Phần 4 - Mục 6.7 ANOVA hai nhân tố",
        "S08_TwoWayMulti": "Mục 6.7 MANOVA hai nhân tố", "S09_Example613": "Ví dụ 6.13", "S10_Summary": "Phần 5 - Tổng kết",
    }
    meta = [";FFMETADATA1"]
    for i, (start, scene) in enumerate(chapters):
        end = chapters[i + 1][0] if i + 1 < len(chapters) else offset
        meta += ["[CHAPTER]", "TIMEBASE=1/1000", f"START={int(start * 1000)}", f"END={int(end * 1000)}", f"title={titles[scene]}"]
    meta_path = ROOT / "chapters.txt"
    meta_path.write_text("\n".join(meta) + "\n", encoding="utf-8")

    # bản có phụ đề bật/tắt được (soft subtitle) + chương
    final = out.with_suffix(".mp4")
    subprocess.run([FFMPEG, "-v", "error", "-y", "-i", str(joined), "-i", str(srt_path), "-i", str(meta_path),
                    "-map", "0", "-map", "1", "-map_metadata", "2", "-map_chapters", "2",
                    "-c", "copy", "-c:s", "mov_text", "-metadata:s:s:0", "language=vie", str(final)], check=True)
    # bản phụ đề in cứng (xem được trên mọi trình phát)
    burned = out.parent / (out.name + "_phude.mp4")
    style = "FontName=Noto Sans,FontSize=15,PrimaryColour=&H00FFFFFF,OutlineColour=&H80000000,BorderStyle=3,Outline=1,Shadow=0,MarginV=6"
    subprocess.run([FFMPEG, "-v", "error", "-y", "-i", str(final), "-map", "0:v", "-map", "0:a", "-map_chapters", "0",
                    "-vf", f"subtitles={srt_path}:force_style='{style}'", "-c:v", "libx264", "-crf", "20",
                    "-preset", "medium", "-c:a", "copy", str(burned)], check=True)
    joined.unlink()
    print(f"Xong: {final}\n      {burned}\n      {srt_path}\nTổng thời lượng: {offset / 60:.1f} phút")


if __name__ == "__main__":
    main()
