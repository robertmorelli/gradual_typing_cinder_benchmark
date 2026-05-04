"""Predict random-perm runtimes using ONLY single-annotation cost measurements."""
from __future__ import annotations

import json
import re
import tempfile
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

from detyper.artifact_runner import run_timed_python_artifact_detailed
from detyper.artifacts import build_source_variant, load_source_artifacts

OUT_DIR = Path('benchmark_results/float_prediction')
RUNS_PER_PERM = 3

# Single-annotation actuals from predict_float_single.py output:
SINGLE_RUNTIME = {
    78: 0.3496, 80: 0.4020, 83: 0.3487, 92: 0.3502, 101: 0.3481,
    110: 0.3478, 165: 0.3985, 167: 0.3916, 170: 0.4379, 252: 0.3479,
    254: 0.3590, 261: 0.3498, 295: 0.3498, 297: 0.3473,
}


def main():
    src = Path('static-python-perf/Benchmark/float/advanced/main.py')
    arts = load_source_artifacts(src, output_dir=OUT_DIR)
    n = len(arts.variant_names)
    ann_ids = [int(a) for a in arts.variant_names]

    # Baseline = all-typed perm (0x0). Re-measure to use the same noise floor
    # as the single-annotation runs (3-of-min protocol).
    with tempfile.TemporaryDirectory(prefix='.float-base-', dir=Path.cwd()) as tmp:
        tmp = Path(tmp)
        prog = build_source_variant(arts, tuple([False]*n))
        artifact = tmp / f'main_{prog.perm_hex}.py'
        artifact.write_text(prog.source, encoding='utf-8')
        rel = artifact.relative_to(Path.cwd())
        baseline = min(run_timed_python_artifact_detailed(rel, skip_typecheck=True).timing for _ in range(RUNS_PER_PERM))
    print(f'baseline (all-typed) = {baseline:.4f}s')

    # Per-annotation marginal cost = single_runtime - baseline
    cost = {a: SINGLE_RUNTIME[a] - baseline for a in ann_ids}
    for a in ann_ids:
        print(f'  ann {a:>4}: marginal = {cost[a]*1000:+.2f} ms')

    samples = json.loads((OUT_DIR / 'samples.json').read_text())

    actuals, preds, n_bits = [], [], []
    for row in samples:
        bits = row['perm']
        actual = row['runtime']
        pred = baseline + sum(cost[ann_ids[i]] for i, b in enumerate(bits) if b)
        actuals.append(actual); preds.append(pred); n_bits.append(sum(bits))

    actuals = np.array(actuals); preds = np.array(preds); n_bits = np.array(n_bits)
    err = actuals - preds
    abs_err = np.abs(err)
    rel_err = abs_err / actuals
    ss_res = np.sum(err**2)
    ss_tot = np.sum((actuals - actuals.mean())**2)
    r2 = 1 - ss_res/ss_tot
    print(f'\npredict {len(samples)} random perms from singles only:')
    print(f'  mean |err| = {abs_err.mean()*1000:.2f}ms ({rel_err.mean()*100:.2f}%)')
    print(f'  max  |err| = {abs_err.max()*1000:.2f}ms ({rel_err.max()*100:.2f}%)')
    print(f'  R²         = {r2:.3f}')

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))
    ax1.scatter(actuals, preds, c=n_bits, cmap='viridis', alpha=0.75)
    lims = [min(actuals.min(), preds.min()), max(actuals.max(), preds.max())]
    ax1.plot(lims, lims, 'k--', linewidth=1)
    ax1.set_xlabel('actual runtime (s)')
    ax1.set_ylabel('predicted: baseline + Σ singles (s)')
    ax1.set_title(f'float: predicted from singles only\nR²={r2:.3f}, mean err {abs_err.mean()*1000:.1f}ms ({rel_err.mean()*100:.1f}%)')
    ax1.set_aspect('equal')
    cbar = plt.colorbar(ax1.collections[0], ax=ax1)
    cbar.set_label('# annotations detyped')

    ax2.scatter(n_bits, err*1000, alpha=0.7)
    ax2.axhline(0, color='black', linewidth=0.5)
    ax2.set_xlabel('# annotations detyped in perm')
    ax2.set_ylabel('actual − predicted (ms)')
    ax2.set_title('residual vs perm size\n(positive = singles under-predict combined cost)')

    fig.tight_layout()
    out = OUT_DIR / 'float_predict_from_singles.png'
    fig.savefig(out, dpi=130)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
