"""Write a simple benchmark execution plan."""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

from detyper.artifacts import load_source_artifacts
from detyper.benchmark_harness import resolve_benchmark_path
from detyper.pipeline import perm_name
from run_experiment import OUTPUT_ROOT, VARIANTS, benchmarks_from_status, sample_variants

PLAN_PATH = OUTPUT_ROOT / 'benchmark_plan.json'
RNG_SEED = 0


def plan_for_benchmark(benchmark: str, limit: int, rng: random.Random) -> dict[str, list[str]]:
    variants: dict[str, list[str]] = {}

    for variant in VARIANTS:
        if variant == 'untyped':
            variants[variant] = ['untyped']
            continue

        source_path = resolve_benchmark_path(benchmark, variant=variant)
        artifacts = load_source_artifacts(source_path)
        total = len(artifacts.variant_names)
        hexes: list[str] = []

        for detyped in range(total + 1):
            for choices in sample_variants(total, detyped, limit, rng):
                hexes.append(perm_name(choices))

        variants[variant] = hexes

    return variants


def build_plan(benchmarks: list[str], limit: int) -> dict[str, dict[str, list[str]]]:
    rng = random.Random(RNG_SEED)
    return {
        benchmark: plan_for_benchmark(benchmark, limit, rng)
        for benchmark in benchmarks
    }


def write_plan(plan: dict[str, dict[str, list[str]]], path: Path = PLAN_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(plan, indent=2, sort_keys=True) + '\n', encoding='utf-8')


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Write benchmark_results/benchmark_plan.json')
    parser.add_argument('benchmarks', nargs='*', help='Benchmark names. Defaults to bench_status.csv all_green rows.')
    parser.add_argument('--limit', type=int, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    benchmarks = args.benchmarks or benchmarks_from_status()
    plan = build_plan(benchmarks, args.limit)
    write_plan(plan)
    print(f'Wrote {PLAN_PATH}', flush=True)


if __name__ == '__main__':
    main()
