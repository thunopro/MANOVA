"""Phần 4: Mục 6.7 — Two-way MANOVA (sách tr. 312-318)."""
from common import *


def interaction_axes(values, colors, names, title, width=5.6, height=3.2, y_range=(0, 6, 1)):
    ax = Axes(x_range=[0.5, 4.5, 1], y_range=list(y_range), x_length=width, y_length=height,
              axis_config={"color": MUTED, "include_ticks": True, "include_tip": True, "tip_length": 0.18},
              x_axis_config={"numbers_to_include": [1, 2, 3, 4], "font_size": 22},
              y_axis_config={"include_ticks": False})
    xl = vt("Mức của nhân tố 2", size=18, color=MUTED).next_to(ax.x_axis, DOWN, buff=0.45)
    yl = vt("Phản hồi kỳ vọng", size=18, color=MUTED).rotate(PI / 2).next_to(ax.y_axis, LEFT, buff=0.2)
    lines = VGroup()
    labels = VGroup()
    for vals, c, n in zip(values, colors, names):
        pts = [ax.c2p(i + 1, v) for i, v in enumerate(vals)]
        ln = VMobject(color=c, stroke_width=4).set_points_as_corners(pts)
        dots = VGroup(*[Dot(p, radius=0.06, color=c) for p in pts])
        lines.add(VGroup(ln, dots))
        labels.add(vt(n, size=17, color=c).next_to(pts[-1], RIGHT, buff=0.15))
    t = vt(title, size=22, color=FG, weight=BOLD).next_to(ax, UP, buff=0.2)
    return VGroup(ax, xl, yl, t), lines, labels


