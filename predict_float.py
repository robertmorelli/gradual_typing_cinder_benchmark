"""Sample float-benchmark perms, run them, fit a linear model, plot results."""
from __future__ import annotations

import json
import random
import sys
import tempfile
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import Ridge

from detyper.artifact_runner import run_timed_python_artifact_detailed
from detyper.artifacts import build_source_variant, load_source_artifacts

BENCH = 'float'
N_SAMPLES = 100
RUNS_PER_PERM = 3
SEED = 42
OUT_DIR = Path('benchmark_results') / f'{BENCH}_prediction'


def collect(arts, perms, tmpdir):
    rows = []
    for i, perm in enumerate(perms, start=1):
        prog = build_source_variant(arts, perm)
        artifact = tmpdir / f'main_{prog.perm_hex}.py'
        artifact.write_text(prog.source, encoding='utf-8')
        rel = artifact.relative_to(Path.cwd())
        try:
            timings = [run_timed_python_artifact_detailed(rel, skip_typecheck=True).timing for _ in range(RUNS_PER_PERM)]
            t = min(timings)
        except Exception as exc:
            print(f'  [{i}/{len(perms)}] {prog.perm_hex} FAILED: {exc!s:.120}', flush=True)
            continue
        rows.append({'perm': list(perm), 'perm_hex': prog.perm_hex, 'runtime': t, 'all_runs': timings})
        print(f'  [{i}/{len(perms)}] {prog.perm_hex} t={t:.4f}s', flush=True)
    return rows


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    src = Path(f'static-python-perf/Benchmark/{BENCH}/advanced/main.py')
    arts = load_source_artifacts(src, output_dir=OUT_DIR)
    n = len(arts.variant_names)
    print(f'{BENCH}: {n} annotations, sampling {N_SAMPLES} perms × {RUNS_PER_PERM} runs', flush=True)

    rng = random.Random(SEED)
    seen = set()
    perms = []
    for boundary in (tuple([False]*n), tuple([True]*n)):
        if boundary not in seen:
            seen.add(boundary); perms.append(boundary)
    while len(perms) < N_SAMPLES:
        cand = tuple(rng.random() < 0.5 for _ in range(n))
        if cand in seen: continue
        seen.add(cand); perms.append(cand)

    with tempfile.TemporaryDirectory(prefix='.float-pred-', dir=Path.cwd()) as tmp:
        rows = collect(arts, perms, Path(tmp))

    (OUT_DIR / 'samples.json').write_text(json.dumps(rows, indent=2))

    X = np.array([r['perm'] for r in rows], dtype=float)
    y = np.array([r['runtime'] for r in rows])
    model = Ridge(alpha=1.0).fit(X, y)
    y_pred = model.predict(X)
    r2 = model.score(X, y)
    print(f'\nfit: intercept={model.intercept_:.4f}s  R²={r2:.3f}')

    coefs = model.coef_
    order = np.argsort(coefs)
    labels = [arts.variant_names[i] for i in order]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    bars = ax1.barh(range(len(coefs)), coefs[order], color=['#d62728' if c>0 else '#2ca02c' for c in coefs[order]])
    ax1.set_yticks(range(len(coefs)))
    ax1.set_yticklabels(labels, fontsize=8)
    ax1.set_xlabel('Δ runtime (s) when annotation is detyped')
    ax1.set_title(f'{BENCH}: per-annotation cost (Ridge, R²={r2:.2f})')
    ax1.axvline(0, color='black', linewidth=0.5)

    ax2.scatter(y, y_pred, alpha=0.6)
    lims = [min(y.min(), y_pred.min()), max(y.max(), y_pred.max())]
    ax2.plot(lims, lims, 'k--', linewidth=1)
    ax2.set_xlabel('actual runtime (s)')
    ax2.set_ylabel('predicted runtime (s)')
    ax2.set_title(f'predicted vs actual ({len(rows)} samples)')
    ax2.set_aspect('equal')

    fig.tight_layout()
    fig.savefig(OUT_DIR / 'float_prediction.png', dpi=130)
    print(f'wrote {OUT_DIR}/float_prediction.png')

    np.savez(OUT_DIR / 'model.npz', coef=model.coef_, intercept=model.intercept_,
             annotation_ids=np.array(arts.variant_names))


if __name__ == '__main__':
    sys.exit(main())
