import math

# --- 1. 基礎幾何物件定義 ---

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __repr__(self):
        return f"({self.x:.2f}, {self.y:.2f})"

class Line:
    """使用一般式 Ax + By + C = 0 表示直線"""
    def __init__(self, p1, p2):
        self.a = p1.y - p2.y
        self.b = p2.x - p1.x
        self.c = p1.x * p2.y - p2.x * p1.y

class Circle:
    def __init__(self, center, r):
        self.center = center
        self.r = r

class Triangle:
    def __init__(self, p1, p2, p3):
        self.points = [p1, p2, p3]
    
    def __repr__(self):
        return f"Triangle{self.points}"

    def translate(self, dx, dy):
        for p in self.points:
            p.x += dx
            p.y += dy

    def rotate(self, angle_deg, center=Point(0,0)):
        rad = math.radians(angle_deg)
        cos_a, sin_a = math.cos(rad), math.sin(rad)
        for p in self.points:
            tx, ty = p.x - center.x, p.y - center.y
            p.x = tx * cos_a - ty * sin_a + center.x
            p.y = tx * sin_a + ty * cos_a + center.y

# --- 2. 運算核心 ---

def intersect_lines(l1, l2):
    det = l1.a * l2.b - l2.a * l1.b
    if abs(det) < 1e-9: return None
    return Point((l1.b * l2.c - l2.b * l1.c) / det, (l2.a * l1.c - l1.a * l2.c) / det)

def get_foot_of_perpendicular(p, line):
    """計算點到直線的垂足"""
    a, b, c = line.a, line.b, line.c
    temp = -(a * p.x + b * p.y + c) / (a**2 + b**2)
    return Point(p.x + a * temp, p.y + b * temp)

def intersect_line_circle(line, circle):
    """計算直線與圓的交點"""
    foot = get_foot_of_perpendicular(circle.center, line)
    d2 = (foot.x - circle.center.x)**2 + (foot.y - circle.center.y)**2
    r2 = circle.r**2
    if d2 > r2: return []
    if math.isclose(d2, r2): return [foot]
    
    h = math.sqrt(r2 - d2)
    vx, vy = line.b, -line.a
    mag = math.sqrt(vx**2 + vy**2)
    vx, vy = vx/mag, vy/mag
    return [Point(foot.x + vx*h, foot.y + vy*h), Point(foot.x - vx*h, foot.y - vy*h)]

# --- 3. 整合驗證主程式 ---

def run_geometry_test():
    print("=== 1. 交點測試 ===")
    l1 = Line(Point(0, 0), Point(10, 10)) # y = x
    l2 = Line(Point(0, 10), Point(10, 0)) # y = -x + 10
    c1 = Circle(Point(5, 5), 3)
    
    print(f"直線 L1 與 L2 交點: {intersect_lines(l1, l2)}")
    print(f"直線 L1 與 圓 C1 交點: {intersect_line_circle(l1, c1)}")

    print("\n=== 2. 垂足與畢氏定理驗證 ===")
    A = Point(3, 4)           # 線外一點
    L = Line(Point(0,0), Point(10,0)) # X 軸
    P = get_foot_of_perpendicular(A, L)
    B = Point(0, 0)           # 線上另一點
    
    # 計算距離平方
    dist_sq = lambda p1, p2: (p1.x-p2.x)**2 + (p1.y-p2.y)**2
    ap2, pb2, ab2 = dist_sq(A, P), dist_sq(P, B), dist_sq(A, B)
    
    print(f"線外點 A: {A}, 垂足 P: {P}, 線上點 B: {B}")
    print(f"AP^2 + PB^2 = {ap2 + pb2:.2f}")
    print(f"斜邊 AB^2   = {ab2:.2f}")
    print(f"驗證結果: {'成功' if math.isclose(ap2 + pb2, ab2) else '失敗'}")

    print("\n=== 3. 三角形變換測試 ===")
    tri = Triangle(Point(0,0), Point(2,0), Point(1,2))
    print(f"初始三角形: {tri}")
    tri.translate(5, 5)
    print(f"平移 (+5, +5) 後: {tri}")
    tri.rotate(90, center=Point(5,5))
    print(f"繞 (5,5) 旋轉 90 度後: {tri}")

if __name__ == "__main__":
    run_geometry_test()