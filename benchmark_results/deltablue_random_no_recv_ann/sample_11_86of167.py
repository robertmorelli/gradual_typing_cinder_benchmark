"""
main.py
============

Ported for the PyPy project.
Contributed by Daniel Lindsley

This implementation of the DeltaBlue benchmark was directly ported
from the `V8's source code`_, which was in turn derived
from the Smalltalk implementation by John Maloney and Mario
Wolczko. The original Javascript implementation was licensed under the GPL.

It's been updated in places to be more idiomatic to Python (for loops over
collections, a couple magic methods, ``OrderedCollection`` being a list & things
altering those collections changed to the builtin methods) but largely retains
the layout & logic from the original. (Ugh.)

.. _`V8's source code`: (https://github.com/v8/v8/blob/master/benchmarks/deltablue.js)
"""
from __future__ import annotations
import __static__
import time
from enum import IntEnum
from __static__ import CheckedList, box, cast, cbool, clen, int64, inline
from typing import final
import time

@inline
def stronger(s1: Strength, s2: Strength) -> cbool:
    return int64(s1.strength) < int64(s2.strength)

@inline
def weaker(s1, s2):
    return box(cbool(int64(cast(Strength, s1).strength) > int64(cast(Strength, s2).strength)))

@inline
def weakest_of(s1: Strength, s2) -> Strength:
    return s1 if int64(s1.strength) > int64(cast(Strength, s2).strength) else s2

@final
class Strength:

    def __init__(self, strength, name: str):
        self.strength = strength
        self.name = name

    def next_weaker(self):
        return cast(Strength, STRENGTHS[int64(self.strength)])
REQUIRED = Strength(0, 'required')
STRONG_PREFERRED = Strength(1, 'strongPreferred')
PREFERRED = Strength(2, 'preferred')
STRONG_DEFAULT = Strength(3, 'strongDefault')
NORMAL = Strength(4, 'normal')
WEAK_DEFAULT = Strength(5, 'weakDefault')
WEAKEST = Strength(6, 'weakest')
STRENGTHS: CheckedList[Strength] = CheckedList[Strength]([WEAKEST, WEAK_DEFAULT, NORMAL, STRONG_DEFAULT, PREFERRED, REQUIRED])

class Constraint(object):

    def __init__(self, strength):
        self.strength = strength

    def add_constraint(self) -> None:
        planner: Planner = cast(Planner, get_planner())
        self.add_to_graph()
        planner.incremental_add(self)

    def satisfy(self, mark: int64):
        planner: Planner = cast(Planner, get_planner())
        self.choose_method(box(int64(mark)))
        if not self.is_satisfied():
            if cast(Strength, self.strength) == REQUIRED:
                print('Could not satisfy a required constraint!')
            return None
        self.mark_inputs(box(int64(mark)))
        out = self.output()
        overridden = cast(Variable, out).determined_by
        if overridden is not None:
            cast(Constraint, overridden).mark_unsatisfied()
        cast(Variable, out).determined_by = self
        if not planner.add_propagate(self, box(int64(mark))):
            print('Cycle encountered')
        cast(Variable, out).mark = mark
        return cast(Constraint | None, overridden)

    def destroy_constraint(self):
        planner = get_planner()
        if self.is_satisfied():
            cast(Planner, planner).incremental_remove(self)
        else:
            self.remove_from_graph()

    def is_input(self):
        return False

    def mark_inputs(self, mark):
        pass

    def inputs_known(self, mark) -> cbool:
        return True

    def choose_method(self, mark) -> None:
        pass

    def output(self):
        raise NotImplementedError()

    def execute(self):
        pass

class UrnaryConstraint(Constraint):

    def __init__(self, v, strength):
        Constraint.__init__(self, strength)
        self.my_output: Variable = v
        self.satisfied: cbool = False
        self.add_constraint()

    def add_to_graph(self):
        self.my_output.add_constraint(self)
        self.satisfied = False

    def choose_method(self, mark) -> None:
        if self.my_output.mark != int64(mark) and stronger(cast(Strength, self.strength), cast(Strength, self.my_output.walk_strength)):
            self.satisfied = True
        else:
            self.satisfied = False

    def is_satisfied(self):
        return box(cbool(self.satisfied))

    def output(self):
        return cast(Variable, self.my_output)

    def recalculate(self):
        self.my_output.walk_strength = cast(Strength, self.strength)
        self.my_output.stay = not cbool(self.is_input())
        if self.my_output.stay:
            self.execute()

    def mark_unsatisfied(self):
        self.satisfied = False

    def remove_from_graph(self) -> None:
        if self.my_output is not None:
            self.my_output.remove_constraint(self)
            self.satisfied = False

