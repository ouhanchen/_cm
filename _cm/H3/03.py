import cmath

def root3(a, b, c, d):
    if a == 0:
        # 如果 a=0，則退化為二次方程
        return solve_quadratic(b, c, d)

    # 1. 將方程化為簡化形式 (Depressed Cubic): t^3 + pt + q = 0
    # 令 x = t - b/(3a)
    p = (3*a*c - b**2) / (3 * a**2)
    q = (2*b**3 - 9*a*b*c + 27*a**2*d) / (27 * a**3)

    # 2. 計算判別式相關變量
    # 根據卡爾丹諾公式，令 t = u + v
    # 其中 u^3 + v^3 = -q 且 uv = -p/3
    delta = (q**2 / 4) + (p**3 / 27)
    
    # 3. 求出 u 和 v (使用複數開方)
    u3 = -q/2 + cmath.sqrt(delta)
    v3 = -q/2 - cmath.sqrt(delta)
    
    u = u3**(1/3)
    # 為了確保 uv = -p/3，我們需要精確選擇 v
    if abs(u) == 0:
        v = v3**(1/3)
    else:
        v = -p / (3 * u)

    # 4. 計算三個單位根 (1, omega, omega^2)
    w = cmath.exp(2j * cmath.pi / 3)
    
    # 5. 求出 t 的三個根
    t1 = u + v
    t2 = u * w + v * (w**2)
    t3 = u * (w**2) + v * w
    
    # 6. 回到 x = t - b/(3a)
    shift = b / (3 * a)
    roots = [t1 - shift, t2 - shift, t3 - shift]
    
    return roots

def solve_quadratic(a, b, c):
    """輔助函數：求解二次方程"""
    if a == 0:
        return [-c/b] if b != 0 else []
    d = cmath.sqrt(b**2 - 4*a*c)
    return [(-b + d) / (2*a), (-b - d) / (2*a)]

# --- 測試範例 ---
# 範例：x^3 - 6x^2 + 11x - 6 = 0 (根應為 1, 2, 3)
results = root3(1, -6, 11, -6)
print("根為：")
for i, r in enumerate(results, 1):
    # 格式化輸出，去除極小的虛部數值
    real = round(r.real, 10)
    imag = round(r.imag, 10)
    print(f"x{i} = {complex(real, imag)}")