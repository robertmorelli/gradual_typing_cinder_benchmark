"""Run proportion benchmarks, write CSV, and render Markdown from that CSV."""

from __future__ import annotations

import argparse
import csv
import math
import random
import statistics
from datetime import datetime
from pathlib import Path

from benchmark_harness import benchmark_output_dir, resolve_benchmark_path
from detyper.artifacts import build_source_variant, load_source_artifacts
from stabalize import foo_stabilizer, run_benchmark_script

LATEST_REPORT = Path('proportion_benchmark_report.md')
OUTPUT_DIR = Path('benchmark_results')
STATUS_FILE = Path('bench_status.md')
RNG_SEED = 0
ITERATIONS_PER_PROPORTION = 20
FIELDNAMES = [
    'generated_at', 'random_seed', 'iterations_per_proportion',
    'benchmark_name', 'total_targets', 'detyped', 'total', 'sample_index',
    'artifact_path', 'error', 'mean', 'stdev', 'batches', 'total_samples',
    'converged', 'ci_lower', 'ci_upper',
]


def _benchmarks_from_status() -> list[str]:
    benchmarks: list[str] = []
    in_works = False
    for line in STATUS_FILE.read_text(encoding='utf-8').splitlines():
        if line == '## Detyping works':
            in_works = True
            continue
        if in_works and line.startswith('## '):
            break
        if in_works and line.startswith('- '):
            benchmarks.append(line[2:].strip())
    return benchmarks


def _sample_variants(total: int, detyped: int, rng: random.Random) -> list[tuple[bool, ...]]:
    if total == 0:
        return [tuple()]
    if detyped == 0:
        return [tuple(False for _ in range(total))]
    if detyped == total:
        return [tuple(True for _ in range(total))]

    target = min(ITERATIONS_PER_PROPORTION, math.comb(total, detyped))
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


def _artifact_path(source_path: Path, perm_hex: str, detyped: int, sample_index: int) -> Path:
    out_dir = benchmark_output_dir(source_path) / 'proportion_sweep'
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / f'{source_path.stem}_{perm_hex}_k{detyped:02d}_s{sample_index:02d}.py'


def _write_variant(source_path: Path, variant: tuple[bool, ...], detyped: int, sample_index: int) -> Path:
    artifacts = load_source_artifacts(source_path, output_dir=benchmark_output_dir(source_path))
    program = build_source_variant(artifacts, variant)
    out_path = _artifact_path(source_path, program.perm_hex, detyped, sample_index)
    out_path.write_text(program.source, encoding='utf-8')
    return out_path


def _base_row(
    *,
    generated_at: str,
    benchmark_name: str,
    total_targets: int,
    detyped: int,
    total: int,
    sample_index: int,
    artifact_path: Path,
) -> dict[str, object]:
    return {
        'generated_at': generated_at,
        'random_seed': RNG_SEED,
        'iterations_per_proportion': ITERATIONS_PER_PROPORTION,
        'benchmark_name': benchmark_name,
        'total_targets': total_targets,
        'detyped': detyped,
        'total': total,
        'sample_index': sample_index,
        'artifact_path': str(artifact_path),
        'error': '',
        'mean': '',
        'stdev': '',
        'batches': '',
        'total_samples': '',
        'converged': '',
        'ci_lower': '',
        'ci_upper': '',
    }


def _run_row(
    *,
    source_path: Path,
    variant: tuple[bool, ...],
    detyped: int,
    sample_index: int,
    generated_at: str,
    benchmark_name: str,
    total_targets: int,
) -> dict[str, object]:
    artifact_path = _write_variant(source_path, variant, detyped, sample_index)
    row = _base_row(
        generated_at=generated_at,
        benchmark_name=benchmark_name,
        total_targets=total_targets,
        detyped=detyped,
        total=len(variant),
        sample_index=sample_index,
        artifact_path=artifact_path,
    )
    try:
        result = foo_stabilizer(lambda: run_benchmark_script(artifact_path))
    except Exception as exc:
        row['error'] = str(exc).strip()
        return row

    row.update(
        mean=repr(result.mean),
        stdev=repr(result.stdev),
        batches=str(result.batches),
        total_samples=str(result.total_samples),
        converged='true' if result.converged else 'false',
        ci_lower=repr(result.ci_lower),
        ci_upper=repr(result.ci_upper),
    )
    return row


