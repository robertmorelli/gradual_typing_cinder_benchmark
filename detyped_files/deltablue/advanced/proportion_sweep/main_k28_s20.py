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

def _repro_add_constraints_consuming_to_arg1_2(f, arg0, arg1):
    _arg1 = CheckedList[Constraint](arg1)
    _out = f(arg0, _arg1)
    arg1.clear()
    arg1.extend(_arg1)
    return _out

def _repro_extract_plan_from_constraints_arg0_2(f, arg0):
    _arg0 = CheckedList[UrnaryConstraint](arg0)
    _out = f(_arg0)
    arg0.clear()
    arg0.extend(_arg0)
    return _out

def _repro_extract_plan_from_constraints_arg0(f, arg0):
    _arg0 = CheckedList[UrnaryConstraint](arg0)
    _out = f(_arg0)
    arg0.clear()
    arg0.extend(_arg0)
    return _out

def _repro_add_constraints_consuming_to_arg1(f, arg0, arg1):
    _arg1 = CheckedList[Constraint](arg1)
    _out = f(arg0, _arg1)
    arg1.clear()
    arg1.extend(_arg1)
    return _out

@inline
def stronger(s1: Strength, s2: Strength) -> cbool:
    return s1.strength < s2.strength

@inline
def weaker(s1: Strength, s2: Strength) -> cbool:
    return s1.strength > s2.strength

@inline
def weakest_of(s1: Strength, s2: Strength) -> Strength:
    return s1 if s1.strength > s2.strength else s2

@final
class Strength:

    def __init__(self, strength: int64, name: str) -> None:
        self.strength: int64 = strength
        self.name: str = name

    def next_weaker(self):
        return STRENGTHS[self.strength]
REQUIRED = Strength(0, 'required')
STRONG_PREFERRED = Strength(1, 'strongPreferred')
PREFERRED = Strength(2, 'preferred')
STRONG_DEFAULT = Strength(3, 'strongDefault')
NORMAL = Strength(4, 'normal')
WEAK_DEFAULT = Strength(5, 'weakDefault')
WEAKEST = Strength(6, 'weakest')
STRENGTHS: CheckedList[Strength] = CheckedList[Strength]([WEAKEST, WEAK_DEFAULT, NORMAL, STRONG_DEFAULT, PREFERRED, REQUIRED])

class Constraint(object):

    def __init__(self, strength: Strength) -> None:
        self.strength: Strength = strength

    def add_constraint(self):
        planner = cast(Planner, get_planner())
        self.add_to_graph()
        planner.incremental_add(cast(Constraint, self))

    def satisfy(self, _mark):
        mark: int64 = int64(_mark)
        planner = cast(Planner, get_planner())
        self.choose_method(box(int64(mark)))
        if not cbool(self.is_satisfied()):
            if self.strength == REQUIRED:
                print('Could not satisfy a required constraint!')
            return None
        self.mark_inputs(box(int64(mark)))
        out = cast(Variable, self.output())
        overridden = out.determined_by
        if overridden is not None:
            overridden.mark_unsatisfied()
        out.determined_by = self
        if not cbool(planner.add_propagate(cast(Constraint, self), box(int64(mark)))):
            print('Cycle encountered')
        out.mark = mark
        return overridden

    def destroy_constraint(self):
        planner = cast(Planner, get_planner())
        if cbool(self.is_satisfied()):
            planner.incremental_remove(cast(Constraint, self))
        else:
            self.remove_from_graph()

    def is_input(self):
        return box(cbool(False))

    def mark_inputs(self, _mark):
        mark: int64 = int64(_mark)
        pass

    def inputs_known(self, _mark):
        mark: int64 = int64(_mark)
        return box(cbool(True))

    def choose_method(self, _mark):
        mark: int64 = int64(_mark)
        pass

    def output(self):
        raise NotImplementedError()

    def execute(self):
        pass

