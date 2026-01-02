import cmath

def dft(f):
    """離散傅立葉正轉換"""
    N = len(f)
    F = [0] * N
    for k in range(N):
        for n in range(N):
            # 指數部分: -i * 2 * pi * k * n / N
            angle = -2j * cmath.pi * k * n / N
            F[k] += f[n] * cmath.exp(angle)
    return F

def idft(F):
    """離散傅立葉逆轉換"""
    N = len(F)
    f = [0] * N
    for n in range(N):
        for k in range(N):
            # 指數部分: i * 2 * pi * k * n / N
            angle = 2j * cmath.pi * k * n / N
            f[n] += F[k] * cmath.exp(angle)
        # 能量歸一化 (對應連續公式的 1/2pi)
        f[n] /= N
    return f

# --- 驗證邏輯 ---

# 1. 定義一個原始函數 f (例如一個簡單的序列)
original_f = [1.0, 2.0, 3.0, 4.0]
print(f"原始函數 f: {original_f}")

# 2. 執行正轉換
F_omega = dft(original_f)
print("\n正轉換後的 F(ω) (前兩個點):")
print(F_omega[:2])

# 3. 執行逆轉換
recovered_f = idft(F_omega)

# 4. 輸出結果與比對
print("\n逆轉換回來的 f':")
# 由於浮點數運算會有極小誤差，我們只取實部並四捨五入
formatted_f = [round(x.real, 10) for x in recovered_f]
print(formatted_f)

# 驗證兩者是否相等
is_same = all(abs(o - r.real) < 1e-10 for o, r in zip(original_f, recovered_f))
print(f"\n驗證結果: {'成功' if is_same else '失敗'}")