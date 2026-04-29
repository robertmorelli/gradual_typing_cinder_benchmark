"""Run one benchmark/variant from benchmark_results/benchmark_plan.json."""

from __future__ import annotations

import argparse
import csv
import json
import random
import shutil
from collections import defaultdict
from pathlib import Path
from tempfile import TemporaryDirectory

from detyper.artifacts import build_source_variant, load_source_artifacts
from detyper.benchmark_harness import resolve_benchmark_path
from detyper.stabilize import DEFAULT_BATCH_SIZE, run_until_stable
from make_detyped_file import VARIANTS, perm_from_hex
from run_experiment import OUTPUT_ROOT, RAW_FIELDS, SUMMARY_FIELDS, summarize
from setup_experiment import PLAN_PATH

RNG_SEED = 0
TYPECHECK_PATH = OUTPUT_ROOT / 'typecheck.json'


def csv_name(benchmark: str, variant: str, kind: str) -> str:
    return f'{benchmark}_{variant}_{kind}.csv'


def write_csv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def load_plan(path: Path = PLAN_PATH) -> dict[str, dict[str, list[str]]]:
    if not path.exists():
        raise SystemExit(f'Missing plan: {path}')
    return json.loads(path.read_text(encoding='utf-8'))


def load_typecheck(path: Path = TYPECHECK_PATH) -> dict[str, dict[str, dict[str, bool]]]:
    if not path.exists():
        raise SystemExit(f'Missing typecheck results: {path}')
    return json.loads(path.read_text(encoding='utf-8'))


def planned_hexes(benchmark: str, variant: str, plan: dict[str, dict[str, list[str]]]) -> list[str]:
    try:
        return plan[benchmark][variant]
    except KeyError:
        raise SystemExit(f'Plan has no entry for {benchmark}/{variant}')


def require_typechecked(benchmark: str, variant: str, hexes: list[str]) -> None:
    typecheck = load_typecheck()
    try:
        variant_results = typecheck[benchmark][variant]
    except KeyError:
        raise SystemExit(f'Typecheck results have no entry for {benchmark}/{variant}')

    missing = [hex_id for hex_id in hexes if hex_id not in variant_results]
    failed = [hex_id for hex_id in hexes if variant_results.get(hex_id) is False]
    if missing or failed:
        messages = []
        if missing:
            messages.append(f'missing: {", ".join(missing[:10])}')
        if failed:
            messages.append(f'failed: {", ".join(failed[:10])}')
        raise SystemExit(f'Typecheck incomplete for {benchmark}/{variant} ({"; ".join(messages)})')


def write_artifact(benchmark: str, variant: str, hex_id: str, output_dir: Path) -> Path:
    source_path = resolve_benchmark_path(benchmark, variant=variant)
    if variant == 'untyped':
        artifact_path = output_dir / source_path.name
        artifact_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source_path, artifact_path)
        return artifact_path

    artifacts = load_source_artifacts(source_path, output_dir=output_dir)
    perm = perm_from_hex(hex_id, len(artifacts.variant_names))
    program = build_source_variant(artifacts, perm)
    artifact_path = output_dir / f'{artifacts.source_stem}_{hex_id}.py'
    artifact_path.parent.mkdir(parents=True, exist_ok=True)
    artifact_path.write_text(program.source, encoding='utf-8')
    return artifact_path


def run_artifact(
    artifact_path: Path,
    proportion: float,
    proportion_index: int,
    hex_id: str,
    rng: random.Random,
    skip_typecheck: bool,
) -> list[dict[str, object]]:
    stabilized = run_until_stable(artifact_path, rng, skip_typecheck=skip_typecheck)
    rows: list[dict[str, object]] = []

    for index, run in enumerate(stabilized.runs):
        rows.append({
            'proportion': repr(proportion),
            'proportion_index': proportion_index,
            'proportion_hex_id': hex_id,
            'batch_number': index // DEFAULT_BATCH_SIZE + 1,
            'batch_index': index % DEFAULT_BATCH_SIZE + 1,
            'run_length': repr(run.timing),
            'stdout': run.result.stdout,
            'stderr': run.result.stderr,
        })

    return rows


def run_part(benchmark: str, variant: str) -> None:
    plan = load_plan()
    hexes = planned_hexes(benchmark, variant, plan)
    require_typechecked(benchmark, variant, hexes)
    raw_path = OUTPUT_ROOT / csv_name(benchmark, variant, 'raw')
    summary_path = OUTPUT_ROOT / csv_name(benchmark, variant, 'summary')
    raw_rows: list[dict[str, object]] = []
    rng = random.Random(RNG_SEED)

    write_csv(raw_path, RAW_FIELDS, raw_rows)
    write_csv(summary_path, SUMMARY_FIELDS, [])

    with TemporaryDirectory(prefix='.run-exp-part-', dir=Path.cwd()) as tmp:
        output_dir = Path(tmp).relative_to(Path.cwd()) / benchmark / variant
        total_detypable = 0
        proportion_indexes: dict[float, int] = defaultdict(int)
        if variant != 'untyped':
            source_path = resolve_benchmark_path(benchmark, variant=variant)
            total_detypable = len(load_source_artifacts(source_path).variant_names)

        for index, hex_id in enumerate(hexes, start=1):
            print(f'{benchmark}/{variant}: {index}/{len(hexes)} {hex_id}', flush=True)
            artifact_path = write_artifact(benchmark, variant, hex_id, output_dir)
            if variant == 'untyped':
                proportion = 1.0
            else:
                proportion = sum(perm_from_hex(hex_id, total_detypable)) / total_detypable if total_detypable else 0.0
            proportion_indexes[proportion] += 1
            raw_rows.extend(run_artifact(
                artifact_path,
                proportion=proportion,
                proportion_index=proportion_indexes[proportion],
                hex_id=hex_id,
                rng=rng,
                skip_typecheck=True,
            ))
            write_csv(raw_path, RAW_FIELDS, raw_rows)
            write_csv(summary_path, SUMMARY_FIELDS, summarize(raw_rows))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Run one benchmark/variant from benchmark_plan.json')
    parser.add_argument('benchmark')
    parser.add_argument('variant', choices=VARIANTS)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    run_part(args.benchmark, args.variant)


if __name__ == '__main__':
    main()
