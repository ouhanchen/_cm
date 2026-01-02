import numpy as np

# 1. 遞迴計算行列式
def recursive_det(matrix):
    n = len(matrix)
    if n == 1: return matrix[0][0]
    if n == 2: return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    
    det = 0
    for c in range(n):
        minor = np.delete(np.delete(matrix, 0, axis=0), c, axis=1)
        det += ((-1)**c) * matrix[0][c] * recursive_det(minor)
    return det

# 2. LU 分解計算行列式
def lu_det(A):
    from scipy.linalg import lu
    P, L, U = lu(A)
    # det(A) = det(P) * det(L) * det(U)
    # P 的行列式取決於交換次數 (+1 或 -1)
    return np.prod(np.diag(U)) * np.linalg.det(P)

# 3. 驗證分解與還原
def verify_decompositions():
    A = np.array([[4, 11], [1, 2]], dtype=float)
    
    # Eigen Decomposition (僅限對稱或方陣)
    evals, evecs = np.linalg.eig(A)
    A_eig = evecs @ np.diag(evals) @ np.linalg.inv(evecs)
    
    # SVD
    U, S, Vt = np.linalg.svd(A)
    A_svd = U @ np.diag(S) @ Vt
    
    print(f"Original A:\n{A}")
    print(f"Reconstructed from SVD:\n{A_svd}")

# 4. PCA 實作 (使用 SVD)
def do_pca(data, k=1):
    # 去中心化
    data_centered = data - np.mean(data, axis=0)
    # SVD
    U, S, Vt = np.linalg.svd(data_centered)
    # 投影到前 k 個主成分
    return data_centered @ Vt.T[:, :k]

# 測試
A_test = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9+1e-9]]) # 加微小值避免奇異矩陣
print("Recursive Det:", recursive_det(A_test))
verify_decompositions()