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

## deltablue/advanced

- Detypable targets: `34`
- Total runs: `68`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/34 | 0 | - | - | - | - | - | 1 failed |
| 0.03 | 1/34 | 0 | - | - | - | - | - | 2 failed |
| 0.06 | 2/34 | 0 | - | - | - | - | - | 2 failed |
| 0.09 | 3/34 | 0 | - | - | - | - | - | 2 failed |
| 0.12 | 4/34 | 0 | - | - | - | - | - | 2 failed |
| 0.15 | 5/34 | 0 | - | - | - | - | - | 2 failed |
| 0.18 | 6/34 | 0 | - | - | - | - | - | 2 failed |
| 0.21 | 7/34 | 0 | - | - | - | - | - | 2 failed |
| 0.24 | 8/34 | 0 | - | - | - | - | - | 2 failed |
| 0.26 | 9/34 | 0 | - | - | - | - | - | 2 failed |
| 0.29 | 10/34 | 0 | - | - | - | - | - | 2 failed |
| 0.32 | 11/34 | 0 | - | - | - | - | - | 2 failed |
| 0.35 | 12/34 | 0 | - | - | - | - | - | 2 failed |
| 0.38 | 13/34 | 0 | - | - | - | - | - | 2 failed |
| 0.41 | 14/34 | 0 | - | - | - | - | - | 2 failed |
| 0.44 | 15/34 | 0 | - | - | - | - | - | 2 failed |
| 0.47 | 16/34 | 0 | - | - | - | - | - | 2 failed |
| 0.50 | 17/34 | 0 | - | - | - | - | - | 2 failed |
| 0.53 | 18/34 | 0 | - | - | - | - | - | 2 failed |
| 0.56 | 19/34 | 0 | - | - | - | - | - | 2 failed |
| 0.59 | 20/34 | 0 | - | - | - | - | - | 2 failed |
| 0.62 | 21/34 | 0 | - | - | - | - | - | 2 failed |
| 0.65 | 22/34 | 0 | - | - | - | - | - | 2 failed |
| 0.68 | 23/34 | 0 | - | - | - | - | - | 2 failed |
| 0.71 | 24/34 | 0 | - | - | - | - | - | 2 failed |
| 0.74 | 25/34 | 0 | - | - | - | - | - | 2 failed |
| 0.76 | 26/34 | 0 | - | - | - | - | - | 2 failed |
| 0.79 | 27/34 | 0 | - | - | - | - | - | 2 failed |
| 0.82 | 28/34 | 0 | - | - | - | - | - | 2 failed |
| 0.85 | 29/34 | 0 | - | - | - | - | - | 2 failed |
| 0.88 | 30/34 | 0 | - | - | - | - | - | 2 failed |
| 0.91 | 31/34 | 0 | - | - | - | - | - | 2 failed |
| 0.94 | 32/34 | 0 | - | - | - | - | - | 2 failed |
| 0.97 | 33/34 | 0 | - | - | - | - | - | 2 failed |
| 1.00 | 34/34 | 0 | - | - | - | - | - | 1 failed |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x0_k00_s01.py` | artifact main_0x0_k00_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x0_k00_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.03 | 1/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x200000000_k01_s01.py` | artifact main_0x200000000_k01_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x200000000_k01_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.03 | 1/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x200000_k01_s02.py` | artifact main_0x200000_k01_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x200000_k01_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.06 | 2/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x801000_k02_s01.py` | artifact main_0x801000_k02_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x801000_k02_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.06 | 2/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0xc0000_k02_s02.py` | artifact main_0xc0000_k02_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0xc0000_k02_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.09 | 3/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2a0_k03_s01.py` | artifact main_0x2a0_k03_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x2a0_k03_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.09 | 3/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x80000180_k03_s02.py` | artifact main_0x80000180_k03_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x80000180_k03_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.12 | 4/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0xa0800020_k04_s01.py` | artifact main_0xa0800020_k04_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0xa0800020_k04_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.12 | 4/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x820021_k04_s02.py` | artifact main_0x820021_k04_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x820021_k04_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.15 | 5/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x280006004_k05_s01.py` | artifact main_0x280006004_k05_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x280006004_k05_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.15 | 5/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x50200090_k05_s02.py` | artifact main_0x50200090_k05_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x50200090_k05_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.18 | 6/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x202101108_k06_s01.py` | artifact main_0x202101108_k06_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x202101108_k06_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.18 | 6/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x200102a02_k06_s02.py` | artifact main_0x200102a02_k06_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x200102a02_k06_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.21 | 7/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x248206002_k07_s01.py` | artifact main_0x248206002_k07_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x248206002_k07_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.21 | 7/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x40654040_k07_s02.py` | artifact main_0x40654040_k07_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x40654040_k07_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.24 | 8/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x150090130_k08_s01.py` | artifact main_0x150090130_k08_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x150090130_k08_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.24 | 8/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x262020842_k08_s02.py` | artifact main_0x262020842_k08_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x262020842_k08_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.26 | 9/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x82d19001_k09_s01.py` | artifact main_0x82d19001_k09_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x82d19001_k09_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.26 | 9/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x90512054_k09_s02.py` | artifact main_0x90512054_k09_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x90512054_k09_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.29 | 10/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x222d08290_k10_s01.py` | artifact main_0x222d08290_k10_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x222d08290_k10_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.29 | 10/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1b3409001_k10_s02.py` | artifact main_0x1b3409001_k10_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x1b3409001_k10_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.32 | 11/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x157068500_k11_s01.py` | artifact main_0x157068500_k11_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x157068500_k11_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.32 | 11/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x61954188_k11_s02.py` | artifact main_0x61954188_k11_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x61954188_k11_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.35 | 12/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x14194181b_k12_s01.py` | artifact main_0x14194181b_k12_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x14194181b_k12_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.35 | 12/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x8d802768_k12_s02.py` | artifact main_0x8d802768_k12_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x8d802768_k12_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.38 | 13/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2412f9a01_k13_s01.py` | artifact main_0x2412f9a01_k13_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x2412f9a01_k13_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.38 | 13/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x5e50824d_k13_s02.py` | artifact main_0x5e50824d_k13_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x5e50824d_k13_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.41 | 14/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x16a243626_k14_s01.py` | artifact main_0x16a243626_k14_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x16a243626_k14_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.41 | 14/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x696dc184_k14_s02.py` | artifact main_0x696dc184_k14_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x696dc184_k14_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.44 | 15/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x88571fd_k15_s01.py` | artifact main_0x88571fd_k15_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x88571fd_k15_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.44 | 15/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3228a5ce8_k15_s02.py` | artifact main_0x3228a5ce8_k15_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x3228a5ce8_k15_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.47 | 16/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3a58a83ac_k16_s01.py` | artifact main_0x3a58a83ac_k16_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x3a58a83ac_k16_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.47 | 16/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x181e2d9b8_k16_s02.py` | artifact main_0x181e2d9b8_k16_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x181e2d9b8_k16_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.50 | 17/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x21535e0f6_k17_s01.py` | artifact main_0x21535e0f6_k17_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x21535e0f6_k17_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.50 | 17/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1b7361ac2_k17_s02.py` | artifact main_0x1b7361ac2_k17_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x1b7361ac2_k17_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.53 | 18/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1e05cd8fa_k18_s01.py` | artifact main_0x1e05cd8fa_k18_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x1e05cd8fa_k18_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.53 | 18/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x368c5627d_k18_s02.py` | artifact main_0x368c5627d_k18_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x368c5627d_k18_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.56 | 19/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x165a87b6d_k19_s01.py` | artifact main_0x165a87b6d_k19_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x165a87b6d_k19_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.56 | 19/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x38a6c2b6f_k19_s02.py` | artifact main_0x38a6c2b6f_k19_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x38a6c2b6f_k19_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.59 | 20/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2f91a9ee5_k20_s01.py` | artifact main_0x2f91a9ee5_k20_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x2f91a9ee5_k20_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.59 | 20/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3d6d077d4_k20_s02.py` | artifact main_0x3d6d077d4_k20_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x3d6d077d4_k20_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.62 | 21/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x37d489d5f_k21_s01.py` | artifact main_0x37d489d5f_k21_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x37d489d5f_k21_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.62 | 21/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2dbc7eb51_k21_s02.py` | artifact main_0x2dbc7eb51_k21_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x2dbc7eb51_k21_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.65 | 22/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3bf7e721c_k22_s01.py` | artifact main_0x3bf7e721c_k22_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x3bf7e721c_k22_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.65 | 22/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3d5faa2f3_k22_s02.py` | artifact main_0x3d5faa2f3_k22_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x3d5faa2f3_k22_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.68 | 23/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x763dcbff_k23_s01.py` | artifact main_0x763dcbff_k23_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x763dcbff_k23_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.68 | 23/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2ebac7f9b_k23_s02.py` | artifact main_0x2ebac7f9b_k23_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x2ebac7f9b_k23_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.71 | 24/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3cf6dba7b_k24_s01.py` | artifact main_0x3cf6dba7b_k24_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x3cf6dba7b_k24_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.71 | 24/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1cfeb5ff2_k24_s02.py` | artifact main_0x1cfeb5ff2_k24_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x1cfeb5ff2_k24_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.74 | 25/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x17b7beaef_k25_s01.py` | artifact main_0x17b7beaef_k25_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x17b7beaef_k25_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.74 | 25/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x36ffe7e78_k25_s02.py` | artifact main_0x36ffe7e78_k25_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x36ffe7e78_k25_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.76 | 26/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3e2f37ffd_k26_s01.py` | artifact main_0x3e2f37ffd_k26_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x3e2f37ffd_k26_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.76 | 26/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0xfcbbbfef_k26_s02.py` | artifact main_0xfcbbbfef_k26_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0xfcbbbfef_k26_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.79 | 27/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1bf6feef7_k27_s01.py` | artifact main_0x1bf6feef7_k27_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x1bf6feef7_k27_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.79 | 27/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x37bf5ddfd_k27_s02.py` | artifact main_0x37bf5ddfd_k27_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x37bf5ddfd_k27_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.82 | 28/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3fafb77df_k28_s01.py` | artifact main_0x3fafb77df_k28_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x3fafb77df_k28_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.82 | 28/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3c5ffeffb_k28_s02.py` | artifact main_0x3c5ffeffb_k28_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x3c5ffeffb_k28_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.85 | 29/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x17ff7fbfd_k29_s01.py` | artifact main_0x17ff7fbfd_k29_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x17ff7fbfd_k29_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.85 | 29/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x37fb7fdbf_k29_s02.py` | artifact main_0x37fb7fdbf_k29_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x37fb7fdbf_k29_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.88 | 30/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3bfeffefd_k30_s01.py` | artifact main_0x3bfeffefd_k30_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x3bfeffefd_k30_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.88 | 30/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2fefff6ff_k30_s02.py` | artifact main_0x2fefff6ff_k30_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x2fefff6ff_k30_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.91 | 31/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3bffbfbff_k31_s01.py` | artifact main_0x3bffbfbff_k31_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x3bffbfbff_k31_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.91 | 31/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3ffffe77f_k31_s02.py` | artifact main_0x3ffffe77f_k31_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x3ffffe77f_k31_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.94 | 32/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3fff6ffff_k32_s01.py` | artifact main_0x3fff6ffff_k32_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x3fff6ffff_k32_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.94 | 32/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3fdffffbf_k32_s02.py` | artifact main_0x3fdffffbf_k32_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x3fdffffbf_k32_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.97 | 33/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3ffefffff_k33_s01.py` | artifact main_0x3ffefffff_k33_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x3ffefffff_k33_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.97 | 33/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3fffffeff_k33_s02.py` | artifact main_0x3fffffeff_k33_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x3fffffeff_k33_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 1.00 | 34/34 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3ffffffff_k34_s01.py` | artifact main_0x3ffffffff_k34_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/advanced/proportion_sweep/main_0x3ffffffff_k34_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |

