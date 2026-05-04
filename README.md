# Gradual Typing Cinder Benchmark

### Running an experiment:

Set up experiment (local):

```bash
python3 setup_experiment.py --limit 1025
```

Setup (cloudlab):

```bash
git clone https://github.com/robertmorelli/gradual_typing_cinder_benchmark.git && cd gradual_typing_cinder_benchmark/ && ./setup.sh 
```

Typecheck experiment (cloudlab):

```bash
python3 typecheck_exp.py
```

List remaining planned parts to run (anywhere):

```bash
python3 whats_next.py
```

Run a particular part

reminder of TMUX stuff:
```bash
tmux new -s work
```
then log in to gh:
```bash
gh auth login
```
make docker not broken
```bash
newgrp docker
```

press `Ctrl-b` then `d` to leave then to come back:
```bash
tmux attach -t work
```
Dont forget to commit results:
```bash
git pull --rebase && git add benchmark_results/ && git commit -m "<message>" && git push
```

Finish up experiment (anywhere):
```bash
python3 make_summary.py
```

### Debugging:

Write one detyped file:

```bash
python3 make_detyped_file.py deltablue advanced 0x0
```

Refresh the benchmark status CSV:

```bash
python3 get_bench_status.py
```