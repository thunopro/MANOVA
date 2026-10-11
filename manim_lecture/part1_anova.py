"""Phần 1: Mở đầu và tổng quan ANOVA một nhân tố (sách tr. 296-301, Ví dụ 6.7, 6.8)."""
from common import *


class S00_Intro(Lecture):
    def construct(self):
        book = vt("Johnson & Wichern — Applied Multivariate Statistical Analysis (6th ed.), Chương 6",
                  size=22, color=MUTED)
        t1 = vt("Phân tích phương sai đa biến", size=56, weight=BOLD)
        t2 = vt("MANOVA một nhân tố (mục 6.4) và hai nhân tố (mục 6.7)", size=32, color=ACCENT)
        title = VGroup(t1, t2, book).arrange(DOWN, buff=0.4)
        with self.say("Chào các em. Hôm nay chúng ta sẽ học một chủ đề rất quan trọng trong thống kê "
                      "nhiều chiều: phân tích phương sai đa biến, thường gọi tắt là ma-nô-va."):
            self.play(FadeIn(t1, shift=UP * 0.3), run_time=1.2)
            self.play(FadeIn(t2, shift=UP * 0.2), run_time=1)
        with self.say("Toàn bộ bài giảng bám sát chương sáu của cuốn sách Applied Multivariate Statistical "
                      "Analysis của Johnson và Wichern, bản thứ sáu. Cụ thể là mục 6.4 về ma-nô-va một nhân tố, "
                      "và nội dung chính là mục 6.7, ma-nô-va hai nhân tố."):
            self.play(FadeIn(book))
        self.clear_all()

        self.set_title("Lộ trình bài giảng")
        steps = [
            ("1", "Tổng quan ANOVA một nhân tố", "mô hình, phân tích tổng bình phương, bảng ANOVA, kiểm định F"),
            ("2", "Các thuật ngữ cần nắm", "nhân tố, mức, hiệu ứng, SS, SSP, B, W, Wilks' lambda, tương tác"),
            ("3", "Mục 6.4 — One-way MANOVA", "Ví dụ 6.9 và Ví dụ 6.10 (viện dưỡng lão Wisconsin)"),
            ("4", "Mục 6.7 — Two-way MANOVA (trọng tâm)", "mô hình có tương tác, bảng MANOVA, Ví dụ 6.13 (màng nhựa)"),
            ("5", "Tổng kết: quy trình thực hành & thuyết trình", "các bước làm bài và mã Python kiểm chứng"),
        ]
        rows = VGroup()
        for n, a, b in steps:
            circ = Circle(radius=0.3, color=ACCENT, fill_color=PANEL, fill_opacity=1)
            num = vt(n, size=26, color=ACCENT, weight=BOLD).move_to(circ)
            txt = VGroup(vt(a, size=28, weight=BOLD), vt(b, size=20, color=MUTED)).arrange(
                DOWN, aligned_edge=LEFT, buff=0.08)
            rows.add(VGroup(VGroup(circ, num), txt).arrange(RIGHT, buff=0.35))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.32).next_to(self.title_mob, DOWN, buff=0.45).set_x(-0.6)
        with self.say("Bài giảng gồm năm phần. Đầu tiên, ta ôn lại phân tích phương sai một biến, a-nô-va, "
                      "vì ma-nô-va chính là sự mở rộng của nó."):
            self.play(FadeIn(rows[0], shift=RIGHT * 0.3))
        with self.say("Thứ hai, ta thống nhất các thuật ngữ. Thứ ba, ta học mục 6.4, ma-nô-va một nhân tố, "
                      "với hai ví dụ trong sách."):
            self.play(FadeIn(rows[1], shift=RIGHT * 0.3))
            self.play(FadeIn(rows[2], shift=RIGHT * 0.3))
        with self.say("Thứ tư, là phần trọng tâm: ma-nô-va hai nhân tố có tương tác, cùng ví dụ 6.13 về màng nhựa. "
                      "Cuối cùng, ta tổng kết quy trình để các em tự thực hành và thuyết trình lại."):
            self.play(FadeIn(rows[3], shift=RIGHT * 0.3))
            self.play(FadeIn(rows[4], shift=RIGHT * 0.3))
        self.clear_all()

        self.set_title("Vì sao cần MANOVA?")
        left = VGroup(
            vt("Một biến phản hồi", size=28, color=GOLD, weight=BOLD),
            vt("So sánh trung bình của g nhóm", size=24),
            mt(r"H_0:\ \mu_1=\mu_2=\cdots=\mu_g", size=38),
            vt("→ ANOVA, kiểm định F", size=24, color=MUTED),
        ).arrange(DOWN, buff=0.3)
        right = VGroup(
            vt("p biến phản hồi cùng lúc", size=28, color=ACCENT, weight=BOLD),
            vt("So sánh các VECTƠ trung bình", size=24),
            mt(r"H_0:\ \boldsymbol\mu_1=\boldsymbol\mu_2=\cdots=\boldsymbol\mu_g", size=38),
            vt("→ MANOVA, Wilks' lambda", size=24, color=MUTED),
        ).arrange(DOWN, buff=0.3)
        lb, rb = boxed(left, color=GOLD, buff=0.35), boxed(right, color=ACCENT, buff=0.35)
        VGroup(lb, rb).arrange(RIGHT, buff=0.8).shift(DOWN * 0.2)
        arrow = Arrow(lb.get_right(), rb.get_left(), color=MUTED, buff=0.1)
        with self.say("Tại sao cần ma-nô-va? Trong a-nô-va, mỗi quan sát chỉ là một con số, và ta so sánh "
                      "trung bình của gờ nhóm."):
            self.play(FadeIn(lb, shift=UP * 0.2))
        with self.say("Nhưng trong thực tế, trên mỗi đơn vị thí nghiệm ta thường đo nhiều biến cùng lúc. "
                      "Ví dụ với màng nhựa, ta đo cả độ bền xé, độ bóng và độ mờ. Khi đó mỗi quan sát là một vectơ "
                      "pê thành phần, và câu hỏi trở thành: các vectơ trung bình có bằng nhau không?"):
            self.play(GrowArrow(arrow), FadeIn(rb, shift=UP * 0.2))
        note = vt("Sách: \"MANOVA is used first to investigate whether the population mean vectors are the same "
                  "and, if not, which mean components differ significantly.\"", size=19, color=MUTED)
        note.scale_to_fit_width(12.4).to_edge(DOWN, buff=0.55)
        with self.say("Theo sách, ma-nô-va được dùng trước hết để xem các vectơ trung bình tổng thể có như nhau không, "
                      "và nếu không thì những thành phần nào khác nhau đáng kể. Ma-nô-va xét đồng thời mọi biến "
                      "và cả tương quan giữa chúng, thay vì làm rời rạc từng biến."):
            self.play(FadeIn(note))
        self.clear_all()


