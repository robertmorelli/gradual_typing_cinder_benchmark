# Policy Matrix Issues

Isolated `(context, type_kind)` policy failures found from the failed-benchmark policy matrices.

## fannkuch shallow

- `(function_local_annotation_with_value, python_user_object)`
  - Issue: runtime failure in isolation.
  - Interpretation: the function-local initialized user-object policy is individually unsafe for `fannkuch shallow`.

## float advanced

- `(function_parameter_annotation, cinder_checked_container)`
  - Issue: runtime failure in isolation.
  - Interpretation: the function checked-container parameter policy is individually unsafe for `float advanced`.

## nbody advanced

- `(function_local_annotation_with_value, cinder_checked_container)`
  - Issue: runtime failure in isolation.
  - Interpretation: the function-local initialized checked-container policy is individually unsafe for `nbody advanced`.

- `(function_parameter_annotation, cinder_checked_container)`
  - Issue: runtime failure in isolation.
  - Interpretation: the function checked-container parameter policy is individually unsafe for `nbody advanced`.

## nqueens advanced

- `(function_parameter_annotation, cinder_scalar)`
  - Issue: typecheck failure in isolation; filtered out before runtime.
  - Interpretation: the function cinder-scalar parameter policy does not preserve static compatibility for `nqueens advanced`.

## richards advanced

- `(constructor_parameter_annotation, cinder_scalar)`
  - Issue: typecheck failure in isolation; filtered out before runtime.
  - Interpretation: the constructor cinder-scalar parameter policy does not preserve static compatibility for `richards advanced`.

- `(method_parameter_annotation, cinder_scalar)`
  - Issue: typecheck failure in isolation; filtered out before runtime.
  - Interpretation: the method cinder-scalar parameter policy does not preserve static compatibility for `richards advanced`.

## call_method shallow

No isolated bad `(context, type_kind)` policy was found in the matrix. The previous failure is therefore likely either a policy interaction or infra noise from the docker daemon conflicts observed during the run.
