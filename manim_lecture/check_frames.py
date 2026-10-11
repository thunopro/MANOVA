"""Trích khung hình cuối mỗi đoạn lời giảng và ghép thành ảnh lưới để soát bố cục."""
import json, subprocess, sys
from pathlib import Path
mod, scene, q = sys.argv[1], sys.argv[2], (sys.argv[3] if len(sys.argv) > 3 else "480p15")
vid = Path(f"media/videos/{mod}/{q}/{scene}.mp4")
subs = json.load(open(f"subs/{scene}.json"))["subs"]
out = Path("/tmp/claude-1000/-home-luongminhthu-Downloads-thecuong/5559e404-7429-4bf8-bdd1-8a7e8bb860a5/scratchpad/frames") / scene
out.mkdir(parents=True, exist_ok=True)
for f in out.glob("*.png"): f.unlink()
for i, s in enumerate(subs):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{s['end']:.2f}", "-i", str(vid), "-frames:v", "1",
                    "-vf", "scale=640:-1", str(out / f"f{i:03d}.png")])
files = sorted(out.glob("f*.png"))
for k in range(0, len(files), 6):
    chunk = files[k:k + 6]
    args = ["ffmpeg", "-v", "error", "-y"]
    for f in chunk: args += ["-i", str(f)]
    n = len(chunk)
    layout = "|".join(f"{(i % 2) * 640}_{(i // 2) * 360}" for i in range(n))
    args += ["-filter_complex", "".join(f"[{i}:v]" for i in range(n)) + f"xstack=inputs={n}:layout={layout}:fill=black" if n > 1 else "null",
             str(out / f"sheet{k // 6}.png")]
    subprocess.run(args)
print(out, len(files))
