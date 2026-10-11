"""Bản tóm tắt ~2 phút: ANOVA → thuật ngữ → 6.4 One-way MANOVA → 6.7 Two-way MANOVA (Ví dụ 6.13)."""
from common import *
from part4_twoway import interaction_axes


class V1_Idea(Lecture):
    def construct(self):
        t1 = vt("MANOVA trong 2 phút", size=56, weight=BOLD)
        t2 = vt("Johnson & Wichern · mục 6.4 và 6.7", size=26, color=MUTED)
        VGroup(t1, t2).arrange(DOWN, buff=0.35)
        with self.say("Ma-nô-va trong hai phút: từ a-nô-va, đến ma-nô-va một nhân tố, rồi hai nhân tố."):
            self.play(FadeIn(t1, shift=UP * 0.3), FadeIn(t2))
        self.clear_all()

        # Ý tưởng ANOVA: tách biến thiên
        self.set_title("① Ý tưởng ANOVA: tách biến thiên")
        rng = [[2.0, 2.6, 1.6], [4.2, 4.8, 3.9], [3.1, 2.7, 3.5]]
        cols = [GOLD, BLUE, GREEN]
        ax = NumberLine(x_range=[1, 5.5, 1], length=9, color=MUTED, include_numbers=False).shift(DOWN * 0.2)
        dots = VGroup()
        means = VGroup()
        for i, (vals, c) in enumerate(zip(rng, cols)):
            y = 1.0 - i * 0.55
            for v in vals:
                dots.add(Dot(ax.n2p(v) + UP * y, color=c, radius=0.09))
            m = sum(vals) / 3
            means.add(Line(ax.n2p(m) + UP * (y + 0.25), ax.n2p(m) + UP * (y - 0.25), color=c, stroke_width=5))
        gm = DashedLine(ax.n2p(3.1) + UP * 1.5, ax.n2p(3.1) + DOWN * 0.3, color=FG)
        eq = mt(r"SS_{\text{total}}", "=", r"SS_{\text{between}}", "+", r"SS_{\text{within}}", size=48)
        eq[2].set_color(GOLD); eq[4].set_color(GREEN)
        F = mix(r"$F=\dfrac{\text{between}}{\text{within}}$", "lớn  ⇒  các nhóm thật sự khác nhau", size=28, color=GOLD)
        grp = VGroup(VGroup(dots, means, gm), eq, F).arrange(DOWN, buff=0.55)
        self.fit(grp, top_buff=0.5)
        with self.say("Ba nhóm số liệu. Câu hỏi: trung bình các nhóm có khác nhau thật không, hay chỉ do ngẫu nhiên?"):
            self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in dots], lag_ratio=0.08), run_time=1.5)
            self.play(Create(means), Create(gm))
        with self.say("A-nô-va tách biến thiên thành hai phần: giữa các nhóm và trong nhóm. Phần giữa nhóm lớn hơn hẳn, tỉ số ép lớn, thì các nhóm khác nhau."):
            self.play(Write(eq))
            self.play(FadeIn(F, shift=UP * 0.2))
        self.clear_all()

        # Nâng lên nhiều biến
        self.set_title("② Nhiều biến cùng lúc → MANOVA (mục 6.4)")
        row1 = VGroup(mix("số", "$x$", size=28), mt(r"\longrightarrow", size=40, color=ACCENT), mix("vectơ", r"$\mathbf x$", "(p biến)", size=28)).arrange(RIGHT, buff=0.4)
        row2 = VGroup(mt(r"(\bar x_\ell-\bar x)^2", size=38), mt(r"\longrightarrow", size=40, color=ACCENT),
                      mt(r"(\bar{\mathbf x}_\ell-\bar{\mathbf x})(\bar{\mathbf x}_\ell-\bar{\mathbf x})'", size=38)).arrange(RIGHT, buff=0.4)
        row3 = VGroup(mt(r"SS_{between},\ SS_{within}", size=38), mt(r"\longrightarrow", size=40, color=ACCENT),
                      mt(r"\mathbf B,\ \mathbf W", size=44, color=GOLD)).arrange(RIGHT, buff=0.4)
        rows = VGroup(row1, row2, row3).arrange(DOWN, buff=0.4)
        lam = mt(r"\Lambda^*=\frac{|\mathbf W|}{|\mathbf B+\mathbf W|}", size=56, color=ACCENT)
        note = vt("Wilks' lambda: Λ* nhỏ ⇒ có hiệu ứng", size=26, color=ACCENT)
        grp = VGroup(rows, VGroup(lam, note).arrange(DOWN, buff=0.2)).arrange(DOWN, buff=0.6)
        self.fit(grp, top_buff=0.5)
        with self.say("Khi đo nhiều biến cùng lúc, ta dùng ma-nô-va: con số thành vectơ, bình phương thành ma trận, và hai tổng bình phương thành hai ma trận bê và đáp-bờ-liu."):
            for r in rows:
                self.play(FadeIn(r, shift=RIGHT * 0.3), run_time=0.8)
        with self.say("So sánh chúng bằng định thức, ta được lam-đa Uyn-xơ. Lam-đa càng nhỏ, khác biệt càng rõ."):
            self.play(Write(lam))
            self.play(FadeIn(note))
        self.clear_content()

        self.set_title("Ví dụ 6.9 — 3 nhóm, 2 biến")
        B = mt(r"\mathbf B=\begin{bmatrix}78&-12\\-12&48\end{bmatrix}", size=42, color=GOLD)
        W = mt(r"\mathbf W=\begin{bmatrix}10&1\\1&24\end{bmatrix}", size=42, color=GREEN)
        mats = VGroup(B, W).arrange(RIGHT, buff=1.2)
        lam = mt(r"\Lambda^*=\frac{239}{6215}=0.0385", r"\ \Rightarrow\ ", r"F=8.19>7.01", size=46)
        lam[2].set_color(GOLD)
        c = vt("⇒ Bác bỏ H₀: các nhóm khác nhau", size=30, color=GOLD)
        grp = VGroup(mats, lam, c).arrange(DOWN, buff=0.6)
        self.fit(grp, top_buff=0.6)
        with self.say("Ví dụ 6.9: lam-đa chỉ không phẩy không ba tám năm, ép tám phẩy một chín vượt ngưỡng bảy phẩy không một. Ba nhóm khác nhau."):
            self.play(FadeIn(mats))
            self.play(Write(lam))
            self.play(FadeIn(c))
        self.clear_all()


