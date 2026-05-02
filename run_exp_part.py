"""Run one benchmark/variant from benchmark_results/benchmark_plan.json."""

from __future__ import annotations

import argparse
import csv
import json
import random
import time
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

from detyper.artifacts import load_source_artifacts
from detyper.benchmark_harness import resolve_benchmark_path
from detyper.stabilize import DEFAULT_BATCH_SIZE, run_until_stable
from make_detyped_file import VARIANTS, perm_from_hex, write_detyped_file
from run_experiment import OUTPUT_ROOT, RAW_FIELDS
from setup_experiment import PLAN_PATH

CHUNKS_PATH = OUTPUT_ROOT / 'chunks.json'
ESTIMATE_PATH = OUTPUT_ROOT / 'estimate.json'

RNG_SEED = 0


def csv_name(benchmark: str, variant: str, kind: str, part: int | None = None, chunks: int | None = None) -> str:
    if part is not None and chunks is not None:
        return f'{benchmark}_{variant}_{part}_{chunks}_{kind}.csv'
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


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else {}


def load_chunks(path: Path = CHUNKS_PATH) -> dict[str, dict[str, int]]:
    return load_json(path)


def chunk_count(chunks: dict[str, dict[str, int]], benchmark: str, variant: str) -> int:
    return chunks.get(benchmark, {}).get(variant, 1)


def planned_hexes(benchmark: str, variant: str, plan: dict[str, dict[str, list[str]]]) -> list[str]:
    try:
        return plan[benchmark][variant]
    except KeyError:
        raise SystemExit(f'Plan has no entry for {benchmark}/{variant}')


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


def select_part(hexes: list[str], part: int | None, chunks: int | None, verbose: bool = True) -> list[str]:
    if part is None and chunks is None:
        return hexes
    if part is None or chunks is None:
        raise SystemExit('--part and --chunks must be used together')
    if chunks < 1:
        raise SystemExit('--chunks must be >= 1')
    if part < 1 or part > chunks:
        raise SystemExit('--part must be between 1 and --chunks')

    start = (len(hexes) * (part - 1)) // chunks
    stop = (len(hexes) * part) // chunks
    if verbose:
        print(f'part {part}/{chunks}: hexes {start + 1}-{stop} of {len(hexes)}', flush=True)
    return hexes[start:stop]


def eta_text(seconds: float) -> str:
    seconds = max(0, round(seconds))
    duration = str(timedelta(seconds=seconds))
    when = datetime.now() + timedelta(seconds=seconds)
    hour = when.hour % 12 or 12
    return f'estimate: {duration} remaining; come back {when:%A, %b} {when.day} at {hour}:{when:%M %p}'


def print_eta(seconds: float | None) -> None:
    if seconds is not None and seconds > 0:
        print(eta_text(seconds), flush=True)


def run_part(benchmark: str, variant: str, part: int | None = None) -> None:
    plan = load_plan()
    chunks_config = load_chunks()
    chunks = chunk_count(chunks_config, benchmark, variant)
    if chunks > 1 and part is None:
        raise SystemExit(f'{benchmark}/{variant} has {chunks} chunks; pass --part 1..{chunks}')
    if chunks == 1:
        part = None

    all_hexes = planned_hexes(benchmark, variant, plan)
    hexes = select_part(all_hexes, part, chunks if part is not None else None)
    raw_path = OUTPUT_ROOT / csv_name(benchmark, variant, 'raw', part, chunks if part is not None else None)
    raw_rows: list[dict[str, object]] = []
    rng = random.Random(RNG_SEED)

    write_csv(raw_path, RAW_FIELDS, raw_rows)

    total_detypable = 0
    proportion_indexes: dict[float, int] = defaultdict(int)
    if variant != 'untyped':
        source_path = resolve_benchmark_path(benchmark, variant=variant)
        total_detypable = len(load_source_artifacts(source_path).variant_names)

    seconds_per_hex = load_json(ESTIMATE_PATH).get(benchmark, {}).get(variant)
    print_eta(seconds_per_hex * len(hexes) if seconds_per_hex is not None else None)
    started_at = time.monotonic()
    for index, hex_id in enumerate(hexes, start=1):
        print(f'{benchmark}/{variant}: {index}/{len(hexes)} {hex_id}', flush=True)
        artifact_path = write_detyped_file(benchmark, variant, hex_id)
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
        if index < len(hexes):
            print_eta((time.monotonic() - started_at) / index * (len(hexes) - index))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Run one benchmark/variant from benchmark_plan.json')
    parser.add_argument('benchmark')
    parser.add_argument('variant', choices=VARIANTS)
    parser.add_argument('--part', type=int, help='1-based part number to run; total chunks comes from benchmark_results/chunks.json')
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    run_part(args.benchmark, args.variant, part=args.part)


if __name__ == '__main__':
    main()
