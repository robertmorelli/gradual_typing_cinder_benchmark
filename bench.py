"""Benchmark prepared files or detyper-produced variants with stabilization."""

from __future__ import annotations

import argparse
import random
from pathlib import Path

from benchmark_harness import benchmark_output_dir, resolve_benchmark_path
from detyper.artifacts import build_source_variant, load_source_artifacts
from stabalize import foo_stabilizer, run_benchmark_script


DEFAULT_BENCHMARK = 'nbody'


def _random_variant(n: int, k: int) -> tuple[bool, ...]:
    indices = set(random.sample(range(n), k))
    return tuple(index in indices for index in range(n))


def _resolve_target_path(target: str) -> Path:
    candidate = Path(target)
    if candidate.exists():
        return candidate
    return resolve_benchmark_path(target)


def benchmark_file(script_path: Path) -> float:
    return foo_stabilizer(lambda: run_benchmark_script(script_path)).mean


def _write_variant(source_path: Path, variant: tuple[bool, ...], label: str) -> Path:
    output_dir = benchmark_output_dir(source_path)
    artifacts = load_source_artifacts(source_path, output_dir=output_dir)
    program = build_source_variant(artifacts, variant)
    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / f'{artifacts.source_stem}_{label}.py'
    out_path.write_text(program.source, encoding='utf-8')
    return out_path


def _print_benchmark_result(script_path: Path) -> None:
    stable_mean = benchmark_file(script_path)
    print(f'{script_path.name}: {stable_mean:.4f}')


def _print_by_proportion_row(source_path: Path, proportion: float, variant: tuple[bool, ...]) -> None:
    label = f'prop_{sum(variant)}'
    artifact_path = _write_variant(source_path, variant, label)
    stable_mean = benchmark_file(artifact_path)
    print(f'{proportion:>12.2f}  {sum(variant):>7}  {stable_mean:>10.4f}s')


def _run_by_proportion(source_path: Path, proportions: int, iterations: int) -> None:
    artifacts = load_source_artifacts(source_path)
    n = len(artifacts.variant_names)

    print(f'{"proportion":>12}  {"detyped":>7}  {"stable_time":>10}')
    print('-' * 36)

    zero_variant = tuple(False for _ in range(n))
    _print_by_proportion_row(source_path, 0.0, zero_variant)

    seen: set[tuple[bool, ...]] = {zero_variant}
    for step in range(1, proportions):
        k_detyped = max(1, min(n - 1, round(step * n / proportions)))
        samples = 0
        attempts = 0
        while samples < iterations and attempts < iterations * 10:
            attempts += 1
            variant = _random_variant(n, k_detyped)
            if variant in seen:
                continue
            seen.add(variant)
            _print_by_proportion_row(source_path, k_detyped / n if n else 0.0, variant)
            samples += 1

    full_variant = tuple(True for _ in range(n))
    _print_by_proportion_row(source_path, 1.0, full_variant)


def main() -> None:
    parser = argparse.ArgumentParser(description='Benchmark Python scripts with stabilization')
    parser.add_argument(
        'targets',
        nargs='*',
        default=[DEFAULT_BENCHMARK],
        help='Prepared files to benchmark, or benchmark names/source paths for --by-proportion',
    )
    parser.add_argument(
        '--by-proportion',
        action='store_true',
        help='Use the detyper to generate typed/intermediate/detyped variants and benchmark each one',
    )
    parser.add_argument('--proportions', type=int, default=5, metavar='N')
    parser.add_argument('--iterations', type=int, default=3, metavar='K')
    args = parser.parse_args()

    if args.by_proportion:
        if len(args.targets) != 1:
            raise SystemExit('--by-proportion expects exactly one benchmark name or source path')
        source_path = _resolve_target_path(args.targets[0])
        _run_by_proportion(source_path, args.proportions, args.iterations)
        return

    for target in args.targets:
        _print_benchmark_result(_resolve_target_path(target))


if __name__ == '__main__':
    main()
