"""Run detyping proportion experiments and write simple CSV outputs."""

from __future__ import annotations

import argparse
import csv
import math
import random
import shutil
import statistics
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from detyper.artifacts import build_source_variant, load_source_artifacts
from detyper.benchmark_harness import resolve_benchmark_path
from detyper.stabilize import (
    DEFAULT_BATCH_SIZE,
    run_until_stable,
)

OUTPUT_ROOT = Path('benchmark_results')
BENCH_STATUS = Path('bench_status.csv')
VARIANTS = ('advanced', 'shallow', 'untyped')
DEFAULT_BENCHMARKS = [
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
RAW_FIELDS = [
    'proportion',
    'proportion_index',
    'proportion_hex_id',
    'batch_number',
    'batch_index',
    'run_length',
    'stdout',
    'stderr',
]
SUMMARY_FIELDS = [
    'proportion',
    'average_runtime',
    'min_runtime',
    'max_runtime',
]


@dataclass(frozen=True)
class Experiment:
    root: Path
    files: Path


@dataclass(frozen=True)
class Artifact:
    path: Path
    proportion: float
    proportion_index: int
    proportion_hex_id: str


def timestamp() -> str:
    return datetime.now().astimezone().strftime('%Y%m%dT%H%M%S%z')


def new_experiment(output_root: Path) -> Experiment:
    root = output_root / f'experiment_{timestamp()}'
    files = root / 'files'
    files.mkdir(parents=True, exist_ok=False)
    return Experiment(root=root, files=files)


def csv_name(benchmark: str, variant: str, kind: str) -> str:
    return f'{benchmark}_{variant}_{kind}.csv'


def write_csv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def summarize(raw_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    timings_by_proportion: dict[str, list[float]] = defaultdict(list)
    for row in raw_rows:
        timings_by_proportion[str(row['proportion'])].append(float(row['run_length']))

    summary_rows: list[dict[str, object]] = []
    for proportion in sorted(timings_by_proportion, key=float):
        timings = timings_by_proportion[proportion]
        summary_rows.append({
            'proportion': proportion,
            'average_runtime': repr(statistics.fmean(timings)),
            'min_runtime': repr(min(timings)),
            'max_runtime': repr(max(timings)),
        })
    return summary_rows


def sample_variants(total: int, detyped: int, samples_per_proportion: int, rng: random.Random) -> list[tuple[bool, ...]]:
    if total == 0:
        return [tuple()]
    if detyped == 0:
        return [tuple(False for _ in range(total))]
    if detyped == total:
        return [tuple(True for _ in range(total))]

    sample_count = min(samples_per_proportion, math.comb(total, detyped))
    variants: list[tuple[bool, ...]] = []
    seen: set[tuple[bool, ...]] = set()
    while len(variants) < sample_count:
        selected = set(rng.sample(range(total), detyped))
        variant = tuple(index in selected for index in range(total))
        if variant not in seen:
            seen.add(variant)
            variants.append(variant)
    return variants


def write_variant_artifacts(
    benchmark: str,
    variant_name: str,
    experiment: Experiment,
    samples_per_proportion: int,
    rng: random.Random,
    artifact_limit: int | None,
) -> list[Artifact]:
    source_path = resolve_benchmark_path(benchmark, variant=variant_name)
    output_dir = experiment.files / benchmark / variant_name
    artifacts = load_source_artifacts(source_path, output_dir=output_dir)
    total = len(artifacts.variant_names)
    result: list[Artifact] = []

    for detyped in range(total + 1):
        proportion = 0.0 if total == 0 else detyped / total
        for proportion_index, choices in enumerate(
            sample_variants(total, detyped, samples_per_proportion, rng),
            start=1,
        ):
            if artifact_limit is not None and len(result) >= artifact_limit:
                return result
            program = build_source_variant(artifacts, choices)
            artifact_path = output_dir / f'{artifacts.source_stem}_{program.perm_hex}_k{detyped:02d}_s{proportion_index:02d}.py'
            artifact_path.parent.mkdir(parents=True, exist_ok=True)
            artifact_path.write_text(program.source, encoding='utf-8')
            result.append(Artifact(
                path=artifact_path,
                proportion=proportion,
                proportion_index=proportion_index,
                proportion_hex_id=program.perm_hex,
            ))

    return result


def write_untyped_artifact(benchmark: str, experiment: Experiment) -> list[Artifact]:
    source_path = resolve_benchmark_path(benchmark, variant='untyped')
    artifact_path = experiment.files / benchmark / 'untyped' / source_path.name
    artifact_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source_path, artifact_path)
    return [Artifact(
        path=artifact_path,
        proportion=1.0,
        proportion_index=1,
        proportion_hex_id='untyped',
    )]


def run_artifact(artifact: Artifact, rng: random.Random) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []

    stabilized = run_until_stable(artifact.path, rng)
    for index, run in enumerate(stabilized.runs):
        rows.append({
            'proportion': repr(artifact.proportion),
            'proportion_index': artifact.proportion_index,
            'proportion_hex_id': artifact.proportion_hex_id,
            'batch_number': index // DEFAULT_BATCH_SIZE + 1,
            'batch_index': index % DEFAULT_BATCH_SIZE + 1,
            'run_length': repr(run.timing),
            'stdout': run.result.stdout,
            'stderr': run.result.stderr,
        })

    return rows


def artifacts_for_variant(
    benchmark: str,
    variant_name: str,
    experiment: Experiment,
    samples_per_proportion: int,
    rng: random.Random,
    artifact_limit: int | None,
) -> list[Artifact]:
    if variant_name == 'untyped':
        return write_untyped_artifact(benchmark, experiment)
    return write_variant_artifacts(benchmark, variant_name, experiment, samples_per_proportion, rng, artifact_limit)


def run_variant(
    benchmark: str,
    variant_name: str,
    experiment: Experiment,
    samples_per_proportion: int,
    rng: random.Random,
    remaining_limit: int | None,
) -> int:
    artifacts = artifacts_for_variant(benchmark, variant_name, experiment, samples_per_proportion, rng, remaining_limit)

    print(f'{benchmark}/{variant_name}: running {len(artifacts)} artifacts', flush=True)
    raw_path = experiment.root / csv_name(benchmark, variant_name, 'raw')
    summary_path = experiment.root / csv_name(benchmark, variant_name, 'summary')
    raw_rows: list[dict[str, object]] = []
    write_csv(raw_path, RAW_FIELDS, raw_rows)
    write_csv(summary_path, SUMMARY_FIELDS, [])

    for artifact_index, artifact in enumerate(artifacts, start=1):
        print(f'  {artifact_index}/{len(artifacts)} {artifact.path.name}', flush=True)
        raw_rows.extend(run_artifact(artifact, rng))
        write_csv(raw_path, RAW_FIELDS, raw_rows)
        write_csv(summary_path, SUMMARY_FIELDS, summarize(raw_rows))

    return len(artifacts)


def run_experiment(
    benchmarks: list[str],
    output_root: Path,
    samples_per_proportion: int,
    seed: int,
    limit: int | None,
) -> Experiment:
    experiment = new_experiment(output_root)
    rng = random.Random(seed)
    remaining_limit = limit

    for benchmark in benchmarks:
        for variant_name in VARIANTS:
            if remaining_limit == 0:
                return experiment
            completed = run_variant(
                benchmark,
                variant_name,
                experiment,
                samples_per_proportion,
                rng,
                remaining_limit,
            )
            if remaining_limit is not None:
                remaining_limit -= completed

    return experiment


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Run simple detyping proportion experiments')
    parser.add_argument('benchmarks', nargs='*', help='Benchmark names. Defaults to bench_status.csv all_green rows.')
    parser.add_argument('--output-root', type=Path, default=OUTPUT_ROOT)
    parser.add_argument('--samples-per-proportion', type=int, default=1)
    parser.add_argument('--seed', type=int, default=0)
    parser.add_argument('--limit', type=int, help='Maximum number of artifacts to run across the whole experiment')
    return parser.parse_args()


def benchmarks_from_status(status_path: Path = BENCH_STATUS) -> list[str]:
    if not status_path.exists():
        return DEFAULT_BENCHMARKS

    with status_path.open('r', newline='', encoding='utf-8') as handle:
        return [
            row['benchmark']
            for row in csv.DictReader(handle)
            if row.get('category') == 'all_green'
        ]


def main() -> None:
    args = parse_args()
    benchmarks = args.benchmarks or benchmarks_from_status()
    experiment = run_experiment(
        benchmarks=benchmarks,
        output_root=args.output_root,
        samples_per_proportion=args.samples_per_proportion,
        seed=args.seed,
        limit=args.limit,
    )
    print(f'Wrote {experiment.root}', flush=True)


if __name__ == '__main__':
    main()
