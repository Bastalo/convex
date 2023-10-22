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
    def new_dist(p, q, k, l):
        y_min = min(k.y, l.y)
        y_max = max(k.y, l.y)
        x_min = min(k.x, l.x)
        x_max = max(k.x, l.x)
        if q.is_inside(k, l) and not p.is_inside(k, l):
            p, q = q, p
        if p.x != q.x:
            k_1 = (p.y - q.y)/(p.x - q.x)
            b_1 = (p.x * q.y - p.y * q.x)/(p.x - q.x)
        else:
            k_1 = 0
            b_1 = p.x
        if not q.is_inside(k, l) and not p.is_inside(k, l):
            return 0.0
        elif p.is_inside(k, l) and q.is_inside(k, l):
            return p.dist(q)
        elif q.y > y_max and k_1 == 0:
            p_intersection = R2Point(b_1, y_max)
            return p.dist(p_intersection)
        elif q.y < y_min and k_1 == 0:
            p_intersection = R2Point(b_1, y_min)
            return p.dist(p_intersection)
        elif y_min <= k_1 * x_max + b_1 and \
            k_1 * x_max + b_1 <= y_max and q.x > x_max:
            p_intersection = R2Point(x_max, k_1 * x_max + b_1)
            return p.dist(p_intersection)
        elif y_min <= k_1 * x_min + b_1 and \
            k_1 * x_min + b_1 <= y_max and q.x < x_min:
            p_intersection = R2Point(x_min, k_1 * x_min + b_1)
            return p.dist(p_intersection)
        elif x_min <= (y_min - b_1)/k_1 and \
            (b_1 - y_min)/k_1 <= x_max and q.y < y_min:
            p_intersection = R2Point((y_min - b_1)/k_1, y_min)
            return p.dist(p_intersection)
        elif x_min <= (y_max - b_1)/k_1 and \
            (b_1 - y_max)/k_1 <= x_max and q.y > y_max:
            p_intersection = R2Point((y_max - b_1)/k_1, y_max)
            return p.dist(p_intersection)

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
    x = R2Point(1.0, 1.0)
    print(type(x), x.__dict__)
    print(x.dist(R2Point(1.0, 0.0)))
    x, y, z, a, b, c = R2Point(
        1.0, 0.0), R2Point(
        0.0, 1.0), R2Point(
        0.0, 1.0), R2Point(
        -5.0, -5.0), R2Point(
        0.0, 4.0), R2Point(
        3.0, -4.0)
    print(R2Point.is_rib_inside(x, y, a, b, c))
