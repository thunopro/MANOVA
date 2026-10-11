"""Phần 3: Mục 6.4 — One-way MANOVA (sách tr. 296-308), Ví dụ 6.9 và 6.10."""
from common import *


class S04_OneWayModel(Lecture):
    section_label = "Phần 3 · Mục 6.4 One-way MANOVA"

    def construct(self):
        card = self.section_card("PHẦN 3 · MỤC 6.4", "So sánh nhiều vectơ trung bình",
                                 "One-Way MANOVA — sách tr. 296–308")
        with self.say("Phần ba. Mục 6.4: so sánh nhiều vectơ trung bình tổng thể, hay ma-nô-va một nhân tố."):
            self.play(FadeIn(card, shift=UP * 0.3))
        self.play(FadeOut(card))

        self.set_title("Cấu trúc dữ liệu", "(6-31)")
        rows = VGroup(
            mix("Tổng thể 1:", r"$\mathbf X_{11},\ \mathbf X_{12},\ \dots,\ \mathbf X_{1n_1}$", size=30),
            mix("Tổng thể 2:", r"$\mathbf X_{21},\ \mathbf X_{22},\ \dots,\ \mathbf X_{2n_2}$", size=30),
            mt(r"\vdots", size=40),
            mix("Tổng thể g:", r"$\mathbf X_{g1},\ \mathbf X_{g2},\ \dots,\ \mathbf X_{gn_g}$", size=30),
        ).arrange(DOWN, buff=0.3)
        vec = mt(r"\mathbf X_{\ell j}=\begin{bmatrix}X_{\ell j1}\\X_{\ell j2}\\\vdots\\X_{\ell jp}\end{bmatrix}", size=40, color=ACCENT)
        vlab = vt("mỗi quan sát là một vectơ p biến", size=22, color=ACCENT)
        right = VGroup(vec, vlab).arrange(DOWN, buff=0.25)
        grp = VGroup(rows, right).arrange(RIGHT, buff=1.2)
        self.fit(grp, top_buff=0.7)
        with self.say("Khi cần so sánh nhiều hơn hai tổng thể, ta thu thập mẫu ngẫu nhiên từ mỗi tổng thể trong gờ tổng thể, "
                      "sắp xếp như sau. Điểm khác so với a-nô-va: mỗi quan sát X đậm l j bây giờ là một vectơ gồm pê biến."):
            self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.3) for r in rows], lag_ratio=0.3), run_time=2.5)
            self.play(FadeIn(right))
        self.clear_content()

        self.set_title("Giả định của One-way MANOVA", "Assumptions about the Structure of the Data, tr. 296–297")
        items = bullet_list([
            mix("1.", r"$\mathbf X_{\ell 1},\dots,\mathbf X_{\ell n_\ell}$", "là mẫu ngẫu nhiên cỡ", "$n_\\ell$",
                "từ tổng thể có trung bình", r"$\boldsymbol\mu_\ell$", size=27),
            vt("    Các mẫu từ những tổng thể khác nhau thì độc lập.", size=27),
            mix("2.", "Mọi tổng thể có chung ma trận hiệp phương sai", r"$\boldsymbol\Sigma$", size=27),
            vt("3. Mỗi tổng thể có phân phối chuẩn nhiều chiều.", size=27),
        ], gap=0.4)
        note = boxed(vt("Giả định 3 có thể nới lỏng nhờ định lý giới hạn trung tâm khi các cỡ mẫu nℓ lớn.",
                        size=24, color=GOLD), color=GOLD)
        grp = VGroup(items, note).arrange(DOWN, buff=0.7)
        self.fit(grp, top_buff=0.7)
        with self.say("Ma-nô-va một nhân tố cần ba giả định. Một: từ mỗi tổng thể l ta có một mẫu ngẫu nhiên cỡ n l, "
                      "và các mẫu từ những tổng thể khác nhau thì độc lập với nhau."):
            self.play(FadeIn(items[0]), FadeIn(items[1]))
        with self.say("Hai: mọi tổng thể có chung một ma trận hiệp phương sai xích-ma. Ba: mỗi tổng thể có phân phối chuẩn nhiều chiều."):
            self.play(FadeIn(items[2]))
            self.play(FadeIn(items[3]))
        with self.say("Theo sách, điều kiện ba có thể nới lỏng nhờ định lý giới hạn trung tâm, khi các cỡ mẫu đủ lớn."):
            self.play(FadeIn(note, shift=UP * 0.2))
        self.clear_content()

        self.set_title("Mô hình MANOVA so sánh g vectơ trung bình", "(6-38)")
        model = mt(r"\mathbf X_{\ell j}", "=", r"\boldsymbol\mu", "+", r"\boldsymbol\tau_\ell", "+", r"\mathbf e_{\ell j}", size=60)
        model[2].set_color(BLUE); model[4].set_color(GOLD); model[6].set_color(GREEN)
        idx = mt(r"j=1,2,\dots,n_\ell,\qquad \ell=1,2,\dots,g", size=34, color=MUTED)
        un, leg = legend(model, [2, 4, 6], ["mức chung (overall level)", "hiệu ứng xử lý thứ ℓ",
                                            "sai số độc lập, chuẩn p chiều N(0, Σ)"], cols=1)
        cons = mix("Ràng buộc:", r"$\sum_{\ell=1}^{g} n_\ell\boldsymbol\tau_\ell=\mathbf 0$", size=28, color=GOLD)
        grp = VGroup(model, idx, leg, cons).arrange(DOWN, buff=0.45)
        self.fit(grp, top_buff=0.6)
        un, _ = legend(model, [2, 4, 6], ["", "", ""], cols=1)
        with self.say("Song song với a-nô-va, mô hình ma-nô-va viết: vectơ quan sát X l j bằng vectơ mức chung muy, cộng hiệu ứng xử lý "
                      "tau l, cộng sai số e l j. Các sai số độc lập, có phân phối chuẩn pê chiều, trung bình không, hiệp phương sai xích-ma."):
            self.play(Write(model), FadeIn(idx))
            self.play(Create(un), FadeIn(leg))
        with self.say("Ràng buộc vẫn là tổng n l nhân tau l bằng vectơ không."):
            self.play(FadeIn(cons))
        rem = boxed(vt("Mỗi thành phần của Xℓj thỏa mô hình ANOVA một biến (6-33).\n"
                       "Sai số giữa các thành phần có tương quan, nhưng Σ như nhau ở mọi tổng thể.", size=24, align=ORIGIN), color=ACCENT)
        rem.next_to(leg, DOWN, buff=0.5)
        with self.say("Theo mô hình này, mỗi thành phần của vectơ quan sát thỏa mãn mô hình a-nô-va một biến. Chỗ khác biệt là: "
                      "sai số giữa các thành phần có tương quan với nhau, nhưng ma trận hiệp phương sai xích-ma là như nhau ở mọi tổng thể."):
            self.play(FadeOut(cons), FadeIn(rem, shift=UP * 0.2))
        self.clear_content()

        self.set_title("Phân tích vectơ quan sát", "(6-39)")
        dec = mt(r"\mathbf x_{\ell j}", "=", r"\bar{\mathbf x}", "+", r"(\bar{\mathbf x}_\ell-\bar{\mathbf x})", "+",
                 r"(\mathbf x_{\ell j}-\bar{\mathbf x}_\ell)", size=54)
        dec[2].set_color(BLUE); dec[4].set_color(GOLD); dec[6].set_color(GREEN)
        un, leg = legend(dec, [2, 4, 6], ["trung bình mẫu chung — ước lượng của μ",
                                          "ước lượng của hiệu ứng xử lý τℓ", "phần dư — ước lượng của sai số eℓj"], cols=1)
        grp = VGroup(dec, leg).arrange(DOWN, buff=0.6)
        self.fit(grp, top_buff=0.8)
        un, _ = legend(dec, [2, 4, 6], ["", "", ""], cols=1)
        with self.say("Tương tự sáu ba tư, vectơ quan sát được phân tích thành: vectơ trung bình mẫu chung, cộng ước lượng hiệu ứng xử lý, "
                      "cộng vectơ phần dư. Mọi thứ giống hệt trước, chỉ là giờ mỗi số hạng là một vectơ."):
            self.play(Write(dec), run_time=2.5)
            self.play(Create(un), FadeIn(leg))
        self.clear_content()

        self.set_title("Từ bình phương sang ma trận tích chéo", "(6-40)")
        step1 = mt(r"(\mathbf x_{\ell j}-\bar{\mathbf x})(\mathbf x_{\ell j}-\bar{\mathbf x})'", "=",
                   r"\big[(\mathbf x_{\ell j}-\bar{\mathbf x}_\ell)+(\bar{\mathbf x}_\ell-\bar{\mathbf x})\big]"
                   r"\big[(\mathbf x_{\ell j}-\bar{\mathbf x}_\ell)+(\bar{\mathbf x}_\ell-\bar{\mathbf x})\big]'", size=34)
        step2 = mt(r"=(\mathbf x_{\ell j}-\bar{\mathbf x}_\ell)(\mathbf x_{\ell j}-\bar{\mathbf x}_\ell)'",
                   r"+(\mathbf x_{\ell j}-\bar{\mathbf x}_\ell)(\bar{\mathbf x}_\ell-\bar{\mathbf x})'"
                   r"+(\bar{\mathbf x}_\ell-\bar{\mathbf x})(\mathbf x_{\ell j}-\bar{\mathbf x}_\ell)'",
                   r"+(\bar{\mathbf x}_\ell-\bar{\mathbf x})(\bar{\mathbf x}_\ell-\bar{\mathbf x})'", size=34)
        why = mix("Cộng theo j: hai số hạng giữa bằng 0 vì", r"$\sum_{j=1}^{n_\ell}(\mathbf x_{\ell j}-\bar{\mathbf x}_\ell)=\mathbf 0$",
                  size=24, color=MUTED)
        grp = VGroup(step1, step2, why).arrange(DOWN, buff=0.35)
        self.fit(grp, top_buff=0.4)
        with self.say("Bây giờ, thay vì bình phương một số, ta lấy tích của vectơ độ lệch với chính chuyển vị của nó. "
                      "Tích x l j trừ x ngang, nhân chuyển vị, được tách thành bốn số hạng."):
            self.play(Write(step1), run_time=2)
            self.play(Write(step2), run_time=2.5)
        with self.say("Khi cộng theo j, hai số hạng ở giữa bằng ma trận không, vì tổng các độ lệch so với trung bình nhóm luôn bằng không."):
            self.play(FadeIn(why))
            self.play(step2[1].animate.set_opacity(0.25))
        self.play(FadeOut(grp))

        main = mt(r"\sum_{\ell=1}^{g}\sum_{j=1}^{n_\ell}(\mathbf x_{\ell j}-\bar{\mathbf x})(\mathbf x_{\ell j}-\bar{\mathbf x})'", "=",
                  r"\sum_{\ell=1}^{g}n_\ell(\bar{\mathbf x}_\ell-\bar{\mathbf x})(\bar{\mathbf x}_\ell-\bar{\mathbf x})'", "+",
                  r"\sum_{\ell=1}^{g}\sum_{j=1}^{n_\ell}(\mathbf x_{\ell j}-\bar{\mathbf x}_\ell)(\mathbf x_{\ell j}-\bar{\mathbf x}_\ell)'",
                  size=34)
        main[2].set_color(GOLD); main[4].set_color(GREEN)
        b = VGroup(
            BraceLabel(main[0], r"\mathbf B+\mathbf W", brace_direction=DOWN, font_size=32),
            BraceLabel(main[2], r"\mathbf B", brace_direction=DOWN, font_size=32),
            BraceLabel(main[4], r"\mathbf W", brace_direction=DOWN, font_size=32),
        )
        names = VGroup(vt("tổng SSP toàn phần\n(hiệu chỉnh)", size=20, align=ORIGIN),
                       vt("SSP xử lý\n(Between)", size=20, color=GOLD, align=ORIGIN),
                       vt("SSP phần dư\n(Within)", size=20, color=GREEN, align=ORIGIN))
        for n, br in zip(names, b):
            n.next_to(br, DOWN, buff=0.15)
        grp = VGroup(main, b, names)
        self.fit(grp, top_buff=0.6)
        with self.say("Cộng theo cả l và j, ta được đẳng thức sáu bốn mươi: ma trận tổng bình phương và tích chéo toàn phần, "
                      "bằng ma trận của xử lý, hay giữa các nhóm, ký hiệu bê, cộng ma trận phần dư, hay trong các nhóm, ký hiệu đáp-bờ-liu."):
            self.play(Write(main), run_time=3)
            self.play(FadeIn(b), FadeIn(names))
        Wf = mt(r"\mathbf W=\sum_{\ell=1}^{g}\sum_{j=1}^{n_\ell}(\mathbf x_{\ell j}-\bar{\mathbf x}_\ell)(\mathbf x_{\ell j}-\bar{\mathbf x}_\ell)'"
                r"=(n_1-1)\mathbf S_1+(n_2-1)\mathbf S_2+\cdots+(n_g-1)\mathbf S_g", size=34, color=GREEN)
        wl = mix("(6-41)", r"$\mathbf S_\ell$", ": ma trận hiệp phương sai mẫu của nhóm ℓ — tổng quát hoá của",
                 r"$(n_1+n_2-2)\mathbf S_{pooled}$", size=20, color=MUTED)
        wg = VGroup(Wf, wl).arrange(DOWN, buff=0.2).to_edge(DOWN, buff=0.6)
        if wg.width > 13: wg.scale_to_fit_width(13)
        with self.say("Đặc biệt, ma trận đáp-bờ-liu có thể tính nhanh: bằng n một trừ một nhân S một, cộng n hai trừ một nhân S hai, "
                      "và cứ thế, với S l là ma trận hiệp phương sai mẫu của nhóm l. Đây là công thức sáu bốn mốt, tổng quát hoá ma trận "
                      "gộp của trường hợp hai mẫu. Ma trận đáp-bờ-liu đóng vai trò chủ đạo trong kiểm định hiệu ứng xử lý."):
            self.play(FadeIn(wg, shift=UP * 0.2))
        self.clear_content()

        self.set_title("Bảng MANOVA so sánh các vectơ trung bình", "sách tr. 302")
        t = table([
            ["Nguồn biến thiên", "Ma trận SSP", "Bậc tự do"],
            ["Xử lý", mt(r"\mathbf B=\sum_{\ell}n_\ell(\bar{\mathbf x}_\ell-\bar{\mathbf x})(\bar{\mathbf x}_\ell-\bar{\mathbf x})'", size=30, color=GOLD), mt("g-1", size=30)],
            ["Phần dư (Error)", mt(r"\mathbf W=\sum_{\ell}\sum_{j}(\mathbf x_{\ell j}-\bar{\mathbf x}_\ell)(\mathbf x_{\ell j}-\bar{\mathbf x}_\ell)'", size=30, color=GREEN), mt(r"\sum n_\ell-g", size=30)],
            ["Toàn phần (hiệu chỉnh)", mt(r"\mathbf B+\mathbf W=\sum_{\ell}\sum_{j}(\mathbf x_{\ell j}-\bar{\mathbf x})(\mathbf x_{\ell j}-\bar{\mathbf x})'", size=30), mt(r"\sum n_\ell-1", size=30)],
        ], [3.4, 7.4, 2.2], row_h=0.9, size=24)
        cmp = mix("Giống bảng ANOVA, chỉ thay", r"$(\bar x_\ell-\bar x)^2$", "bằng", r"$(\bar{\mathbf x}_\ell-\bar{\mathbf x})(\bar{\mathbf x}_\ell-\bar{\mathbf x})'$",
                  size=26, color=ACCENT)
        grp = VGroup(t, cmp).arrange(DOWN, buff=0.6)
        self.fit(grp, top_buff=0.5)
        with self.say("Ta tóm tắt trong bảng ma-nô-va. Bảng này có đúng hình thức của bảng a-nô-va, từng thành phần một."):
            self.play(Create(t.lines), FadeIn(t.rows[0]))
            self.play(LaggedStart(*[FadeIn(r) for r in t.rows[1:]], lag_ratio=0.4), run_time=2)
        with self.say("Chỉ khác ở chỗ bình phương của các số vô hướng được thay bằng tích của vectơ với chuyển vị của nó. "
                      "Bậc tự do thì giữ nguyên như trường hợp một biến."):
            self.play(FadeIn(cmp, shift=UP * 0.2))
        self.clear_content()

        self.set_title("Lambda của Wilks", "(6-42)")
        h0 = mt(r"H_0:\ \boldsymbol\tau_1=\boldsymbol\tau_2=\cdots=\boldsymbol\tau_g=\mathbf 0", size=42, color=GOLD)
        lam = mt(r"\Lambda^*=\frac{|\mathbf W|}{|\mathbf B+\mathbf W|}=",
                 r"\frac{\left|\sum_{\ell}\sum_{j}(\mathbf x_{\ell j}-\bar{\mathbf x}_\ell)(\mathbf x_{\ell j}-\bar{\mathbf x}_\ell)'\right|}"
                 r"{\left|\sum_{\ell}\sum_{j}(\mathbf x_{\ell j}-\bar{\mathbf x})(\mathbf x_{\ell j}-\bar{\mathbf x})'\right|}", size=44)
        rule = boxed(mix("Bác bỏ", "$H_0$", "nếu", r"$\Lambda^*$", "quá NHỎ", size=30, color=GOLD), color=GOLD)
        grp = VGroup(h0, lam, rule).arrange(DOWN, buff=0.55)
        self.fit(grp, top_buff=0.5)
        with self.say("Giả thuyết không có hiệu ứng xử lý được kiểm định bằng cách so sánh độ lớn tương đối của ma trận xử lý và ma trận phần dư. "
                      "Một cách là dùng phương sai tổng quát, tức là định thức."):
            self.play(Write(h0))
        with self.say("Ta tính lam-đa sao, bằng định thức của đáp-bờ-liu, chia định thức của bê cộng đáp-bờ-liu. "
                      "Đại lượng này do Uyn-xơ đề xuất, nên gọi là lam-đa Uyn-xơ. Ta bác bỏ giả thuyết không nếu lam-đa quá nhỏ."):
            self.play(Write(lam), run_time=2.5)
            self.play(FadeIn(rule))
        self.play(FadeOut(grp))
        pts = bullet_list([
            mix("Tương ứng với dạng (6-37) của kiểm định F:", r"$\dfrac{SS_{res}}{SS_{res}+SS_{tr}}$", size=26),
            vt("Λ* nằm giữa 0 và 1. Hiệu ứng xử lý càng mạnh thì |B + W|\ncàng lớn so với |W|  ⇒  Λ* càng nhỏ.", size=26),
            vt("Liên hệ với kiểm định tỉ số hợp lý (likelihood ratio).", size=26),
            mix("Dạng trị riêng:", r"$\Lambda^*=\prod_{i=1}^{s}\dfrac{1}{1+\hat\lambda_i}$", ",", r"$\hat\lambda_i$",
                "là trị riêng của", r"$\mathbf W^{-1}\mathbf B$", size=26),
            vt("Thống kê khác: Pillai's trace, Lawley–Hotelling trace, Roy's largest root\n(với cỡ mẫu lớn: về cơ bản tương đương).",
               size=24, color=MUTED),
        ], gap=0.45)
        self.fit(pts, top_buff=0.6, grow=1.2)
        with self.say("Vài điểm cần hiểu. Lam-đa sao tương ứng với dạng tương đương sáu ba bảy của kiểm định ép trong a-nô-va. "
                      "Giá trị của nó nằm giữa không và một: hiệu ứng xử lý càng mạnh thì ma trận bê càng lớn, và lam-đa càng nhỏ."):
            self.play(FadeIn(pts[0]))
            self.play(FadeIn(pts[1]))
        with self.say("Lam-đa Uyn-xơ thuận tiện và có liên hệ với tiêu chuẩn tỉ số hợp lý. Theo chú thích của sách, nó cũng viết được qua "
                      "các trị riêng của đáp-bờ-liu nghịch đảo nhân bê. Các phần mềm còn in thêm vết Pi-lai, vết Lo-lây Hô-tơ-linh và "
                      "nghiệm lớn nhất của Roi. Với mẫu lớn, các thống kê này về cơ bản tương đương."):
            self.play(FadeIn(pts[2]))
            self.play(FadeIn(pts[3]))
            self.play(FadeIn(pts[4]))
        self.clear_content()

        self.set_title("Bảng 6.3 — Phân phối chính xác của Wilks' lambda", "Table 6.3, tr. 303 (dữ liệu chuẩn nhiều chiều)")
        def fr(a, b, c, d):
            return mt(rf"\left(\frac{{{a}}}{{{b}}}\right)\left(\frac{{{c}}}{{{d}}}\right)", size=32)
        t = table([
            ["Số biến", "Số nhóm", "Thống kê", "Phân phối"],
            [mt("p=1", size=32), mt(r"g\ge 2", size=32), fr(r"\sum n_\ell-g", "g-1", r"1-\Lambda^*", r"\Lambda^*"), mt(r"F_{g-1,\ \sum n_\ell-g}", size=32, color=GOLD)],
            [mt("p=2", size=32), mt(r"g\ge 2", size=32), fr(r"\sum n_\ell-g-1", "g-1", r"1-\sqrt{\Lambda^*}", r"\sqrt{\Lambda^*}"), mt(r"F_{2(g-1),\ 2(\sum n_\ell-g-1)}", size=32, color=GOLD)],
            [mt(r"p\ge 1", size=32), mt("g=2", size=32), fr(r"\sum n_\ell-p-1", "p", r"1-\Lambda^*", r"\Lambda^*"), mt(r"F_{p,\ \sum n_\ell-p-1}", size=32, color=GOLD)],
            [mt(r"p\ge 1", size=32), mt("g=3", size=32), fr(r"\sum n_\ell-p-2", "p", r"1-\sqrt{\Lambda^*}", r"\sqrt{\Lambda^*}"), mt(r"F_{2p,\ 2(\sum n_\ell-p-2)}", size=32, color=GOLD)],
        ], [1.8, 1.8, 5.2, 4.2], row_h=1.15, size=24)
        self.fit(t, top_buff=0.4)
        with self.say("Phân phối chính xác của lam-đa sao đã được tìm ra cho một số trường hợp đặc biệt, liệt kê trong bảng 6.3. "
                      "Mỗi dòng cho một hàm của lam-đa có phân phối ép chính xác."):
            self.play(Create(t.lines), FadeIn(t.rows[0]))
            self.play(LaggedStart(*[FadeIn(r) for r in t.rows[1:]], lag_ratio=0.3), run_time=2.5)
        hl = row_highlight(t, 2)
        with self.say("Ví dụ, khi có hai biến, với số nhóm bất kỳ, ta dùng căn bậc hai của lam-đa, và thống kê có phân phối ép với "
                      "hai nhân gờ trừ một, và hai nhân tổng n l trừ gờ trừ một bậc tự do. Dòng này sẽ dùng cho ví dụ 6.9."):
            self.play(FadeIn(hl))
        hl2 = row_highlight(t, 4, color=ACCENT)
        with self.say("Còn khi có ba nhóm, với số biến bất kỳ, ta dùng dòng cuối. Dòng này sẽ dùng cho ví dụ 6.10."):
            self.play(FadeIn(hl2))
        self.clear_content()

        self.set_title("Xấp xỉ Bartlett khi cỡ mẫu lớn", "(6-43), (6-44)")
        f1 = mt(r"-\left(n-1-\frac{p+g}{2}\right)\ln\Lambda^*", "=", r"-\left(n-1-\frac{p+g}{2}\right)\ln\left(\frac{|\mathbf W|}{|\mathbf B+\mathbf W|}\right)", size=40)
        d1 = mix("xấp xỉ phân phối", r"$\chi^2$", "với", r"$p(g-1)$", "bậc tự do,  khi", r"$\sum n_\ell=n$", "lớn", size=26, color=MUTED)
        f2 = mix("Bác bỏ", "$H_0$", "nếu", r"$-\left(n-1-\frac{p+g}{2}\right)\ln\left(\frac{|\mathbf W|}{|\mathbf B+\mathbf W|}\right)>\chi^2_{p(g-1)}(\alpha)$", size=28, color=GOLD)
        grp = VGroup(f1, d1, f2).arrange(DOWN, buff=0.55)
        self.fit(grp, top_buff=0.7)
        with self.say("Với các trường hợp khác, và khi cỡ mẫu lớn, Bác-lét đã chỉ ra một xấp xỉ: nếu giả thuyết không đúng và tổng cỡ mẫu "
                      "en lớn, thì âm của en trừ một trừ pê cộng gờ chia hai, nhân với lốc-a-rít của lam-đa, có phân phối xấp xỉ "
                      "khi bình phương với pê nhân gờ trừ một bậc tự do."):
            self.play(Write(f1), run_time=2.5)
            self.play(FadeIn(d1))
        with self.say("Vậy ta bác bỏ giả thuyết không ở mức an-pha nếu đại lượng này lớn hơn phân vị trên an-pha của phân phối khi bình phương."):
            self.play(Write(f2), run_time=2)
        self.clear_all()