@final
class StayConstraint(UrnaryConstraint):
    pass

@final
class EditConstraint(UrnaryConstraint):

    def is_input(self):
        return True

@final
class Direction(IntEnum):
    NONE = 0
    FORWARD = 1
    BACKWARD = -1

class BinaryConstraint(Constraint):

    def __init__(self, v1, v2, strength):
        Constraint.__init__(self, strength)
        self.v1 = v1
        self.v2: Variable = v2
        self.direction = Direction.NONE
        self.add_constraint()

    def choose_method(self, mark) -> None:
        if cast(Variable, self.v1).mark == int64(mark):
            if self.v2.mark != int64(mark) and stronger(cast(Strength, self.strength), cast(Strength, self.v2.walk_strength)):
                self.direction = Direction.FORWARD
            else:
                self.direction = Direction.BACKWARD
        if self.v2.mark == int64(mark):
            if cast(Variable, self.v1).mark != int64(mark) and stronger(cast(Strength, self.strength), cast(Strength, cast(Variable, self.v1).walk_strength)):
                self.direction = Direction.BACKWARD
            else:
                self.direction = Direction.NONE
        if cbool(weaker(cast(Strength, cast(Variable, self.v1).walk_strength), cast(Strength, self.v2.walk_strength))):
            if stronger(cast(Strength, self.strength), cast(Strength, cast(Variable, self.v1).walk_strength)):
                self.direction = Direction.BACKWARD
            else:
                self.direction = Direction.NONE
        elif stronger(cast(Strength, self.strength), cast(Strength, self.v2.walk_strength)):
            self.direction = Direction.FORWARD
        else:
            self.direction = Direction.BACKWARD

    def add_to_graph(self):
        cast(Variable, self.v1).add_constraint(self)
        self.v2.add_constraint(self)
        self.direction = Direction.NONE

    def is_satisfied(self) -> cbool:
        if self.direction != Direction.NONE:
            return True
        return False

    def mark_inputs(self, mark):
        self.input().mark = int64(mark)

    def input(self) -> Variable:
        return cast(Variable, self.v1) if self.direction == Direction.FORWARD else self.v2

    def output(self):
        return cast(Variable, self.v2 if self.direction == Direction.FORWARD else cast(Variable, self.v1))

    def recalculate(self) -> None:
        ihn = cast(Variable, self.input())
        out = self.output()
        cast(Variable, out).walk_strength = weakest_of(cast(Strength, self.strength), cast(Strength, cast(Variable, ihn).walk_strength))
        cast(Variable, out).stay = cast(Variable, ihn).stay
        if cast(Variable, out).stay:
            self.execute()

    def mark_unsatisfied(self) -> None:
        self.direction = Direction.NONE

    def inputs_known(self, mark) -> cbool:
        i: Variable = self.input()
        return i.mark == int64(mark) or i.stay or cbool(cast(Constraint | None, i.determined_by) is None)

    def remove_from_graph(self):
        if cast(Variable, self.v1) is not None:
            cast(Variable, self.v1).remove_constraint(self)
        if self.v2 is not None:
            self.v2.remove_constraint(self)
        self.direction = Direction.NONE

@final
class ScaleConstraint(BinaryConstraint):

    def __init__(self, src, scale, offset, dest: Variable, strength: Strength):
        self.direction: Direction = Direction.NONE
        self.scale: Variable = scale
        self.offset = offset
        BinaryConstraint.__init__(self, src, dest, strength)

    def add_to_graph(self):
        BinaryConstraint.add_to_graph(self)
        self.scale.add_constraint(self)
        cast(Variable, self.offset).add_constraint(self)

    def remove_from_graph(self):
        BinaryConstraint.remove_from_graph(self)
        if self.scale is not None:
            self.scale.remove_constraint(self)
        if cast(Variable, self.offset) is not None:
            cast(Variable, self.offset).remove_constraint(self)

    def mark_inputs(self, mark):
        BinaryConstraint.mark_inputs(self, mark)
        self.scale.mark = int64(mark)
        cast(Variable, self.offset).mark = int64(mark)

    def execute(self):
        if self.direction == Direction.FORWARD:
            self.v2.value = cast(Variable, self.v1).value * self.scale.value + cast(Variable, self.offset).value
        else:
            cast(Variable, self.v1).value = (self.v2.value - cast(Variable, self.offset).value) / self.scale.value

    def recalculate(self) -> None:
        ihn: Variable = self.input()
        out: Variable = cast(Variable, self.output())
        out.walk_strength = weakest_of(cast(Strength, self.strength), cast(Strength, ihn.walk_strength))
        out.stay = ihn.stay and self.scale.stay and cast(Variable, self.offset).stay
        if out.stay:
            self.execute()

