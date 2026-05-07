"""Test detyping per-kind: only annotations of specific kind selected."""
import sys
sys.path.insert(0, '.')
import ast
import subprocess
import os
from pathlib import Path
from detyper.annotation_sites import annotation_sites_from_tree
from detyper.plan_data import build_plan_data
from detyper.ast_utils import all_function_defs, label_tree
from detyper.typecheck import decorate_ast_with_pyright
from make_detyped_file import write_detyped_file

KINDS = ['param', 'return', 'body', 'field', 'constructor_param', 'inline_return', 'global']
BENCHES = ['call_method', 'call_method_slots', 'call_simple', 'chaos', 'deltablue', 'fannkuch', 'float', 'nbody', 'nqueens', 'pystone', 'richards']


def perm_for_kind(bench, kind):
    src = open(f'static-python-perf/Benchmark/{bench}/advanced/main.py').read()
    tree = ast.parse(src)
    label_tree(tree)
    decorate_ast_with_pyright(tree, src)
    defs = all_function_defs(tree)
    plan = build_plan_data(tree, defs, {})
    sites = annotation_sites_from_tree(tree, plan.aliases)
    bits = ''.join('1' if s.kind == kind else '0' for s in sites)
    if '1' not in bits:
        return None
    return hex(int(bits, 2))


def perm_all(bench):
    src = open(f'static-python-perf/Benchmark/{bench}/advanced/main.py').read()
    tree = ast.parse(src)
    label_tree(tree)
    decorate_ast_with_pyright(tree, src)
    defs = all_function_defs(tree)
    plan = build_plan_data(tree, defs, {})
    sites = annotation_sites_from_tree(tree, plan.aliases)
    if not sites:
        return None
    return hex((1 << len(sites)) - 1)


def typecheck(b, h):
    os.makedirs(f'detyped_files/{b}/advanced', exist_ok=True)
    for f in Path(f'detyped_files/{b}/advanced').glob('detyper_map_*.json'):
        f.unlink()
    try:
        write_detyped_file(b, 'advanced', h)
    except Exception as e:
        return f'gen-err: {e}'[:60]
    p = subprocess.run(
        ['bash', '-c', f'source cinder_env/bin/activate && python --typecheck-only detyped_files/{b}/advanced/main_{h}.py 2>&1 | tail -1'],
        capture_output=True,
        text=True,
    )
    out = p.stdout.strip()
    return 'OK' if not out else out[-80:]


def main():
    results = {}
    for b in BENCHES:
        print(f'== {b}', flush=True)
        results[(b, 'all')] = typecheck(b, perm_all(b))
        for k in KINDS:
            h = perm_for_kind(b, k)
            if h is None:
                results[(b, k)] = '-'
                continue
            results[(b, k)] = typecheck(b, h)

    print()
    cols = ['all'] + KINDS
    print(f'{"":18s}', *[f'{k[:9]:9s}' for k in cols])
    for b in BENCHES:
        cells = []
        for k in cols:
            r = results[(b, k)]
            if r == 'OK':
                cells.append('OK')
            elif r == '-':
                cells.append('--')
            else:
                cells.append('FAIL')
        print(f'{b:18s}', *[f'{c:9s}' for c in cells])

    print()
    for (b, k), r in results.items():
        if r not in ('OK', '-'):
            print(f'{b}/{k}: {r}')


if __name__ == '__main__':
    main()