class V2_TwoWay(Lecture):
    def construct(self):
        self.set_title("③ Hai nhân tố → Two-way MANOVA (mục 6.7)")
        m = mt(r"\mathbf X_{\ell k r}", "=", r"\boldsymbol\mu", "+", r"\boldsymbol\tau_\ell", "+", r"\boldsymbol\beta_k", "+",
               r"\boldsymbol\gamma_{\ell k}", "+", r"\mathbf e_{\ell k r}", size=58)
        for i, c in [(2, BLUE), (4, GOLD), (6, PURPLE), (8, RED), (10, GREEN)]:
            m[i].set_color(c)
        un, leg = legend(m, [4, 6, 8, 10], ["nhân tố 1", "nhân tố 2", "tương tác", "sai số"], cols=4, size=26, col_gap=0.7)
        ssp = mt(r"\mathbf{SSP}_{cor}", "=", r"\mathbf{SSP}_{fac1}", "+", r"\mathbf{SSP}_{fac2}", "+", r"\mathbf{SSP}_{int}", "+", r"\mathbf{SSP}_{res}", size=42)
        ssp[2].set_color(GOLD); ssp[4].set_color(PURPLE); ssp[6].set_color(RED); ssp[8].set_color(GREEN)
        grp = VGroup(m, leg, ssp).arrange(DOWN, buff=0.6)
        self.fit(grp, top_buff=0.6)
        un, _ = legend(m, [4, 6, 8, 10], [""] * 4)
        with self.say("Mục 6.7, phần trọng tâm: có hai nhân tố cùng tác động. Mô hình thêm hiệu ứng nhân tố hai, và một số hạng mới: tương tác gam-ma."):
            self.play(Write(m), run_time=2)
            self.play(Create(un), FadeIn(leg))
        with self.say("Tương ứng, ma trận toàn phần tách thành bốn phần: nhân tố một, nhân tố hai, tương tác, và phần dư."):
            self.play(Write(ssp))
        self.clear_content()

        self.set_title("Tương tác: các đường có song song không?")
        va = [[2.0, 4.2, 1.5, 4.6], [2.6, 3.4, 2.9, 3.6], [1.4, 3.0, 0.8, 5.2]]
        vb = [[2.3, 3.5, 1.8, 4.3], [1.3, 2.5, 0.8, 3.3], [3.3, 4.5, 2.8, 5.3]]
        cols = [GOLD, BLUE, GREEN]
        names = ["Mức 1", "Mức 2", "Mức 3"]
        A, la, laa = interaction_axes(vb, cols, names, "Song song: KHÔNG tương tác")
        Bx, lb, lbb = interaction_axes(va, cols, names, "Cắt nhau: CÓ tương tác")
        panel = VGroup(VGroup(A, la, laa), VGroup(Bx, lb, lbb)).arrange(RIGHT, buff=1.4)
        rule = vt("Luôn kiểm định TƯƠNG TÁC trước, rồi mới đến từng nhân tố", size=28, color=GOLD)
        grp = VGroup(panel, rule).arrange(DOWN, buff=0.5)
        self.fit(grp, top_buff=0.4, grow=1.3)
        with self.say("Tương tác là gì? Nếu các đường song song, hiệu ứng hai nhân tố chỉ cộng dồn. "
                      "Nếu các đường cắt nhau, tác động của nhân tố này phụ thuộc vào nhân tố kia."):
            self.play(FadeIn(A), FadeIn(Bx))
            self.play(LaggedStart(*[Create(l) for l in la], lag_ratio=0.3), FadeIn(laa), run_time=1.5)
            self.play(LaggedStart(*[Create(l) for l in lb], lag_ratio=0.3), FadeIn(lbb), run_time=1.5)
        with self.say("Vì vậy, quy tắc của sách là: luôn kiểm định tương tác trước, rồi mới kiểm định từng nhân tố."):
            self.play(FadeIn(rule, shift=UP * 0.2))
        self.clear_all()