class S01_AnovaModel(Lecture):
    section_label = "Phần 1 · Tổng quan ANOVA"

    def construct(self):
        card = self.section_card("PHẦN 1", "Tổng quan về ANOVA một nhân tố",
                                 "A Summary of Univariate ANOVA — sách tr. 297–301")
        with self.say("Phần một. Tổng quan về phân tích phương sai một biến, một nhân tố. Đây là nền móng, "
                      "vì sách nói rõ: ôn lại a-nô-va sẽ giúp ta hiểu các giả định và phương pháp nhiều chiều."):
            self.play(FadeIn(card, shift=UP * 0.3))
        self.play(FadeOut(card))

        self.set_title("Bài toán và giả định", "Univariate one-way ANOVA")
        pops = VGroup(*[
            VGroup(vt(f"Tổng thể {i}", size=24, color=c),
                   mt(rf"X_{{{i}1}},\,X_{{{i}2}},\dots,X_{{{i}n_{i}}}", size=34),
                   mt(rf"\sim N(\mu_{i},\sigma^2)", size=34, color=c)).arrange(RIGHT, buff=0.35)
            for i, c in [("1", GOLD), ("2", BLUE)]
        ])
        dots = mt(r"\vdots", size=34)
        last = VGroup(vt("Tổng thể g", size=24, color=GREEN),
                      mt(r"X_{g1},\,X_{g2},\dots,X_{gn_g}", size=34),
                      mt(r"\sim N(\mu_g,\sigma^2)", size=34, color=GREEN)).arrange(RIGHT, buff=0.35)
        data = VGroup(*pops, dots, last).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        data.next_to(self.title_mob, DOWN, buff=0.5)
        dots.set_x(data.get_x())
        with self.say("Giả sử ta có gờ tổng thể. Từ tổng thể thứ l, ta lấy một mẫu ngẫu nhiên cỡ n l, "
                      "các quan sát có phân phối chuẩn với trung bình muy l và cùng phương sai xích-ma bình phương. "
                      "Các mẫu từ những tổng thể khác nhau thì độc lập với nhau."):
            self.play(LaggedStart(*[FadeIn(m, shift=RIGHT * 0.3) for m in data], lag_ratio=0.3), run_time=3)
        h0 = mt(r"H_0:\ \mu_1=\mu_2=\cdots=\mu_g", size=44, color=GOLD)
        h0.next_to(data, DOWN, buff=0.6)
        with self.say("Câu hỏi: các trung bình có bằng nhau không? Giả thuyết không là muy một bằng muy hai, "
                      "cho tới muy gờ."):
            self.play(Write(h0))
        self.clear_content()

        self.set_title("Tham số hoá lại: trung bình = mức chung + hiệu ứng", "(6-32)")
        eq = mt(r"\mu_\ell", "=", r"\mu", "+", r"(\mu_\ell-\mu)", size=56)
        eq2 = mt(r"\mu_\ell", "=", r"\mu", "+", r"\tau_\ell", size=56)
        eq[2].set_color(BLUE); eq[4].set_color(GOLD)
        eq2[2].set_color(BLUE); eq2[4].set_color(GOLD)
        eq.shift(UP * 1.2); eq2.move_to(eq)
        with self.say("Thay vì làm việc trực tiếp với muy l, ta tách nó thành hai phần: một mức chung muy, "
                      "cộng với độ lệch muy l trừ muy."):
            self.play(Write(eq))
        with self.say("Độ lệch đó ta đặt tên là tau l, gọi là hiệu ứng của tổng thể thứ l, hay hiệu ứng xử lý."):
            self.play(TransformMatchingTex(eq, eq2))
        un, labels = legend(eq2, [0, 2, 4], ["trung bình tổng thể ℓ", "trung bình chung (overall mean)",
                                             "hiệu ứng xử lý thứ ℓ (treatment effect)"], cols=1)
        self.play(Create(un), FadeIn(labels))
        h0 = mt(r"H_0:\ \mu_1=\cdots=\mu_g", r"\iff", r"H_0:\ \tau_1=\tau_2=\cdots=\tau_g=0", size=44)
        h0[2].set_color(GOLD)
        h0.next_to(labels, DOWN, buff=0.8)
        with self.say("Vì các tổng thể thường tương ứng với các điều kiện thí nghiệm khác nhau, nên xét hiệu ứng tau l "
                      "rất tiện. Giả thuyết các trung bình bằng nhau trở thành: mọi hiệu ứng tau đều bằng không. "
                      "Nghĩa là, không có hiệu ứng xử lý nào."):
            self.play(Write(h0))
        self.clear_content()

        self.set_title("Mô hình ANOVA một nhân tố", "(6-33)")
        model = mt(r"X_{\ell j}", "=", r"\mu", "+", r"\tau_\ell", "+", r"e_{\ell j}", size=60)
        model[2].set_color(BLUE); model[4].set_color(GOLD); model[6].set_color(GREEN)
        model.shift(UP * 1.4)
        un, labs = legend(model, [0, 2, 4, 6], ["quan sát thứ j của tổng thể ℓ", "trung bình chung",
                                                "hiệu ứng xử lý", "sai số ngẫu nhiên"])
        with self.say("Từ đó, mỗi quan sát X l j được viết dưới dạng gợi ý: bằng trung bình chung muy, "
                      "cộng hiệu ứng xử lý tau l, cộng sai số ngẫu nhiên e l j."):
            self.play(Write(model))
            self.play(Create(un), FadeIn(labs))
        cond = VGroup(
            mix("Các sai số", "$e_{\\ell j}$", "độc lập,", "$e_{\\ell j}\\sim N(0,\\sigma^2)$", size=28),
            VGroup(vt("Ràng buộc để tham số xác định duy nhất:", size=24, color=MUTED),
                   mt(r"\sum_{\ell=1}^{g} n_\ell\,\tau_\ell = 0", size=40, color=GOLD)).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.45).next_to(labs, DOWN, buff=0.7)
        with self.say("Các sai số e l j độc lập, có phân phối chuẩn trung bình không, phương sai xích-ma bình phương. "
                      "Để các tham số được xác định duy nhất, người ta đặt thêm ràng buộc: tổng có trọng số n l nhân tau l "
                      "bằng không."):
            self.play(FadeIn(cond[0]))
            self.play(FadeIn(cond[1]))
        self.clear_content()

        self.set_title("Phân tích quan sát tương ứng với mô hình", "(6-34)")
        dec = mt(r"x_{\ell j}", "=", r"\bar x", "+", r"(\bar x_\ell-\bar x)", "+", r"(x_{\ell j}-\bar x_\ell)", size=58)
        dec[2].set_color(BLUE); dec[4].set_color(GOLD); dec[6].set_color(GREEN)
        dec.shift(UP * 1.2)
        un, labs = legend(dec, [0, 2, 4, 6], ["quan sát", "trung bình mẫu chung",
                                              "ước lượng hiệu ứng xử lý", "phần dư (residual)"])
        est = VGroup(mt(r"\bar x\ \to\ \hat\mu", size=38, color=BLUE),
                     mt(r"\hat\tau_\ell=\bar x_\ell-\bar x", size=38, color=GOLD),
                     mt(r"x_{\ell j}-\bar x_\ell\ \to\ \hat e_{\ell j}", size=38, color=GREEN)).arrange(RIGHT, buff=1.0)
        est.next_to(labs, DOWN, buff=0.9)
        with self.say("Tương ứng với mô hình, ta phân tích chính dữ liệu quan sát. Mỗi giá trị x l j bằng trung bình mẫu "
                      "chung x ngang, cộng với x ngang l trừ x ngang, cộng với x l j trừ x ngang l."):
            self.play(Write(dec), run_time=2.5)
            self.play(Create(un), FadeIn(labs))
        with self.say("Trong đó x ngang ước lượng muy, x ngang l trừ x ngang ước lượng hiệu ứng tau l, "
                      "và x l j trừ x ngang l ước lượng sai số. Đây là công thức sáu ba tư, các em cần nhớ thật kỹ, "
                      "vì cả ma-nô-va một nhân tố lẫn hai nhân tố đều xây dựng trên ý tưởng này."):
            self.play(LaggedStart(*[FadeIn(e, shift=UP * 0.2) for e in est], lag_ratio=0.4))
        self.clear_all()


