import importlib.util
spec=importlib.util.spec_from_file_location('db','benchmark_results/deltablue_max_detyped.py')
db=importlib.util.module_from_spec(spec); spec.loader.exec_module(db)
planner=db.recreate_planner()
prev=None; first=None; last=None
vars=[]
for i in range(3):
    v=db.Variable('v%s'%i); vars.append(v)
    if prev is not None: db.EqualityConstraint(prev, v, db.REQUIRED)
    if i==0: first=v
    if i==2: last=v
    prev=v
db.StayConstraint(last, db.STRONG_DEFAULT)
edit=db.EditConstraint(first, db.PREFERRED)
print('determined', [type(v.determined_by).__name__ if v.determined_by else None for v in vars])
for v in vars: print(v.name, 'mark', v.mark, 'stay', v.stay, 'walk', getattr(v.walk_strength,'name',None), 'constraints', [(type(c).__name__, getattr(c,'direction',None), c.is_satisfied()) for c in v.constraints])
todo=db.CheckedList[db.Constraint]([])
planner.add_constraints_consuming_to(first, todo)
print('todo after consuming first', [type(c).__name__ for c in todo])
edits=db.CheckedList[db.UrnaryConstraint]([]); edits.append(edit)
plan=planner.extract_plan_from_constraints(db.CheckedList[db.UrnaryConstraint](edits))
print('plan len', len(plan.v), [type(c).__name__ for c in plan.v])
first.value=db.box(db.int64(42)); plan.execute(); print('values', [v.value for v in vars])
