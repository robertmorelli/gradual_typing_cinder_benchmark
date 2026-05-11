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
def stronger(s1: Strength, s2: Strength):
    return box(cbool(int64(s1.strength) < int64(s2.strength)))

@inline
def weaker(s1: Strength, s2: Strength):
    return box(cbool(int64(s1.strength) > int64(s2.strength)))

@inline
def weakest_of(s1, s2) -> Strength:
    return s1 if int64(cast(Strength, s1).strength) > int64(cast(Strength, s2).strength) else s2

@final
class Strength:

    def __init__(self, strength, name: str) -> None:
        self.strength = strength
        self.name = name

    def next_weaker(self):
        return cast(Strength, cast(Strength, STRENGTHS[self.strength]))
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

    def add_constraint(self) -> None:
        planner = get_planner()
        self.add_to_graph()
        cast(Planner, planner).incremental_add(self)

    def satisfy(self, mark):
        planner: Planner = cast(Planner, get_planner())
        self.choose_method(mark)
        if not self.is_satisfied():
            if cast(Strength, self.strength) == REQUIRED:
                print('Could not satisfy a required constraint!')
            return None
        self.mark_inputs(mark)
        out: Variable = cast(Variable, self.output())
        overridden: Constraint | None = out.determined_by
        if overridden is not None:
            overridden.mark_unsatisfied()
        out.determined_by = self
        if not cbool(planner.add_propagate(self, mark)):
            print('Cycle encountered')
        out.mark = box(int64(int64(mark)))
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

    def choose_method(self, mark):
        pass

    def output(self):
        raise NotImplementedError()

    def execute(self):
        pass

class UrnaryConstraint(Constraint):

    def __init__(self, v, strength):
        Constraint.__init__(self, strength)
        self.my_output = v
        self.satisfied: cbool = False
        self.add_constraint()

    def add_to_graph(self):
        cast(Variable, self.my_output).add_constraint(self)
        self.satisfied = False

    def choose_method(self, mark):
        if int64(cast(Variable, self.my_output).mark) != int64(mark) and cbool(stronger(cast(Strength, self.strength), cast(Variable, self.my_output).walk_strength)):
            self.satisfied = True
        else:
            self.satisfied = False

    def is_satisfied(self):
        return box(cbool(self.satisfied))

    def output(self):
        return cast(Variable, cast(Variable, self.my_output))

    def recalculate(self):
        cast(Variable, self.my_output).walk_strength = cast(Strength, self.strength)
        cast(Variable, self.my_output).stay = not cbool(self.is_input())
        if cast(Variable, self.my_output).stay:
            self.execute()

    def mark_unsatisfied(self) -> None:
        self.satisfied = False

    def remove_from_graph(self):
        if cast(Variable, self.my_output) is not None:
            cast(Variable, self.my_output).remove_constraint(self)
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
        self.v1: Variable = v1
        self.v2 = v2
        self.direction: Direction = Direction.NONE
        self.add_constraint()

    def choose_method(self, mark):
        if int64(self.v1.mark) == int64(mark):
            if int64(cast(Variable, self.v2).mark) != int64(mark) and cbool(stronger(cast(Strength, self.strength), cast(Variable, self.v2).walk_strength)):
                self.direction = Direction.FORWARD
            else:
                self.direction = Direction.BACKWARD
        if int64(cast(Variable, self.v2).mark) == int64(mark):
            if int64(self.v1.mark) != int64(mark) and cbool(stronger(cast(Strength, self.strength), self.v1.walk_strength)):
                self.direction = Direction.BACKWARD
            else:
                self.direction = Direction.NONE
        if cbool(weaker(self.v1.walk_strength, cast(Variable, self.v2).walk_strength)):
            if cbool(stronger(cast(Strength, self.strength), self.v1.walk_strength)):
                self.direction = Direction.BACKWARD
            else:
                self.direction = Direction.NONE
        elif cbool(stronger(cast(Strength, self.strength), cast(Variable, self.v2).walk_strength)):
            self.direction = Direction.FORWARD
        else:
            self.direction = Direction.BACKWARD

    def add_to_graph(self):
        self.v1.add_constraint(self)
        cast(Variable, self.v2).add_constraint(self)
        self.direction = Direction.NONE

    def is_satisfied(self) -> cbool:
        if self.direction != Direction.NONE:
            return True
        return False

    def mark_inputs(self, mark):
        cast(Variable, self.input()).mark = box(int64(int64(mark)))

    def input(self):
        return cast(Variable, self.v1 if self.direction == Direction.FORWARD else cast(Variable, self.v2))

    def output(self):
        return cast(Variable, cast(Variable, self.v2) if self.direction == Direction.FORWARD else self.v1)

    def recalculate(self):
        ihn = self.input()
        out: Variable = cast(Variable, self.output())
        out.walk_strength = weakest_of(cast(Strength, self.strength), cast(Variable, ihn).walk_strength)
        out.stay = cast(Variable, ihn).stay
        if out.stay:
            self.execute()

    def mark_unsatisfied(self) -> None:
        self.direction = Direction.NONE

    def inputs_known(self, mark) -> cbool:
        i = self.input()
        return int64(cast(Variable, i).mark) == int64(mark) or cast(Variable, i).stay or cbool(cast(Variable, i).determined_by is None)

    def remove_from_graph(self):
        if self.v1 is not None:
            self.v1.remove_constraint(self)
        if cast(Variable, self.v2) is not None:
            cast(Variable, self.v2).remove_constraint(self)
        self.direction = Direction.NONE

