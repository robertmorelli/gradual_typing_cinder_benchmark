# Policy suggestions from 5x11 random detyping check

Run: `benchmark_results/random_5x11_phase1_true_types/summary.csv` after phase1 true-type extraction fixes.

Advanced variants, 5 random detypings each:

| benchmark | ok |
|---|---:|
| call_method | 5/5 |
| call_method_slots | 5/5 |
| call_simple | 5/5 |
| chaos | 5/5 |
| deltablue | 0/5 |
| fannkuch | 5/5 |
| float | 5/5 |
| nbody | 1/5 |
| nqueens | 1/5 |
| pystone | 0/5 |
| richards | 0/5 |

## Suggested framework-local fixes

### 1. Add object-parameter attribute receiver places

Failures: `richards` assignments from `initialState.isTaskWaiting()` / `isPacketPending()` returning dynamic.

Likely cause: for a detyped `python_user_object` parameter, `initialState.foo()` needs the receiver cast before member access. Current policy has `attribute_receivers -> cast_wrap`, but phase1 is not consistently emitting that place for the base `Name` of a `MemberAccess`.

Suggested place change:
- emit `attribute_receivers` for parameter/local/global annotations when their reference is the left side of a `MemberAccess`.

Suggested policy coverage:
- `constructor_parameter_annotation`, `function_parameter_annotation`, `method_parameter_annotation`, and local variants with `python_user_object` should cast-wrap `attribute_receivers`.

### 2. Fix class-qualified unbound method call argument indexing

Failures: `BinaryConstraint.mark_inputs(box(int64(self)), ...)`, `Task.findtcb(box(int64(self)), ...)`.

Likely cause: phase1 treats every `MemberAccess` call as a bound method call and offsets positional args by +1. For `ClassName.method(self, ...)`, the first explicit arg is `self`; it must not be shifted onto the second parameter annotation.

Suggested place change:
- in call-site place generation, distinguish instance-bound calls from class-qualified function calls using pyright's callee/left-expression type.
- do not apply the `+1` param offset when the callee receiver is a class object.

### 3. Add cinder container local-read casts

Failures: `nqueens`: `bad argument type 'dynamic' for clen(pool)`.

Likely cause: detyped checked/static container locals/params used at container-consuming operations are not restored to their checked container type.

Suggested policy additions:
- for `function_local_annotation_*`, `method_local_annotation_*`, `constructor_local_annotation_*` with `cinder_checked_container` or `cinder_static_container`, add `local_reads -> cast_wrap`.
- consider a more specific place for `clen_args` if broad local-read casting is too aggressive.

### 4. Strengthen instance field write RHS wrapping for cinder scalars

Failures: `nbody`: `double cannot be assigned to dynamic` at `v.x = double(px) / m`.

Likely cause: when a cinder-scalar instance field annotation is detyped, reassignments through non-`self` receivers are not always categorized as field writes for that field annotation.

Suggested place change:
- ensure pyright declaration lookup for `MemberAccess` writes emits `field_reassign_rhs_value` / `instance_field_writes_value` even when receiver is not literally `self`.

Suggested policy coverage:
- `*_instance_variable_annotation_*` + `cinder_scalar` should box producer values assigned into detyped fields (`primitive_wrap_then_box` for value RHS, constructor/primitive wrapping for literal RHS as appropriate).

### 5. Cover optional/union globals initialized with `None` under `_with_value` fallback

Failures: `pystone`: `Record cannot be assigned to None` after detyping one of `PtrGlb: Record | None = None` / `PtrGlbNext: Record | None = None`.

Likely cause: `Record | None = None` sometimes lands in `module_global_annotation_with_value` rather than `_with_none`; current policy casts `with_none` initializers but not all `with_value` union/optional literal initializers.

Suggested policy additions:
- `module_global_annotation_with_value`, `class_attribute_annotation_with_value`, and instance-variable `_with_value` contexts with `optional`/`union`: add `annotated_value_literal -> cast_wrap` and possibly `annotated_value -> cast_wrap`.

### 6. Add comparison/binop operand places for cinder scalars

Failures: `deltablue`: `can't compare int64 to dynamic`, `dynamic cannot be assigned to int64` around `s1.strength < s2.strength` and `cbool(...)`.

Likely cause: one operand of a primitive operation is dynamic after a related field/parameter detype, and existing `field_reads`/`local_reads` coverage is insufficient in these expression shapes.

Suggested place change:
- emit specific places for cinder-scalar uses in `BinaryOperation` / comparison operands, e.g. `primitive_binop_operands` and `primitive_compare_operands`.

Suggested policy:
- for `cinder_scalar` annotations, wrap those operand places with `primitive_wrap`.
