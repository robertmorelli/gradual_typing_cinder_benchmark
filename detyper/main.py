"""CLI entry point for preparing detyped source artifacts."""

from __future__ import annotations

import argparse
import itertools
import random
import sys
from pathlib import Path

from .artifacts import build_source_variant, load_source_artifacts, write_source_variant
from .backends import available_backends
from .core.types import perm_name


def _random_perm(n: int, k: int) -> tuple[bool, ...]:
    indices = set(random.sample(range(n), k))
    return tuple(index in indices for index in range(n))


def _perm_from_hex(target_hex: str, n: int) -> tuple[bool, ...] | None:
    try:
        value = int(target_hex, 16)
    except ValueError:
        return None

    bits = format(value, f'0{n}b') if n > 0 else ''
    if len(bits) > n:
        return None
    return tuple(bit == '1' for bit in bits)


def _resolve_output_dir(source_path: Path, output_dir: str | None) -> Path:
    if output_dir is not None:
        return Path(output_dir)
    return source_path.parent


def _show_variant(source_path: Path, variant_hex: str, backend_name: str) -> None:
    artifacts = load_source_artifacts(source_path, backend_name=backend_name)
    variant = _perm_from_hex(variant_hex, len(artifacts.variant_names))
    if variant is None:
        print(f'No variant found for hex {variant_hex}', file=sys.stderr)
        raise SystemExit(1)

    print(build_source_variant(artifacts, variant).source)


def _write_variant(
    source_path: Path,
    variant: tuple[bool, ...],
    output_dir: Path,
    backend_name: str,
) -> Path:
    artifacts = load_source_artifacts(source_path, output_dir=output_dir, backend_name=backend_name)
    program = build_source_variant(artifacts, variant)
    return write_source_variant(artifacts, program)


def _write_all_variants(source_path: Path, output_dir: Path, backend_name: str) -> None:
    artifacts = load_source_artifacts(source_path, output_dir=output_dir, backend_name=backend_name)
    for variant in itertools.product([False, True], repeat=len(artifacts.variant_names)):
        out_file = write_source_variant(artifacts, build_source_variant(artifacts, variant))
        print(out_file)


def _write_random_variants(
    source_path: Path,
    output_dir: Path,
    proportions: int,
    iterations: int,
    backend_name: str,
) -> None:
    artifacts = load_source_artifacts(source_path, output_dir=output_dir, backend_name=backend_name)
    n = len(artifacts.variant_names)

    base_variants: list[tuple[bool, ...]] = [
        tuple(False for _ in range(n)),
        tuple(True for _ in range(n)),
    ]
    seen: set[tuple[bool, ...]] = set(base_variants)

    for variant in base_variants:
        print(_write_variant(source_path, variant, output_dir, backend_name))

    for step in range(1, proportions):
        k_detyped = max(1, min(n - 1, round(step * n / proportions)))
        samples = 0
        attempts = 0
        while samples < iterations and attempts < iterations * 10:
            attempts += 1
            variant = _random_perm(n, k_detyped)
            if variant in seen:
                continue
            seen.add(variant)
            print(_write_variant(source_path, variant, output_dir, backend_name))
            samples += 1


def main() -> None:
    parser = argparse.ArgumentParser(description='Prepare detyped source variants')
    parser.add_argument('source_file', help='Path to a Python source file')
    parser.add_argument('--show-perm', metavar='HEX', help='Print a specific variant and exit')
    parser.add_argument('--write-perm', metavar='HEX', help='Write a specific variant and print its path')
    parser.add_argument('--write-all', action='store_true', help='Write every variant and print each path')
    parser.add_argument(
        '--write-by-proportion',
        action='store_true',
        help='Write 0%%, sampled intermediate variants, and 100%% variants',
    )
    parser.add_argument('--proportions', type=int, default=5, metavar='N')
    parser.add_argument('--iterations', type=int, default=3, metavar='K')
    parser.add_argument('--output-dir', help='Directory for written variants')
    parser.add_argument(
        '--backend',
        default='cinder',
        choices=available_backends(),
        help='Detyper backend/runtime policy set',
    )
    args = parser.parse_args()

    source_path = Path(args.source_file)
    output_dir = _resolve_output_dir(source_path, args.output_dir)

    if args.show_perm:
        _show_variant(source_path, args.show_perm, args.backend)
        return
    if args.write_perm:
        variant = _perm_from_hex(
            args.write_perm,
            len(load_source_artifacts(source_path, backend_name=args.backend).variant_names),
        )
        if variant is None:
            print(f'No variant found for hex {args.write_perm}', file=sys.stderr)
            raise SystemExit(1)
        print(_write_variant(source_path, variant, output_dir, args.backend))
        return
    if args.write_all:
        _write_all_variants(source_path, output_dir, args.backend)
        return
    if args.write_by_proportion:
        _write_random_variants(source_path, output_dir, args.proportions, args.iterations, args.backend)
        return

    typed_variant = tuple(False for _ in load_source_artifacts(source_path, backend_name=args.backend).variant_names)
    out_file = _write_variant(source_path, typed_variant, output_dir, args.backend)
    print(f'{perm_name(typed_variant)} {out_file}')


if __name__ == '__main__':
    main()