class S02_AnovaExample(Lecture):
    section_label = "Phần 1 · Tổng quan ANOVA"

    def construct(self):
        self.set_title("Ví dụ 6.7 — Phân tích tổng bình phương", "Example 6.7, sách tr. 298")
        pops = VGroup(
            VGroup(vt("Tổng thể 1:", size=28, color=MUTED), mt("9,\\ 6,\\ 9", size=40)).arrange(RIGHT),
            VGroup(vt("Tổng thể 2:", size=28, color=MUTED), mt("0,\\ 2", size=40)).arrange(RIGHT),
            VGroup(vt("Tổng thể 3:", size=28, color=MUTED), mt("3,\\ 1,\\ 2", size=40)).arrange(RIGHT),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(self.title_mob, DOWN, buff=0.4).to_edge(LEFT, buff=1)
        means = VGroup(mt(r"\bar x_1=8", size=38), mt(r"\bar x_2=1", size=38), mt(r"\bar x_3=2", size=38))
        for m, p in zip(means, pops):
            m.next_to(p, RIGHT, buff=0.8)
            m.set_x(2.2)
        with self.say("Hãy làm cụ thể với ví dụ 6.7 trong sách. Có ba tổng thể, với các mẫu độc lập: "
                      "tổng thể một gồm chín, sáu, chín. Tổng thể hai gồm không và hai. Tổng thể ba gồm ba, một, hai."):
            self.play(LaggedStart(*[FadeIn(p, shift=RIGHT * 0.3) for p in pops], lag_ratio=0.4), run_time=2.5)
        grand = mt(r"\bar x=\frac{9+6+9+0+2+3+1+2}{8}=4", size=38, color=BLUE)
        grand.next_to(pops, DOWN, buff=0.45).set_x(0)
        with self.say("Trung bình từng nhóm lần lượt là tám, một và hai. Trung bình chung của cả tám quan sát là bốn."):
            self.play(LaggedStart(*[FadeIn(m) for m in means], lag_ratio=0.3))
            self.play(Write(grand))
        one = mt(r"x_{31}=3", "=", r"\bar x", "+", r"(\bar x_3-\bar x)", "+", r"(x_{31}-\bar x_3)", size=38)
        two = mt("3", "=", "4", "+", "(2-4)", "+", "(3-2)", "=", "4", "+", "(-2)", "+", "1", size=38)
        for m in (one, two):
            m[2].set_color(BLUE); m[4].set_color(GOLD); m[6].set_color(GREEN)
        two[8].set_color(BLUE); two[10].set_color(GOLD); two[12].set_color(GREEN)
        VGroup(one, two).arrange(DOWN, buff=0.3).next_to(grand, DOWN, buff=0.45)
        with self.say("Lấy thử quan sát đầu tiên của tổng thể ba, x ba một bằng ba. Ta viết: ba bằng bốn, "
                      "cộng hai trừ bốn, cộng ba trừ hai. Tức là bốn, cộng âm hai, cộng một."):
            self.play(Write(one))
            self.play(Write(two))
        self.clear_content()

        # các mảng
        obs = mt(r"\begin{pmatrix}9&6&9\\0&2\\3&1&2\end{pmatrix}", size=36)
        mean = mt(r"\begin{pmatrix}4&4&4\\4&4\\4&4&4\end{pmatrix}", size=36, color=BLUE)
        trt = mt(r"\begin{pmatrix}4&4&4\\-3&-3\\-2&-2&-2\end{pmatrix}", size=36, color=GOLD)
        res = mt(r"\begin{pmatrix}1&-2&1\\-1&1\\1&-1&0\end{pmatrix}", size=36, color=GREEN)
        eqs = [mt("=", size=44), mt("+", size=44), mt("+", size=44)]
        row = VGroup(obs, eqs[0], mean, eqs[1], trt, eqs[2], res).arrange(RIGHT, buff=0.3)
        row.next_to(self.title_mob, DOWN, buff=0.6)
        names = VGroup(
            vt("quan sát", size=20), vt("trung bình", size=20, color=BLUE),
            vt("hiệu ứng xử lý", size=20, color=GOLD), vt("phần dư", size=20, color=GREEN))
        sym = VGroup(mt(r"(x_{\ell j})", size=28), mt(r"(\bar x)", size=28, color=BLUE),
                     mt(r"(\bar x_\ell-\bar x)", size=28, color=GOLD), mt(r"(x_{\ell j}-\bar x_\ell)", size=28, color=GREEN))
        for n, s, a in zip(names, sym, [obs, mean, trt, res]):
            n.next_to(a, DOWN, buff=0.25)
            s.next_to(n, DOWN, buff=0.1)
        ss_title = vt("Độ lớn của mảng = tổng bình phương (SS): xếp thành vectơ, lấy độ dài bình phương", size=22, color=MUTED)
        ss_title.next_to(sym, DOWN, buff=0.3)
        ss = VGroup(
            mt(r"SS_{obs}=9^2+6^2+9^2+0^2+2^2+3^2+1^2+2^2=216", size=34),
            mt(r"SS_{mean}=8\,(4^2)=128", size=34, color=BLUE),
            mt(r"SS_{tr}=3(4^2)+2(-3)^2+3(-2)^2=78", size=34, color=GOLD),
            mt(r"SS_{res}=1^2+(-2)^2+1^2+(-1)^2+1^2+1^2+(-1)^2+0^2=10", size=34, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(ss_title, DOWN, buff=0.2)
        self.fit(VGroup(row, names, sym, ss_title, ss), top_buff=0.3)
        with self.say("Làm như vậy với mọi quan sát, ta được bốn mảng số. Mảng quan sát bằng mảng trung bình, "
                      "cộng mảng hiệu ứng xử lý, cộng mảng phần dư."):
            self.play(FadeIn(obs))
            self.play(FadeIn(eqs[0]), TransformFromCopy(obs, mean))
            self.play(FadeIn(eqs[1]), TransformFromCopy(obs, trt))
            self.play(FadeIn(eqs[2]), TransformFromCopy(obs, res))
            self.play(FadeIn(names), FadeIn(sym))
        q = vt("Mảng hiệu ứng xử lý có \"lớn\" so với mảng phần dư không?", size=28, color=GOLD)
        q.next_to(sym, DOWN, buff=0.5)
        with self.say("Câu hỏi các trung bình có bằng nhau không, được trả lời bằng cách xem: đóng góp của mảng hiệu ứng "
                      "xử lý có lớn so với mảng phần dư hay không. Nếu đóng góp của xử lý lớn, ta bác bỏ giả thuyết không."):
            self.play(FadeIn(q, shift=UP * 0.2))
        self.play(FadeOut(q))
        with self.say("Độ lớn của một mảng được đo bằng tổng bình phương, viết tắt S S: xếp các phần tử thành một vectơ "
                      "rồi tính bình phương độ dài của nó. Với mảng quan sát, ta được hai trăm mười sáu."):
            self.play(FadeIn(ss_title))
            self.play(Write(ss[0]))
        with self.say("Tương tự, tổng bình phương của trung bình là một trăm hai mươi tám. Của xử lý là bảy mươi tám. "
                      "Và của phần dư là mười."):
            self.play(Write(ss[1]))
            self.play(Write(ss[2]))
            self.play(Write(ss[3]))
        self.clear_content()

        big = mt("216", "=", "128", "+", "78", "+", "10", size=80)
        big[2].set_color(BLUE); big[4].set_color(GOLD); big[6].set_color(GREEN)
        sym = mt(r"SS_{obs}", "=", r"SS_{mean}", "+", r"SS_{tr}", "+", r"SS_{res}", size=56)
        sym[2].set_color(BLUE); sym[4].set_color(GOLD); sym[6].set_color(GREEN)
        VGroup(big, sym).arrange(DOWN, buff=0.6).shift(UP * 0.3)
        with self.say("Điều thú vị là các tổng bình phương cũng phân tích giống hệt như các quan sát: hai trăm mười sáu "
                      "bằng một trăm hai mươi tám, cộng bảy mươi tám, cộng mười."):
            self.play(Write(big))
            self.play(TransformFromCopy(big, sym))
        cor = mt(r"SS_{cor}=SS_{obs}-SS_{mean}=216-128=88=78+10", size=40)
        cor.next_to(sym, DOWN, buff=0.6)
        with self.say("Nếu chuyển tổng bình phương của trung bình sang vế trái, ta có tổng bình phương toàn phần đã hiệu chỉnh, "
                      "bằng tám mươi tám, chính là bảy mươi tám cộng mười. Nếu giả thuyết không đúng, thì phương sai tính từ "
                      "S S xử lý và từ S S phần dư phải xấp xỉ nhau."):
            self.play(Write(cor))
        self.clear_content()

        self.set_title("Công thức tổng quát", "(6-35), (6-36)")
        f = mt(r"\sum_{\ell=1}^{g}\sum_{j=1}^{n_\ell}(x_{\ell j}-\bar x)^2", "=",
               r"\sum_{\ell=1}^{g}n_\ell(\bar x_\ell-\bar x)^2", "+",
               r"\sum_{\ell=1}^{g}\sum_{j=1}^{n_\ell}(x_{\ell j}-\bar x_\ell)^2", size=42)
        f[2].set_color(GOLD); f[4].set_color(GREEN)
        f.shift(UP * 1.3)
        braces = VGroup(
            BraceLabel(f[0], r"SS_{cor}", brace_direction=DOWN, font_size=34),
            BraceLabel(f[2], r"SS_{tr}", brace_direction=DOWN, font_size=34),
            BraceLabel(f[4], r"SS_{res}", brace_direction=DOWN, font_size=34),
        )
        names = VGroup(vt("toàn phần (hiệu chỉnh)", size=22), vt("giữa các mẫu (between)", size=22, color=GOLD),
                       vt("trong các mẫu (within)", size=22, color=GREEN))
        for n, b in zip(names, braces):
            n.next_to(b, DOWN, buff=0.15)
        with self.say("Tổng quát hoá, ta lấy công thức sáu ba tư, trừ x ngang hai vế, bình phương, rồi cộng theo mọi j và mọi l. "
                      "Do tổng các độ lệch x l j trừ x ngang l trong mỗi nhóm bằng không, nên tích chéo biến mất, và ta có "
                      "đẳng thức sáu ba năm."):
            self.play(Write(f), run_time=3)
        with self.say("Tổng bình phương toàn phần hiệu chỉnh, bằng tổng bình phương giữa các mẫu, cộng tổng bình phương trong các mẫu. "
                      "Giữa các mẫu, tiếng Anh là between, phản ánh khác biệt giữa các nhóm. Trong các mẫu, within, "
                      "phản ánh dao động ngẫu nhiên bên trong mỗi nhóm."):
            self.play(FadeIn(braces), FadeIn(names))
        df = VGroup(vt("Bậc tự do tương ứng:", size=26, color=MUTED),
                    mt(r"\sum n_\ell-1", "=", r"(g-1)", "+", r"\left(\sum n_\ell-g\right)", size=40)).arrange(RIGHT, buff=0.4)
        df[1][2].set_color(GOLD); df[1][4].set_color(GREEN)
        df.next_to(names, DOWN, buff=0.6)
        with self.say("Về bậc tự do: S S xử lý có gờ trừ một bậc tự do, S S phần dư có tổng n l trừ gờ bậc tự do, "
                      "và tổng là tổng n l trừ một. Sách giải thích bằng hình học: các mảng trung bình, xử lý và phần dư, "
                      "xem như các vectơ, thì vuông góc với nhau, và số chiều của không gian mà mỗi vectơ được tự do nằm trong "
                      "chính là số bậc tự do."):
            self.play(FadeIn(df))
        self.clear_content()

        self.set_title("Bảng ANOVA và kiểm định F", "sách tr. 300")
        t = table([
            ["Nguồn biến thiên", "Tổng bình phương (SS)", "Bậc tự do"],
            ["Xử lý (Treatments)", mt(r"SS_{tr}=\sum_{\ell} n_\ell(\bar x_\ell-\bar x)^2", size=30, color=GOLD), mt(r"g-1", size=30)],
            ["Phần dư (Error)", mt(r"SS_{res}=\sum_{\ell}\sum_{j}(x_{\ell j}-\bar x_\ell)^2", size=30, color=GREEN), mt(r"\sum n_\ell-g", size=30)],
            ["Toàn phần (hiệu chỉnh)", mt(r"SS_{cor}=\sum_{\ell}\sum_{j}(x_{\ell j}-\bar x)^2", size=30), mt(r"\sum n_\ell-1", size=30)],
        ], [3.6, 5.8, 2.4], row_h=0.85, size=24)
        t.next_to(self.title_mob, DOWN, buff=0.35)
        with self.say("Các kết quả được tóm tắt gọn trong bảng a-nô-va: ba dòng là xử lý, phần dư và toàn phần, "
                      "mỗi dòng có tổng bình phương và bậc tự do."):
            self.play(Create(t.lines), FadeIn(t.rows[0]))
            self.play(LaggedStart(*[FadeIn(r) for r in t.rows[1:]], lag_ratio=0.4), run_time=2)
        F = mt(r"F=\frac{SS_{tr}/(g-1)}{SS_{res}/\left(\sum n_\ell-g\right)}", r">", r"F_{g-1,\ \sum n_\ell-g}(\alpha)", size=42)
        F[2].set_color(GOLD)
        F.next_to(t, DOWN, buff=0.4)
        rule = mix("⇒ bác bỏ", r"$H_0:\tau_1=\cdots=\tau_g=0$", "ở mức α", size=26, color=GOLD).next_to(F, DOWN, buff=0.25)
        self.fit(VGroup(t, F, rule))
        with self.say("Kiểm định ép thông thường bác bỏ giả thuyết không ở mức an-pha nếu tỉ số ép, bằng S S xử lý chia gờ trừ một, "
                      "trên S S phần dư chia tổng n l trừ gờ, lớn hơn phân vị trên an-pha của phân phối ép với gờ trừ một và "
                      "tổng n l trừ gờ bậc tự do."):
            self.play(Write(F))
            self.play(FadeIn(rule))
        self.clear_content()

        self.set_title("Ví dụ 6.8 — Bảng ANOVA và kiểm định F", "Example 6.8, sách tr. 301")
        t = table([
            ["Nguồn biến thiên", "SS", "Bậc tự do"],
            ["Xử lý", mt(r"SS_{tr}=78", size=34, color=GOLD), mt(r"g-1=3-1=2", size=34)],
            ["Phần dư", mt(r"SS_{res}=10", size=34, color=GREEN), mt(r"\sum n_\ell-g=(3+2+3)-3=5", size=34)],
            ["Toàn phần (hiệu chỉnh)", mt(r"SS_{cor}=88", size=34), mt(r"\sum n_\ell-1=7", size=34)],
        ], [3.8, 3.2, 5.0], row_h=0.75, size=26)
        t.next_to(self.title_mob, DOWN, buff=0.4)
        with self.say("Áp dụng cho ví dụ 6.7, ta có ví dụ 6.8. S S xử lý bằng bảy mươi tám với hai bậc tự do. "
                      "S S phần dư bằng mười với năm bậc tự do. Toàn phần bằng tám mươi tám với bảy bậc tự do."):
            self.play(FadeIn(t))
        F = mt(r"F=\frac{SS_{tr}/(g-1)}{SS_{res}/(\sum n_\ell-g)}=\frac{78/2}{10/5}=19.5", size=42)
        F.next_to(t, DOWN, buff=0.5)
        cmp = mt(r"19.5", r">", r"F_{2,5}(0.01)=13.27", size=42)
        cmp[0].set_color(GOLD)
        cmp.next_to(F, DOWN, buff=0.35)
        concl = mix("⇒ Bác bỏ", r"$H_0:\tau_1=\tau_2=\tau_3=0$", "ở mức ý nghĩa 1%", size=28, color=GOLD).next_to(cmp, DOWN, buff=0.3)
        self.fit(VGroup(t, F, cmp, concl))
        with self.say("Tỉ số ép bằng bảy mươi tám chia hai, trên mười chia năm, bằng mười chín phẩy năm."):
            self.play(Write(F))
        with self.say("So với phân vị ép hai, năm ở mức một phần trăm là mười ba phẩy hai bảy. Vì mười chín phẩy năm lớn hơn, "
                      "ta bác bỏ giả thuyết không có hiệu ứng xử lý, ở mức ý nghĩa một phần trăm."):
            self.play(Write(cmp))
            self.play(FadeIn(concl, shift=UP * 0.2))
        self.clear_content()

        self.set_title("Cầu nối sang trường hợp nhiều chiều", "(6-37)")
        r1 = mix("Bác bỏ", "$H_0$", "khi", r"$SS_{tr}/SS_{res}$", "lớn  ⇔  khi đại lượng sau NHỎ:", size=28)
        f = mt(r"\frac{1}{1+SS_{tr}/SS_{res}}=\frac{SS_{res}}{SS_{res}+SS_{tr}}", size=54)
        arrow = mt(r"\Downarrow", size=50, color=ACCENT)
        f2 = mt(r"\Lambda^*=\frac{|\mathbf W|}{|\mathbf B+\mathbf W|}", size=54, color=ACCENT)
        lab = vt("Wilks' lambda — sẽ học ở mục 6.4", size=24, color=ACCENT)
        VGroup(r1, f, arrow, f2, lab).arrange(DOWN, buff=0.35).next_to(self.title_mob, DOWN, buff=0.5)
        with self.say("Kiểm định ép tương đương với bác bỏ khi tỉ số S S xử lý trên S S phần dư lớn. Và điều này lại tương đương "
                      "với bác bỏ khi đại lượng nghịch đảo: S S phần dư chia cho S S phần dư cộng S S xử lý, là nhỏ."):
            self.play(FadeIn(r1))
            self.play(Write(f))
        with self.say("Hãy nhớ đại lượng này. Trong trường hợp nhiều chiều, các con số bình phương sẽ được thay bằng ma trận, "
                      "và tỉ số này trở thành lam-đa Uyn-xơ, công cụ trung tâm của ma-nô-va."):
            self.play(Write(arrow), Write(f2))
            self.play(FadeIn(lab))
        self.clear_all()
