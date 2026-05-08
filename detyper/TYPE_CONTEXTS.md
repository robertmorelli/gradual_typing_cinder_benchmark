# Detyper type contexts

Stage 1 should classify every annotation site with one annotation context and one type kind.

Keep annotation contexts separate from use contexts. Annotation contexts are places where source code carries a type annotation. Use contexts are places where values flow later.

## Annotation contexts

### Module scope

- `module_global_annotation_no_value`
- `module_global_annotation_with_value`

Examples:

```py
x: int64
x: int64 = 1
```

### Class scope

- `class_attribute_annotation_no_value`
- `class_attribute_annotation_with_value`

Examples:

```py
class C:
    x: int64
    y: int64 = 1
```

### Function signatures

- `function_parameter_annotation`
- `function_return_annotation`

Examples:

```py
def f(x: int64) -> int64:
    ...
```

### Method signatures

- `method_self_parameter_annotation`
- `method_parameter_annotation`
- `method_return_annotation`

Examples:

```py
class C:
    def f(self, x: int64) -> int64:
        ...
```

### Constructor signatures

- `constructor_self_parameter_annotation`
- `constructor_parameter_annotation`
- `constructor_return_annotation`

Examples:

```py
class C:
    def __init__(self, x: int64) -> None:
        ...
```

### Function body locals

- `function_local_annotation_no_value`
- `function_local_annotation_with_value`

Examples:

```py
def f():
    x: int64
    y: int64 = 1
```

### Method body locals

- `method_local_annotation_no_value`
- `method_local_annotation_with_value`

Examples:

```py
class C:
    def f(self):
        x: int64
        y: int64 = 1
```

### Constructor body locals

- `constructor_local_annotation_no_value`
- `constructor_local_annotation_with_value`

Examples:

```py
class C:
    def __init__(self):
        x: int64
        y: int64 = 1
```

### Instance variables

- `instance_variable_annotation_no_value`
- `instance_variable_annotation_with_value`
- `init_instance_variable_annotation_no_value`
- `init_instance_variable_annotation_with_value`
- `non_init_instance_variable_annotation_no_value`
- `non_init_instance_variable_annotation_with_value`

Examples:

```py
class C:
    def __init__(self):
        self.x: int64
        self.y: int64 = 1

    def reset(self):
        self.z: int64 = 2
```

### Type aliases

- `type_alias_assignment`
- `annotated_type_alias_assignment`

Examples:

```py
T = int64
T: object = int64
```

## Type kinds

- `cinder_scalar`
- `cinder_checked_container`
- `cinder_static_container`
- `python_scalar`
- `python_container`
- `python_user_object`
- `none_only`
- `optional`
- `union`
- `callable`
- `type_alias`
- `dynamic_unknown`

## Notes

`dynamic_unknown` is real data. Do not guess and pretend certainty.

Pyright is the source of truth for alias resolution in stage 1. Store the source annotation for debugging, but generators should use `resolved_type_src` and `type_kind`.

Recommended shape:

```json
{
  "id": 42,
  "context": "function_local_annotation_with_value",
  "type_kind": "cinder_scalar",
  "annotation_src": "MyInt",
  "resolved_type_src": "int64",
  "resolved_by": "pyright"
}
```
