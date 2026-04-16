# Proportion Benchmark Report

- Generated: `2026-04-15T22:39:16-06:00`
- Source CSV: `benchmark_results/proportion_benchmark_20260415T223916-0600.csv`
- Benchmarks run serially: `yes`
- Iterations per detyped-count bucket: `2`
- Random seed: `0`

## call_method/advanced

- Detypable targets: `6`
- Total runs: `12`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 0 | - | - | - | - | - | 1 failed |
| 0.17 | 1/6 | 0 | - | - | - | - | - | 2 failed |
| 0.33 | 2/6 | 0 | - | - | - | - | - | 2 failed |
| 0.50 | 3/6 | 0 | - | - | - | - | - | 2 failed |
| 0.67 | 4/6 | 0 | - | - | - | - | - | 2 failed |
| 0.83 | 5/6 | 0 | - | - | - | - | - | 2 failed |
| 1.00 | 6/6 | 0 | - | - | - | - | - | 1 failed |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_method/advanced/proportion_sweep/main_0x0_k00_s01.py` | artifact main_0x0_k00_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method/advanced/proportion_sweep/main_0x0_k00_s01.py", line 1, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.17 | 1/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_method/advanced/proportion_sweep/main_0x4_k01_s01.py` | artifact main_0x4_k01_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method/advanced/proportion_sweep/main_0x4_k01_s01.py", line 1, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.17 | 1/6 | 2 | - | - | - | - | - | - | - | `detyped_files/call_method/advanced/proportion_sweep/main_0x20_k01_s02.py` | artifact main_0x20_k01_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method/advanced/proportion_sweep/main_0x20_k01_s02.py", line 1, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.33 | 2/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_method/advanced/proportion_sweep/main_0xa_k02_s01.py` | artifact main_0xa_k02_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method/advanced/proportion_sweep/main_0xa_k02_s01.py", line 1, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.33 | 2/6 | 2 | - | - | - | - | - | - | - | `detyped_files/call_method/advanced/proportion_sweep/main_0x5_k02_s02.py` | artifact main_0x5_k02_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method/advanced/proportion_sweep/main_0x5_k02_s02.py", line 1, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.50 | 3/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_method/advanced/proportion_sweep/main_0xd_k03_s01.py` | artifact main_0xd_k03_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method/advanced/proportion_sweep/main_0xd_k03_s01.py", line 1, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.50 | 3/6 | 2 | - | - | - | - | - | - | - | `detyped_files/call_method/advanced/proportion_sweep/main_0x13_k03_s02.py` | artifact main_0x13_k03_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method/advanced/proportion_sweep/main_0x13_k03_s02.py", line 1, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.67 | 4/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_method/advanced/proportion_sweep/main_0x39_k04_s01.py` | artifact main_0x39_k04_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method/advanced/proportion_sweep/main_0x39_k04_s01.py", line 1, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.67 | 4/6 | 2 | - | - | - | - | - | - | - | `detyped_files/call_method/advanced/proportion_sweep/main_0x1e_k04_s02.py` | artifact main_0x1e_k04_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method/advanced/proportion_sweep/main_0x1e_k04_s02.py", line 1, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.83 | 5/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_method/advanced/proportion_sweep/main_0x3b_k05_s01.py` | artifact main_0x3b_k05_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method/advanced/proportion_sweep/main_0x3b_k05_s01.py", line 1, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.83 | 5/6 | 2 | - | - | - | - | - | - | - | `detyped_files/call_method/advanced/proportion_sweep/main_0x2f_k05_s02.py` | artifact main_0x2f_k05_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method/advanced/proportion_sweep/main_0x2f_k05_s02.py", line 1, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 1.00 | 6/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_method/advanced/proportion_sweep/main_0x3f_k06_s01.py` | artifact main_0x3f_k06_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method/advanced/proportion_sweep/main_0x3f_k06_s01.py", line 1, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |

## call_method/shallow

- Detypable targets: `6`
- Total runs: `12`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 0 | - | - | - | - | - | 1 failed |
| 0.17 | 1/6 | 0 | - | - | - | - | - | 2 failed |
| 0.33 | 2/6 | 0 | - | - | - | - | - | 2 failed |
| 0.50 | 3/6 | 0 | - | - | - | - | - | 2 failed |
| 0.67 | 4/6 | 0 | - | - | - | - | - | 2 failed |
| 0.83 | 5/6 | 0 | - | - | - | - | - | 2 failed |
| 1.00 | 6/6 | 0 | - | - | - | - | - | 1 failed |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_method/shallow/proportion_sweep/main_0x0_k00_s01.py` | artifact main_0x0_k00_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method/shallow/proportion_sweep/main_0x0_k00_s01.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.17 | 1/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_method/shallow/proportion_sweep/main_0x2_k01_s01.py` | artifact main_0x2_k01_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method/shallow/proportion_sweep/main_0x2_k01_s01.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.17 | 1/6 | 2 | - | - | - | - | - | - | - | `detyped_files/call_method/shallow/proportion_sweep/main_0x4_k01_s02.py` | artifact main_0x4_k01_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method/shallow/proportion_sweep/main_0x4_k01_s02.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.33 | 2/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_method/shallow/proportion_sweep/main_0x6_k02_s01.py` | artifact main_0x6_k02_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method/shallow/proportion_sweep/main_0x6_k02_s01.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.33 | 2/6 | 2 | - | - | - | - | - | - | - | `detyped_files/call_method/shallow/proportion_sweep/main_0x28_k02_s02.py` | artifact main_0x28_k02_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method/shallow/proportion_sweep/main_0x28_k02_s02.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.50 | 3/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_method/shallow/proportion_sweep/main_0x23_k03_s01.py` | artifact main_0x23_k03_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method/shallow/proportion_sweep/main_0x23_k03_s01.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.50 | 3/6 | 2 | - | - | - | - | - | - | - | `detyped_files/call_method/shallow/proportion_sweep/main_0x25_k03_s02.py` | artifact main_0x25_k03_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method/shallow/proportion_sweep/main_0x25_k03_s02.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.67 | 4/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_method/shallow/proportion_sweep/main_0x2e_k04_s01.py` | artifact main_0x2e_k04_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method/shallow/proportion_sweep/main_0x2e_k04_s01.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.67 | 4/6 | 2 | - | - | - | - | - | - | - | `detyped_files/call_method/shallow/proportion_sweep/main_0x2d_k04_s02.py` | artifact main_0x2d_k04_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method/shallow/proportion_sweep/main_0x2d_k04_s02.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.83 | 5/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_method/shallow/proportion_sweep/main_0x37_k05_s01.py` | artifact main_0x37_k05_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method/shallow/proportion_sweep/main_0x37_k05_s01.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.83 | 5/6 | 2 | - | - | - | - | - | - | - | `detyped_files/call_method/shallow/proportion_sweep/main_0x3d_k05_s02.py` | artifact main_0x3d_k05_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method/shallow/proportion_sweep/main_0x3d_k05_s02.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 1.00 | 6/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_method/shallow/proportion_sweep/main_0x3f_k06_s01.py` | artifact main_0x3f_k06_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method/shallow/proportion_sweep/main_0x3f_k06_s01.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |

