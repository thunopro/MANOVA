"""Phần 2: Các thuật ngữ cần nắm (tổng hợp từ mục 6.4 và 6.7)."""
from common import *


def term_table(rows):
    data = [["Thuật ngữ", "Tiếng Anh / ký hiệu", "Ý nghĩa"]]
    for vi, en, mean in rows:
        data.append([vt(vi, size=24, weight=BOLD, color=GOLD),
                     en if isinstance(en, Mobject) else vt(en, size=22, color=ACCENT),
                     vt(mean, size=21)])
    return table(data, [3.9, 3.3, 6.0], row_h=0.74, size=24)


class S03_Terms(Lecture):
    section_label = "Phần 2 · Thuật ngữ"

    def construct(self):
        card = self.section_card("PHẦN 2", "Các thuật ngữ cần nắm", "Thống nhất ngôn ngữ trước khi vào MANOVA")
        with self.say("Phần hai. Trước khi vào ma-nô-va, ta thống nhất các thuật ngữ. Các em nên nắm chắc cả tên tiếng Việt "
                      "lẫn tên tiếng Anh, vì sách và phần mềm thống kê đều dùng tiếng Anh."):
            self.play(FadeIn(card, shift=UP * 0.3))
        self.play(FadeOut(card))

        self.set_title("Nhóm 1 — Thiết kế thí nghiệm")
        t = term_table([
            ("Biến phản hồi", "response variable", "Đại lượng đo được. MANOVA: vectơ p biến"),
            ("Nhân tố", "factor", "Điều kiện thí nghiệm dùng để phân nhóm"),
            ("Mức", "level", "Một giá trị cụ thể của nhân tố"),
            ("Xử lý / tổng thể", "treatment / population", "Mỗi mức (hay tổ hợp mức) là một nhóm"),
            ("Lặp", "replication (n)", "Số quan sát độc lập ở mỗi tổ hợp mức"),
            ("Mô hình hiệu ứng cố định", "fixed-effects model", "Các mức là cố định, chọn sẵn, không ngẫu nhiên"),
        ])
        self.fit(t)
        with self.say("Nhóm thứ nhất là các thuật ngữ thiết kế thí nghiệm. Biến phản hồi, response variable, là đại lượng ta đo. "
                      "Trong ma-nô-va, mỗi quan sát là một vectơ gồm pê biến phản hồi."):
            self.play(Create(t.lines), FadeIn(t.rows[0]))
            self.play(FadeIn(t.rows[1]))
        with self.say("Nhân tố, factor, là điều kiện thí nghiệm dùng để chia nhóm, ví dụ loại hình sở hữu của viện dưỡng lão, "
                      "hay tốc độ đùn của máy làm màng nhựa. Mức, level, là một giá trị cụ thể của nhân tố, "
                      "chẳng hạn tốc độ thấp hay tốc độ cao."):
            self.play(FadeIn(t.rows[2]))
            self.play(FadeIn(t.rows[3]))
        with self.say("Mỗi mức, hoặc mỗi tổ hợp mức khi có hai nhân tố, tạo thành một nhóm, gọi là một xử lý, treatment, hay một tổng thể. "
                      "Lặp, replication, là số quan sát độc lập ở mỗi tổ hợp mức, sách ký hiệu là en."):
            self.play(FadeIn(t.rows[4]))
            self.play(FadeIn(t.rows[5]))
        with self.say("Lưu ý, sách chú thích rằng chữ nhân tố ở đây chỉ là điều kiện thí nghiệm, không nhầm với nhân tố ẩn trong "
                      "phân tích nhân tố ở chương chín. Và các mô hình ta học đều là mô hình hiệu ứng cố định: "
                      "các mức được chọn sẵn, ta chỉ quan tâm đến chính các mức đó."):
            self.play(Indicate(t.rows[6], color=GOLD, scale_factor=1.03))
        self.clear_content()

        self.set_title("Nhóm 2 — Tham số của mô hình")
        t = term_table([
            ("Trung bình chung", mt(r"\boldsymbol\mu", size=34, color=BLUE), "Mức chung (overall mean / level)"),
            ("Hiệu ứng xử lý", mt(r"\boldsymbol\tau_\ell=\boldsymbol\mu_\ell-\boldsymbol\mu", size=34, color=GOLD),
             "Độ lệch của nhóm ℓ so với mức chung"),
            ("Hiệu ứng chính", mt(r"\text{main effect: }\boldsymbol\tau_\ell,\ \boldsymbol\beta_k", size=30, color=PURPLE), "Tác động riêng của nhân tố 1, nhân tố 2"),
            ("Tương tác", mt(r"\boldsymbol\gamma_{\ell k}", size=34, color=RED),
             "Hiệu ứng nhân tố 1 phụ thuộc mức của nhân tố 2"),
            ("Sai số ngẫu nhiên", mt(r"\mathbf e\sim N_p(\mathbf 0,\boldsymbol\Sigma)", size=34, color=GREEN),
             "Phần dao động không giải thích được"),
            ("Ma trận hiệp phương sai", mt(r"\boldsymbol\Sigma", size=34), "Giả định: như nhau ở mọi nhóm"),
        ])
        self.fit(t)
        with self.say("Nhóm thứ hai là các tham số của mô hình. Trung bình chung muy là mức nền. Hiệu ứng xử lý tau l bằng "
                      "muy l trừ muy, cho biết nhóm l lệch khỏi mức chung bao nhiêu."):
            self.play(Create(t.lines), FadeIn(t.rows[0]))
            self.play(FadeIn(t.rows[1]), FadeIn(t.rows[2]))
        with self.say("Khi có hai nhân tố, ta có hiệu ứng chính của nhân tố một là tau l, của nhân tố hai là bê-ta k. "
                      "Và hiệu ứng tương tác gam-ma l k: tác động của nhân tố này thay đổi tùy theo mức của nhân tố kia."):
            self.play(FadeIn(t.rows[3]), FadeIn(t.rows[4]))
        with self.say("Sai số ngẫu nhiên e có phân phối chuẩn pê chiều, trung bình không, ma trận hiệp phương sai xích-ma. "
                      "Một giả định quan trọng: xích-ma là như nhau ở mọi nhóm."):
            self.play(FadeIn(t.rows[5]), FadeIn(t.rows[6]))
        self.clear_content()

        self.set_title("Nhóm 3 — Đại lượng tính toán và kiểm định")
        t = term_table([
            ("Tổng bình phương", "SS — sum of squares", "Độ lớn (độ dài bình phương) của một mảng"),
            ("Bậc tự do", "degrees of freedom", "Số chiều mà thành phần được tự do biến thiên"),
            ("Giữa / trong nhóm", "between / within", "Khác biệt giữa các nhóm / dao động trong nhóm"),
            ("Ma trận SSP", "SSP matrix",
             "Đường chéo: SS từng biến; ngoài: tích chéo"),
            ("B và W", mt(r"\mathbf B,\ \mathbf W", size=34, color=ACCENT), "SSP xử lý (between) và SSP phần dư (within)"),
            ("Phương sai tổng quát", mt(r"|\mathbf W|,\ |\mathbf B+\mathbf W|", size=32), "Định thức của ma trận SSP"),
            ("Lambda của Wilks", mt(r"\Lambda^*=|\mathbf W|/|\mathbf B+\mathbf W|", size=32, color=GOLD),
             "Nhỏ ⇒ bác bỏ H₀ (có hiệu ứng)"),
        ])
        self.fit(t)
        with self.say("Nhóm thứ ba là các đại lượng tính toán. Tổng bình phương S S, bậc tự do, và hai khái niệm giữa nhóm, "
                      "trong nhóm, các em đã gặp ở phần a-nô-va."):
            self.play(Create(t.lines), FadeIn(t.rows[0]))
            self.play(FadeIn(t.rows[1]), FadeIn(t.rows[2]), FadeIn(t.rows[3]))
        with self.say("Trong ma-nô-va, mỗi tổng bình phương được thay bằng một ma trận tổng bình phương và tích chéo, viết tắt S S P. "
                      "Đường chéo của nó là tổng bình phương của từng biến, còn ngoài đường chéo là tổng các tích chéo giữa hai biến. "
                      "Ma trận bê là S S P của xử lý, còn ma trận đáp-bờ-liu là S S P phần dư."):
            self.play(FadeIn(t.rows[4]), FadeIn(t.rows[5]))
        with self.say("Để so sánh hai ma trận, ta dùng định thức, gọi là phương sai tổng quát. Và tỉ số giữa định thức của đáp-bờ-liu với "
                      "định thức của bê cộng đáp-bờ-liu chính là lam-đa Uyn-xơ. Lam-đa nhỏ nghĩa là có hiệu ứng, ta bác bỏ giả thuyết không."):
            self.play(FadeIn(t.rows[6]), FadeIn(t.rows[7]))
            self.play(FadeIn(row_highlight(t, 7)))
        self.clear_content()

        self.set_title("Quy ước màu trong bài giảng")
        items = [
            (BLUE, "Trung bình chung", r"\bar{\mathbf x}"),
            (GOLD, "Hiệu ứng xử lý / nhân tố 1", r"\bar{\mathbf x}_\ell-\bar{\mathbf x}"),
            (PURPLE, "Nhân tố 2", r"\bar{\mathbf x}_{\cdot k}-\bar{\mathbf x}"),
            (RED, "Tương tác", r"\bar{\mathbf x}_{\ell k}-\bar{\mathbf x}_{\ell\cdot}-\bar{\mathbf x}_{\cdot k}+\bar{\mathbf x}"),
            (GREEN, "Phần dư", r"\mathbf x_{\ell j}-\bar{\mathbf x}_\ell"),
        ]
        rows = VGroup()
        for c, name, tex in items:
            sw = RoundedRectangle(width=0.5, height=0.5, corner_radius=0.08, fill_color=c, fill_opacity=1, stroke_width=0)
            rows.add(VGroup(sw, vt(name, size=28, color=c), mt(tex, size=36, color=c)).arrange(RIGHT, buff=0.4))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        self.fit(rows, top_buff=0.6)
        with self.say("Để dễ theo dõi, bài giảng dùng một quy ước màu thống nhất. Màu xanh dương cho trung bình chung, màu vàng cho hiệu ứng "
                      "xử lý hoặc nhân tố một, màu tím cho nhân tố hai, màu đỏ cho tương tác, và màu xanh lá cho phần dư."):
            self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.3) for r in rows], lag_ratio=0.35), run_time=4)
        self.clear_all()
