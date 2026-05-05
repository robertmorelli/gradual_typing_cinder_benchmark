"""Selected-aware context facts for detyping.

This module is the boring middle layer between policy and concrete generators.
It answers questions about ownership and selected storage without generators
having to guess from names alone.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from ast import FunctionDef, Module
from typing import Literal

from .plan_data import PlanData, TypeSpec
from .rules import classify_type


ValueShape = Literal['typed', 'boxed_dynamic', 'dynamic_unknown']


@dataclass(frozen=True)
class ExprShapeFact:
    typ: TypeSpec | None
    shape: ValueShape


@dataclass(frozen=True)
class FieldRefFact:
    owner_class: str
    field_name: str
    declared_type: TypeSpec | None
    selected_type: TypeSpec | None

    @property
    def storage_detyped(self) -> bool:
        return self.selected_type is not None


@dataclass(frozen=True)
class ConstructorCallFact:
    call: ast.Call
    class_name: str


def annotation_name(typ: ast.expr | None) -> str | None:
    if isinstance(typ, ast.Name):
        return typ.id
    if isinstance(typ, ast.Constant) and isinstance(typ.value, str):
        return typ.value
    return None


def call_return_type(expr: ast.expr, plan: PlanData) -> TypeSpec | None:
    if not isinstance(expr, ast.Call):
        return None
    if isinstance(expr.func, ast.Name):
        info = plan.funcs.get(expr.func.id)
    elif isinstance(expr.func, ast.Attribute):
        info = plan.funcs.get(expr.func.attr)
    else:
        info = None
    return info.return_type if info is not None else None


def local_class_types(func: FunctionDef, plan: PlanData) -> dict[str, str]:
    local_types: dict[str, str] = {}
    info = plan.funcs.get(func.name)
    if info is not None:
        for idx, arg in enumerate(func.args.args):
            if idx < len(info.param_types):
                name = annotation_name(info.param_types[idx])
                if name is not None:
                    local_types[arg.arg] = name
    for stmt in ast.walk(func):
        if isinstance(stmt, ast.Assign) and len(stmt.targets) == 1 and isinstance(stmt.targets[0], ast.Name):
            name = annotation_name(call_return_type(stmt.value, plan))
            if name is not None:
                local_types[stmt.targets[0].id] = name
        elif isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name):
            name = annotation_name(stmt.annotation)
            if name is not None:
                local_types[stmt.target.id] = name
    return local_types


def attr_owner_class(expr: ast.expr, *, owner_class: str | None, local_types: dict[str, str], plan: PlanData) -> str | None:
    if isinstance(expr, ast.Name):
        if expr.id == 'self':
            return owner_class
        return local_types.get(expr.id)
    if isinstance(expr, ast.Attribute):
        cls = attr_owner_class(expr.value, owner_class=owner_class, local_types=local_types, plan=plan)
        if cls is None:
            return None
        return annotation_name(plan.class_fields.get(cls, {}).get(expr.attr))
    if isinstance(expr, ast.Call) and isinstance(expr.func, ast.Name) and expr.func.id == 'cast' and expr.args:
        return annotation_name(expr.args[0])
    ret = call_return_type(expr, plan)
    if ret is not None:
        return annotation_name(ret)
    return None


def field_ref_fact(expr: ast.Attribute, *, owner_class: str | None, local_types: dict[str, str], plan: PlanData) -> FieldRefFact | None:
    cls = attr_owner_class(expr.value, owner_class=owner_class, local_types=local_types, plan=plan)
    if cls is None:
        return None
    declared = plan.class_fields.get(cls, {}).get(expr.attr)
    selected = (plan.selected_field_types or {}).get((cls, expr.attr))
    if declared is None and selected is None:
        return None
    return FieldRefFact(cls, expr.attr, declared, selected)


def field_expr_shape(expr: ast.Attribute, *, owner_class: str | None, local_types: dict[str, str], plan: PlanData) -> ExprShapeFact | None:
    fact = field_ref_fact(expr, owner_class=owner_class, local_types=local_types, plan=plan)
    if fact is None:
        return None
    typ = fact.selected_type if fact.selected_type is not None else fact.declared_type
    if typ is None:
        return None
    if fact.storage_detyped and classify_type(typ, plan.aliases) == 'primitive':
        return ExprShapeFact(typ, 'boxed_dynamic')
    return ExprShapeFact(typ, 'typed')


def primitive_field_read_type(expr: ast.Attribute, *, owner_class: str | None, local_types: dict[str, str], plan: PlanData) -> TypeSpec | None:
    fact = field_expr_shape(expr, owner_class=owner_class, local_types=local_types, plan=plan)
    if fact is None:
        return None
    return fact.typ if classify_type(fact.typ, plan.aliases) == 'primitive' else None


def constructor_call_facts(module: Module) -> list[ConstructorCallFact]:
    facts: list[ConstructorCallFact] = []
    for node in ast.walk(module):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            facts.append(ConstructorCallFact(node, node.func.id))
    return facts
