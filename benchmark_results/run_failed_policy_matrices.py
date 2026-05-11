from __future__ import annotations

import csv
import subprocess
from collections import defaultdict
from pathlib import Path

# Ensure Stage-1 fact fixes before importing detyper modules.
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

FAILED_VARIANTS = [
    ('call_method', 'shallow'),
    ('chaos', 'advanced'),
    ('fannkuch', 'shallow'),
    ('float', 'advanced'),
    ('nbody', 'advanced'),
    ('nqueens', 'advanced'),
    ('richards', 'advanced'),
]
PY = Path('cinder_env/bin/python')
OUT = Path('benchmark_results/failed_policy_matrices')


def is_infra_conflict(text: str) -> bool:
    return 'container name "/cinder-env-daemon" is already in use' in text or 'is not running' in text


def reset_daemon() -> None:
    subprocess.run(['bash', '-lc', 'source cinder_env/bin/activate && docker rm -f cinder-env-daemon'], capture_output=True, text=True, timeout=30)


def run_cmd(args: list[str], timeout: int) -> tuple[int, str]:
    last = ''
    for attempt in range(3):
        p = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
        text = (p.stdout + p.stderr).replace('\n', ' | ')
        last = text
        if p.returncode == 0 or not is_infra_conflict(text):
            return p.returncode, text[-1000:]
        reset_daemon()
    return 999, last[-1000:]


def safe_name(text: str) -> str:
    return ''.join(ch if ch.isalnum() or ch in '._-' else '_' for ch in text)


def perm_for(annotation_ids: list[str], selected: set[str]) -> tuple[bool, ...]:
    return tuple(str(aid) in selected for aid in annotation_ids)


def run_matrix(bench: str, variant: str) -> list[dict[str, object]]:
    src_path = Path('static-python-perf/Benchmark') / bench / variant / 'main.py'
    out_dir = OUT / bench / variant
    out_dir.mkdir(parents=True, exist_ok=True)
    src = src_path.read_text()
    ast_data = build_ast_data(src)
    detyper_map = build_detyper_map_from_ast_data(ast_data)
    annotation_ids = [str(x) for x in detyper_map['annotation_ids']]
    anns = ast_data.indexes['annotations']

    by_pair: dict[tuple[str, str], list[str]] = defaultdict(list)
    for aid in annotation_ids:
        rec = anns.get(str(aid), {})
        by_pair[(rec.get('context'), rec.get('type_kind'))].append(str(aid))

    rows: list[dict[str, object]] = []
    for idx, ((context, kind), ids) in enumerate(sorted(by_pair.items())):
        program = build_detyped_program_from_ast_data(ast_data, detyper_map, perm_for(annotation_ids, set(ids)))
        path = out_dir / safe_name(f'{idx:03d}_{context}__{kind}_{len(ids)}of{len(annotation_ids)}.py')
        path.write_text(program.source)

        tc_code, tc_msg = run_cmd([str(PY), '--typecheck-only', str(path)], timeout=90)
        if tc_code != 0:
            status = 'TC_FILTER_FAIL'
            msg = tc_msg
        else:
            rt_code, rt_msg = run_cmd([str(PY), '--skip-typecheck', str(path)], timeout=240)
            status = 'RUNTIME_PASS' if rt_code == 0 else 'RUNTIME_FAIL'
            msg = rt_msg

        row = {
            'benchmark': bench,
            'variant': variant,
            'context': context,
            'type_kind': kind,
            'count': len(ids),
            'total_annotations': len(annotation_ids),
            'status': status,
            'msg': msg,
            'path': str(path),
        }
        rows.append(row)
        print(f'{bench:10} {variant:8} {context:45} {kind:24} count={len(ids):3d} {status}')
        if status != 'RUNTIME_PASS':
            print('  ', msg[:250])

    with (out_dir / 'matrix.csv').open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['benchmark', 'variant', 'context', 'type_kind', 'count', 'total_annotations', 'status', 'msg', 'path'])
        writer.writeheader()
        writer.writerows(rows)
    return rows


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    all_rows: list[dict[str, object]] = []
    for bench, variant in FAILED_VARIANTS:
        print(f'\n=== {bench} {variant} ===')
        all_rows.extend(run_matrix(bench, variant))

    with (OUT / 'all_matrices.csv').open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['benchmark', 'variant', 'context', 'type_kind', 'count', 'total_annotations', 'status', 'msg', 'path'])
        writer.writeheader()
        writer.writerows(all_rows)

    print('\nSUMMARY failing isolated policies')
    for bench, variant in FAILED_VARIANTS:
        rows = [r for r in all_rows if r['benchmark'] == bench and r['variant'] == variant]
        bad = [r for r in rows if r['status'] != 'RUNTIME_PASS']
        print(f'{bench:18} {variant:8} bad_isolated={len(bad):2d}/{len(rows):2d}')
        for r in bad:
            print(f"  {r['status']:15} {r['context']} / {r['type_kind']} count={r['count']}")
    print(OUT / 'all_matrices.csv')


if __name__ == '__main__':
    main()