class V3_Example(Lecture):
    def construct(self):
        self.set_title("④ Ví dụ 6.13 — Màng nhựa")
        ctx = mix("3 biến: độ bền xé, độ bóng, độ mờ  ·  nhân tố: tốc độ đùn, lượng phụ gia  ·  n = 5", size=24, color=MUTED)
        def bar(label, lam, F, color, verdict):
            box_ = RoundedRectangle(width=12.4, height=1.15, corner_radius=0.15, stroke_color=color, fill_color=PANEL, fill_opacity=1)
            l = vt(label, size=28, color=color, weight=BOLD)
            s = mt(rf"\Lambda^*={lam}\qquad F={F}", size=36)
            v = vt(verdict, size=26, color=color)
            row = VGroup(l, s, v)
            l.move_to(box_.get_left() + RIGHT * 1.6)
            s.move_to(box_.get_center() + LEFT * 0.4)
            v.move_to(box_.get_right() + LEFT * 2.0)
            return VGroup(box_, row)
        b1 = bar("Tương tác", ".7771", "1.34", MUTED, "✗ không ý nghĩa")
        b2 = bar("Tốc độ đùn", ".3819", "7.55", GOLD, "✓ có hiệu ứng")
        b3 = bar("Phụ gia", ".5230", "4.26", PURPLE, "✓ có hiệu ứng")
        thr = mix("Ngưỡng:", r"$F_{3,14}(0.05)=3.34$", size=26, color=MUTED)
        grp = VGroup(ctx, thr, b1, b2, b3).arrange(DOWN, buff=0.35)
        self.fit(grp, top_buff=0.45)
        with self.say("Ví dụ 6.13: màng nhựa đo ba biến, theo tốc độ đùn và lượng phụ gia. Ngưỡng ép là ba phẩy ba tư."):
            self.play(FadeIn(ctx), FadeIn(thr))
        with self.say("Bước một, tương tác: ép chỉ một phẩy ba tư, không có ý nghĩa."):
            self.play(FadeIn(b1, shift=RIGHT * 0.3))
        with self.say("Bước hai, hiệu ứng chính: tốc độ đùn, ép bảy phẩy năm lăm; phụ gia, ép bốn phẩy hai sáu. Cả hai đều có ý nghĩa."):
            self.play(FadeIn(b2, shift=RIGHT * 0.3))
            self.play(FadeIn(b3, shift=RIGHT * 0.3))
        self.clear_all()

        head = vt("Kết luận", size=44, color=ACCENT, weight=BOLD)
        c = vt("Tốc độ đùn và lượng phụ gia đều ảnh hưởng đến màng nhựa,\ntheo cách cộng dồn — không có tương tác.",
               size=30, align=ORIGIN)
        flow = VGroup(*[boxed(vt(s, size=24), color=col) for s, col in
                        [("Bảng MANOVA", ACCENT), ("Tương tác?", RED), ("Hiệu ứng chính", GOLD), ("Kết luận", GREEN)]]).arrange(RIGHT, buff=0.6)
        arrows = VGroup(*[Arrow(flow[i].get_right(), flow[i + 1].get_left(), buff=0.08, color=MUTED, max_tip_length_to_length_ratio=0.3)
                          for i in range(3)])
        g = VGroup(head, c, VGroup(flow, arrows)).arrange(DOWN, buff=0.7)
        with self.say("Kết luận: cả hai nhân tố đều ảnh hưởng, theo cách cộng dồn. Đó là toàn bộ logic: lập bảng, kiểm định tương tác, rồi hiệu ứng chính."):
            self.play(FadeIn(head), FadeIn(c))
            self.play(LaggedStart(*[FadeIn(f) for f in flow], lag_ratio=0.4), Create(arrows), run_time=2.5)
        self.wait(1)
        self.play(FadeOut(g))