class UrnaryConstraint(Constraint):

    def __init__(self, v: Variable, strength: Strength) -> None:
        Constraint.__init__(self, strength)
        self.my_output: Variable = v
        self.satisfied: cbool = False
        self.add_constraint()

    def add_to_graph(self):
        self.my_output.add_constraint(self)
        self.satisfied = False

    def choose_method(self, _mark):
        mark: int64 = int64(_mark)
        if self.my_output.mark != mark and stronger(self.strength, self.my_output.walk_strength):
            self.satisfied = True
        else:
            self.satisfied = False

    def is_satisfied(self):
        return box(cbool(self.satisfied))

    def output(self):
        return self.my_output

    def recalculate(self):
        self.my_output.walk_strength = self.strength
        self.my_output.stay = not cbool(self.is_input())
        if self.my_output.stay:
            self.execute()

    def mark_unsatisfied(self):
        self.satisfied = False

    def remove_from_graph(self):
        if self.my_output is not None:
            self.my_output.remove_constraint(cast(Constraint, self))
            self.satisfied = False

@final
class StayConstraint(UrnaryConstraint):
    pass

@final
class EditConstraint(UrnaryConstraint):

    def is_input(self):
        return box(cbool(True))

@final
class Direction(IntEnum):
    NONE = 0
    FORWARD = 1
    BACKWARD = -1

class BinaryConstraint(Constraint):

    def __init__(self, v1: Variable, v2: Variable, strength: Strength) -> None:
        Constraint.__init__(self, strength)
        self.v1: Variable = v1
        self.v2: Variable = v2
        self.direction: Direction = Direction.NONE
        self.add_constraint()

    def choose_method(self, _mark):
        mark: int64 = int64(_mark)
        if self.v1.mark == mark:
            if self.v2.mark != mark and stronger(self.strength, self.v2.walk_strength):
                self.direction = Direction.FORWARD
            else:
                self.direction = Direction.BACKWARD
        if self.v2.mark == mark:
            if self.v1.mark != mark and stronger(self.strength, self.v1.walk_strength):
                self.direction = Direction.BACKWARD
            else:
                self.direction = Direction.NONE
        if weaker(self.v1.walk_strength, self.v2.walk_strength):
            if stronger(self.strength, self.v1.walk_strength):
                self.direction = Direction.BACKWARD
            else:
                self.direction = Direction.NONE
        elif stronger(self.strength, self.v2.walk_strength):
            self.direction = Direction.FORWARD
        else:
            self.direction = Direction.BACKWARD

    def add_to_graph(self):
        self.v1.add_constraint(self)
        self.v2.add_constraint(self)
        self.direction = Direction.NONE

    def is_satisfied(self):
        if self.direction != Direction.NONE:
            return box(cbool(True))
        return box(cbool(False))

    def mark_inputs(self, _mark):
        mark: int64 = int64(_mark)
        self.input().mark = mark

    def input(self) -> Variable:
        return self.v1 if self.direction == Direction.FORWARD else self.v2

    def output(self):
        return self.v2 if self.direction == Direction.FORWARD else self.v1

    def recalculate(self):
        ihn = self.input()
        out = cast(Variable, self.output())
        out.walk_strength = weakest_of(self.strength, ihn.walk_strength)
        out.stay = ihn.stay
        if out.stay:
            self.execute()

    def mark_unsatisfied(self):
        self.direction = Direction.NONE

    def inputs_known(self, _mark):
        mark: int64 = int64(_mark)
        i = self.input()
        return box(cbool(i.mark == mark or i.stay or cbool(i.determined_by is None)))

    def remove_from_graph(self):
        if self.v1 is not None:
            self.v1.remove_constraint(cast(Constraint, self))
        if self.v2 is not None:
            self.v2.remove_constraint(cast(Constraint, self))
        self.direction = Direction.NONE

@final
class ScaleConstraint(BinaryConstraint):

    def __init__(self, src: Variable, scale: Variable, offset: Variable, dest: Variable, strength: Strength) -> None:
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
            self.scale.remove_constraint(cast(Constraint, self))
        if self.offset is not None:
            self.offset.remove_constraint(cast(Constraint, self))

    def mark_inputs(self, _mark):
        mark: int64 = int64(_mark)
        BinaryConstraint.mark_inputs(self, box(int64(mark)))
        self.scale.mark = mark
        self.offset.mark = mark

    def execute(self):
        if self.direction == Direction.FORWARD:
            self.v2.value = self.v1.value * self.scale.value + self.offset.value
        else:
            self.v1.value = (self.v2.value - self.offset.value) / self.scale.value

    def recalculate(self):
        ihn = self.input()
        out = cast(Variable, self.output())
        out.walk_strength = weakest_of(self.strength, ihn.walk_strength)
        out.stay = ihn.stay and self.scale.stay and self.offset.stay
        if out.stay:
            self.execute()