@final
class ScaleConstraint(BinaryConstraint):

    def __init__(self, src, scale, offset, dest, strength: Strength):
        self.direction: Direction = Direction.NONE
        self.scale: Variable = scale
        self.offset: Variable = offset
        BinaryConstraint.__init__(self, src, dest, strength)

    def add_to_graph(self):
        BinaryConstraint.add_to_graph(self)
        self.scale.add_constraint(self)
        self.offset.add_constraint(self)

    def remove_from_graph(self):
        BinaryConstraint.remove_from_graph(self)
        if self.scale is not None:
            self.scale.remove_constraint(self)
        if self.offset is not None:
            self.offset.remove_constraint(self)

    def mark_inputs(self, mark):
        BinaryConstraint.mark_inputs(self, mark)
        self.scale.mark = box(int64(int64(mark)))
        self.offset.mark = box(int64(int64(mark)))

    def execute(self):
        if self.direction == Direction.FORWARD:
            cast(Variable, self.v2).value = box(int64(int64(self.v1.value) * int64(self.scale.value) + int64(self.offset.value)))
        else:
            self.v1.value = box(int64((int64(cast(Variable, self.v2).value) - int64(self.offset.value)) / int64(self.scale.value)))

    def recalculate(self):
        ihn = self.input()
        out: Variable = cast(Variable, self.output())
        out.walk_strength = weakest_of(cast(Strength, self.strength), cast(Variable, ihn).walk_strength)
        out.stay = cast(Variable, ihn).stay and self.scale.stay and self.offset.stay
        if out.stay:
            self.execute()

@final
class EqualityConstraint(BinaryConstraint):

    def execute(self):
        cast(Variable, self.output()).value = box(int64(int64(cast(Variable, self.input()).value)))

@final
class Variable(object):

    def __init__(self, name, initial_value=0):
        self.name: str = name
        self.value = initial_value
        self.constraints = CheckedList[Constraint]([])
        self.determined_by: Constraint | None = None
        self.mark = box(int64(0))
        self.walk_strength: Strength = WEAKEST
        self.stay: cbool = True

    def add_constraint(self, constraint: Constraint) -> None:
        self.constraints.append(constraint)

    def remove_constraint(self, constraint: Constraint):
        self.constraints.remove(constraint)
        if self.determined_by == constraint:
            self.determined_by = None

