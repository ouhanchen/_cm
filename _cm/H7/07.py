import numpy as np
from scipy import stats

# 1. 模擬數據產生 (設定母體平均值為 100)
np.random.seed(42)
data = np.random.normal(loc=105, scale=15, size=30)  # 樣本平均值會接近 105

# 2. 設定虛無假設 H0: mu = 100
mu_0 = 100
n = len(data)

# ---------------------------------------------------------
# 手動推導單樣本 t 檢定 (Manual Calculation)
# ---------------------------------------------------------
sample_mean = np.mean(data)
sample_std = np.std(data, ddof=1)  # ddof=1 代表樣本標準差 (n-1)
standard_error = sample_std / np.sqrt(n)

# t 公式: (樣本平均 - 假設平均) / 標準誤差
t_stat_manual = (sample_mean - mu_0) / standard_error

# ---------------------------------------------------------
# 使用 Scipy 套件驗證
# ---------------------------------------------------------
t_stat_scipy, p_value = stats.ttest_1samp(data, mu_0)

print(f"--- 驗證結果 ---")
print(f"樣本平均值: {sample_mean:.4f}")
print(f"手動計算的 t 統計量: {t_stat_manual:.4f}")
print(f"Scipy 計算的 t 統計量: {t_stat_scipy:.4f}")
print(f"P 值 (顯著性): {p_value:.4f}")

if p_value < 0.05:
    print("\n結論: P < 0.05，拒絕虛無假設 (有顯著差異)")
else:
    print("\n結論: P >= 0.05，無法拒絕虛無假設 (無顯著差異)")