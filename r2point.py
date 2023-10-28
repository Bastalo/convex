from math import sqrt


class R2Point:
    """ Точка (Point) на плоскости (R2) """

    # Конструктор
    def __init__(self, x=None, y=None):
        if x is None:
            x = float(input("x -> "))
        if y is None:
            y = float(input("y -> "))
        self.x, self.y = x, y

    # Площадь треугольника
    @staticmethod
    def area(a, b, c):
        return 0.5 * ((a.x - c.x) * (b.y - c.y) - (a.y - c.y) * (b.x - c.x))

    # Лежат ли точки на одной прямой?
    @staticmethod
    def is_triangle(a, b, c):
        return R2Point.area(a, b, c) != 0.0

    # Расстояние до другой точки
    def dist(self, other):
        return sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

    # Лежит ли точка внутри "стандартного" прямоугольника?
    def is_inside(self, a, b):
        return (((a.x <= self.x and self.x <= b.x) or
                 (a.x >= self.x and self.x >= b.x)) and
                ((a.y <= self.y and self.y <= b.y) or
                 (a.y >= self.y and self.y >= b.y)))

    # Вычисление длины части отрезка лежащей внутри "стандартного"
    # прямоугольника ()
    @staticmethod
    def new_dist(p, q, k, m):
        d = 0.0
        a = R2Point(0.0, 0.0)
        b = R2Point(0.0, 0.0)
        y_min = min(k.y, m.y)
        y_max = max(k.y, m.y)
        x_min = min(k.x, m.x)
        x_max = max(k.x, m.x)
        if q.is_inside(k, m) and p.is_inside(k, m):
            return p.dist(q)
        if q.is_inside(k, m) and not p.is_inside(k, m):
            p, q = q, p
        if p.x != q.x:
            k_1 = (p.y - q.y)/(p.x - q.x)
            b_1 = (p.x * q.y - p.y * q.x)/(p.x - q.x)
        else:
            k_1 = 0
            b_1 = p.x
        if k_1 != 0:
            if y_min <= k_1 * x_max + b_1 <= y_max and \
                    (p.x <= x_max <= q.x or q.x <= x_max <= p.x):
                a = R2Point(x_max, k_1 * x_max + b_1)
                if p.is_inside(k, m):
                    b = p
                else:
                    if y_min <= k_1 * x_min + b_1 <= y_max:
                        b = R2Point(x_min, k_1 * x_min + b_1)
                    elif x_min <= (y_min - b_1)/k_1 <= x_max:
                        b = R2Point((y_min - b_1)/k_1, y_min)
                    elif x_min <= (y_max - b_1)/k_1 <= x_max:
                        b = R2Point((y_max - b_1)/k_1, y_max)
            elif y_min <= k_1 * x_min + b_1 <= y_max and \
                    (p.x <= x_min <= q.x or q.x <= x_min <= p.x):
                a = R2Point(x_min, k_1 * x_min + b_1)
                if p.is_inside(k, m):
                    b = p
                else:
                    if x_min <= (y_min - b_1)/k_1 <= x_max:
                        b = R2Point((y_min - b_1)/k_1, y_min)
                    elif x_min <= (y_max - b_1)/k_1 <= x_max:
                        b = R2Point((y_max - b_1)/k_1, y_max)
            elif x_min <= (y_min - b_1)/k_1 <= x_max and \
                    (p.y <= y_min <= q.y or q.y <= y_min <= p.y):
                a = R2Point((y_min - b_1)/k_1, y_min)
                if p.is_inside(k, m):
                    b = p
                elif x_min <= (y_max - b_1)/k_1 <= x_max:
                    b = R2Point((y_max - b_1)/k_1, y_max)
            elif x_min <= (y_max - b_1)/k_1 <= x_max and \
                    (p.y <= y_max <= q.y or q.y <= y_max <= p.y):
                a = R2Point((y_max - b_1)/k_1, y_max)
                b = p
            d = a.dist(b)
        elif y_min <= p.y <= y_max and y_min <= q.y <= y_max or \
                x_min <= p.x <= x_max and x_min <= q.x <= x_max:
            if b_1 == p.x and b_1 != q.y:
                if p.y <= y_max <= q.y:
                    if p.y >= y_min:
                        d = p.dist(R2Point(b_1, y_max))
                    else:
                        d = R2Point(b_1, y_min).dist(R2Point(b_1, y_max))
                elif q.y <= y_min <= p.y:
                    if p.y <= y_max:
                        d = p.dist(R2Point(b_1, y_min))
                    else:
                        d = R2Point(b_1, y_min).dist(R2Point(b_1, y_max))
            elif b_1 == p.y and b_1 != q.x:
                if p.x <= x_max <= q.x:
                    if p.x >= x_min:
                        d = p.dist(R2Point(x_max, b_1))
                    else:
                        d = R2Point(x_min, b_1).dist(R2Point(x_max, b_1))
                elif q.x <= x_min <= p.x:
                    if p.x <= x_max:
                        d = p.dist(R2Point(x_min, b_1))
                    else:
                        d = R2Point(x_max, b_1).dist(R2Point(x_min, b_1))
        return d

    # Освещено ли из данной точки ребро (a,b)?
    def is_light(self, a, b):
        s = R2Point.area(a, b, self)
        return s < 0.0 or (s == 0.0 and not self.is_inside(a, b))

    # Совпадает ли точка с другой?
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.x == other.x and self.y == other.y
        return False


if __name__ == "__main__":
    p, q, k, m = R2Point(
        1.0, 1.0), R2Point(
        0.0, 0.0), R2Point(
        0.0, 0.0), R2Point(
        2.0, 2.0)
    a, b, c = R2Point(
        0.0, 1.0), R2Point(
        -3.0, 0.0), R2Point(
        3.0, 1.0)
    print(R2Point.new_dist(p, q, k, m))
    print(R2Point.new_dist(q, b, k, m))
    print(R2Point.new_dist(b, a, k, m))
    print(R2Point.new_dist(a, p, k, m))
    print(R2Point.new_dist(c, p, k, m))
    print(R2Point.new_dist(c, q, k, m))
