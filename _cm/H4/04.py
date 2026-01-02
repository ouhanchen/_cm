import numpy as np

def root(c):
    """
    求解多項式 c[n]x^n + ... + c[1]x + c[0] = 0 的根
    c: 係數陣列 [c0, c1, c2, ..., cn]
    """
    # 1. 轉換為浮點數並移除高次的零係數
    c = np.trim_zeros(np.array(c, dtype=float), 'b')
    n = len(c) - 1
    
    if n < 1:
        return np.array([])
    
    # 2. 規格化：讓最高次項係數為 1
    # 這裡假設 c[n] 在陣列最後面，即 c = [c0, c1, ..., cn]
    lead_coeff = c[-1]
    coeffs = c[:-1] / lead_coeff
    
    # 3. 建立伴隨矩陣 (Companion Matrix)
    # 結構如下：
    # [[0, 0, ..., -c0],
    #  [1, 0, ..., -c1],
    #  [0, 1, ..., -c2]]
    A = np.eye(n, k=-1)
    A[:, -1] = -coeffs
    
    # 4. 求特徵值，即為多項式的根
    roots = np.linalg.eigvals(A)
    
    return roots

# 測試範例：x^5 - 1 = 0 (五次方根)
coeffs = [-1, 0, 0, 0, 0, 1]  # 代表 1*x^5 + 0*x^4 + ... - 1
print(f"多項式係數: {coeffs}")
print(f"求得的根:\n{root(coeffs)}")