## call_method/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.1419s | 0.1419s | 0.1419s | 8.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.1419s | 0.0558s | 8 | 64 | yes | 0.1291s | 0.1561s | `static-python-perf/Benchmark/call_method/untyped/main.py` |  |

## call_method_slots/advanced

- Detypable targets: `6`
- Total runs: `12`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 0 | - | - | - | - | - | 1 failed |
| 0.17 | 1/6 | 0 | - | - | - | - | - | 2 failed |
| 0.33 | 2/6 | 0 | - | - | - | - | - | 2 failed |
| 0.50 | 3/6 | 0 | - | - | - | - | - | 2 failed |
| 0.67 | 4/6 | 0 | - | - | - | - | - | 2 failed |
| 0.83 | 5/6 | 0 | - | - | - | - | - | 2 failed |
| 1.00 | 6/6 | 0 | - | - | - | - | - | 1 failed |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x0_k00_s01.py` | artifact main_0x0_k00_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method_slots/advanced/proportion_sweep/main_0x0_k00_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.17 | 1/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x20_k01_s01.py` | artifact main_0x20_k01_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method_slots/advanced/proportion_sweep/main_0x20_k01_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.17 | 1/6 | 2 | - | - | - | - | - | - | - | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x8_k01_s02.py` | artifact main_0x8_k01_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method_slots/advanced/proportion_sweep/main_0x8_k01_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.33 | 2/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0xa_k02_s01.py` | artifact main_0xa_k02_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method_slots/advanced/proportion_sweep/main_0xa_k02_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.33 | 2/6 | 2 | - | - | - | - | - | - | - | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x21_k02_s02.py` | artifact main_0x21_k02_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method_slots/advanced/proportion_sweep/main_0x21_k02_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.50 | 3/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x1a_k03_s01.py` | artifact main_0x1a_k03_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method_slots/advanced/proportion_sweep/main_0x1a_k03_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.50 | 3/6 | 2 | - | - | - | - | - | - | - | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0xb_k03_s02.py` | artifact main_0xb_k03_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method_slots/advanced/proportion_sweep/main_0xb_k03_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.67 | 4/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x35_k04_s01.py` | artifact main_0x35_k04_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method_slots/advanced/proportion_sweep/main_0x35_k04_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.67 | 4/6 | 2 | - | - | - | - | - | - | - | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x3a_k04_s02.py` | artifact main_0x3a_k04_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method_slots/advanced/proportion_sweep/main_0x3a_k04_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.83 | 5/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x3b_k05_s01.py` | artifact main_0x3b_k05_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method_slots/advanced/proportion_sweep/main_0x3b_k05_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.83 | 5/6 | 2 | - | - | - | - | - | - | - | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x2f_k05_s02.py` | artifact main_0x2f_k05_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method_slots/advanced/proportion_sweep/main_0x2f_k05_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 1.00 | 6/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x3f_k06_s01.py` | artifact main_0x3f_k06_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method_slots/advanced/proportion_sweep/main_0x3f_k06_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |

