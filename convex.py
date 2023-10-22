from deq import Deq
from r2point import R2Point


class Figure:
    """ Абстрактная фигура """

    def perimeter(self):
        return 0.0

    def area(self):
        return 0.0

    def per(self):
        return 0.0


class Void(Figure):
    """ "Hульугольник" """

    def add(self, p):
        return Point(p)


class Point(Figure):
    """ "Одноугольник" """

    def __init__(self, p):
        self.p = p

    def add(self, q):
        return self if self.p == q else Segment(self.p, q)


class Segment(Figure):
    """ "Двуугольник" """

    def __init__(self, p, q):
        self.p, self.q = p, q

    def perimeter(self):
        return 2.0 * self.p.dist(self.q)

    # Вхождение двуугольника в стандартный прямоугольник
    def per(self):
        return 2.0 * R2Point.new_dist(self.p, self.q, self.k, self.m)

    def add(self, r):
        if R2Point.is_triangle(self.p, self.q, r):
            return Polygon(self.p, self.q, r)
        elif self.q.is_inside(self.p, r):
            return Segment(self.p, r)
        elif self.p.is_inside(r, self.q):
            return Segment(r, self.q)
        else:
            return self


class Polygon(Figure):
    """ Многоугольник """

    def __init__(self, a, b, c):
        self.points = Deq()
        self.points.push_first(b)
        if b.is_light(a, c):
            self.points.push_first(a)
            self.points.push_last(c)
        else:
            self.points.push_last(a)
            self.points.push_first(c)
        self._perimeter = a.dist(b) + b.dist(c) + c.dist(a)
        self._area = abs(R2Point.area(a, b, c))
        # Инитиализация искомого периметра в многоугольнике ()
        self._per = 0.0
        self._per += R2Point.new_dist(a, b, self.k, self.m) + \
            R2Point.new_dist(b, c, self.k, self.m) + \
            R2Point.new_dist(a, c, self.k, self.m)

    def perimeter(self):
        return self._perimeter

    def area(self):
        return self._area

    # Вызов счетчика ()
    def per(self):
        return self._per

    # добавление новой точки
    def add(self, t):

        # поиск освещённого ребра
        for n in range(self.points.size()):
            if t.is_light(self.points.last(), self.points.first()):
                break
            self.points.push_last(self.points.pop_first())

        # хотя бы одно освещённое ребро есть
        if t.is_light(self.points.last(), self.points.first()):

            # учёт удаления ребра, соединяющего конец и начало дека
            self._perimeter -= self.points.first().dist(self.points.last())
            self._area += abs(R2Point.area(t,
                                           self.points.last(),
                                           self.points.first()))
            # ()
            self._per -= R2Point.new_dist(self.points.first(),
                                          self.points.last(), self.k, self.m)

            # удаление освещённых рёбер из начала дека
            p = self.points.pop_first()
            while t.is_light(p, self.points.first()):
                self._perimeter -= p.dist(self.points.first())
                self._area += abs(R2Point.area(t, p, self.points.first()))
                # ()
                self._per -= R2Point.new_dist(self.points.first(), p,
                                              self.k, self.m)
                p = self.points.pop_first()
            self.points.push_first(p)

            # удаление освещённых рёбер из конца дека
            p = self.points.pop_last()
            while t.is_light(self.points.last(), p):
                self._perimeter -= p.dist(self.points.last())
                self._area += abs(R2Point.area(t, p, self.points.last()))
                # ()
                self._per -= R2Point.new_dist(p, self.points.last(),
                                              self.k, self.m)
                p = self.points.pop_last()
            self.points.push_last(p)

            # добавление двух новых рёбер
            self._perimeter += t.dist(self.points.first()) + \
                t.dist(self.points.last())
            # ()
            self._per += R2Point.new_dist(t, self.points.first(), self.k,
                                          self.m) + \
                R2Point.new_dist(t, self.points.last(), self.k, self.m)
            self.points.push_first(t)
        return self


if __name__ == "__main__":
    print("Заданный прямоугольник")
    Figure.k = R2Point()
    Figure.m = R2Point()
    print("\nТочки плоскости")
    f = Void()
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, -6.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(6.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, 1.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(-1.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(-1.0, -1.0))
    print(type(f), f.__dict__)
