from __future__ import annotations

import csv
import random
import subprocess
from pathlib import Path

# Ensure the Stage-1 facts needed by the current checked-container policy are in
# place before importing detyper modules in this process.
def ensure_stage1_fact_fixes() -> None:
    ast_path = Path('detyper/ast_data.py')
    s = ast_path.read_text()
    s = s.replace(
        """        if isinstance(ann_node, ast.AnnAssign) and ann_node.value is not None:\n            records.append(_place_record(Place.ANNOTATED_VALUE, ann_node.value.detyping_id))""",
        """        if isinstance(ann_node, ast.AnnAssign) and ann_node.value is not None:\n            annotated_value_place = Place.ANNOTATED_VALUE_LITERAL if isinstance(ann_node.value, (ast.List, ast.ListComp)) else Place.ANNOTATED_VALUE\n            records.append(_place_record(annotated_value_place, ann_node.value.detyping_id))""",
    )
    s = s.replace(
        """        for node_id in call_args_by_param_annotation.get(str(ann_id), []):\n            node_id = int(node_id)\n            if node_id in literal_arg_ids:""",
        """        for node_id in call_args_by_param_annotation.get(str(ann_id), []):\n            node_id = int(node_id)\n            call_arg_payload = {key: call_arg_uses.get(str(node_id), {}).get(key) for key in ('call_id', 'arg_index')}\n            if node_id in literal_arg_ids:""",
    )
    s = s.replace("records.append(_place_record(Place.CALL_ARGS_TO_PARAMETER_LITERAL, node_id))", "records.append(_place_record(Place.CALL_ARGS_TO_PARAMETER_LITERAL, node_id, **call_arg_payload))")
    s = s.replace("records.append(_place_record(Place.CALL_ARGS_TO_PARAMETER_FROM_CINDER_SCALAR, node_id))", "records.append(_place_record(Place.CALL_ARGS_TO_PARAMETER_FROM_CINDER_SCALAR, node_id, **call_arg_payload))")
    s = s.replace("records.append(_place_record(Place.CALL_ARGS_TO_PARAMETER_FROM_PYTHON_OBJECT, node_id))", "records.append(_place_record(Place.CALL_ARGS_TO_PARAMETER_FROM_PYTHON_OBJECT, node_id, **call_arg_payload))")
    s = s.replace("records.append(_place_record(Place.CALL_ARGS_TO_PARAMETER_VALUE, node_id))", "records.append(_place_record(Place.CALL_ARGS_TO_PARAMETER_VALUE, node_id, **call_arg_payload))")
    ast_path.write_text(s)

ensure_stage1_fact_fixes()

from detyper.ast_data import build_ast_data
from detyper.bundle_builder import build_detyper_map_from_ast_data
from detyper.pipeline import build_detyped_program_from_ast_data

BENCHMARKS = [
    'call_method',
    'call_method_slots',
    'call_simple',
    'chaos',
    'deltablue',
    'fannkuch',
    'float',
    'nbody',
    'nqueens',
    'pystone',
    'richards',
]
VARIANTS = ['advanced', 'shallow']
SAMPLES = 12
SEED = 1729
PY = Path('cinder_env/bin/python')
OUT = Path('benchmark_results/runtime_11x12_advanced_shallow')


def typecheck(path: Path) -> tuple[bool, str]:
    p = subprocess.run([str(PY), '--typecheck-only', str(path)], capture_output=True, text=True, timeout=90)
    return p.returncode == 0, (p.stdout + p.stderr).replace('\n', ' | ')[-700:]


def runtime(path: Path) -> tuple[bool, str]:
    p = subprocess.run([str(PY), '--skip-typecheck', str(path)], capture_output=True, text=True, timeout=240)
    return p.returncode == 0, (p.stdout + p.stderr).replace('\n', ' | ')[-700:]


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rng = random.Random(SEED)
    rows: list[dict[str, object]] = []

    for bench in BENCHMARKS:
        for variant in VARIANTS:
            src_path = Path('static-python-perf/Benchmark') / bench / variant / 'main.py'
            if not src_path.exists():
                print(f'MISSING {bench} {variant}')
                for i in range(SAMPLES):
                    rows.append({'benchmark': bench, 'variant': variant, 'sample': i, 'detyped': 0, 'total': 0, 'status': 'MISSING', 'msg': 'missing source', 'path': ''})
                continue

            src = src_path.read_text()
            ast_data = build_ast_data(src)
            detyper_map = build_detyper_map_from_ast_data(ast_data)
            ids = list(detyper_map['annotation_ids'])
            out_dir = OUT / bench / variant
            out_dir.mkdir(parents=True, exist_ok=True)

            for sample in range(SAMPLES):
                perm = tuple(rng.choice([False, True]) for _ in ids)
                path = out_dir / f'sample_{sample:02d}_{sum(perm)}of{len(ids)}.py'
                try:
                    program = build_detyped_program_from_ast_data(ast_data, detyper_map, perm)
                    path.write_text(program.source)
                    tc_ok, tc_msg = typecheck(path)
                    if not tc_ok:
                        status = 'TC_FILTER_FAIL'
                        msg = tc_msg
                    else:
                        rt_ok, rt_msg = runtime(path)
                        status = 'RUNTIME_PASS' if rt_ok else 'RUNTIME_FAIL'
                        msg = rt_msg
                except Exception as exc:
                    status = 'HARNESS_FAIL'
                    msg = repr(exc)

                print(f'{bench:18} {variant:8} sample={sample:02d} detyped={sum(perm)}/{len(ids)} {status} {msg[:180]}')
                rows.append({'benchmark': bench, 'variant': variant, 'sample': sample, 'detyped': sum(perm), 'total': len(ids), 'status': status, 'msg': msg, 'path': str(path)})

    summary_path = OUT / 'summary.csv'
    with summary_path.open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['benchmark', 'variant', 'sample', 'detyped', 'total', 'status', 'msg', 'path'])
        writer.writeheader()
        writer.writerows(rows)

    print('\nAGGREGATE')
    for bench in BENCHMARKS:
        for variant in VARIANTS:
            rs = [r for r in rows if r['benchmark'] == bench and r['variant'] == variant]
            passed = sum(1 for r in rs if r['status'] == 'RUNTIME_PASS')
            filtered = sum(1 for r in rs if r['status'] == 'TC_FILTER_FAIL')
            failed = sum(1 for r in rs if r['status'] == 'RUNTIME_FAIL')
            other = len(rs) - passed - filtered - failed
            print(f'{bench:18} {variant:8} runtime_pass={passed:2d}/{len(rs)} tc_filtered={filtered:2d} runtime_fail={failed:2d} other={other:2d}')
    print(summary_path)


if __name__ == '__main__':
    main()
