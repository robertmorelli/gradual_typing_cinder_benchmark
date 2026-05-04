"""Measure pairwise interactions for float, then predict random perms."""
from __future__ import annotations

import json
import tempfile
from itertools import combinations
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

from detyper.artifact_runner import run_timed_python_artifact_detailed
from detyper.artifacts import build_source_variant, load_source_artifacts

OUT_DIR = Path('benchmark_results/float_prediction')
RUNS_PER_PERM = 3

SINGLE_RUNTIME = {
    78: 0.3496, 80: 0.4020, 83: 0.3487, 92: 0.3502, 101: 0.3481,
    110: 0.3478, 165: 0.3985, 167: 0.3916, 170: 0.4379, 252: 0.3479,
    254: 0.3590, 261: 0.3498, 295: 0.3498, 297: 0.3473,
}


def measure(arts, n, idxs, tmp):
    perm = tuple(j in set(idxs) for j in range(n))
    prog = build_source_variant(arts, perm)
    art = tmp / f'main_{prog.perm_hex}.py'
    art.write_text(prog.source, encoding='utf-8')
    rel = art.relative_to(Path.cwd())
    return min(run_timed_python_artifact_detailed(rel, skip_typecheck=True).timing for _ in range(RUNS_PER_PERM))


def main():
    src = Path('static-python-perf/Benchmark/float/advanced/main.py')
    arts = load_source_artifacts(src, output_dir=OUT_DIR)
    n = len(arts.variant_names)
    ann_ids = [int(a) for a in arts.variant_names]

    pair_path = OUT_DIR / 'pairs.json'
    with tempfile.TemporaryDirectory(prefix='.float-pairs-', dir=Path.cwd()) as tmp:
        tmp = Path(tmp)
        baseline = measure(arts, n, [], tmp)
        print(f'baseline = {baseline:.4f}s')

        single = {a: SINGLE_RUNTIME[a] - baseline for a in ann_ids}

        if pair_path.exists():
            pair_runtime = {tuple(map(int,k.split(','))): v for k,v in json.loads(pair_path.read_text()).items()}
            print(f'loaded {len(pair_runtime)} cached pair runtimes')
        else:
            pair_runtime = {}
        pairs = list(combinations(range(n), 2))
        for k, (i, j) in enumerate(pairs, start=1):
            key = (i, j)
            if key in pair_runtime:
                continue
            t = measure(arts, n, [i, j], tmp)
            pair_runtime[key] = t
            if k % 10 == 0 or k == len(pairs):
                print(f'  [{k}/{len(pairs)}] pair ({ann_ids[i]},{ann_ids[j]}) t={t:.4f}s', flush=True)
                pair_path.write_text(json.dumps({f'{a},{b}': v for (a,b),v in pair_runtime.items()}, indent=2))
        pair_path.write_text(json.dumps({f'{a},{b}': v for (a,b),v in pair_runtime.items()}, indent=2))

    # interaction(i,j) = T(i,j) - baseline - single(i) - single(j)
    inter = {}
    for (i, j), t in pair_runtime.items():
        inter[(i, j)] = t - baseline - single[ann_ids[i]] - single[ann_ids[j]]

    # heatmap of interactions
    M = np.zeros((n, n))
    for (i, j), v in inter.items():
        M[i, j] = v * 1000
        M[j, i] = v * 1000

    fig, ax = plt.subplots(figsize=(8, 7))
    vmax = max(abs(M.min()), abs(M.max()))
    im = ax.imshow(M, cmap='RdBu_r', vmin=-vmax, vmax=vmax)
    ax.set_xticks(range(n)); ax.set_xticklabels(arts.variant_names, rotation=90, fontsize=8)
    ax.set_yticks(range(n)); ax.set_yticklabels(arts.variant_names, fontsize=8)
    ax.set_title('float: pairwise interactions (ms)\n(red = sub-additive: pair costs less than sum of singles)')
    plt.colorbar(im, ax=ax, label='interaction (ms)')
    fig.tight_layout()
    fig.savefig(OUT_DIR / 'float_pair_heatmap.png', dpi=130)
    print(f'wrote {OUT_DIR}/float_pair_heatmap.png')

    # predict random samples using baseline + singles + pair interactions
    samples = json.loads((OUT_DIR / 'samples.json').read_text())
    actuals, preds_s, preds_sp, n_bits = [], [], [], []
    for row in samples:
        bits = row['perm']
        on = [k for k, b in enumerate(bits) if b]
        s = sum(single[ann_ids[k]] for k in on)
        p = sum(inter[(min(i,j), max(i,j))] for i, j in combinations(on, 2)) if len(on) >= 2 else 0.0
        actuals.append(row['runtime'])
        preds_s.append(baseline + s)
        preds_sp.append(baseline + s + p)
        n_bits.append(len(on))

    actuals = np.array(actuals); preds_s = np.array(preds_s); preds_sp = np.array(preds_sp); n_bits = np.array(n_bits)

    def stats(pred):
        err = actuals - pred
        ae = np.abs(err); re = ae / actuals
        ss_res = np.sum(err**2); ss_tot = np.sum((actuals - actuals.mean())**2)
        return ae.mean()*1000, re.mean()*100, ae.max()*1000, re.max()*100, 1-ss_res/ss_tot
    s = stats(preds_s); sp = stats(preds_sp)
    print(f'\nsingles only  : mean |err|={s[0]:.2f}ms ({s[1]:.2f}%), max={s[2]:.2f}ms ({s[3]:.2f}%), R²={s[4]:.3f}')
    print(f'singles+pairs : mean |err|={sp[0]:.2f}ms ({sp[1]:.2f}%), max={sp[2]:.2f}ms ({sp[3]:.2f}%), R²={sp[4]:.3f}')

    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    for ax, pred, label, st in [(axes[0], preds_s, 'singles only', s), (axes[1], preds_sp, 'singles + pairs', sp)]:
        sc = ax.scatter(actuals, pred, c=n_bits, cmap='viridis', alpha=0.75)
        lims = [min(actuals.min(), pred.min()), max(actuals.max(), pred.max())]
        ax.plot(lims, lims, 'k--', linewidth=1)
        ax.set_xlabel('actual runtime (s)'); ax.set_ylabel('predicted (s)')
        ax.set_title(f'{label}\nR²={st[4]:.3f}, mean {st[0]:.1f}ms ({st[1]:.1f}%), max {st[2]:.1f}ms ({st[3]:.1f}%)')
        ax.set_aspect('equal')
        plt.colorbar(sc, ax=ax, label='# detyped')
    fig.tight_layout()
    out = OUT_DIR / 'float_predict_singles_vs_pairs.png'
    fig.savefig(out, dpi=130)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