## deltablue/shallow

- Detypable targets: `35`
- Total runs: `70`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/35 | 0 | - | - | - | - | - | 1 failed |
| 0.03 | 1/35 | 0 | - | - | - | - | - | 2 failed |
| 0.06 | 2/35 | 0 | - | - | - | - | - | 2 failed |
| 0.09 | 3/35 | 0 | - | - | - | - | - | 2 failed |
| 0.11 | 4/35 | 0 | - | - | - | - | - | 2 failed |
| 0.14 | 5/35 | 0 | - | - | - | - | - | 2 failed |
| 0.17 | 6/35 | 0 | - | - | - | - | - | 2 failed |
| 0.20 | 7/35 | 0 | - | - | - | - | - | 2 failed |
| 0.23 | 8/35 | 0 | - | - | - | - | - | 2 failed |
| 0.26 | 9/35 | 0 | - | - | - | - | - | 2 failed |
| 0.29 | 10/35 | 0 | - | - | - | - | - | 2 failed |
| 0.31 | 11/35 | 0 | - | - | - | - | - | 2 failed |
| 0.34 | 12/35 | 0 | - | - | - | - | - | 2 failed |
| 0.37 | 13/35 | 0 | - | - | - | - | - | 2 failed |
| 0.40 | 14/35 | 0 | - | - | - | - | - | 2 failed |
| 0.43 | 15/35 | 0 | - | - | - | - | - | 2 failed |
| 0.46 | 16/35 | 0 | - | - | - | - | - | 2 failed |
| 0.49 | 17/35 | 0 | - | - | - | - | - | 2 failed |
| 0.51 | 18/35 | 0 | - | - | - | - | - | 2 failed |
| 0.54 | 19/35 | 0 | - | - | - | - | - | 2 failed |
| 0.57 | 20/35 | 0 | - | - | - | - | - | 2 failed |
| 0.60 | 21/35 | 0 | - | - | - | - | - | 2 failed |
| 0.63 | 22/35 | 0 | - | - | - | - | - | 2 failed |
| 0.66 | 23/35 | 0 | - | - | - | - | - | 2 failed |
| 0.69 | 24/35 | 0 | - | - | - | - | - | 2 failed |
| 0.71 | 25/35 | 0 | - | - | - | - | - | 2 failed |
| 0.74 | 26/35 | 0 | - | - | - | - | - | 2 failed |
| 0.77 | 27/35 | 0 | - | - | - | - | - | 2 failed |
| 0.80 | 28/35 | 0 | - | - | - | - | - | 2 failed |
| 0.83 | 29/35 | 0 | - | - | - | - | - | 2 failed |
| 0.86 | 30/35 | 0 | - | - | - | - | - | 2 failed |
| 0.89 | 31/35 | 0 | - | - | - | - | - | 2 failed |
| 0.91 | 32/35 | 0 | - | - | - | - | - | 2 failed |
| 0.94 | 33/35 | 0 | - | - | - | - | - | 2 failed |
| 0.97 | 34/35 | 0 | - | - | - | - | - | 2 failed |
| 1.00 | 35/35 | 0 | - | - | - | - | - | 1 failed |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x0_k00_s01.py` | artifact main_0x0_k00_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x0_k00_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.03 | 1/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x40000000_k01_s01.py` | artifact main_0x40000000_k01_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x40000000_k01_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.03 | 1/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x80_k01_s02.py` | artifact main_0x80_k01_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x80_k01_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.06 | 2/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x820000_k02_s01.py` | artifact main_0x820000_k02_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x820000_k02_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.06 | 2/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x1000002_k02_s02.py` | artifact main_0x1000002_k02_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x1000002_k02_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.09 | 3/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x49000000_k03_s01.py` | artifact main_0x49000000_k03_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x49000000_k03_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.09 | 3/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x405_k03_s02.py` | artifact main_0x405_k03_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x405_k03_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.11 | 4/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x38080_k04_s01.py` | artifact main_0x38080_k04_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x38080_k04_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.11 | 4/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x400060080_k04_s02.py` | artifact main_0x400060080_k04_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x400060080_k04_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.14 | 5/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x406003_k05_s01.py` | artifact main_0x406003_k05_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x406003_k05_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.14 | 5/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x402000484_k05_s02.py` | artifact main_0x402000484_k05_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x402000484_k05_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.17 | 6/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x10000c920_k06_s01.py` | artifact main_0x10000c920_k06_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x10000c920_k06_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.17 | 6/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x211102800_k06_s02.py` | artifact main_0x211102800_k06_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x211102800_k06_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.20 | 7/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x208091048_k07_s01.py` | artifact main_0x208091048_k07_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x208091048_k07_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.20 | 7/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x48930100_k07_s02.py` | artifact main_0x48930100_k07_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x48930100_k07_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.23 | 8/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x130700044_k08_s01.py` | artifact main_0x130700044_k08_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x130700044_k08_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.23 | 8/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x8606e0_k08_s02.py` | artifact main_0x8606e0_k08_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x8606e0_k08_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.26 | 9/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x63408c400_k09_s01.py` | artifact main_0x63408c400_k09_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x63408c400_k09_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.26 | 9/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x2000117c2_k09_s02.py` | artifact main_0x2000117c2_k09_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x2000117c2_k09_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.29 | 10/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x4054e1120_k10_s01.py` | artifact main_0x4054e1120_k10_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x4054e1120_k10_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.29 | 10/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x5b480100a_k10_s02.py` | artifact main_0x5b480100a_k10_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x5b480100a_k10_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.31 | 11/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x5414041b1_k11_s01.py` | artifact main_0x5414041b1_k11_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x5414041b1_k11_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.31 | 11/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x26246018c_k11_s02.py` | artifact main_0x26246018c_k11_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x26246018c_k11_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.34 | 12/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x124425954_k12_s01.py` | artifact main_0x124425954_k12_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x124425954_k12_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.34 | 12/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x35801723_k12_s02.py` | artifact main_0x35801723_k12_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x35801723_k12_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.37 | 13/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x262174461_k13_s01.py` | artifact main_0x262174461_k13_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x262174461_k13_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.37 | 13/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x17814c285_k13_s02.py` | artifact main_0x17814c285_k13_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x17814c285_k13_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.40 | 14/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x585262538_k14_s01.py` | artifact main_0x585262538_k14_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x585262538_k14_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.40 | 14/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x4e18475c0_k14_s02.py` | artifact main_0x4e18475c0_k14_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x4e18475c0_k14_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.43 | 15/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x226e0f09a_k15_s01.py` | artifact main_0x226e0f09a_k15_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x226e0f09a_k15_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.43 | 15/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0xc6b1a568_k15_s02.py` | artifact main_0xc6b1a568_k15_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0xc6b1a568_k15_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.46 | 16/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7b0c485a5_k16_s01.py` | artifact main_0x7b0c485a5_k16_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x7b0c485a5_k16_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.46 | 16/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7844e40af_k16_s02.py` | artifact main_0x7844e40af_k16_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x7844e40af_k16_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.49 | 17/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x673467238_k17_s01.py` | artifact main_0x673467238_k17_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x673467238_k17_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.49 | 17/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x60bc8e0fa_k17_s02.py` | artifact main_0x60bc8e0fa_k17_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x60bc8e0fa_k17_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.51 | 18/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x469f96453_k18_s01.py` | artifact main_0x469f96453_k18_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x469f96453_k18_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.51 | 18/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x6c3c5c738_k18_s02.py` | artifact main_0x6c3c5c738_k18_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x6c3c5c738_k18_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.54 | 19/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x1d0ef23f4_k19_s01.py` | artifact main_0x1d0ef23f4_k19_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x1d0ef23f4_k19_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.54 | 19/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x50cdf5533_k19_s02.py` | artifact main_0x50cdf5533_k19_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x50cdf5533_k19_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.57 | 20/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7c07af3ca_k20_s01.py` | artifact main_0x7c07af3ca_k20_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x7c07af3ca_k20_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.57 | 20/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x2f3ad363a_k20_s02.py` | artifact main_0x2f3ad363a_k20_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x2f3ad363a_k20_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.60 | 21/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x2d6e763d6_k21_s01.py` | artifact main_0x2d6e763d6_k21_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x2d6e763d6_k21_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.60 | 21/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x371737799_k21_s02.py` | artifact main_0x371737799_k21_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x371737799_k21_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.63 | 22/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x2a7b6b9fc_k22_s01.py` | artifact main_0x2a7b6b9fc_k22_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x2a7b6b9fc_k22_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.63 | 22/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x4c2ecd5ff_k22_s02.py` | artifact main_0x4c2ecd5ff_k22_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x4c2ecd5ff_k22_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.66 | 23/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7adfab956_k23_s01.py` | artifact main_0x7adfab956_k23_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x7adfab956_k23_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.66 | 23/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x57f74e997_k23_s02.py` | artifact main_0x57f74e997_k23_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x57f74e997_k23_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.69 | 24/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x3ad5efec7_k24_s01.py` | artifact main_0x3ad5efec7_k24_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x3ad5efec7_k24_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.69 | 24/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x5cfeb8a7f_k24_s02.py` | artifact main_0x5cfeb8a7f_k24_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x5cfeb8a7f_k24_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.71 | 25/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x5cddfbdd6_k25_s01.py` | artifact main_0x5cddfbdd6_k25_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x5cddfbdd6_k25_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.71 | 25/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x57bfdd2fc_k25_s02.py` | artifact main_0x57bfdd2fc_k25_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x57bfdd2fc_k25_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.74 | 26/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x3eefc57ef_k26_s01.py` | artifact main_0x3eefc57ef_k26_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x3eefc57ef_k26_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.74 | 26/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x6afddf79d_k26_s02.py` | artifact main_0x6afddf79d_k26_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x6afddf79d_k26_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.77 | 27/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7bdbb6edf_k27_s01.py` | artifact main_0x7bdbb6edf_k27_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x7bdbb6edf_k27_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.77 | 27/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x57a6fddff_k27_s02.py` | artifact main_0x57a6fddff_k27_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x57a6fddff_k27_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.80 | 28/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7dfefb9bb_k28_s01.py` | artifact main_0x7dfefb9bb_k28_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x7dfefb9bb_k28_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.80 | 28/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x55dffb77f_k28_s02.py` | artifact main_0x55dffb77f_k28_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x55dffb77f_k28_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.83 | 29/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x5fafdf3ff_k29_s01.py` | artifact main_0x5fafdf3ff_k29_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x5fafdf3ff_k29_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.83 | 29/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x6fbf777bf_k29_s02.py` | artifact main_0x6fbf777bf_k29_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x6fbf777bf_k29_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.86 | 30/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7fffffd2d_k30_s01.py` | artifact main_0x7fffffd2d_k30_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x7fffffd2d_k30_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.86 | 30/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7fef7feee_k30_s02.py` | artifact main_0x7fef7feee_k30_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x7fef7feee_k30_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.89 | 31/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x57fffafff_k31_s01.py` | artifact main_0x57fffafff_k31_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x57fffafff_k31_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.89 | 31/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x77fdfdeff_k31_s02.py` | artifact main_0x77fdfdeff_k31_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x77fdfdeff_k31_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.91 | 32/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7fffedfbf_k32_s01.py` | artifact main_0x7fffedfbf_k32_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x7fffedfbf_k32_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.91 | 32/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x3ffffddff_k32_s02.py` | artifact main_0x3ffffddff_k32_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x3ffffddff_k32_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.94 | 33/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7ffffd7ff_k33_s01.py` | artifact main_0x7ffffd7ff_k33_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x7ffffd7ff_k33_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.94 | 33/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7ffbffffd_k33_s02.py` | artifact main_0x7ffbffffd_k33_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x7ffbffffd_k33_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.97 | 34/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7fffffeff_k34_s01.py` | artifact main_0x7fffffeff_k34_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x7fffffeff_k34_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.97 | 34/35 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x5ffffffff_k34_s02.py` | artifact main_0x5ffffffff_k34_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x5ffffffff_k34_s02.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 1.00 | 35/35 | 1 | - | - | - | - | - | - | - | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7ffffffff_k35_s01.py` | artifact main_0x7ffffffff_k35_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/deltablue/shallow/proportion_sweep/main_0x7ffffffff_k35_s01.py", line 21, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |

## deltablue/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.5681s | 0.5681s | 0.5681s | 2.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.5681s | 0.1070s | 2 | 16 | yes | 0.5185s | 0.6209s | `static-python-perf/Benchmark/deltablue/untyped/main.py` |  |

## fannkuch/advanced

- Detypable targets: `1`
- Total runs: `2`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/1 | 0 | - | - | - | - | - | 1 failed |
| 1.00 | 1/1 | 0 | - | - | - | - | - | 1 failed |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/1 | 1 | - | - | - | - | - | - | - | `detyped_files/fannkuch/advanced/proportion_sweep/main_0x0_k00_s01.py` | artifact main_0x0_k00_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/fannkuch/advanced/proportion_sweep/main_0x0_k00_s01.py", line 7, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 1.00 | 1/1 | 1 | - | - | - | - | - | - | - | `detyped_files/fannkuch/advanced/proportion_sweep/main_0x1_k01_s01.py` | artifact main_0x1_k01_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/fannkuch/advanced/proportion_sweep/main_0x1_k01_s01.py", line 7, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |

## fannkuch/shallow

- Detypable targets: `1`
- Total runs: `2`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/1 | 0 | - | - | - | - | - | 1 failed |
| 1.00 | 1/1 | 0 | - | - | - | - | - | 1 failed |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/1 | 1 | - | - | - | - | - | - | - | `detyped_files/fannkuch/shallow/proportion_sweep/main_0x0_k00_s01.py` | artifact main_0x0_k00_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/fannkuch/shallow/proportion_sweep/main_0x0_k00_s01.py", line 7, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 1.00 | 1/1 | 1 | - | - | - | - | - | - | - | `detyped_files/fannkuch/shallow/proportion_sweep/main_0x1_k01_s01.py` | artifact main_0x1_k01_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/fannkuch/shallow/proportion_sweep/main_0x1_k01_s01.py", line 7, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |

## fannkuch/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.4899s | 0.4899s | 0.4899s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.4899s | 0.0505s | 1 | 8 | yes | 0.4587s | 0.5229s | `static-python-perf/Benchmark/fannkuch/untyped/main.py` |  |

## float/advanced

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
| 0.00 | 0/5 | 1 | - | - | - | - | - | - | - | `detyped_files/float/advanced/proportion_sweep/main_0x0_k00_s01.py` | artifact main_0x0_k00_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/float/advanced/proportion_sweep/main_0x0_k00_s01.py", line 3, in <module>
    from __static__ import CheckedList, inline
ModuleNotFoundError: No module named '__static__' |
| 0.20 | 1/5 | 1 | - | - | - | - | - | - | - | `detyped_files/float/advanced/proportion_sweep/main_0x2_k01_s01.py` | artifact main_0x2_k01_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/float/advanced/proportion_sweep/main_0x2_k01_s01.py", line 3, in <module>
    from __static__ import CheckedList, inline
ModuleNotFoundError: No module named '__static__' |
| 0.20 | 1/5 | 2 | - | - | - | - | - | - | - | `detyped_files/float/advanced/proportion_sweep/main_0x8_k01_s02.py` | artifact main_0x8_k01_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/float/advanced/proportion_sweep/main_0x8_k01_s02.py", line 3, in <module>
    from __static__ import CheckedList, inline
ModuleNotFoundError: No module named '__static__' |
| 0.40 | 2/5 | 1 | - | - | - | - | - | - | - | `detyped_files/float/advanced/proportion_sweep/main_0x3_k02_s01.py` | artifact main_0x3_k02_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/float/advanced/proportion_sweep/main_0x3_k02_s01.py", line 3, in <module>
    from __static__ import CheckedList, inline
ModuleNotFoundError: No module named '__static__' |
| 0.40 | 2/5 | 2 | - | - | - | - | - | - | - | `detyped_files/float/advanced/proportion_sweep/main_0xa_k02_s02.py` | artifact main_0xa_k02_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/float/advanced/proportion_sweep/main_0xa_k02_s02.py", line 3, in <module>
    from __static__ import CheckedList, inline
ModuleNotFoundError: No module named '__static__' |
| 0.60 | 3/5 | 1 | - | - | - | - | - | - | - | `detyped_files/float/advanced/proportion_sweep/main_0x13_k03_s01.py` | artifact main_0x13_k03_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/float/advanced/proportion_sweep/main_0x13_k03_s01.py", line 3, in <module>
    from __static__ import CheckedList, inline
ModuleNotFoundError: No module named '__static__' |
| 0.60 | 3/5 | 2 | - | - | - | - | - | - | - | `detyped_files/float/advanced/proportion_sweep/main_0x1c_k03_s02.py` | artifact main_0x1c_k03_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/float/advanced/proportion_sweep/main_0x1c_k03_s02.py", line 3, in <module>
    from __static__ import CheckedList, inline
ModuleNotFoundError: No module named '__static__' |
| 0.80 | 4/5 | 1 | - | - | - | - | - | - | - | `detyped_files/float/advanced/proportion_sweep/main_0x17_k04_s01.py` | artifact main_0x17_k04_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/float/advanced/proportion_sweep/main_0x17_k04_s01.py", line 3, in <module>
    from __static__ import CheckedList, inline
