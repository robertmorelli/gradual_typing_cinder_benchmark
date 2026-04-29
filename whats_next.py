"""Print missing run_exp_part.py commands for the current plan."""

from __future__ import annotations

import csv
from pathlib import Path

from run_experiment import OUTPUT_ROOT
from setup_experiment import PLAN_PATH
from run_exp_part import load_plan


def result_pair_complete(benchmark: str, variant: str, planned_hexes: list[str]) -> bool:
    raw = OUTPUT_ROOT / f'{benchmark}_{variant}_raw.csv'
    summary = OUTPUT_ROOT / f'{benchmark}_{variant}_summary.csv'
    if not raw.exists() or not summary.exists():
        return False

    with raw.open('r', newline='', encoding='utf-8') as handle:
        completed = {
            row['proportion_hex_id']
            for row in csv.DictReader(handle)
            if row.get('proportion_hex_id')
        }
    return completed == set(planned_hexes)


def main() -> None:
    plan = load_plan(PLAN_PATH)
    for benchmark, variants in plan.items():
        for variant, hexes in variants.items():
            if not result_pair_complete(benchmark, variant, hexes):
                print(f'python3 run_exp_part.py {benchmark} {variant}')


if __name__ == '__main__':
    main()