def _run_benchmark(name: str, rng: random.Random, generated_at: str) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []

    for variant_name in ('advanced', 'shallow'):
        benchmark_name = f'{name}/{variant_name}'
        source_path = resolve_benchmark_path(name, variant=variant_name)
        total_targets = len(load_source_artifacts(source_path).variant_names)
        for detyped in range(total_targets + 1):
            for sample_index, variant in enumerate(_sample_variants(total_targets, detyped, rng), start=1):
                rows.append(
                    _run_row(
                        source_path=source_path,
                        variant=variant,
                        detyped=detyped,
                        sample_index=sample_index,
                        generated_at=generated_at,
                        benchmark_name=benchmark_name,
                        total_targets=total_targets,
                    )
                )

    benchmark_name = f'{name}/untyped'
    source_path = resolve_benchmark_path(name, variant='untyped')
    row = _base_row(
        generated_at=generated_at,
        benchmark_name=benchmark_name,
        total_targets=0,
        detyped=0,
        total=0,
        sample_index=1,
        artifact_path=source_path,
    )
    try:
        result = foo_stabilizer(lambda: run_benchmark_script(source_path))
    except Exception as exc:
        row['error'] = str(exc).strip()
    else:
        row.update(
            mean=repr(result.mean),
            stdev=repr(result.stdev),
            batches=str(result.batches),
            total_samples=str(result.total_samples),
            converged='true' if result.converged else 'false',
            ci_lower=repr(result.ci_lower),
            ci_upper=repr(result.ci_upper),
        )
    rows.append(row)
    return rows


def write_csv(rows: list[dict[str, object]], csv_path: Path) -> None:
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


def load_csv_rows(csv_path: Path) -> list[dict[str, object]]:
    with csv_path.open('r', newline='', encoding='utf-8') as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        for key in ('random_seed', 'iterations_per_proportion', 'total_targets', 'detyped', 'total', 'sample_index'):
            row[key] = int(row[key])
        for key in ('mean', 'stdev', 'ci_lower', 'ci_upper'):
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


def _format_summary(group_rows: list[dict[str, object]]) -> str:
    lines = [
        '| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |',
        '| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |',
    ]
    buckets: dict[int, list[dict[str, object]]] = {}
    for row in group_rows:
        buckets.setdefault(row['detyped'], []).append(row)

    for detyped in sorted(buckets):
        bucket = buckets[detyped]
        ok = [row for row in bucket if row['mean'] is not None]
        failed = [row for row in bucket if row['error']]
        proportion = 0.0 if bucket[0]['total'] == 0 else detyped / bucket[0]['total']
        if ok:
            times = [row['mean'] for row in ok]
            batches = [row['batches'] for row in ok]
            converged = [row['converged'] for row in ok]
            mean_s = f'{statistics.fmean(times):.4f}s'
            min_s = f'{min(times):.4f}s'
            max_s = f'{max(times):.4f}s'
            batch_s = f'{statistics.fmean(batches):.1f}'
            converged_s = 'yes' if all(converged) else 'no'
        else:
            mean_s = min_s = max_s = batch_s = converged_s = '-'
        status = f'{len(failed)} failed' if failed else 'ok'
        lines.append(
            f'| {proportion:.2f} | {detyped}/{bucket[0]["total"]} | {len(ok)} | '
            f'{mean_s} | {min_s} | {max_s} | {batch_s} | {converged_s} | {status} |'
        )
    return '\n'.join(lines)


def _format_details(group_rows: list[dict[str, object]]) -> str:
    lines = [
        '| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |',
        '| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |',
    ]
    for row in group_rows:
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
            f'| `{row["artifact_path"]}` | {row["error"]} |'
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
    rng = random.Random(RNG_SEED)
    rows: list[dict[str, object]] = []

    benchmarks = _benchmarks_from_status()
    print(f'Running {len(benchmarks)} benchmarks (advanced + shallow + untyped) serially...', flush=True)
    for index, name in enumerate(benchmarks, start=1):
        print(f'[{index}/{len(benchmarks)}] {name}', flush=True)
        rows.extend(_run_benchmark(name, rng, generated_at))
        write_csv(rows, csv_path)
        latest = write_report_from_csv(csv_path, report_path)
        LATEST_REPORT.write_text(latest.read_text(encoding='utf-8'), encoding='utf-8')

    print(f'Wrote {csv_path}', flush=True)
    print(f'Wrote {report_path}', flush=True)
    print(f'Updated {LATEST_REPORT}', flush=True)


if __name__ == '__main__':
    main()