ModuleNotFoundError: No module named '__static__' |
| 0.80 | 4/5 | 2 | - | - | - | - | - | - | - | `detyped_files/float/advanced/proportion_sweep/main_0xf_k04_s02.py` | artifact main_0xf_k04_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/float/advanced/proportion_sweep/main_0xf_k04_s02.py", line 3, in <module>
    from __static__ import CheckedList, inline
ModuleNotFoundError: No module named '__static__' |
| 1.00 | 5/5 | 1 | - | - | - | - | - | - | - | `detyped_files/float/advanced/proportion_sweep/main_0x1f_k05_s01.py` | artifact main_0x1f_k05_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/float/advanced/proportion_sweep/main_0x1f_k05_s01.py", line 3, in <module>
    from __static__ import CheckedList, inline
ModuleNotFoundError: No module named '__static__' |

## float/shallow

- Detypable targets: `3`
- Total runs: `6`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/3 | 1 | 0.1787s | 0.1787s | 0.1787s | 1.0 | yes | ok |
| 0.33 | 1/3 | 0 | - | - | - | - | - | 2 failed |
| 0.67 | 2/3 | 0 | - | - | - | - | - | 2 failed |
| 1.00 | 3/3 | 0 | - | - | - | - | - | 1 failed |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/3 | 1 | 0.1787s | 0.0197s | 1 | 8 | yes | 0.1670s | 0.1923s | `detyped_files/float/shallow/proportion_sweep/main_0x0_k00_s01.py` |  |
| 0.33 | 1/3 | 1 | - | - | - | - | - | - | - | `detyped_files/float/shallow/proportion_sweep/main_0x2_k01_s01.py` | artifact main_0x2_k01_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/float/shallow/proportion_sweep/main_0x2_k01_s01.py", line 5, in <module>
    from __static__ import cast
ModuleNotFoundError: No module named '__static__' |
| 0.33 | 1/3 | 2 | - | - | - | - | - | - | - | `detyped_files/float/shallow/proportion_sweep/main_0x1_k01_s02.py` | artifact main_0x1_k01_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/float/shallow/proportion_sweep/main_0x1_k01_s02.py", line 5, in <module>
    from __static__ import cast
ModuleNotFoundError: No module named '__static__' |
| 0.67 | 2/3 | 1 | - | - | - | - | - | - | - | `detyped_files/float/shallow/proportion_sweep/main_0x3_k02_s01.py` | artifact main_0x3_k02_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/float/shallow/proportion_sweep/main_0x3_k02_s01.py", line 5, in <module>
    from __static__ import cast
ModuleNotFoundError: No module named '__static__' |
| 0.67 | 2/3 | 2 | - | - | - | - | - | - | - | `detyped_files/float/shallow/proportion_sweep/main_0x5_k02_s02.py` | artifact main_0x5_k02_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/float/shallow/proportion_sweep/main_0x5_k02_s02.py", line 5, in <module>
    from __static__ import cast
ModuleNotFoundError: No module named '__static__' |
| 1.00 | 3/3 | 1 | - | - | - | - | - | - | - | `detyped_files/float/shallow/proportion_sweep/main_0x7_k03_s01.py` | artifact main_0x7_k03_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/float/shallow/proportion_sweep/main_0x7_k03_s01.py", line 5, in <module>
    from __static__ import cast
ModuleNotFoundError: No module named '__static__' |

## float/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.2123s | 0.2123s | 0.2123s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.2123s | 0.0242s | 1 | 8 | yes | 0.1961s | 0.2278s | `static-python-perf/Benchmark/float/untyped/main.py` |  |

## nbody/advanced

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
| 0.00 | 0/6 | 1 | - | - | - | - | - | - | - | `detyped_files/nbody/advanced/proportion_sweep/main_0x0_k00_s01.py` | artifact main_0x0_k00_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nbody/advanced/proportion_sweep/main_0x0_k00_s01.py", line 16, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.17 | 1/6 | 1 | - | - | - | - | - | - | - | `detyped_files/nbody/advanced/proportion_sweep/main_0x10_k01_s01.py` | artifact main_0x10_k01_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nbody/advanced/proportion_sweep/main_0x10_k01_s01.py", line 16, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.17 | 1/6 | 2 | - | - | - | - | - | - | - | `detyped_files/nbody/advanced/proportion_sweep/main_0x2_k01_s02.py` | artifact main_0x2_k01_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nbody/advanced/proportion_sweep/main_0x2_k01_s02.py", line 16, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.33 | 2/6 | 1 | - | - | - | - | - | - | - | `detyped_files/nbody/advanced/proportion_sweep/main_0x11_k02_s01.py` | artifact main_0x11_k02_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nbody/advanced/proportion_sweep/main_0x11_k02_s01.py", line 16, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.33 | 2/6 | 2 | - | - | - | - | - | - | - | `detyped_files/nbody/advanced/proportion_sweep/main_0x21_k02_s02.py` | artifact main_0x21_k02_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nbody/advanced/proportion_sweep/main_0x21_k02_s02.py", line 16, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.50 | 3/6 | 1 | - | - | - | - | - | - | - | `detyped_files/nbody/advanced/proportion_sweep/main_0x26_k03_s01.py` | artifact main_0x26_k03_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nbody/advanced/proportion_sweep/main_0x26_k03_s01.py", line 16, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.50 | 3/6 | 2 | - | - | - | - | - | - | - | `detyped_files/nbody/advanced/proportion_sweep/main_0x15_k03_s02.py` | artifact main_0x15_k03_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nbody/advanced/proportion_sweep/main_0x15_k03_s02.py", line 16, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.67 | 4/6 | 1 | - | - | - | - | - | - | - | `detyped_files/nbody/advanced/proportion_sweep/main_0x2b_k04_s01.py` | artifact main_0x2b_k04_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nbody/advanced/proportion_sweep/main_0x2b_k04_s01.py", line 16, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.67 | 4/6 | 2 | - | - | - | - | - | - | - | `detyped_files/nbody/advanced/proportion_sweep/main_0x1e_k04_s02.py` | artifact main_0x1e_k04_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nbody/advanced/proportion_sweep/main_0x1e_k04_s02.py", line 16, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.83 | 5/6 | 1 | - | - | - | - | - | - | - | `detyped_files/nbody/advanced/proportion_sweep/main_0x1f_k05_s01.py` | artifact main_0x1f_k05_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nbody/advanced/proportion_sweep/main_0x1f_k05_s01.py", line 16, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.83 | 5/6 | 2 | - | - | - | - | - | - | - | `detyped_files/nbody/advanced/proportion_sweep/main_0x3e_k05_s02.py` | artifact main_0x3e_k05_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nbody/advanced/proportion_sweep/main_0x3e_k05_s02.py", line 16, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 1.00 | 6/6 | 1 | - | - | - | - | - | - | - | `detyped_files/nbody/advanced/proportion_sweep/main_0x3f_k06_s01.py` | artifact main_0x3f_k06_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nbody/advanced/proportion_sweep/main_0x3f_k06_s01.py", line 16, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |

## nbody/shallow

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
| 0.00 | 0/6 | 1 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0x0_k00_s01.py` | artifact main_0x0_k00_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nbody/shallow/proportion_sweep/main_0x0_k00_s01.py", line 16, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.17 | 1/6 | 1 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0x2_k01_s01.py` | artifact main_0x2_k01_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nbody/shallow/proportion_sweep/main_0x2_k01_s01.py", line 16, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.17 | 1/6 | 2 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0x4_k01_s02.py` | artifact main_0x4_k01_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nbody/shallow/proportion_sweep/main_0x4_k01_s02.py", line 16, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.33 | 2/6 | 1 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0xc_k02_s01.py` | artifact main_0xc_k02_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nbody/shallow/proportion_sweep/main_0xc_k02_s01.py", line 16, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.33 | 2/6 | 2 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0x14_k02_s02.py` | artifact main_0x14_k02_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nbody/shallow/proportion_sweep/main_0x14_k02_s02.py", line 16, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.50 | 3/6 | 1 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0xb_k03_s01.py` | artifact main_0xb_k03_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nbody/shallow/proportion_sweep/main_0xb_k03_s01.py", line 16, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.50 | 3/6 | 2 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0x7_k03_s02.py` | artifact main_0x7_k03_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nbody/shallow/proportion_sweep/main_0x7_k03_s02.py", line 16, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.67 | 4/6 | 1 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0xf_k04_s01.py` | artifact main_0xf_k04_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nbody/shallow/proportion_sweep/main_0xf_k04_s01.py", line 16, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.67 | 4/6 | 2 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0x3a_k04_s02.py` | artifact main_0x3a_k04_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nbody/shallow/proportion_sweep/main_0x3a_k04_s02.py", line 16, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.83 | 5/6 | 1 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0x3d_k05_s01.py` | artifact main_0x3d_k05_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nbody/shallow/proportion_sweep/main_0x3d_k05_s01.py", line 16, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.83 | 5/6 | 2 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0x1f_k05_s02.py` | artifact main_0x1f_k05_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nbody/shallow/proportion_sweep/main_0x1f_k05_s02.py", line 16, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 1.00 | 6/6 | 1 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0x3f_k06_s01.py` | artifact main_0x3f_k06_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nbody/shallow/proportion_sweep/main_0x3f_k06_s01.py", line 16, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |

## nbody/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 1.1561s | 1.1561s | 1.1561s | 2.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 1.1561s | 0.2017s | 2 | 16 | yes | 1.0588s | 1.2489s | `static-python-perf/Benchmark/nbody/untyped/main.py` |  |

