"""CLI entry point."""

import ast
import argparse
import itertools
import random
import sys
from pathlib import Path

from .plan_data import all_function_defs
from .runner import run_permutation, perm_name


def _run_one(source, perm, fun_names, output_dir, source_stem) -> dict:
    return run_permutation(source, perm, fun_names, output_dir, source_stem)


def _random_perm(n: int, k: int) -> tuple:
    """Random permutation with exactly k True values out of n."""
    indices = set(random.sample(range(n), k))
    return tuple(i in indices for i in range(n))


def _parse_stdout_time(stdout: str) -> float | None:
    """Try to parse a float from the first line of stdout."""
    try:
        return float(stdout.strip().splitlines()[0])
    except (ValueError, IndexError):
        return None


def main():
    parser = argparse.ArgumentParser(description='Detyper for Static Python benchmarks')
    parser.add_argument('benchmark_file', help='Path to .py benchmark file')
    parser.add_argument('--show-perm', metavar='HEX',
                        help='Print transformed source for a specific permutation and exit')
    parser.add_argument('--test', action='store_true',
                        help='Run fully typed and fully detyped once')
    parser.add_argument('--by-proportion', action='store_true',
                        help='Run 0%, n intermediate proportions, and 100%% detyped')
    parser.add_argument('--proportions', type=int, default=5, metavar='N',
                        help='Number of intermediate proportions (default: 5)')
    parser.add_argument('--iterations', type=int, default=3, metavar='K',
                        help='Random samples per intermediate proportion (default: 3)')
    args = parser.parse_args()

    src_path = Path(args.benchmark_file)
    if not src_path.exists():
        print(f"Error: file not found: {src_path}", file=sys.stderr)
        sys.exit(1)

    source = src_path.read_text(encoding='utf-8')
    tree = ast.parse(source)
    defs = all_function_defs(tree)
    fun_names = sorted({f.name for f in defs})
    n = len(fun_names)

    try:
        bench_idx = src_path.parts.index('Benchmark')
        rel = Path(*src_path.parts[bench_idx + 1:-1])
    except (ValueError, TypeError):
        rel = Path(src_path.parent.name)
    output_dir = Path('detyped_files') / rel
    output_dir.mkdir(parents=True, exist_ok=True)
    source_stem = src_path.stem

    # ── --show-perm ───────────────────────────────────────────────────────────
    if args.show_perm:
        target_hex = args.show_perm
        for perm in itertools.product([False, True], repeat=n):
            if perm_name(perm) == target_hex:
                result = _run_one(source, perm, fun_names, output_dir, source_stem)
                print(Path(result['file']).read_text(encoding='utf-8'))
                return
        print(f"No permutation found for hex {target_hex}", file=sys.stderr)
        sys.exit(1)

    # ── --test ────────────────────────────────────────────────────────────────
    if args.test:
        for label, perm in [
            ('fully_typed',   tuple(False for _ in range(n))),
            ('fully_detyped', tuple(True  for _ in range(n))),
        ]:
            result = _run_one(source, perm, fun_names, output_dir, source_stem)
            print(f"=== {label} ({result['perm_hex']}) ===")
            print(f"returncode: {result['returncode']}")
            if result['stdout']:
                print("stdout:", result['stdout'].rstrip())
            if result['stderr']:
                print("stderr:", result['stderr'].rstrip())
            print()
        return

    # ── --by-proportion ───────────────────────────────────────────────────────
    if args.by_proportion:
        N = args.proportions   # intermediate steps
        K = args.iterations    # samples per step

        print(f"{'proportion':>12}  {'detyped':>7}  {'samples':>7}  {'avg_time':>10}  {'min_time':>10}")
        print("-" * 58)

        def run_proportion(k_detyped: int, samples: int) -> None:
            times = []
            errors = 0
            perms_used = set()
            attempts = 0
            while len(times) + errors < samples and attempts < samples * 10:
                attempts += 1
                perm = _random_perm(n, k_detyped)
                if perm in perms_used:
                    continue
                perms_used.add(perm)
                result = _run_one(source, perm, fun_names, output_dir, source_stem)
                if result['returncode'] == 0:
                    t = _parse_stdout_time(result['stdout'])
                    if t is not None:
                        times.append(t)
                    else:
                        errors += 1
                else:
                    errors += 1

            prop = k_detyped / n if n > 0 else 0
            if times:
                avg = sum(times) / len(times)
                mn  = min(times)
                err_note = f"  ({errors} err)" if errors else ""
                print(f"{prop:>12.2f}  {k_detyped:>7}  {len(times):>7}  {avg:>10.4f}s  {mn:>10.4f}s{err_note}")
            else:
                print(f"{prop:>12.2f}  {k_detyped:>7}  {'—':>7}  {'all failed':>10}")

        # 0% — fully typed, single run
        perm0 = tuple(False for _ in range(n))
        r0 = _run_one(source, perm0, fun_names, output_dir, source_stem)
        t0 = _parse_stdout_time(r0['stdout']) if r0['returncode'] == 0 else None
        if t0 is not None:
            print(f"{0.0:>12.2f}  {0:>7}  {1:>7}  {t0:>10.4f}s  {t0:>10.4f}s")
        else:
            print(f"{0.0:>12.2f}  {0:>7}  {'—':>7}  {'failed':>10}")

        # N intermediate proportions, K samples each
        for i in range(1, N + 1):
            k_detyped = max(1, min(n - 1, round(i * n / (N + 1))))
            run_proportion(k_detyped, K)

        # 100% — fully detyped, single run
        permN = tuple(True for _ in range(n))
        rN = _run_one(source, permN, fun_names, output_dir, source_stem)
        tN = _parse_stdout_time(rN['stdout']) if rN['returncode'] == 0 else None
        if tN is not None:
            print(f"{1.0:>12.2f}  {n:>7}  {1:>7}  {tN:>10.4f}s  {tN:>10.4f}s")
        else:
            print(f"{1.0:>12.2f}  {n:>7}  {'—':>7}  {'failed':>10}")
        return

    # ── default: all permutations ─────────────────────────────────────────────
    for perm in itertools.product([False, True], repeat=n):
        result = _run_one(source, perm, fun_names, output_dir, source_stem)
        status = 'OK' if result['returncode'] == 0 else f"EXIT {result['returncode']}"
        print(f"{result['perm_hex']} {status} -> {result['file']}")


if __name__ == '__main__':
    main()
