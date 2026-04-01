"""Run valid benchmarks sequentially across all detyping proportions and write Markdown."""

from __future__ import annotations

import math
import random
import statistics
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from benchmark_harness import benchmark_output_dir, resolve_benchmark_path
from detyper.artifacts import build_source_variant, load_source_artifacts
from stabalize import foo_stabilizer, run_benchmark_script

OUT_FILE = Path('proportion_benchmark_report.md')
STATUS_FILE = Path('bench_status.md')
RNG_SEED = 0
ITERATIONS_PER_PROPORTION = 10


@dataclass(frozen=True)
class ProportionRun:
    detyped: int
    total: int
    sample_index: int
    stable_time: float | None
    artifact_path: str | None
    error: str | None

    @property
    def proportion(self) -> float:
        if self.total == 0:
            return 0.0
        return self.detyped / self.total


@dataclass(frozen=True)
class BenchmarkReport:
    name: str
    total_targets: int
    runs: list[ProportionRun]


def _benchmarks_from_status() -> list[str]:
    lines = STATUS_FILE.read_text(encoding='utf-8').splitlines()
    in_works = False
    benchmarks: list[str] = []
    for line in lines:
        if line == '## Detyping works':
            in_works = True
            continue
        if in_works and line.startswith('## '):
            break
        if in_works and line.startswith('- '):
            benchmarks.append(line[2:].strip())
    return benchmarks


def _variant_for_indices(total: int, chosen: set[int]) -> tuple[bool, ...]:
    return tuple(index in chosen for index in range(total))


def _sample_variants(total: int, detyped: int, samples: int, rng: random.Random) -> list[tuple[bool, ...]]:
    if total == 0:
        return [tuple()]

    possible = math.comb(total, detyped)
    target_samples = min(samples, possible)

    if detyped == 0:
        return [tuple(False for _ in range(total))]
    if detyped == total:
        return [tuple(True for _ in range(total))]

    variants: list[tuple[bool, ...]] = []
    seen: set[tuple[bool, ...]] = set()
    while len(variants) < target_samples:
        chosen = set(rng.sample(range(total), detyped))
        variant = _variant_for_indices(total, chosen)
        if variant in seen:
            continue
        seen.add(variant)
        variants.append(variant)
    return variants


def _artifact_path(source_path: Path, detyped: int, sample_index: int) -> Path:
    output_dir = benchmark_output_dir(source_path) / 'proportion_sweep'
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir / f'{source_path.stem}_k{detyped:02d}_s{sample_index:02d}.py'


def _write_variant(source_path: Path, variant: tuple[bool, ...], detyped: int, sample_index: int) -> Path:
    artifacts = load_source_artifacts(source_path, output_dir=benchmark_output_dir(source_path))
    program = build_source_variant(artifacts, variant)
    out_path = _artifact_path(source_path, detyped, sample_index)
    out_path.write_text(program.source, encoding='utf-8')
    return out_path


def _run_variant(source_path: Path, variant: tuple[bool, ...], detyped: int, sample_index: int) -> ProportionRun:
    artifact_path = _write_variant(source_path, variant, detyped, sample_index)
    try:
        stable_time = foo_stabilizer(lambda: run_benchmark_script(artifact_path))
    except Exception as exc:  # pragma: no cover - benchmark failures are part of the report
        return ProportionRun(
            detyped=detyped,
            total=len(variant),
            sample_index=sample_index,
            stable_time=None,
            artifact_path=str(artifact_path),
            error=str(exc).strip(),
        )
    return ProportionRun(
        detyped=detyped,
        total=len(variant),
        sample_index=sample_index,
        stable_time=stable_time,
        artifact_path=str(artifact_path),
        error=None,
    )


def run_benchmark(name: str, rng: random.Random) -> BenchmarkReport:
    source_path = resolve_benchmark_path(name)
    artifacts = load_source_artifacts(source_path)
    total_targets = len(artifacts.variant_names)
    runs: list[ProportionRun] = []

    for detyped in range(total_targets + 1):
        variants = _sample_variants(total_targets, detyped, ITERATIONS_PER_PROPORTION, rng)
        for sample_index, variant in enumerate(variants, start=1):
            runs.append(_run_variant(source_path, variant, detyped, sample_index))

    return BenchmarkReport(name=name, total_targets=total_targets, runs=runs)


def _summarize_runs(runs: list[ProportionRun]) -> str:
    lines = [
        '| proportion | detyped | samples | mean stable time | min | max | status |',
        '| --- | ---: | ---: | ---: | ---: | ---: | --- |',
    ]
    by_detyped: dict[int, list[ProportionRun]] = {}
    for run in runs:
        by_detyped.setdefault(run.detyped, []).append(run)

    for detyped in sorted(by_detyped):
        group = by_detyped[detyped]
        failures = [run for run in group if run.error]
        successes = [run.stable_time for run in group if run.stable_time is not None]
        proportion = group[0].proportion
        if successes:
            mean = statistics.fmean(successes)
            low = min(successes)
            high = max(successes)
            timing = f'{mean:.4f}s'
            low_s = f'{low:.4f}s'
            high_s = f'{high:.4f}s'
        else:
            timing = low_s = high_s = '-'
        if failures:
            status = f'{len(failures)} failed'
        else:
            status = 'ok'
        lines.append(
            f'| {proportion:.2f} | {detyped}/{group[0].total} | {len(group)} | {timing} | {low_s} | {high_s} | {status} |'
        )

    return '\n'.join(lines)


def _details_runs(runs: list[ProportionRun]) -> str:
    lines = [
        '| proportion | detyped | sample | stable time | artifact | notes |',
        '| --- | ---: | ---: | ---: | --- | --- |',
    ]
    for run in runs:
        stable = '-' if run.stable_time is None else f'{run.stable_time:.4f}s'
        notes = run.error or ''
        artifact = run.artifact_path or ''
        lines.append(
            f'| {run.proportion:.2f} | {run.detyped}/{run.total} | {run.sample_index} | {stable} | `{artifact}` | {notes} |'
        )
    return '\n'.join(lines)


def render_markdown(reports: list[BenchmarkReport]) -> str:
    timestamp = datetime.now().astimezone().isoformat(timespec='seconds')
    lines = [
        '# Proportion Benchmark Report',
        '',
        f'- Generated: `{timestamp}`',
        f'- Benchmarks run serially: `yes`',
        f'- Iterations per detyped-count bucket: `{ITERATIONS_PER_PROPORTION}`',
        f'- Random seed: `{RNG_SEED}`',
        '',
    ]
    for report in reports:
        lines.append(f'## {report.name}')
        lines.append('')
        lines.append(f'- Detypable targets: `{report.total_targets}`')
        lines.append(f'- Total runs: `{len(report.runs)}`')
        lines.append('')
        lines.append('### Summary')
        lines.append('')
        lines.append(_summarize_runs(report.runs))
        lines.append('')
        lines.append('### Detailed Runs')
        lines.append('')
        lines.append(_details_runs(report.runs))
        lines.append('')
    return '\n'.join(lines)


def main() -> None:
    rng = random.Random(RNG_SEED)
    reports: list[BenchmarkReport] = []
    benchmarks = _benchmarks_from_status()

    print(f'Running {len(benchmarks)} valid benchmarks serially...', flush=True)
    for index, name in enumerate(benchmarks, start=1):
        print(f'[{index}/{len(benchmarks)}] {name}', flush=True)
        reports.append(run_benchmark(name, rng))
        OUT_FILE.write_text(render_markdown(reports), encoding='utf-8')

    print(f'Wrote {OUT_FILE}', flush=True)


if __name__ == '__main__':
    main()
