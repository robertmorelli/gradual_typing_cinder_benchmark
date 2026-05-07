"""Pure detyping pipeline with no benchmark execution side effects."""

from __future__ import annotations

import ast
import json
from ast import Module
from dataclasses import dataclass
from functools import reduce
from pathlib import Path

from .annotation_sites import annotation_selection_closure, annotation_sites_from_tree
from .ast_utils import all_function_defs, all_function_uses, all_method_uses, label_tree, node_index
from .generators import (
    generate_tasks_body,
    generate_tasks_constructor_calls,
    generate_tasks_global_annotations,
    generate_tasks_params_calls,
    generate_tasks_params_definition,
    generate_tasks_return_calls,
    generate_tasks_return_definition,
)
from .plan_data import build_plan_data
from .tasks import Detyper, intent_from_json, intent_to_json
from .typecheck import decorate_ast_with_pyright

Permutation = tuple[bool, ...]
GuideType = dict[str, bool]


@dataclass(frozen=True)
class DetypedProgram:
    perm: Permutation
    perm_hex: str
    source: str


def perm_name(perm: Permutation) -> str:
    if not perm:
        return '0x0'
    return hex(int(''.join(str(int(bit)) for bit in perm), 2))


def _convert_sentinel_ann_assigns(body: list[ast.stmt]) -> list[ast.stmt]:
    """Replace AnnAssign(annotation=None) sentinels with plain Assign nodes."""
    result: list[ast.stmt] = []
    for stmt in body:
        if isinstance(stmt, ast.AnnAssign) and stmt.annotation is None:
            if stmt.value is not None:
                result.append(ast.Assign(
                    targets=[stmt.target],
                    value=stmt.value,
                    lineno=stmt.lineno,
                    col_offset=stmt.col_offset,
                ))
            continue
        result.append(stmt)
    return result


def _post_process(module: Module) -> None:
    """Normalize sentinel nodes across every statement list in the module."""
    for node in ast.walk(module):
        if hasattr(node, 'body') and isinstance(node.body, list):
            node.body = _convert_sentinel_ann_assigns(node.body)
        for attr in ('orelse', 'finalbody', 'handlers'):
            value = getattr(node, attr, None)
            if isinstance(value, list):
                if value and isinstance(value[0], list):
                    continue
                setattr(node, attr, _convert_sentinel_ann_assigns(value))
    _unwrap_redundant_box(module)


_PRIMITIVE_NUMERIC_NAMES = frozenset({
    'int64', 'int32', 'int16', 'int8',
    'uint64', 'uint32', 'uint16', 'uint8',
    'float64', 'float32', 'double', 'cbool',
})


class _RedundantBoxUnwrapper(ast.NodeTransformer):
    def __init__(self, boxed_names: set[str], skip_node_ids: set[int] | None = None):
        self.boxed_names = boxed_names
        self.skip_node_ids = skip_node_ids or set()

    def _is_boxed_name(self, expr: ast.expr) -> bool:
        return isinstance(expr, ast.Name) and expr.id in self.boxed_names

    def visit_Call(self, node: ast.Call):
        if id(node) in self.skip_node_ids:
            return node
        if isinstance(node.func, ast.Name) and len(node.args) == 1:
            func_name = node.func.id
            inner = node.args[0]
            if (
                func_name in _PRIMITIVE_NUMERIC_NAMES
                and isinstance(inner, ast.Call)
                and isinstance(inner.func, ast.Name)
                and inner.func.id == 'box'
                and len(inner.args) == 1
                and self._is_boxed_name(inner.args[0])
            ):
                return ast.copy_location(inner.args[0], node)
            if (
                func_name == 'box'
                and isinstance(inner, ast.Call)
                and isinstance(inner.func, ast.Name)
                and inner.func.id in _PRIMITIVE_NUMERIC_NAMES
                and len(inner.args) == 1
                and self._is_boxed_name(inner.args[0])
            ):
                return ast.copy_location(inner.args[0], node)
        self.generic_visit(node)
        if not (isinstance(node.func, ast.Name) and len(node.args) == 1):
            return node
        if node.func.id == 'box' and self._is_boxed_name(node.args[0]):
            return ast.copy_location(node.args[0], node)
        return node