class S07_TwoWayUni(Lecture):
    section_label = "Phần 4 · Mục 6.7 Two-way MANOVA"

    def construct(self):
        card = self.section_card("PHẦN 4 · MỤC 6.7", "Phân tích phương sai đa biến hai nhân tố",
                                 "Two-Way Multivariate Analysis of Variance — tr. 312–323")
        with self.say("Phần bốn, nội dung chính của bài: mục 6.7, phân tích phương sai đa biến hai nhân tố. Giống như với ma-nô-va một nhân tố, "
                      "sách sẽ ôn nhanh mô hình hai nhân tố hiệu ứng cố định cho một biến, rồi tổng quát hoá sang nhiều biến bằng phép tương tự."):
            self.play(FadeIn(card, shift=UP * 0.3))
        self.play(FadeOut(card))

        self.set_title("Thiết kế hai nhân tố có lặp", "Univariate Two-Way Fixed-Effects Model with Interaction")
        g, b = 3, 4
        cw, ch = 1.7, 0.95
        cells = VGroup()
        for l in range(g):
            for k in range(b):
                r = Rectangle(width=cw, height=ch, stroke_color=MUTED, stroke_width=1.5, fill_color=PANEL, fill_opacity=1)
                r.move_to([k * cw, -l * ch, 0])
                dots = VGroup(*[Dot(radius=0.055, color=ACCENT) for _ in range(5)]).arrange(RIGHT, buff=0.1).move_to(r)
                cells.add(VGroup(r, dots))
        top = VGroup(*[vt(f"k = {k + 1}", size=20, color=PURPLE).next_to(cells[k], UP, buff=0.12) for k in range(b)])
        left = VGroup(*[vt(f"ℓ = {l + 1}", size=20, color=GOLD).next_to(cells[l * b], LEFT, buff=0.15) for l in range(g)])
        f2 = vt("Nhân tố 2: b mức", size=22, color=PURPLE, weight=BOLD).next_to(top, UP, buff=0.15)
        f1 = vt("Nhân tố 1: g mức", size=22, color=GOLD, weight=BOLD).rotate(PI / 2).next_to(left, LEFT, buff=0.2)
        grid = VGroup(cells, top, left, f1, f2)
        notes = bullet_list([
            vt("Nhân tố 1: g mức; nhân tố 2: b mức", size=24),
            vt("Mỗi ô (ℓ, k): n quan sát độc lập\n(n lần lặp)", size=24),
            vt("Tổng số quan sát: gbn", size=24),
            vt("Quan sát ở các ô khác nhau\nđộc lập với nhau", size=24),
        ], gap=0.35)
        lab = mt(r"X_{\ell k r}", size=36, color=RED)
        lab2 = vt("quan sát thứ r ở mức ℓ của nhân tố 1\nvà mức k của nhân tố 2", size=20, color=RED)
        lg = VGroup(lab, lab2).arrange(RIGHT, buff=0.3).next_to(cells, DOWN, buff=0.35)
        grp = VGroup(VGroup(grid, lg), notes).arrange(RIGHT, buff=0.7)
        self.fit(grp, top_buff=0.5, grow=1.4)
        with self.say("Giả sử các phép đo được ghi nhận ở các mức khác nhau của hai nhân tố. Nhân tố một có gờ mức, nhân tố hai có bê mức. "
                      "Sách không đi sâu vào thiết kế thí nghiệm, nhưng giả định các quan sát ở những tổ hợp điều kiện khác nhau là độc lập."):
            self.play(FadeIn(VGroup(*[c[0] for c in cells])), FadeIn(top), FadeIn(left), FadeIn(f1), FadeIn(f2))
            self.play(FadeIn(notes[0]))
        with self.say("Ở mỗi tổ hợp trong gờ nhân bê tổ hợp mức, ta quan sát en lần độc lập. Đó là các lần lặp. "
                      "Tổng cộng có gờ nhân bê nhân en quan sát."):
            self.play(LaggedStart(*[FadeIn(c[1], scale=0.5) for c in cells], lag_ratio=0.05), run_time=2)
            self.play(FadeIn(notes[1]), FadeIn(notes[2]), FadeIn(notes[3]))
        with self.say("Ta ký hiệu X l k r là quan sát thứ r, ở mức l của nhân tố một và mức k của nhân tố hai."):
            hl = SurroundingRectangle(cells[1 * b + 2], color=RED, buff=0.02, stroke_width=4)
            self.play(Create(hl), FadeIn(lg))
        self.clear_content()

        self.set_title("Mô hình hai nhân tố một biến", "(6-54), (6-55)")
        m = mt(r"X_{\ell k r}", "=", r"\mu", "+", r"\tau_\ell", "+", r"\beta_k", "+", r"\gamma_{\ell k}", "+", r"e_{\ell k r}", size=58)
        for i, c in [(2, BLUE), (4, GOLD), (6, PURPLE), (8, RED), (10, GREEN)]:
            m[i].set_color(c)
        idx = mt(r"\ell=1,\dots,g;\quad k=1,\dots,b;\quad r=1,\dots,n", size=32, color=MUTED)
        un, leg = legend(m, [2, 4, 6, 8, 10], ["mức chung", "hiệu ứng cố định của nhân tố 1",
                                               "hiệu ứng cố định của nhân tố 2", "tương tác nhân tố 1 – nhân tố 2",
                                               "sai số độc lập N(0, σ²)"], cols=2, size=22)
        cons = mt(r"\sum_{\ell=1}^{g}\tau_\ell=\sum_{k=1}^{b}\beta_k=\sum_{\ell=1}^{g}\gamma_{\ell k}=\sum_{k=1}^{b}\gamma_{\ell k}=0", size=34, color=MUTED)
        grp = VGroup(m, idx, leg, cons).arrange(DOWN, buff=0.4)
        self.fit(grp, top_buff=0.5)
        un, _ = legend(m, [2, 4, 6, 8, 10], [""] * 5)
        with self.say("Mô hình hai nhân tố cho một biến viết: X l k r bằng muy, cộng tau l, cộng bê-ta k, cộng gam-ma l k, cộng e l k r."):
            self.play(Write(m), run_time=2.5)
            self.play(FadeIn(idx))
        with self.say("Trong đó muy là mức chung. Tau l là hiệu ứng cố định của nhân tố một. Bê-ta k là hiệu ứng cố định của nhân tố hai. "
                      "Gam-ma l k là tương tác giữa nhân tố một và nhân tố hai. Còn e l k r là các sai số độc lập, chuẩn, trung bình không, "
                      "phương sai xích-ma bình phương."):
            self.play(Create(un), FadeIn(leg))
        with self.say("Để mô hình xác định duy nhất, các ràng buộc là: tổng các tau bằng không, tổng các bê-ta bằng không, và tổng các gam-ma "
                      "theo từng chỉ số cũng bằng không."):
            self.play(FadeIn(cons))
        self.clear_content()

        e = mt(r"E(X_{\ell k r})", "=", r"\mu", "+", r"\tau_\ell", "+", r"\beta_k", "+", r"\gamma_{\ell k}", size=58)
        for i, c in [(2, BLUE), (4, GOLD), (6, PURPLE), (8, RED)]:
            e[i].set_color(c)
        un, leg = legend(e, [0, 2, 4, 6, 8], ["phản hồi trung bình", "mức chung", "hiệu ứng nhân tố 1",
                                             "hiệu ứng nhân tố 2", "tương tác"], cols=3, size=22)
        grp = VGroup(e, leg).arrange(DOWN, buff=0.6)
        self.fit(grp, top_buff=0.9)
        un, _ = legend(e, [0, 2, 4, 6, 8], [""] * 5)
        with self.say("Vì vậy, phản hồi kỳ vọng ở mức l của nhân tố một và mức k của nhân tố hai bằng: mức chung, cộng hiệu ứng nhân tố một, "
                      "cộng hiệu ứng nhân tố hai, cộng tương tác. Đây là công thức sáu năm lăm."):
            self.play(Write(e), run_time=2)
            self.play(Create(un), FadeIn(leg))
        self.clear_content()

        self.set_title("Tương tác là gì? — Hình 6.3", "Figure 6.3: (a) có tương tác, (b) không có tương tác")
        va = [[2.0, 4.2, 1.5, 4.6], [2.6, 3.4, 2.9, 3.6], [1.4, 3.0, 0.8, 5.2]]
        vb = [[2.3, 3.5, 1.8, 4.3], [1.3, 2.5, 0.8, 3.3], [3.3, 4.5, 2.8, 5.3]]
        cols = [GOLD, BLUE, GREEN]
        names = ["Mức 1 của NT 1", "Mức 2 của NT 1", "Mức 3 của NT 1"]
        A, la, laa = interaction_axes(va, cols, names, "(a) Có tương tác")
        Bx, lb, lbb = interaction_axes(vb, cols, names, "(b) Không có tương tác")
        panel = VGroup(VGroup(A, la, laa), VGroup(Bx, lb, lbb)).arrange(RIGHT, buff=1.4)
        key = boxed(mix("Không có tương tác  ⇔ ", r"$\gamma_{\ell k}=0$", "với mọi ℓ, k  ⇔  các đường song song", size=26, color=GOLD), color=GOLD)
        self.fit(VGroup(panel, key).arrange(DOWN, buff=0.5), top_buff=0.4, grow=1.3)
        with self.say("Tương tác là khái niệm then chốt của mục này. Sự có mặt của tương tác gam-ma l k có nghĩa là hiệu ứng của các nhân tố "
                      "không cộng dồn được, và nó làm việc diễn giải kết quả phức tạp hơn. Hình 6.3 của sách minh hoạ điều này."):
            self.play(FadeIn(A), FadeIn(Bx))
        with self.say("Mỗi đường biểu diễn phản hồi kỳ vọng theo các mức của nhân tố hai, ứng với một mức của nhân tố một. "
                      "Ở hình bê, không có tương tác: các đường song song với nhau. Hiệu ứng của nhân tố hai là như nhau, bất kể nhân tố một ở mức nào. "
                      "Khoảng cách giữa các đường chính là hiệu ứng của nhân tố một."):
            self.play(LaggedStart(*[Create(l) for l in lb], lag_ratio=0.3), FadeIn(lbb), run_time=2.5)
        with self.say("Ở hình a, có tương tác: các đường không song song, thậm chí cắt nhau. Tác động khi chuyển từ mức này sang mức khác của "
                      "nhân tố hai phụ thuộc vào việc nhân tố một đang ở mức nào. Khi đó, nói chung chung về hiệu ứng của nhân tố một là không có ý nghĩa rõ ràng."):
            self.play(LaggedStart(*[Create(l) for l in la], lag_ratio=0.3), FadeIn(laa), run_time=2.5)
        with self.say("Tóm lại: không có tương tác nghĩa là mọi gam-ma l k bằng không, và trên đồ thị, các đường song song."):
            self.play(FadeIn(key, shift=UP * 0.2))
        self.clear_content()

        self.set_title("Phân tích quan sát hai nhân tố", "(6-56)")
        d = mt(r"x_{\ell k r}", "=", r"\bar x", "+", r"(\bar x_{\ell\cdot}-\bar x)", "+", r"(\bar x_{\cdot k}-\bar x)", "+",
               r"(\bar x_{\ell k}-\bar x_{\ell\cdot}-\bar x_{\cdot k}+\bar x)", "+", r"(x_{\ell k r}-\bar x_{\ell k})", size=40)
        for i, c in [(2, BLUE), (4, GOLD), (6, PURPLE), (8, RED), (10, GREEN)]:
            d[i].set_color(c)
        defs = bullet_list([
            mix(r"$\bar x$", ": trung bình chung của tất cả gbn quan sát", size=24),
            mix(r"$\bar x_{\ell\cdot}$", ": trung bình ở mức ℓ của nhân tố 1 (trung bình hàng)", size=24),
            mix(r"$\bar x_{\cdot k}$", ": trung bình ở mức k của nhân tố 2 (trung bình cột)", size=24),
            mix(r"$\bar x_{\ell k}$", ": trung bình của ô (ℓ, k) — mức ℓ của nhân tố 1 VÀ mức k của nhân tố 2", size=24),
        ], gap=0.28)
        un, leg = legend(d, [4, 6, 8, 10], ["hiệu ứng nhân tố 1", "hiệu ứng nhân tố 2", "tương tác", "phần dư"], cols=2, size=24)
        grp = VGroup(d, leg, defs).arrange(DOWN, buff=0.45)
        self.fit(grp, top_buff=0.5)
        un, _ = legend(d, [4, 6, 8, 10], [""] * 4)
        with self.say("Tương tự sáu năm lăm, mỗi quan sát được phân tích thành năm phần: trung bình chung; độ lệch của trung bình hàng; "
                      "độ lệch của trung bình cột; phần tương tác; và phần dư."):
            self.play(Write(d), run_time=3)
            self.play(Create(un), FadeIn(leg))
        with self.say("Ở đây, x ngang là trung bình chung. X ngang l chấm là trung bình ở mức l của nhân tố một. X ngang chấm k là trung bình ở mức k "
                      "của nhân tố hai. Và x ngang l k là trung bình của ô, tức là ở mức l của nhân tố một và mức k của nhân tố hai."):
            self.play(LaggedStart(*[FadeIn(r) for r in defs], lag_ratio=0.4), run_time=3)
        with self.say("Chú ý phần tương tác: x ngang l k trừ x ngang l chấm, trừ x ngang chấm k, cộng x ngang. Nó đo xem trung bình ô lệch bao nhiêu "
                      "so với giá trị mà ta dự đoán nếu hai nhân tố chỉ cộng dồn."):
            self.play(Indicate(d[8], color=RED, scale_factor=1.08), run_time=1.5)
        self.clear_content()

        self.set_title("Phân tích tổng bình phương và bậc tự do", "(6-57), (6-58)")
        s = mt(r"\sum_{\ell}\sum_{k}\sum_{r}(x_{\ell kr}-\bar x)^2", "=", r"\sum_{\ell}bn(\bar x_{\ell\cdot}-\bar x)^2", "+",
               r"\sum_{k}gn(\bar x_{\cdot k}-\bar x)^2", r"+\sum_{\ell}\sum_{k}n(\bar x_{\ell k}-\bar x_{\ell\cdot}-\bar x_{\cdot k}+\bar x)^2",
               r"+\sum_{\ell}\sum_{k}\sum_{r}(x_{\ell kr}-\bar x_{\ell k})^2", size=34)
        s[2].set_color(GOLD); s[4].set_color(PURPLE); s[5].set_color(RED); s[6].set_color(GREEN)
        top = VGroup(s[0], s[1], s[2], s[3], s[4]).copy()
        bot = VGroup(s[5], s[6]).copy()
        top.arrange(RIGHT, buff=0.15)
        bot.arrange(RIGHT, buff=0.15)
        eqg = VGroup(top, bot).arrange(DOWN, buff=0.3, aligned_edge=RIGHT)
        short = mt(r"SS_{cor}", "=", r"SS_{fac1}", "+", r"SS_{fac2}", "+", r"SS_{int}", "+", r"SS_{res}", size=46)
        short[2].set_color(GOLD); short[4].set_color(PURPLE); short[6].set_color(RED); short[8].set_color(GREEN)
        df = mt(r"gbn-1", "=", r"(g-1)", "+", r"(b-1)", "+", r"(g-1)(b-1)", "+", r"gb(n-1)", size=44)
        df[2].set_color(GOLD); df[4].set_color(PURPLE); df[6].set_color(RED); df[8].set_color(GREEN)
        dl = vt("Bậc tự do tương ứng:", size=24, color=MUTED)
        grp = VGroup(eqg, short, dl, df).arrange(DOWN, buff=0.45)
        self.fit(grp, top_buff=0.45)
        with self.say("Trừ x ngang hai vế, bình phương rồi cộng theo l, k và r, các tích chéo đều triệt tiêu. Ta được tổng bình phương toàn phần hiệu chỉnh "
                      "bằng tổng của bốn phần."):
            self.play(Write(eqg), run_time=3.5)
        with self.say("Viết gọn: S S cor bằng S S của nhân tố một, cộng S S nhân tố hai, cộng S S tương tác, cộng S S phần dư."):
            self.play(Write(short))
        with self.say("Bậc tự do cũng phân tích tương ứng: gờ bê en trừ một, bằng gờ trừ một, cộng bê trừ một, cộng gờ trừ một nhân bê trừ một, "
                      "cộng gờ bê nhân en trừ một."):
            self.play(FadeIn(dl), Write(df))
        self.clear_content()

        self.set_title("Bảng ANOVA hai nhân tố", "sách tr. 314")
        t = table([
            ["Nguồn", "Tổng bình phương (SS)", "Bậc tự do"],
            ["Nhân tố 1", mt(r"SS_{fac1}=\sum_{\ell=1}^{g}bn(\bar x_{\ell\cdot}-\bar x)^2", size=28, color=GOLD), mt("g-1", size=30)],
            ["Nhân tố 2", mt(r"SS_{fac2}=\sum_{k=1}^{b}gn(\bar x_{\cdot k}-\bar x)^2", size=28, color=PURPLE), mt("b-1", size=30)],
            ["Tương tác", mt(r"SS_{int}=\sum_{\ell}\sum_{k}n(\bar x_{\ell k}-\bar x_{\ell\cdot}-\bar x_{\cdot k}+\bar x)^2", size=28, color=RED), mt("(g-1)(b-1)", size=30)],
            ["Phần dư", mt(r"SS_{res}=\sum_{\ell}\sum_{k}\sum_{r}(x_{\ell kr}-\bar x_{\ell k})^2", size=28, color=GREEN), mt("gb(n-1)", size=30)],
            ["Toàn phần (h.c.)", mt(r"SS_{cor}=\sum_{\ell}\sum_{k}\sum_{r}(x_{\ell kr}-\bar x)^2", size=28), mt("gbn-1", size=30)],
        ], [2.8, 7.6, 2.6], row_h=0.9, size=24)
        Fr = mix("Kiểm định F:", r"$\dfrac{SS_{fac1}/(g-1)}{SS_{res}/(gb(n-1))}$", ",", r"$\dfrac{SS_{fac2}/(b-1)}{SS_{res}/(gb(n-1))}$", ",",
                 r"$\dfrac{SS_{int}/((g-1)(b-1))}{SS_{res}/(gb(n-1))}$", size=25)
        grp = VGroup(t, Fr).arrange(DOWN, buff=0.4)
        self.fit(grp, top_buff=0.35)
        with self.say("Bảng a-nô-va hai nhân tố có năm dòng: nhân tố một, nhân tố hai, tương tác, phần dư và toàn phần."):
            self.play(Create(t.lines), FadeIn(t.rows[0]))
            self.play(LaggedStart(*[FadeIn(r) for r in t.rows[1:]], lag_ratio=0.3), run_time=3)
        with self.say("Các tỉ số ép, lấy trung bình bình phương của nhân tố một, nhân tố hai và tương tác, chia cho trung bình bình phương phần dư, "
                      "được dùng để kiểm định lần lượt hiệu ứng của nhân tố một, nhân tố hai, và tương tác."):
            self.play(FadeIn(Fr, shift=UP * 0.2))
        self.clear_all()


