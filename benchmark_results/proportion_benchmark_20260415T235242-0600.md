# Proportion Benchmark Report

- Generated: `2026-04-15T23:52:42-06:00`
- Source CSV: `benchmark_results/proportion_benchmark_20260415T235242-0600.csv`
- Benchmarks run serially: `yes`
- Iterations per detyped-count bucket: `1`
- Random seed: `0`

## call_method/advanced

- Detypable targets: `6`
- Total runs: `7`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.3140s | 0.3140s | 0.3140s | 10.0 | yes | ok |
| 0.17 | 1/6 | 1 | 0.3873s | 0.3873s | 0.3873s | 5.0 | yes | ok |
| 0.33 | 2/6 | 1 | 0.5153s | 0.5153s | 0.5153s | 14.0 | yes | ok |
| 0.50 | 3/6 | 1 | 1.6489s | 1.6489s | 1.6489s | 3.0 | yes | ok |
| 0.67 | 4/6 | 1 | 0.4527s | 0.4527s | 0.4527s | 25.0 | yes | ok |
| 0.83 | 5/6 | 1 | 1.7123s | 1.7123s | 1.7123s | 2.0 | yes | ok |
| 1.00 | 6/6 | 1 | 1.6879s | 1.6879s | 1.6879s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.3140s | 0.1282s | 10 | 80 | yes | 0.2877s | 0.3438s | `detyped_files/call_method/advanced/proportion_sweep/main_0x0_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 0.3873s | 0.1192s | 5 | 40 | yes | 0.3522s | 0.4250s | `detyped_files/call_method/advanced/proportion_sweep/main_0x4_k01_s01.py` |  |
| 0.33 | 2/6 | 1 | 0.5153s | 0.2559s | 14 | 112 | yes | 0.4700s | 0.5631s | `detyped_files/call_method/advanced/proportion_sweep/main_0x24_k02_s01.py` |  |
| 0.50 | 3/6 | 1 | 1.6489s | 0.3565s | 3 | 24 | yes | 1.5250s | 1.7967s | `detyped_files/call_method/advanced/proportion_sweep/main_0xe_k03_s01.py` |  |
| 0.67 | 4/6 | 1 | 0.4527s | 0.2829s | 25 | 200 | yes | 0.4199s | 0.4967s | `detyped_files/call_method/advanced/proportion_sweep/main_0x1d_k04_s01.py` |  |
| 0.83 | 5/6 | 1 | 1.7123s | 0.2845s | 2 | 16 | yes | 1.5886s | 1.8516s | `detyped_files/call_method/advanced/proportion_sweep/main_0x37_k05_s01.py` |  |
| 1.00 | 6/6 | 1 | 1.6879s | 0.1861s | 1 | 8 | yes | 1.5612s | 1.8006s | `detyped_files/call_method/advanced/proportion_sweep/main_0x3f_k06_s01.py` |  |

## call_method/shallow

- Detypable targets: `6`
- Total runs: `7`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.2205s | 0.2205s | 0.2205s | 5.0 | yes | ok |
| 0.17 | 1/6 | 1 | 0.1733s | 0.1733s | 0.1733s | 3.0 | yes | ok |
| 0.33 | 2/6 | 1 | 1.3562s | 1.3562s | 1.3562s | 1.0 | yes | ok |
| 0.50 | 3/6 | 1 | 1.4892s | 1.4892s | 1.4892s | 3.0 | yes | ok |
| 0.67 | 4/6 | 1 | 1.4013s | 1.4013s | 1.4013s | 1.0 | yes | ok |
| 0.83 | 5/6 | 1 | 0.2464s | 0.2464s | 0.2464s | 1.0 | yes | ok |
| 1.00 | 6/6 | 1 | 1.6277s | 1.6277s | 1.6277s | 3.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.2205s | 0.0618s | 5 | 40 | yes | 0.2026s | 0.2403s | `detyped_files/call_method/shallow/proportion_sweep/main_0x0_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 0.1733s | 0.0410s | 3 | 24 | yes | 0.1578s | 0.1901s | `detyped_files/call_method/shallow/proportion_sweep/main_0x20_k01_s01.py` |  |
| 0.33 | 2/6 | 1 | 1.3562s | 0.1609s | 1 | 8 | yes | 1.2461s | 1.4512s | `detyped_files/call_method/shallow/proportion_sweep/main_0xa_k02_s01.py` |  |
| 0.50 | 3/6 | 1 | 1.4892s | 0.2838s | 3 | 24 | yes | 1.3875s | 1.6075s | `detyped_files/call_method/shallow/proportion_sweep/main_0x13_k03_s01.py` |  |
| 0.67 | 4/6 | 1 | 1.4013s | 0.1073s | 1 | 8 | yes | 1.3337s | 1.4713s | `detyped_files/call_method/shallow/proportion_sweep/main_0x2b_k04_s01.py` |  |
| 0.83 | 5/6 | 1 | 0.2464s | 0.0338s | 1 | 8 | yes | 0.2252s | 0.2681s | `detyped_files/call_method/shallow/proportion_sweep/main_0x3d_k05_s01.py` |  |
| 1.00 | 6/6 | 1 | 1.6277s | 0.3550s | 3 | 24 | yes | 1.4979s | 1.7771s | `detyped_files/call_method/shallow/proportion_sweep/main_0x3f_k06_s01.py` |  |

