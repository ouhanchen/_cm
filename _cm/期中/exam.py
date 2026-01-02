def is_prime(n):
    """判斷一個數字是否為質數"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # 使用 6k ± 1 優化演算法
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes_in_range(start, end):
    """找出特定範圍內的所有質數"""
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return primes

# 程式執行入口
if __name__ == "__main__":
    num = int(input("請輸入一個整數來檢查是否為質數: "))
    if is_prime(num):
        print(f"{num} 是質數！")
    else:
        print(f"{num} 不是質數。")

    limit = int(input("接著，你想搜尋從 1 到多少之間的質數？ "))
    result = find_primes_in_range(1, limit)
    print(f"1 到 {limit} 之間的質數有：\n{result}")