from __future__ import annotations
from typing import List
from math import sin, cos, sqrt
import time
from __static__ import cast
'\nbg:\n- add `ITERATIONS` constant\n- remove `main` function\n- add missing type annotations\n- replace `xrange` with `range`\n- remove unused imports\n'

class Point(object):

    def __init__(self, i):
        x = sin(i)
        self.x: float = x
        self.y = cos(i) * 3
        self.z = x * x / 2

    def normalize(self: Point) -> None:
        x: float = self.x
        y: float = self.y
        z: float = self.z
        norm: float = sqrt(x * x + y * y + z * z)
        self.x /= norm
        self.y /= norm
        self.z /= norm

    def maximize(self: Point, other):
        self.x = self.x if self.x > cast(Point, other).x else cast(Point, other).x
        self.y = self.y if self.y > cast(Point, other).y else cast(Point, other).y
        self.z = self.z if self.z > cast(Point, other).z else cast(Point, other).z
        return cast(Point, self)

def maximize(points):
    next = cast(Point, points[0])
    for p in points[1:]:
        next = cast(Point, cast(Point, next).maximize(p))
    return cast(Point, next)

def benchmark(n: int) -> Point:
    points: List[Point] = [Point(i) for i in range(n)]
    for p in points:
        p.normalize()
    return cast(Point, maximize(points))
POINTS = 200000
if __name__ == '__main__':
    start_time = time.time()
    benchmark(POINTS)
    end_time = time.time()
    runtime = end_time - start_time
    print(runtime)