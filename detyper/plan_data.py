"""PlanData and function-level annotation merging."""

from dataclasses import dataclass
import ast
from ast import FunctionDef, Module

from .ast_utils import node_index
from .rules import expand_aliases, resolve_annotation

TypeSpec = ast.expr


@dataclass(frozen=True)
class FuncInfo:
    fun_name: str
    param_types: list[TypeSpec | None]
    return_type: TypeSpec | None
    is_detyped: bool


@dataclass(frozen=True)
class PlanData:
    funcs: dict[str, FuncInfo]
    aliases: dict[str, TypeSpec]
    class_fields: dict[str, dict[str, TypeSpec]]
    class_init_params: dict[str, list[TypeSpec | None]]
    func_classes: dict[int, str]
    selected_annotation_ids: set[int] | None = None
    selected_field_types: dict[tuple[str, str], TypeSpec] | None = None
    selected_constructor_param_types: dict[tuple[str, int], TypeSpec] | None = None
    class_bases: dict[str, str] | None = None


def _annotations_equal(a: TypeSpec, b: TypeSpec) -> bool:
    return ast.dump(a) == ast.dump(b)


def _optional_member(typ: TypeSpec | None) -> TypeSpec | None:
    if typ is None:
        return None
    if isinstance(typ, ast.Subscript) and isinstance(typ.value, ast.Name) and typ.value.id == 'Optional':
        return typ.slice
    if (
        isinstance(typ, ast.BinOp)
        and isinstance(typ.op, ast.BitOr)
        and isinstance(typ.right, ast.Constant)
        and typ.right.value is None
    ):
        return typ.left
    if (
        isinstance(typ, ast.BinOp)
        and isinstance(typ.op, ast.BitOr)
        and isinstance(typ.left, ast.Constant)
        and typ.left.value is None
    ):
        return typ.right
    return None


def _merge_annotations(a: TypeSpec | None, b: TypeSpec | None) -> TypeSpec | None | object:
    """Tiny ad-hoc unifier for benchmark examples.

    Supported special case:
    - T with Optional[T]
    - T with T | None

    In that case we keep the optional form, since it is the less specific type.
    Returns _CONFLICT when the two annotations still do not unify.
    """
    if a is None:
        return b
    if b is None:
        return a
    if _annotations_equal(a, b):
        return a

    a_inner = _optional_member(a)
    if a_inner is not None and _annotations_equal(a_inner, b):
        return a

    b_inner = _optional_member(b)
    if b_inner is not None and _annotations_equal(a, b_inner):
        return b

    return _CONFLICT


_CONFLICT = object()


def _is_type_expr(expr: ast.expr | None) -> bool:
    if expr is None:
        return False
    if isinstance(expr, ast.Name):
        return True
    if isinstance(expr, ast.Constant):
        return expr.value is None or isinstance(expr.value, str)
    if isinstance(expr, ast.Subscript):
        return _is_type_expr(expr.value) and _is_type_expr(expr.slice)
    if isinstance(expr, ast.Tuple):
        return all(_is_type_expr(elt) for elt in expr.elts)
    if isinstance(expr, ast.BinOp) and isinstance(expr.op, ast.BitOr):
        return _is_type_expr(expr.left) and _is_type_expr(expr.right)
    return False


def _collect_type_aliases(module: Module) -> dict[str, TypeSpec]:
    aliases: dict[str, TypeSpec] = {}
    for stmt in module.body:
        if isinstance(stmt, ast.Assign) and len(stmt.targets) == 1 and isinstance(stmt.targets[0], ast.Name):
            resolved = resolve_annotation(stmt.value)
            if _is_type_expr(resolved):
                aliases[stmt.targets[0].id] = resolved
        elif isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name) and stmt.value is not None:
            resolved = resolve_annotation(stmt.value)
            if _is_type_expr(resolved):
                aliases[stmt.target.id] = resolved
    return {name: expand_aliases(typ, aliases) or typ for name, typ in aliases.items()}


def _indexes(module: Module) -> dict:
    indexes = getattr(module, 'detyping_indexes', None)
    if indexes is None:
        raise ValueError('PlanData requires staged AstData indexes')
    return indexes