class S05_Example69(Lecture):
    section_label = "Phần 3 · Ví dụ 6.9"

    def construct(self):
        self.set_title("Ví dụ 6.9 — Bảng MANOVA và Wilks' lambda", "Example 6.9, tr. 304–306 · g = 3, p = 2")
        def col(*vs):
            return VGroup(*[mt(rf"\begin{{bmatrix}}{a}\\{b}\end{{bmatrix}}", size=34) for a, b in vs]).arrange(RIGHT, buff=0.3)
        g1 = col((9, 3), (6, 2), (9, 7)); g2 = col((0, 4), (2, 0)); g3 = col((3, 8), (1, 9), (2, 7))
        labs = [vt(f"Nhóm {i}", size=22, color=c) for i, c in [(1, GOLD), (2, BLUE), (3, GREEN)]]
        rows = VGroup(*[VGroup(l, g).arrange(RIGHT, buff=0.4) for l, g in zip(labs, [g1, g2, g3])]).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        means = VGroup(
            mt(r"\bar{\mathbf x}_1=\begin{bmatrix}8\\4\end{bmatrix}", size=34),
            mt(r"\bar{\mathbf x}_2=\begin{bmatrix}1\\2\end{bmatrix}", size=34),
            mt(r"\bar{\mathbf x}_3=\begin{bmatrix}2\\8\end{bmatrix}", size=34),
        )
        for m, r in zip(means, rows):
            m.next_to(r, RIGHT, buff=1.0)
        means.set_x(rows.get_right()[0] + 2.0)
        grand = mt(r"\bar{\mathbf x}=\begin{bmatrix}4\\5\end{bmatrix}", size=38, color=BLUE)
        grp = VGroup(rows, means, grand)
        grand.next_to(means, RIGHT, buff=1.0)
        self.fit(grp, top_buff=0.6, grow=1.4)
        with self.say("Bây giờ làm ví dụ 6.9. Ta lấy lại dữ liệu ví dụ 6.7, nhưng mỗi quan sát có thêm một biến thứ hai. "
                      "Cỡ mẫu vẫn là ba, hai và ba. Mỗi quan sát giờ là một vectơ hai thành phần."):
            self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.3) for r in rows], lag_ratio=0.3), run_time=2.5)
        with self.say("Vectơ trung bình các nhóm là tám bốn, một hai, và hai tám. Vectơ trung bình chung là bốn, năm."):
            self.play(LaggedStart(*[FadeIn(m) for m in means], lag_ratio=0.3))
            self.play(Write(grand))
        self.clear_content()

        def arrays(obs, mean, trt, res, size=34):
            parts = [mt(rf"\begin{{pmatrix}}{a}\end{{pmatrix}}", size=size, color=c)
                     for a, c in [(obs, FG), (mean, BLUE), (trt, GOLD), (res, GREEN)]]
            ops = [mt(o, size=40) for o in ("=", "+", "+")]
            return VGroup(parts[0], ops[0], parts[1], ops[1], parts[2], ops[2], parts[3]).arrange(RIGHT, buff=0.25)
        v1 = arrays(r"9&6&9\\0&2\\3&1&2", r"4&4&4\\4&4\\4&4&4", r"4&4&4\\-3&-3\\-2&-2&-2", r"1&-2&1\\-1&1\\1&-1&0")
        v2 = arrays(r"3&2&7\\4&0\\8&9&7", r"5&5&5\\5&5\\5&5&5", r"-1&-1&-1\\-3&-3\\3&3&3", r"-1&-2&3\\2&-2\\0&1&-1")
        l1 = vt("Biến 1 (đã có ở Ví dụ 6.7)", size=24, color=MUTED)
        l2 = vt("Biến 2", size=24, color=MUTED)
        s1 = mt(r"216=128+78+10\quad\Rightarrow\quad SS_{cor}=216-128=88", size=32)
        s2 = mt(r"272=200+48+24\quad\Rightarrow\quad SS_{cor}=272-200=72", size=32)
        grp = VGroup(l1, v1, s1, l2, v2, s2).arrange(DOWN, buff=0.25)
        for l in (l1, l2):
            l.align_to(grp, LEFT)
        self.fit(grp, top_buff=0.3)
        with self.say("Với biến thứ nhất, ta đã có phân tích từ ví dụ 6.7: hai trăm mười sáu bằng một trăm hai mươi tám, cộng bảy mươi tám, "
                      "cộng mười. Tổng bình phương hiệu chỉnh là tám mươi tám."):
            self.play(FadeIn(l1), FadeIn(v1))
            self.play(Write(s1))
        with self.say("Lặp lại cho biến thứ hai. Trung bình chung là năm, hiệu ứng xử lý của ba nhóm là âm một, âm ba và ba. "
                      "Ta được hai trăm bảy mươi hai bằng hai trăm, cộng bốn mươi tám, cộng hai mươi bốn. Tổng hiệu chỉnh là bảy mươi hai."):
            self.play(FadeIn(l2), FadeIn(v2))
            self.play(Write(s2))
        self.clear_content()

        self.set_title("Ví dụ 6.9 — Tính các tích chéo", "nhân từng phần tử tương ứng của hai biến rồi cộng lại")
        cp = VGroup(
            mix("Trung bình:", r"$4(5)+4(5)+\cdots+4(5)=8(4)(5)=160$", size=26, color=BLUE),
            mix("Xử lý:", r"$3(4)(-1)+2(-3)(-3)+3(-2)(3)=-12$", size=26, color=GOLD),
            mix("Phần dư:", r"$1(-1)+(-2)(-2)+1(3)+(-1)(2)+\cdots+0(-1)=1$", size=26, color=GREEN),
            mix("Toàn phần:", r"$9(3)+6(2)+9(7)+0(4)+\cdots+2(7)=149$", size=26),
            mix("Toàn phần hiệu chỉnh:", r"$149-160=-11$", size=26, color=ACCENT),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        self.fit(cp, top_buff=0.6, grow=1.2)
        with self.say("Hai phân tích một biến này phải được bổ sung bằng tổng các tích chéo, để hoàn thiện bảng ma-nô-va. "
                      "Ta đi từng hàng trong các mảng của hai biến, nhân phần tử tương ứng, rồi cộng lại."):
            self.play(FadeIn(cp[0]))
        with self.say("Với mảng xử lý: ba nhân bốn nhân âm một, cộng hai nhân âm ba nhân âm ba, cộng ba nhân âm hai nhân ba, bằng âm mười hai. "
                      "Với mảng phần dư, ta được một. Tổng tích chéo toàn phần là một trăm bốn mươi chín."):
            self.play(FadeIn(cp[1]))
            self.play(FadeIn(cp[2]))
            self.play(FadeIn(cp[3]))
        with self.say("Lấy một trăm bốn mươi chín trừ đi tích chéo của trung bình là một trăm sáu mươi, ta được tích chéo toàn phần hiệu chỉnh "
                      "bằng âm mười một."):
            self.play(FadeIn(cp[4]))
        self.clear_content()

        self.set_title("Ví dụ 6.9 — Bảng MANOVA", "tr. 305")
        def M(a, b, c, d, color=FG):
            return mt(rf"\begin{{bmatrix}}{a}&{b}\\{c}&{d}\end{{bmatrix}}", size=34, color=color)
        t = table([
            ["Nguồn biến thiên", "Ma trận SSP", "Bậc tự do"],
            ["Xử lý (B)", M(78, -12, -12, 48, GOLD), mt("3-1=2", size=32)],
            ["Phần dư (W)", M(10, 1, 1, 24, GREEN), mt("3+2+3-3=5", size=32)],
            ["Toàn phần (hiệu chỉnh)", M(88, -11, -11, 72), mt("7", size=32)],
        ], [4.0, 3.6, 3.6], row_h=1.2, size=26)
        chk = mt(r"\begin{bmatrix}88&-11\\-11&72\end{bmatrix}=\begin{bmatrix}78&-12\\-12&48\end{bmatrix}+\begin{bmatrix}10&1\\1&24\end{bmatrix}", size=32)
        grp = VGroup(t, chk).arrange(DOWN, buff=0.5)
        self.fit(grp, top_buff=0.35, grow=1.3)
        with self.say("Đưa tất cả vào bảng ma-nô-va. Đường chéo của mỗi ma trận là tổng bình phương từng biến, ngoài đường chéo là tích chéo. "
                      "Ma trận xử lý bê là bảy tám, âm mười hai, âm mười hai, bốn tám. Ma trận phần dư đáp-bờ-liu là mười, một, một, hai mươi bốn."):
            self.play(Create(t.lines), FadeIn(t.rows[0]))
            self.play(LaggedStart(*[FadeIn(r) for r in t.rows[1:]], lag_ratio=0.4), run_time=2.5)
        with self.say("Kiểm tra lại đẳng thức sáu bốn mươi: ma trận toàn phần đúng bằng bê cộng đáp-bờ-liu."):
            self.play(Write(chk))
        self.clear_content()

        self.set_title("Ví dụ 6.9 — Kiểm định bằng Wilks' lambda", "tr. 305–306")
        lam = mt(r"\Lambda^*=\frac{|\mathbf W|}{|\mathbf B+\mathbf W|}=\frac{\begin{vmatrix}10&1\\1&24\end{vmatrix}}{\begin{vmatrix}88&-11\\-11&72\end{vmatrix}}"
                 r"=\frac{10(24)-(1)^2}{88(72)-(-11)^2}=\frac{239}{6215}=0.0385", size=38)
        why = mix("p = 2, g = 3 ⇒ dùng dòng 2 của Bảng 6.3 (kiểm định chính xác)", size=24, color=MUTED)
        F = mt(r"\left(\frac{1-\sqrt{\Lambda^*}}{\sqrt{\Lambda^*}}\right)\left(\frac{\sum n_\ell-g-1}{g-1}\right)"
               r"=\left(\frac{1-\sqrt{0.0385}}{\sqrt{0.0385}}\right)\left(\frac{8-3-1}{3-1}\right)=8.19", size=36)
        df = mix("so với", r"$F_{4,8}(0.01)=7.01$", ";", r"$\nu_1=2(g-1)=4,\ \nu_2=2(\sum n_\ell-g-1)=8$", size=24, color=MUTED)
        cmp = mt(r"8.19>F_{4,8}(0.01)=7.01", size=40, color=GOLD)
        concl = boxed(mix("⇒ Bác bỏ", r"$H_0:\boldsymbol\tau_1=\boldsymbol\tau_2=\boldsymbol\tau_3=\mathbf 0$",
                          "ở mức α = 0.01: có khác biệt giữa các xử lý", size=26, color=GOLD), color=GOLD)
        grp = VGroup(lam, why, F, df, cmp, concl).arrange(DOWN, buff=0.32)
        self.fit(grp, top_buff=0.35)
        with self.say("Tính lam-đa Uyn-xơ: định thức của đáp-bờ-liu là mười nhân hai mươi bốn trừ một, bằng hai trăm ba mươi chín. "
                      "Định thức của ma trận toàn phần là sáu nghìn hai trăm mười lăm. Vậy lam-đa sao bằng không phẩy không ba tám năm, rất nhỏ."):
            self.play(Write(lam), run_time=3)
        with self.say("Vì pê bằng hai và gờ bằng ba, bảng 6.3 cho ta một kiểm định chính xác, giả định phân phối chuẩn và ma trận hiệp phương sai "
                      "bằng nhau. Thống kê kiểm định bằng tám phẩy một chín."):
            self.play(FadeIn(why))
            self.play(Write(F), run_time=2.5)
        with self.say("Phân phối ép có bậc tự do nuy một bằng hai nhân gờ trừ một bằng bốn, và nuy hai bằng tám. Phân vị một phần trăm là bảy phẩy "
                      "không một. Vì tám phẩy một chín lớn hơn bảy phẩy không một, ta bác bỏ giả thuyết không ở mức một phần trăm, "
                      "và kết luận có sự khác biệt giữa các xử lý."):
            self.play(FadeIn(df))
            self.play(Write(cmp))
            self.play(FadeIn(concl, shift=UP * 0.2))
        self.clear_content()

        self.set_title("Lời khuyên thực hành", "sách tr. 306")
        tip = bullet_list([
            vt("Khi p lớn, thường không lập bảng MANOVA đầy đủ,", size=28),
            vt("nhưng vẫn nên cho máy in B và W để phát hiện các phần tử lớn bất thường.", size=28),
            mix("Kiểm tra phần dư", r"$\hat{\mathbf e}_{\ell j}=\mathbf x_{\ell j}-\bar{\mathbf x}_\ell$",
                ": tính chuẩn và điểm ngoại lai (mục 4.6, 4.7).", size=28),
        ], gap=0.45)
        self.fit(tip, top_buff=0.8)
        with self.say("Một lời khuyên thực hành từ sách: khi số biến lớn, người ta thường không lập bảng ma-nô-va đầy đủ. Tuy vậy, vẫn nên cho "
                      "máy tính in ra ma trận bê và đáp-bờ-liu để thấy các phần tử lớn. Đồng thời, các vectơ phần dư nên được kiểm tra "
                      "tính chuẩn và điểm ngoại lai, bằng các kỹ thuật ở mục 4.6 và 4.7."):
            self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.2) for r in tip], lag_ratio=0.5), run_time=3)
        self.clear_all()


