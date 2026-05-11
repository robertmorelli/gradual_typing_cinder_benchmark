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
def stronger(s1: Strength, s2):
    return box(cbool(int64(s1.strength) < int64(cast(Strength, s2).strength)))

@inline
def weaker(s1: Strength, s2: Strength) -> cbool:
    return int64(s1.strength) > int64(s2.strength)

@inline
def weakest_of(s1, s2: Strength) -> Strength:
    return s1 if int64(cast(Strength, s1).strength) > int64(s2.strength) else s2

@final
class Strength:

    def __init__(self, strength, name):
        self.strength = strength
        self.name: str = name

    def next_weaker(self) -> Strength:
        return cast(Strength, cast(CheckedList[Strength], STRENGTHS)[self.strength])
REQUIRED = Strength(0, 'required')
STRONG_PREFERRED = Strength(1, 'strongPreferred')
PREFERRED = Strength(2, 'preferred')
STRONG_DEFAULT = Strength(3, 'strongDefault')
NORMAL = Strength(4, 'normal')
WEAK_DEFAULT = Strength(5, 'weakDefault')
WEAKEST = Strength(6, 'weakest')
STRENGTHS = cast(CheckedList[Strength], CheckedList[Strength]([WEAKEST, WEAK_DEFAULT, NORMAL, STRONG_DEFAULT, PREFERRED, REQUIRED]))

class Constraint(object):

    def __init__(self, strength):
        self.strength = strength

    def add_constraint(self):
        planner: Planner = cast(Planner, get_planner())
        self.add_to_graph()
        planner.incremental_add(self)

    def satisfy(self, mark: int64):
        planner = get_planner()
        self.choose_method(box(int64(mark)))
        if not self.is_satisfied():
            if cast(Strength, self.strength) == REQUIRED:
                print('Could not satisfy a required constraint!')
            return None
        self.mark_inputs(box(int64(mark)))
        out = cast(Variable, self.output())
        overridden: Constraint | None = cast(Variable, out).determined_by
        if overridden is not None:
            overridden.mark_unsatisfied()
        cast(Variable, out).determined_by = self
        if not cast(Planner, planner).add_propagate(self, box(int64(mark))):
            print('Cycle encountered')
        cast(Variable, out).mark = mark
        return cast(Constraint | None, overridden)

    def destroy_constraint(self) -> None:
        planner: Planner = cast(Planner, get_planner())
        if self.is_satisfied():
            planner.incremental_remove(self)
        else:
            self.remove_from_graph()

    def is_input(self):
        return False

    def mark_inputs(self, mark):
        pass

    def inputs_known(self, mark):
        return True

    def choose_method(self, mark) -> None:
        pass

    def output(self) -> Variable:
        raise NotImplementedError()

    def execute(self) -> None:
        pass