def _unwrap_redundant_box(module: Module) -> None:
    """Remove box(name) when name is a local already assigned via box(...)."""
    class_primitive_fields = _collect_primitive_attr_fields_per_class(module)
    func_owner_class = _func_owner_classes(module)
    func_local_classes = _func_local_class_types(module, func_owner_class)
    for fdef in ast.walk(module):
        if not isinstance(fdef, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        boxed: set[str] = set()
        for assign in ast.walk(fdef):
            if not isinstance(assign, ast.Assign):
                continue
            if not (isinstance(assign.value, ast.Call) and isinstance(assign.value.func, ast.Name) and assign.value.func.id == 'box'):
                continue
            for target in assign.targets:
                if isinstance(target, ast.Name):
                    boxed.add(target.id)
        owner_cls = func_owner_class.get(id(fdef))
        local_types = func_local_classes.get(id(fdef), {})

        def _target_attr_is_primitive_kept(target: ast.expr) -> bool:
            if not isinstance(target, ast.Attribute):
                return False
            cls = _resolve_target_owner(target.value, owner_cls, local_types)
            if cls is None:
                return False
            return target.attr in class_primitive_fields.get(cls, set())

        skip_value_ids: set[int] = set()
        for assign in ast.walk(fdef):
            if not isinstance(assign, ast.Assign):
                continue
            for target in assign.targets:
                if _target_attr_is_primitive_kept(target):
                    skip_value_ids.add(id(assign.value))
                    break
        if boxed:
            _RedundantBoxUnwrapper(boxed, skip_value_ids).visit(fdef)
        for assign in ast.walk(fdef):
            if not isinstance(assign, ast.Assign):
                continue
            if not any(_target_attr_is_primitive_kept(t) for t in assign.targets):
                continue
            v = assign.value
            if (
                isinstance(v, ast.Call)
                and isinstance(v.func, ast.Name)
                and v.func.id == 'box'
                and len(v.args) == 1
                and isinstance(v.args[0], ast.Call)
                and isinstance(v.args[0].func, ast.Name)
                and v.args[0].func.id in _PRIMITIVE_NUMERIC_NAMES
            ):
                assign.value = v.args[0]
        _wrap_kept_primitive_assigns(fdef, boxed)


def _collect_primitive_attr_fields_per_class(module: Module) -> dict[str, set[str]]:
    result: dict[str, set[str]] = {}
    for cls in module.body:
        if not isinstance(cls, ast.ClassDef):
            continue
        fields: set[str] = set()
        for stmt in ast.walk(cls):
            if (
                isinstance(stmt, ast.AnnAssign)
                and isinstance(stmt.target, ast.Attribute)
                and isinstance(stmt.target.value, ast.Name)
                and stmt.target.value.id == 'self'
                and isinstance(stmt.annotation, ast.Name)
                and stmt.annotation.id in _PRIMITIVE_NUMERIC_NAMES
            ):
                fields.add(stmt.target.attr)
        result[cls.name] = fields
    bases: dict[str, str] = {}
    for cls in module.body:
        if isinstance(cls, ast.ClassDef):
            for base in cls.bases:
                if isinstance(base, ast.Name):
                    bases[cls.name] = base.id
                    break
    changed = True
    while changed:
        changed = False
        for cls, base in bases.items():
            if base in result:
                merged = result[base] | result.get(cls, set())
                if merged != result.get(cls, set()):
                    result[cls] = merged
                    changed = True
    return result


def _func_owner_classes(module: Module) -> dict[int, str]:
    result: dict[int, str] = {}
    for cls in module.body:
        if isinstance(cls, ast.ClassDef):
            for item in cls.body:
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    result[id(item)] = cls.name
    return result


def _func_local_class_types(module: Module, owner_classes: dict[int, str]) -> dict[int, dict[str, str]]:
    result: dict[int, dict[str, str]] = {}
    for fdef in ast.walk(module):
        if not isinstance(fdef, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        local_types: dict[str, str] = {}
        for arg in fdef.args.args:
            if isinstance(arg.annotation, ast.Name):
                local_types[arg.arg] = arg.annotation.id
        for stmt in ast.walk(fdef):
            if isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name) and isinstance(stmt.annotation, ast.Name):
                local_types[stmt.target.id] = stmt.annotation.id
            elif isinstance(stmt, ast.Assign) and len(stmt.targets) == 1 and isinstance(stmt.targets[0], ast.Name) and isinstance(stmt.value, ast.Call) and isinstance(stmt.value.func, ast.Name) and stmt.value.func.id == 'cast' and stmt.value.args:
                cast_typ = stmt.value.args[0]
                cls_name = None
                if isinstance(cast_typ, ast.Name):
                    cls_name = cast_typ.id
                elif isinstance(cast_typ, ast.Subscript) and isinstance(cast_typ.value, ast.Name) and cast_typ.value.id == 'Optional' and isinstance(cast_typ.slice, ast.Name):
                    cls_name = cast_typ.slice.id
                if cls_name is not None:
                    local_types[stmt.targets[0].id] = cls_name
        result[id(fdef)] = local_types
    return result


def _resolve_target_owner(expr: ast.expr, owner_cls: str | None, local_types: dict[str, str]) -> str | None:
    if isinstance(expr, ast.Name):
        if expr.id == 'self':
            return owner_cls
        return local_types.get(expr.id)
    if isinstance(expr, ast.Call) and isinstance(expr.func, ast.Name) and expr.func.id == 'cast' and expr.args and isinstance(expr.args[0], ast.Name):
        return expr.args[0].id
    return None


def _collect_primitive_attr_fields(module: Module) -> set[str]:
    """Field names that still have a primitive annotation somewhere in the module."""
    result: set[str] = set()
    for cls in module.body:
        if not isinstance(cls, ast.ClassDef):
            continue
        for stmt in ast.walk(cls):
            if (
                isinstance(stmt, ast.AnnAssign)
                and isinstance(stmt.target, ast.Attribute)
                and isinstance(stmt.target.value, ast.Name)
                and stmt.target.value.id == 'self'
                and isinstance(stmt.annotation, ast.Name)
                and stmt.annotation.id in _PRIMITIVE_NUMERIC_NAMES
            ):
                result.add(stmt.target.attr)
    return result


def _wrap_kept_primitive_assigns(fdef: ast.FunctionDef, boxed: set[str]) -> None:
    """For args/locals annotated primitive (kept), wrap reassigned boxed values with the primitive type."""
    kept_primitive: dict[str, ast.expr] = {}
    for arg in fdef.args.args:
        if arg.annotation is not None and isinstance(arg.annotation, ast.Name) and arg.annotation.id in _PRIMITIVE_NUMERIC_NAMES:
            kept_primitive[arg.arg] = arg.annotation
    for stmt in ast.walk(fdef):
        if isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name) and isinstance(stmt.annotation, ast.Name) and stmt.annotation.id in _PRIMITIVE_NUMERIC_NAMES:
            kept_primitive[stmt.target.id] = stmt.annotation
    if not kept_primitive:
        return
    for assign in ast.walk(fdef):
        if not isinstance(assign, ast.Assign):
            continue
        if len(assign.targets) != 1:
            continue
        target = assign.targets[0]
        if not (isinstance(target, ast.Name) and target.id in kept_primitive):
            continue
        if not (isinstance(assign.value, ast.Name) and assign.value.id in boxed):
            continue
        typ = kept_primitive[target.id]
        assign.value = ast.copy_location(
            ast.Call(func=ast.Name(id=typ.id, ctx=ast.Load()), args=[assign.value], keywords=[]),
            assign.value,
        )