@final
class EqualityConstraint(BinaryConstraint):

    def execute(self):
        cast(Variable, self.output()).value = self.input().value

@final
class Variable(object):

    def __init__(self, name: str, initial_value=0):
        self.name: str = name
        self.value: int64 = int64(initial_value)
        self.constraints: CheckedList[Constraint] = []
        self.determined_by = None
        self.mark: int64 = 0
        self.walk_strength = WEAKEST
        self.stay: cbool = True

    def add_constraint(self, constraint) -> None:
        self.constraints.append(cast(Constraint, constraint))

    def remove_constraint(self, constraint):
        self.constraints.remove(cast(Constraint, constraint))
        if cast(Constraint | None, self.determined_by) == cast(Constraint, constraint):
            self.determined_by = None

@final
class Planner(object):

    def __init__(self):
        self.current_mark: int64 = 0

    def incremental_add(self, constraint: Constraint) -> None:
        mark = self.new_mark()
        overridden: Constraint | None = cast(Constraint | None, constraint.satisfy(int64(mark)))
        while overridden is not None:
            overridden = cast(Constraint | None, overridden.satisfy(int64(mark)))

    def incremental_remove(self, constraint: Constraint):
        out: Variable = cast(Variable, constraint.output())
        constraint.mark_unsatisfied()
        constraint.remove_from_graph()
        unsatisfied = self.remove_propagate_from(out)
        strength = REQUIRED
        repeat = True
        while repeat:
            for u in unsatisfied:
                if cast(Strength, u.strength) == strength:
                    self.incremental_add(u)
                strength = cast(Strength, strength.next_weaker())
            repeat = strength != WEAKEST

    def new_mark(self):
        x: int64 = self.current_mark + 1
        self.current_mark = x
        return box(int64(self.current_mark))

    def make_plan(self, sources) -> Plan:
        sources = cast(CheckedList[UrnaryConstraint], sources)
        mark = self.new_mark()
        plan: Plan = Plan()
        todo = CheckedList[Constraint]([s for s in sources])
        while clen(todo):
            c = todo.pop(0)
            if cast(Variable, c.output()).mark != int64(mark) and c.inputs_known(mark):
                plan.add_constraint(c)
                cast(Variable, c.output()).mark = int64(mark)
                self.add_constraints_consuming_to(cast(Variable, c.output()), todo)
        return plan

    def extract_plan_from_constraints(self, constraints) -> Plan:
        constraints = cast(CheckedList[UrnaryConstraint], constraints)
        sources = CheckedList[UrnaryConstraint]([])
        for c in constraints:
            if cbool(c.is_input()) and cbool(c.is_satisfied()):
                sources.append(c)
        return self.make_plan(sources)

    def add_propagate(self, c: Constraint, mark) -> cbool:
        todo = CheckedList[Constraint]([])
        todo.append(c)
        while clen(todo):
            d = todo.pop(0)
            if cast(Variable, d.output()).mark == int64(mark):
                self.incremental_remove(c)
                return False
            d.recalculate()
            self.add_constraints_consuming_to(cast(Variable, d.output()), todo)
        return True

    def remove_propagate_from(self, out) -> CheckedList[Constraint]:
        cast(Variable, out).determined_by = None
        cast(Variable, out).walk_strength = WEAKEST
        cast(Variable, out).stay = True
        unsatisfied: CheckedList[Constraint] = []
        todo: CheckedList[Variable] = []
        todo.append(cast(Variable, out))
        while len(todo):
            v = todo.pop(0)
            cs = cast(CheckedList[Constraint], v.constraints)
            for c in cs:
                if not c.is_satisfied():
                    unsatisfied.append(c)
            determining = cast(Constraint | None, v.determined_by)
            for c in cs:
                if c != determining and c.is_satisfied():
                    c.recalculate()
                    todo.append(cast(Variable, c.output()))
        return unsatisfied

    def add_constraints_consuming_to(self, v: Variable, coll: CheckedList[Constraint]):
        determining: Constraint | None = cast(Constraint | None, v.determined_by)
        cc = cast(CheckedList[Constraint], v.constraints)
        for c in cc:
            if c != determining and c.is_satisfied():
                coll.append(c)

