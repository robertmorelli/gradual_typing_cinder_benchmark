"""Run --test on every benchmark and write bench_status.md."""

import subprocess
import sys
from pathlib import Path

BENCH_DIR = Path('static-python-perf/Benchmark')
OUT_FILE = Path('bench_status.md')

NO_ADVANCED = []
WORKS = []
DETYPE_BROKEN = []
BENCH_BROKEN = []


def run_test(name: str) -> tuple[int, int, str]:
    """Returns (typed_rc, detyped_rc, stderr)."""
    result = subprocess.run(
        [sys.executable, 'detype.py', '--test', name],
        capture_output=True, text=True,
    )
    typed_rc = detyped_rc = -1
    for line in result.stdout.splitlines():
        if line.startswith('returncode:'):
            rc = int(line.split(':')[1].strip())
            if typed_rc == -1:
                typed_rc = rc
            else:
                detyped_rc = rc
    return typed_rc, detyped_rc, result.stderr


benchmarks = sorted(p.parent.parent.name for p in BENCH_DIR.glob('*/advanced/main.py'))
no_advanced = sorted(
    p.name for p in BENCH_DIR.iterdir()
    if p.is_dir() and not (p / 'advanced' / 'main.py').exists()
    and p.name != '__pycache__'
)

print(f"Testing {len(benchmarks)} benchmarks...")

for name in benchmarks:
    print(f"  {name}...", end='', flush=True)
    typed_rc, detyped_rc, stderr = run_test(name)
    if typed_rc != 0:
        BENCH_BROKEN.append(name)
        print(f" broken (typed exit {typed_rc})")
    elif detyped_rc != 0:
        DETYPE_BROKEN.append(name)
        print(f" detyping broken (detyped exit {detyped_rc})")
    else:
        WORKS.append(name)
        print(" ok")


def ul(items):
    if not items:
        return ''
    return '\n'.join(f'- {x}' for x in sorted(items)) + '\n'


lines = ['# Benchmark Status\n']

lines.append('## Detyping works\n')
lines.append(ul(WORKS))

lines.append('## Detyping broken\n')
lines.append(ul(DETYPE_BROKEN))

lines.append('## Benchmark broken\n')
lines.append(ul(BENCH_BROKEN))

lines.append('## No advanced/main.py\n')
lines.append(ul(no_advanced))

OUT_FILE.write_text('\n'.join(lines), encoding='utf-8')
print(f"\nWrote {OUT_FILE}")