class _StaticShapeSanitizer(ast.NodeTransformer):
    def visit_FunctionDef(self, node: ast.FunctionDef):
        primitive_ann_names = {
            stmt.target.id
            for stmt in ast.walk(node)
            if isinstance(stmt, ast.AnnAssign)
            and isinstance(stmt.target, ast.Name)
            and isinstance(stmt.annotation, ast.Name)
            and stmt.annotation.id in {'int64', 'int32', 'int16', 'int8', 'uint64', 'uint32', 'uint16', 'uint8', 'double', 'float64', 'float32', 'cbool'}
        }
        self.generic_visit(node)
        returns_int = isinstance(node.returns, ast.Name) and node.returns.id == 'int'
        for stmt in ast.walk(node):
            if returns_int and isinstance(stmt, ast.Return) and stmt.value is not None:
                if isinstance(stmt.value, (ast.Attribute, ast.UnaryOp)):
                    stmt.value = ast.copy_location(ast.Call(func=ast.Name(id='int', ctx=ast.Load()), args=[stmt.value], keywords=[]), stmt.value)
            if isinstance(stmt, ast.While) and isinstance(stmt.test, ast.Name) and stmt.test.id in primitive_ann_names:
                stmt.test = ast.copy_location(ast.Call(func=ast.Name(id='cbool', ctx=ast.Load()), args=[stmt.test], keywords=[]), stmt.test)
            if isinstance(stmt, ast.Assign) and len(stmt.targets) == 1 and isinstance(stmt.targets[0], ast.Name) and stmt.targets[0].id in primitive_ann_names:
                if isinstance(stmt.value, ast.Call) and isinstance(stmt.value.func, ast.Name) and stmt.value.func.id == 'box' and stmt.value.args:
                    stmt.value = stmt.value.args[0]
        return node

    def visit_Call(self, node: ast.Call):
        self.generic_visit(node)
        if isinstance(node.func, ast.Name) and node.func.id == 'box' and len(node.args) == 1:
            arg = node.args[0]
            if isinstance(arg, ast.Attribute) or (isinstance(arg, ast.Call) and isinstance(arg.func, ast.Name) and arg.func.id == 'cast'):
                return ast.copy_location(arg, node)
        return node


