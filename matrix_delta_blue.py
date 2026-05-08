"""Build context/type-kind detyping matrix for deltablue advanced.

For each context-kind square present in deltablue, try up to 3 deterministic
single-annotation detypes and typecheck the result.
"""

from __future__ import annotations

import csv
import random
import subprocess
from collections import defaultdict
from pathlib import Path

from detyper.ast_data import build_ast_data
from detyper.bundle_builder import build_detyper_map_from_ast_data
from detyper.pipeline import build_detyped_program_from_ast_data
from detyper.kind_context_policy import POLICY

SOURCE = Path('static-python-perf/Benchmark/deltablue/advanced/main.py')
OUT_DIR = Path('benchmark_results/deltablue_kind_context_matrix')
CSV_OUT = OUT_DIR / 'matrix.csv'
PYTHON = Path('cinder_env/bin/python')
SAMPLES_PER_CELL = 3
SEED = 1729


def typecheck(path: Path) -> tuple[bool, str]:
    proc = subprocess.run(
        [str(PYTHON), '--typecheck-only', str(path)],
        capture_output=True,
        text=True,
        timeout=30,
    )
    text = (proc.stdout + proc.stderr).strip().replace('\n', ' | ')
    return proc.returncode == 0, text[-300:]


def perm_for(annotation_ids: list[str], selected_id: str) -> tuple[bool, ...]:
    return tuple(item == selected_id for item in annotation_ids)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    source = SOURCE.read_text(encoding='utf-8')
    ast_data = build_ast_data(source)
    detyper_map = build_detyper_map_from_ast_data(ast_data)
    annotation_ids = [str(item) for item in detyper_map['annotation_ids']]
    annotations = ast_data.indexes['annotations']

    by_pair: dict[tuple[str, str], list[str]] = defaultdict(list)
    for annotation_id in annotation_ids:
        rec = annotations.get(str(annotation_id))
        if rec is None:
            continue
        by_pair[(rec['context'], rec['type_kind'])].append(str(annotation_id))

    rng = random.Random(SEED)
    all_kinds = [
        'cinder_scalar', 'cinder_checked_container', 'cinder_static_container',
        'python_scalar', 'python_container', 'python_user_object',
        'none_only', 'optional', 'union', 'callable', 'type_alias', 'dynamic_unknown',
    ]
    all_pairs = [(context, kind) for context in sorted(POLICY) for kind in all_kinds]

    rows = []
    for context, kind in all_pairs:
        ids = by_pair.get((context, kind), [])
        if not ids:
            rows.append({
                'context': context,
                'type_kind': kind,
                'available': 0,
                'sampled': 0,
                'typecheck_ok': 0,
                'removed': 0,
                'success': 0,
                'status': 'N/A',
                'details': '',
            })
            continue
        samples = list(ids)
        rng.shuffle(samples)
        samples = samples[:SAMPLES_PER_CELL]
        ok_count = 0
        removed_count = 0
        success_count = 0
        details = []
        for annotation_id in samples:
            program = build_detyped_program_from_ast_data(
                ast_data,
                detyper_map,
                perm_for(annotation_ids, annotation_id),
            )
            out_path = OUT_DIR / f'deltablue_{context}_{kind}_{annotation_id}.py'
            safe = ''.join(ch if ch.isalnum() or ch in '._-' else '_' for ch in out_path.name)
            out_path = OUT_DIR / safe
            out_path.write_text(program.source, encoding='utf-8')
            ok, msg = typecheck(out_path)
            bundle = detyper_map.get('bundles', {}).get(str(annotation_id), [])
            removed = any(intent.get('kind') == 'remove_annotation' for intent in bundle)
            success = ok and removed
            ok_count += int(ok)
            removed_count += int(removed)
            success_count += int(success)
            details.append(f'{annotation_id}:typecheck={"OK" if ok else "FAIL"}:removed={"YES" if removed else "NO"}:{msg}')
        status = 'N/A' if not ids else 'OK' if success_count == len(samples) else 'FAIL' if success_count == 0 else 'PARTIAL'
        rows.append({
            'context': context,
            'type_kind': kind,
            'available': len(ids),
            'sampled': len(samples),
            'typecheck_ok': ok_count,
            'removed': removed_count,
            'success': success_count,
            'status': status,
            'details': ' || '.join(details),
        })

    with CSV_OUT.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['context', 'type_kind', 'available', 'sampled', 'typecheck_ok', 'removed', 'success', 'status', 'details'])
        writer.writeheader()
        writer.writerows(rows)

    for row in rows:
        if row['status'] != 'N/A':
            print(f"{row['context']:48} {row['type_kind']:22} {row['status']} success={row['success']}/{row['sampled']} typecheck={row['typecheck_ok']}/{row['sampled']} removed={row['removed']}/{row['sampled']} of {row['available']}")
    print(CSV_OUT)


if __name__ == '__main__':
    main()