@final
class EqualityConstraint(BinaryConstraint):

    def execute(self):
        cast(Variable, self.output()).value = self.input().value

@final
class Variable(object):

    def __init__(self, name: str, initial_value: int64=0) -> None:
        self.name: str = name
        self.value: int64 = initial_value
        self.constraints: CheckedList[Constraint] = []
        self.determined_by: Constraint | None = None
        self.mark: int64 = 0
        self.walk_strength: Strength = WEAKEST
        self.stay: cbool = True

    def add_constraint(self, constraint: Constraint):
        self.constraints.append(constraint)

    def remove_constraint(self, _constraint):
        constraint: Constraint = cast(Constraint, _constraint)
        self.constraints.remove(constraint)
        if self.determined_by == constraint:
            self.determined_by = None

@final
class Planner(object):

    def __init__(self) -> None:
        self.current_mark: int64 = 0

    def incremental_add(self, _constraint):
        constraint: Constraint = cast(Constraint, _constraint)
        mark = self.new_mark()
        overridden = cast(Constraint | None, constraint.satisfy(box(int64(mark))))
        while overridden is not None:
            overridden = cast(Constraint | None, overridden.satisfy(box(int64(mark))))

    def incremental_remove(self, _constraint):
        constraint: Constraint = cast(Constraint, _constraint)
        out = cast(Variable, constraint.output())
        constraint.mark_unsatisfied()
        constraint.remove_from_graph()
        unsatisfied = self.remove_propagate_from(out)
        strength = REQUIRED
        repeat = True
        while repeat:
            for u in unsatisfied:
                if u.strength == strength:
                    self.incremental_add(cast(Constraint, u))
                strength = cast(Strength, strength.next_weaker())
            repeat = strength != WEAKEST

    def new_mark(self) -> int64:
        x = self.current_mark + 1
        self.current_mark = x
        return self.current_mark

    def make_plan(self, sources: CheckedList[UrnaryConstraint]) -> Plan:
        mark = self.new_mark()
        plan = Plan()
        todo: CheckedList[Constraint] = [s for s in sources]
        while clen(todo):
            c = todo.pop(0)
            if cast(Variable, c.output()).mark != mark and cbool(c.inputs_known(box(int64(mark)))):
                plan.add_constraint(c)
                cast(Variable, c.output()).mark = mark
                _repro_add_constraints_consuming_to_arg1_2(self.add_constraints_consuming_to, cast(Variable, c.output()), todo)
        return plan

    def extract_plan_from_constraints(self, constraints):
        constraints = cast(CheckedList[UrnaryConstraint], constraints)
        sources = CheckedList[UrnaryConstraint]([])
        for c in constraints:
            if cbool(c.is_input()) and cbool(c.is_satisfied()):
                sources.append(c)
        return self.make_plan(sources)

    def add_propagate(self, _c, _mark):
        c: Constraint = cast(Constraint, _c)
        mark: int64 = int64(_mark)
        todo = CheckedList[Constraint]([])
        todo.append(c)
        while clen(todo):
            d = todo.pop(0)
            if cast(Variable, d.output()).mark == mark:
                self.incremental_remove(cast(Constraint, c))
                return box(cbool(False))
            d.recalculate()
            _repro_add_constraints_consuming_to_arg1(self.add_constraints_consuming_to, cast(Variable, d.output()), todo)
        return box(cbool(True))

    def remove_propagate_from(self, out: Variable) -> CheckedList[Constraint]:
        out.determined_by = None
        out.walk_strength = WEAKEST
        out.stay = True
        unsatisfied: CheckedList[Constraint] = []
        todo: CheckedList[Variable] = []
        todo.append(out)
        while len(todo):
            v = todo.pop(0)
            cs = v.constraints
            for c in cs:
                if not cbool(c.is_satisfied()):
                    unsatisfied.append(c)
            determining = v.determined_by
            for c in cs:
                if c != determining and cbool(c.is_satisfied()):
                    c.recalculate()
                    todo.append(cast(Variable, c.output()))
        return unsatisfied

    def add_constraints_consuming_to(self, _v, coll):
        v: Variable = cast(Variable, _v)
        coll = cast(CheckedList[Constraint], coll)
        determining = v.determined_by
        cc = v.constraints
        for c in cc:
            if c != determining and cbool(c.is_satisfied()):
                coll.append(c)

