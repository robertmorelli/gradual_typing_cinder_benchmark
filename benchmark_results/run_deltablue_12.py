from pathlib import Path
import random, subprocess, csv
from detyper.ast_data import build_ast_data
from detyper.bundle_builder import build_detyper_map_from_ast_data
from detyper.pipeline import build_detyped_program_from_ast_data
SRC=Path('static-python-perf/Benchmark/deltablue/advanced/main.py')
OUT=Path('benchmark_results/deltablue_random_12_current'); OUT.mkdir(parents=True, exist_ok=True)
PY=Path('cinder_env/bin/python')
rng=random.Random(1729)
src=SRC.read_text(); ad=build_ast_data(src); m=build_detyper_map_from_ast_data(ad); ids=list(m['annotation_ids']); n=len(ids)
perms=[tuple(False for _ in ids), tuple(True for _ in ids)]
for _ in range(10): perms.append(tuple(rng.choice([False, True]) for _ in ids))
rows=[]
for i,perm in enumerate(perms):
    path=OUT/f'sample_{i:02d}_{sum(perm)}of{n}.py'
    path.write_text(build_detyped_program_from_ast_data(ad,m,perm).source)
    tc=subprocess.run([str(PY),'--typecheck-only',str(path)],capture_output=True,text=True,timeout=90)
    if tc.returncode!=0:
        status='TC_FILTER_FAIL'; msg=(tc.stdout+tc.stderr).replace('\n',' | ')[-500:]
    else:
        rt=subprocess.run([str(PY),'--skip-typecheck',str(path)],capture_output=True,text=True,timeout=180)
        status='RUNTIME_PASS' if rt.returncode==0 else 'RUNTIME_FAIL'; msg=(rt.stdout+rt.stderr).replace('\n',' | ')[-500:]
    print(i, sum(perm), status, msg)
    rows.append({'sample':i,'detyped':sum(perm),'total':n,'status':status,'msg':msg,'path':str(path)})
with (OUT/'summary.csv').open('w', newline='') as f:
    w=csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