## call_method_slots/shallow

- Detypable targets: `6`
- Total runs: `12`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 0 | - | - | - | - | - | 1 failed |
| 0.17 | 1/6 | 0 | - | - | - | - | - | 2 failed |
| 0.33 | 2/6 | 0 | - | - | - | - | - | 2 failed |
| 0.50 | 3/6 | 0 | - | - | - | - | - | 2 failed |
| 0.67 | 4/6 | 0 | - | - | - | - | - | 2 failed |
| 0.83 | 5/6 | 0 | - | - | - | - | - | 2 failed |
| 1.00 | 6/6 | 0 | - | - | - | - | - | 1 failed |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x0_k00_s01.py` | artifact main_0x0_k00_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method_slots/shallow/proportion_sweep/main_0x0_k00_s01.py", line 14, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.17 | 1/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x10_k01_s01.py` | artifact main_0x10_k01_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method_slots/shallow/proportion_sweep/main_0x10_k01_s01.py", line 14, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.17 | 1/6 | 2 | - | - | - | - | - | - | - | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x20_k01_s02.py` | artifact main_0x20_k01_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method_slots/shallow/proportion_sweep/main_0x20_k01_s02.py", line 14, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.33 | 2/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x22_k02_s01.py` | artifact main_0x22_k02_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method_slots/shallow/proportion_sweep/main_0x22_k02_s01.py", line 14, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.33 | 2/6 | 2 | - | - | - | - | - | - | - | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x5_k02_s02.py` | artifact main_0x5_k02_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method_slots/shallow/proportion_sweep/main_0x5_k02_s02.py", line 14, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.50 | 3/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0xb_k03_s01.py` | artifact main_0xb_k03_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method_slots/shallow/proportion_sweep/main_0xb_k03_s01.py", line 14, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.50 | 3/6 | 2 | - | - | - | - | - | - | - | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x13_k03_s02.py` | artifact main_0x13_k03_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method_slots/shallow/proportion_sweep/main_0x13_k03_s02.py", line 14, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.67 | 4/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0xf_k04_s01.py` | artifact main_0xf_k04_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method_slots/shallow/proportion_sweep/main_0xf_k04_s01.py", line 14, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.67 | 4/6 | 2 | - | - | - | - | - | - | - | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x39_k04_s02.py` | artifact main_0x39_k04_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method_slots/shallow/proportion_sweep/main_0x39_k04_s02.py", line 14, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.83 | 5/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x3e_k05_s01.py` | artifact main_0x3e_k05_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method_slots/shallow/proportion_sweep/main_0x3e_k05_s01.py", line 14, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.83 | 5/6 | 2 | - | - | - | - | - | - | - | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x3b_k05_s02.py` | artifact main_0x3b_k05_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method_slots/shallow/proportion_sweep/main_0x3b_k05_s02.py", line 14, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 1.00 | 6/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x3f_k06_s01.py` | artifact main_0x3f_k06_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_method_slots/shallow/proportion_sweep/main_0x3f_k06_s01.py", line 14, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |

## call_method_slots/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.1847s | 0.1847s | 0.1847s | 3.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.1847s | 0.0410s | 3 | 24 | yes | 0.1694s | 0.2014s | `static-python-perf/Benchmark/call_method_slots/untyped/main.py` |  |

## call_simple/advanced

- Detypable targets: `6`
- Total runs: `12`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 0 | - | - | - | - | - | 1 failed |
| 0.17 | 1/6 | 0 | - | - | - | - | - | 2 failed |
| 0.33 | 2/6 | 0 | - | - | - | - | - | 2 failed |
| 0.50 | 3/6 | 0 | - | - | - | - | - | 2 failed |
| 0.67 | 4/6 | 0 | - | - | - | - | - | 2 failed |
| 0.83 | 5/6 | 0 | - | - | - | - | - | 2 failed |
| 1.00 | 6/6 | 0 | - | - | - | - | - | 1 failed |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_simple/advanced/proportion_sweep/main_0x0_k00_s01.py` | artifact main_0x0_k00_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_simple/advanced/proportion_sweep/main_0x0_k00_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.17 | 1/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_simple/advanced/proportion_sweep/main_0x20_k01_s01.py` | artifact main_0x20_k01_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_simple/advanced/proportion_sweep/main_0x20_k01_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.17 | 1/6 | 2 | - | - | - | - | - | - | - | `detyped_files/call_simple/advanced/proportion_sweep/main_0x1_k01_s02.py` | artifact main_0x1_k01_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_simple/advanced/proportion_sweep/main_0x1_k01_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.33 | 2/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_simple/advanced/proportion_sweep/main_0x18_k02_s01.py` | artifact main_0x18_k02_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_simple/advanced/proportion_sweep/main_0x18_k02_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.33 | 2/6 | 2 | - | - | - | - | - | - | - | `detyped_files/call_simple/advanced/proportion_sweep/main_0x24_k02_s02.py` | artifact main_0x24_k02_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_simple/advanced/proportion_sweep/main_0x24_k02_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.50 | 3/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_simple/advanced/proportion_sweep/main_0x32_k03_s01.py` | artifact main_0x32_k03_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_simple/advanced/proportion_sweep/main_0x32_k03_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.50 | 3/6 | 2 | - | - | - | - | - | - | - | `detyped_files/call_simple/advanced/proportion_sweep/main_0x23_k03_s02.py` | artifact main_0x23_k03_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_simple/advanced/proportion_sweep/main_0x23_k03_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.67 | 4/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_simple/advanced/proportion_sweep/main_0x39_k04_s01.py` | artifact main_0x39_k04_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_simple/advanced/proportion_sweep/main_0x39_k04_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.67 | 4/6 | 2 | - | - | - | - | - | - | - | `detyped_files/call_simple/advanced/proportion_sweep/main_0x27_k04_s02.py` | artifact main_0x27_k04_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_simple/advanced/proportion_sweep/main_0x27_k04_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.83 | 5/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_simple/advanced/proportion_sweep/main_0x2f_k05_s01.py` | artifact main_0x2f_k05_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_simple/advanced/proportion_sweep/main_0x2f_k05_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.83 | 5/6 | 2 | - | - | - | - | - | - | - | `detyped_files/call_simple/advanced/proportion_sweep/main_0x37_k05_s02.py` | artifact main_0x37_k05_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_simple/advanced/proportion_sweep/main_0x37_k05_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 1.00 | 6/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_simple/advanced/proportion_sweep/main_0x3f_k06_s01.py` | artifact main_0x3f_k06_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_simple/advanced/proportion_sweep/main_0x3f_k06_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |

## call_simple/shallow

- Detypable targets: `6`
- Total runs: `12`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 0 | - | - | - | - | - | 1 failed |
| 0.17 | 1/6 | 0 | - | - | - | - | - | 2 failed |
| 0.33 | 2/6 | 0 | - | - | - | - | - | 2 failed |
| 0.50 | 3/6 | 0 | - | - | - | - | - | 2 failed |
| 0.67 | 4/6 | 0 | - | - | - | - | - | 2 failed |
| 0.83 | 5/6 | 0 | - | - | - | - | - | 2 failed |
| 1.00 | 6/6 | 0 | - | - | - | - | - | 1 failed |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_simple/shallow/proportion_sweep/main_0x0_k00_s01.py` | artifact main_0x0_k00_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_simple/shallow/proportion_sweep/main_0x0_k00_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.17 | 1/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_simple/shallow/proportion_sweep/main_0x1_k01_s01.py` | artifact main_0x1_k01_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_simple/shallow/proportion_sweep/main_0x1_k01_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.17 | 1/6 | 2 | - | - | - | - | - | - | - | `detyped_files/call_simple/shallow/proportion_sweep/main_0x20_k01_s02.py` | artifact main_0x20_k01_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_simple/shallow/proportion_sweep/main_0x20_k01_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.33 | 2/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_simple/shallow/proportion_sweep/main_0x21_k02_s01.py` | artifact main_0x21_k02_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_simple/shallow/proportion_sweep/main_0x21_k02_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.33 | 2/6 | 2 | - | - | - | - | - | - | - | `detyped_files/call_simple/shallow/proportion_sweep/main_0x6_k02_s02.py` | artifact main_0x6_k02_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_simple/shallow/proportion_sweep/main_0x6_k02_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.50 | 3/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_simple/shallow/proportion_sweep/main_0x2a_k03_s01.py` | artifact main_0x2a_k03_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_simple/shallow/proportion_sweep/main_0x2a_k03_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.50 | 3/6 | 2 | - | - | - | - | - | - | - | `detyped_files/call_simple/shallow/proportion_sweep/main_0x31_k03_s02.py` | artifact main_0x31_k03_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_simple/shallow/proportion_sweep/main_0x31_k03_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.67 | 4/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_simple/shallow/proportion_sweep/main_0x1b_k04_s01.py` | artifact main_0x1b_k04_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_simple/shallow/proportion_sweep/main_0x1b_k04_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.67 | 4/6 | 2 | - | - | - | - | - | - | - | `detyped_files/call_simple/shallow/proportion_sweep/main_0x36_k04_s02.py` | artifact main_0x36_k04_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_simple/shallow/proportion_sweep/main_0x36_k04_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.83 | 5/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_simple/shallow/proportion_sweep/main_0x37_k05_s01.py` | artifact main_0x37_k05_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_simple/shallow/proportion_sweep/main_0x37_k05_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.83 | 5/6 | 2 | - | - | - | - | - | - | - | `detyped_files/call_simple/shallow/proportion_sweep/main_0x3d_k05_s02.py` | artifact main_0x3d_k05_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_simple/shallow/proportion_sweep/main_0x3d_k05_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 1.00 | 6/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_simple/shallow/proportion_sweep/main_0x3f_k06_s01.py` | artifact main_0x3f_k06_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/call_simple/shallow/proportion_sweep/main_0x3f_k06_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |

## call_simple/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.1475s | 0.1475s | 0.1475s | 8.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.1475s | 0.0560s | 8 | 64 | yes | 0.1350s | 0.1619s | `static-python-perf/Benchmark/call_simple/untyped/main.py` |  |

## chaos/advanced

- Detypable targets: `5`
- Total runs: `10`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/5 | 0 | - | - | - | - | - | 1 failed |
| 0.20 | 1/5 | 0 | - | - | - | - | - | 2 failed |
| 0.40 | 2/5 | 0 | - | - | - | - | - | 2 failed |
| 0.60 | 3/5 | 0 | - | - | - | - | - | 2 failed |
| 0.80 | 4/5 | 0 | - | - | - | - | - | 2 failed |
| 1.00 | 5/5 | 0 | - | - | - | - | - | 1 failed |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/5 | 1 | - | - | - | - | - | - | - | `detyped_files/chaos/advanced/proportion_sweep/main_0x0_k00_s01.py` | artifact main_0x0_k00_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/chaos/advanced/proportion_sweep/main_0x0_k00_s01.py", line 25, in <module>
    from __static__ import CheckedList
ModuleNotFoundError: No module named '__static__' |
| 0.20 | 1/5 | 1 | - | - | - | - | - | - | - | `detyped_files/chaos/advanced/proportion_sweep/main_0x10_k01_s01.py` | artifact main_0x10_k01_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/chaos/advanced/proportion_sweep/main_0x10_k01_s01.py", line 25, in <module>
    from __static__ import CheckedList