@final
class Plan(object):

    def __init__(self) -> None:
        self.v: CheckedList[Constraint] = []

    def add_constraint(self, c: Constraint):
        self.v.append(c)

    def __len__(self):
        return len(self.v)

    def __getitem__(self, index):
        return self.v[index]

    def execute(self):
        for c in self.v:
            c.execute()

def recreate_planner() -> Planner:
    global planner
    planner = Planner()
    return planner

def get_planner():
    global planner
    return planner

def chain_test(_n):
    n: int64 = int64(_n)
    '\n    This is the standard DeltaBlue benchmark. A long chain of equality\n    constraints is constructed with a stay constraint on one end. An\n    edit constraint is then added to the opposite end and the time is\n    measured for adding and removing this constraint, and extracting\n    and executing a constraint satisfaction plan. There are two cases.\n    In case 1, the added constraint is stronger than the stay\n    constraint and values must propagate down the entire length of the\n    chain. In case 2, the added constraint is weaker than the stay\n    constraint so it cannot be accomodated. The cost in this case is,\n    of course, very low. Typical situations lie somewhere between these\n    two extremes.\n    '
    planner = recreate_planner()
    prev = cast(Variable | None, None)
    first = cast(Variable | None, None)
    last = cast(Variable | None, None)
    i: int64 = int64(0)
    end: int64 = int64(n + 1)
    while i < n + 1:
        name = 'v%s' % box(i)
        v = Variable(name)
        if prev is not None:
            EqualityConstraint(prev, v, REQUIRED)
        if i == 0:
            first = v
        if i == n:
            last = v
        prev = v
        i = i + 1
    first = cast(Variable, first)
    last = cast(Variable, last)
    StayConstraint(last, STRONG_DEFAULT)
    edit = EditConstraint(first, PREFERRED)
    edits = CheckedList[UrnaryConstraint]([])
    edits.append(edit)
    plan = cast(Plan, _repro_extract_plan_from_constraints_arg0(planner.extract_plan_from_constraints, edits))
    i = 0
    while i < 100:
        first.value = i
        plan.execute()
        if last.value != i:
            print('Chain test failed.')
        i = i + 1

def projection_test(_n):
    n: int64 = int64(_n)
    '\n    This test constructs a two sets of variables related to each\n    other by a simple linear transformation (scale and offset). The\n    time is measured to change a variable on either side of the\n    mapping and to change the scale and offset factors.\n    '
    planner = recreate_planner()
    scale = Variable('scale', 10)
    offset = Variable('offset', 1000)
    src = cast(Variable | None, None)
    dests = CheckedList[Variable]([])
    i: int64 = int64(0)
    dst = Variable('dst%s' % 0, 0)
    while i < n:
        bi = box(i)
        src = Variable('src%s' % bi, i)
        dst = Variable('dst%s' % bi, i)
        dests.append(dst)
        StayConstraint(src, NORMAL)
        ScaleConstraint(src, scale, offset, dst, REQUIRED)
        i = i + 1
    src = cast(Variable, src)
    change(cast(Variable, src), box(int64(17)))
    if dst.value != 1170:
        print('Projection 1 failed')
    change(cast(Variable, dst), box(int64(1050)))
    if src.value != 5:
        print('Projection 2 failed')
    change(cast(Variable, scale), box(int64(5)))
    i = 0
    while i < n - 1:
        if dests[i].value != i * 5 + 1000:
            print('Projection 3 failed')
        i = i + 1
    change(cast(Variable, offset), box(int64(2000)))
    i = 0
    while i < n - 1:
        if dests[i].value != i * 5 + 2000:
            print('Projection 4 failed')
        i = i + 1

def change(_v, _new_value):
    v: Variable = cast(Variable, _v)
    new_value: int64 = int64(_new_value)
    planner = cast(Planner, get_planner())
    edit = EditConstraint(v, PREFERRED)
    edits = CheckedList[UrnaryConstraint]([])
    edits.append(edit)
    plan = cast(Plan, _repro_extract_plan_from_constraints_arg0_2(planner.extract_plan_from_constraints, edits))
    i: int64 = int64(0)
    while i < 10:
        v.value = new_value
        plan.execute()
        i = i + 1
    edit.destroy_constraint()
planner = None

def delta_blue(i: int) -> None:
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