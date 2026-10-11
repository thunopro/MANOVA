"""Bản rút gọn ~5 phút: ANOVA -> thuật ngữ -> 6.4 One-way MANOVA -> 6.7 Two-way MANOVA (Ví dụ 6.13)."""
from common import *
from part4_twoway import interaction_axes


class Short01_Anova(Lecture):
    section_label = "1 · Tổng quan ANOVA"

    def construct(self):
        t1 = vt("MANOVA một nhân tố và hai nhân tố", size=50, weight=BOLD)
        t2 = vt("Johnson & Wichern, Applied Multivariate Statistical Analysis — mục 6.4 và 6.7", size=24, color=MUTED)
        title = VGroup(t1, t2).arrange(DOWN, buff=0.4)
        with self.say("Chào các em. Trong năm phút, ta sẽ đi từ a-nô-va, qua ma-nô-va một nhân tố ở mục 6.4, "
                      "đến nội dung chính là ma-nô-va hai nhân tố ở mục 6.7."):
            self.play(FadeIn(t1, shift=UP * 0.3), FadeIn(t2))
        self.clear_all()

        self.set_title("Tổng quan ANOVA", "So sánh trung bình của g nhóm · (6-33), (6-34)")
        model = mt(r"X_{\ell j}", "=", r"\mu", "+", r"\tau_\ell", "+", r"e_{\ell j}", size=56)
        model[2].set_color(BLUE); model[4].set_color(GOLD); model[6].set_color(GREEN)
        h0 = mt(r"H_0:\ \tau_1=\tau_2=\cdots=\tau_g=0", size=40, color=GOLD)
        ss = mt(r"SS_{cor}", "=", r"SS_{tr}", "+", r"SS_{res}", size=48)
        ss[2].set_color(GOLD); ss[4].set_color(GREEN)
        F = mt(r"F=\frac{SS_{tr}/(g-1)}{SS_{res}/(\sum n_\ell-g)}", size=44)
        ex = mix("Ví dụ 6.7–6.8:", r"$88=78+10$", ",", r"$F=\frac{78/2}{10/5}=19.5>F_{2,5}(.01)=13.27$", "⇒ bác bỏ", "$H_0$",
                 size=24, color=MUTED)
        grp = VGroup(model, h0, VGroup(ss, F).arrange(RIGHT, buff=1.0), ex).arrange(DOWN, buff=0.5)
        self.fit(grp, top_buff=0.5)
        with self.say("A-nô-va so sánh trung bình của gờ nhóm. Mỗi quan sát bằng trung bình chung muy, cộng hiệu ứng xử lý tau l, "
                      "cộng sai số. Giả thuyết không là mọi hiệu ứng tau bằng không."):
            self.play(Write(model))
            self.play(FadeIn(h0))
        with self.say("Tổng bình phương toàn phần được tách thành phần giữa các nhóm, S S xử lý, và phần trong nhóm, S S phần dư. "
                      "Nếu phần xử lý lớn so với phần dư, tỉ số ép lớn, ta bác bỏ giả thuyết. Ví dụ 6.8 trong sách cho ép bằng mười chín phẩy năm, "
                      "lớn hơn mười ba phẩy hai bảy, nên bác bỏ."):
            self.play(Write(grp[2]))
            self.play(FadeIn(ex))
        self.clear_all()


