#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Figure, Void

f = Void()
t = Void()

print("Predefined rectangle")
Figure.k = R2Point()
Figure.m = R2Point()
t = t.add(Figure.k)
t = t.add(Figure.m)
print("\nPlane points")

try:
    while True:
        f = f.add(R2Point())
        print(f"S = {f.area()}, P = {f.perimeter()}, Per = {f.per()}")
        print()
except (EOFError, KeyboardInterrupt):
    print("\nStop")