## call_method/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.1803s | 0.1803s | 0.1803s | 9.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.1803s | 0.0664s | 9 | 72 | yes | 0.1666s | 0.1970s | `static-python-perf/Benchmark/call_method/untyped/main.py` |  |

## call_method_slots/advanced

- Detypable targets: `6`
- Total runs: `7`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.2292s | 0.2292s | 0.2292s | 1.0 | yes | ok |
| 0.17 | 1/6 | 1 | 0.1846s | 0.1846s | 0.1846s | 4.0 | yes | ok |
| 0.33 | 2/6 | 1 | 1.3792s | 1.3792s | 1.3792s | 2.0 | yes | ok |
| 0.50 | 3/6 | 1 | 1.3902s | 1.3902s | 1.3902s | 1.0 | yes | ok |
| 0.67 | 4/6 | 1 | 1.3831s | 1.3831s | 1.3831s | 2.0 | yes | ok |
| 0.83 | 5/6 | 1 | 1.4877s | 1.4877s | 1.4877s | 2.0 | yes | ok |
| 1.00 | 6/6 | 1 | 1.4740s | 1.4740s | 1.4740s | 2.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.2292s | 0.0319s | 1 | 8 | yes | 0.2092s | 0.2502s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x0_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 0.1846s | 0.0453s | 4 | 32 | yes | 0.1719s | 0.2024s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x8_k01_s01.py` |  |
| 0.33 | 2/6 | 1 | 1.3792s | 0.2111s | 2 | 16 | yes | 1.2832s | 1.4838s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x12_k02_s01.py` |  |
| 0.50 | 3/6 | 1 | 1.3902s | 0.1340s | 1 | 8 | yes | 1.3170s | 1.4870s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x7_k03_s01.py` |  |
| 0.67 | 4/6 | 1 | 1.3831s | 0.1966s | 2 | 16 | yes | 1.2930s | 1.4793s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x2b_k04_s01.py` |  |
| 0.83 | 5/6 | 1 | 1.4877s | 0.2434s | 2 | 16 | yes | 1.3828s | 1.6090s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x2f_k05_s01.py` |  |
| 1.00 | 6/6 | 1 | 1.4740s | 0.2331s | 2 | 16 | yes | 1.3734s | 1.5973s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x3f_k06_s01.py` |  |

## call_method_slots/shallow

- Detypable targets: `6`
- Total runs: `7`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1956s | 0.1956s | 0.1956s | 4.0 | yes | ok |
| 0.17 | 1/6 | 1 | 1.4314s | 1.4314s | 1.4314s | 2.0 | yes | ok |
| 0.33 | 2/6 | 1 | 0.2677s | 0.2677s | 0.2677s | 4.0 | yes | ok |
| 0.50 | 3/6 | 1 | 0.1623s | 0.1623s | 0.1623s | 3.0 | yes | ok |
| 0.67 | 4/6 | 1 | 1.4517s | 1.4517s | 1.4517s | 1.0 | yes | ok |
| 0.83 | 5/6 | 1 | 1.3888s | 1.3888s | 1.3888s | 1.0 | yes | ok |
| 1.00 | 6/6 | 1 | 1.5286s | 1.5286s | 1.5286s | 2.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1956s | 0.0505s | 4 | 32 | yes | 0.1807s | 0.2148s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x0_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 1.4314s | 0.2165s | 2 | 16 | yes | 1.3348s | 1.5397s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x2_k01_s01.py` |  |
| 0.33 | 2/6 | 1 | 0.2677s | 0.0746s | 4 | 32 | yes | 0.2445s | 0.2939s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0xc_k02_s01.py` |  |
| 0.50 | 3/6 | 1 | 0.1623s | 0.0289s | 3 | 24 | yes | 0.1515s | 0.1740s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x38_k03_s01.py` |  |
| 0.67 | 4/6 | 1 | 1.4517s | 0.2081s | 1 | 8 | yes | 1.3312s | 1.5937s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x33_k04_s01.py` |  |
| 0.83 | 5/6 | 1 | 1.3888s | 0.1547s | 1 | 8 | yes | 1.2904s | 1.4902s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x3e_k05_s01.py` |  |
| 1.00 | 6/6 | 1 | 1.5286s | 0.2243s | 2 | 16 | yes | 1.4266s | 1.6407s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x3f_k06_s01.py` |  |

## call_method_slots/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.2042s | 0.2042s | 0.2042s | 13.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.2042s | 0.1001s | 13 | 104 | yes | 0.1864s | 0.2245s | `static-python-perf/Benchmark/call_method_slots/untyped/main.py` |  |