def _collect_func_classes(module: Module) -> dict[int, str]:
    return {int(key): value for key, value in _indexes(module).get('func_classes', {}).items()}


def _collect_class_init_params(module: Module, aliases: dict[str, TypeSpec]) -> dict[str, list[TypeSpec | None]]:
    result: dict[str, list[TypeSpec | None]] = {}
    indexes = _indexes(module)
    by_id = node_index(module)
    for cls, arg_ids in indexes.get('class_init_param_annotation_ids', {}).items():
        result[cls] = [
            expand_aliases(resolve_annotation(by_id[arg_id].annotation), aliases)
            if arg_id is not None and arg_id in by_id and isinstance(by_id[arg_id], ast.arg)
            else None
            for arg_id in arg_ids
        ]
    bases = dict(indexes.get('class_bases', {}))
    changed = True
    while changed:
        changed = False
        for cls, base in bases.items():
            if cls not in result and base in result:
                result[cls] = result[base]
                changed = True
    return result


def _collect_class_fields(module: Module, aliases: dict[str, TypeSpec]) -> dict[str, dict[str, TypeSpec]]:
    fields: dict[str, dict[str, TypeSpec]] = {}
    indexes = _indexes(module)
    by_id = node_index(module)
    bases = dict(indexes.get('class_bases', {}))
    for cls_data in indexes.get('classes', {}).values():
        fields.setdefault(cls_data['name'], {})
    for cls, ann_by_field in indexes.get('class_field_annotations', {}).items():
        cls_fields: dict[str, TypeSpec] = {}
        for field, ann_id in ann_by_field.items():
            ann = by_id.get(int(ann_id))
            if isinstance(ann, ast.AnnAssign):
                typ = expand_aliases(resolve_annotation(ann.annotation), aliases)
                if typ is not None:
                    cls_fields[field] = typ
        fields[cls] = cls_fields
    changed = True
    while changed:
        changed = False
        for cls, base in bases.items():
            if base not in fields:
                continue
            inherited = dict(fields[base])
            inherited.update(fields.get(cls, {}))
            if inherited != fields.get(cls, {}):
                fields[cls] = inherited
                changed = True
    return fields


def _function_annotation_ids(fdef: FunctionDef) -> set[int]:
    indexes = getattr(fdef, 'detyping_indexes', None)
    if indexes is None:
        raise ValueError('Function annotation metadata requires staged AstData indexes')
    return set(indexes.get('function_annotation_ids', {}).get(str(fdef.detyping_id), []))


