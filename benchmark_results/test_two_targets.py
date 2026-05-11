from pathlib import Path
import subprocess
from detyper.ast_data import build_ast_data
from detyper.bundle_builder import build_detyper_map_from_ast_data
from detyper.pipeline import build_detyped_program_from_ast_data

SRC=Path('static-python-perf/Benchmark/deltablue/advanced/main.py')
OUT=Path('benchmark_results/two_target_current'); OUT.mkdir(parents=True, exist_ok=True)
PY=Path('cinder_env/bin/python')
targets=[('method_parameter_annotation','cinder_checked_container'),('method_local_annotation_with_value','cinder_checked_container')]
src=SRC.read_text(); ad=build_ast_data(src); m=build_detyper_map_from_ast_data(ad); ids=[str(x) for x in m['annotation_ids']]; anns=ad.indexes['annotations']
for ctx, kind in targets:
    sel={i for i in ids if anns.get(i,{}).get('context')==ctx and anns.get(i,{}).get('type_kind')==kind}
    perm=tuple(i in sel for i in ids)
    prog=build_detyped_program_from_ast_data(ad,m,perm)
    path=OUT/f'{ctx}__{kind}_{len(sel)}.py'; path.write_text(prog.source)
    tc=subprocess.run([str(PY),'--typecheck-only',str(path)],capture_output=True,text=True,timeout=60)
    if tc.returncode!=0:
        print(ctx, kind, len(sel), 'TC_FILTER_FAIL', (tc.stdout+tc.stderr).replace('\n',' | ')[-500:]); continue
    rt=subprocess.run([str(PY),'--skip-typecheck',str(path)],capture_output=True,text=True,timeout=120)
    print(ctx, kind, len(sel), 'RUNTIME_PASS' if rt.returncode==0 else 'RUNTIME_FAIL', (rt.stdout+rt.stderr).replace('\n',' | ')[-500:])