class UrnaryConstraint(Constraint):

    def __init__(self, v, strength):
        Constraint.__init__(self, strength)
        self.my_output: Variable = v
        self.satisfied = False
        self.add_constraint()

    def add_to_graph(self) -> None:
        self.my_output.add_constraint(self)
        self.satisfied = False

    def choose_method(self, mark) -> None:
        if self.my_output.mark != int64(mark) and cbool(stronger(cast(Strength, self.strength), self.my_output.walk_strength)):
            self.satisfied = True
        else:
            self.satisfied = False

    def is_satisfied(self):
        return self.satisfied

    def output(self) -> Variable:
        return self.my_output

    def recalculate(self):
        self.my_output.walk_strength = cast(Strength, self.strength)
        self.my_output.stay = box(cbool(not cbool(self.is_input())))
        if cbool(self.my_output.stay):
            self.execute()

    def mark_unsatisfied(self) -> None:
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
        self.direction: Direction = Direction.NONE
        self.add_constraint()

    def choose_method(self, mark) -> None:
        if cast(Variable, self.v1).mark == int64(mark):
            if self.v2.mark != int64(mark) and cbool(stronger(cast(Strength, self.strength), self.v2.walk_strength)):
                self.direction = Direction.FORWARD
            else:
                self.direction = Direction.BACKWARD
        if self.v2.mark == int64(mark):
            if cast(Variable, self.v1).mark != int64(mark) and cbool(stronger(cast(Strength, self.strength), cast(Variable, self.v1).walk_strength)):
                self.direction = Direction.BACKWARD
            else:
                self.direction = Direction.NONE
        if weaker(cast(Variable, self.v1).walk_strength, self.v2.walk_strength):
            if cbool(stronger(cast(Strength, self.strength), cast(Variable, self.v1).walk_strength)):
                self.direction = Direction.BACKWARD
            else:
                self.direction = Direction.NONE
        elif cbool(stronger(cast(Strength, self.strength), self.v2.walk_strength)):
            self.direction = Direction.FORWARD
        else:
            self.direction = Direction.BACKWARD

    def add_to_graph(self):
        cast(Variable, self.v1).add_constraint(self)
        self.v2.add_constraint(self)
        self.direction = Direction.NONE

    def is_satisfied(self):
        if self.direction != Direction.NONE:
            return True
        return False

    def mark_inputs(self, mark):
        self.input().mark = int64(mark)

    def input(self) -> Variable:
        return cast(Variable, self.v1) if self.direction == Direction.FORWARD else self.v2

    def output(self) -> Variable:
        return self.v2 if self.direction == Direction.FORWARD else cast(Variable, self.v1)

    def recalculate(self):
        ihn: Variable = self.input()
        out: Variable = self.output()
        out.walk_strength = weakest_of(cast(Strength, self.strength), ihn.walk_strength)
        out.stay = box(cbool(cbool(ihn.stay)))
        if cbool(out.stay):
            self.execute()

    def mark_unsatisfied(self):
        self.direction = Direction.NONE

    def inputs_known(self, mark):
        i = cast(Variable, self.input())
        return box(cbool(cast(Variable, i).mark == int64(mark) or cbool(cast(Variable, i).stay) or cbool(cast(Variable, i).determined_by is None)))

    def remove_from_graph(self):
        if cast(Variable, self.v1) is not None:
            cast(Variable, self.v1).remove_constraint(self)
        if self.v2 is not None:
            self.v2.remove_constraint(self)
        self.direction = Direction.NONE

@final
class ScaleConstraint(BinaryConstraint):

    def __init__(self, src, scale, offset, dest, strength):
        self.direction = Direction.NONE
        self.scale = scale
        self.offset = offset
        BinaryConstraint.__init__(self, src, dest, strength)

    def add_to_graph(self):
        BinaryConstraint.add_to_graph(self)
        cast(Variable, self.scale).add_constraint(self)
        cast(Variable, self.offset).add_constraint(self)

    def remove_from_graph(self):
        BinaryConstraint.remove_from_graph(self)
        if cast(Variable, self.scale) is not None:
            cast(Variable, self.scale).remove_constraint(self)
        if cast(Variable, self.offset) is not None:
            cast(Variable, self.offset).remove_constraint(self)

    def mark_inputs(self, mark):
        BinaryConstraint.mark_inputs(self, mark)
        cast(Variable, self.scale).mark = int64(mark)
        cast(Variable, self.offset).mark = int64(mark)

    def execute(self) -> None:
        if self.direction == Direction.FORWARD:
            self.v2.value = cast(Variable, self.v1).value * cast(Variable, self.scale).value + cast(Variable, self.offset).value
        else:
            cast(Variable, self.v1).value = (self.v2.value - cast(Variable, self.offset).value) / cast(Variable, self.scale).value

    def recalculate(self):
        ihn = cast(Variable, self.input())
        out = cast(Variable, self.output())
        cast(Variable, out).walk_strength = weakest_of(cast(Strength, self.strength), cast(Variable, ihn).walk_strength)
        cast(Variable, out).stay = box(cbool(cbool(cast(Variable, ihn).stay) and cbool(cast(Variable, self.scale).stay) and cbool(cast(Variable, self.offset).stay)))
        if cbool(cast(Variable, out).stay):
            self.execute()