class S06_Example610(Lecture):
    section_label = "Phần 3 · Ví dụ 6.10"

    def construct(self):
        self.set_title("Ví dụ 6.10 — Dữ liệu viện dưỡng lão Wisconsin", "Example 6.10, tr. 306–308")
        ctx = bullet_list([
            vt("Sở Y tế & Dịch vụ xã hội bang Wisconsin hoàn trả chi phí cho các viện dưỡng lão.", size=25),
            vt("Mục tiêu: chi phí có khác nhau theo loại hình sở hữu không?", size=25, color=GOLD),
            vt("Nhân tố: sở hữu, g = 3 mức — tư nhân (271), phi lợi nhuận (138), nhà nước (107); n = 516", size=25),
            vt("p = 4 biến chi phí (giờ / bệnh nhân / ngày):", size=25),
        ], gap=0.3)
        vars_ = VGroup(
            mix("$X_1:$", "nhân công điều dưỡng", size=24), mix("$X_2:$", "nhân công dinh dưỡng", size=24),
            mix("$X_3:$", "vận hành & bảo trì cơ sở", size=24), mix("$X_4:$", "dọn phòng & giặt là", size=24),
        )
        vg = VGroup(VGroup(vars_[0], vars_[1]).arrange(RIGHT, buff=0.8), VGroup(vars_[2], vars_[3]).arrange(RIGHT, buff=0.8)).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        grp = VGroup(ctx, vg).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        vg.shift(RIGHT * 0.6)
        self.fit(grp, top_buff=0.5, grow=1.15)
        with self.say("Ví dụ 6.10 là một ứng dụng thực tế. Sở Y tế và Dịch vụ xã hội bang Wisconsin hoàn trả chi phí cho các viện dưỡng lão. "
                      "Một nghiên cứu muốn biết: loại hình sở hữu có ảnh hưởng đến chi phí hay không."):
            self.play(FadeIn(ctx[0]), FadeIn(ctx[1]))
        with self.say("Nhân tố ở đây là loại hình sở hữu, với ba mức: tư nhân hai trăm bảy mươi mốt viện, phi lợi nhuận một trăm ba mươi tám, "
                      "và nhà nước một trăm lẻ bảy. Tổng cộng năm trăm mười sáu quan sát. Có bốn biến chi phí, tính theo giờ trên mỗi bệnh nhân "
                      "mỗi ngày: nhân công điều dưỡng, nhân công dinh dưỡng, vận hành bảo trì, và dọn phòng giặt là."):
            self.play(FadeIn(ctx[2]), FadeIn(ctx[3]))
            self.play(FadeIn(vg))
        self.clear_content()

        self.set_title("Ví dụ 6.10 — Thống kê tóm tắt và các ma trận", "tr. 306–307")
        means = VGroup(
            mt(r"\bar{\mathbf x}_1=\begin{bmatrix}2.066\\.480\\.082\\.360\end{bmatrix}", size=30),
            mt(r"\bar{\mathbf x}_2=\begin{bmatrix}2.167\\.596\\.124\\.418\end{bmatrix}", size=30),
            mt(r"\bar{\mathbf x}_3=\begin{bmatrix}2.273\\.521\\.125\\.383\end{bmatrix}", size=30),
            mt(r"\bar{\mathbf x}=\begin{bmatrix}2.136\\.519\\.102\\.380\end{bmatrix}", size=30, color=BLUE),
        ).arrange(RIGHT, buff=0.5)
        W = mt(r"\mathbf W=\sum_{\ell=1}^{3}(n_\ell-1)\mathbf S_\ell=\begin{bmatrix}182.962&&&\\4.408&8.200&&\\1.695&.633&1.484&\\9.581&2.428&.394&6.538\end{bmatrix}", size=28, color=GREEN)
        B = mt(r"\mathbf B=\sum_{\ell=1}^{3}n_\ell(\bar{\mathbf x}_\ell-\bar{\mathbf x})(\bar{\mathbf x}_\ell-\bar{\mathbf x})'=\begin{bmatrix}3.475&&&\\1.111&1.225&&\\.821&.453&.235&\\.584&.610&.230&.304\end{bmatrix}", size=28, color=GOLD)
        mats = VGroup(W, B).arrange(RIGHT, buff=0.5)
        grp = VGroup(means, mats).arrange(DOWN, buff=0.45)
        self.fit(grp, top_buff=0.35, grow=1.3)
        with self.say("Đây là các vectơ trung bình mẫu của ba nhóm và vectơ trung bình chung."):
            self.play(FadeIn(means))
        with self.say("Vì các ma trận hiệp phương sai mẫu S l có vẻ tương thích, sách gộp chúng lại để được ma trận đáp-bờ-liu theo công thức sáu bốn mốt. "
                      "Ma trận bê tính từ độ lệch của các trung bình nhóm so với trung bình chung. Chỉ cần in nửa dưới, vì ma trận đối xứng."):
            self.play(FadeIn(W))
            self.play(FadeIn(B))
        self.clear_content()

        self.set_title("Ví dụ 6.10 — Kiểm định", "g = 3 ⇒ dòng cuối Bảng 6.3; đối chiếu với xấp xỉ Bartlett")
        lam = mt(r"\Lambda^*=\frac{|\mathbf W|}{|\mathbf B+\mathbf W|}=0.7714", size=44)
        F = mt(r"\left(\frac{\sum n_\ell-p-2}{p}\right)\left(\frac{1-\sqrt{\Lambda^*}}{\sqrt{\Lambda^*}}\right)"
               r"=\left(\frac{516-4-2}{4}\right)\left(\frac{1-\sqrt{.7714}}{\sqrt{.7714}}\right)=17.67", size=36)
        cmp = mt(r"17.67>F_{8,1020}(0.01)\doteq\chi^2_8(0.01)/8=2.51", size=36, color=GOLD)
        bart = mt(r"-\left(n-1-\tfrac{p+g}{2}\right)\ln\Lambda^*=-511.5\ln(0.7714)=132.76>\chi^2_8(0.01)=20.09", size=34, color=ACCENT)
        concl = boxed(vt("⇒ Bác bỏ H₀ ở mức 1%: chi phí trung bình khác nhau theo loại hình sở hữu", size=26, color=GOLD), color=GOLD)
        grp = VGroup(lam, F, cmp, bart, concl).arrange(DOWN, buff=0.4)
        self.fit(grp, top_buff=0.4)
        with self.say("Để kiểm định giả thuyết không có hiệu ứng sở hữu, tức là chi phí trung bình như nhau giữa ba loại hình, máy tính cho lam-đa sao "
                      "bằng không phẩy bảy bảy một bốn."):
            self.play(Write(lam))
        with self.say("Vì gờ bằng ba, ta dùng dòng cuối bảng 6.3, được thống kê bằng mười bảy phẩy sáu bảy. So với phân vị một phần trăm của ép tám, "
                      "một nghìn không trăm hai mươi, xấp xỉ bằng khi bình phương tám chia tám, là hai phẩy năm một. Mười bảy phẩy sáu bảy lớn hơn nhiều, "
                      "nên ta bác bỏ giả thuyết không ở mức một phần trăm."):
            self.play(Write(F), run_time=2.5)
            self.play(Write(cmp))
        with self.say("Vì cỡ mẫu lớn, ta cũng có thể dùng xấp xỉ Bác-lét: âm năm trăm mười một phẩy năm nhân lốc của không phẩy bảy bảy một bốn, "
                      "bằng một trăm ba mươi hai phẩy bảy sáu, lớn hơn khi bình phương tám ở mức một phần trăm là hai mươi phẩy không chín. "
                      "Hai cách cho cùng một kết luận: chi phí trung bình khác nhau tùy loại hình sở hữu."):
            self.play(Write(bart), run_time=2)
            self.play(FadeIn(concl, shift=UP * 0.2))
        self.clear_all()
