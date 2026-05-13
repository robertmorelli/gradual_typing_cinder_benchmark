"""Detypable annotation site discovery.

This module gives annotation detyping a small data model separate from the
pipeline. The pipeline should ask for sites and bundles, not know how sites are
found or coupled.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from typing import Literal

from .ast_utils import all_function_defs, find_ann_assigns, label_tree
from .rules import expand_aliases, resolve_annotation

AnnotationSiteKind = Literal['param', 'return', 'body', 'field', 'constructor_param', 'inline_param', 'inline_return', 'global']


@dataclass(frozen=True)
class AnnotationSite:
    id: int
    kind: AnnotationSiteKind
    function_name: str
    typ: ast.expr | None
    param_index: int | None = None
    span: tuple[int | None, int | None, int | None, int | None] | None = None


def _span(node: ast.AST) -> tuple[int | None, int | None, int | None, int | None]:
    return getattr(node, 'detyping_span', (
        getattr(node, 'lineno', None),
        getattr(node, 'col_offset', None),
        getattr(node, 'end_lineno', None),
        getattr(node, 'end_col_offset', None),
    ))


def _has_inline(fdef: ast.FunctionDef) -> bool:
    return any(
        (isinstance(d, ast.Name) and d.id == 'inline') or
        (isinstance(d, ast.Attribute) and d.attr == 'inline')
        for d in fdef.decorator_list
    )


def annotation_sites_from_tree(module: ast.Module, aliases: dict[str, ast.expr] | None = None) -> list[AnnotationSite]:
    sites: list[AnnotationSite] = []
    for stmt in module.body:
        if isinstance(stmt, ast.AnnAssign) and stmt.annotation is not None:
            sites.append(AnnotationSite(
                id=stmt.detyping_id,
                kind='global',
                function_name='<module>',
                typ=expand_aliases(resolve_annotation(stmt.annotation), aliases),
                span=_span(stmt),
            ))

    for fdef in all_function_defs(module):
        is_dunder = fdef.name.startswith('__') and fdef.name.endswith('__')
        is_inline = _has_inline(fdef)

        if is_inline:
            for idx, arg in enumerate(fdef.args.args):
                if arg.annotation is not None:
                    sites.append(AnnotationSite(
                        id=arg.detyping_id,
                        kind='inline_param',
                        function_name=fdef.name,
                        typ=expand_aliases(resolve_annotation(arg.annotation), aliases),
                        param_index=idx,
                        span=_span(arg),
                    ))
            if fdef.returns is not None:
                sites.append(AnnotationSite(
                    id=fdef.detyping_id,
                    kind='inline_return',
                    function_name=fdef.name,
                    typ=expand_aliases(resolve_annotation(fdef.returns), aliases),
                    span=_span(fdef),
                ))
            continue

        if not is_dunder or fdef.name == '__init__':
            start_idx = 1 if fdef.name == '__init__' and fdef.args.args else 0
            for idx, arg in enumerate(fdef.args.args[start_idx:], start=start_idx):
                if arg.annotation is not None:
                    sites.append(AnnotationSite(
                        id=arg.detyping_id,
                        kind='constructor_param' if fdef.name == '__init__' else 'param',
                        function_name=fdef.name,
                        typ=expand_aliases(resolve_annotation(arg.annotation), aliases),
                        param_index=idx,
                        span=_span(arg),
                    ))

            if (not is_dunder or fdef.name == '__init__') and fdef.returns is not None:
                sites.append(AnnotationSite(
                    id=fdef.detyping_id,
                    kind='constructor_return' if fdef.name == '__init__' else 'return',
                    function_name=fdef.name,
                    typ=expand_aliases(resolve_annotation(fdef.returns), aliases),
                    span=_span(fdef),
                ))

        for ann in find_ann_assigns(fdef):
            if ann.annotation is not None:
                is_self_field = (
                    isinstance(ann.target, ast.Attribute)
                    and isinstance(ann.target.value, ast.Name)
                    and ann.target.value.id == 'self'
                )
                if is_dunder and not is_self_field:
                    continue
                sites.append(AnnotationSite(
                    id=ann.detyping_id,
                    kind='field' if is_self_field else 'body',
                    function_name=fdef.name,
                    typ=expand_aliases(resolve_annotation(ann.annotation), aliases),
                    span=_span(ann),
                ))
    return sorted(sites, key=lambda site: site.id)


def annotation_sites_from_source(source: str) -> list[AnnotationSite]:
    module = ast.parse(source)
    label_tree(module)
    return annotation_sites_from_tree(module)


def annotation_selection_closure(sites: list[AnnotationSite]) -> dict[int, set[int]]:
    """Annotation ids that must be selected together for override-shaped slots."""
    return_ids_by_name: dict[str, set[int]] = {}
    param_ids_by_name_index: dict[tuple[str, int], set[int]] = {}

    for site in sites:
        if site.kind == 'return':
            return_ids_by_name.setdefault(site.function_name, set()).add(site.id)
        elif site.kind == 'param' and site.param_index is not None:
            param_ids_by_name_index.setdefault((site.function_name, site.param_index), set()).add(site.id)

    closure: dict[int, set[int]] = {
        ret_id: ids for ids in return_ids_by_name.values() for ret_id in ids
    }
    closure.update({
        param_id: ids for ids in param_ids_by_name_index.values() for param_id in ids
    })
    return closure
