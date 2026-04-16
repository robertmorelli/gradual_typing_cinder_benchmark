"""Run proportion benchmarks, stream progress, write a rich CSV, and render Markdown from it."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import random
import statistics
import sys
import time
from datetime import datetime
from pathlib import Path

from benchmark_harness import benchmark_output_dir, resolve_benchmark_path
from detyper.artifacts import SourceArtifactSet, build_source_variant, load_source_artifacts
from stabalize import (
    BOOTSTRAP_RESAMPLES,
    DEFAULT_ALPHA,
    DEFAULT_BATCH_SIZE,
    DEFAULT_MAX_ITERATIONS,
    DEFAULT_RUN_RETRIES,
    DEFAULT_TOLERANCE,
    run_benchmark_script_detailed,
)

LATEST_REPORT = Path('proportion_benchmark_report.md')
OUTPUT_DIR = Path('benchmark_results')
STATUS_FILE = Path('bench_status.md')
RNG_SEED = 0
ITERATIONS_PER_PROPORTION = 1025

CSV_FIELDNAMES = [
    'generated_at',
    'row_started_at',
    'row_finished_at',
    'row_elapsed_seconds',
    'random_seed',
    'iterations_per_proportion',
    'benchmark_base_name',
    'benchmark_variant',
    'benchmark_name',
    'source_path',
    'source_exists',
    'source_size_bytes',
    'source_sha256',
    'output_dir',
    'artifact_path',
    'artifact_exists',
    'artifact_size_bytes',
    'artifact_sha256',
    'artifact_perm_hex',
    'artifact_label',
    'total_targets',
    'variant_names_json',
    'detyped',
    'total',
    'proportion',
    'sample_index',
    'combination_count',
    'bucket_example_count',
    'example_sequence_index',
    'total_examples_planned',
    'variant_bits',
    'variant_indices_json',
    'variant_names_selected_json',
    'success',
    'error_type',
    'error_message',
    'error_json',
    'batch_size',
    'tolerance',
    'alpha',
    'max_iterations',
    'max_batches',
    'bootstrap_resamples',
    'retries',
    'expected_total_runs',
    'runs_completed_before_row',
    'runs_completed_after_row',
    'attempts_total',
    'attempts_per_sample_json',
    'retry_errors_per_sample_json',
    'returncodes_json',
    'stdout_json',
    'stderr_json',
    'sample_timings_json',
    'sample_min',
    'sample_max',
    'sample_median',
    'mean',
    'stdev',
    'total_samples',
    'batches',
    'converged',
    'ci_lower',
    'ci_upper',
    'batch_sample_counts_json',
    'batch_means_json',
    'batch_stdevs_json',
    'batch_ci_lowers_json',
    'batch_ci_uppers_json',
    'batch_converged_json',
]


def _benchmarks_from_status() -> list[str]:
    benchmarks: list[str] = []
    in_works = False
    for line in STATUS_FILE.read_text(encoding='utf-8').splitlines():
        if line in {'## Detyping works', '### All green'}:
            in_works = True
            continue
        if in_works and line.startswith('## '):
            break
        if in_works and line.startswith('### ') and line != '### All green':
            break
        if in_works and line.startswith('- '):
            benchmarks.append(line[2:].strip())
    return benchmarks


def _json_dump(value: object) -> str:
    return json.dumps(value, sort_keys=True)


def _path_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _path_size(path: Path) -> int:
    return path.stat().st_size


def _variant_count(total: int, detyped: int) -> int:
    if total == 0 or detyped == 0 or detyped == total:
        return 1
    return min(ITERATIONS_PER_PROPORTION, math.comb(total, detyped))


def _sample_variants(total: int, detyped: int, rng: random.Random) -> list[tuple[bool, ...]]:
    if total == 0:
        return [tuple()]
    if detyped == 0:
        return [tuple(False for _ in range(total))]
    if detyped == total:
        return [tuple(True for _ in range(total))]

    target = _variant_count(total, detyped)
    variants: list[tuple[bool, ...]] = []
    seen: set[tuple[bool, ...]] = set()
    while len(variants) < target:
        chosen = frozenset(rng.sample(range(total), detyped))
        variant = tuple(index in chosen for index in range(total))
        if variant in seen:
            continue
        seen.add(variant)
        variants.append(variant)
    return variants


def _artifact_path(output_dir: Path, source_stem: str, perm_hex: str, detyped: int, sample_index: int) -> Path:
    proportion_dir = output_dir / 'proportion_sweep'
    proportion_dir.mkdir(parents=True, exist_ok=True)
    return proportion_dir / f'{source_stem}_{perm_hex}_k{detyped:02d}_s{sample_index:02d}.py'


def _bootstrap_summary(data: list[float]) -> tuple[float, float, float, float]:
    if not data:
        return (0.0, 0.0, 0.0, 0.0)
    sample_mean = statistics.fmean(data)
    sample_stdev = 0.0 if len(data) < 2 else statistics.stdev(data)
    resample_means = sorted(
        statistics.fmean(random.choices(data, k=len(data)))
        for _ in range(BOOTSTRAP_RESAMPLES)
    )
    lower_index = int((DEFAULT_ALPHA / 2) * len(resample_means))
    upper_index = int((1 - DEFAULT_ALPHA / 2) * len(resample_means)) - 1
    ci_lower = resample_means[max(0, lower_index)]
    ci_upper = resample_means[min(len(resample_means) - 1, upper_index)]
    return sample_mean, sample_stdev, ci_lower, ci_upper


class ProgressTracker:
    def __init__(self, total_examples: int, batch_size: int, max_batches: int) -> None:
        self.total_examples = max(total_examples, 1)
        self.batch_size = batch_size
        self.max_batches = max_batches
        self.units_per_example = batch_size * max_batches
        self.total_units = self.total_examples * self.units_per_example
        self.last_len = 0

    def update(
        self,
        *,
        example_sequence_index: int,
        benchmark_name: str,
        detyped: int,
        total: int,
        sample_index: int,
        batch_index: int,
        run_index: int,
    ) -> None:
        units_done = (
            (example_sequence_index - 1) * self.units_per_example
            + (batch_index - 1) * self.batch_size
            + run_index
        )
        percent = 100.0 * units_done / self.total_units
        line = (
            f'overall completion: {percent:6.2f}% | '
            f'benchmark: {benchmark_name} '
            f'proportion: {detyped}/{total} '
            f'example: {sample_index}'
        )
        sys.stdout.write('\r' + line.ljust(self.last_len))
        sys.stdout.flush()
        self.last_len = max(self.last_len, len(line))

    def finish(self) -> None:
        if self.last_len:
            sys.stdout.write('\n')
            sys.stdout.flush()


def _make_base_row(
    *,
    generated_at: str,
    benchmark_base_name: str,
    benchmark_variant: str,
    benchmark_name: str,
    source_path: Path,
    output_dir: Path,
    artifact_path: Path,
    artifact_perm_hex: str,
    artifact_label: str,
    total_targets: int,
    variant_names: list[str],
    detyped: int,
    total: int,
    sample_index: int,
    combination_count: int,
    bucket_example_count: int,
    example_sequence_index: int,
    total_examples_planned: int,
    variant: tuple[bool, ...],
) -> dict[str, object]:
    selected_indices = [index for index, chosen in enumerate(variant) if chosen]
    selected_names = [variant_names[index] for index in selected_indices]
    source_exists = source_path.exists()
    artifact_exists = artifact_path.exists()
    return {
        'generated_at': generated_at,
        'row_started_at': '',
        'row_finished_at': '',
        'row_elapsed_seconds': '',
        'random_seed': RNG_SEED,
        'iterations_per_proportion': ITERATIONS_PER_PROPORTION,
        'benchmark_base_name': benchmark_base_name,
        'benchmark_variant': benchmark_variant,
        'benchmark_name': benchmark_name,
        'source_path': str(source_path),
        'source_exists': 'true' if source_exists else 'false',
        'source_size_bytes': str(_path_size(source_path)) if source_exists else '',
        'source_sha256': _path_sha256(source_path) if source_exists else '',
        'output_dir': str(output_dir),
        'artifact_path': str(artifact_path),
        'artifact_exists': 'true' if artifact_exists else 'false',
        'artifact_size_bytes': str(_path_size(artifact_path)) if artifact_exists else '',
        'artifact_sha256': _path_sha256(artifact_path) if artifact_exists else '',
        'artifact_perm_hex': artifact_perm_hex,
        'artifact_label': artifact_label,
        'total_targets': total_targets,
        'variant_names_json': _json_dump(variant_names),
        'detyped': detyped,
        'total': total,
        'proportion': repr(0.0 if total == 0 else detyped / total),
        'sample_index': sample_index,
        'combination_count': combination_count,
        'bucket_example_count': bucket_example_count,
        'example_sequence_index': example_sequence_index,
        'total_examples_planned': total_examples_planned,
        'variant_bits': ''.join('1' if chosen else '0' for chosen in variant),
        'variant_indices_json': _json_dump(selected_indices),
        'variant_names_selected_json': _json_dump(selected_names),
        'success': 'false',
        'error_type': '',
        'error_message': '',
        'error_json': '',
        'batch_size': DEFAULT_BATCH_SIZE,
        'tolerance': repr(DEFAULT_TOLERANCE),
        'alpha': repr(DEFAULT_ALPHA),
        'max_iterations': DEFAULT_MAX_ITERATIONS,
        'max_batches': DEFAULT_MAX_ITERATIONS + 1,
        'bootstrap_resamples': BOOTSTRAP_RESAMPLES,
        'retries': DEFAULT_RUN_RETRIES,
        'expected_total_runs': total_examples_planned * DEFAULT_BATCH_SIZE * (DEFAULT_MAX_ITERATIONS + 1),
        'runs_completed_before_row': (example_sequence_index - 1) * DEFAULT_BATCH_SIZE * (DEFAULT_MAX_ITERATIONS + 1),
        'runs_completed_after_row': '',
        'attempts_total': '',
        'attempts_per_sample_json': '[]',
        'retry_errors_per_sample_json': '[]',
        'returncodes_json': '[]',
        'stdout_json': '[]',
        'stderr_json': '[]',
        'sample_timings_json': '[]',
        'sample_min': '',
        'sample_max': '',
        'sample_median': '',
        'mean': '',
        'stdev': '',
        'total_samples': '',
        'batches': '',
        'converged': '',
        'ci_lower': '',
        'ci_upper': '',
        'batch_sample_counts_json': '[]',
        'batch_means_json': '[]',
        'batch_stdevs_json': '[]',
        'batch_ci_lowers_json': '[]',
        'batch_ci_uppers_json': '[]',
        'batch_converged_json': '[]',
    }


def _stabilize_artifact(
    *,
    script_path: Path,
    progress: ProgressTracker,
    example_sequence_index: int,
    benchmark_name: str,
    detyped: int,
    total: int,
    sample_index: int,
) -> dict[str, object]:
    timings: list[float] = []
    attempts_per_sample: list[int] = []
    retry_errors_per_sample: list[list[str]] = []
    returncodes: list[int] = []
    stdouts: list[str] = []
    stderrs: list[str] = []
    batch_sample_counts: list[int] = []
    batch_means: list[float] = []
    batch_stdevs: list[float] = []
    batch_ci_lowers: list[float] = []
    batch_ci_uppers: list[float] = []
    batch_converged: list[bool] = []

    for batch_index in range(1, DEFAULT_MAX_ITERATIONS + 2):
        for run_index in range(1, DEFAULT_BATCH_SIZE + 1):
            progress.update(
                example_sequence_index=example_sequence_index,
                benchmark_name=benchmark_name,
                detyped=detyped,
                total=total,
                sample_index=sample_index,
                batch_index=batch_index,
                run_index=run_index,
            )
            try:
                detailed = run_benchmark_script_detailed(script_path)
            except Exception as exc:
                return {
                    'timings': timings,
                    'attempts_per_sample': attempts_per_sample,
                    'retry_errors_per_sample': retry_errors_per_sample,
                    'returncodes': returncodes,
                    'stdouts': stdouts,
                    'stderrs': stderrs,
                    'batch_sample_counts': batch_sample_counts,
                    'batch_means': batch_means,
                    'batch_stdevs': batch_stdevs,
                    'batch_ci_lowers': batch_ci_lowers,
                    'batch_ci_uppers': batch_ci_uppers,
                    'batch_converged': batch_converged,
                    'error_type': type(exc).__name__,
                    'error_message': str(exc).strip(),
                }
            timings.append(detailed.timing)
            attempts_per_sample.append(detailed.attempts)
            retry_errors_per_sample.append(list(detailed.attempt_errors))
            returncodes.append(detailed.timed_run.result.returncode)
            stdouts.append(detailed.timed_run.result.stdout)
            stderrs.append(detailed.timed_run.result.stderr)

        mean, stdev, ci_lower, ci_upper = _bootstrap_summary(timings)
        margin = abs(mean * DEFAULT_TOLERANCE)
        converged = (mean - margin) <= ci_lower and ci_upper <= (mean + margin)
        batch_sample_counts.append(len(timings))
        batch_means.append(mean)
        batch_stdevs.append(stdev)
        batch_ci_lowers.append(ci_lower)
        batch_ci_uppers.append(ci_upper)
        batch_converged.append(converged)
        if converged:
            break

    return {
        'timings': timings,
        'attempts_per_sample': attempts_per_sample,
        'retry_errors_per_sample': retry_errors_per_sample,
        'returncodes': returncodes,
        'stdouts': stdouts,
        'stderrs': stderrs,
        'batch_sample_counts': batch_sample_counts,
        'batch_means': batch_means,
        'batch_stdevs': batch_stdevs,
        'batch_ci_lowers': batch_ci_lowers,
        'batch_ci_uppers': batch_ci_uppers,
        'batch_converged': batch_converged,
        'error_type': '',
        'error_message': '',
    }


def _finalize_row(row: dict[str, object], details: dict[str, object], row_started_at: float) -> dict[str, object]:
    timings: list[float] = details['timings']  # type: ignore[assignment]
    row_finished_at = datetime.now().astimezone().isoformat(timespec='seconds')
    row['row_started_at'] = datetime.fromtimestamp(row_started_at).astimezone().isoformat(timespec='seconds')
    row['row_finished_at'] = row_finished_at
    row['row_elapsed_seconds'] = repr(time.time() - row_started_at)
    row['runs_completed_after_row'] = row['runs_completed_before_row'] + len(timings)
    row['attempts_total'] = sum(details['attempts_per_sample'])  # type: ignore[arg-type]
    row['attempts_per_sample_json'] = _json_dump(details['attempts_per_sample'])
    row['retry_errors_per_sample_json'] = _json_dump(details['retry_errors_per_sample'])
    row['returncodes_json'] = _json_dump(details['returncodes'])
    row['stdout_json'] = _json_dump(details['stdouts'])
    row['stderr_json'] = _json_dump(details['stderrs'])
    row['sample_timings_json'] = _json_dump(timings)
    row['batch_sample_counts_json'] = _json_dump(details['batch_sample_counts'])
    row['batch_means_json'] = _json_dump(details['batch_means'])
    row['batch_stdevs_json'] = _json_dump(details['batch_stdevs'])
    row['batch_ci_lowers_json'] = _json_dump(details['batch_ci_lowers'])
    row['batch_ci_uppers_json'] = _json_dump(details['batch_ci_uppers'])
    row['batch_converged_json'] = _json_dump(details['batch_converged'])
    row['error_type'] = details['error_type']
    row['error_message'] = details['error_message']
    row['error_json'] = _json_dump(
        {
            'type': details['error_type'],
            'message': details['error_message'],
        }
    ) if details['error_message'] else ''
    if not timings:
        return row

    mean = details['batch_means'][-1]
    stdev = details['batch_stdevs'][-1]
    ci_lower = details['batch_ci_lowers'][-1]
    ci_upper = details['batch_ci_uppers'][-1]
    converged = details['batch_converged'][-1]
    row.update(
        success='true',
        sample_min=repr(min(timings)),
        sample_max=repr(max(timings)),
        sample_median=repr(statistics.median(timings)),
        mean=repr(mean),
        stdev=repr(stdev),
        total_samples=len(timings),
        batches=len(details['batch_sample_counts']),
        converged='true' if converged else 'false',
        ci_lower=repr(ci_lower),
        ci_upper=repr(ci_upper),
    )
    if details['error_message']:
        row['success'] = 'false'
    return row


def _run_example(
    *,
    generated_at: str,
    benchmark_base_name: str,
    benchmark_variant: str,
    benchmark_name: str,
    source_path: Path,
    output_dir: Path,
    artifact_path: Path,
    artifact_perm_hex: str,
    artifact_label: str,
    total_targets: int,
    variant_names: list[str],
    detyped: int,
    total: int,
    sample_index: int,
    combination_count: int,
    bucket_example_count: int,
    example_sequence_index: int,
    total_examples_planned: int,
    variant: tuple[bool, ...],
    progress: ProgressTracker,
) -> dict[str, object]:
    row = _make_base_row(
        generated_at=generated_at,
        benchmark_base_name=benchmark_base_name,
        benchmark_variant=benchmark_variant,
        benchmark_name=benchmark_name,
        source_path=source_path,
        output_dir=output_dir,
        artifact_path=artifact_path,
        artifact_perm_hex=artifact_perm_hex,
        artifact_label=artifact_label,
        total_targets=total_targets,
        variant_names=variant_names,
        detyped=detyped,
        total=total,
        sample_index=sample_index,
        combination_count=combination_count,
        bucket_example_count=bucket_example_count,
        example_sequence_index=example_sequence_index,
        total_examples_planned=total_examples_planned,
        variant=variant,
    )
    row_started_at = time.time()
    details = _stabilize_artifact(
        script_path=artifact_path,
        progress=progress,
        example_sequence_index=example_sequence_index,
        benchmark_name=benchmark_name,
        detyped=detyped,
        total=total,
        sample_index=sample_index,
    )
    return _finalize_row(row, details, row_started_at)


def _plan_total_examples(benchmarks: list[str]) -> int:
    total_examples = 0
    for name in benchmarks:
        for variant in ('advanced', 'shallow'):
            source_path = resolve_benchmark_path(name, variant=variant)
            total_targets = len(load_source_artifacts(source_path).variant_names)
            total_examples += sum(_variant_count(total_targets, detyped) for detyped in range(total_targets + 1))
        total_examples += 1
    return total_examples


def _run_benchmark(
    name: str,
    rng: random.Random,
    generated_at: str,
    progress: ProgressTracker,
    total_examples_planned: int,
    example_counter: int,
) -> tuple[list[dict[str, object]], int]:
    rows: list[dict[str, object]] = []

    for variant_name in ('advanced', 'shallow'):
        source_path = resolve_benchmark_path(name, variant=variant_name)
        output_dir = benchmark_output_dir(source_path)
        artifacts = load_source_artifacts(source_path, output_dir=output_dir)
        total_targets = len(artifacts.variant_names)
        for detyped in range(total_targets + 1):
            bucket_example_count = _variant_count(total_targets, detyped)
            combination_count = math.comb(total_targets, detyped) if total_targets else 1
            for sample_index, variant in enumerate(_sample_variants(total_targets, detyped, rng), start=1):
                program = build_source_variant(artifacts, variant)
                artifact_label = f'k{detyped:02d}_s{sample_index:02d}'
                artifact_path = _artifact_path(output_dir, artifacts.source_stem, program.perm_hex, detyped, sample_index)
                artifact_path.write_text(program.source, encoding='utf-8')
                rows.append(
                    _run_example(
                        generated_at=generated_at,
                        benchmark_base_name=name,
                        benchmark_variant=variant_name,
                        benchmark_name=f'{name}/{variant_name}',
                        source_path=artifacts.source_path,
                        output_dir=output_dir,
                        artifact_path=artifact_path,
                        artifact_perm_hex=program.perm_hex,
                        artifact_label=artifact_label,
                        total_targets=total_targets,
                        variant_names=artifacts.variant_names,
                        detyped=detyped,
                        total=total_targets,
                        sample_index=sample_index,
                        combination_count=combination_count,
                        bucket_example_count=bucket_example_count,
                        example_sequence_index=example_counter,
                        total_examples_planned=total_examples_planned,
                        variant=variant,
                        progress=progress,
                    )
                )
                example_counter += 1

    source_path = resolve_benchmark_path(name, variant='untyped')
    rows.append(
        _run_example(
            generated_at=generated_at,
            benchmark_base_name=name,
            benchmark_variant='untyped',
            benchmark_name=f'{name}/untyped',
            source_path=source_path,
            output_dir=source_path.parent,
            artifact_path=source_path,
            artifact_perm_hex='',
            artifact_label='untyped',
            total_targets=0,
            variant_names=[],
            detyped=0,
            total=0,
            sample_index=1,
            combination_count=1,
            bucket_example_count=1,
            example_sequence_index=example_counter,
            total_examples_planned=total_examples_planned,
            variant=tuple(),
            progress=progress,
        )
    )
    example_counter += 1
    return rows, example_counter


def write_csv(rows: list[dict[str, object]], csv_path: Path) -> None:
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


def load_csv_rows(csv_path: Path) -> list[dict[str, object]]:
    with csv_path.open('r', newline='', encoding='utf-8') as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        for key in ('random_seed', 'iterations_per_proportion', 'total_targets', 'detyped', 'total', 'sample_index'):
            row[key] = int(row[key])
        for key in ('proportion', 'mean', 'stdev', 'ci_lower', 'ci_upper'):
            row[key] = None if row[key] == '' else float(row[key])
        for key in ('batches', 'total_samples'):
            row[key] = None if row[key] == '' else int(row[key])
        row['converged'] = None if row['converged'] == '' else row['converged'] == 'true'
    return rows


def _group_rows(rows: list[dict[str, object]]) -> list[tuple[str, int, list[dict[str, object]]]]:
    grouped: dict[str, list[dict[str, object]]] = {}
    totals: dict[str, int] = {}
    order: list[str] = []
    for row in rows:
        name = row['benchmark_name']
        if name not in grouped:
            grouped[name] = []
            totals[name] = row['total_targets']
            order.append(name)
        grouped[name].append(row)
    return [(name, totals[name], grouped[name]) for name in order]


def _format_summary(rows: list[dict[str, object]]) -> str:
    lines = [
        '| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |',
        '| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |',
    ]
    buckets: dict[int, list[dict[str, object]]] = {}
    for row in rows:
        buckets.setdefault(row['detyped'], []).append(row)
    for detyped in sorted(buckets):
        bucket = buckets[detyped]
        successes = [row for row in bucket if row['mean'] is not None]
        failures = [row for row in bucket if row['error_message']]
        proportion = 0.0 if bucket[0]['total'] == 0 else detyped / bucket[0]['total']
        if successes:
            times = [row['mean'] for row in successes]
            batches = [row['batches'] for row in successes]
            converged = [row['converged'] for row in successes]
            mean_s = f'{statistics.fmean(times):.4f}s'
            min_s = f'{min(times):.4f}s'
            max_s = f'{max(times):.4f}s'
            batch_s = f'{statistics.fmean(batches):.1f}'
            converged_s = 'yes' if all(converged) else 'no'
        else:
            mean_s = min_s = max_s = batch_s = converged_s = '-'
        status = f'{len(failures)} failed' if failures else 'ok'
        lines.append(
            f'| {proportion:.2f} | {detyped}/{bucket[0]["total"]} | {len(successes)} '
            f'| {mean_s} | {min_s} | {max_s} | {batch_s} | {converged_s} | {status} |'
        )
    return '\n'.join(lines)


def _format_details(rows: list[dict[str, object]]) -> str:
    lines = [
        '| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |',
        '| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |',
    ]
    for row in rows:
        proportion = 0.0 if row['total'] == 0 else row['detyped'] / row['total']
        if row['mean'] is None:
            cells = ('-', '-', '-', '-', '-', '-', '-')
        else:
            cells = (
                f'{row["mean"]:.4f}s',
                f'{row["stdev"]:.4f}s',
                str(row['batches']),
                str(row['total_samples']),
                'yes' if row['converged'] else 'no',
                f'{row["ci_lower"]:.4f}s',
                f'{row["ci_upper"]:.4f}s',
            )
        lines.append(
            f'| {proportion:.2f} | {row["detyped"]}/{row["total"]} | {row["sample_index"]} '
            f'| {cells[0]} | {cells[1]} | {cells[2]} | {cells[3]} | {cells[4]} | {cells[5]} | {cells[6]} '
            f'| `{row["artifact_path"]}` | {row["error_message"]} |'
        )
    return '\n'.join(lines)


def render_markdown(rows: list[dict[str, object]], csv_path: Path) -> str:
    generated_at = rows[0]['generated_at'] if rows else datetime.now().astimezone().isoformat(timespec='seconds')
    iterations = rows[0]['iterations_per_proportion'] if rows else ITERATIONS_PER_PROPORTION
    seed = rows[0]['random_seed'] if rows else RNG_SEED
    lines = [
        '# Proportion Benchmark Report',
        '',
        f'- Generated: `{generated_at}`',
        f'- Source CSV: `{csv_path}`',
        f'- Benchmarks run serially: `yes`',
        f'- Iterations per detyped-count bucket: `{iterations}`',
        f'- Random seed: `{seed}`',
        '',
    ]
    for benchmark_name, total_targets, group_rows in _group_rows(rows):
        lines.extend([
            f'## {benchmark_name}',
            '',
            f'- Detypable targets: `{total_targets}`',
            f'- Total runs: `{len(group_rows)}`',
            '',
            '### Summary',
            '',
            _format_summary(group_rows),
            '',
            '### Detailed Runs',
            '',
            _format_details(group_rows),
            '',
        ])
    return '\n'.join(lines)


def write_report_from_csv(csv_path: Path, report_path: Path | None = None) -> Path:
    rows = load_csv_rows(csv_path)
    target = report_path or csv_path.with_suffix('.md')
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(render_markdown(rows, csv_path), encoding='utf-8')
    return target


def _default_csv_path(now: datetime) -> Path:
    return OUTPUT_DIR / f'proportion_benchmark_{now.strftime("%Y%m%dT%H%M%S%z")}.csv'


def main() -> None:
    parser = argparse.ArgumentParser(description='Run detyping proportion benchmarks and emit CSV + Markdown')
    parser.add_argument('--from-csv', type=Path, help='Render Markdown from an existing CSV instead of rerunning')
    parser.add_argument('--csv-out', type=Path, help='Output CSV path for a new run')
    parser.add_argument('--report-out', type=Path, help='Output Markdown path')
    args = parser.parse_args()

    if args.from_csv is not None:
        report_path = write_report_from_csv(args.from_csv, args.report_out)
        LATEST_REPORT.write_text(report_path.read_text(encoding='utf-8'), encoding='utf-8')
        print(f'Wrote {report_path}', flush=True)
        print(f'Updated {LATEST_REPORT}', flush=True)
        return

    now = datetime.now().astimezone()
    generated_at = now.isoformat(timespec='seconds')
    csv_path = args.csv_out or _default_csv_path(now)
    report_path = args.report_out or csv_path.with_suffix('.md')
    benchmarks = _benchmarks_from_status()
    total_examples_planned = _plan_total_examples(benchmarks)
    progress = ProgressTracker(
        total_examples=total_examples_planned,
        batch_size=DEFAULT_BATCH_SIZE,
        max_batches=DEFAULT_MAX_ITERATIONS + 1,
    )
    rng = random.Random(RNG_SEED)
    rows: list[dict[str, object]] = []
    example_counter = 1

    print(f'Running {len(benchmarks)} benchmarks (advanced + shallow + untyped) serially...', flush=True)
    try:
        for name in benchmarks:
            benchmark_rows, example_counter = _run_benchmark(
                name,
                rng,
                generated_at,
                progress,
                total_examples_planned,
                example_counter,
            )
            rows.extend(benchmark_rows)
            write_csv(rows, csv_path)
            latest = write_report_from_csv(csv_path, report_path)
            LATEST_REPORT.write_text(latest.read_text(encoding='utf-8'), encoding='utf-8')
    finally:
        progress.finish()

    print(f'Wrote {csv_path}', flush=True)
    print(f'Wrote {report_path}', flush=True)
    print(f'Updated {LATEST_REPORT}', flush=True)


if __name__ == '__main__':
    main()