def _sanitize_static_shapes(module: Module) -> None:
    _StaticShapeSanitizer().visit(module)


def _inject_static_imports(module: Module) -> None:
    """Import cast/box from __static__ if the transformed module now needs them."""
    already: set[str] = set()
    for stmt in module.body:
        if isinstance(stmt, ast.ImportFrom) and stmt.module == '__static__':
            for alias in stmt.names:
                already.add(alias.asname or alias.name)

    needed: set[str] = set()
    for node in ast.walk(module):
        if isinstance(node, ast.Name) and node.id in ('cast', 'box') and node.id not in already:
            needed.add(node.id)

    if not needed:
        return

    insert_idx = 0
    for index, stmt in enumerate(module.body):
        if isinstance(stmt, (ast.Import, ast.ImportFrom)):
            insert_idx = index + 1

    new_import = ast.ImportFrom(
        module='__static__',
        names=[ast.alias(name=name) for name in sorted(needed)],
        level=0,
    )
    ast.fix_missing_locations(new_import)
    module.body.insert(insert_idx, new_import)


def _collect_detypers(module: Module, defs: list, plan, func_uses, method_uses) -> list[Detyper]:
    all_detypers: list[Detyper] = []
    all_detypers += generate_tasks_global_annotations(module, plan)
    all_detypers += generate_tasks_constructor_calls(module, plan)
    for fdef in defs:
        all_detypers += generate_tasks_params_definition(fdef, plan)
        all_detypers += generate_tasks_params_calls(fdef, plan, func_uses, method_uses, module)
        all_detypers += generate_tasks_body(fdef, plan)
        all_detypers += generate_tasks_return_definition(fdef, plan)
        all_detypers += generate_tasks_return_calls(fdef, plan, func_uses, method_uses)
    return all_detypers


