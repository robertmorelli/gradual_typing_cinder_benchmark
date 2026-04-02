# Proportion Benchmark Report

- Generated: `2026-04-01T22:27:36-06:00`
- Benchmarks run serially: `yes`
- Iterations per detyped-count bucket: `2`
- Random seed: `0`

## call_method/advanced

- Detypable targets: `6`
- Total runs: `12`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1653s | 0.1653s | 0.1653s | 1.0 | yes | ok |
| 0.17 | 1/6 | 2 | 0.1677s | 0.1337s | 0.2018s | 1.0 | yes | ok |
| 0.33 | 2/6 | 2 | 0.5692s | 0.2097s | 0.9288s | 1.0 | yes | ok |
| 0.50 | 3/6 | 2 | 0.5686s | 0.2196s | 0.9175s | 1.0 | yes | ok |
| 0.67 | 4/6 | 2 | 0.5781s | 0.1542s | 1.0020s | 1.0 | yes | ok |
| 0.83 | 5/6 | 2 | 0.9979s | 0.9218s | 1.0740s | 1.0 | yes | ok |
| 1.00 | 6/6 | 1 | 1.0599s | 1.0599s | 1.0599s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1653s | 0.0034s | 1 | 8 | yes | 0.1633s | 0.1677s | `detyped_files/call_method/advanced/proportion_sweep/main_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 0.2018s | 0.0004s | 1 | 8 | yes | 0.2015s | 0.2020s | `detyped_files/call_method/advanced/proportion_sweep/main_k01_s01.py` |  |
| 0.17 | 1/6 | 2 | 0.1337s | 0.0026s | 1 | 8 | yes | 0.1322s | 0.1356s | `detyped_files/call_method/advanced/proportion_sweep/main_k01_s02.py` |  |
| 0.33 | 2/6 | 1 | 0.9288s | 0.1262s | 1 | 8 | yes | 0.8686s | 1.0172s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s01.py` |  |
| 0.33 | 2/6 | 2 | 0.2097s | 0.0157s | 1 | 8 | yes | 0.2019s | 0.2206s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s02.py` |  |
| 0.50 | 3/6 | 1 | 0.2196s | 0.0004s | 1 | 8 | yes | 0.2194s | 0.2199s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s01.py` |  |
| 0.50 | 3/6 | 2 | 0.9175s | 0.1168s | 1 | 8 | yes | 0.8723s | 1.0014s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s02.py` |  |
| 0.67 | 4/6 | 1 | 0.1542s | 0.0008s | 1 | 8 | yes | 0.1537s | 0.1547s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s01.py` |  |
| 0.67 | 4/6 | 2 | 1.0020s | 0.0900s | 1 | 8 | yes | 0.9648s | 1.0674s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s02.py` |  |
| 0.83 | 5/6 | 1 | 0.9218s | 0.0538s | 1 | 8 | yes | 0.9019s | 0.9602s | `detyped_files/call_method/advanced/proportion_sweep/main_k05_s01.py` |  |
| 0.83 | 5/6 | 2 | 1.0740s | 0.1114s | 1 | 8 | yes | 1.0063s | 1.1509s | `detyped_files/call_method/advanced/proportion_sweep/main_k05_s02.py` |  |
| 1.00 | 6/6 | 1 | 1.0599s | 0.1110s | 1 | 8 | yes | 0.9966s | 1.1381s | `detyped_files/call_method/advanced/proportion_sweep/main_k06_s01.py` |  |

## call_method/shallow

- Detypable targets: `6`
- Total runs: `12`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1490s | 0.1490s | 0.1490s | 1.0 | yes | ok |
| 0.17 | 1/6 | 2 | 0.5446s | 0.1623s | 0.9268s | 1.5 | yes | ok |
| 0.33 | 2/6 | 2 | 0.5383s | 0.1386s | 0.9380s | 1.0 | yes | ok |
| 0.50 | 3/6 | 2 | 0.5422s | 0.1818s | 0.9026s | 1.5 | yes | ok |
| 0.67 | 4/6 | 2 | 0.5800s | 0.1893s | 0.9707s | 1.5 | yes | ok |
| 0.83 | 5/6 | 2 | 0.5645s | 0.1637s | 0.9654s | 1.5 | yes | ok |
| 1.00 | 6/6 | 1 | 0.9164s | 0.9164s | 0.9164s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1490s | 0.0164s | 1 | 8 | yes | 0.1421s | 0.1608s | `detyped_files/call_method/shallow/proportion_sweep/main_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 0.9268s | 0.1193s | 2 | 16 | yes | 0.8770s | 0.9898s | `detyped_files/call_method/shallow/proportion_sweep/main_k01_s01.py` |  |
| 0.17 | 1/6 | 2 | 0.1623s | 0.0144s | 1 | 8 | yes | 0.1541s | 0.1722s | `detyped_files/call_method/shallow/proportion_sweep/main_k01_s02.py` |  |
| 0.33 | 2/6 | 1 | 0.9380s | 0.0956s | 1 | 8 | yes | 0.8926s | 1.0064s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s01.py` |  |
| 0.33 | 2/6 | 2 | 0.1386s | 0.0169s | 1 | 8 | yes | 0.1324s | 0.1507s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s02.py` |  |
| 0.50 | 3/6 | 1 | 0.9026s | 0.0934s | 1 | 8 | yes | 0.8540s | 0.9685s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s01.py` |  |
| 0.50 | 3/6 | 2 | 0.1818s | 0.0316s | 2 | 16 | yes | 0.1701s | 0.1991s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s02.py` |  |
| 0.67 | 4/6 | 1 | 0.9707s | 0.1322s | 2 | 16 | yes | 0.9132s | 1.0403s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s01.py` |  |
| 0.67 | 4/6 | 2 | 0.1893s | 0.0164s | 1 | 8 | yes | 0.1804s | 0.2025s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s02.py` |  |
| 0.83 | 5/6 | 1 | 0.9654s | 0.1229s | 2 | 16 | yes | 0.9100s | 1.0267s | `detyped_files/call_method/shallow/proportion_sweep/main_k05_s01.py` |  |
| 0.83 | 5/6 | 2 | 0.1637s | 0.0123s | 1 | 8 | yes | 0.1570s | 0.1724s | `detyped_files/call_method/shallow/proportion_sweep/main_k05_s02.py` |  |
| 1.00 | 6/6 | 1 | 0.9164s | 0.0357s | 1 | 8 | yes | 0.8974s | 0.9413s | `detyped_files/call_method/shallow/proportion_sweep/main_k06_s01.py` |  |

## call_method/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.1245s | 0.1245s | 0.1245s | 2.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.1245s | 0.0173s | 2 | 16 | yes | 0.1183s | 0.1340s | `static-python-perf/Benchmark/call_method/untyped/main.py` |  |
