import numpy as np
from collections import Counter

def solve_ode_general(coefficients):
    """
    求解常係數齊次常微分方程 (Linear Homogeneous ODE with Constant Coefficients)
    coefficients: 係數列表 [a_n, a_{n-1}, ..., a_0]
    """
    # 1. 求解特徵方程的根 (characteristic equation: a_n*r^n + ... + a_0 = 0)
    roots = np.roots(coefficients)
    
    # 2. 處理浮點數誤差：將非常接近 0 的虛部或實部捨去，並對根進行四捨五入以便統計重根
    # 使用 round 定義精度，避免因為 2.000000000001 和 1.999999999999 被視為不同根
    rounded_roots = [complex(round(r.real, 6), round(r.imag, 6)) for r in roots]
    
    # 3. 統計每個根出現的次數（重數）
    root_counts = Counter(rounded_roots)
    
    # 儲存結果字串的列表
    terms = []
    c_index = 1
    
    # 為了處理複數共軛對，我們記錄已經處理過的根
    processed_roots = set()
    
    # 排序根，讓輸出結果較美觀（先實部後虛部）
    unique_roots = sorted(root_counts.keys(), key=lambda x: (x.real, x.imag), reverse=True)

    for r in unique_roots:
        if r in processed_roots:
            continue
            
        real_part = r.real
        imag_part = r.imag
        multiplicity = root_counts[r]
        
        # 情況 A: 實數根 (虛部極小)
        if abs(imag_part) < 1e-6:
            for m in range(multiplicity):
                x_pow = f"x^{m}" if m > 1 else ("x" if m == 1 else "")
                terms.append(f"C_{c_index}{x_pow}e^({real_part}x)")
                c_index += 1
            processed_roots.add(r)
            
        # 情況 B: 複數共軛根 (alpha +/- beta*i)
        else:
            # 尋找對應的共軛根
            conj_r = complex(real_part, -imag_part)
            # 在複數平面，我們只處理正虛部的那一個，一次生成 sin 和 cos
            if imag_part > 0:
                beta = imag_part
                alpha = real_part
                
                for m in range(multiplicity):
                    x_pow = f"x^{m}" if m > 1 else ("x" if m == 1 else "")
                    # 處理 e^(alpha*x) 的顯示，若 alpha 為 0 則省略
                    e_part = f"e^({alpha}x)" if abs(alpha) > 1e-6 else ""
                    
                    terms.append(f"C_{c_index}{x_pow}{e_part}cos({beta}x)")
                    c_index += 1
                    terms.append(f"C_{c_index}{x_pow}{e_part}sin({beta}x)")
                    c_index += 1
                
                processed_roots.add(r)
                processed_roots.add(conj_r)

    return "y(x) = " + " + ".join(terms)

# --- 以下是測試主程式 ---
if __name__ == "__main__":
    # 範例測試 (1): 實數單根
    print("--- 實數單根範例 ---")
    coeffs1 = [1, -3, 2]
    print(f"方程係數: {coeffs1}")
    print(solve_ode_general(coeffs1))

    # 範例測試 (2): 實數重根
    print("\n--- 實數重根範例 ---")
    coeffs2 = [1, -4, 4]
    print(f"方程係數: {coeffs2}")
    print(solve_ode_general(coeffs2))

    # 範例測試 (3): 複數共軛根
    print("\n--- 複數共軛根範例 ---")
    coeffs3 = [1, 0, 4]
    print(f"方程係數: {coeffs3}")
    print(solve_ode_general(coeffs3))

    # 範例測試 (4): 複數重根
    print("\n--- 複數重根範例 ---")
    coeffs4 = [1, 0, 2, 0, 1]
    print(f"方程係數: {coeffs4}")
    print(solve_ode_general(coeffs4))

    # 範例測試 (5): 高階重根
    print("\n--- 高階重根範例 ---")
    coeffs5 = [1, -6, 12, -8]
    print(f"方程係數: {coeffs5}")
    print(solve_ode_general(coeffs5))