def build_detyper_map(source: str, annotation_ids: list[str] | None = None) -> dict:
    """Build serializable per-annotation edit bundles keyed by annotation id."""
    tree = ast.parse(source)
    label_tree(tree)
    decorate_ast_with_pyright(tree, source)
    defs = all_function_defs(tree)
    plan_names = {f.name for f in defs}
    func_uses = all_function_uses(tree, plan_names)
    method_uses = all_method_uses(tree, plan_names)
    base_plan = build_plan_data(tree, defs, {})
    sites = annotation_sites_from_tree(tree, base_plan.aliases)
    if annotation_ids is None:
        annotation_ids = [str(site.id) for site in sites]
    annotation_closure = annotation_selection_closure(sites)

    bundles = {}
    for annotation_id in annotation_ids:
        selected = annotation_closure.get(int(annotation_id), {int(annotation_id)})
        guide = {item: True for item in selected}
        plan = build_plan_data(tree, defs, guide)
        detyper = reduce(lambda left, right: left + right, _collect_detypers(tree, defs, plan, func_uses, method_uses), Detyper())
        bundles[annotation_id] = [intent_to_json(intent) for intent in detyper.intentions()]
    return {'version': 1, 'annotation_ids': annotation_ids, 'bundles': bundles}


def build_detyped_program_from_map(source: str, detyper_map: dict, perm: Permutation) -> DetypedProgram:
    tree = ast.parse(source)
    label_tree(tree)
    selected_ids = [annotation_id for annotation_id, bit in zip(detyper_map['annotation_ids'], perm) if bit]
    detyper = Detyper()
    for annotation_id in selected_ids:
        for intent_data in detyper_map['bundles'][annotation_id]:
            detyper.add(intent_from_json(intent_data))
    detyper.execute(node_index(tree))
    _post_process(tree)
    _inject_static_imports(tree)
    ast.fix_missing_locations(tree)
    return DetypedProgram(perm=perm, perm_hex=perm_name(perm), source=ast.unparse(tree))


def write_detyper_map(source: str, output_path: Path, annotation_ids: list[str] | None = None) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(build_detyper_map(source, annotation_ids), indent=2), encoding='utf-8')
    return output_path


def read_detyper_map(path: Path) -> dict:
    return json.loads(path.read_text(encoding='utf-8'))


def build_detyped_program(
    source: str,
    perm: Permutation,
    fun_names: list[str],
) -> DetypedProgram:
    """Apply the pure detyping transform for one permutation."""
    tree = ast.parse(source)
    label_tree(tree)
    decorate_ast_with_pyright(tree, source)
    module = tree

    defs = all_function_defs(tree)
    plan_names = {f.name for f in defs}
    func_uses = all_function_uses(tree, plan_names)
    method_uses = all_method_uses(tree, plan_names)

    guide: GuideType | dict[int, bool]
    if all(name.isdigit() for name in fun_names):
        guide = {int(name): bit for name, bit in zip(fun_names, perm)}
    else:
        guide = dict(zip(fun_names, perm))
    plan = build_plan_data(module, defs, guide)

    detyper = reduce(lambda left, right: left + right, _collect_detypers(module, defs, plan, func_uses, method_uses), Detyper())
    detyper.execute(node_index(tree))

    _post_process(module)
    _inject_static_imports(module)
    ast.fix_missing_locations(tree)

    return DetypedProgram(
        perm=perm,
        perm_hex=perm_name(perm),
        source=ast.unparse(tree),
    )


def write_detyped_program(
    program: DetypedProgram,
    output_dir: Path,
    source_stem: str,
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    out_file = output_dir / f'{source_stem}_{program.perm_hex}.py'
    out_file.write_text(program.source, encoding='utf-8')
    return out_file
