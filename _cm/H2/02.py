import cmath

def root2(a, b, c):
    """
    求解二次多項式 ax^2 + bx + c = 0 的根。
    回傳：(x1, x2) 兩個根的元組
    """
    # 計算判別式 D = b^2 - 4ac
    d = (b**2) - (4*a*c)
    
    # 使用 cmath.sqrt 處理，無論實數或複數皆適用
    sol1 = (-b + cmath.sqrt(d)) / (2 * a)
    sol2 = (-b - cmath.sqrt(d)) / (2 * a)
    
    return sol1, sol2

# --- 驗證與測試 ---

def verify_roots(a, b, c):
    # 呼叫求根函數
    roots = root2(a, b, c)
    print(f"方程式: {a}x² + {b}x + {c} = 0")
    
    for i, x in enumerate(roots, 1):
        # 計算 f(x) = ax^2 + bx + c
        f_x = a * (x**2) + b * x + c
        
        # 驗證是否接近於 0
        is_zero = cmath.isclose(f_x, 0, abs_tol=1e-9)
        
        print(f"根 x{i} = {x}")
        print(f"f(x{i}) = {f_x}")
        print(f"驗證結果 (是否接近0): {is_zero}")
        print("-" * 30)

# 測試 1: 實數根
verify_roots(1, -3, 2)  # x^2 - 3x + 2 = 0, 根應該是 2, 1

# 測試 2: 複數根 (b^2 - 4ac < 0)
verify_roots(1, 1, 1)   # x^2 + x + 1 = 0