class S08_TwoWayMulti(Lecture):
    section_label = "Phần 4 · Mục 6.7 Two-way MANOVA"

    def construct(self):
        self.set_title("Mô hình MANOVA hai nhân tố có tương tác", "Multivariate Two-Way Fixed-Effects Model with Interaction · (6-59)")
        m = mt(r"\mathbf X_{\ell k r}", "=", r"\boldsymbol\mu", "+", r"\boldsymbol\tau_\ell", "+", r"\boldsymbol\beta_k", "+",
               r"\boldsymbol\gamma_{\ell k}", "+", r"\mathbf e_{\ell k r}", size=58)
        for i, c in [(2, BLUE), (4, GOLD), (6, PURPLE), (8, RED), (10, GREEN)]:
            m[i].set_color(c)
        idx = mt(r"\ell=1,\dots,g;\quad k=1,\dots,b;\quad r=1,\dots,n", size=32, color=MUTED)
        cons = mt(r"\sum_{\ell}\boldsymbol\tau_\ell=\sum_{k}\boldsymbol\beta_k=\sum_{\ell}\boldsymbol\gamma_{\ell k}=\sum_{k}\boldsymbol\gamma_{\ell k}=\mathbf 0", size=34, color=MUTED)
        notes = bullet_list([
            vt("Mọi vectơ có cấp p × 1", size=24),
            mix(r"$\mathbf e_{\ell kr}$", "độc lập,", r"$\sim N_p(\mathbf 0,\boldsymbol\Sigma)$", size=24),
            vt("Phản hồi gồm p phép đo, lặp n lần ở mỗi tổ hợp mức của nhân tố 1 và 2", size=24),
        ], gap=0.3)
        grp = VGroup(m, idx, cons, notes).arrange(DOWN, buff=0.45)
        self.fit(grp, top_buff=0.5)
        with self.say("Bây giờ, làm tương tự, ta xây dựng mô hình hai nhân tố hiệu ứng cố định cho một phản hồi dạng vectơ gồm pê thành phần. "
                      "Mô hình giống hệt trường hợp một biến, chỉ khác là mọi thứ giờ là vectơ, in đậm."):
            self.play(Write(m), run_time=2.5)
            self.play(FadeIn(idx))
        with self.say("Các ràng buộc vẫn như cũ, nhưng là vectơ không. Mọi vectơ có cấp pê nhân một. Sai số e l k r độc lập, có phân phối chuẩn pê chiều, "
                      "trung bình không, hiệp phương sai xích-ma. Như vậy, phản hồi gồm pê phép đo, được lặp en lần ở mỗi tổ hợp mức của hai nhân tố."):
            self.play(FadeIn(cons))
            self.play(LaggedStart(*[FadeIn(r) for r in notes], lag_ratio=0.4), run_time=2)
        self.clear_content()

        self.set_title("Phân tích vectơ quan sát", "(6-60)")
        d = mt(r"\mathbf x_{\ell k r}", "=", r"\bar{\mathbf x}", "+", r"(\bar{\mathbf x}_{\ell\cdot}-\bar{\mathbf x})", "+",
               r"(\bar{\mathbf x}_{\cdot k}-\bar{\mathbf x})", "+",
               r"(\bar{\mathbf x}_{\ell k}-\bar{\mathbf x}_{\ell\cdot}-\bar{\mathbf x}_{\cdot k}+\bar{\mathbf x})", "+",
               r"(\mathbf x_{\ell k r}-\bar{\mathbf x}_{\ell k})", size=38)
        for i, c in [(2, BLUE), (4, GOLD), (6, PURPLE), (8, RED), (10, GREEN)]:
            d[i].set_color(c)
        rule = boxed(VGroup(
            vt("Quy tắc tổng quát hoá từ một biến sang nhiều biến:", size=26, color=ACCENT),
            mt(r"(\bar x_{\ell\cdot}-\bar x)^2\quad\longrightarrow\quad(\bar{\mathbf x}_{\ell\cdot}-\bar{\mathbf x})(\bar{\mathbf x}_{\ell\cdot}-\bar{\mathbf x})'", size=40),
        ).arrange(DOWN, buff=0.3), color=ACCENT)
        grp = VGroup(d, rule).arrange(DOWN, buff=0.8)
        self.fit(grp, top_buff=0.8)
        with self.say("Theo sáu năm sáu, vectơ quan sát được phân tích thành năm thành phần: trung bình chung, hiệu ứng nhân tố một, hiệu ứng nhân tố hai, "
                      "tương tác, và phần dư. Ở đây x ngang là trung bình của mọi vectơ quan sát, x ngang l chấm là trung bình ở mức l của nhân tố một, "
                      "x ngang chấm k là trung bình ở mức k của nhân tố hai, và x ngang l k là trung bình của ô l k."):
            self.play(Write(d), run_time=3.5)
        with self.say("Và một lần nữa, quy tắc tổng quát hoá rất đơn giản: thay mỗi bình phương của số vô hướng bằng tích của vectơ với chuyển vị của nó."):
            self.play(FadeIn(rule, shift=UP * 0.2))
        self.clear_content()

        self.set_title("Bảng MANOVA hai nhân tố", "sách tr. 315–316 · (6-61), (6-62)")
        t = table([
            ["Nguồn", "Ma trận SSP", "Bậc tự do"],
            ["Nhân tố 1", mt(r"\mathbf{SSP}_{fac1}=\sum_{\ell=1}^{g}bn(\bar{\mathbf x}_{\ell\cdot}-\bar{\mathbf x})(\bar{\mathbf x}_{\ell\cdot}-\bar{\mathbf x})'", size=26, color=GOLD), mt("g-1", size=28)],
            ["Nhân tố 2", mt(r"\mathbf{SSP}_{fac2}=\sum_{k=1}^{b}gn(\bar{\mathbf x}_{\cdot k}-\bar{\mathbf x})(\bar{\mathbf x}_{\cdot k}-\bar{\mathbf x})'", size=26, color=PURPLE), mt("b-1", size=28)],
            ["Tương tác", mt(r"\mathbf{SSP}_{int}=\sum_{\ell}\sum_{k}n(\bar{\mathbf x}_{\ell k}-\bar{\mathbf x}_{\ell\cdot}-\bar{\mathbf x}_{\cdot k}+\bar{\mathbf x})(\cdots)'", size=26, color=RED), mt("(g-1)(b-1)", size=28)],
            ["Phần dư", mt(r"\mathbf{SSP}_{res}=\sum_{\ell}\sum_{k}\sum_{r}(\mathbf x_{\ell kr}-\bar{\mathbf x}_{\ell k})(\mathbf x_{\ell kr}-\bar{\mathbf x}_{\ell k})'", size=26, color=GREEN), mt("gb(n-1)", size=28)],
            ["Toàn phần (h.c.)", mt(r"\mathbf{SSP}_{cor}=\sum_{\ell}\sum_{k}\sum_{r}(\mathbf x_{\ell kr}-\bar{\mathbf x})(\mathbf x_{\ell kr}-\bar{\mathbf x})'", size=26), mt("gbn-1", size=28)],
        ], [2.7, 8.2, 2.3], row_h=0.95, size=24)
        eq = mt(r"\mathbf{SSP}_{cor}", "=", r"\mathbf{SSP}_{fac1}", "+", r"\mathbf{SSP}_{fac2}", "+", r"\mathbf{SSP}_{int}", "+", r"\mathbf{SSP}_{res}", size=36)
        eq[2].set_color(GOLD); eq[4].set_color(PURPLE); eq[6].set_color(RED); eq[8].set_color(GREEN)
        grp = VGroup(t, eq).arrange(DOWN, buff=0.4)
        self.fit(grp, top_buff=0.35)
        with self.say("Tổng quát hoá trực tiếp sáu năm bảy và sáu năm tám, ta có phân tích ma trận tổng bình phương và tích chéo, cùng bậc tự do, "
                      "tóm tắt trong bảng ma-nô-va hai nhân tố."):
            self.play(Create(t.lines), FadeIn(t.rows[0]))
            self.play(LaggedStart(*[FadeIn(r) for r in t.rows[1:]], lag_ratio=0.3), run_time=3)
        with self.say("Ma trận toàn phần bằng tổng của bốn ma trận: nhân tố một, nhân tố hai, tương tác và phần dư. Bậc tự do giữ nguyên như bảng a-nô-va."):
            self.play(Write(eq))
        self.clear_content()

        self.set_title("Bước 1: Kiểm định tương tác TRƯỚC", "(6-63), (6-64), (6-65)")
        h = VGroup(
            mix(r"$H_0:\ \boldsymbol\gamma_{11}=\boldsymbol\gamma_{12}=\cdots=\boldsymbol\gamma_{gb}=\mathbf 0$", "(không có hiệu ứng tương tác)", size=28, color=RED),
            mix(r"$H_1:$", "có ít nhất một", r"$\boldsymbol\gamma_{\ell k}\neq\mathbf 0$", size=28),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        lam = mt(r"\Lambda^*=\frac{|\mathbf{SSP}_{res}|}{|\mathbf{SSP}_{int}+\mathbf{SSP}_{res}|}", size=48)
        bart = mt(r"-\left[gb(n-1)-\frac{p+1-(g-1)(b-1)}{2}\right]\ln\Lambda^*>\chi^2_{(g-1)(b-1)p}(\alpha)", size=38, color=GOLD)
        bl = vt("Bác bỏ H₀ ở mức α nếu (xấp xỉ Bartlett, mẫu lớn):", size=24, color=MUTED)
        foot = vt("Chú thích 5: kiểm định tỉ số hợp lý cần p ≤ gb(n − 1) để ma trận SSP phần dư xác định dương.", size=20, color=MUTED)
        grp = VGroup(h, lam, bl, bart, foot).arrange(DOWN, buff=0.38)
        self.fit(grp, top_buff=0.4)
        with self.say("Giờ đến phần kiểm định. Thông thường, kiểm định tương tác được thực hiện trước, rồi mới đến các hiệu ứng chính. "
                      "Giả thuyết không là: mọi gam-ma l k bằng vectơ không, tức là không có hiệu ứng tương tác. Đối thuyết là có ít nhất một gam-ma khác không."):
            self.play(FadeIn(h))
        with self.say("Kiểm định tỉ số hợp lý bác bỏ giả thuyết không khi lam-đa sao nhỏ. Ở đây, lam-đa sao bằng định thức của S S P phần dư, "
                      "chia định thức của S S P tương tác cộng S S P phần dư."):
            self.play(Write(lam))
        with self.say("Với mẫu lớn, dùng hệ số hiệu chỉnh của Bác-lét: ta bác bỏ nếu âm của, gờ bê nhân en trừ một, trừ pê cộng một trừ gờ trừ một nhân bê trừ một, "
                      "tất cả chia hai, nhân với lốc lam-đa, lớn hơn phân vị khi bình phương với gờ trừ một nhân bê trừ một nhân pê bậc tự do."):
            self.play(FadeIn(bl), Write(bart), run_time=2.5)
        with self.say("Lưu ý chú thích của sách: kiểm định này đòi hỏi pê không vượt quá gờ bê nhân en trừ một, để ma trận phần dư xác định dương."):
            self.play(FadeIn(foot))
        self.clear_content()

        self.set_title("Nếu có tương tác thì sao?", "Lời khuyên của sách, tr. 316–317")
        flow = VGroup()
        b1 = boxed(vt("Kiểm định tương tác", size=26, weight=BOLD), color=RED)
        b2 = boxed(VGroup(vt("CÓ tương tác", size=24, color=RED, weight=BOLD),
                          vt("Hiệu ứng nhân tố không có\ndiễn giải rõ ràng.\nKhông nên làm tiếp các\nkiểm định đa biến.\n→ Làm p ANOVA hai nhân tố\ncho từng biến; vẽ đồ thị tương tác", size=20)).arrange(DOWN, buff=0.15), color=RED)
        b3 = boxed(VGroup(vt("KHÔNG có tương tác", size=24, color=GREEN, weight=BOLD),
                          vt("Hiệu ứng cộng dồn.\nKiểm định hiệu ứng chính\ncủa nhân tố 1 và nhân tố 2", size=20)).arrange(DOWN, buff=0.15), color=GREEN)
        VGroup(b2, b3).arrange(RIGHT, buff=1.5)
        VGroup(b1, VGroup(b2, b3)).arrange(DOWN, buff=0.9)
        a1 = Arrow(b1.get_bottom(), b2.get_top(), color=RED, buff=0.1)
        a2 = Arrow(b1.get_bottom(), b3.get_top(), color=GREEN, buff=0.1)
        flow = VGroup(b1, b2, b3, a1, a2)
        self.fit(flow, top_buff=0.5, grow=1.5)
        with self.say("Vì sao phải kiểm định tương tác trước? Sách giải thích: nếu tồn tại hiệu ứng tương tác, các hiệu ứng nhân tố không có một diễn giải rõ ràng."):
            self.play(FadeIn(b1))
        with self.say("Khi đó, về mặt thực hành, không nên tiến hành thêm các kiểm định đa biến. Thay vào đó, người ta thường làm pê phân tích a-nô-va hai nhân tố, "
                      "mỗi biến một lần, để xem tương tác xuất hiện ở những biến phản hồi nào. Những biến không có tương tác có thể diễn giải theo hiệu ứng cộng dồn "
                      "của nhân tố một và hai, nếu các hiệu ứng này tồn tại. Đồ thị tương tác giống hình 6.3, nhưng dùng trung bình mẫu, giúp làm rõ nhất."):
            self.play(GrowArrow(a1), FadeIn(b2))
        with self.say("Ngược lại, nếu không có tương tác, hiệu ứng của hai nhân tố cộng dồn, và ta chuyển sang kiểm định các hiệu ứng chính."):
            self.play(GrowArrow(a2), FadeIn(b3))
        self.clear_content()

        self.set_title("Bước 2: Kiểm định các hiệu ứng chính", "(6-66) – (6-69)")
        f1 = VGroup(
            mix("Nhân tố 1:", r"$H_0:\boldsymbol\tau_1=\cdots=\boldsymbol\tau_g=\mathbf 0$", size=26, color=GOLD),
            mt(r"\Lambda^*=\frac{|\mathbf{SSP}_{res}|}{|\mathbf{SSP}_{fac1}+\mathbf{SSP}_{res}|}", size=40),
            mt(r"-\left[gb(n-1)-\frac{p+1-(g-1)}{2}\right]\ln\Lambda^*>\chi^2_{(g-1)p}(\alpha)", size=32, color=GOLD),
        ).arrange(DOWN, buff=0.3)
        f2 = VGroup(
            mix("Nhân tố 2:", r"$H_0:\boldsymbol\beta_1=\cdots=\boldsymbol\beta_b=\mathbf 0$", size=26, color=PURPLE),
            mt(r"\Lambda^*=\frac{|\mathbf{SSP}_{res}|}{|\mathbf{SSP}_{fac2}+\mathbf{SSP}_{res}|}", size=40),
            mt(r"-\left[gb(n-1)-\frac{p+1-(b-1)}{2}\right]\ln\Lambda^*>\chi^2_{(b-1)p}(\alpha)", size=32, color=PURPLE),
        ).arrange(DOWN, buff=0.3)
        grp = VGroup(f1, f2).arrange(DOWN, buff=0.6)
        self.fit(grp, top_buff=0.45)
        with self.say("Trong mô hình nhiều chiều, hiệu ứng chính của nhân tố một được kiểm định với giả thuyết không: mọi tau l bằng không. "
                      "Ta tính lam-đa sao bằng định thức S S P phần dư, chia định thức của S S P nhân tố một cộng S S P phần dư. Lam-đa nhỏ ủng hộ đối thuyết. "
                      "Với hiệu chỉnh Bác-lét, ta bác bỏ nếu thống kê lớn hơn khi bình phương với gờ trừ một nhân pê bậc tự do."):
            self.play(FadeIn(f1[0]))
            self.play(Write(f1[1]))
            self.play(Write(f1[2]))
        with self.say("Hoàn toàn tương tự cho nhân tố hai: thay S S P nhân tố một bằng S S P nhân tố hai, và bậc tự do là bê trừ một nhân pê."):
            self.play(FadeIn(f2[0]))
            self.play(Write(f2[1]))
            self.play(Write(f2[2]))
        self.clear_content()

        self.set_title("Khoảng tin cậy đồng thời (Bonferroni)", "(6-70), (6-71)")
        c1 = mt(r"\tau_{\ell i}-\tau_{m i}\ \in\ (\bar x_{\ell\cdot i}-\bar x_{m\cdot i})\pm t_\nu\!\left(\frac{\alpha}{pg(g-1)}\right)\sqrt{\frac{E_{ii}}{\nu}\frac{2}{bn}}", size=40, color=GOLD)
        c2 = mt(r"\beta_{k i}-\beta_{q i}\ \in\ (\bar x_{\cdot k i}-\bar x_{\cdot q i})\pm t_\nu\!\left(\frac{\alpha}{pb(b-1)}\right)\sqrt{\frac{E_{ii}}{\nu}\frac{2}{gn}}", size=40, color=PURPLE)
        wh = bullet_list([
            mix(r"$\nu=gb(n-1)$", ",", r"$E_{ii}$", "là phần tử đường chéo thứ i của", r"$\mathbf E=\mathbf{SSP}_{res}$", size=24),
            mix(r"$\bar x_{\ell\cdot i}-\bar x_{m\cdot i}$", "là thành phần thứ i của", r"$\bar{\mathbf x}_{\ell\cdot}-\bar{\mathbf x}_{m\cdot}$", size=24),
            vt("Dùng khi tương tác không đáng kể: tập trung vào tương phản của các hiệu ứng chính", size=24),
        ], gap=0.3)
        grp = VGroup(c1, c2, wh).arrange(DOWN, buff=0.5)
        self.fit(grp, top_buff=0.5)
        with self.say("Khi bác bỏ giả thuyết về hiệu ứng chính, ta muốn biết cụ thể khác nhau ở đâu. Khi tương tác không đáng kể, ta tập trung vào các tương phản "
                      "của hiệu ứng chính. Phương pháp Bôn-phe-rô-ni áp dụng cho từng thành phần của hiệu tau l trừ tau m, và bê-ta k trừ bê-ta q."):
            self.play(Write(c1), run_time=2.5)
            self.play(Write(c2), run_time=2.5)
        with self.say("Trong đó nuy bằng gờ bê nhân en trừ một, E i i là phần tử đường chéo thứ i của ma trận phần dư, và hiệu trung bình là thành phần thứ i "
                      "của hiệu hai vectơ trung bình."):
            self.play(LaggedStart(*[FadeIn(r) for r in wh], lag_ratio=0.4), run_time=2.5)
        self.clear_content()

        self.set_title("Nhận xét: khi chỉ có một quan sát mỗi ô", "Comment, tr. 318")
        cmt = bullet_list([
            vt("Mô hình trên có n lần lặp ở mỗi tổ hợp mức ⇒ ước lượng được tương tác.", size=27),
            vt("Nếu mỗi ô chỉ có MỘT vectơ quan sát (n = 1):", size=27, color=GOLD),
            vt("   không thể đưa số hạng tương tác tổng quát γℓk vào mô hình;", size=27),
            vt("   bảng MANOVA chỉ còn nhân tố 1, nhân tố 2 và phần dư.", size=27),
        ], gap=0.4)
        self.fit(cmt, top_buff=0.8)
        with self.say("Một nhận xét cuối của sách. Mô hình ta vừa học có en lần lặp ở mỗi tổ hợp mức, nhờ vậy mới khảo sát được tương tác. "
                      "Nếu mỗi tổ hợp chỉ có một vectơ quan sát, mô hình hai nhân tố không cho phép có số hạng tương tác tổng quát. "
                      "Khi đó bảng ma-nô-va chỉ gồm nhân tố một, nhân tố hai và phần dư."):
            self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.2) for r in cmt], lag_ratio=0.5), run_time=4)
        self.clear_all()