@final
class EqualityConstraint(BinaryConstraint):

    def execute(self) -> None:
        self.output().value = self.input().value

@final
class Variable(object):

    def __init__(self, name: str, initial_value=0) -> None:
        self.name = name
        self.value: int64 = int64(initial_value)
        self.constraints: CheckedList[Constraint] = []
        self.determined_by: Constraint | None = None
        self.mark: int64 = 0
        self.walk_strength: Strength = WEAKEST
        self.stay = True

    def add_constraint(self, constraint):
        self.constraints.append(cast(Constraint, constraint))

    def remove_constraint(self, constraint: Constraint) -> None:
        self.constraints.remove(constraint)
        if self.determined_by == constraint:
            self.determined_by = None

@final
class Planner(object):

    def __init__(self):
        self.current_mark = 0

    def incremental_add(self, constraint) -> None:
        mark = box(int64(self.new_mark()))
        overridden = constraint.satisfy(int64(mark))
        while overridden is not None:
            overridden = cast(Constraint | None, cast(Constraint, overridden).satisfy(int64(mark)))

    def incremental_remove(self, constraint: Constraint) -> None:
        out = cast(Variable, constraint.output())
        constraint.mark_unsatisfied()
        constraint.remove_from_graph()
        unsatisfied = self.remove_propagate_from(out)
        strength = REQUIRED
        repeat = True
        while repeat:
            for u in unsatisfied:
                if cast(Strength, u.strength) == strength:
                    self.incremental_add(u)
                strength = strength.next_weaker()
            repeat = strength != WEAKEST

    def new_mark(self) -> int64:
        x: int64 = int64(self.current_mark) + 1
        self.current_mark = box(int64(x))
        return int64(self.current_mark)

    def make_plan(self, sources: CheckedList[UrnaryConstraint]) -> Plan:
        mark: int64 = self.new_mark()
        plan = cast(Plan, Plan())
        todo = CheckedList[Constraint]([s for s in sources])
        while clen(todo):
            c = todo.pop(0)
            if c.output().mark != mark and cbool(c.inputs_known(box(int64(mark)))):
                cast(Plan, plan).add_constraint(c)
                c.output().mark = mark
                self.add_constraints_consuming_to(c.output(), todo)
        return plan

    def extract_plan_from_constraints(self, constraints):
        constraints = cast(CheckedList[UrnaryConstraint], constraints)
        sources: CheckedList[UrnaryConstraint] = []
        for c in constraints:
            if cbool(c.is_input()) and cbool(c.is_satisfied()):
                sources.append(c)
        return cast(Plan, self.make_plan(sources))

    def add_propagate(self, c, mark) -> cbool:
        todo: CheckedList[Constraint] = []
        todo.append(cast(Constraint, c))
        while clen(todo):
            d = todo.pop(0)
            if d.output().mark == int64(mark):
                self.incremental_remove(cast(Constraint, c))
                return False
            d.recalculate()
            self.add_constraints_consuming_to(d.output(), todo)
        return True

    def remove_propagate_from(self, out: Variable) -> CheckedList[Constraint]:
        out.determined_by = None
        out.walk_strength = WEAKEST
        out.stay = True
        unsatisfied: CheckedList[Constraint] = []
        todo = CheckedList[Variable]([])
        todo.append(out)
        while len(todo):
            v = todo.pop(0)
            cs = cast(CheckedList[Constraint], v.constraints)
            for c in cs:
                if not c.is_satisfied():
                    unsatisfied.append(c)
            determining = v.determined_by
            for c in cs:
                if c != determining and c.is_satisfied():
                    c.recalculate()
                    todo.append(c.output())
        return unsatisfied

    def add_constraints_consuming_to(self, v, coll: CheckedList[Constraint]):
        determining = cast(Constraint | None, v.determined_by)
        cc = cast(CheckedList[Constraint], v.constraints)
        for c in cc:
            if c != determining and c.is_satisfied():
                coll.append(c)