@final
class Planner(object):

    def __init__(self):
        self.current_mark: int64 = 0

    def incremental_add(self, constraint):
        mark: int64 = int64(self.new_mark())
        overridden = cast(Constraint, constraint).satisfy(box(int64(mark)))
        while overridden is not None:
            overridden = cast(Constraint | None, cast(Constraint, overridden).satisfy(box(int64(mark))))

    def incremental_remove(self, constraint) -> None:
        out: Variable = cast(Variable, cast(Constraint, constraint).output())
        cast(Constraint, constraint).mark_unsatisfied()
        cast(Constraint, constraint).remove_from_graph()
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
        mark = self.new_mark()
        plan: Plan = Plan()
        todo: CheckedList[Constraint] = [s for s in sources]
        while clen(todo):
            c = todo.pop(0)
            if int64(cast(Variable, c.output()).mark) != int64(mark) and c.inputs_known(mark):
                plan.add_constraint(c)
                cast(Variable, c.output()).mark = box(int64(int64(mark)))
                self.add_constraints_consuming_to(cast(Variable, c.output()), cast(CheckedList[Constraint], todo))
        return plan

    def extract_plan_from_constraints(self, constraints: CheckedList[UrnaryConstraint]):
        sources = CheckedList[UrnaryConstraint]([])
        for c in constraints:
            if cbool(c.is_input()) and cbool(c.is_satisfied()):
                sources.append(c)
        return cast(Plan, self.make_plan(cast(CheckedList[UrnaryConstraint], sources)))

    def add_propagate(self, c: Constraint, mark):
        todo: CheckedList[Constraint] = []
        todo.append(c)
        while clen(todo):
            d = todo.pop(0)
            if int64(cast(Variable, d.output()).mark) == int64(mark):
                self.incremental_remove(c)
                return False
            d.recalculate()
            self.add_constraints_consuming_to(cast(Variable, d.output()), cast(CheckedList[Constraint], todo))
        return True

    def remove_propagate_from(self, out):
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
            determining = v.determined_by
            for c in cs:
                if c != determining and c.is_satisfied():
                    c.recalculate()
                    todo.append(cast(Variable, c.output()))
        return unsatisfied

    def add_constraints_consuming_to(self, v, coll) -> None:
        determining: Constraint | None = cast(Variable, v).determined_by
        cc = cast(CheckedList[Constraint], cast(Variable, v).constraints)
        for c in cc:
            if c != determining and c.is_satisfied():
                coll.append(c)

@final
class Plan(object):

    def __init__(self) -> None:
        self.v: CheckedList[Constraint] = []

    def add_constraint(self, c):
        self.v.append(cast(Constraint, c))

    def __len__(self):
        return len(self.v)

    def __getitem__(self, index):
        return self.v[index]

    def execute(self):
        for c in self.v:
            c.execute()

def recreate_planner():
    global planner
    planner = Planner()
    return cast(Planner, planner)

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
    planner: Planner = cast(Planner, recreate_planner())
    prev: Variable | None = None
    first = None
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
    edits = []
    edits.append(edit)
    plan = cast(Plan, planner.extract_plan_from_constraints(edits))
    i = 0
    while i < 100:
        first.value = box(int64(i))
        plan.execute()
        if int64(last.value) != i:
            print('Chain test failed.')
        i = i + 1

def projection_test(n: int64) -> None:
    """
    This test constructs a two sets of variables related to each
    other by a simple linear transformation (scale and offset). The
    time is measured to change a variable on either side of the
    mapping and to change the scale and offset factors.
    """
    planner = recreate_planner()
    scale = Variable('scale', 10)
    offset = Variable('offset', 1000)
    src: Variable | None = None
    dests = []
    i = box(int64(0))
    dst = Variable('dst%s' % 0, 0)
    while int64(i) < n:
        bi = i
        src = Variable('src%s' % bi, i)
        dst = Variable('dst%s' % bi, i)
        dests.append(dst)
        StayConstraint(src, NORMAL)
        ScaleConstraint(src, scale, offset, dst, REQUIRED)
        i = box(int64(int64(i) + 1))
    src = cast(Variable, src)
    change(src, 17)
    if int64(dst.value) != 1170:
        print('Projection 1 failed')
    change(dst, 1050)
    if int64(src.value) != 5:
        print('Projection 2 failed')
    change(scale, 5)
    i = box(int64(0))
    while int64(i) < n - 1:
        if int64(cast(Variable, dests[i]).value) != int64(i) * 5 + 1000:
            print('Projection 3 failed')
        i = box(int64(int64(i) + 1))
    change(offset, 2000)
    i = box(int64(0))
    while int64(i) < n - 1:
        if int64(cast(Variable, dests[i]).value) != int64(i) * 5 + 2000:
            print('Projection 4 failed')
        i = box(int64(int64(i) + 1))

def change(v, new_value) -> None:
    planner = get_planner()
    edit = EditConstraint(v, PREFERRED)
    edits = []
    edits.append(edit)
    plan = cast(Plan, cast(Planner, planner).extract_plan_from_constraints(edits))
    i = box(int64(0))
    while int64(i) < 10:
        cast(Variable, v).value = box(int64(int64(new_value)))
        plan.execute()
        i = box(int64(int64(i) + 1))
    edit.destroy_constraint()
planner = None

def delta_blue(i):
    n = int64(i)
    chain_test(box(int64(n)))
    projection_test(n)
if __name__ == '__main__':
    n = 10000
    startTime = time.time()
    delta_blue(n)
    endTime = time.time()
    runtime = endTime - startTime
    print(runtime)