ModuleNotFoundError: No module named '__static__' |
| 0.20 | 1/5 | 2 | - | - | - | - | - | - | - | `detyped_files/chaos/advanced/proportion_sweep/main_0x8_k01_s02.py` | artifact main_0x8_k01_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/chaos/advanced/proportion_sweep/main_0x8_k01_s02.py", line 25, in <module>
    from __static__ import CheckedList
ModuleNotFoundError: No module named '__static__' |
| 0.40 | 2/5 | 1 | - | - | - | - | - | - | - | `detyped_files/chaos/advanced/proportion_sweep/main_0xc_k02_s01.py` | artifact main_0xc_k02_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/chaos/advanced/proportion_sweep/main_0xc_k02_s01.py", line 25, in <module>
    from __static__ import CheckedList
ModuleNotFoundError: No module named '__static__' |
| 0.40 | 2/5 | 2 | - | - | - | - | - | - | - | `detyped_files/chaos/advanced/proportion_sweep/main_0x5_k02_s02.py` | artifact main_0x5_k02_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/chaos/advanced/proportion_sweep/main_0x5_k02_s02.py", line 25, in <module>
    from __static__ import CheckedList
ModuleNotFoundError: No module named '__static__' |
| 0.60 | 3/5 | 1 | - | - | - | - | - | - | - | `detyped_files/chaos/advanced/proportion_sweep/main_0x16_k03_s01.py` | artifact main_0x16_k03_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/chaos/advanced/proportion_sweep/main_0x16_k03_s01.py", line 25, in <module>
    from __static__ import CheckedList
ModuleNotFoundError: No module named '__static__' |
| 0.60 | 3/5 | 2 | - | - | - | - | - | - | - | `detyped_files/chaos/advanced/proportion_sweep/main_0x19_k03_s02.py` | artifact main_0x19_k03_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/chaos/advanced/proportion_sweep/main_0x19_k03_s02.py", line 25, in <module>
    from __static__ import CheckedList
ModuleNotFoundError: No module named '__static__' |
| 0.80 | 4/5 | 1 | - | - | - | - | - | - | - | `detyped_files/chaos/advanced/proportion_sweep/main_0xf_k04_s01.py` | artifact main_0xf_k04_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/chaos/advanced/proportion_sweep/main_0xf_k04_s01.py", line 25, in <module>
    from __static__ import CheckedList
ModuleNotFoundError: No module named '__static__' |
| 0.80 | 4/5 | 2 | - | - | - | - | - | - | - | `detyped_files/chaos/advanced/proportion_sweep/main_0x17_k04_s02.py` | artifact main_0x17_k04_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/chaos/advanced/proportion_sweep/main_0x17_k04_s02.py", line 25, in <module>
    from __static__ import CheckedList