## nqueens/advanced

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
| 0.00 | 0/5 | 1 | - | - | - | - | - | - | - | `detyped_files/nqueens/advanced/proportion_sweep/main_0x0_k00_s01.py` | artifact main_0x0_k00_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nqueens/advanced/proportion_sweep/main_0x0_k00_s01.py", line 6, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.20 | 1/5 | 1 | - | - | - | - | - | - | - | `detyped_files/nqueens/advanced/proportion_sweep/main_0x2_k01_s01.py` | artifact main_0x2_k01_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nqueens/advanced/proportion_sweep/main_0x2_k01_s01.py", line 6, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.20 | 1/5 | 2 | - | - | - | - | - | - | - | `detyped_files/nqueens/advanced/proportion_sweep/main_0x4_k01_s02.py` | artifact main_0x4_k01_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nqueens/advanced/proportion_sweep/main_0x4_k01_s02.py", line 6, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.40 | 2/5 | 1 | - | - | - | - | - | - | - | `detyped_files/nqueens/advanced/proportion_sweep/main_0x12_k02_s01.py` | artifact main_0x12_k02_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nqueens/advanced/proportion_sweep/main_0x12_k02_s01.py", line 6, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.40 | 2/5 | 2 | - | - | - | - | - | - | - | `detyped_files/nqueens/advanced/proportion_sweep/main_0xc_k02_s02.py` | artifact main_0xc_k02_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nqueens/advanced/proportion_sweep/main_0xc_k02_s02.py", line 6, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.60 | 3/5 | 1 | - | - | - | - | - | - | - | `detyped_files/nqueens/advanced/proportion_sweep/main_0x13_k03_s01.py` | artifact main_0x13_k03_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nqueens/advanced/proportion_sweep/main_0x13_k03_s01.py", line 6, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.60 | 3/5 | 2 | - | - | - | - | - | - | - | `detyped_files/nqueens/advanced/proportion_sweep/main_0x19_k03_s02.py` | artifact main_0x19_k03_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nqueens/advanced/proportion_sweep/main_0x19_k03_s02.py", line 6, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.80 | 4/5 | 1 | - | - | - | - | - | - | - | `detyped_files/nqueens/advanced/proportion_sweep/main_0x1d_k04_s01.py` | artifact main_0x1d_k04_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nqueens/advanced/proportion_sweep/main_0x1d_k04_s01.py", line 6, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.80 | 4/5 | 2 | - | - | - | - | - | - | - | `detyped_files/nqueens/advanced/proportion_sweep/main_0x17_k04_s02.py` | artifact main_0x17_k04_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nqueens/advanced/proportion_sweep/main_0x17_k04_s02.py", line 6, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 1.00 | 5/5 | 1 | - | - | - | - | - | - | - | `detyped_files/nqueens/advanced/proportion_sweep/main_0x1f_k05_s01.py` | artifact main_0x1f_k05_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nqueens/advanced/proportion_sweep/main_0x1f_k05_s01.py", line 6, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |

## nqueens/shallow

- Detypable targets: `3`
- Total runs: `6`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/3 | 0 | - | - | - | - | - | 1 failed |
| 0.33 | 1/3 | 0 | - | - | - | - | - | 2 failed |
| 0.67 | 2/3 | 0 | - | - | - | - | - | 2 failed |
| 1.00 | 3/3 | 0 | - | - | - | - | - | 1 failed |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/3 | 1 | - | - | - | - | - | - | - | `detyped_files/nqueens/shallow/proportion_sweep/main_0x0_k00_s01.py` | artifact main_0x0_k00_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nqueens/shallow/proportion_sweep/main_0x0_k00_s01.py", line 6, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.33 | 1/3 | 1 | - | - | - | - | - | - | - | `detyped_files/nqueens/shallow/proportion_sweep/main_0x4_k01_s01.py` | artifact main_0x4_k01_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nqueens/shallow/proportion_sweep/main_0x4_k01_s01.py", line 6, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.33 | 1/3 | 2 | - | - | - | - | - | - | - | `detyped_files/nqueens/shallow/proportion_sweep/main_0x1_k01_s02.py` | artifact main_0x1_k01_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nqueens/shallow/proportion_sweep/main_0x1_k01_s02.py", line 6, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.67 | 2/3 | 1 | - | - | - | - | - | - | - | `detyped_files/nqueens/shallow/proportion_sweep/main_0x6_k02_s01.py` | artifact main_0x6_k02_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nqueens/shallow/proportion_sweep/main_0x6_k02_s01.py", line 6, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.67 | 2/3 | 2 | - | - | - | - | - | - | - | `detyped_files/nqueens/shallow/proportion_sweep/main_0x3_k02_s02.py` | artifact main_0x3_k02_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nqueens/shallow/proportion_sweep/main_0x3_k02_s02.py", line 6, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 1.00 | 3/3 | 1 | - | - | - | - | - | - | - | `detyped_files/nqueens/shallow/proportion_sweep/main_0x7_k03_s01.py` | artifact main_0x7_k03_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/nqueens/shallow/proportion_sweep/main_0x7_k03_s01.py", line 6, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |

## nqueens/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.1147s | 0.1147s | 0.1147s | 2.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.1147s | 0.0202s | 2 | 16 | yes | 0.1050s | 0.1243s | `static-python-perf/Benchmark/nqueens/untyped/main.py` |  |

## pystone/advanced

- Detypable targets: `15`
- Total runs: `30`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/15 | 0 | - | - | - | - | - | 1 failed |
| 0.07 | 1/15 | 0 | - | - | - | - | - | 2 failed |
| 0.13 | 2/15 | 0 | - | - | - | - | - | 2 failed |
| 0.20 | 3/15 | 0 | - | - | - | - | - | 2 failed |
| 0.27 | 4/15 | 0 | - | - | - | - | - | 2 failed |
| 0.33 | 5/15 | 0 | - | - | - | - | - | 2 failed |
| 0.40 | 6/15 | 0 | - | - | - | - | - | 2 failed |
| 0.47 | 7/15 | 0 | - | - | - | - | - | 2 failed |
| 0.53 | 8/15 | 0 | - | - | - | - | - | 2 failed |
| 0.60 | 9/15 | 0 | - | - | - | - | - | 2 failed |
| 0.67 | 10/15 | 0 | - | - | - | - | - | 2 failed |
| 0.73 | 11/15 | 0 | - | - | - | - | - | 2 failed |
| 0.80 | 12/15 | 0 | - | - | - | - | - | 2 failed |
| 0.87 | 13/15 | 0 | - | - | - | - | - | 2 failed |
| 0.93 | 14/15 | 0 | - | - | - | - | - | 2 failed |
| 1.00 | 15/15 | 0 | - | - | - | - | - | 1 failed |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/advanced/proportion_sweep/main_0x0_k00_s01.py` | artifact main_0x0_k00_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/advanced/proportion_sweep/main_0x0_k00_s01.py", line 47, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.07 | 1/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/advanced/proportion_sweep/main_0x2_k01_s01.py` | artifact main_0x2_k01_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/advanced/proportion_sweep/main_0x2_k01_s01.py", line 47, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.07 | 1/15 | 2 | - | - | - | - | - | - | - | `detyped_files/pystone/advanced/proportion_sweep/main_0x200_k01_s02.py` | artifact main_0x200_k01_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/advanced/proportion_sweep/main_0x200_k01_s02.py", line 47, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.13 | 2/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/advanced/proportion_sweep/main_0x2020_k02_s01.py` | artifact main_0x2020_k02_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/advanced/proportion_sweep/main_0x2020_k02_s01.py", line 47, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.13 | 2/15 | 2 | - | - | - | - | - | - | - | `detyped_files/pystone/advanced/proportion_sweep/main_0x104_k02_s02.py` | artifact main_0x104_k02_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/advanced/proportion_sweep/main_0x104_k02_s02.py", line 47, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.20 | 3/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/advanced/proportion_sweep/main_0x6008_k03_s01.py` | artifact main_0x6008_k03_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/advanced/proportion_sweep/main_0x6008_k03_s01.py", line 47, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.20 | 3/15 | 2 | - | - | - | - | - | - | - | `detyped_files/pystone/advanced/proportion_sweep/main_0x5004_k03_s02.py` | artifact main_0x5004_k03_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/advanced/proportion_sweep/main_0x5004_k03_s02.py", line 47, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.27 | 4/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/advanced/proportion_sweep/main_0x660_k04_s01.py` | artifact main_0x660_k04_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/advanced/proportion_sweep/main_0x660_k04_s01.py", line 47, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.27 | 4/15 | 2 | - | - | - | - | - | - | - | `detyped_files/pystone/advanced/proportion_sweep/main_0x90a_k04_s02.py` | artifact main_0x90a_k04_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/advanced/proportion_sweep/main_0x90a_k04_s02.py", line 47, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.33 | 5/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/advanced/proportion_sweep/main_0x1286_k05_s01.py` | artifact main_0x1286_k05_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/advanced/proportion_sweep/main_0x1286_k05_s01.py", line 47, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.33 | 5/15 | 2 | - | - | - | - | - | - | - | `detyped_files/pystone/advanced/proportion_sweep/main_0x1074_k05_s02.py` | artifact main_0x1074_k05_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/advanced/proportion_sweep/main_0x1074_k05_s02.py", line 47, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.40 | 6/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/advanced/proportion_sweep/main_0x4934_k06_s01.py` | artifact main_0x4934_k06_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/advanced/proportion_sweep/main_0x4934_k06_s01.py", line 47, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.40 | 6/15 | 2 | - | - | - | - | - | - | - | `detyped_files/pystone/advanced/proportion_sweep/main_0x5138_k06_s02.py` | artifact main_0x5138_k06_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/advanced/proportion_sweep/main_0x5138_k06_s02.py", line 47, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.47 | 7/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/advanced/proportion_sweep/main_0x2f60_k07_s01.py` | artifact main_0x2f60_k07_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/advanced/proportion_sweep/main_0x2f60_k07_s01.py", line 47, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.47 | 7/15 | 2 | - | - | - | - | - | - | - | `detyped_files/pystone/advanced/proportion_sweep/main_0x568c_k07_s02.py` | artifact main_0x568c_k07_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/advanced/proportion_sweep/main_0x568c_k07_s02.py", line 47, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.53 | 8/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/advanced/proportion_sweep/main_0x36b1_k08_s01.py` | artifact main_0x36b1_k08_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/advanced/proportion_sweep/main_0x36b1_k08_s01.py", line 47, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.53 | 8/15 | 2 | - | - | - | - | - | - | - | `detyped_files/pystone/advanced/proportion_sweep/main_0x25e5_k08_s02.py` | artifact main_0x25e5_k08_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/advanced/proportion_sweep/main_0x25e5_k08_s02.py", line 47, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.60 | 9/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/advanced/proportion_sweep/main_0x3337_k09_s01.py` | artifact main_0x3337_k09_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/advanced/proportion_sweep/main_0x3337_k09_s01.py", line 47, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.60 | 9/15 | 2 | - | - | - | - | - | - | - | `detyped_files/pystone/advanced/proportion_sweep/main_0x25fa_k09_s02.py` | artifact main_0x25fa_k09_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/advanced/proportion_sweep/main_0x25fa_k09_s02.py", line 47, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.67 | 10/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/advanced/proportion_sweep/main_0x66db_k10_s01.py` | artifact main_0x66db_k10_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/advanced/proportion_sweep/main_0x66db_k10_s01.py", line 47, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.67 | 10/15 | 2 | - | - | - | - | - | - | - | `detyped_files/pystone/advanced/proportion_sweep/main_0x73ad_k10_s02.py` | artifact main_0x73ad_k10_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/advanced/proportion_sweep/main_0x73ad_k10_s02.py", line 47, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.73 | 11/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/advanced/proportion_sweep/main_0x6bfa_k11_s01.py` | artifact main_0x6bfa_k11_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/advanced/proportion_sweep/main_0x6bfa_k11_s01.py", line 47, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.73 | 11/15 | 2 | - | - | - | - | - | - | - | `detyped_files/pystone/advanced/proportion_sweep/main_0x55f7_k11_s02.py` | artifact main_0x55f7_k11_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/advanced/proportion_sweep/main_0x55f7_k11_s02.py", line 47, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.80 | 12/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/advanced/proportion_sweep/main_0x7cdf_k12_s01.py` | artifact main_0x7cdf_k12_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/advanced/proportion_sweep/main_0x7cdf_k12_s01.py", line 47, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.80 | 12/15 | 2 | - | - | - | - | - | - | - | `detyped_files/pystone/advanced/proportion_sweep/main_0x7fe3_k12_s02.py` | artifact main_0x7fe3_k12_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/advanced/proportion_sweep/main_0x7fe3_k12_s02.py", line 47, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.87 | 13/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/advanced/proportion_sweep/main_0x7b7f_k13_s01.py` | artifact main_0x7b7f_k13_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/advanced/proportion_sweep/main_0x7b7f_k13_s01.py", line 47, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.87 | 13/15 | 2 | - | - | - | - | - | - | - | `detyped_files/pystone/advanced/proportion_sweep/main_0x6ffe_k13_s02.py` | artifact main_0x6ffe_k13_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/advanced/proportion_sweep/main_0x6ffe_k13_s02.py", line 47, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.93 | 14/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/advanced/proportion_sweep/main_0x7ffe_k14_s01.py` | artifact main_0x7ffe_k14_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/advanced/proportion_sweep/main_0x7ffe_k14_s01.py", line 47, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.93 | 14/15 | 2 | - | - | - | - | - | - | - | `detyped_files/pystone/advanced/proportion_sweep/main_0x7fdf_k14_s02.py` | artifact main_0x7fdf_k14_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/advanced/proportion_sweep/main_0x7fdf_k14_s02.py", line 47, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 1.00 | 15/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/advanced/proportion_sweep/main_0x7fff_k15_s01.py` | artifact main_0x7fff_k15_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/advanced/proportion_sweep/main_0x7fff_k15_s01.py", line 47, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |

## pystone/shallow

- Detypable targets: `15`
- Total runs: `30`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/15 | 0 | - | - | - | - | - | 1 failed |
| 0.07 | 1/15 | 0 | - | - | - | - | - | 2 failed |
| 0.13 | 2/15 | 0 | - | - | - | - | - | 2 failed |
| 0.20 | 3/15 | 0 | - | - | - | - | - | 2 failed |
| 0.27 | 4/15 | 0 | - | - | - | - | - | 2 failed |
| 0.33 | 5/15 | 0 | - | - | - | - | - | 2 failed |
| 0.40 | 6/15 | 0 | - | - | - | - | - | 2 failed |
| 0.47 | 7/15 | 0 | - | - | - | - | - | 2 failed |
| 0.53 | 8/15 | 0 | - | - | - | - | - | 2 failed |
| 0.60 | 9/15 | 0 | - | - | - | - | - | 2 failed |
| 0.67 | 10/15 | 0 | - | - | - | - | - | 2 failed |
| 0.73 | 11/15 | 0 | - | - | - | - | - | 2 failed |
| 0.80 | 12/15 | 0 | - | - | - | - | - | 2 failed |
| 0.87 | 13/15 | 0 | - | - | - | - | - | 2 failed |
| 0.93 | 14/15 | 0 | - | - | - | - | - | 2 failed |
| 1.00 | 15/15 | 0 | - | - | - | - | - | 1 failed |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/shallow/proportion_sweep/main_0x0_k00_s01.py` | artifact main_0x0_k00_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/shallow/proportion_sweep/main_0x0_k00_s01.py", line 45, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.07 | 1/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/shallow/proportion_sweep/main_0x40_k01_s01.py` | artifact main_0x40_k01_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/shallow/proportion_sweep/main_0x40_k01_s01.py", line 45, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.07 | 1/15 | 2 | - | - | - | - | - | - | - | `detyped_files/pystone/shallow/proportion_sweep/main_0x400_k01_s02.py` | artifact main_0x400_k01_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/shallow/proportion_sweep/main_0x400_k01_s02.py", line 45, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.13 | 2/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/shallow/proportion_sweep/main_0x420_k02_s01.py` | artifact main_0x420_k02_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/shallow/proportion_sweep/main_0x420_k02_s01.py", line 45, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.13 | 2/15 | 2 | - | - | - | - | - | - | - | `detyped_files/pystone/shallow/proportion_sweep/main_0x210_k02_s02.py` | artifact main_0x210_k02_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/shallow/proportion_sweep/main_0x210_k02_s02.py", line 45, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.20 | 3/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/shallow/proportion_sweep/main_0x8a_k03_s01.py` | artifact main_0x8a_k03_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/shallow/proportion_sweep/main_0x8a_k03_s01.py", line 45, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.20 | 3/15 | 2 | - | - | - | - | - | - | - | `detyped_files/pystone/shallow/proportion_sweep/main_0x320_k03_s02.py` | artifact main_0x320_k03_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/shallow/proportion_sweep/main_0x320_k03_s02.py", line 45, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.27 | 4/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/shallow/proportion_sweep/main_0xb8_k04_s01.py` | artifact main_0xb8_k04_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/shallow/proportion_sweep/main_0xb8_k04_s01.py", line 45, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.27 | 4/15 | 2 | - | - | - | - | - | - | - | `detyped_files/pystone/shallow/proportion_sweep/main_0xa41_k04_s02.py` | artifact main_0xa41_k04_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/shallow/proportion_sweep/main_0xa41_k04_s02.py", line 45, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.33 | 5/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/shallow/proportion_sweep/main_0x430a_k05_s01.py` | artifact main_0x430a_k05_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/shallow/proportion_sweep/main_0x430a_k05_s01.py", line 45, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.33 | 5/15 | 2 | - | - | - | - | - | - | - | `detyped_files/pystone/shallow/proportion_sweep/main_0x4864_k05_s02.py` | artifact main_0x4864_k05_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/shallow/proportion_sweep/main_0x4864_k05_s02.py", line 45, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.40 | 6/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/shallow/proportion_sweep/main_0x23a1_k06_s01.py` | artifact main_0x23a1_k06_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/shallow/proportion_sweep/main_0x23a1_k06_s01.py", line 45, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.40 | 6/15 | 2 | - | - | - | - | - | - | - | `detyped_files/pystone/shallow/proportion_sweep/main_0x684a_k06_s02.py` | artifact main_0x684a_k06_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/shallow/proportion_sweep/main_0x684a_k06_s02.py", line 45, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.47 | 7/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/shallow/proportion_sweep/main_0x5235_k07_s01.py` | artifact main_0x5235_k07_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/shallow/proportion_sweep/main_0x5235_k07_s01.py", line 45, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.47 | 7/15 | 2 | - | - | - | - | - | - | - | `detyped_files/pystone/shallow/proportion_sweep/main_0x4d86_k07_s02.py` | artifact main_0x4d86_k07_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/shallow/proportion_sweep/main_0x4d86_k07_s02.py", line 45, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.53 | 8/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/shallow/proportion_sweep/main_0x529b_k08_s01.py` | artifact main_0x529b_k08_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/shallow/proportion_sweep/main_0x529b_k08_s01.py", line 45, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.53 | 8/15 | 2 | - | - | - | - | - | - | - | `detyped_files/pystone/shallow/proportion_sweep/main_0xdba_k08_s02.py` | artifact main_0xdba_k08_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/shallow/proportion_sweep/main_0xdba_k08_s02.py", line 45, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.60 | 9/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/shallow/proportion_sweep/main_0x50fd_k09_s01.py` | artifact main_0x50fd_k09_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/shallow/proportion_sweep/main_0x50fd_k09_s01.py", line 45, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.60 | 9/15 | 2 | - | - | - | - | - | - | - | `detyped_files/pystone/shallow/proportion_sweep/main_0x1b75_k09_s02.py` | artifact main_0x1b75_k09_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/shallow/proportion_sweep/main_0x1b75_k09_s02.py", line 45, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.67 | 10/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/shallow/proportion_sweep/main_0xf7d_k10_s01.py` | artifact main_0xf7d_k10_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/shallow/proportion_sweep/main_0xf7d_k10_s01.py", line 45, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.67 | 10/15 | 2 | - | - | - | - | - | - | - | `detyped_files/pystone/shallow/proportion_sweep/main_0x3bb3_k10_s02.py` | artifact main_0x3bb3_k10_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/shallow/proportion_sweep/main_0x3bb3_k10_s02.py", line 45, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.73 | 11/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/shallow/proportion_sweep/main_0x3eee_k11_s01.py` | artifact main_0x3eee_k11_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/shallow/proportion_sweep/main_0x3eee_k11_s01.py", line 45, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.73 | 11/15 | 2 | - | - | - | - | - | - | - | `detyped_files/pystone/shallow/proportion_sweep/main_0x3bed_k11_s02.py` | artifact main_0x3bed_k11_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/shallow/proportion_sweep/main_0x3bed_k11_s02.py", line 45, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.80 | 12/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/shallow/proportion_sweep/main_0x6fee_k12_s01.py` | artifact main_0x6fee_k12_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/shallow/proportion_sweep/main_0x6fee_k12_s01.py", line 45, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.80 | 12/15 | 2 | - | - | - | - | - | - | - | `detyped_files/pystone/shallow/proportion_sweep/main_0x77f6_k12_s02.py` | artifact main_0x77f6_k12_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/shallow/proportion_sweep/main_0x77f6_k12_s02.py", line 45, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.87 | 13/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/shallow/proportion_sweep/main_0x3dff_k13_s01.py` | artifact main_0x3dff_k13_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/shallow/proportion_sweep/main_0x3dff_k13_s01.py", line 45, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.87 | 13/15 | 2 | - | - | - | - | - | - | - | `detyped_files/pystone/shallow/proportion_sweep/main_0x67ff_k13_s02.py` | artifact main_0x67ff_k13_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/shallow/proportion_sweep/main_0x67ff_k13_s02.py", line 45, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.93 | 14/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/shallow/proportion_sweep/main_0x7ffe_k14_s01.py` | artifact main_0x7ffe_k14_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/shallow/proportion_sweep/main_0x7ffe_k14_s01.py", line 45, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.93 | 14/15 | 2 | - | - | - | - | - | - | - | `detyped_files/pystone/shallow/proportion_sweep/main_0x7f7f_k14_s02.py` | artifact main_0x7f7f_k14_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/shallow/proportion_sweep/main_0x7f7f_k14_s02.py", line 45, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 1.00 | 15/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/shallow/proportion_sweep/main_0x7fff_k15_s01.py` | artifact main_0x7fff_k15_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/pystone/shallow/proportion_sweep/main_0x7fff_k15_s01.py", line 45, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |

## pystone/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.2842s | 0.2842s | 0.2842s | 2.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.2842s | 0.0566s | 2 | 16 | yes | 0.2573s | 0.3112s | `static-python-perf/Benchmark/pystone/untyped/main.py` |  |

## richards/advanced

- Detypable targets: `23`
- Total runs: `46`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/23 | 0 | - | - | - | - | - | 1 failed |
| 0.04 | 1/23 | 0 | - | - | - | - | - | 2 failed |
| 0.09 | 2/23 | 0 | - | - | - | - | - | 2 failed |
| 0.13 | 3/23 | 0 | - | - | - | - | - | 2 failed |
| 0.17 | 4/23 | 0 | - | - | - | - | - | 2 failed |
| 0.22 | 5/23 | 0 | - | - | - | - | - | 2 failed |
| 0.26 | 6/23 | 0 | - | - | - | - | - | 2 failed |
| 0.30 | 7/23 | 0 | - | - | - | - | - | 2 failed |
| 0.35 | 8/23 | 0 | - | - | - | - | - | 2 failed |
| 0.39 | 9/23 | 0 | - | - | - | - | - | 2 failed |
| 0.43 | 10/23 | 0 | - | - | - | - | - | 2 failed |
| 0.48 | 11/23 | 0 | - | - | - | - | - | 2 failed |
| 0.52 | 12/23 | 0 | - | - | - | - | - | 2 failed |
| 0.57 | 13/23 | 0 | - | - | - | - | - | 2 failed |
| 0.61 | 14/23 | 0 | - | - | - | - | - | 2 failed |
| 0.65 | 15/23 | 0 | - | - | - | - | - | 2 failed |
| 0.70 | 16/23 | 0 | - | - | - | - | - | 2 failed |
| 0.74 | 17/23 | 0 | - | - | - | - | - | 2 failed |
| 0.78 | 18/23 | 0 | - | - | - | - | - | 2 failed |
| 0.83 | 19/23 | 0 | - | - | - | - | - | 2 failed |
| 0.87 | 20/23 | 0 | - | - | - | - | - | 2 failed |
| 0.91 | 21/23 | 0 | - | - | - | - | - | 2 failed |
| 0.96 | 22/23 | 0 | - | - | - | - | - | 2 failed |
| 1.00 | 23/23 | 0 | - | - | - | - | - | 1 failed |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x0_k00_s01.py` | artifact main_0x0_k00_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x0_k00_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.04 | 1/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x40000_k01_s01.py` | artifact main_0x40000_k01_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x40000_k01_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.04 | 1/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x2_k01_s02.py` | artifact main_0x2_k01_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x2_k01_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.09 | 2/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x20200_k02_s01.py` | artifact main_0x20200_k02_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x20200_k02_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.09 | 2/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x10010_k02_s02.py` | artifact main_0x10010_k02_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x10010_k02_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.13 | 3/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x400820_k03_s01.py` | artifact main_0x400820_k03_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x400820_k03_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.13 | 3/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x40082_k03_s02.py` | artifact main_0x40082_k03_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x40082_k03_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.17 | 4/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x104009_k04_s01.py` | artifact main_0x104009_k04_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x104009_k04_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.17 | 4/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0xc009_k04_s02.py` | artifact main_0xc009_k04_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0xc009_k04_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.22 | 5/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x450012_k05_s01.py` | artifact main_0x450012_k05_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x450012_k05_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.22 | 5/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x4402a0_k05_s02.py` | artifact main_0x4402a0_k05_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x4402a0_k05_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.26 | 6/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x229140_k06_s01.py` | artifact main_0x229140_k06_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x229140_k06_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.26 | 6/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x1d102_k06_s02.py` | artifact main_0x1d102_k06_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x1d102_k06_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.30 | 7/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x868a2_k07_s01.py` | artifact main_0x868a2_k07_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x868a2_k07_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.30 | 7/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x132428_k07_s02.py` | artifact main_0x132428_k07_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x132428_k07_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.35 | 8/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0xc0175_k08_s01.py` | artifact main_0xc0175_k08_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0xc0175_k08_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.35 | 8/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x134322_k08_s02.py` | artifact main_0x134322_k08_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x134322_k08_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.39 | 9/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x241c66_k09_s01.py` | artifact main_0x241c66_k09_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x241c66_k09_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.39 | 9/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x2c2331_k09_s02.py` | artifact main_0x2c2331_k09_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x2c2331_k09_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.43 | 10/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x195534_k10_s01.py` | artifact main_0x195534_k10_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x195534_k10_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.43 | 10/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x2ba134_k10_s02.py` | artifact main_0x2ba134_k10_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x2ba134_k10_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.48 | 11/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x3903ec_k11_s01.py` | artifact main_0x3903ec_k11_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x3903ec_k11_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.48 | 11/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x5167b_k11_s02.py` | artifact main_0x5167b_k11_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x5167b_k11_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.52 | 12/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x4918fe_k12_s01.py` | artifact main_0x4918fe_k12_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x4918fe_k12_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.52 | 12/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x65a167_k12_s02.py` | artifact main_0x65a167_k12_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x65a167_k12_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.57 | 13/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x3a369e_k13_s01.py` | artifact main_0x3a369e_k13_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x3a369e_k13_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.57 | 13/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x46f687_k13_s02.py` | artifact main_0x46f687_k13_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x46f687_k13_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.61 | 14/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x1d58df_k14_s01.py` | artifact main_0x1d58df_k14_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x1d58df_k14_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.61 | 14/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x37a73c_k14_s02.py` | artifact main_0x37a73c_k14_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x37a73c_k14_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.65 | 15/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x5fc29f_k15_s01.py` | artifact main_0x5fc29f_k15_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x5fc29f_k15_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.65 | 15/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x78fa9b_k15_s02.py` | artifact main_0x78fa9b_k15_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x78fa9b_k15_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.70 | 16/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x3af5bb_k16_s01.py` | artifact main_0x3af5bb_k16_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x3af5bb_k16_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.70 | 16/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x77ab3e_k16_s02.py` | artifact main_0x77ab3e_k16_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x77ab3e_k16_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.74 | 17/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x7d7b5d_k17_s01.py` | artifact main_0x7d7b5d_k17_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x7d7b5d_k17_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.74 | 17/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x77fdd8_k17_s02.py` | artifact main_0x77fdd8_k17_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x77fdd8_k17_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.78 | 18/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x5ffdd9_k18_s01.py` | artifact main_0x5ffdd9_k18_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x5ffdd9_k18_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.78 | 18/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x7fdb7a_k18_s02.py` | artifact main_0x7fdb7a_k18_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x7fdb7a_k18_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.83 | 19/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x77deef_k19_s01.py` | artifact main_0x77deef_k19_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x77deef_k19_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.83 | 19/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x7f9faf_k19_s02.py` | artifact main_0x7f9faf_k19_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x7f9faf_k19_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.87 | 20/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x7dffdd_k20_s01.py` | artifact main_0x7dffdd_k20_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x7dffdd_k20_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.87 | 20/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x5ff9ff_k20_s02.py` | artifact main_0x5ff9ff_k20_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x5ff9ff_k20_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.91 | 21/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x6ffffb_k21_s01.py` | artifact main_0x6ffffb_k21_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x6ffffb_k21_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.91 | 21/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x7f7f7f_k21_s02.py` | artifact main_0x7f7f7f_k21_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x7f7f7f_k21_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.96 | 22/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x7fff7f_k22_s01.py` | artifact main_0x7fff7f_k22_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x7fff7f_k22_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.96 | 22/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x7fffdf_k22_s02.py` | artifact main_0x7fffdf_k22_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x7fffdf_k22_s02.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 1.00 | 23/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/advanced/proportion_sweep/main_0x7fffff_k23_s01.py` | artifact main_0x7fffff_k23_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/advanced/proportion_sweep/main_0x7fffff_k23_s01.py", line 13, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |

