from __future__ import annotations

import argparse
import csv
import random
import subprocess
from collections import defaultdict
from pathlib import Path

from detyper.ast_data import build_ast_data
from detyper.bundle_builder import build_detyper_map_from_ast_data
from detyper.pipeline import build_detyped_program_from_ast_data
from detyper.kind_context_policy import POLICY

PYTHON = Path('cinder_env/bin/python')
SAMPLES_PER_CELL = 3
SEED = 1729
ALL_KINDS = [
    'cinder_scalar', 'cinder_checked_container', 'cinder_static_container',
    'python_scalar', 'python_container', 'python_user_object', 'int_enum',
    'none_only', 'optional', 'union', 'callable', 'type_alias', 'dynamic_unknown',
]


def run_cmd(args: list[str], timeout_s: int) -> tuple[bool, str, int]:
    try:
        proc = subprocess.run(args, capture_output=True, text=True, timeout=timeout_s)
        text = (proc.stdout + proc.stderr).strip().replace('\n', ' | ')
        return proc.returncode == 0, text[-500:], proc.returncode
    except subprocess.TimeoutExpired as e:
        text = ((e.stdout or b'') + (e.stderr or b''))
        if isinstance(text, bytes):
            text = text.decode(errors='replace')
        return False, ('TIMEOUT: ' + text.strip().replace('\n', ' | '))[-500:], 124


def perm_for(annotation_ids: list[str], selected_id: str) -> tuple[bool, ...]:
    return tuple(item == selected_id for item in annotation_ids)


def run_runtime_matrix(source: Path, out_dir: Path, runtime_timeout: int = 10) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    csv_out = out_dir / 'runtime_matrix.csv'
    ast_data = build_ast_data(source.read_text(encoding='utf-8'))
    detyper_map = build_detyper_map_from_ast_data(ast_data)
    annotation_ids = [str(item) for item in detyper_map['annotation_ids']]
    annotations = ast_data.indexes['annotations']

    by_pair: dict[tuple[str, str], list[str]] = defaultdict(list)
    for annotation_id in annotation_ids:
        rec = annotations.get(annotation_id)
        if rec is not None:
            by_pair[(rec['context'], rec['type_kind'])].append(annotation_id)

    rng = random.Random(SEED)
    rows = []
    for context, kind in [(context, kind) for context in sorted(POLICY) for kind in ALL_KINDS]:
        ids = by_pair.get((context, kind), [])
        if not ids:
            rows.append({'context': context, 'type_kind': kind, 'available': 0, 'sampled': 0, 'typecheck_ok': 0, 'runtime_ok': 0, 'removed': 0, 'success': 0, 'status': 'N/A', 'details': ''})
            continue
        samples = list(ids)
        rng.shuffle(samples)
        samples = samples[:SAMPLES_PER_CELL]
        typecheck_count = runtime_count = removed_count = success_count = 0
        details = []
        for annotation_id in samples:
            program = build_detyped_program_from_ast_data(ast_data, detyper_map, perm_for(annotation_ids, annotation_id))
            safe = ''.join(ch if ch.isalnum() or ch in '._-' else '_' for ch in f'{source.parent.name}_{context}_{kind}_{annotation_id}.py')
            out_path = out_dir / safe
            out_path.write_text(program.source, encoding='utf-8')
            tc_ok, tc_msg, _ = run_cmd([str(PYTHON), '--typecheck-only', str(out_path)], timeout_s=30)
            rt_ok = False
            rt_msg = ''
            if tc_ok:
                rt_ok, rt_msg, _ = run_cmd([str(PYTHON), str(out_path)], timeout_s=runtime_timeout)
            else:
                rt_msg = 'SKIPPED_RUNTIME_TYPECHECK_FAIL'
            removed = any(intent.get('kind') == 'remove_annotation' for intent in detyper_map.get('bundles', {}).get(str(annotation_id), []))
            success = tc_ok and rt_ok and removed
            typecheck_count += int(tc_ok)
            runtime_count += int(rt_ok)
            removed_count += int(removed)
            success_count += int(success)
            msg = rt_msg if not rt_ok else rt_msg[:120]
            if not tc_ok:
                msg = tc_msg
            details.append(f'{annotation_id}:tc={"OK" if tc_ok else "FAIL"}:run={"OK" if rt_ok else "FAIL"}:removed={"YES" if removed else "NO"}:{msg}')
        status = 'OK' if success_count == len(samples) else 'FAIL' if success_count == 0 else 'PARTIAL'
        rows.append({'context': context, 'type_kind': kind, 'available': len(ids), 'sampled': len(samples), 'typecheck_ok': typecheck_count, 'runtime_ok': runtime_count, 'removed': removed_count, 'success': success_count, 'status': status, 'details': ' || '.join(details)})

    with csv_out.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['context', 'type_kind', 'available', 'sampled', 'typecheck_ok', 'runtime_ok', 'removed', 'success', 'status', 'details'])
        writer.writeheader(); writer.writerows(rows)
    for row in rows:
        if row['status'] != 'N/A':
            print(f"{row['context']:48} {row['type_kind']:22} {row['status']} success={row['success']}/{row['sampled']} tc={row['typecheck_ok']}/{row['sampled']} run={row['runtime_ok']}/{row['sampled']} of {row['available']}")
    print(csv_out)
    return csv_out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('benchmark', nargs='?', default='deltablue')
    parser.add_argument('variant', nargs='?', default='advanced')
    parser.add_argument('--timeout', type=int, default=10)
    args = parser.parse_args()
    source = Path('static-python-perf/Benchmark') / args.benchmark / args.variant / 'main.py'
    out_dir = Path('benchmark_results') / 'runtime_kind_context_matrices' / args.benchmark / args.variant
    run_runtime_matrix(source, out_dir, runtime_timeout=args.timeout)


if __name__ == '__main__':
    main()
