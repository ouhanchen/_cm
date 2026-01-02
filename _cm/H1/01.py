import math

# 定義數值微分：使用對稱差分法 (Symmetric Difference Quotient)
def df(f, x, h=1e-7):
    return (f(x + h) - f(x - h)) / (2 * h)

# 定義數值積分：使用黎曼和（中點法）
def integral(f, a, b, n=100000):
    if a == b: return 0
    h = (b - a) / n
    total_sum = 0
    for i in range(n):
        # 取中點
        mid = a + (i + 0.5) * h
        total_sum += f(mid)
    return total_sum * h

# 驗證微積分基本定理
def theorem1(f, x, tol=1e-5):
    # 定義變數上限函數 F(x) = ∫[0, x] f(t) dt
    F = lambda x_val: integral(f, 0, x_val)
    
    # 計算 d/dx F(x)
    derivative_of_integral = df(F, x)
    
    # 取得原始函數值 f(x)
    actual_f_x = f(x)
    
    # 驗證兩者是否接近
    is_verified = math.isclose(derivative_of_integral, actual_f_x, rel_tol=tol)
    
    print(f"在 x = {x} 處：")
    print(f"d/dx [∫f(t)dt] = {derivative_of_integral:.6f}")
    print(f"f(x)             = {actual_f_x:.6f}")
    print(f"驗證結果：{'通過' if is_verified else '失敗'}")
    
    return is_verified

# --- 測試案例 ---
# 測試 f(t) = t^2，理論上其積分的導數應為 x^2
print("測試 f(x) = x^2")
theorem1(lambda x: x**2, 3.0)

print("\n測試 f(x) = sin(x)")
theorem1(lambda x: math.sin(x), math.pi / 4)