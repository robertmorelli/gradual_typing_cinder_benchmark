"""Print missing run_exp_part.py commands for the current plan."""

from __future__ import annotations

import csv
import json
from pathlib import Path

from run_experiment import OUTPUT_ROOT
from setup_experiment import PLAN_PATH
from run_exp_part import CHUNKS_PATH, chunk_count, load_chunks, load_plan, select_part


def completed_hexes(paths: list[Path]) -> set[str]:
    completed: set[str] = set()
    for path in paths:
        if not path.exists():
            continue
        with path.open('r', newline='', encoding='utf-8') as handle:
            completed.update(
                row['proportion_hex_id']
                for row in csv.DictReader(handle)
                if row.get('proportion_hex_id')
            )
    return completed


def raw_paths(benchmark: str, variant: str, chunks: int) -> list[Path]:
    if chunks == 1:
        return [OUTPUT_ROOT / f'{benchmark}_{variant}_raw.csv']
    return [
        OUTPUT_ROOT / f'{benchmark}_{variant}_{part}_{chunks}_raw.csv'
        for part in range(1, chunks + 1)
    ]


def result_complete(benchmark: str, variant: str, planned_hexes: list[str], chunks: int) -> bool:
    return completed_hexes(raw_paths(benchmark, variant, chunks)) == set(planned_hexes)


def main() -> None:
    plan = load_plan(PLAN_PATH)
    chunks_config = load_chunks()
    for benchmark, variants in plan.items():
        for variant, hexes in variants.items():
            chunks = chunk_count(chunks_config, benchmark, variant)
            if result_complete(benchmark, variant, hexes, chunks):
                continue
            if chunks == 1:
                print(f'python3 run_exp_part.py {benchmark} {variant}')
            else:
                for part in range(1, chunks + 1):
                    part_hexes = select_part(hexes, part, chunks, verbose=False)
                    part_paths = [OUTPUT_ROOT / f'{benchmark}_{variant}_{part}_{chunks}_raw.csv']
                    if completed_hexes(part_paths) != set(part_hexes):
                        print(f'python3 run_exp_part.py {benchmark} {variant} --part {part}')


if __name__ == '__main__':
    main()
