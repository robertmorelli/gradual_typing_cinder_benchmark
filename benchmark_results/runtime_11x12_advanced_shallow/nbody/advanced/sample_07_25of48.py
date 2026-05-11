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
import __static__
from __static__ import double, CheckedList, CheckedDict, box, int64
import time
from __static__ import cast
__contact__ = 'collinwinter@google.com (Collin Winter)'
DEFAULT_ITERATIONS = 20000
DEFAULT_REFERENCE = 'sun'
PI = 3.141592653589793
SOLAR_MASS = 4 * PI * PI
DAYS_PER_YEAR = 365.24

class Vector:

    def __init__(self, x, y: double, z):
        self.x: double = double(x)
        self.y: double = y
        self.z = z

    def __repr__(self):
        return f'Vector({(box(self.x), box(self.y), box(double(self.z)))})'

class Body:

    def __init__(self, pos: Vector, _v, mass):
        v = cast(Vector, _v)
        self.pos = pos
        self.v: Vector = v
        self.mass = mass

    def __repr__(self):
        return f'Body({cast(Vector, self.pos)}, {self.v}, {box(double(self.mass))})'

def combinations(l) -> list[tuple[Body, Body]]:
    """Pure-Python implementation of itertools.combinations(l, 2)."""
    result: list[tuple[Body, Body]] = []
    for x in range(len(l) - 1):
        ls: CheckedList[Body] = cast(CheckedList[Body], l[x + 1:])
        for y in ls:
            result.append((cast(Body, l[x]), y))
    return result
BODIES = CheckedDict[str, Body]({'sun': Body(Vector(0.0, 0.0, 0.0), Vector(0.0, 0.0, 0.0), box(double(double(SOLAR_MASS)))), 'jupiter': Body(Vector(4.841431442464721, -1.1603200440274284, box(double(-0.10362204447112311))), Vector(box(double(0.001660076642744037 * double(DAYS_PER_YEAR))), 0.007699011184197404 * double(DAYS_PER_YEAR), box(double(-6.90460016972063e-05 * double(DAYS_PER_YEAR)))), box(double(0.0009547919384243266 * double(SOLAR_MASS)))), 'saturn': Body(Vector(8.34336671824458, 4.124798564124305, box(double(-0.4035234171143214))), Vector(box(double(-0.002767425107268624 * double(DAYS_PER_YEAR))), 0.004998528012349172 * double(DAYS_PER_YEAR), box(double(2.3041729757376393e-05 * double(DAYS_PER_YEAR)))), box(double(0.0002858859806661308 * double(SOLAR_MASS)))), 'uranus': Body(Vector(12.894369562139131, -15.111151401698631, box(double(-0.22330757889265573))), Vector(box(double(0.002964601375647616 * double(DAYS_PER_YEAR))), 0.0023784717395948095 * double(DAYS_PER_YEAR), box(double(-2.9658956854023756e-05 * double(DAYS_PER_YEAR)))), box(double(4.366244043351563e-05 * double(SOLAR_MASS)))), 'neptune': Body(Vector(15.379697114850917, -25.919314609987964, 0.17925877295037118), Vector(box(double(0.0026806777249038932 * double(DAYS_PER_YEAR))), 0.001628241700382423 * double(DAYS_PER_YEAR), box(double(-9.515922545197159e-05 * double(DAYS_PER_YEAR)))), box(double(5.1513890204661145e-05 * double(SOLAR_MASS))))})
SYSTEM: CheckedList[Body] = CheckedList[Body](BODIES.values())
PAIRS: list[tuple[Body, Body]] = combinations(cast(CheckedList[Body], SYSTEM))

def advance(dt: double, n, bodies=SYSTEM, pairs=PAIRS):
    for i in range(n):
        for b1, b2 in pairs:
            pos1 = cast(Vector, cast(Body, b1).pos)
            pos2 = cast(Vector, cast(Body, b2).pos)
            dx = box(double(pos1.x - pos2.x))
            dy = box(double(pos1.y - pos2.y))
            dz = box(double(double(pos1.z) - double(pos2.z)))
            mag = dt * (double(dx) * double(dx) + double(dy) * double(dy) + double(dz) * double(dz)) ** double(-1.5)
            b1m = double(cast(Body, b1).mass) * mag
            b2m = double(cast(Body, b2).mass) * mag
            v1 = cast(Body, b1).v
            v2 = cast(Body, b2).v
            v1.x -= double(dx) * b2m
            v1.y -= double(dy) * b2m
            v1.z -= double(dz) * b2m
            v2.x += double(dx) * b1m
            v2.y += double(dy) * b1m
            v2.z += double(dz) * b1m
        for body in bodies:
            r = cast(Vector, body.pos)
            v = body.v
            r.x += dt * v.x
            r.y += dt * v.y
            r.z += dt * double(v.z)

def report_energy(bodies: CheckedList[Body]=SYSTEM, pairs=PAIRS, e=0.0) -> double:
    b2: Body
    body: Body
    for b1, b2 in pairs:
        pos1 = cast(Vector, cast(Body, b1).pos)
        pos2 = cast(Vector, b2.pos)
        dx = pos1.x - pos2.x
        dy = pos1.y - pos2.y
        dz = double(pos1.z) - double(pos2.z)
        e -= double(cast(Body, b1).mass) * double(b2.mass) / (dx * dx + dy * dy + dz * dz) ** 0.5
    for body in bodies:
        v = body.v
        e += double(body.mass) * (v.x * v.x + v.y * v.y + double(v.z) * double(v.z)) / 2.0
    return double(e)

def offset_momentum(ref: Body, bodies: CheckedList[Body], px=0.0, py: double=0.0, pz=0.0):
    body: Body
    for body in bodies:
        v: Vector = body.v
        m: double = double(body.mass)
        px -= v.x * m
        py -= v.y * m
        pz -= double(v.z) * m
    m = double(ref.mass)
    v = ref.v
    v.x = double(px) / m
    v.y = py / m
    v.z = box(double(double(pz) / m))

def bench_nbody(loops: int, reference, iterations: int):
    offset_momentum(BODIES[reference], SYSTEM)
    range_it = range(loops)
    for _ in range_it:
        report_energy(SYSTEM, PAIRS)
        advance(0.01, iterations, cast(CheckedList[Body], SYSTEM), PAIRS)
        report_energy(SYSTEM, PAIRS)

def run():
    num_loops = 5
    bench_nbody(num_loops, DEFAULT_REFERENCE, DEFAULT_ITERATIONS)
if __name__ == '__main__':
    import sys
    num_loops = 5
    startTime = time.time()
    bench_nbody(num_loops, DEFAULT_REFERENCE, DEFAULT_ITERATIONS)
    endTime = time.time()
    runtime = endTime - startTime
    print(runtime)