@final
class Plan(object):

    def __init__(self):
        self.v = CheckedList[Constraint]([])

    def add_constraint(self, c: Constraint):
        cast(CheckedList[Constraint], self.v).append(c)

    def __len__(self):
        return len(cast(CheckedList[Constraint], self.v))

    def __getitem__(self, index):
        return cast(CheckedList[Constraint], self.v)[index]

    def execute(self) -> None:
        for c in cast(CheckedList[Constraint], self.v):
            c.execute()

def recreate_planner() -> Planner:
    global planner
    planner = Planner()
    return planner

def get_planner():
    global planner
    return cast(Planner, planner)

def chain_test(n) -> None:
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
    planner: Planner = recreate_planner()
    prev: Variable | None = None
    first: Variable | None = None
    last: Variable | None = None
    i: int64 = 0
    end = box(int64(int64(n) + 1))
    while i < int64(n) + 1:
        name = 'v%s' % box(i)
        v = Variable(name)
        if prev is not None:
            EqualityConstraint(prev, v, REQUIRED)
        if i == 0:
            first = v
        if i == int64(n):
            last = v
        prev = v
        i = i + 1
    first = cast(Variable, first)
    last = cast(Variable, last)
    StayConstraint(last, STRONG_DEFAULT)
    edit = EditConstraint(first, PREFERRED)
    edits: CheckedList[UrnaryConstraint] = []
    edits.append(edit)
    plan = cast(Plan, planner.extract_plan_from_constraints(edits))
    i = 0
    while i < 100:
        first.value = i
        plan.execute()
        if last.value != i:
            print('Chain test failed.')
        i = i + 1

def projection_test(n) -> None:
    """
    This test constructs a two sets of variables related to each
    other by a simple linear transformation (scale and offset). The
    time is measured to change a variable on either side of the
    mapping and to change the scale and offset factors.
    """
    planner: Planner = recreate_planner()
    scale = Variable('scale', 10)
    offset = Variable('offset', 1000)
    src = None
    dests: CheckedList[Variable] = []
    i = 0
    dst = Variable('dst%s' % 0, 0)
    while int64(i) < int64(n):
        bi = i
        src = Variable('src%s' % bi, i)
        dst = Variable('dst%s' % bi, i)
        dests.append(dst)
        StayConstraint(src, NORMAL)
        ScaleConstraint(src, scale, offset, dst, REQUIRED)
        i = box(int64(int64(i) + 1))
    src = cast(Variable, src)
    change(src, 17)
    if dst.value != 1170:
        print('Projection 1 failed')
    change(dst, 1050)
    if src.value != 5:
        print('Projection 2 failed')
    change(scale, 5)
    i = box(int64(0))
    while int64(i) < int64(n) - 1:
        if dests[int64(i)].value != int64(i) * 5 + 1000:
            print('Projection 3 failed')
        i = box(int64(int64(i) + 1))
    change(offset, 2000)
    i = box(int64(0))
    while int64(i) < int64(n) - 1:
        if dests[int64(i)].value != int64(i) * 5 + 2000:
            print('Projection 4 failed')
        i = box(int64(int64(i) + 1))

def change(v, new_value):
    planner: Planner = cast(Planner, get_planner())
    edit = EditConstraint(v, PREFERRED)
    edits: CheckedList[UrnaryConstraint] = []
    edits.append(edit)
    plan = cast(Plan, planner.extract_plan_from_constraints(edits))
    i: int64 = 0
    while i < 10:
        cast(Variable, v).value = int64(new_value)
        plan.execute()
        i = i + 1
    edit.destroy_constraint()
planner = None

def delta_blue(i) -> None:
    n = int64(i)
    chain_test(box(int64(n)))
    projection_test(box(int64(n)))
if __name__ == '__main__':
    n = 10000
    startTime = time.time()
    delta_blue(n)
    endTime = time.time()
    runtime = endTime - startTime
    print(runtime)