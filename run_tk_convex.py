#!/usr/bin/env -S python3 -B
from tk_drawer import TkDrawer
from r2point import R2Point
from convex import Figure, Void, Point, Segment, Polygon


def void_draw(self, tk):
    pass


def point_draw(self, tk, color):
    tk.draw_point(self.p, color)


def segment_draw(self, tk, color):
    tk.draw_line(self.p, self.q, color)


def polygon_draw(self, tk, color):
    for n in range(self.points.size()):
        tk.draw_line(self.points.last(), self.points.first(), color)
        self.points.push_last(self.points.pop_first())


def rectangle_draw(self, tk):
    tk.draw_rectangle(self.p, self.q)


setattr(Void, 'draw', void_draw)
setattr(Point, 'draw', point_draw)
setattr(Segment, 'draw', segment_draw)
setattr(Segment, 'draw_rectangle', rectangle_draw)
setattr(Polygon, 'draw', polygon_draw)

tk = TkDrawer()
f = Void()
t = Void()
tk.clean()

print("Predefined rectangle")
Figure.k = R2Point()
Figure.m = R2Point()
t = t.add(Figure.k)
t = t.add(Figure.m)
t.draw_rectangle(tk)
print("\nPlane points")

try:
    while True:
        f = f.add(R2Point())
        tk.clean()
        t.draw_rectangle(tk)
        f.draw(tk, "black")
        print(f"S = {f.area()}, P = {f.perimeter()}, Per = {f.per()}\n")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
