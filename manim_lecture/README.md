# Bài giảng video: MANOVA một nhân tố (mục 6.4) và hai nhân tố (mục 6.7)

Nguồn: Johnson & Wichern, *Applied Multivariate Statistical Analysis*, 6th ed., Chương 6.

## Nội dung video
| Phần | Scene | Nội dung (trang sách) |
|---|---|---|
| Mở đầu | `S00_Intro` | Lộ trình, vì sao cần MANOVA |
| 1 | `S01_AnovaModel`, `S02_AnovaExample` | Tổng quan ANOVA (tr. 297–301), Ví dụ 6.7, 6.8 |
| 2 | `S03_Terms` | Thuật ngữ: nhân tố, mức, hiệu ứng, SS, SSP, B, W, Wilks' lambda, tương tác |
| 3 | `S04_OneWayModel`, `S05_Example69`, `S06_Example610` | Mục 6.4 (tr. 296–308), Bảng 6.3, Bartlett, Ví dụ 6.9, 6.10 |
| 4 | `S07_TwoWayUni`, `S08_TwoWayMulti`, `S09_Example613` | Mục 6.7 (tr. 312–323), Hình 6.3, Ví dụ 6.13 |
| 5 | `S10_Summary` | So sánh mô hình, quy trình 6 bước, gợi ý thuyết trình, code Python |

## Kết quả
- `../BaiGiang_MANOVA_6.4_6.7.mp4` — video 1080p, có phụ đề bật/tắt được và chia chương.
- `../BaiGiang_MANOVA_6.4_6.7_phude.mp4` — cùng video, phụ đề in cứng (xem được ở mọi trình phát).
- `../BaiGiang_MANOVA_6.4_6.7.srt` — phụ đề tiếng Việt riêng.
- `thuc_hanh_manova.py` + `plastic_film.csv` — tính lại Ví dụ 6.9 và 6.13 (numpy + statsmodels).

## Dựng lại video
Môi trường đã cài: `../.menv` (micromamba, manim 0.20 + edge-tts), LaTeX ở `~/.TinyTeX`.

```bash
cd manim_lecture
../.menv/bin/python build_video.py              # 1080p60, ~ nhiều phút
../.menv/bin/python build_video.py --quality l  # bản nháp 480p
../.menv/bin/python thuc_hanh_manova.py         # chạy phần thực hành
```

Giọng đọc: `vi-VN-NamMinhNeural` (Microsoft Edge TTS, cần Internet lần đầu; đã lưu cache ở `voice_cache/`).
Đổi sang giọng nữ: `LECTURE_VOICE=vi-VN-HoaiMyNeural ../.menv/bin/python build_video.py`.
Lời giảng nằm trong các khối `with self.say("...")` của từng file `partN_*.py` — sửa lời ở đó rồi dựng lại.