## richards/shallow

- Detypable targets: `23`
- Total runs: `46`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/23 | 0 | - | - | - | - | - | 1 failed |
| 0.04 | 1/23 | 0 | - | - | - | - | - | 2 failed |
| 0.09 | 2/23 | 0 | - | - | - | - | - | 2 failed |
| 0.13 | 3/23 | 0 | - | - | - | - | - | 2 failed |
| 0.17 | 4/23 | 0 | - | - | - | - | - | 2 failed |
| 0.22 | 5/23 | 0 | - | - | - | - | - | 2 failed |
| 0.26 | 6/23 | 0 | - | - | - | - | - | 2 failed |
| 0.30 | 7/23 | 0 | - | - | - | - | - | 2 failed |
| 0.35 | 8/23 | 0 | - | - | - | - | - | 2 failed |
| 0.39 | 9/23 | 0 | - | - | - | - | - | 2 failed |
| 0.43 | 10/23 | 0 | - | - | - | - | - | 2 failed |
| 0.48 | 11/23 | 0 | - | - | - | - | - | 2 failed |
| 0.52 | 12/23 | 0 | - | - | - | - | - | 2 failed |
| 0.57 | 13/23 | 0 | - | - | - | - | - | 2 failed |
| 0.61 | 14/23 | 0 | - | - | - | - | - | 2 failed |
| 0.65 | 15/23 | 0 | - | - | - | - | - | 2 failed |
| 0.70 | 16/23 | 0 | - | - | - | - | - | 2 failed |
| 0.74 | 17/23 | 0 | - | - | - | - | - | 2 failed |
| 0.78 | 18/23 | 0 | - | - | - | - | - | 2 failed |
| 0.83 | 19/23 | 0 | - | - | - | - | - | 2 failed |
| 0.87 | 20/23 | 0 | - | - | - | - | - | 2 failed |
| 0.91 | 21/23 | 0 | - | - | - | - | - | 2 failed |
| 0.96 | 22/23 | 0 | - | - | - | - | - | 2 failed |
| 1.00 | 23/23 | 0 | - | - | - | - | - | 1 failed |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x0_k00_s01.py` | artifact main_0x0_k00_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x0_k00_s01.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.04 | 1/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x200000_k01_s01.py` | artifact main_0x200000_k01_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x200000_k01_s01.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.04 | 1/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x80_k01_s02.py` | artifact main_0x80_k01_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x80_k01_s02.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.09 | 2/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x300_k02_s01.py` | artifact main_0x300_k02_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x300_k02_s01.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.09 | 2/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x900_k02_s02.py` | artifact main_0x900_k02_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x900_k02_s02.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.13 | 3/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x410010_k03_s01.py` | artifact main_0x410010_k03_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x410010_k03_s01.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.13 | 3/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x110080_k03_s02.py` | artifact main_0x110080_k03_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x110080_k03_s02.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.17 | 4/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x140042_k04_s01.py` | artifact main_0x140042_k04_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x140042_k04_s01.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.17 | 4/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x423_k04_s02.py` | artifact main_0x423_k04_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x423_k04_s02.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.22 | 5/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x114208_k05_s01.py` | artifact main_0x114208_k05_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x114208_k05_s01.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.22 | 5/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x4010a1_k05_s02.py` | artifact main_0x4010a1_k05_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x4010a1_k05_s02.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.26 | 6/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x412308_k06_s01.py` | artifact main_0x412308_k06_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x412308_k06_s01.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.26 | 6/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x302049_k06_s02.py` | artifact main_0x302049_k06_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x302049_k06_s02.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.30 | 7/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0xae06_k07_s01.py` | artifact main_0xae06_k07_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0xae06_k07_s01.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.30 | 7/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x4026a1_k07_s02.py` | artifact main_0x4026a1_k07_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x4026a1_k07_s02.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.35 | 8/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x42e92_k08_s01.py` | artifact main_0x42e92_k08_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x42e92_k08_s01.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.35 | 8/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x222b12_k08_s02.py` | artifact main_0x222b12_k08_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x222b12_k08_s02.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.39 | 9/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x50b50a_k09_s01.py` | artifact main_0x50b50a_k09_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x50b50a_k09_s01.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.39 | 9/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x3e10a4_k09_s02.py` | artifact main_0x3e10a4_k09_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x3e10a4_k09_s02.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.43 | 10/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x43a256_k10_s01.py` | artifact main_0x43a256_k10_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x43a256_k10_s01.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.43 | 10/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x2aa2e8_k10_s02.py` | artifact main_0x2aa2e8_k10_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x2aa2e8_k10_s02.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.48 | 11/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x60751b_k11_s01.py` | artifact main_0x60751b_k11_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x60751b_k11_s01.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.48 | 11/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x21a56e_k11_s02.py` | artifact main_0x21a56e_k11_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x21a56e_k11_s02.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.52 | 12/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x702b73_k12_s01.py` | artifact main_0x702b73_k12_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x702b73_k12_s01.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.52 | 12/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x760ea9_k12_s02.py` | artifact main_0x760ea9_k12_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x760ea9_k12_s02.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.57 | 13/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x39cacd_k13_s01.py` | artifact main_0x39cacd_k13_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x39cacd_k13_s01.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.57 | 13/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x6e5e68_k13_s02.py` | artifact main_0x6e5e68_k13_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x6e5e68_k13_s02.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.61 | 14/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x38bece_k14_s01.py` | artifact main_0x38bece_k14_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x38bece_k14_s01.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.61 | 14/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x5c3cfa_k14_s02.py` | artifact main_0x5c3cfa_k14_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x5c3cfa_k14_s02.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.65 | 15/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x5e66d7_k15_s01.py` | artifact main_0x5e66d7_k15_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x5e66d7_k15_s01.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.65 | 15/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x2f73d6_k15_s02.py` | artifact main_0x2f73d6_k15_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x2f73d6_k15_s02.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.70 | 16/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x7d7e27_k16_s01.py` | artifact main_0x7d7e27_k16_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x7d7e27_k16_s01.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.70 | 16/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x76de1f_k16_s02.py` | artifact main_0x76de1f_k16_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x76de1f_k16_s02.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.74 | 17/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x57bbfa_k17_s01.py` | artifact main_0x57bbfa_k17_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x57bbfa_k17_s01.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.74 | 17/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x33f73f_k17_s02.py` | artifact main_0x33f73f_k17_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x33f73f_k17_s02.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.78 | 18/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x4bfeef_k18_s01.py` | artifact main_0x4bfeef_k18_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x4bfeef_k18_s01.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.78 | 18/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x77efce_k18_s02.py` | artifact main_0x77efce_k18_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x77efce_k18_s02.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.83 | 19/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x2efffb_k19_s01.py` | artifact main_0x2efffb_k19_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x2efffb_k19_s01.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.83 | 19/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x717fff_k19_s02.py` | artifact main_0x717fff_k19_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x717fff_k19_s02.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.87 | 20/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x76efff_k20_s01.py` | artifact main_0x76efff_k20_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x76efff_k20_s01.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.87 | 20/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x3efff7_k20_s02.py` | artifact main_0x3efff7_k20_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x3efff7_k20_s02.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.91 | 21/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x7fef7f_k21_s01.py` | artifact main_0x7fef7f_k21_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x7fef7f_k21_s01.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.91 | 21/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x7ff7fd_k21_s02.py` | artifact main_0x7ff7fd_k21_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x7ff7fd_k21_s02.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.96 | 22/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x6fffff_k22_s01.py` | artifact main_0x6fffff_k22_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x6fffff_k22_s01.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 0.96 | 22/23 | 2 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x7fffbf_k22_s02.py` | artifact main_0x7fffbf_k22_s02 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x7fffbf_k22_s02.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |
| 1.00 | 23/23 | 1 | - | - | - | - | - | - | - | `detyped_files/richards/shallow/proportion_sweep/main_0x7fffff_k23_s01.py` | artifact main_0x7fffff_k23_s01 failed (exit 1):
Traceback (most recent call last):
  File "/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files/richards/shallow/proportion_sweep/main_0x7fffff_k23_s01.py", line 12, in <module>
    import __static__
ModuleNotFoundError: No module named '__static__' |

## richards/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | timed samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.7174s | 0.7174s | 0.7174s | 3.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.7174s | 0.1477s | 3 | 24 | yes | 0.6600s | 0.7761s | `static-python-perf/Benchmark/richards/untyped/main.py` |  |
