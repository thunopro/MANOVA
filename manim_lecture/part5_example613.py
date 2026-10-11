"""Phần 5: Ví dụ 6.13 (màng nhựa, tr. 318-323) và tổng kết."""
from common import *
from part4_twoway import interaction_axes

DATA = {  # (nhân tố 1, nhân tố 2) -> 5 vectơ (x1, x2, x3), Bảng 6.4
    (0, 0): [(6.5, 9.5, 4.4), (6.2, 9.9, 6.4), (5.8, 9.6, 3.0), (6.5, 9.6, 4.1), (6.5, 9.2, 0.8)],
    (0, 1): [(6.9, 9.1, 5.7), (7.2, 10.0, 2.0), (6.9, 9.9, 3.9), (6.1, 9.5, 1.9), (6.3, 9.4, 5.7)],
    (1, 0): [(6.7, 9.1, 2.8), (6.6, 9.3, 4.1), (7.2, 8.3, 3.8), (7.1, 8.4, 1.6), (6.8, 8.5, 3.4)],
    (1, 1): [(7.1, 9.2, 8.4), (7.0, 8.8, 5.2), (7.2, 9.7, 6.9), (7.5, 10.1, 2.7), (7.6, 9.2, 1.9)],
}


def sym3(rows, color=FG, size=34):
    a, b, c, d, e, f = rows
    return mt(rf"\begin{{bmatrix}}{a}&{b}&{c}\\&{d}&{e}\\&&{f}\end{{bmatrix}}", size=size, color=color)


