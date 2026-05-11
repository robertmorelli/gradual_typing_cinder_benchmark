from __future__ import annotations

import csv
import random
import subprocess
from pathlib import Path

# Stage-1 fact fixes needed by the checked-container policy. Keep this local to
# the run so this composition check uses the intended policy/fact combination.
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

from detyper.ast_data import build_ast_data
from detyper.bundle_builder import build_detyper_map_from_ast_data
from detyper.pipeline import build_detyped_program_from_ast_data

SRC = Path('static-python-perf/Benchmark/deltablue/advanced/main.py')
OUT = Path('benchmark_results/deltablue_advanced_12_random_compose')
PY = Path('cinder_env/bin/python')
SEED = 1729
SAMPLES = 12

OUT.mkdir(parents=True, exist_ok=True)
rng = random.Random(SEED)
src = SRC.read_text()
ast_data = build_ast_data(src)
detyper_map = build_detyper_map_from_ast_data(ast_data)
ids = list(detyper_map['annotation_ids'])

rows = []
for i in range(SAMPLES):
    perm = tuple(rng.choice([False, True]) for _ in ids)
    path = OUT / f'sample_{i:02d}_{sum(perm)}of{len(ids)}.py'
    program = build_detyped_program_from_ast_data(ast_data, detyper_map, perm)
    path.write_text(program.source)

    tc = subprocess.run([str(PY), '--typecheck-only', str(path)], capture_output=True, text=True, timeout=90)
    if tc.returncode != 0:
        status = 'TC_FILTER_FAIL'
        msg = (tc.stdout + tc.stderr).replace('\n', ' | ')[-700:]
    else:
        rt = subprocess.run([str(PY), '--skip-typecheck', str(path)], capture_output=True, text=True, timeout=180)
        status = 'RUNTIME_PASS' if rt.returncode == 0 else 'RUNTIME_FAIL'
        msg = (rt.stdout + rt.stderr).replace('\n', ' | ')[-700:]

    print(f'{i:02d} detyped={sum(perm)}/{len(ids)} {status} {msg}')
    rows.append({'sample': i, 'detyped': sum(perm), 'total': len(ids), 'status': status, 'msg': msg, 'path': str(path)})

with (OUT / 'summary.csv').open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['sample', 'detyped', 'total', 'status', 'msg', 'path'])
    writer.writeheader()
    writer.writerows(rows)

runtime_pass = sum(1 for r in rows if r['status'] == 'RUNTIME_PASS')
tc_filtered = sum(1 for r in rows if r['status'] == 'TC_FILTER_FAIL')
runtime_fail = sum(1 for r in rows if r['status'] == 'RUNTIME_FAIL')
print(f'SUMMARY runtime_pass={runtime_pass}/{SAMPLES} tc_filtered={tc_filtered} runtime_fail={runtime_fail}')
print(OUT / 'summary.csv')