class Short02_Terms(Lecture):
    section_label = "2 · Thuật ngữ"

    def construct(self):
        self.set_title("Thuật ngữ cần nắm")
        data = [["Thuật ngữ", "Ý nghĩa"]]
        rows = [
            ("Nhân tố (factor) / mức (level)", "điều kiện thí nghiệm / giá trị cụ thể của nó"),
            ("Hiệu ứng xử lý τℓ", "độ lệch trung bình nhóm ℓ so với mức chung"),
            ("Tương tác γℓk (interaction)", "hiệu ứng nhân tố 1 phụ thuộc mức nhân tố 2"),
            ("Ma trận SSP", "tổng bình phương & tích chéo — bản nhiều chiều của SS"),
            ("B và W", "SSP giữa nhóm (between) và trong nhóm (within)"),
            ("Wilks' lambda Λ*", "|W| / |B + W| — nhỏ ⇒ có hiệu ứng"),
        ]
        for a, b in rows:
            data.append([vt(a, size=24, color=GOLD, weight=BOLD), vt(b, size=23)])
        t = table(data, [5.2, 7.6], row_h=0.72, size=24)
        self.fit(t, top_buff=0.45)
        with self.say("Vài thuật ngữ cần nắm. Nhân tố là điều kiện thí nghiệm, mức là giá trị cụ thể của nó. "
                      "Hiệu ứng xử lý là độ lệch của nhóm so với mức chung. Tương tác nghĩa là hiệu ứng của nhân tố này thay đổi theo mức của nhân tố kia."):
            self.play(Create(t.lines), FadeIn(t.rows[0]))
            self.play(LaggedStart(*[FadeIn(r) for r in t.rows[1:4]], lag_ratio=0.4), run_time=3)
        with self.say("Trong ma-nô-va, tổng bình phương được thay bằng ma trận tổng bình phương và tích chéo, S S P. "
                      "Bê là S S P giữa các nhóm, đáp-bờ-liu là S S P trong nhóm. Và lam-đa Uyn-xơ bằng định thức đáp-bờ-liu chia định thức bê cộng đáp-bờ-liu. "
                      "Lam-đa càng nhỏ, hiệu ứng càng rõ."):
            self.play(LaggedStart(*[FadeIn(r) for r in t.rows[4:]], lag_ratio=0.4), run_time=3)
            self.play(FadeIn(row_highlight(t, 6)))
        self.clear_all()


class Short03_OneWay(Lecture):
    section_label = "3 · Mục 6.4 One-way MANOVA"

    def construct(self):
        self.set_title("Mục 6.4 — One-way MANOVA", "(6-38), (6-40), (6-42)")
        model = mt(r"\mathbf X_{\ell j}", "=", r"\boldsymbol\mu", "+", r"\boldsymbol\tau_\ell", "+", r"\mathbf e_{\ell j}", size=54)
        model[2].set_color(BLUE); model[4].set_color(GOLD); model[6].set_color(GREEN)
        asm = vt("Giả định: mẫu độc lập · chung ma trận hiệp phương sai Σ · chuẩn nhiều chiều", size=24, color=MUTED)
        dec = mt(r"\underbrace{\textstyle\sum\sum(\mathbf x_{\ell j}-\bar{\mathbf x})(\mathbf x_{\ell j}-\bar{\mathbf x})'}_{\mathbf B+\mathbf W}", "=",
                 r"\underbrace{\textstyle\sum n_\ell(\bar{\mathbf x}_\ell-\bar{\mathbf x})(\bar{\mathbf x}_\ell-\bar{\mathbf x})'}_{\mathbf B}", "+",
                 r"\underbrace{\textstyle\sum\sum(\mathbf x_{\ell j}-\bar{\mathbf x}_\ell)(\mathbf x_{\ell j}-\bar{\mathbf x}_\ell)'}_{\mathbf W}", size=36)
        dec[2].set_color(GOLD); dec[4].set_color(GREEN)
        lam = mt(r"\Lambda^*=\frac{|\mathbf W|}{|\mathbf B+\mathbf W|}", size=48, color=ACCENT)
        grp = VGroup(model, asm, dec, lam).arrange(DOWN, buff=0.45)
        self.fit(grp, top_buff=0.45)
        with self.say("Mục 6.4. Khi mỗi quan sát là một vectơ pê biến, mô hình giữ nguyên dạng, chỉ là các số hạng giờ là vectơ. "
                      "Giả định: các mẫu độc lập, cùng ma trận hiệp phương sai xích-ma, và có phân phối chuẩn nhiều chiều."):
            self.play(Write(model))
            self.play(FadeIn(asm))
        with self.say("Thay bình phương bằng tích của vectơ với chuyển vị, ta tách ma trận toàn phần thành bê, giữa các nhóm, cộng đáp-bờ-liu, trong nhóm. "
                      "Thống kê kiểm định là lam-đa Uyn-xơ, lam-đa nhỏ thì bác bỏ giả thuyết không có hiệu ứng xử lý."):
            self.play(Write(dec), run_time=2.5)
            self.play(Write(lam))
        self.clear_content()

        self.set_title("Ví dụ 6.9 — g = 3 nhóm, p = 2 biến", "tr. 304–306")
        B = mt(r"\mathbf B=\begin{bmatrix}78&-12\\-12&48\end{bmatrix}", size=40, color=GOLD)
        W = mt(r"\mathbf W=\begin{bmatrix}10&1\\1&24\end{bmatrix}", size=40, color=GREEN)
        mats = VGroup(B, W).arrange(RIGHT, buff=1.2)
        lam = mt(r"\Lambda^*=\frac{|\mathbf W|}{|\mathbf B+\mathbf W|}=\frac{239}{6215}=0.0385", size=42)
        F = mt(r"\left(\frac{1-\sqrt{\Lambda^*}}{\sqrt{\Lambda^*}}\right)\left(\frac{8-3-1}{3-1}\right)=8.19>F_{4,8}(.01)=7.01", size=38, color=GOLD)
        concl = vt("⇒ Bác bỏ H₀: các vectơ trung bình khác nhau", size=28, color=GOLD)
        grp = VGroup(mats, lam, F, concl).arrange(DOWN, buff=0.5)
        self.fit(grp, top_buff=0.5)
        with self.say("Ví dụ 6.9: ba nhóm, hai biến. Tính được ma trận bê và đáp-bờ-liu như trên màn hình. "
                      "Lam-đa bằng hai trăm ba mươi chín chia sáu nghìn hai trăm mười lăm, bằng không phẩy không ba tám năm."):
            self.play(FadeIn(mats))
            self.play(Write(lam))
        with self.say("Với hai biến, bảng 6.3 cho kiểm định ép chính xác: tám phẩy một chín, lớn hơn bảy phẩy không một. Ta bác bỏ giả thuyết không."):
            self.play(Write(F))
            self.play(FadeIn(concl))
        self.clear_all()


