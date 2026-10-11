"""Thực hành: tính lại Ví dụ 6.9 (one-way MANOVA) và Ví dụ 6.13 (two-way MANOVA)
trong Johnson & Wichern, Applied Multivariate Statistical Analysis (6th ed.), chương 6.

Chạy:  python thuc_hanh_manova.py
"""
import numpy as np
from scipy import stats


def wilks(E, H):
    return np.linalg.det(E) / np.linalg.det(E + H)


# ---------------------------------------------------------------- Ví dụ 6.9
print("=" * 60, "\nVÍ DỤ 6.9 - One-way MANOVA, g = 3, p = 2")
groups = [
    np.array([[9, 3], [6, 2], [9, 7]]),
    np.array([[0, 4], [2, 0]]),
    np.array([[3, 8], [1, 9], [2, 7]]),
]
allx = np.vstack(groups)
xbar = allx.mean(axis=0)
n = len(allx); g = len(groups); p = allx.shape[1]
B = sum(len(G) * np.outer(G.mean(0) - xbar, G.mean(0) - xbar) for G in groups)
W = sum((G - G.mean(0)).T @ (G - G.mean(0)) for G in groups)
T = (allx - xbar).T @ (allx - xbar)
print("x̄ =", xbar)
print("B (treatment) =\n", B)
print("W (residual)  =\n", W)
print("B + W (total) =\n", T)
lam = wilks(W, B)
F = (1 - np.sqrt(lam)) / np.sqrt(lam) * (n - g - 1) / (g - 1)
print(f"Wilks' Lambda = {lam:.4f}")
print(f"F = {F:.2f}, F_(4,8)(0.01) = {stats.f.ppf(0.99, 2*(g-1), 2*(n-g-1)):.2f}")

# ---------------------------------------------------------------- Ví dụ 6.13
print("=" * 60, "\nVÍ DỤ 6.13 - Two-way MANOVA (plastic film), g = b = 2, n = 5, p = 3")
# data[l][k] : nhân tố 1 mức l (tốc độ đùn: thấp, cao), nhân tố 2 mức k (phụ gia: thấp, cao)
data = np.array([
    [[[6.5, 9.5, 4.4], [6.2, 9.9, 6.4], [5.8, 9.6, 3.0], [6.5, 9.6, 4.1], [6.5, 9.2, 0.8]],
     [[6.9, 9.1, 5.7], [7.2, 10.0, 2.0], [6.9, 9.9, 3.9], [6.1, 9.5, 1.9], [6.3, 9.4, 5.7]]],
    [[[6.7, 9.1, 2.8], [6.6, 9.3, 4.1], [7.2, 8.3, 3.8], [7.1, 8.4, 1.6], [6.8, 8.5, 3.4]],
     [[7.1, 9.2, 8.4], [7.0, 8.8, 5.2], [7.2, 9.7, 6.9], [7.5, 10.1, 2.7], [7.6, 9.2, 1.9]]],
])
g, b, n, p = data.shape
xbar = data.mean(axis=(0, 1, 2))
xl = data.mean(axis=(1, 2))          # x̄_l.
xk = data.mean(axis=(0, 2))          # x̄_.k
xlk = data.mean(axis=2)              # x̄_lk
op = np.outer
SSP_f1 = sum(b * n * op(xl[l] - xbar, xl[l] - xbar) for l in range(g))
SSP_f2 = sum(g * n * op(xk[k] - xbar, xk[k] - xbar) for k in range(b))
SSP_int = sum(n * op(d, d) for l in range(g) for k in range(b)
              for d in [xlk[l, k] - xl[l] - xk[k] + xbar])
SSP_res = sum(op(d, d) for l in range(g) for k in range(b) for r in range(n)
              for d in [data[l, k, r] - xlk[l, k]])
SSP_cor = sum(op(d, d) for d in (data.reshape(-1, p) - xbar))
np.set_printoptions(precision=4, suppress=True)
for name, M in [("SSP_fac1", SSP_f1), ("SSP_fac2", SSP_f2), ("SSP_int", SSP_int),
                ("SSP_res", SSP_res), ("SSP_cor", SSP_cor)]:
    print(name, "=\n", M)
nu2 = g * b * (n - 1) - p + 1
for name, H, df in [("Tương tác", SSP_int, (g - 1) * (b - 1)),
                    ("Nhân tố 1", SSP_f1, g - 1), ("Nhân tố 2", SSP_f2, b - 1)]:
    lam = wilks(SSP_res, H)
    nu1 = abs(df - p) + 1
    F = (1 - lam) / lam * (nu2 / 2) / (nu1 / 2)
    chi = -(g * b * (n - 1) - (p + 1 - df) / 2) * np.log(lam)
    print(f"{name}: Lambda* = {lam:.4f}, F = {F:.2f} ~ F({nu1},{nu2}), "
          f"F_crit(0.05) = {stats.f.ppf(0.95, nu1, nu2):.2f}, p-value = {stats.f.sf(F, nu1, nu2):.4f}, "
          f"Bartlett chi2 = {chi:.2f} (crit {stats.chi2.ppf(0.95, df * p):.2f})")
print("|SSP_res| =", round(np.linalg.det(SSP_res), 4),
      " |SSP_int + SSP_res| =", round(np.linalg.det(SSP_int + SSP_res), 4))

# ---------------------------------------------------------------- Kiểm chứng bằng statsmodels
# f1: tốc độ đùn (0 = thấp, 1 = cao), f2: lượng phụ gia (0 = thấp, 1 = cao)
try:
    import pandas as pd
    from pathlib import Path
    from statsmodels.multivariate.manova import MANOVA

    df = pd.read_csv(Path(__file__).with_name("plastic_film.csv"))
    m = MANOVA.from_formula("x1 + x2 + x3 ~ C(f1, Sum) * C(f2, Sum)", data=df)
    print("=" * 60, "\nstatsmodels MANOVA (Ví dụ 6.13)")
    print(m.mv_test())
except ImportError:
    print("Cài thêm: pip install pandas statsmodels để chạy phần kiểm chứng")