class S09_Example613(Lecture):
    section_label = "Phần 4 · Ví dụ 6.13"

    def construct(self):
        self.set_title("Ví dụ 6.13 — MANOVA hai nhân tố cho dữ liệu màng nhựa", "Example 6.13, tr. 318–323")
        ctx = bullet_list([
            vt("Tìm điều kiện tối ưu để đùn (ép) màng nhựa — kỹ thuật Evolutionary Operation", size=25),
            mix("3 biến phản hồi:", "$X_1$", "= độ bền xé,", "$X_2$", "= độ bóng,", "$X_3$", "= độ mờ", size=25, color=ACCENT),
            vt("Nhân tố 1: thay đổi tốc độ đùn — Thấp (−10%), Cao (10%)  ⇒ g = 2", size=25, color=GOLD),
            vt("Nhân tố 2: lượng chất phụ gia — Thấp (1.0%), Cao (1.5%)  ⇒ b = 2", size=25, color=PURPLE),
            vt("Lặp n = 5 lần ở mỗi tổ hợp  ⇒  gbn = 20 quan sát, p = 3", size=25),
        ], gap=0.35)
        self.fit(ctx, top_buff=0.6)
        with self.say("Bây giờ là ví dụ quan trọng nhất của mục 6.7: ví dụ 6.13. Người ta khảo sát điều kiện tối ưu để đùn màng nhựa, "
                      "bằng một kỹ thuật gọi là Evolutionary Operation."):
            self.play(FadeIn(ctx[0]))
        with self.say("Có ba biến phản hồi được đo: X một là độ bền xé, X hai là độ bóng, và X ba là độ mờ."):
            self.play(FadeIn(ctx[1]))
        with self.say("Chúng được đo ở hai mức của hai nhân tố. Nhân tố một là tốc độ đùn, mức thấp và mức cao. Nhân tố hai là lượng chất phụ gia, "
                      "mức thấp một phần trăm và mức cao một phẩy năm phần trăm. Phép đo được lặp năm lần ở mỗi tổ hợp, nên có hai mươi quan sát."):
            self.play(FadeIn(ctx[2]))
            self.play(FadeIn(ctx[3]))
            self.play(FadeIn(ctx[4]))
        self.clear_content()

        self.set_title("Bảng 6.4 — Dữ liệu màng nhựa", "x₁ = độ bền xé, x₂ = độ bóng, x₃ = độ mờ")
        def cell(key):
            rows = r"\\".join(rf"{a}&{b}&{c}" for a, b, c in DATA[key])
            return mt(rf"\begin{{matrix}}x_1&x_2&x_3\\ \hline {rows}\end{{matrix}}", size=26)
        cells = {k: cell(k) for k in DATA}
        c00, c01, c10, c11 = cells[(0, 0)], cells[(0, 1)], cells[(1, 0)], cells[(1, 1)]
        top = VGroup(c00, c01).arrange(RIGHT, buff=1.0)
        bot = VGroup(c10, c11).arrange(RIGHT, buff=1.0)
        body = VGroup(top, bot).arrange(DOWN, buff=0.5)
        h1 = vt("Phụ gia thấp (1.0%)", size=22, color=PURPLE).next_to(c00, UP, buff=0.25)
        h2 = vt("Phụ gia cao (1.5%)", size=22, color=PURPLE).next_to(c01, UP, buff=0.25)
        r1 = vt("Tốc độ đùn\nthấp (−10%)", size=22, color=GOLD).next_to(c00, LEFT, buff=0.5)
        r2 = vt("Tốc độ đùn\ncao (10%)", size=22, color=GOLD).next_to(c10, LEFT, buff=0.5)
        frame = VGroup(*[SurroundingRectangle(c, color=MUTED, buff=0.15, stroke_width=1.5) for c in (c00, c01, c10, c11)])
        tbl = VGroup(body, h1, h2, r1, r2, frame)
        self.fit(tbl, top_buff=0.3, grow=1.5)
        with self.say("Đây là bảng 6.4. Mỗi ô ứng với một tổ hợp mức, chứa năm vectơ quan sát gồm ba thành phần."):
            self.play(FadeIn(h1), FadeIn(h2), FadeIn(r1), FadeIn(r2), Create(frame))
            self.play(LaggedStart(*[FadeIn(c) for c in (c00, c01, c10, c11)], lag_ratio=0.3), run_time=2.5)
        with self.say("Ví dụ, ô góc trên bên trái là tốc độ đùn thấp và phụ gia thấp. Quan sát đầu tiên có độ bền xé sáu phẩy năm, "
                      "độ bóng chín phẩy năm và độ mờ bốn phẩy bốn."):
            self.play(Indicate(c00, color=ACCENT, scale_factor=1.05))
        self.clear_content()

        self.set_title("Bảng MANOVA của Ví dụ 6.13", "tính bằng SAS PROC GLM (Panel 6.1), tr. 319")
        t = table([
            ["Nguồn biến thiên", "Ma trận SSP", "d.f."],
            ["Nhân tố 1: tốc độ đùn", sym3(["1.7405", "-1.5045", ".8555", "1.3005", "-.7395", ".4205"], GOLD), mt("1", size=28)],
            ["Nhân tố 2: phụ gia", sym3([".7605", ".6825", "1.9305", ".6125", "1.7325", "4.9005"], PURPLE), mt("1", size=28)],
            ["Tương tác", sym3([".0005", ".0165", ".0445", ".5445", "1.4685", "3.9605"], RED), mt("1", size=28)],
            ["Phần dư", sym3(["1.7640", ".0200", "-3.0700", "2.6280", "-.5520", "64.9240"], GREEN), mt("16", size=28)],
            ["Toàn phần (h.c.)", sym3(["4.2655", "-.7855", "-.2395", "5.0855", "1.9095", "74.2055"]), mt("19", size=28)],
        ], [4.0, 5.2, 1.4], row_h=1.0, size=22)
        self.fit(t, top_buff=0.25)
        with self.say("Các ma trận tổng bình phương và tích chéo được tính bằng phần mềm Sát, cho ta bảng ma-nô-va này. "
                      "Chỉ in nửa trên vì các ma trận đối xứng."):
            self.play(Create(t.lines), FadeIn(t.rows[0]))
            self.play(LaggedStart(*[FadeIn(r) for r in t.rows[1:]], lag_ratio=0.3), run_time=3)
        with self.say("Bậc tự do: nhân tố một có gờ trừ một bằng một. Nhân tố hai có bê trừ một bằng một. Tương tác có một nhân một bằng một. "
                      "Phần dư có gờ bê nhân en trừ một, bằng hai nhân hai nhân bốn, bằng mười sáu. Và toàn phần là mười chín."):
            self.play(Indicate(VGroup(*[r[2] for r in t.rows[1:]]), color=GOLD))
        with self.say("Các em nên tự kiểm tra: cộng bốn ma trận nhân tố một, nhân tố hai, tương tác và phần dư, ta được đúng ma trận toàn phần. "
                      "Ví dụ phần tử đầu tiên: một phẩy bảy bốn không năm, cộng không phẩy bảy sáu không năm, cộng không phẩy không không không năm, "
                      "cộng một phẩy bảy sáu bốn, bằng bốn phẩy hai sáu năm năm."):
            self.play(FadeIn(row_highlight(t, 5, color=ACCENT)))
        self.clear_content()

        self.set_title("Bước 1 — Kiểm định tương tác", "tr. 321–322")
        lam = mt(r"\Lambda^*=\frac{|\mathbf{SSP}_{res}|}{|\mathbf{SSP}_{int}+\mathbf{SSP}_{res}|}=\frac{275.7098}{354.7906}=0.7771", size=42)
        F = mt(r"F=\left(\frac{1-\Lambda^*}{\Lambda^*}\right)\frac{(gb(n-1)-p+1)/2}{(|(g-1)(b-1)-p|+1)/2}"
               r"=\left(\frac{1-.7771}{.7771}\right)\frac{(2(2)(4)-3+1)/2}{(|1(1)-3|+1)/2}=1.34", size=34)
        dfs = mix("Khi (g − 1)(b − 1) = 1: F có phân phối F chính xác với", r"$\nu_1=|(g-1)(b-1)-p|+1=3$", ",",
                  r"$\nu_2=gb(n-1)-p+1=14$", size=22, color=MUTED)
        cmp = mt(r"F=1.34<F_{3,14}(0.05)=3.34", size=40, color=GOLD)
        chi = mix("Xấp xỉ χ² (6-65):", r"$-\left[2(2)(4)-(3+1-1(1))/2\right]\ln(.7771)=3.66<\chi^2_3(.05)=7.81$", size=24, color=ACCENT)
        concl = boxed(mix("⇒ KHÔNG bác bỏ", r"$H_0:\boldsymbol\gamma_{11}=\boldsymbol\gamma_{12}=\boldsymbol\gamma_{21}=\boldsymbol\gamma_{22}=\mathbf 0$",
                          ": không có hiệu ứng tương tác", size=24, color=GOLD), color=GOLD)
        grp = VGroup(lam, F, dfs, cmp, chi, concl).arrange(DOWN, buff=0.33)
        self.fit(grp, top_buff=0.35)
        with self.say("Đúng theo quy trình, ta kiểm định tương tác trước. Lam-đa sao bằng định thức S S P phần dư là hai trăm bảy mươi lăm phẩy bảy không chín tám, "
                      "chia định thức của S S P tương tác cộng S S P phần dư là ba trăm năm mươi tư phẩy bảy chín không sáu. Ta được không phẩy bảy bảy bảy một."):
            self.play(Write(lam), run_time=2.5)
        with self.say("Vì gờ trừ một nhân bê trừ một bằng một, sách dùng một phép biến đổi có phân phối ép chính xác. Thay số, ta được ép bằng một phẩy ba tư, "
                      "với nuy một bằng ba và nuy hai bằng mười bốn bậc tự do."):
            self.play(Write(F), run_time=3)
            self.play(FadeIn(dfs))
        with self.say("Phân vị năm phần trăm của ép ba, mười bốn là ba phẩy ba tư. Vì một phẩy ba tư nhỏ hơn ba phẩy ba tư, ta không bác bỏ giả thuyết không. "
                      "Kiểm định khi bình phương xấp xỉ cho ba phẩy sáu sáu, nhỏ hơn bảy phẩy tám mốt, cũng đi đến cùng kết luận: không có hiệu ứng tương tác."):
            self.play(Write(cmp))
            self.play(FadeIn(chi))
            self.play(FadeIn(concl, shift=UP * 0.2))
        self.clear_content()

        self.set_title("Bước 2 — Kiểm định hiệu ứng chính", "tr. 322–323")
        l1 = mt(r"\Lambda_1^*=\frac{|\mathbf{SSP}_{res}|}{|\mathbf{SSP}_{fac1}+\mathbf{SSP}_{res}|}=\frac{275.7098}{722.0212}=0.3819", size=36, color=GOLD)
        l2 = mt(r"\Lambda_2^*=\frac{|\mathbf{SSP}_{res}|}{|\mathbf{SSP}_{fac2}+\mathbf{SSP}_{res}|}=\frac{275.7098}{527.1347}=0.5230", size=36, color=PURPLE)
        Fgen = mt(r"F_1=\left(\frac{1-\Lambda_1^*}{\Lambda_1^*}\right)\frac{(gb(n-1)-p+1)/2}{(|(g-1)-p|+1)/2},\qquad"
                  r"\nu_1=|(g-1)-p|+1,\ \ \nu_2=gb(n-1)-p+1", size=28, color=MUTED)
        F1 = mt(r"F_1=\left(\frac{1-.3819}{.3819}\right)\frac{(16-3+1)/2}{(|1-3|+1)/2}=7.55", size=34, color=GOLD)
        F2 = mt(r"F_2=\left(\frac{1-.5230}{.5230}\right)\frac{(16-3+1)/2}{(|1-3|+1)/2}=4.26", size=34, color=PURPLE)
        dfs = mt(r"\nu_1=|1-3|+1=3,\qquad \nu_2=16-3+1=14,\qquad F_{3,14}(0.05)=3.34", size=30)
        grp = VGroup(l1, l2, Fgen, F1, F2, dfs).arrange(DOWN, buff=0.33)
        self.fit(grp, top_buff=0.35)
        with self.say("Không có tương tác, nên ta kiểm định các hiệu ứng chính. Với nhân tố một, lam-đa một sao bằng hai trăm bảy mươi lăm phẩy bảy không chín tám "
                      "chia bảy trăm hai mươi hai phẩy không hai một hai, bằng không phẩy ba tám một chín."):
            self.play(Write(l1), run_time=2)
        with self.say("Với nhân tố hai, lam-đa hai sao bằng hai trăm bảy mươi lăm phẩy bảy không chín tám chia năm trăm hai mươi bảy phẩy một ba bốn bảy, "
                      "bằng không phẩy năm hai ba không."):
            self.play(Write(l2), run_time=2)
        with self.say("Vì cả gờ trừ một và bê trừ một đều bằng một, các thống kê ép một và ép hai có phân phối ép chính xác, với nuy một bằng ba và nuy hai bằng mười bốn."):
            self.play(FadeIn(Fgen))
        with self.say("Thay số: ép một bằng bảy phẩy năm lăm, ép hai bằng bốn phẩy hai sáu. Cả hai đều so với phân vị năm phần trăm là ba phẩy ba tư."):
            self.play(Write(F1), run_time=1.5)
            self.play(Write(F2), run_time=1.5)
            self.play(FadeIn(dfs))
        self.clear_content()

        self.set_title("Kết luận Ví dụ 6.13")
        t = table([
            ["Hiệu ứng", "Wilks' Λ*", "F", "So với F₃,₁₄(0.05) = 3.34", "Kết luận"],
            [vt("Tương tác", size=24, color=RED), mt(".7771", size=30), mt("1.34", size=30), mt("1.34<3.34", size=30), vt("Không bác bỏ H₀", size=22)],
            [vt("Nhân tố 1: tốc độ đùn", size=24, color=GOLD), mt(".3819", size=30), mt("7.55", size=30), mt("7.55>3.34", size=30), vt("Bác bỏ H₀ — có hiệu ứng", size=22, color=GOLD)],
            [vt("Nhân tố 2: phụ gia", size=24, color=PURPLE), mt(".5230", size=30), mt("4.26", size=30), mt("4.26>3.34", size=30), vt("Bác bỏ H₀ — có hiệu ứng", size=22, color=PURPLE)],
        ], [3.6, 1.8, 1.4, 3.2, 3.4], row_h=0.8, size=21)
        pv = vt("Giá trị p (SAS, Panel 6.1): tương tác 0.3018 · nhân tố 1 0.0030 · nhân tố 2 0.0247", size=22, color=MUTED)
        concl = boxed(vt("Cả tốc độ đùn và lượng phụ gia đều ảnh hưởng đến các phản hồi,\nvà chúng tác động theo cách CỘNG DỒN (không có tương tác).",
                         size=26, color=GOLD, align=ORIGIN), color=GOLD)
        grp = VGroup(t, pv, concl).arrange(DOWN, buff=0.5)
        self.fit(grp, top_buff=0.45)
        with self.say("Tổng hợp lại. Tương tác: lam-đa không phẩy bảy bảy bảy một, ép một phẩy ba tư, không có ý nghĩa. Nhân tố một: ép bảy phẩy năm lăm, "
                      "lớn hơn ba phẩy ba tư, ta bác bỏ, có hiệu ứng của tốc độ đùn. Nhân tố hai: ép bốn phẩy hai sáu, lớn hơn ba phẩy ba tư, "
                      "ta bác bỏ, có hiệu ứng của lượng phụ gia."):
            self.play(Create(t.lines), FadeIn(t.rows[0]))
            self.play(LaggedStart(*[FadeIn(r) for r in t.rows[1:]], lag_ratio=0.5), run_time=3)
        with self.say("Kết quả này khớp với bảng in của Sát, với giá trị pê lần lượt là không phẩy ba không một tám, không phẩy không không ba, "
                      "và không phẩy không hai bốn bảy."):
            self.play(FadeIn(pv))
        with self.say("Kết luận của sách: cả tốc độ đùn và lượng phụ gia đều ảnh hưởng đến các phản hồi, và chúng tác động theo cách cộng dồn. "
                      "Bản chất của các hiệu ứng này được khảo sát thêm ở bài tập 6.15, bằng khoảng tin cậy đồng thời cho các tương phản."):
            self.play(FadeIn(concl, shift=UP * 0.2))
        self.clear_content()

        self.set_title("Nhìn sâu hơn: kết quả từng biến (SAS, Panel 6.1)", "ANOVA hai nhân tố cho từng biến — giá trị p")
        t = table([
            ["Biến", "Nhân tố 1", "Nhân tố 2", "Tương tác"],
            [vt("X₁ — độ bền xé", size=24), vt("0.0011", size=24, color=GOLD), vt("0.0183", size=24, color=PURPLE), vt("0.9471", size=24)],
            [vt("X₂ — độ bóng", size=24), vt("0.0125", size=24, color=GOLD), vt("0.0714", size=24), vt("0.0874", size=24)],
            [vt("X₃ — độ mờ", size=24), vt("0.7517", size=24), vt("0.2881", size=24), vt("0.3379", size=24)],
        ], [3.8, 2.6, 2.6, 2.6], row_h=0.75, size=24)
        mean_t = table([
            ["Trung bình", "x̄₁", "x̄₂", "x̄₃"],
            [vt("Tốc độ đùn thấp / cao", size=22, color=GOLD), mt("6.49\\ /\\ 7.08", size=28), mt("9.57\\ /\\ 9.06", size=28), mt("3.79\\ /\\ 4.08", size=28)],
            [vt("Phụ gia thấp / cao", size=22, color=PURPLE), mt("6.59\\ /\\ 6.98", size=28), mt("9.14\\ /\\ 9.49", size=28), mt("3.44\\ /\\ 4.43", size=28)],
        ], [3.8, 2.6, 2.6, 2.6], row_h=0.7, size=24)
        grp = VGroup(t, mean_t).arrange(DOWN, buff=0.5)
        self.fit(grp, top_buff=0.35)
        with self.say("Bảng in của Sát trong panel 6.1 còn cho kết quả a-nô-va hai nhân tố cho từng biến. Đây là thông tin rất hữu ích khi thuyết trình. "
                      "Với độ bền xé X một, cả hai nhân tố đều có ý nghĩa. Với độ bóng X hai, nhân tố một có ý nghĩa ở mức năm phần trăm. "
                      "Còn với độ mờ X ba, không nhân tố nào có ý nghĩa, do phương sai phần dư của X ba rất lớn."):
            self.play(Create(t.lines), FadeIn(t.rows))
        with self.say("Các trung bình theo mức cho thấy chiều hướng: tăng tốc độ đùn làm tăng độ bền xé, từ sáu phẩy bốn chín lên bảy phẩy không tám, "
                      "nhưng làm giảm độ bóng. Tăng phụ gia làm tăng cả độ bền xé lẫn độ bóng."):
            self.play(Create(mean_t.lines), FadeIn(mean_t.rows))
        self.clear_content()

        self.set_title("Đồ thị tương tác từ trung bình mẫu", "vẽ từ trung bình các ô của Bảng 6.4 — gợi ý của sách, tr. 317")
        cellm = {"x1": [[6.30, 6.68], [6.88, 7.28]], "x2": [[9.56, 9.58], [8.72, 9.40]], "x3": [[3.74, 3.84], [3.14, 5.02]]}
        plots = VGroup()
        titles = {"x1": "x₁ — độ bền xé", "x2": "x₂ — độ bóng", "x3": "x₃ — độ mờ"}
        ranges = {"x1": (6.0, 7.5), "x2": (8.5, 10.0), "x3": (2.5, 5.5)}
        for key in ("x1", "x2", "x3"):
            lo, hi = ranges[key]
            ax = Axes(x_range=[0.5, 2.5, 1], y_range=[lo, hi, (hi - lo) / 3], x_length=3.4, y_length=2.8,
                      axis_config={"color": MUTED, "include_tip": False, "font_size": 18},
                      y_axis_config={"numbers_to_include": [lo, hi], "decimal_number_config": {"num_decimal_places": 1}})
            xl = VGroup(vt("thấp", size=16, color=PURPLE).next_to(ax.c2p(1, lo), DOWN, buff=0.15),
                        vt("cao", size=16, color=PURPLE).next_to(ax.c2p(2, lo), DOWN, buff=0.15))
            lines = VGroup()
            for l, c in [(0, GOLD), (1, RED)]:
                pts = [ax.c2p(k + 1, cellm[key][l][k]) for k in range(2)]
                lines.add(VGroup(Line(pts[0], pts[1], color=c, stroke_width=4), *[Dot(p, color=c, radius=0.06) for p in pts]))
            tt = vt(titles[key], size=20, weight=BOLD).next_to(ax, UP, buff=0.2)
            plots.add(VGroup(VGroup(ax, xl, tt), lines))
        plots.arrange(RIGHT, buff=0.8)
        leg = VGroup(
            VGroup(Line(ORIGIN, RIGHT * 0.5, color=GOLD, stroke_width=4), vt("Tốc độ đùn thấp", size=20, color=GOLD)).arrange(RIGHT, buff=0.15),
            VGroup(Line(ORIGIN, RIGHT * 0.5, color=RED, stroke_width=4), vt("Tốc độ đùn cao", size=20, color=RED)).arrange(RIGHT, buff=0.15),
            vt("Trục ngang: lượng phụ gia", size=20, color=PURPLE),
        ).arrange(RIGHT, buff=0.7)
        note = vt("x₁: hai đường gần song song ⇒ gần như không có tương tác (p = 0.947).\n"
                  "x₂, x₃: các đường lệch nhau, nhưng dao động phần dư lớn nên tương tác không có ý nghĩa (p = 0.087; 0.338).",
                  size=21, color=MUTED, align=ORIGIN)
        grp = VGroup(plots, leg, note).arrange(DOWN, buff=0.45)
        self.fit(grp, top_buff=0.45, grow=1.4)
        with self.say("Cuối cùng, theo gợi ý của sách, ta vẽ đồ thị tương tác giống hình 6.3, nhưng dùng trung bình mẫu của từng ô thay cho giá trị kỳ vọng. "
                      "Trục ngang là lượng phụ gia, mỗi đường là một mức tốc độ đùn."):
            self.play(FadeIn(VGroup(*[p[0] for p in plots])), FadeIn(leg))
            self.play(LaggedStart(*[Create(p[1]) for p in plots], lag_ratio=0.3), run_time=3)
        with self.say("Với độ bền xé, hai đường gần như song song: không có tương tác, khớp với tổng bình phương tương tác gần bằng không. "
                      "Với độ bóng và độ mờ, các đường có lệch nhau, nhưng dao động phần dư, đặc biệt của độ mờ, rất lớn, nên tương tác không có ý nghĩa thống kê."):
            self.play(FadeIn(note))
        self.clear_all()