class Short04_TwoWay(Lecture):
    section_label = "4 · Mục 6.7 Two-way MANOVA"

    def construct(self):
        self.set_title("Mục 6.7 — Two-way MANOVA", "Mô hình hiệu ứng cố định có tương tác · (6-59)")
        m = mt(r"\mathbf X_{\ell k r}", "=", r"\boldsymbol\mu", "+", r"\boldsymbol\tau_\ell", "+", r"\boldsymbol\beta_k", "+",
               r"\boldsymbol\gamma_{\ell k}", "+", r"\mathbf e_{\ell k r}", size=56)
        for i, c in [(2, BLUE), (4, GOLD), (6, PURPLE), (8, RED), (10, GREEN)]:
            m[i].set_color(c)
        un, leg = legend(m, [4, 6, 8, 10], ["nhân tố 1 (g mức)", "nhân tố 2 (b mức)", "tương tác", "sai số N_p(0, Σ)".replace("N_p", "Nₚ")],
                         cols=2, size=24)
        idx = vt("ℓ = 1..g,  k = 1..b,  r = 1..n lần lặp ở mỗi ô", size=24, color=MUTED)
        grp = VGroup(m, idx, leg).arrange(DOWN, buff=0.45)
        self.fit(grp, top_buff=0.6)
        un, _ = legend(m, [4, 6, 8, 10], [""] * 4)
        with self.say("Giờ đến phần chính, mục 6.7. Có hai nhân tố: nhân tố một có gờ mức, nhân tố hai có bê mức, mỗi tổ hợp lặp en lần. "
                      "Vectơ quan sát bằng mức chung, cộng hiệu ứng nhân tố một tau, hiệu ứng nhân tố hai bê-ta, tương tác gam-ma, và sai số."):
            self.play(Write(m), run_time=2.5)
            self.play(Create(un), FadeIn(leg), FadeIn(idx))
        self.clear_content()

        self.set_title("Tương tác — Hình 6.3", "các đường song song ⇔ không có tương tác")
        va = [[2.0, 4.2, 1.5, 4.6], [2.6, 3.4, 2.9, 3.6], [1.4, 3.0, 0.8, 5.2]]
        vb = [[2.3, 3.5, 1.8, 4.3], [1.3, 2.5, 0.8, 3.3], [3.3, 4.5, 2.8, 5.3]]
        cols = [GOLD, BLUE, GREEN]
        names = ["Mức 1 của NT 1", "Mức 2 của NT 1", "Mức 3 của NT 1"]
        A, la, laa = interaction_axes(va, cols, names, "(a) Có tương tác")
        Bx, lb, lbb = interaction_axes(vb, cols, names, "(b) Không có tương tác")
        panel = VGroup(VGroup(A, la, laa), VGroup(Bx, lb, lbb)).arrange(RIGHT, buff=1.4)
        self.fit(panel, top_buff=0.5, grow=1.3)
        with self.say("Tương tác là gì? Ở hình bê, các đường song song: tác động của nhân tố hai như nhau ở mọi mức của nhân tố một, hiệu ứng cộng dồn. "
                      "Ở hình a, các đường cắt nhau: có tương tác, và khi đó hiệu ứng riêng của từng nhân tố không còn diễn giải rõ ràng."):
            self.play(FadeIn(A), FadeIn(Bx))
            self.play(LaggedStart(*[Create(l) for l in lb], lag_ratio=0.3), FadeIn(lbb), run_time=2)
            self.play(LaggedStart(*[Create(l) for l in la], lag_ratio=0.3), FadeIn(laa), run_time=2)
        self.clear_content()

        self.set_title("Bảng MANOVA hai nhân tố và các kiểm định", "(6-61) – (6-69)")
        t = table([
            ["Nguồn", "Ma trận SSP", "d.f."],
            ["Nhân tố 1", mt(r"\sum_\ell bn(\bar{\mathbf x}_{\ell\cdot}-\bar{\mathbf x})(\cdot)'", size=28, color=GOLD), mt("g-1", size=28)],
            ["Nhân tố 2", mt(r"\sum_k gn(\bar{\mathbf x}_{\cdot k}-\bar{\mathbf x})(\cdot)'", size=28, color=PURPLE), mt("b-1", size=28)],
            ["Tương tác", mt(r"\sum_\ell\sum_k n(\bar{\mathbf x}_{\ell k}-\bar{\mathbf x}_{\ell\cdot}-\bar{\mathbf x}_{\cdot k}+\bar{\mathbf x})(\cdot)'", size=28, color=RED), mt("(g-1)(b-1)", size=28)],
            ["Phần dư", mt(r"\sum_\ell\sum_k\sum_r(\mathbf x_{\ell kr}-\bar{\mathbf x}_{\ell k})(\cdot)'", size=28, color=GREEN), mt("gb(n-1)", size=28)],
        ], [2.6, 7.4, 2.4], row_h=0.8, size=24)
        lam = mt(r"\Lambda^*=\frac{|\mathbf{SSP}_{res}|}{|\mathbf{SSP}_{H}+\mathbf{SSP}_{res}|},\quad H\in\{int,\ fac1,\ fac2\}", size=36, color=ACCENT)
        order = vt("Thứ tự: kiểm định TƯƠNG TÁC trước → nếu không có, mới kiểm định nhân tố 1, nhân tố 2", size=24, color=GOLD)
        grp = VGroup(t, lam, order).arrange(DOWN, buff=0.4)
        self.fit(grp, top_buff=0.35)
        with self.say("Tổng quát hoá a-nô-va hai nhân tố, ma trận toàn phần được tách thành bốn ma trận: nhân tố một, nhân tố hai, tương tác và phần dư, "
                      "với bậc tự do tương ứng."):
            self.play(Create(t.lines), FadeIn(t.rows[0]))
            self.play(LaggedStart(*[FadeIn(r) for r in t.rows[1:]], lag_ratio=0.3), run_time=2.5)
        with self.say("Mỗi kiểm định dùng lam-đa Uyn-xơ: định thức S S P phần dư chia định thức của S S P hiệu ứng cộng S S P phần dư. "
                      "Quan trọng: luôn kiểm định tương tác trước. Nếu có tương tác, nên phân tích từng biến và vẽ đồ thị tương tác; "
                      "nếu không, mới kiểm định hai nhân tố. Với mẫu lớn, dùng xấp xỉ khi bình phương của Bác-lét."):
            self.play(Write(lam))
            self.play(FadeIn(order, shift=UP * 0.2))
        self.clear_all()


