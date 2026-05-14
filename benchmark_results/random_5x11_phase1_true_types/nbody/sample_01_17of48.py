"""
N-body benchmark from the Computer Language Benchmarks Game.

This is intended to support Unladen Swallow's pyperf.py. Accordingly, it has been
modified from the Shootout version:
- Accept standard Unladen Swallow benchmark options.
- Run report_energy()/advance() in a loop.
- Reimplement itertools.combinations() to work with older Python versions.

Pulled from:
http://benchmarksgame.alioth.debian.org/u64q/program.php?test=nbody&lang=python3&id=1

Contributed by Kevin Carson.
Modified by Tupteq, Fredrik Johansson, and Daniel Nanz.
"""
from __static__ import box, cast
import __static__
from __static__ import double, CheckedList, CheckedDict, box, int64
import time
__contact__ = 'collinwinter@google.com (Collin Winter)'
DEFAULT_ITERATIONS = 20000
DEFAULT_REFERENCE: str = 'sun'
PI = 3.141592653589793
SOLAR_MASS = 4 * PI * PI
DAYS_PER_YEAR = 365.24

class Vector:

    def __init__(self, x, y: double, z: double):
        self.x = box(double(double(x)))
        self.y: double = y
        self.z: double = z

    def __repr__(self):
        return f'Vector({(box(double(self.x)), box(self.y), box(self.z))})'

class Body:

    def __init__(self, pos, v: Vector, mass):
        self.pos = pos
        self.v: Vector = v
        self.mass: double = double(mass)

    def __repr__(self):
        return f'Body({cast(Vector, self.pos)}, {self.v}, {box(self.mass)})'

def combinations(l: CheckedList[Body]) -> list[tuple[Body, Body]]:
    """Pure-Python implementation of itertools.combinations(l, 2)."""
    result = []
    for x in range(len(l) - 1):
        ls: CheckedList[Body] = l[x + 1:]
        for y in ls:
            result.append((l[x], y))
    return result
BODIES = CheckedDict[str, Body]({'sun': Body(Vector(box(double(0.0)), 0.0, 0.0), Vector(box(double(0.0)), 0.0, 0.0), box(double(SOLAR_MASS))), 'jupiter': Body(Vector(box(double(4.841431442464721)), -1.1603200440274284, -0.10362204447112311), Vector(box(double(0.001660076642744037 * double(DAYS_PER_YEAR))), 0.007699011184197404 * double(DAYS_PER_YEAR), -6.90460016972063e-05 * double(DAYS_PER_YEAR)), box(double(0.0009547919384243266 * double(SOLAR_MASS)))), 'saturn': Body(Vector(box(double(8.34336671824458)), 4.124798564124305, -0.4035234171143214), Vector(box(double(-0.002767425107268624 * double(DAYS_PER_YEAR))), 0.004998528012349172 * double(DAYS_PER_YEAR), 2.3041729757376393e-05 * double(DAYS_PER_YEAR)), box(double(0.0002858859806661308 * double(SOLAR_MASS)))), 'uranus': Body(Vector(box(double(12.894369562139131)), -15.111151401698631, -0.22330757889265573), Vector(box(double(0.002964601375647616 * double(DAYS_PER_YEAR))), 0.0023784717395948095 * double(DAYS_PER_YEAR), -2.9658956854023756e-05 * double(DAYS_PER_YEAR)), box(double(4.366244043351563e-05 * double(SOLAR_MASS)))), 'neptune': Body(Vector(box(double(15.379697114850917)), -25.919314609987964, 0.17925877295037118), Vector(box(double(0.0026806777249038932 * double(DAYS_PER_YEAR))), 0.001628241700382423 * double(DAYS_PER_YEAR), -9.515922545197159e-05 * double(DAYS_PER_YEAR)), box(double(5.1513890204661145e-05 * double(SOLAR_MASS))))})
SYSTEM = CheckedList[Body](BODIES.values())
PAIRS = combinations(SYSTEM)

def advance(dt, n, bodies=SYSTEM, pairs: list[tuple[Body, Body]]=PAIRS):
    for i in range(n):
        b2: Body
        for b1, b2 in pairs:
            pos1 = cast(Vector, b1.pos)
            pos2 = cast(Vector, b2.pos)
            dx: double = double(pos1.x) - double(pos2.x)
            dy: double = pos1.y - pos2.y
            dz: double = pos1.z - pos2.z
            mag = double(dt) * (dx * dx + dy * dy + dz * dz) ** double(-1.5)
            b1m = b1.mass * mag
            b2m = b2.mass * mag
            v1 = b1.v
            v2 = b2.v
            v1.x -= dx * b2m
            v1.y -= dy * b2m
            v1.z -= dz * b2m
            v2.x += dx * b1m
            v2.y += dy * b1m
            v2.z += dz * b1m
        for body in cast(CheckedList[Body], bodies):
            r = cast(Vector, body.pos)
            v = body.v
            r.x += double(dt) * double(v.x)
            r.y += double(dt) * v.y
            r.z += double(dt) * v.z

def report_energy(bodies: CheckedList[Body]=SYSTEM, pairs: list[tuple[Body, Body]]=PAIRS, e: double=0.0):
    b1: Body
    b2: Body
    body: Body
    for b1, b2 in pairs:
        pos1 = cast(Vector, b1.pos)
        pos2 = cast(Vector, b2.pos)
        dx = double(pos1.x) - double(pos2.x)
        dy = pos1.y - pos2.y
        dz = pos1.z - pos2.z
        e -= b1.mass * b2.mass / (dx * dx + dy * dy + dz * dz) ** 0.5
    for body in bodies:
        v = body.v
        e += body.mass * (double(v.x) * double(v.x) + v.y * v.y + v.z * v.z) / 2.0
    return box(double(e))

def offset_momentum(ref: Body, bodies: CheckedList[Body], px=0.0, py: double=0.0, pz: double=0.0):
    body: Body
    for body in bodies:
        v: Vector = body.v
        m = box(double(body.mass))
        px -= double(v.x) * double(m)
        py -= v.y * double(m)
        pz -= v.z * double(m)
    m = box(double(ref.mass))
    v = ref.v
    v.x = box(double(double(px) / double(m)))
    v.y = py / double(m)
    v.z = pz / double(m)

def bench_nbody(loops, reference: str, iterations: int):
    offset_momentum(BODIES[reference], SYSTEM)
    range_it = range(loops)
    for _ in range_it:
        report_energy(SYSTEM, PAIRS)
        advance(box(double(0.01)), iterations, SYSTEM, PAIRS)
        report_energy(SYSTEM, PAIRS)

def run():
    num_loops = 5
    bench_nbody(num_loops, DEFAULT_REFERENCE, DEFAULT_ITERATIONS)
if __name__ == '__main__':
    import sys
    num_loops: int = 5
    startTime = time.time()
    bench_nbody(num_loops, DEFAULT_REFERENCE, DEFAULT_ITERATIONS)
    endTime = time.time()
    runtime = endTime - startTime
    print(runtime)