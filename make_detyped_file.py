"""Write one benchmark variant into detyped_files."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from detyper.artifacts import build_source_variant, load_source_artifacts, write_source_variant
from detyper.benchmark_harness import benchmark_output_dir, resolve_benchmark_path

VARIANTS = ('advanced', 'shallow', 'untyped')


def perm_from_hex(value: str, width: int) -> tuple[bool, ...]:
    try:
        integer = int(value, 16)
    except ValueError:
        raise SystemExit(f'Invalid detype hex: {value}')

    bits = format(integer, f'0{width}b') if width else ''
    if len(bits) > width:
        raise SystemExit(f'Detype hex {value} does not fit {width} detypable functions')
    return tuple(bit == '1' for bit in bits)


def write_detyped_file(benchmark: str, variant_name: str, detype_hex: str) -> Path:
    source_path = resolve_benchmark_path(benchmark, variant=variant_name)
    output_dir = benchmark_output_dir(source_path)

    if variant_name == 'untyped':
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / f'{source_path.stem}_untyped.py'
        shutil.copyfile(source_path, output_path)
        return output_path

    artifacts = load_source_artifacts(source_path, output_dir=output_dir)
    perm = perm_from_hex(detype_hex, len(artifacts.variant_names))
    program = build_source_variant(artifacts, perm)
    return write_source_variant(artifacts, program)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Write one detyped benchmark file')
    parser.add_argument('benchmark')
    parser.add_argument('variant', choices=VARIANTS)
    parser.add_argument('detype_hex')
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(write_detyped_file(args.benchmark, args.variant, args.detype_hex))


if __name__ == '__main__':
    main()