class S10_Summary(Lecture):
    section_label = "Phần 5 · Tổng kết"

    def construct(self):
        card = self.section_card("PHẦN 5", "Tổng kết, quy trình thực hành và thuyết trình")
        with self.say("Phần năm. Ta tổng kết lại toàn bộ bài, và rút ra quy trình để các em tự thực hành và thuyết trình."):
            self.play(FadeIn(card, shift=UP * 0.3))
        self.play(FadeOut(card))

        self.set_title("So sánh ba mô hình")
        t = table([
            ["", "ANOVA một nhân tố", "MANOVA một nhân tố (6.4)", "MANOVA hai nhân tố (6.7)"],
            [vt("Quan sát", size=22, color=MUTED), mt(r"x_{\ell j}", size=30), mt(r"\mathbf x_{\ell j}\ (p\times1)", size=30), mt(r"\mathbf x_{\ell kr}\ (p\times1)", size=30)],
            [vt("Mô hình", size=22, color=MUTED), mt(r"\mu+\tau_\ell+e", size=28), mt(r"\boldsymbol\mu+\boldsymbol\tau_\ell+\mathbf e", size=28), mt(r"\boldsymbol\mu+\boldsymbol\tau_\ell+\boldsymbol\beta_k+\boldsymbol\gamma_{\ell k}+\mathbf e", size=28)],
            [vt("Phân tích", size=22, color=MUTED), mt(r"SS_{tr}+SS_{res}", size=28), mt(r"\mathbf B+\mathbf W", size=28), mt(r"\mathbf{SSP}_{fac1}+\mathbf{SSP}_{fac2}+\mathbf{SSP}_{int}+\mathbf{SSP}_{res}", size=24)],
            [vt("Thống kê", size=22, color=MUTED), mt(r"F", size=30), mt(r"\Lambda^*=\frac{|\mathbf W|}{|\mathbf B+\mathbf W|}", size=28), mt(r"\Lambda^*=\frac{|\mathbf{SSP}_{res}|}{|\mathbf{SSP}_{H}+\mathbf{SSP}_{res}|}", size=28)],
            [vt("Phân phối", size=22, color=MUTED), mt(r"F", size=28), vt("Bảng 6.3 / Bartlett χ²", size=20), vt("F chính xác / Bartlett χ²", size=20)],
        ], [2.0, 3.0, 3.6, 5.2], row_h=1.0, size=22)
        self.fit(t, top_buff=0.4)
        with self.say("Bảng này so sánh ba mô hình. Từ a-nô-va sang ma-nô-va, quan sát trở thành vectơ, tổng bình phương trở thành ma trận tổng bình phương và tích chéo, "
                      "và tỉ số ép được thay bằng lam-đa Uyn-xơ, là tỉ số của hai định thức. Với hai nhân tố, ta có thêm nhân tố thứ hai và số hạng tương tác. "
                      "Trong công thức lam-đa, S S P H là ma trận của hiệu ứng cần kiểm định: nhân tố một, nhân tố hai, hoặc tương tác."):
            self.play(Create(t.lines), FadeIn(t.rows[0]))
            self.play(LaggedStart(*[FadeIn(r) for r in t.rows[1:]], lag_ratio=0.3), run_time=4)
        self.clear_content()

        self.set_title("Quy trình làm bài MANOVA hai nhân tố")
        steps = [
            ("1", "Mô tả bài toán", "biến phản hồi (p), nhân tố & số mức (g, b), số lần lặp n; kiểm tra p ≤ gb(n − 1)"),
            ("2", "Tính các trung bình", "x̄, x̄ℓ· (hàng), x̄·k (cột), x̄ℓk (ô)"),
            ("3", "Lập bảng MANOVA", "SSP nhân tố 1, nhân tố 2, tương tác, phần dư; kiểm tra tổng = SSP toàn phần"),
            ("4", "Kiểm định TƯƠNG TÁC trước", "Λ* = |SSP_res| / |SSP_int + SSP_res|; F chính xác hoặc Bartlett χ²"),
            ("5", "Nếu không có tương tác", "kiểm định nhân tố 1 và 2; nếu có: ANOVA từng biến + đồ thị tương tác"),
            ("6", "Diễn giải & kiểm tra giả định", "khoảng tin cậy Bonferroni, phần dư: chuẩn, ngoại lai, Σ bằng nhau"),
        ]
        rows = VGroup()
        for n, a, b in steps:
            circ = Circle(radius=0.27, color=ACCENT, fill_color=PANEL, fill_opacity=1)
            num = vt(n, size=24, color=ACCENT, weight=BOLD).move_to(circ)
            txt = VGroup(vt(a, size=25, weight=BOLD), vt(b.replace("SSP_res", "SSPres").replace("SSP_int", "SSPint"), size=19, color=MUTED)).arrange(DOWN, aligned_edge=LEFT, buff=0.06)
            rows.add(VGroup(VGroup(circ, num), txt).arrange(RIGHT, buff=0.3))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        self.fit(rows, top_buff=0.4, grow=1.15)
        with self.say("Đây là quy trình sáu bước để làm một bài ma-nô-va hai nhân tố. Bước một: mô tả bài toán, xác định số biến pê, số mức gờ và bê, số lần lặp en, "
                      "và kiểm tra pê không vượt quá gờ bê nhân en trừ một. Bước hai: tính các vectơ trung bình chung, trung bình hàng, trung bình cột và trung bình ô."):
            self.play(FadeIn(rows[0], shift=RIGHT * 0.2))
            self.play(FadeIn(rows[1], shift=RIGHT * 0.2))
        with self.say("Bước ba: lập bảng ma-nô-va và kiểm tra tổng các ma trận bằng ma trận toàn phần. Bước bốn: luôn kiểm định tương tác trước, "
                      "bằng lam-đa Uyn-xơ, với phân phối ép chính xác hoặc xấp xỉ khi bình phương của Bác-lét."):
            self.play(FadeIn(rows[2], shift=RIGHT * 0.2))
            self.play(FadeIn(rows[3], shift=RIGHT * 0.2))
        with self.say("Bước năm: nếu không có tương tác, kiểm định hiệu ứng chính của từng nhân tố. Nếu có tương tác, làm a-nô-va cho từng biến và vẽ đồ thị tương tác. "
                      "Bước sáu: diễn giải bằng khoảng tin cậy Bôn-phe-rô-ni, và kiểm tra các giả định qua phần dư."):
            self.play(FadeIn(rows[4], shift=RIGHT * 0.2))
            self.play(FadeIn(rows[5], shift=RIGHT * 0.2))
        self.clear_content()

        self.set_title("Gợi ý khi thuyết trình lại", "những ý cần nói được bằng lời của mình")
        tips = bullet_list([
            vt("MANOVA = ANOVA cho vectơ: bình phương → tích ngoài (x̄ℓ − x̄)(x̄ℓ − x̄)′, số → ma trận SSP", size=24),
            vt("Wilks' lambda là tỉ số phương sai tổng quát; Λ* nhỏ ⇒ hiệu ứng lớn ⇒ bác bỏ H₀", size=24),
            vt("Tương tác = các đường không song song; phải kiểm định tương tác TRƯỚC hiệu ứng chính", size=24),
            vt("Trình bày ví dụ 6.9 bằng tay (p = 2) để chứng minh hiểu bản chất các ma trận B, W", size=24),
            vt("Trình bày ví dụ 6.13 theo thứ tự: dữ liệu → bảng MANOVA → tương tác → hiệu ứng chính → kết luận", size=24),
            vt("Kết luận phải gắn với ngữ cảnh: tốc độ đùn và phụ gia đều ảnh hưởng, tác động cộng dồn", size=24),
        ], gap=0.38)
        self.fit(tips, top_buff=0.5, grow=1.3)
        with self.say("Khi thuyết trình, các em nên nói được bằng lời của mình những ý sau. Ma-nô-va chính là a-nô-va cho vectơ. Lam-đa Uyn-xơ là tỉ số "
                      "các phương sai tổng quát, lam-đa nhỏ nghĩa là hiệu ứng lớn. Tương tác nghĩa là các đường không song song, và phải kiểm định nó trước."):
            self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.2) for r in tips[:3]], lag_ratio=0.4), run_time=3)
        with self.say("Hãy tự làm tay ví dụ 6.9 để hiểu bản chất các ma trận bê và đáp-bờ-liu. Trình bày ví dụ 6.13 theo đúng trình tự: dữ liệu, bảng ma-nô-va, "
                      "kiểm định tương tác, rồi hiệu ứng chính, và kết luận gắn với ngữ cảnh thực tế."):
            self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.2) for r in tips[3:]], lag_ratio=0.4), run_time=3)
        self.clear_content()

        self.set_title("Thực hành với Python", "file kèm theo: thuc_hanh_manova.py — kết quả trùng với SAS trong sách")
        code = Code(code_string=(
            "import pandas as pd\n"
            "from statsmodels.multivariate.manova import MANOVA\n\n"
            "df = pd.read_csv(\"plastic_film.csv\")   # cột: f1, f2, x1, x2, x3\n"
            "m = MANOVA.from_formula(\n"
            "    \"x1 + x2 + x3 ~ C(f1, Sum) * C(f2, Sum)\", data=df)\n"
            "print(m.mv_test())\n\n"
            "# Wilks' lambda:  f1 = 0.3819   f2 = 0.5230   f1:f2 = 0.7771\n"
            "# F (3, 14):      f1 = 7.55     f2 = 4.26     f1:f2 = 1.34"),
            language="python", formatter_style="monokai", background="rectangle",
            add_line_numbers=False, paragraph_config={"font": "DejaVu Sans Mono", "font_size": 22})
        self.fit(code, top_buff=0.6)
        with self.say("Để thực hành, đi kèm video là file Python tên thuc hanh manova. Nó tính lại ví dụ 6.9 bằng công thức, và ví dụ 6.13 bằng cả công thức lẫn "
                      "thư viện stats-models. Lệnh ma-nô-va from formula với công thức x một cộng x hai cộng x ba theo f một nhân f hai cho ra đúng các giá trị lam-đa "
                      "và ép như trong sách: không phẩy ba tám một chín, không phẩy năm hai ba không, và không phẩy bảy bảy bảy một."):
            self.play(FadeIn(code, shift=UP * 0.2), run_time=1.5)
        self.clear_all()

        end = VGroup(
            vt("Cảm ơn các em đã theo dõi!", size=50, weight=BOLD),
            vt("Tài liệu: Johnson & Wichern, Applied Multivariate Statistical Analysis, 6th ed.\nChương 6 — mục 6.4 và 6.7", size=24, color=MUTED, align=ORIGIN),
            vt("Bài tập gợi ý trong sách: 6.13, 6.15 (khoảng tin cậy cho Ví dụ 6.13)", size=22, color=ACCENT),
        ).arrange(DOWN, buff=0.45)
        with self.say("Bài giảng đến đây là kết thúc. Các em hãy làm thêm bài tập 6.13 và 6.15 trong sách để củng cố. Cảm ơn các em đã theo dõi, và chúc các em học tốt."):
            self.play(FadeIn(end, shift=UP * 0.3), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(end))
