"""Typecheck every artifact in benchmark_results/benchmark_plan.json."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from tempfile import TemporaryDirectory

from detyper.artifact_runner import run_typecheck_python_artifact
from run_exp_part import load_plan, write_artifact
from setup_experiment import PLAN_PATH

TYPECHECK_PATH = Path('benchmark_results/typecheck.json')


def load_typecheck(path: Path = TYPECHECK_PATH) -> dict[str, dict[str, dict[str, bool]]]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding='utf-8'))


def write_typecheck(results: dict[str, dict[str, dict[str, bool]]], path: Path = TYPECHECK_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(results, indent=2, sort_keys=True) + '\n', encoding='utf-8')


def ensure_slot(
    results: dict[str, dict[str, dict[str, bool]]],
    benchmark: str,
    variant: str,
) -> dict[str, bool]:
    return results.setdefault(benchmark, {}).setdefault(variant, {})


def typecheck_plan() -> None:
    plan = load_plan(PLAN_PATH)
    results = load_typecheck()

    with TemporaryDirectory(prefix='.typecheck-exp-', dir=Path.cwd()) as tmp:
        tmp_root = Path(tmp).relative_to(Path.cwd())
        for benchmark, variants in plan.items():
            for variant, hexes in variants.items():
                variant_results = ensure_slot(results, benchmark, variant)
                output_dir = tmp_root / benchmark / variant

                for index, hex_id in enumerate(hexes, start=1):
                    if variant_results.get(hex_id) is True:
                        continue

                    print(f'{benchmark}/{variant}: {index}/{len(hexes)} {hex_id}', flush=True)
                    if variant == 'untyped':
                        variant_results[hex_id] = True
                        write_typecheck(results)
                        continue

                    artifact_path = write_artifact(benchmark, variant, hex_id, output_dir)
                    try:
                        run_typecheck_python_artifact(artifact_path)
                    except Exception as exc:
                        print(f'  failed: {exc}', flush=True)
                        variant_results[hex_id] = False
                    else:
                        variant_results[hex_id] = True
                    write_typecheck(results)


def parse_args() -> argparse.Namespace:
    return argparse.ArgumentParser(description='Write benchmark_results/typecheck.json').parse_args()


def main() -> None:
    parse_args()
    typecheck_plan()
    print(f'Wrote {TYPECHECK_PATH}', flush=True)


if __name__ == '__main__':
    main()