class Short05_Example613(Lecture):
    section_label = "4 · Ví dụ 6.13"

    def construct(self):
        self.set_title("Ví dụ 6.13 — Màng nhựa", "tr. 318–323")
        ctx = bullet_list([
            mix("Phản hồi p = 3:", "$X_1$", "độ bền xé,", "$X_2$", "độ bóng,", "$X_3$", "độ mờ", size=26),
            vt("Nhân tố 1: tốc độ đùn (thấp / cao) · Nhân tố 2: lượng phụ gia (thấp / cao)", size=26),
            vt("g = b = 2, lặp n = 5 ⇒ 20 quan sát", size=26),
        ], gap=0.3)
        t = table([
            ["Hiệu ứng", "Wilks' Λ*", "F (3, 14)", "Kết luận (F₃,₁₄(.05) = 3.34)"],
            [vt("Tương tác", size=24, color=RED), mt(r"\frac{275.71}{354.79}=.7771", size=28), mt("1.34", size=30), vt("Không bác bỏ — không có tương tác", size=21)],
            [vt("Tốc độ đùn", size=24, color=GOLD), mt(r"\frac{275.71}{722.02}=.3819", size=28), mt("7.55", size=30), vt("Bác bỏ — có hiệu ứng", size=21, color=GOLD)],
            [vt("Phụ gia", size=24, color=PURPLE), mt(r"\frac{275.71}{527.13}=.5230", size=28), mt("4.26", size=30), vt("Bác bỏ — có hiệu ứng", size=21, color=PURPLE)],
        ], [2.6, 3.4, 1.8, 5.0], row_h=1.0, size=22)
        grp = VGroup(ctx, t).arrange(DOWN, buff=0.5)
        self.fit(grp, top_buff=0.4)
        with self.say("Ví dụ 6.13. Người ta đo ba biến của màng nhựa: độ bền xé, độ bóng và độ mờ, ở hai mức tốc độ đùn và hai mức phụ gia, "
                      "mỗi tổ hợp lặp năm lần."):
            self.play(LaggedStart(*[FadeIn(r) for r in ctx], lag_ratio=0.4), run_time=2)
        with self.say("Bước một, kiểm định tương tác: lam-đa bằng không phẩy bảy bảy bảy một, ép bằng một phẩy ba tư, nhỏ hơn ba phẩy ba tư. "
                      "Không bác bỏ, tức là không có tương tác."):
            self.play(Create(t.lines), FadeIn(t.rows[0]))
            self.play(FadeIn(t.rows[1]))
        with self.say("Bước hai, hiệu ứng chính: tốc độ đùn có ép bảy phẩy năm lăm, phụ gia có ép bốn phẩy hai sáu, đều lớn hơn ba phẩy ba tư. "
                      "Cả hai đều có ý nghĩa."):
            self.play(FadeIn(t.rows[2]))
            self.play(FadeIn(t.rows[3]))
        concl = boxed(vt("Kết luận: tốc độ đùn và lượng phụ gia đều ảnh hưởng đến các phản hồi,\ntheo cách cộng dồn (không có tương tác).",
                         size=26, color=GOLD, align=ORIGIN), color=GOLD)
        concl.to_edge(DOWN, buff=0.45)
        self.play(FadeOut(ctx))
        self.play(t.animate.next_to(self.title_mob, DOWN, buff=0.5))
        with self.say("Kết luận của sách: cả tốc độ đùn và lượng phụ gia đều ảnh hưởng đến các phản hồi, và chúng tác động theo cách cộng dồn."):
            self.play(FadeIn(concl, shift=UP * 0.2))
        self.clear_all()

        steps = bullet_list([
            vt("1. Lập bảng MANOVA: SSP nhân tố 1, nhân tố 2, tương tác, phần dư", size=28),
            vt("2. Kiểm định tương tác trước bằng Wilks' lambda", size=28),
            vt("3. Không có tương tác ⇒ kiểm định các hiệu ứng chính", size=28),
            vt("4. Kết luận gắn với ngữ cảnh; kiểm tra giả định qua phần dư", size=28),
        ], gap=0.4)
        head = vt("Tóm tắt quy trình", size=40, color=ACCENT, weight=BOLD)
        g = VGroup(head, steps).arrange(DOWN, buff=0.6)
        with self.say("Tóm lại, quy trình gồm bốn bước: lập bảng ma-nô-va, kiểm định tương tác trước, rồi đến hiệu ứng chính, và kết luận gắn với ngữ cảnh. "
                      "Cảm ơn các em đã theo dõi."):
            self.play(FadeIn(head))
            self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.2) for r in steps], lag_ratio=0.4), run_time=3)
        self.play(FadeOut(g))
