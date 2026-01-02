import numpy as np
import math

class InformationTheoryTool:
    def __init__(self):
        pass

    # --- 1. 機率與對數計算 ---
    def calculate_coin_probability(self, n=10000):
        print(f"--- 1. 投擲 {n} 次公平銅板 ---")
        # 直接計算
        try:
            p_direct = 0.5 ** n
        except OverflowError:
            p_direct = 0.0
            
        # 對數計算
        log_p_n = n * math.log2(0.5)
        
        print(f"直接計算結果 (p^n): {p_direct}")
        print(f"對數計算結果 log2(p^n): {log_p_n} bits")
        print(f"這代表機率極小，接近 2 的 {log_p_n} 次方\n")

    # --- 2. 資訊理論核心指標 ---
    def entropy(self, p):
        p = np.array(p)
        return -np.sum(p * np.log2(p + 1e-12))

    def cross_entropy(self, p, q):
        p, q = np.array(p), np.array(q)
        return -np.sum(p * np.log2(q + 1e-12))

    def kl_divergence(self, p, q):
        return self.cross_entropy(p, q) - self.entropy(p)

    def verify_gibbs_inequality(self):
        print("--- 2. 驗證交叉熵不等式 H(p,p) vs H(p,q) ---")
        p = [0.3, 0.7]
        q = [0.1, 0.9]
        h_pp = self.cross_entropy(p, p)
        h_pq = self.cross_entropy(p, q)
        print(f"當 p={p}, q={q} 時:")
        print(f"H(p, p) = {h_pp:.4f}")
        print(f"H(p, q) = {h_pq:.4f}")
        print(f"驗證 H(p,p) < H(p,q): {h_pp < h_pq}\n")

    # --- 3. 7-4 漢明碼實作 ---
    def hamming_74_demo(self, data_bits=[1, 0, 1, 1]):
        print(f"--- 3. 7-4 漢明碼編解碼 (輸入資料: {data_bits}) ---")
        # 生成矩陣 G 與 檢查矩陣 H
        G = np.array([[1,1,0,1], [1,0,1,1], [1,0,0,0], [0,1,1,1], [0,1,0,0], [0,0,1,0], [0,0,0,1]])
        H = np.array([[1,0,1,0,1,0,1], [0,1,1,0,0,1,1], [0,0,0,1,1,1,1]])
        
        # 編碼
        encoded = np.dot(G, data_bits) % 2
        print(f"編碼後的位元 (7位): {encoded}")
        
        # 模擬錯誤：翻轉第 3 個位元 (index 2)
        error_idx = 2
        encoded[error_idx] = 1 - encoded[error_idx]
        print(f"模擬傳輸錯誤 (翻轉 index {error_idx}): {encoded}")
        
        # 解碼與修正
        syndrome = np.dot(H, encoded) % 2
        error_pos = int(syndrome[0] + syndrome[1]*2 + syndrome[2]*4)
        
        if error_pos != 0:
            print(f"偵測到錯誤！位置在第 {error_pos} 位，正在修復...")
            encoded[error_pos-1] = 1 - encoded[error_pos-1]
            
        decoded = np.array([encoded[2], encoded[4], encoded[5], encoded[6]])
        print(f"修復後的資料位元: {decoded}\n")

# --- 執行整合腳本 ---
if __name__ == "__main__":
    tool = InformationTheoryTool()
    
    # 執行任務 1
    tool.calculate_coin_probability(10000)
    
    # 執行任務 2
    tool.verify_gibbs_inequality()
    
    # 執行任務 3
    tool.hamming_74_demo([1, 1, 0, 1])