@final
class Plan(object):

    def __init__(self) -> None:
        self.v: CheckedList[Constraint] = []

    def add_constraint(self, c: Constraint) -> None:
        self.v.append(c)

    def __len__(self):
        return len(self.v)

    def __getitem__(self, index):
        return self.v[index]

    def execute(self) -> None:
        for c in self.v:
            c.execute()

def recreate_planner() -> Planner:
    global planner
    planner = Planner()
    return planner

def get_planner():
    global planner
    return cast(Planner, planner)

def chain_test(n: int64):
    """
    This is the standard DeltaBlue benchmark. A long chain of equality
    constraints is constructed with a stay constraint on one end. An
    edit constraint is then added to the opposite end and the time is
    measured for adding and removing this constraint, and extracting
    and executing a constraint satisfaction plan. There are two cases.
    In case 1, the added constraint is stronger than the stay
    constraint and values must propagate down the entire length of the
    chain. In case 2, the added constraint is weaker than the stay
    constraint so it cannot be accomodated. The cost in this case is,
    of course, very low. Typical situations lie somewhere between these
    two extremes.
    """
    planner = cast(Planner, recreate_planner())
    prev: Variable | None = None
    first = None
    last = None
    i = 0
    end = box(int64(n + 1))
    while int64(i) < n + 1:
        name = 'v%s' % i
        v = Variable(name)
        if prev is not None:
            EqualityConstraint(prev, v, REQUIRED)
        if int64(i) == 0:
            first = v
        if int64(i) == n:
            last = v
        prev = v
        i = box(int64(int64(i) + 1))
    first = cast(Variable, first)
    last = cast(Variable, last)
    StayConstraint(last, STRONG_DEFAULT)
    edit = EditConstraint(first, PREFERRED)
    edits: CheckedList[UrnaryConstraint] = []
    edits.append(edit)
    plan = cast(Planner, planner).extract_plan_from_constraints(edits)
    i = box(int64(0))
    while int64(i) < 100:
        first.value = int64(i)
        plan.execute()
        if last.value != int64(i):
            print('Chain test failed.')
        i = box(int64(int64(i) + 1))

def projection_test(n: int64):
    """
    This test constructs a two sets of variables related to each
    other by a simple linear transformation (scale and offset). The
    time is measured to change a variable on either side of the
    mapping and to change the scale and offset factors.
    """
    planner = cast(Planner, recreate_planner())
    scale = Variable('scale', 10)
    offset = Variable('offset', 1000)
    src: Variable | None = None
    dests = CheckedList[Variable]([])
    i: int64 = 0
    dst = Variable('dst%s' % 0, 0)
    while i < n:
        bi = box(i)
        src = Variable('src%s' % bi, box(int64(i)))
        dst = Variable('dst%s' % bi, box(int64(i)))
        dests.append(dst)
        StayConstraint(src, NORMAL)
        ScaleConstraint(src, scale, offset, dst, REQUIRED)
        i = i + 1
    src = cast(Variable, src)
    change(src, 17)
    if dst.value != 1170:
        print('Projection 1 failed')
    change(dst, 1050)
    if src.value != 5:
        print('Projection 2 failed')
    change(scale, 5)
    i = 0
    while i < n - 1:
        if cast(Variable, dests[box(i)]).value != i * 5 + 1000:
            print('Projection 3 failed')
        i = i + 1
    change(offset, 2000)
    i = 0
    while i < n - 1:
        if cast(Variable, dests[box(i)]).value != i * 5 + 2000:
            print('Projection 4 failed')
        i = i + 1

def change(v: Variable, new_value):
    planner: Planner = cast(Planner, get_planner())
    edit = EditConstraint(v, PREFERRED)
    edits = CheckedList[UrnaryConstraint]([])
    edits.append(edit)
    plan = planner.extract_plan_from_constraints(edits)
    i = 0
    while int64(i) < 10:
        v.value = int64(new_value)
        plan.execute()
        i = box(int64(int64(i) + 1))
    edit.destroy_constraint()
planner = None

def delta_blue(i):
    n = int64(i)
    chain_test(n)
    projection_test(n)
if __name__ == '__main__':
    n = 10000
    startTime = time.time()
    delta_blue(n)
    endTime = time.time()
    runtime = endTime - startTime
    print(runtime)