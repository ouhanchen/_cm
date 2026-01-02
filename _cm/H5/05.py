import math

# ==========================================
# 1. 有限體元素類別 (類似 rational_number.py)
# ==========================================
class Fp:
    p = 13  # 定義模數 (需為質數)

    def __init__(self, value):
        if isinstance(value, Fp):
            self.value = value.value
        else:
            self.value = value % Fp.p

    def __add__(self, other):
        return Fp(self.value + Fp(other).value)

    def __sub__(self, other):
        return Fp(self.value - Fp(other).value)

    def __mul__(self, other):
        return Fp(self.value * Fp(other).value)

    def __truediv__(self, other):
        other = Fp(other)
        if other.value == 0:
            raise ZeroDivisionError("有限體除法中除數不能為 0")
        # 使用費馬小定理求逆元素：a^(p-2) % p
        return self * (other ** (Fp.p - 2))

    def __pow__(self, exponent):
        # 使用 Python 內建的三參數 pow(base, exp, mod) 效率最高
        return Fp(pow(self.value, exponent, Fp.p))

    def __eq__(self, other):
        if not isinstance(other, Fp):
            other = Fp(other)
        return self.value == other.value

    def __repr__(self):
        return str(self.value)

# ==========================================
# 2. 群公理驗證器 (類似 group_axioms.py)
# ==========================================
def check_group_axioms(group):
    elements = group.elements
    op = group.op
    identity = group.identity
    
    print(f"--- 正在驗證群公理: {group.__class__.__name__} (元素數量: {len(elements)}) ---")
    
    # 1. 封閉性 (Closure) - 簡化驗證
    for a in elements:
        for b in elements:
            res = op(a, b)
            if res not in elements:
                raise Exception(f"違反封閉性: {a} op {b} = {res}")
    print("OK: 封閉性通過")

    # 2. 結合律 (Associativity)
    a, b, c = elements[1], elements[2], elements[3]
    if op(op(a, b), c) == op(a, op(b, c)):
        print(f"OK: 結合律通過 ({a}, {b}, {c})")
    else:
        raise Exception("違反結合律")

    # 3. 單位元 (Identity)
    for a in elements:
        if not (op(a, identity) == a and op(identity, a) == a):
            raise Exception(f"違反單位元性質: {a}")
    print(f"OK: 單位元驗證通過 (Identity = {identity})")

    # 4. 反元素 (Inverse)
    for a in elements:
        inv_a = group.inv(a)
        if not (op(a, inv_a) == identity):
            raise Exception(f"違反反元素性質: {a}")
    print("OK: 反元素驗證通過")
    print("結果: 該結構符合群公理!\n")

# ==========================================
# 3. 有限體的群結構包裝 (參考 field_rational.py)
# ==========================================
class FpAddGroup:
    def __init__(self, p):
        Fp.p = p
        self.elements = [Fp(i) for i in range(p)]
        self.identity = Fp(0)
    
    def op(self, a, b): return a + b
    def inv(self, a): return Fp(-a.value)

class FpMulGroup:
    def __init__(self, p):
        Fp.p = p
        # 乘法群排除 0
        self.elements = [Fp(i) for i in range(1, p)]
        self.identity = Fp(1)
    
    def op(self, a, b): return a * b
    def inv(self, a): return a ** (Fp.p - 2)

# ==========================================
# 4. 分配律驗證 (參考 field_axioms.py)
# ==========================================
def check_distributivity(a, b, c):
    left = a * (b + c)
    right = (a * b) + (a * c)
    print(f"分配律驗證: {a}*({b}+{c}) = {left}")
    assert left == right
    print("OK: 分配律通過\n")

# ==========================================
# 主程式執行
# ==========================================
if __name__ == "__main__":
    P_VALUE = 13
    
    # 驗證加法群
    add_group = FpAddGroup(P_VALUE)
    check_group_axioms(add_group)
    
    # 驗證乘法群 (不含0)
    mul_group = FpMulGroup(P_VALUE)
    check_group_axioms(mul_group)
    
    # 驗證分配律
    a, b, c = Fp(3), Fp(7), Fp(10)
    check_distributivity(a, b, c)
    
    # 示範四則運算
    x = Fp(5)
    y = Fp(8)
    print(f"示範運算 (p={P_VALUE}):")
    print(f"{x} + {y} = {x + y}")
    print(f"{x} - {y} = {x - y}")
    print(f"{x} * {y} = {x * y}")
    print(f"{x} / {y} = {x / y}  (因為 {x/y} * {y} = {(x/y)*y})")