ModuleNotFoundError: No module named '__static__' |
| 1.00 | 5/5 | 1 | - | - | - | - | - | - | - | `detyped_files/chaos/advanced/proportion_sweep/main_0x1f_k05_s01.py` | artifact main_0x1f_k05_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/chaos/advanced/proportion_sweep/main_0x1f_k05_s01.py", line 25, in <module>
    from __static__ import CheckedList
ModuleNotFoundError: No module named '__static__' |

## chaos/shallow

- Detypable targets: `5`
- Total runs: `10`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/5 | 0 | - | - | - | - | - | 1 failed |
| 0.20 | 1/5 | 0 | - | - | - | - | - | 2 failed |
| 0.40 | 2/5 | 0 | - | - | - | - | - | 2 failed |
| 0.60 | 3/5 | 0 | - | - | - | - | - | 2 failed |
| 0.80 | 4/5 | 0 | - | - | - | - | - | 2 failed |
| 1.00 | 5/5 | 0 | - | - | - | - | - | 1 failed |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/5 | 1 | - | - | - | - | - | - | - | `detyped_files/chaos/shallow/proportion_sweep/main_0x0_k00_s01.py` | artifact main_0x0_k00_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/chaos/shallow/proportion_sweep/main_0x0_k00_s01.py", line 5, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.20 | 1/5 | 1 | - | - | - | - | - | - | - | `detyped_files/chaos/shallow/proportion_sweep/main_0x2_k01_s01.py` | artifact main_0x2_k01_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/chaos/shallow/proportion_sweep/main_0x2_k01_s01.py", line 5, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.20 | 1/5 | 2 | - | - | - | - | - | - | - | `detyped_files/chaos/shallow/proportion_sweep/main_0x10_k01_s02.py` | artifact main_0x10_k01_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/chaos/shallow/proportion_sweep/main_0x10_k01_s02.py", line 5, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.40 | 2/5 | 1 | - | - | - | - | - | - | - | `detyped_files/chaos/shallow/proportion_sweep/main_0x14_k02_s01.py` | artifact main_0x14_k02_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/chaos/shallow/proportion_sweep/main_0x14_k02_s01.py", line 5, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.40 | 2/5 | 2 | - | - | - | - | - | - | - | `detyped_files/chaos/shallow/proportion_sweep/main_0x5_k02_s02.py` | artifact main_0x5_k02_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/chaos/shallow/proportion_sweep/main_0x5_k02_s02.py", line 5, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.60 | 3/5 | 1 | - | - | - | - | - | - | - | `detyped_files/chaos/shallow/proportion_sweep/main_0xb_k03_s01.py` | artifact main_0xb_k03_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/chaos/shallow/proportion_sweep/main_0xb_k03_s01.py", line 5, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.60 | 3/5 | 2 | - | - | - | - | - | - | - | `detyped_files/chaos/shallow/proportion_sweep/main_0x7_k03_s02.py` | artifact main_0x7_k03_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/chaos/shallow/proportion_sweep/main_0x7_k03_s02.py", line 5, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.80 | 4/5 | 1 | - | - | - | - | - | - | - | `detyped_files/chaos/shallow/proportion_sweep/main_0xf_k04_s01.py` | artifact main_0xf_k04_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/chaos/shallow/proportion_sweep/main_0xf_k04_s01.py", line 5, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.80 | 4/5 | 2 | - | - | - | - | - | - | - | `detyped_files/chaos/shallow/proportion_sweep/main_0x17_k04_s02.py` | artifact main_0x17_k04_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/chaos/shallow/proportion_sweep/main_0x17_k04_s02.py", line 5, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 1.00 | 5/5 | 1 | - | - | - | - | - | - | - | `detyped_files/chaos/shallow/proportion_sweep/main_0x1f_k05_s01.py` | artifact main_0x1f_k05_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/chaos/shallow/proportion_sweep/main_0x1f_k05_s01.py", line 5, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |

## chaos/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.1023s | 0.1023s | 0.1023s | 5.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.1023s | 0.0289s | 5 | 40 | yes | 0.0937s | 0.1116s | `static-python-perf/Benchmark/chaos/untyped/main.py` |  |