def build_plan_data(module: Module, defs: list, guide: dict) -> PlanData:
    """Build PlanData from function defs and a permutation guide.

    guide: dict[str, bool] — fun_name -> is_detyped
    On arity or annotation conflict (for example, same method name in different
    classes), the conflicting annotation slots are cleared to None so wrapping
    can be skipped safely without discarding the whole function.
    """
    aliases = _collect_type_aliases(module)
    class_fields = _collect_class_fields(module, aliases)
    class_init_params = _collect_class_init_params(module, aliases)
    func_classes = _collect_func_classes(module)
    indexes = _indexes(module)
    class_bases: dict[str, str] = dict(indexes.get('class_bases', {}))
    guide_selected_ids = {key for key, value in guide.items() if isinstance(key, int) and value}
    if guide_selected_ids:
        expanded_selected_ids = set(guide_selected_ids)
        for fdef in defs:
            if fdef.name != '__init__':
                continue
            selected_arg_names = {
                arg.arg
                for arg in fdef.args.args[1:]
                if arg.annotation is not None and arg.detyping_id in guide_selected_ids
            }
            if not selected_arg_names:
                continue
            candidate_ids = indexes.get('ann_assigns_by_function', {}).get(str(fdef.detyping_id), [])
            by_id = node_index(module)
            for ann_id in candidate_ids:
                node = by_id.get(int(ann_id))
                if (
                    isinstance(node, ast.AnnAssign)
                    and node.annotation is not None
                    and isinstance(node.target, ast.Attribute)
                    and isinstance(node.target.value, ast.Name)
                    and node.target.value.id == 'self'
                    and isinstance(node.value, ast.Name)
                    and node.value.id in selected_arg_names
                ):
                    expanded_selected_ids.add(node.detyping_id)
        guide_selected_ids = expanded_selected_ids
    selected_field_types: dict[tuple[str, str], TypeSpec] | None = None
    selected_constructor_param_types: dict[tuple[str, int], TypeSpec] | None = None
    if guide_selected_ids:
        selected_field_types = {}
        selected_constructor_param_types = {}
        for fdef in defs:
            owner_class = func_classes.get(fdef.detyping_id)
            if owner_class is None:
                continue
            if fdef.name == '__init__':
                for idx, arg in enumerate(fdef.args.args[1:]):
                    if arg.annotation is not None and arg.detyping_id in guide_selected_ids:
                        typ = expand_aliases(resolve_annotation(arg.annotation), aliases)
                        if typ is not None:
                            selected_constructor_param_types[(owner_class, idx)] = typ
            candidate_ids = indexes.get('ann_assigns_by_function', {}).get(str(fdef.detyping_id), [])
            by_id = node_index(module)
            for ann_id in candidate_ids:
                node = by_id.get(int(ann_id))
                if (
                    isinstance(node, ast.AnnAssign)
                    and node.detyping_id in guide_selected_ids
                    and isinstance(node.target, ast.Attribute)
                ):
                    typ = expand_aliases(resolve_annotation(node.annotation), aliases)
                    if typ is not None:
                        selected_field_types[(owner_class, node.target.attr)] = typ
    grouped: dict[str, list] = {}
    for fdef in defs:
        name = fdef.name
        grouped.setdefault(name, []).append(fdef)

    funcs: dict[str, FuncInfo] = {}
    for name, fdefs in grouped.items():
        base = fdefs[0]
        base_params = base.args.args
        n = len(base_params)

        param_types: list = [
            expand_aliases(resolve_annotation(a.annotation if a.annotation else None), aliases)
            for a in base_params
        ]
        return_type: TypeSpec | None = expand_aliases(resolve_annotation(base.returns), aliases)
        param_locked = [False] * n
        return_locked = False

        for fdef in fdefs[1:]:
            fargs = fdef.args.args
            if len(fargs) != n:
                param_types = [None] * n
                return_type = None
                break
            for i, (merged, new_arg) in enumerate(zip(param_types, fargs)):
                if param_locked[i]:
                    continue
                new_ann = expand_aliases(resolve_annotation(new_arg.annotation if new_arg.annotation else None), aliases)
                merged_ann = _merge_annotations(merged, new_ann)
                if merged_ann is _CONFLICT:
                    param_types[i] = None
                    param_locked[i] = True
                else:
                    param_types[i] = merged_ann
            new_ret = expand_aliases(resolve_annotation(fdef.returns), aliases)
            if return_locked:
                pass
            else:
                merged_ret = _merge_annotations(return_type, new_ret)
                if merged_ret is _CONFLICT:
                    return_type = None
                    return_locked = True
                else:
                    return_type = merged_ret

        has_inline = any(
            (isinstance(d, ast.Name) and d.id == 'inline') or
            (isinstance(d, ast.Attribute) and d.attr == 'inline')
            for fdef in fdefs
            for d in fdef.decorator_list
        )
        selected_annotation_ids = guide_selected_ids
        if selected_annotation_ids:
            is_detyped = (not has_inline) and any(_function_annotation_ids(fdef) & selected_annotation_ids for fdef in fdefs)
        else:
            selected_annotation_ids = None
            is_detyped = (not has_inline) and guide.get(name, False)
        funcs[name] = FuncInfo(
            fun_name=name,
            param_types=param_types,
            return_type=return_type,
            is_detyped=is_detyped,
        )

    return PlanData(
        funcs=funcs,
        aliases=aliases,
        class_fields=class_fields,
        class_init_params=class_init_params,
        func_classes=func_classes,
        selected_annotation_ids=selected_annotation_ids,
        selected_field_types=selected_field_types,
        selected_constructor_param_types=selected_constructor_param_types,
        class_bases=class_bases,
    )
