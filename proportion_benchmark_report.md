# Proportion Benchmark Report

- Generated: `2026-04-01T17:52:33-06:00`
- Benchmarks run serially: `yes`
- Iterations per detyped-count bucket: `2`
- Random seed: `0`

## call_method/advanced

- Detypable targets: `6`
- Total runs: `12`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1685s | 0.1685s | 0.1685s | 1.0 | yes | ok |
| 0.17 | 1/6 | 2 | 0.1819s | 0.1409s | 0.2229s | 5.0 | yes | ok |
| 0.33 | 2/6 | 2 | 0.5501s | 0.2016s | 0.8986s | 1.0 | yes | ok |
| 0.50 | 3/6 | 2 | 0.5619s | 0.2192s | 0.9047s | 1.0 | yes | ok |
| 0.67 | 4/6 | 2 | 0.5755s | 0.1542s | 0.9968s | 1.0 | yes | ok |
| 0.83 | 5/6 | 2 | 0.9762s | 0.9317s | 1.0207s | 1.0 | yes | ok |
| 1.00 | 6/6 | 1 | 0.9949s | 0.9949s | 0.9949s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1685s | 0.0057s | 1 | 8 | yes | 0.1650s | 0.1723s | `detyped_files/call_method/advanced/proportion_sweep/main_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 0.2229s | 0.0532s | 4 | 32 | yes | 0.2069s | 0.2426s | `detyped_files/call_method/advanced/proportion_sweep/main_k01_s01.py` |  |
| 0.17 | 1/6 | 2 | 0.1409s | 0.0379s | 6 | 48 | yes | 0.1326s | 0.1530s | `detyped_files/call_method/advanced/proportion_sweep/main_k01_s02.py` |  |
| 0.33 | 2/6 | 1 | 0.8986s | 0.0890s | 1 | 8 | yes | 0.8665s | 0.9617s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s01.py` |  |
| 0.33 | 2/6 | 2 | 0.2016s | 0.0005s | 1 | 8 | yes | 0.2013s | 0.2020s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s02.py` |  |
| 0.50 | 3/6 | 1 | 0.2192s | 0.0003s | 1 | 8 | yes | 0.2190s | 0.2194s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s01.py` |  |
| 0.50 | 3/6 | 2 | 0.9047s | 0.0991s | 1 | 8 | yes | 0.8692s | 0.9749s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s02.py` |  |
| 0.67 | 4/6 | 1 | 0.1542s | 0.0012s | 1 | 8 | yes | 0.1536s | 0.1551s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s01.py` |  |
| 0.67 | 4/6 | 2 | 0.9968s | 0.0875s | 1 | 8 | yes | 0.9636s | 1.0592s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s02.py` |  |
| 0.83 | 5/6 | 1 | 0.9317s | 0.0744s | 1 | 8 | yes | 0.9018s | 0.9849s | `detyped_files/call_method/advanced/proportion_sweep/main_k05_s01.py` |  |
| 0.83 | 5/6 | 2 | 1.0207s | 0.1336s | 1 | 8 | yes | 0.9701s | 1.1160s | `detyped_files/call_method/advanced/proportion_sweep/main_k05_s02.py` |  |
| 1.00 | 6/6 | 1 | 0.9949s | 0.0580s | 1 | 8 | yes | 0.9741s | 1.0360s | `detyped_files/call_method/advanced/proportion_sweep/main_k06_s01.py` |  |

## call_method/shallow

- Detypable targets: `6`
- Total runs: `12`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1584s | 0.1584s | 0.1584s | 5.0 | yes | ok |
| 0.17 | 1/6 | 2 | 0.5310s | 0.1583s | 0.9036s | 1.0 | yes | ok |
| 0.33 | 2/6 | 2 | 0.5329s | 0.1331s | 0.9327s | 1.0 | yes | ok |
| 0.50 | 3/6 | 2 | 0.5468s | 0.1853s | 0.9083s | 1.0 | yes | ok |
| 0.67 | 4/6 | 2 | 0.5727s | 0.1845s | 0.9610s | 1.5 | yes | ok |
| 0.83 | 5/6 | 2 | 0.5683s | 0.1644s | 0.9721s | 1.5 | yes | ok |
| 1.00 | 6/6 | 1 | 0.9423s | 0.9423s | 0.9423s | 2.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1584s | 0.0470s | 5 | 40 | yes | 0.1464s | 0.1743s | `detyped_files/call_method/shallow/proportion_sweep/main_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 0.9036s | 0.0908s | 1 | 8 | yes | 0.8703s | 0.9682s | `detyped_files/call_method/shallow/proportion_sweep/main_k01_s01.py` |  |
| 0.17 | 1/6 | 2 | 0.1583s | 0.0143s | 1 | 8 | yes | 0.1527s | 0.1686s | `detyped_files/call_method/shallow/proportion_sweep/main_k01_s02.py` |  |
| 0.33 | 2/6 | 1 | 0.9327s | 0.1127s | 1 | 8 | yes | 0.8879s | 1.0135s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s01.py` |  |
| 0.33 | 2/6 | 2 | 0.1331s | 0.0005s | 1 | 8 | yes | 0.1328s | 0.1334s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s02.py` |  |
| 0.50 | 3/6 | 1 | 0.9083s | 0.1075s | 1 | 8 | yes | 0.8526s | 0.9839s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s01.py` |  |
| 0.50 | 3/6 | 2 | 0.1853s | 0.0148s | 1 | 8 | yes | 0.1756s | 0.1946s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s02.py` |  |
| 0.67 | 4/6 | 1 | 0.9610s | 0.1368s | 2 | 16 | yes | 0.9207s | 1.0325s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s01.py` |  |
| 0.67 | 4/6 | 2 | 0.1845s | 0.0098s | 1 | 8 | yes | 0.1807s | 0.1915s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s02.py` |  |
| 0.83 | 5/6 | 1 | 0.9721s | 0.1711s | 2 | 16 | yes | 0.9071s | 1.0658s | `detyped_files/call_method/shallow/proportion_sweep/main_k05_s01.py` |  |
| 0.83 | 5/6 | 2 | 0.1644s | 0.0222s | 1 | 8 | yes | 0.1551s | 0.1804s | `detyped_files/call_method/shallow/proportion_sweep/main_k05_s02.py` |  |
| 1.00 | 6/6 | 1 | 0.9423s | 0.1301s | 2 | 16 | yes | 0.9018s | 1.0113s | `detyped_files/call_method/shallow/proportion_sweep/main_k06_s01.py` |  |

## call_method/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.1237s | 0.1237s | 0.1237s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.1237s | 0.0143s | 1 | 8 | yes | 0.1183s | 0.1339s | `static-python-perf/Benchmark/call_method/untyped/main.py` |  |

## call_method_slots/advanced

- Detypable targets: `6`
- Total runs: `12`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1648s | 0.1648s | 0.1648s | 1.0 | yes | ok |
| 0.17 | 1/6 | 2 | 0.1380s | 0.1318s | 0.1441s | 1.5 | yes | ok |
| 0.33 | 2/6 | 2 | 0.5322s | 0.1345s | 0.9299s | 1.0 | yes | ok |
| 0.50 | 3/6 | 2 | 0.9153s | 0.8843s | 0.9464s | 1.0 | yes | ok |
| 0.67 | 4/6 | 2 | 0.5761s | 0.2245s | 0.9278s | 1.0 | yes | ok |
| 0.83 | 5/6 | 2 | 0.9562s | 0.9229s | 0.9894s | 1.0 | yes | ok |
| 1.00 | 6/6 | 1 | 0.9989s | 0.9989s | 0.9989s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1648s | 0.0026s | 1 | 8 | yes | 0.1631s | 0.1665s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 0.1318s | 0.0003s | 1 | 8 | yes | 0.1316s | 0.1320s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k01_s01.py` |  |
| 0.17 | 1/6 | 2 | 0.1441s | 0.0216s | 2 | 16 | yes | 0.1373s | 0.1557s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k01_s02.py` |  |
| 0.33 | 2/6 | 1 | 0.9299s | 0.1065s | 1 | 8 | yes | 0.8767s | 1.0077s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k02_s01.py` |  |
| 0.33 | 2/6 | 2 | 0.1345s | 0.0031s | 1 | 8 | yes | 0.1324s | 0.1364s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k02_s02.py` |  |
| 0.50 | 3/6 | 1 | 0.9464s | 0.0931s | 1 | 8 | yes | 0.8936s | 1.0132s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s01.py` |  |
| 0.50 | 3/6 | 2 | 0.8843s | 0.0392s | 1 | 8 | yes | 0.8677s | 0.9123s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s02.py` |  |
| 0.67 | 4/6 | 1 | 0.2245s | 0.0018s | 1 | 8 | yes | 0.2235s | 0.2257s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k04_s01.py` |  |
| 0.67 | 4/6 | 2 | 0.9278s | 0.0683s | 1 | 8 | yes | 0.8915s | 0.9781s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k04_s02.py` |  |
| 0.83 | 5/6 | 1 | 0.9229s | 0.0610s | 1 | 8 | yes | 0.8905s | 0.9671s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k05_s01.py` |  |
| 0.83 | 5/6 | 2 | 0.9894s | 0.0306s | 1 | 8 | yes | 0.9728s | 1.0115s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k05_s02.py` |  |
| 1.00 | 6/6 | 1 | 0.9989s | 0.0333s | 1 | 8 | yes | 0.9798s | 1.0225s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k06_s01.py` |  |

## call_method_slots/shallow

- Detypable targets: `6`
- Total runs: `12`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1509s | 0.1509s | 0.1509s | 4.0 | yes | ok |
| 0.17 | 1/6 | 2 | 0.1275s | 0.1168s | 0.1383s | 1.0 | yes | ok |
| 0.33 | 2/6 | 2 | 0.5271s | 0.1642s | 0.8899s | 2.5 | yes | ok |
| 0.50 | 3/6 | 2 | 0.9042s | 0.8617s | 0.9466s | 2.0 | yes | ok |
| 0.67 | 4/6 | 2 | 0.5269s | 0.1261s | 0.9277s | 1.0 | yes | ok |
| 0.83 | 5/6 | 2 | 0.9239s | 0.8772s | 0.9706s | 1.0 | yes | ok |
| 1.00 | 6/6 | 1 | 0.9398s | 0.9398s | 0.9398s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1509s | 0.0307s | 4 | 32 | yes | 0.1423s | 0.1629s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 0.1383s | 0.0181s | 1 | 8 | yes | 0.1313s | 0.1513s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k01_s01.py` |  |
| 0.17 | 1/6 | 2 | 0.1168s | 0.0018s | 1 | 8 | yes | 0.1159s | 0.1181s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k01_s02.py` |  |
| 0.33 | 2/6 | 1 | 0.8899s | 0.0641s | 1 | 8 | yes | 0.8542s | 0.9353s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k02_s01.py` |  |
| 0.33 | 2/6 | 2 | 0.1642s | 0.0373s | 4 | 32 | yes | 0.1543s | 0.1792s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k02_s02.py` |  |
| 0.50 | 3/6 | 1 | 0.8617s | 0.0211s | 1 | 8 | yes | 0.8516s | 0.8766s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s01.py` |  |
| 0.50 | 3/6 | 2 | 0.9466s | 0.1653s | 3 | 24 | yes | 0.8924s | 1.0193s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s02.py` |  |
| 0.67 | 4/6 | 1 | 0.9277s | 0.0414s | 1 | 8 | yes | 0.9022s | 0.9564s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k04_s01.py` |  |
| 0.67 | 4/6 | 2 | 0.1261s | 0.0169s | 1 | 8 | yes | 0.1186s | 0.1382s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k04_s02.py` |  |
| 0.83 | 5/6 | 1 | 0.9706s | 0.1090s | 1 | 8 | yes | 0.9146s | 1.0486s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k05_s01.py` |  |
| 0.83 | 5/6 | 2 | 0.8772s | 0.0606s | 1 | 8 | yes | 0.8550s | 0.9204s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k05_s02.py` |  |
| 1.00 | 6/6 | 1 | 0.9398s | 0.0741s | 1 | 8 | yes | 0.9000s | 0.9909s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k06_s01.py` |  |

## call_method_slots/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.1317s | 0.1317s | 0.1317s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.1317s | 0.0145s | 1 | 8 | yes | 0.1252s | 0.1424s | `static-python-perf/Benchmark/call_method_slots/untyped/main.py` |  |

## call_simple/advanced

- Detypable targets: `6`
- Total runs: `12`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | - | - | - | - | - | 1 failed |
| 0.17 | 1/6 | 2 | 0.0909s | 0.0909s | 0.0909s | 1.0 | yes | 1 failed |
| 0.33 | 2/6 | 2 | 0.1335s | 0.1138s | 0.1533s | 1.5 | yes | ok |
| 0.50 | 3/6 | 2 | 0.1217s | 0.1114s | 0.1320s | 1.0 | yes | ok |
| 0.67 | 4/6 | 2 | 0.1713s | 0.1541s | 0.1886s | 1.0 | yes | ok |
| 0.83 | 5/6 | 2 | 0.1969s | 0.1863s | 0.2075s | 1.0 | yes | ok |
| 1.00 | 6/6 | 1 | 0.2005s | 0.2005s | 0.2005s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_simple/advanced/proportion_sweep/main_k00_s01.py` | benchmark script failed (1): detyped_files/call_simple/advanced/proportion_sweep/main_k00_s01.py
docker error: container create: Cannot connect to the Docker daemon at unix:///Users/robertmorelli/.docker/run/docker.sock. Is the docker daemon running? |
| 0.17 | 1/6 | 1 | - | - | - | - | - | - | - | `detyped_files/call_simple/advanced/proportion_sweep/main_k01_s01.py` | benchmark script failed (1): detyped_files/call_simple/advanced/proportion_sweep/main_k01_s01.py
docker error: container create: Cannot connect to the Docker daemon at unix:///Users/robertmorelli/.docker/run/docker.sock. Is the docker daemon running? |
| 0.17 | 1/6 | 2 | 0.0909s | 0.0034s | 1 | 8 | yes | 0.0894s | 0.0934s | `detyped_files/call_simple/advanced/proportion_sweep/main_k01_s02.py` |  |
| 0.33 | 2/6 | 1 | 0.1138s | 0.0056s | 1 | 8 | yes | 0.1107s | 0.1176s | `detyped_files/call_simple/advanced/proportion_sweep/main_k02_s01.py` |  |
| 0.33 | 2/6 | 2 | 0.1533s | 0.0252s | 2 | 16 | yes | 0.1455s | 0.1667s | `detyped_files/call_simple/advanced/proportion_sweep/main_k02_s02.py` |  |
| 0.50 | 3/6 | 1 | 0.1114s | 0.0005s | 1 | 8 | yes | 0.1111s | 0.1117s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s01.py` |  |
| 0.50 | 3/6 | 2 | 0.1320s | 0.0130s | 1 | 8 | yes | 0.1218s | 0.1393s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s02.py` |  |
| 0.67 | 4/6 | 1 | 0.1541s | 0.0051s | 1 | 8 | yes | 0.1518s | 0.1577s | `detyped_files/call_simple/advanced/proportion_sweep/main_k04_s01.py` |  |
| 0.67 | 4/6 | 2 | 0.1886s | 0.0175s | 1 | 8 | yes | 0.1816s | 0.2012s | `detyped_files/call_simple/advanced/proportion_sweep/main_k04_s02.py` |  |
| 0.83 | 5/6 | 1 | 0.1863s | 0.0006s | 1 | 8 | yes | 0.1860s | 0.1868s | `detyped_files/call_simple/advanced/proportion_sweep/main_k05_s01.py` |  |
| 0.83 | 5/6 | 2 | 0.2075s | 0.0125s | 1 | 8 | yes | 0.2029s | 0.2164s | `detyped_files/call_simple/advanced/proportion_sweep/main_k05_s02.py` |  |
| 1.00 | 6/6 | 1 | 0.2005s | 0.0006s | 1 | 8 | yes | 0.2002s | 0.2010s | `detyped_files/call_simple/advanced/proportion_sweep/main_k06_s01.py` |  |

## call_simple/shallow

- Detypable targets: `6`
- Total runs: `12`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1084s | 0.1084s | 0.1084s | 1.0 | yes | ok |
| 0.17 | 1/6 | 2 | 0.1109s | 0.1084s | 0.1134s | 1.0 | yes | ok |
| 0.33 | 2/6 | 2 | 0.1156s | 0.1134s | 0.1178s | 5.5 | yes | ok |
| 0.50 | 3/6 | 2 | 0.1146s | 0.1133s | 0.1159s | 2.0 | yes | ok |
| 0.67 | 4/6 | 2 | 0.1126s | 0.1085s | 0.1167s | 4.0 | yes | ok |
| 0.83 | 5/6 | 2 | 0.1085s | 0.1085s | 0.1085s | 1.0 | yes | ok |
| 1.00 | 6/6 | 1 | 0.1083s | 0.1083s | 0.1083s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1084s | 0.0003s | 1 | 8 | yes | 0.1082s | 0.1086s | `detyped_files/call_simple/shallow/proportion_sweep/main_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 0.1084s | 0.0003s | 1 | 8 | yes | 0.1082s | 0.1086s | `detyped_files/call_simple/shallow/proportion_sweep/main_k01_s01.py` |  |
| 0.17 | 1/6 | 2 | 0.1134s | 0.0131s | 1 | 8 | yes | 0.1087s | 0.1228s | `detyped_files/call_simple/shallow/proportion_sweep/main_k01_s02.py` |  |
| 0.33 | 2/6 | 1 | 0.1134s | 0.0134s | 2 | 16 | yes | 0.1088s | 0.1211s | `detyped_files/call_simple/shallow/proportion_sweep/main_k02_s01.py` |  |
| 0.33 | 2/6 | 2 | 0.1178s | 0.0421s | 9 | 72 | yes | 0.1101s | 0.1287s | `detyped_files/call_simple/shallow/proportion_sweep/main_k02_s02.py` |  |
| 0.50 | 3/6 | 1 | 0.1133s | 0.0131s | 2 | 16 | yes | 0.1088s | 0.1207s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s01.py` |  |
| 0.50 | 3/6 | 2 | 0.1159s | 0.0205s | 2 | 16 | yes | 0.1083s | 0.1271s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s02.py` |  |
| 0.67 | 4/6 | 1 | 0.1085s | 0.0003s | 1 | 8 | yes | 0.1083s | 0.1087s | `detyped_files/call_simple/shallow/proportion_sweep/main_k04_s01.py` |  |
| 0.67 | 4/6 | 2 | 0.1167s | 0.0368s | 7 | 56 | yes | 0.1097s | 0.1277s | `detyped_files/call_simple/shallow/proportion_sweep/main_k04_s02.py` |  |
| 0.83 | 5/6 | 1 | 0.1085s | 0.0004s | 1 | 8 | yes | 0.1083s | 0.1088s | `detyped_files/call_simple/shallow/proportion_sweep/main_k05_s01.py` |  |
| 0.83 | 5/6 | 2 | 0.1085s | 0.0007s | 1 | 8 | yes | 0.1081s | 0.1089s | `detyped_files/call_simple/shallow/proportion_sweep/main_k05_s02.py` |  |
| 1.00 | 6/6 | 1 | 0.1083s | 0.0003s | 1 | 8 | yes | 0.1081s | 0.1085s | `detyped_files/call_simple/shallow/proportion_sweep/main_k06_s01.py` |  |

## call_simple/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.1094s | 0.1094s | 0.1094s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.1094s | 0.0045s | 1 | 8 | yes | 0.1077s | 0.1127s | `static-python-perf/Benchmark/call_simple/untyped/main.py` |  |

## chaos/advanced

- Detypable targets: `5`
- Total runs: `10`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/5 | 1 | 0.2288s | 0.2288s | 0.2288s | 1.0 | yes | ok |
| 0.20 | 1/5 | 2 | 0.2493s | 0.2463s | 0.2522s | 3.0 | yes | ok |
| 0.40 | 2/5 | 2 | 0.2342s | 0.2315s | 0.2370s | 1.0 | yes | ok |
| 0.60 | 3/5 | 2 | 0.2791s | 0.2403s | 0.3178s | 1.5 | yes | ok |
| 0.80 | 4/5 | 2 | 0.3235s | 0.3186s | 0.3285s | 1.5 | yes | ok |
| 1.00 | 5/5 | 1 | 0.3174s | 0.3174s | 0.3174s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/5 | 1 | 0.2288s | 0.0033s | 1 | 8 | yes | 0.2271s | 0.2311s | `detyped_files/chaos/advanced/proportion_sweep/main_k00_s01.py` |  |
| 0.20 | 1/5 | 1 | 0.2463s | 0.0284s | 1 | 8 | yes | 0.2306s | 0.2675s | `detyped_files/chaos/advanced/proportion_sweep/main_k01_s01.py` |  |
| 0.20 | 1/5 | 2 | 0.2522s | 0.0668s | 5 | 40 | yes | 0.2346s | 0.2746s | `detyped_files/chaos/advanced/proportion_sweep/main_k01_s02.py` |  |
| 0.40 | 2/5 | 1 | 0.2315s | 0.0016s | 1 | 8 | yes | 0.2304s | 0.2326s | `detyped_files/chaos/advanced/proportion_sweep/main_k02_s01.py` |  |
| 0.40 | 2/5 | 2 | 0.2370s | 0.0017s | 1 | 8 | yes | 0.2362s | 0.2382s | `detyped_files/chaos/advanced/proportion_sweep/main_k02_s02.py` |  |
| 0.60 | 3/5 | 1 | 0.3178s | 0.0379s | 2 | 16 | yes | 0.3047s | 0.3391s | `detyped_files/chaos/advanced/proportion_sweep/main_k03_s01.py` |  |
| 0.60 | 3/5 | 2 | 0.2403s | 0.0143s | 1 | 8 | yes | 0.2346s | 0.2507s | `detyped_files/chaos/advanced/proportion_sweep/main_k03_s02.py` |  |
| 0.80 | 4/5 | 1 | 0.3186s | 0.0265s | 1 | 8 | yes | 0.3083s | 0.3377s | `detyped_files/chaos/advanced/proportion_sweep/main_k04_s01.py` |  |
| 0.80 | 4/5 | 2 | 0.3285s | 0.0465s | 2 | 16 | yes | 0.3082s | 0.3527s | `detyped_files/chaos/advanced/proportion_sweep/main_k04_s02.py` |  |
| 1.00 | 5/5 | 1 | 0.3174s | 0.0224s | 1 | 8 | yes | 0.3086s | 0.3335s | `detyped_files/chaos/advanced/proportion_sweep/main_k05_s01.py` |  |

## chaos/shallow

- Detypable targets: `5`
- Total runs: `10`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/5 | 1 | 0.2485s | 0.2485s | 0.2485s | 3.0 | yes | ok |
| 0.20 | 1/5 | 2 | 0.2855s | 0.2627s | 0.3083s | 1.0 | yes | ok |
| 0.40 | 2/5 | 2 | 0.2628s | 0.2545s | 0.2710s | 2.5 | yes | ok |
| 0.60 | 3/5 | 2 | 0.3270s | 0.3264s | 0.3277s | 1.5 | yes | ok |
| 0.80 | 4/5 | 2 | 0.3356s | 0.3146s | 0.3565s | 2.0 | yes | ok |
| 1.00 | 5/5 | 1 | 0.3573s | 0.3573s | 0.3573s | 3.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/5 | 1 | 0.2485s | 0.0526s | 3 | 24 | yes | 0.2299s | 0.2715s | `detyped_files/chaos/shallow/proportion_sweep/main_k00_s01.py` |  |
| 0.20 | 1/5 | 1 | 0.3083s | 0.0168s | 1 | 8 | yes | 0.3015s | 0.3204s | `detyped_files/chaos/shallow/proportion_sweep/main_k01_s01.py` |  |
| 0.20 | 1/5 | 2 | 0.2627s | 0.0172s | 1 | 8 | yes | 0.2560s | 0.2751s | `detyped_files/chaos/shallow/proportion_sweep/main_k01_s02.py` |  |
| 0.40 | 2/5 | 1 | 0.2710s | 0.0427s | 2 | 16 | yes | 0.2569s | 0.2950s | `detyped_files/chaos/shallow/proportion_sweep/main_k02_s01.py` |  |
| 0.40 | 2/5 | 2 | 0.2545s | 0.0573s | 3 | 24 | yes | 0.2370s | 0.2798s | `detyped_files/chaos/shallow/proportion_sweep/main_k02_s02.py` |  |
| 0.60 | 3/5 | 1 | 0.3264s | 0.0360s | 1 | 8 | yes | 0.3064s | 0.3532s | `detyped_files/chaos/shallow/proportion_sweep/main_k03_s01.py` |  |
| 0.60 | 3/5 | 2 | 0.3277s | 0.0422s | 2 | 16 | yes | 0.3090s | 0.3500s | `detyped_files/chaos/shallow/proportion_sweep/main_k03_s02.py` |  |
| 0.80 | 4/5 | 1 | 0.3146s | 0.0125s | 1 | 8 | yes | 0.3092s | 0.3236s | `detyped_files/chaos/shallow/proportion_sweep/main_k04_s01.py` |  |
| 0.80 | 4/5 | 2 | 0.3565s | 0.0626s | 3 | 24 | yes | 0.3371s | 0.3848s | `detyped_files/chaos/shallow/proportion_sweep/main_k04_s02.py` |  |
| 1.00 | 5/5 | 1 | 0.3573s | 0.0671s | 3 | 24 | yes | 0.3393s | 0.3872s | `detyped_files/chaos/shallow/proportion_sweep/main_k05_s01.py` |  |

## chaos/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.2681s | 0.2681s | 0.2681s | 2.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.2681s | 0.0347s | 2 | 16 | yes | 0.2523s | 0.2858s | `static-python-perf/Benchmark/chaos/untyped/main.py` |  |

## deltablue/advanced

- Detypable targets: `34`
- Total runs: `68`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/34 | 1 | 1.2113s | 1.2113s | 1.2113s | 1.0 | yes | ok |
| 0.03 | 1/34 | 2 | 1.2476s | 1.2178s | 1.2774s | 1.0 | yes | ok |
| 0.06 | 2/34 | 2 | 1.4287s | 1.2814s | 1.5760s | 1.0 | yes | ok |
| 0.09 | 3/34 | 2 | 1.3287s | 1.2783s | 1.3792s | 1.0 | yes | ok |
| 0.12 | 4/34 | 2 | 1.2980s | 1.2968s | 1.2991s | 1.5 | yes | ok |
| 0.15 | 5/34 | 2 | 1.3042s | 1.2610s | 1.3474s | 1.0 | yes | ok |
| 0.18 | 6/34 | 2 | 1.3218s | 1.2751s | 1.3685s | 1.0 | yes | ok |
| 0.21 | 7/34 | 2 | 1.3369s | 1.2455s | 1.4284s | 1.0 | yes | ok |
| 0.24 | 8/34 | 2 | 3.0702s | 1.1819s | 4.9586s | 1.0 | yes | ok |
| 0.26 | 9/34 | 2 | 1.4295s | 1.4136s | 1.4455s | 1.0 | yes | ok |
| 0.29 | 10/34 | 2 | 3.2117s | 1.2011s | 5.2223s | 1.0 | yes | ok |
| 0.32 | 11/34 | 2 | 5.1730s | 5.1730s | 5.1730s | 1.0 | yes | 1 failed |
| 0.35 | 12/34 | 2 | 3.3054s | 1.9199s | 4.6909s | 1.0 | yes | ok |
| 0.38 | 13/34 | 2 | 1.5629s | 1.3850s | 1.7408s | 1.0 | yes | ok |
| 0.41 | 14/34 | 2 | 3.3804s | 1.7423s | 5.0184s | 1.0 | yes | ok |
| 0.44 | 15/34 | 2 | 3.5561s | 1.4773s | 5.6349s | 1.0 | yes | ok |
| 0.47 | 16/34 | 2 | 5.5181s | 5.3731s | 5.6630s | 1.0 | yes | ok |
| 0.50 | 17/34 | 2 | 3.2182s | 1.3455s | 5.0908s | 1.0 | yes | ok |
| 0.53 | 18/34 | 2 | 5.2765s | 4.8042s | 5.7488s | 1.0 | yes | ok |
| 0.56 | 19/34 | 2 | 5.1989s | 4.9676s | 5.4303s | 1.0 | yes | ok |
| 0.59 | 20/34 | 2 | 3.8532s | 2.2714s | 5.4350s | 1.0 | yes | ok |
| 0.62 | 21/34 | 2 | 3.5784s | 1.4759s | 5.6809s | 1.0 | yes | ok |
| 0.65 | 22/34 | 2 | 5.5061s | 5.4486s | 5.5636s | 1.0 | yes | ok |
| 0.68 | 23/34 | 2 | 2.0504s | 1.8284s | 2.2723s | 1.0 | yes | ok |
| 0.71 | 24/34 | 2 | 5.8540s | 5.7461s | 5.9620s | 1.0 | yes | ok |
| 0.74 | 25/34 | 2 | 5.7245s | 5.7140s | 5.7350s | 1.0 | yes | ok |
| 0.76 | 26/34 | 2 | 4.2367s | 2.3324s | 6.1411s | 1.0 | yes | ok |
| 0.79 | 27/34 | 2 | 5.8054s | 5.4898s | 6.1209s | 1.0 | yes | ok |
| 0.82 | 28/34 | 2 | 6.0274s | 5.8925s | 6.1623s | 1.0 | yes | ok |
| 0.85 | 29/34 | 2 | 5.2464s | 5.0146s | 5.4782s | 1.0 | yes | ok |
| 0.88 | 30/34 | 2 | 4.3401s | 2.3935s | 6.2866s | 1.0 | yes | ok |
| 0.91 | 31/34 | 2 | 6.0506s | 5.8346s | 6.2667s | 1.0 | yes | ok |
| 0.94 | 32/34 | 2 | 6.0175s | 5.8692s | 6.1658s | 1.0 | yes | ok |
| 0.97 | 33/34 | 2 | 6.3098s | 6.3018s | 6.3179s | 1.0 | yes | ok |
| 1.00 | 34/34 | 1 | 6.2527s | 6.2527s | 6.2527s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/34 | 1 | 1.2113s | 0.0904s | 1 | 8 | yes | 1.1563s | 1.2736s | `detyped_files/deltablue/advanced/proportion_sweep/main_k00_s01.py` |  |
| 0.03 | 1/34 | 1 | 1.2178s | 0.0940s | 1 | 8 | yes | 1.1612s | 1.2843s | `detyped_files/deltablue/advanced/proportion_sweep/main_k01_s01.py` |  |
| 0.03 | 1/34 | 2 | 1.2774s | 0.1533s | 1 | 8 | yes | 1.1906s | 1.3834s | `detyped_files/deltablue/advanced/proportion_sweep/main_k01_s02.py` |  |
| 0.06 | 2/34 | 1 | 1.2814s | 0.1131s | 1 | 8 | yes | 1.2134s | 1.3603s | `detyped_files/deltablue/advanced/proportion_sweep/main_k02_s01.py` |  |
| 0.06 | 2/34 | 2 | 1.5760s | 0.1430s | 1 | 8 | yes | 1.5064s | 1.6800s | `detyped_files/deltablue/advanced/proportion_sweep/main_k02_s02.py` |  |
| 0.09 | 3/34 | 1 | 1.2783s | 0.1751s | 1 | 8 | yes | 1.1757s | 1.3969s | `detyped_files/deltablue/advanced/proportion_sweep/main_k03_s01.py` |  |
| 0.09 | 3/34 | 2 | 1.3792s | 0.1629s | 1 | 8 | yes | 1.2876s | 1.4930s | `detyped_files/deltablue/advanced/proportion_sweep/main_k03_s02.py` |  |
| 0.12 | 4/34 | 1 | 1.2991s | 0.1241s | 1 | 8 | yes | 1.2282s | 1.3903s | `detyped_files/deltablue/advanced/proportion_sweep/main_k04_s01.py` |  |
| 0.12 | 4/34 | 2 | 1.2968s | 0.1826s | 2 | 16 | yes | 1.2152s | 1.3914s | `detyped_files/deltablue/advanced/proportion_sweep/main_k04_s02.py` |  |
| 0.15 | 5/34 | 1 | 1.3474s | 0.1122s | 1 | 8 | yes | 1.2834s | 1.4254s | `detyped_files/deltablue/advanced/proportion_sweep/main_k05_s01.py` |  |
| 0.15 | 5/34 | 2 | 1.2610s | 0.1320s | 1 | 8 | yes | 1.1845s | 1.3545s | `detyped_files/deltablue/advanced/proportion_sweep/main_k05_s02.py` |  |
| 0.18 | 6/34 | 1 | 1.3685s | 0.1828s | 1 | 8 | yes | 1.2574s | 1.4904s | `detyped_files/deltablue/advanced/proportion_sweep/main_k06_s01.py` |  |
| 0.18 | 6/34 | 2 | 1.2751s | 0.1540s | 1 | 8 | yes | 1.1811s | 1.3749s | `detyped_files/deltablue/advanced/proportion_sweep/main_k06_s02.py` |  |
| 0.21 | 7/34 | 1 | 1.2455s | 0.0841s | 1 | 8 | yes | 1.2098s | 1.3066s | `detyped_files/deltablue/advanced/proportion_sweep/main_k07_s01.py` |  |
| 0.21 | 7/34 | 2 | 1.4284s | 0.1588s | 1 | 8 | yes | 1.3243s | 1.5332s | `detyped_files/deltablue/advanced/proportion_sweep/main_k07_s02.py` |  |
| 0.24 | 8/34 | 1 | 4.9586s | 0.1092s | 1 | 8 | yes | 4.8992s | 5.0371s | `detyped_files/deltablue/advanced/proportion_sweep/main_k08_s01.py` |  |
| 0.24 | 8/34 | 2 | 1.1819s | 0.0575s | 1 | 8 | yes | 1.1514s | 1.2237s | `detyped_files/deltablue/advanced/proportion_sweep/main_k08_s02.py` |  |
| 0.26 | 9/34 | 1 | 1.4136s | 0.1091s | 1 | 8 | yes | 1.3574s | 1.4925s | `detyped_files/deltablue/advanced/proportion_sweep/main_k09_s01.py` |  |
| 0.26 | 9/34 | 2 | 1.4455s | 0.1713s | 1 | 8 | yes | 1.3469s | 1.5655s | `detyped_files/deltablue/advanced/proportion_sweep/main_k09_s02.py` |  |
| 0.29 | 10/34 | 1 | 1.2011s | 0.0378s | 1 | 8 | yes | 1.1765s | 1.2254s | `detyped_files/deltablue/advanced/proportion_sweep/main_k10_s01.py` |  |
| 0.29 | 10/34 | 2 | 5.2223s | 0.1100s | 1 | 8 | yes | 5.1515s | 5.2934s | `detyped_files/deltablue/advanced/proportion_sweep/main_k10_s02.py` |  |
| 0.32 | 11/34 | 1 | 5.1730s | 0.0743s | 1 | 8 | yes | 5.1248s | 5.2204s | `detyped_files/deltablue/advanced/proportion_sweep/main_k11_s01.py` |  |
| 0.32 | 11/34 | 2 | - | - | - | - | - | - | - | `detyped_files/deltablue/advanced/proportion_sweep/main_k11_s02.py` | benchmark script failed (1): detyped_files/deltablue/advanced/proportion_sweep/main_k11_s02.py
docker error: container create: Cannot connect to the Docker daemon at unix:///Users/robertmorelli/.docker/run/docker.sock. Is the docker daemon running? |
| 0.35 | 12/34 | 1 | 4.6909s | 0.1344s | 1 | 8 | yes | 4.6130s | 4.7817s | `detyped_files/deltablue/advanced/proportion_sweep/main_k12_s01.py` |  |
| 0.35 | 12/34 | 2 | 1.9199s | 0.2145s | 1 | 8 | yes | 1.7940s | 2.0703s | `detyped_files/deltablue/advanced/proportion_sweep/main_k12_s02.py` |  |
| 0.38 | 13/34 | 1 | 1.7408s | 0.1209s | 1 | 8 | yes | 1.6714s | 1.8255s | `detyped_files/deltablue/advanced/proportion_sweep/main_k13_s01.py` |  |
| 0.38 | 13/34 | 2 | 1.3850s | 0.1735s | 1 | 8 | yes | 1.2848s | 1.5023s | `detyped_files/deltablue/advanced/proportion_sweep/main_k13_s02.py` |  |
| 0.41 | 14/34 | 1 | 5.0184s | 0.1148s | 1 | 8 | yes | 4.9368s | 5.0844s | `detyped_files/deltablue/advanced/proportion_sweep/main_k14_s01.py` |  |
| 0.41 | 14/34 | 2 | 1.7423s | 0.1270s | 1 | 8 | yes | 1.6698s | 1.8329s | `detyped_files/deltablue/advanced/proportion_sweep/main_k14_s02.py` |  |
| 0.44 | 15/34 | 1 | 1.4773s | 0.1439s | 1 | 8 | yes | 1.3871s | 1.5733s | `detyped_files/deltablue/advanced/proportion_sweep/main_k15_s01.py` |  |
| 0.44 | 15/34 | 2 | 5.6349s | 0.3711s | 1 | 8 | yes | 5.4209s | 5.8959s | `detyped_files/deltablue/advanced/proportion_sweep/main_k15_s02.py` |  |
| 0.47 | 16/34 | 1 | 5.6630s | 0.1636s | 1 | 8 | yes | 5.5639s | 5.7741s | `detyped_files/deltablue/advanced/proportion_sweep/main_k16_s01.py` |  |
| 0.47 | 16/34 | 2 | 5.3731s | 0.1228s | 1 | 8 | yes | 5.2893s | 5.4472s | `detyped_files/deltablue/advanced/proportion_sweep/main_k16_s02.py` |  |
| 0.50 | 17/34 | 1 | 1.3455s | 0.1287s | 1 | 8 | yes | 1.2795s | 1.4383s | `detyped_files/deltablue/advanced/proportion_sweep/main_k17_s01.py` |  |
| 0.50 | 17/34 | 2 | 5.0908s | 0.1406s | 1 | 8 | yes | 5.0015s | 5.1830s | `detyped_files/deltablue/advanced/proportion_sweep/main_k17_s02.py` |  |
| 0.53 | 18/34 | 1 | 5.7488s | 0.1644s | 1 | 8 | yes | 5.6458s | 5.8625s | `detyped_files/deltablue/advanced/proportion_sweep/main_k18_s01.py` |  |
| 0.53 | 18/34 | 2 | 4.8042s | 0.1289s | 1 | 8 | yes | 4.7232s | 4.8910s | `detyped_files/deltablue/advanced/proportion_sweep/main_k18_s02.py` |  |
| 0.56 | 19/34 | 1 | 4.9676s | 0.1543s | 1 | 8 | yes | 4.8791s | 5.0756s | `detyped_files/deltablue/advanced/proportion_sweep/main_k19_s01.py` |  |
| 0.56 | 19/34 | 2 | 5.4303s | 0.1248s | 1 | 8 | yes | 5.3491s | 5.5130s | `detyped_files/deltablue/advanced/proportion_sweep/main_k19_s02.py` |  |
| 0.59 | 20/34 | 1 | 2.2714s | 0.2002s | 1 | 8 | yes | 2.1522s | 2.4095s | `detyped_files/deltablue/advanced/proportion_sweep/main_k20_s01.py` |  |
| 0.59 | 20/34 | 2 | 5.4350s | 0.1402s | 1 | 8 | yes | 5.3438s | 5.5232s | `detyped_files/deltablue/advanced/proportion_sweep/main_k20_s02.py` |  |
| 0.62 | 21/34 | 1 | 5.6809s | 0.1155s | 1 | 8 | yes | 5.6104s | 5.7572s | `detyped_files/deltablue/advanced/proportion_sweep/main_k21_s01.py` |  |
| 0.62 | 21/34 | 2 | 1.4759s | 0.1150s | 1 | 8 | yes | 1.4169s | 1.5603s | `detyped_files/deltablue/advanced/proportion_sweep/main_k21_s02.py` |  |
| 0.65 | 22/34 | 1 | 5.4486s | 0.1128s | 1 | 8 | yes | 5.3728s | 5.5186s | `detyped_files/deltablue/advanced/proportion_sweep/main_k22_s01.py` |  |
| 0.65 | 22/34 | 2 | 5.5636s | 0.1001s | 1 | 8 | yes | 5.5023s | 5.6297s | `detyped_files/deltablue/advanced/proportion_sweep/main_k22_s02.py` |  |
| 0.68 | 23/34 | 1 | 1.8284s | 0.1507s | 1 | 8 | yes | 1.7355s | 1.9266s | `detyped_files/deltablue/advanced/proportion_sweep/main_k23_s01.py` |  |
| 0.68 | 23/34 | 2 | 2.2723s | 0.0962s | 1 | 8 | yes | 2.2074s | 2.3358s | `detyped_files/deltablue/advanced/proportion_sweep/main_k23_s02.py` |  |
| 0.71 | 24/34 | 1 | 5.7461s | 0.1695s | 1 | 8 | yes | 5.6471s | 5.8669s | `detyped_files/deltablue/advanced/proportion_sweep/main_k24_s01.py` |  |
| 0.71 | 24/34 | 2 | 5.9620s | 0.2546s | 1 | 8 | yes | 5.8341s | 6.1501s | `detyped_files/deltablue/advanced/proportion_sweep/main_k24_s02.py` |  |
| 0.74 | 25/34 | 1 | 5.7350s | 0.4415s | 1 | 8 | yes | 5.4688s | 6.0367s | `detyped_files/deltablue/advanced/proportion_sweep/main_k25_s01.py` |  |
| 0.74 | 25/34 | 2 | 5.7140s | 0.4301s | 1 | 8 | yes | 5.5013s | 6.0312s | `detyped_files/deltablue/advanced/proportion_sweep/main_k25_s02.py` |  |
| 0.76 | 26/34 | 1 | 6.1411s | 0.7187s | 1 | 8 | yes | 5.7300s | 6.6558s | `detyped_files/deltablue/advanced/proportion_sweep/main_k26_s01.py` |  |
| 0.76 | 26/34 | 2 | 2.3324s | 0.1819s | 1 | 8 | yes | 2.2220s | 2.4573s | `detyped_files/deltablue/advanced/proportion_sweep/main_k26_s02.py` |  |
| 0.79 | 27/34 | 1 | 6.1209s | 0.1006s | 1 | 8 | yes | 6.0583s | 6.1870s | `detyped_files/deltablue/advanced/proportion_sweep/main_k27_s01.py` |  |
| 0.79 | 27/34 | 2 | 5.4898s | 0.0936s | 1 | 8 | yes | 5.4306s | 5.5528s | `detyped_files/deltablue/advanced/proportion_sweep/main_k27_s02.py` |  |
| 0.82 | 28/34 | 1 | 5.8925s | 0.1183s | 1 | 8 | yes | 5.8210s | 5.9729s | `detyped_files/deltablue/advanced/proportion_sweep/main_k28_s01.py` |  |
| 0.82 | 28/34 | 2 | 6.1623s | 0.1711s | 1 | 8 | yes | 6.0518s | 6.2754s | `detyped_files/deltablue/advanced/proportion_sweep/main_k28_s02.py` |  |
| 0.85 | 29/34 | 1 | 5.0146s | 0.0816s | 1 | 8 | yes | 4.9623s | 5.0671s | `detyped_files/deltablue/advanced/proportion_sweep/main_k29_s01.py` |  |
| 0.85 | 29/34 | 2 | 5.4782s | 0.1545s | 1 | 8 | yes | 5.3768s | 5.5802s | `detyped_files/deltablue/advanced/proportion_sweep/main_k29_s02.py` |  |
| 0.88 | 30/34 | 1 | 6.2866s | 0.2446s | 1 | 8 | yes | 6.1521s | 6.4557s | `detyped_files/deltablue/advanced/proportion_sweep/main_k30_s01.py` |  |
| 0.88 | 30/34 | 2 | 2.3935s | 0.1394s | 1 | 8 | yes | 2.3082s | 2.4876s | `detyped_files/deltablue/advanced/proportion_sweep/main_k30_s02.py` |  |
| 0.91 | 31/34 | 1 | 5.8346s | 0.2142s | 1 | 8 | yes | 5.7019s | 5.9753s | `detyped_files/deltablue/advanced/proportion_sweep/main_k31_s01.py` |  |
| 0.91 | 31/34 | 2 | 6.2667s | 0.1923s | 1 | 8 | yes | 6.1420s | 6.3918s | `detyped_files/deltablue/advanced/proportion_sweep/main_k31_s02.py` |  |
| 0.94 | 32/34 | 1 | 5.8692s | 0.2507s | 1 | 8 | yes | 5.7094s | 6.0394s | `detyped_files/deltablue/advanced/proportion_sweep/main_k32_s01.py` |  |
| 0.94 | 32/34 | 2 | 6.1658s | 0.1625s | 1 | 8 | yes | 6.0627s | 6.2718s | `detyped_files/deltablue/advanced/proportion_sweep/main_k32_s02.py` |  |
| 0.97 | 33/34 | 1 | 6.3018s | 0.1954s | 1 | 8 | yes | 6.1791s | 6.4304s | `detyped_files/deltablue/advanced/proportion_sweep/main_k33_s01.py` |  |
| 0.97 | 33/34 | 2 | 6.3179s | 0.3291s | 1 | 8 | yes | 6.1214s | 6.5462s | `detyped_files/deltablue/advanced/proportion_sweep/main_k33_s02.py` |  |
| 1.00 | 34/34 | 1 | 6.2527s | 0.3329s | 1 | 8 | yes | 6.0722s | 6.4916s | `detyped_files/deltablue/advanced/proportion_sweep/main_k34_s01.py` |  |

## deltablue/shallow

- Detypable targets: `35`
- Total runs: `70`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/35 | 1 | 0.9533s | 0.9533s | 0.9533s | 1.0 | yes | ok |
| 0.03 | 1/35 | 2 | 0.9787s | 0.9780s | 0.9793s | 1.0 | yes | ok |
| 0.06 | 2/35 | 2 | 1.1062s | 1.0601s | 1.1523s | 1.0 | yes | ok |
| 0.09 | 3/35 | 2 | 1.0526s | 0.9664s | 1.1388s | 1.0 | yes | ok |
| 0.11 | 4/35 | 2 | 0.9797s | 0.9659s | 0.9936s | 1.0 | yes | ok |
| 0.14 | 5/35 | 2 | 1.1667s | 0.9666s | 1.3667s | 1.5 | yes | ok |
| 0.17 | 6/35 | 2 | 1.6725s | 1.4654s | 1.8795s | 1.0 | yes | ok |
| 0.20 | 7/35 | 2 | 1.2914s | 1.1461s | 1.4367s | 1.0 | yes | ok |
| 0.23 | 8/35 | 2 | 1.2597s | 1.0333s | 1.4860s | 1.0 | yes | ok |
| 0.26 | 9/35 | 2 | 1.1492s | 1.0634s | 1.2349s | 1.0 | yes | ok |
| 0.29 | 10/35 | 2 | 1.1551s | 0.9925s | 1.3178s | 1.0 | yes | ok |
| 0.31 | 11/35 | 2 | 1.3022s | 1.2849s | 1.3195s | 1.0 | yes | ok |
| 0.34 | 12/35 | 2 | 1.4355s | 1.3394s | 1.5316s | 1.0 | yes | ok |
| 0.37 | 13/35 | 2 | 1.5786s | 1.5149s | 1.6423s | 1.0 | yes | ok |
| 0.40 | 14/35 | 2 | 1.1166s | 1.0617s | 1.1715s | 1.0 | yes | ok |
| 0.43 | 15/35 | 2 | 1.4748s | 1.4517s | 1.4978s | 1.0 | yes | ok |
| 0.46 | 16/35 | 2 | 1.4484s | 1.3475s | 1.5494s | 1.0 | yes | ok |
| 0.49 | 17/35 | 2 | 1.3940s | 1.3454s | 1.4425s | 1.0 | yes | ok |
| 0.51 | 18/35 | 2 | 1.5310s | 1.3469s | 1.7151s | 1.0 | yes | ok |
| 0.54 | 19/35 | 2 | 1.4924s | 1.1142s | 1.8706s | 2.0 | yes | ok |
| 0.57 | 20/35 | 2 | 1.6208s | 1.4481s | 1.7935s | 2.0 | yes | ok |
| 0.60 | 21/35 | 2 | 1.5899s | 1.2994s | 1.8803s | 1.0 | yes | ok |
| 0.63 | 22/35 | 2 | 1.7323s | 1.4601s | 2.0044s | 2.0 | yes | ok |
| 0.66 | 23/35 | 2 | 2.1315s | 2.0906s | 2.1724s | 1.0 | yes | ok |
| 0.69 | 24/35 | 2 | 2.0864s | 1.9283s | 2.2446s | 1.0 | yes | ok |
| 0.71 | 25/35 | 2 | 1.8461s | 1.5320s | 2.1601s | 1.5 | yes | ok |
| 0.74 | 26/35 | 2 | 1.8160s | 1.7933s | 1.8387s | 1.5 | yes | ok |
| 0.77 | 27/35 | 2 | 2.1005s | 1.8925s | 2.3084s | 1.0 | yes | ok |
| 0.80 | 28/35 | 2 | 1.9552s | 1.8183s | 2.0920s | 1.5 | yes | ok |
| 0.83 | 29/35 | 2 | 1.8692s | 1.7366s | 2.0018s | 1.0 | yes | ok |
| 0.86 | 30/35 | 2 | 2.1743s | 2.1714s | 2.1772s | 1.0 | yes | ok |
| 0.89 | 31/35 | 2 | 2.3342s | 2.3260s | 2.3424s | 1.0 | yes | ok |
| 0.91 | 32/35 | 2 | 2.3859s | 2.3850s | 2.3869s | 1.0 | yes | ok |
| 0.94 | 33/35 | 2 | 2.1530s | 2.0640s | 2.2420s | 1.5 | yes | ok |
| 0.97 | 34/35 | 2 | 2.3287s | 2.2970s | 2.3604s | 1.0 | yes | ok |
| 1.00 | 35/35 | 1 | 2.3566s | 2.3566s | 2.3566s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/35 | 1 | 0.9533s | 0.0555s | 1 | 8 | yes | 0.9245s | 0.9929s | `detyped_files/deltablue/shallow/proportion_sweep/main_k00_s01.py` |  |
| 0.03 | 1/35 | 1 | 0.9793s | 0.1332s | 1 | 8 | yes | 0.9227s | 1.0759s | `detyped_files/deltablue/shallow/proportion_sweep/main_k01_s01.py` |  |
| 0.03 | 1/35 | 2 | 0.9780s | 0.1001s | 1 | 8 | yes | 0.9297s | 1.0492s | `detyped_files/deltablue/shallow/proportion_sweep/main_k01_s02.py` |  |
| 0.06 | 2/35 | 1 | 1.0601s | 0.1269s | 1 | 8 | yes | 0.9806s | 1.1450s | `detyped_files/deltablue/shallow/proportion_sweep/main_k02_s01.py` |  |
| 0.06 | 2/35 | 2 | 1.1523s | 0.0975s | 1 | 8 | yes | 1.0900s | 1.2189s | `detyped_files/deltablue/shallow/proportion_sweep/main_k02_s02.py` |  |
| 0.09 | 3/35 | 1 | 0.9664s | 0.0768s | 1 | 8 | yes | 0.9283s | 1.0239s | `detyped_files/deltablue/shallow/proportion_sweep/main_k03_s01.py` |  |
| 0.09 | 3/35 | 2 | 1.1388s | 0.0842s | 1 | 8 | yes | 1.0882s | 1.1946s | `detyped_files/deltablue/shallow/proportion_sweep/main_k03_s02.py` |  |
| 0.11 | 4/35 | 1 | 0.9659s | 0.0638s | 1 | 8 | yes | 0.9298s | 1.0085s | `detyped_files/deltablue/shallow/proportion_sweep/main_k04_s01.py` |  |
| 0.11 | 4/35 | 2 | 0.9936s | 0.1121s | 1 | 8 | yes | 0.9314s | 1.0703s | `detyped_files/deltablue/shallow/proportion_sweep/main_k04_s02.py` |  |
| 0.14 | 5/35 | 1 | 1.3667s | 0.2126s | 2 | 16 | yes | 1.2765s | 1.4787s | `detyped_files/deltablue/shallow/proportion_sweep/main_k05_s01.py` |  |
| 0.14 | 5/35 | 2 | 0.9666s | 0.0672s | 1 | 8 | yes | 0.9316s | 1.0152s | `detyped_files/deltablue/shallow/proportion_sweep/main_k05_s02.py` |  |
| 0.17 | 6/35 | 1 | 1.4654s | 0.1156s | 1 | 8 | yes | 1.3991s | 1.5443s | `detyped_files/deltablue/shallow/proportion_sweep/main_k06_s01.py` |  |
| 0.17 | 6/35 | 2 | 1.8795s | 0.1971s | 1 | 8 | yes | 1.7707s | 2.0185s | `detyped_files/deltablue/shallow/proportion_sweep/main_k06_s02.py` |  |
| 0.20 | 7/35 | 1 | 1.1461s | 0.0193s | 1 | 8 | yes | 1.1345s | 1.1596s | `detyped_files/deltablue/shallow/proportion_sweep/main_k07_s01.py` |  |
| 0.20 | 7/35 | 2 | 1.4367s | 0.1974s | 1 | 8 | yes | 1.3271s | 1.5789s | `detyped_files/deltablue/shallow/proportion_sweep/main_k07_s02.py` |  |
| 0.23 | 8/35 | 1 | 1.4860s | 0.1705s | 1 | 8 | yes | 1.3828s | 1.6013s | `detyped_files/deltablue/shallow/proportion_sweep/main_k08_s01.py` |  |
| 0.23 | 8/35 | 2 | 1.0333s | 0.0971s | 1 | 8 | yes | 0.9757s | 1.0992s | `detyped_files/deltablue/shallow/proportion_sweep/main_k08_s02.py` |  |
| 0.26 | 9/35 | 1 | 1.0634s | 0.0230s | 1 | 8 | yes | 1.0497s | 1.0792s | `detyped_files/deltablue/shallow/proportion_sweep/main_k09_s01.py` |  |
| 0.26 | 9/35 | 2 | 1.2349s | 0.1131s | 1 | 8 | yes | 1.1904s | 1.3163s | `detyped_files/deltablue/shallow/proportion_sweep/main_k09_s02.py` |  |
| 0.29 | 10/35 | 1 | 0.9925s | 0.0691s | 1 | 8 | yes | 0.9531s | 1.0410s | `detyped_files/deltablue/shallow/proportion_sweep/main_k10_s01.py` |  |
| 0.29 | 10/35 | 2 | 1.3178s | 0.1116s | 1 | 8 | yes | 1.2517s | 1.3932s | `detyped_files/deltablue/shallow/proportion_sweep/main_k10_s02.py` |  |
| 0.31 | 11/35 | 1 | 1.2849s | 0.1418s | 1 | 8 | yes | 1.1981s | 1.3772s | `detyped_files/deltablue/shallow/proportion_sweep/main_k11_s01.py` |  |
| 0.31 | 11/35 | 2 | 1.3195s | 0.1661s | 1 | 8 | yes | 1.2155s | 1.4316s | `detyped_files/deltablue/shallow/proportion_sweep/main_k11_s02.py` |  |
| 0.34 | 12/35 | 1 | 1.5316s | 0.0706s | 1 | 8 | yes | 1.4893s | 1.5802s | `detyped_files/deltablue/shallow/proportion_sweep/main_k12_s01.py` |  |
| 0.34 | 12/35 | 2 | 1.3394s | 0.1419s | 1 | 8 | yes | 1.2581s | 1.4369s | `detyped_files/deltablue/shallow/proportion_sweep/main_k12_s02.py` |  |
| 0.37 | 13/35 | 1 | 1.6423s | 0.1868s | 1 | 8 | yes | 1.5433s | 1.7719s | `detyped_files/deltablue/shallow/proportion_sweep/main_k13_s01.py` |  |
| 0.37 | 13/35 | 2 | 1.5149s | 0.1344s | 1 | 8 | yes | 1.4429s | 1.6103s | `detyped_files/deltablue/shallow/proportion_sweep/main_k13_s02.py` |  |
| 0.40 | 14/35 | 1 | 1.1715s | 0.1078s | 1 | 8 | yes | 1.1054s | 1.2465s | `detyped_files/deltablue/shallow/proportion_sweep/main_k14_s01.py` |  |
| 0.40 | 14/35 | 2 | 1.0617s | 0.1308s | 1 | 8 | yes | 0.9863s | 1.1508s | `detyped_files/deltablue/shallow/proportion_sweep/main_k14_s02.py` |  |
| 0.43 | 15/35 | 1 | 1.4517s | 0.1888s | 1 | 8 | yes | 1.3743s | 1.5883s | `detyped_files/deltablue/shallow/proportion_sweep/main_k15_s01.py` |  |
| 0.43 | 15/35 | 2 | 1.4978s | 0.1489s | 1 | 8 | yes | 1.4151s | 1.6000s | `detyped_files/deltablue/shallow/proportion_sweep/main_k15_s02.py` |  |
| 0.46 | 16/35 | 1 | 1.3475s | 0.1373s | 1 | 8 | yes | 1.2661s | 1.4446s | `detyped_files/deltablue/shallow/proportion_sweep/main_k16_s01.py` |  |
| 0.46 | 16/35 | 2 | 1.5494s | 0.1588s | 1 | 8 | yes | 1.4666s | 1.6625s | `detyped_files/deltablue/shallow/proportion_sweep/main_k16_s02.py` |  |
| 0.49 | 17/35 | 1 | 1.3454s | 0.1626s | 1 | 8 | yes | 1.2457s | 1.4520s | `detyped_files/deltablue/shallow/proportion_sweep/main_k17_s01.py` |  |
| 0.49 | 17/35 | 2 | 1.4425s | 0.1568s | 1 | 8 | yes | 1.3638s | 1.5542s | `detyped_files/deltablue/shallow/proportion_sweep/main_k17_s02.py` |  |
| 0.51 | 18/35 | 1 | 1.7151s | 0.1279s | 1 | 8 | yes | 1.6414s | 1.8028s | `detyped_files/deltablue/shallow/proportion_sweep/main_k18_s01.py` |  |
| 0.51 | 18/35 | 2 | 1.3469s | 0.1721s | 1 | 8 | yes | 1.2536s | 1.4689s | `detyped_files/deltablue/shallow/proportion_sweep/main_k18_s02.py` |  |
| 0.54 | 19/35 | 1 | 1.1142s | 0.1333s | 2 | 16 | yes | 1.0723s | 1.1854s | `detyped_files/deltablue/shallow/proportion_sweep/main_k19_s01.py` |  |
| 0.54 | 19/35 | 2 | 1.8706s | 0.3539s | 2 | 16 | yes | 1.7226s | 2.0472s | `detyped_files/deltablue/shallow/proportion_sweep/main_k19_s02.py` |  |
| 0.57 | 20/35 | 1 | 1.7935s | 0.2010s | 2 | 16 | yes | 1.7146s | 1.9028s | `detyped_files/deltablue/shallow/proportion_sweep/main_k20_s01.py` |  |
| 0.57 | 20/35 | 2 | 1.4481s | 0.2436s | 2 | 16 | yes | 1.3537s | 1.5822s | `detyped_files/deltablue/shallow/proportion_sweep/main_k20_s02.py` |  |
| 0.60 | 21/35 | 1 | 1.2994s | 0.0642s | 1 | 8 | yes | 1.2734s | 1.3461s | `detyped_files/deltablue/shallow/proportion_sweep/main_k21_s01.py` |  |
| 0.60 | 21/35 | 2 | 1.8803s | 0.2377s | 1 | 8 | yes | 1.7432s | 2.0471s | `detyped_files/deltablue/shallow/proportion_sweep/main_k21_s02.py` |  |
| 0.63 | 22/35 | 1 | 2.0044s | 0.1790s | 1 | 8 | yes | 1.9145s | 2.1285s | `detyped_files/deltablue/shallow/proportion_sweep/main_k22_s01.py` |  |
| 0.63 | 22/35 | 2 | 1.4601s | 0.2443s | 3 | 24 | yes | 1.3818s | 1.5684s | `detyped_files/deltablue/shallow/proportion_sweep/main_k22_s02.py` |  |
| 0.66 | 23/35 | 1 | 2.0906s | 0.1260s | 1 | 8 | yes | 2.0298s | 2.1841s | `detyped_files/deltablue/shallow/proportion_sweep/main_k23_s01.py` |  |
| 0.66 | 23/35 | 2 | 2.1724s | 0.2624s | 1 | 8 | yes | 2.0355s | 2.3541s | `detyped_files/deltablue/shallow/proportion_sweep/main_k23_s02.py` |  |
| 0.69 | 24/35 | 1 | 2.2446s | 0.2376s | 1 | 8 | yes | 2.1092s | 2.4144s | `detyped_files/deltablue/shallow/proportion_sweep/main_k24_s01.py` |  |
| 0.69 | 24/35 | 2 | 1.9283s | 0.1871s | 1 | 8 | yes | 1.8327s | 2.0567s | `detyped_files/deltablue/shallow/proportion_sweep/main_k24_s02.py` |  |
| 0.71 | 25/35 | 1 | 2.1601s | 0.3188s | 2 | 16 | yes | 2.0225s | 2.3193s | `detyped_files/deltablue/shallow/proportion_sweep/main_k25_s01.py` |  |
| 0.71 | 25/35 | 2 | 1.5320s | 0.1115s | 1 | 8 | yes | 1.4831s | 1.6127s | `detyped_files/deltablue/shallow/proportion_sweep/main_k25_s02.py` |  |
| 0.74 | 26/35 | 1 | 1.8387s | 0.0452s | 1 | 8 | yes | 1.8122s | 1.8699s | `detyped_files/deltablue/shallow/proportion_sweep/main_k26_s01.py` |  |
| 0.74 | 26/35 | 2 | 1.7933s | 0.2198s | 2 | 16 | yes | 1.6961s | 1.9049s | `detyped_files/deltablue/shallow/proportion_sweep/main_k26_s02.py` |  |
| 0.77 | 27/35 | 1 | 2.3084s | 0.2064s | 1 | 8 | yes | 2.1926s | 2.4716s | `detyped_files/deltablue/shallow/proportion_sweep/main_k27_s01.py` |  |
| 0.77 | 27/35 | 2 | 1.8925s | 0.2147s | 1 | 8 | yes | 1.7733s | 2.0570s | `detyped_files/deltablue/shallow/proportion_sweep/main_k27_s02.py` |  |
| 0.80 | 28/35 | 1 | 2.0920s | 0.3161s | 2 | 16 | yes | 1.9538s | 2.2565s | `detyped_files/deltablue/shallow/proportion_sweep/main_k28_s01.py` |  |
| 0.80 | 28/35 | 2 | 1.8183s | 0.1416s | 1 | 8 | yes | 1.7534s | 1.9203s | `detyped_files/deltablue/shallow/proportion_sweep/main_k28_s02.py` |  |
| 0.83 | 29/35 | 1 | 1.7366s | 0.0093s | 1 | 8 | yes | 1.7321s | 1.7434s | `detyped_files/deltablue/shallow/proportion_sweep/main_k29_s01.py` |  |
| 0.83 | 29/35 | 2 | 2.0018s | 0.2533s | 1 | 8 | yes | 1.8538s | 2.1772s | `detyped_files/deltablue/shallow/proportion_sweep/main_k29_s02.py` |  |
| 0.86 | 30/35 | 1 | 2.1772s | 0.2513s | 1 | 8 | yes | 2.0392s | 2.3465s | `detyped_files/deltablue/shallow/proportion_sweep/main_k30_s01.py` |  |
| 0.86 | 30/35 | 2 | 2.1714s | 0.2378s | 1 | 8 | yes | 2.0786s | 2.3422s | `detyped_files/deltablue/shallow/proportion_sweep/main_k30_s02.py` |  |
| 0.89 | 31/35 | 1 | 2.3260s | 0.2717s | 1 | 8 | yes | 2.1767s | 2.5093s | `detyped_files/deltablue/shallow/proportion_sweep/main_k31_s01.py` |  |
| 0.89 | 31/35 | 2 | 2.3424s | 0.1859s | 1 | 8 | yes | 2.2348s | 2.4664s | `detyped_files/deltablue/shallow/proportion_sweep/main_k31_s02.py` |  |
| 0.91 | 32/35 | 1 | 2.3850s | 0.2961s | 1 | 8 | yes | 2.2438s | 2.6004s | `detyped_files/deltablue/shallow/proportion_sweep/main_k32_s01.py` |  |
| 0.91 | 32/35 | 2 | 2.3869s | 0.2716s | 1 | 8 | yes | 2.2381s | 2.5721s | `detyped_files/deltablue/shallow/proportion_sweep/main_k32_s02.py` |  |
| 0.94 | 33/35 | 1 | 2.0640s | 0.3023s | 2 | 16 | yes | 1.9291s | 2.2133s | `detyped_files/deltablue/shallow/proportion_sweep/main_k33_s01.py` |  |
| 0.94 | 33/35 | 2 | 2.2420s | 0.2624s | 1 | 8 | yes | 2.0997s | 2.4228s | `detyped_files/deltablue/shallow/proportion_sweep/main_k33_s02.py` |  |
| 0.97 | 34/35 | 1 | 2.3604s | 0.2321s | 1 | 8 | yes | 2.2340s | 2.5301s | `detyped_files/deltablue/shallow/proportion_sweep/main_k34_s01.py` |  |
| 0.97 | 34/35 | 2 | 2.2970s | 0.2649s | 1 | 8 | yes | 2.1477s | 2.4828s | `detyped_files/deltablue/shallow/proportion_sweep/main_k34_s02.py` |  |
| 1.00 | 35/35 | 1 | 2.3566s | 0.2573s | 1 | 8 | yes | 2.2166s | 2.5304s | `detyped_files/deltablue/shallow/proportion_sweep/main_k35_s01.py` |  |

## deltablue/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | - | - | - | - | - | 1 failed |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | - | - | - | - | - | - | - | `static-python-perf/Benchmark/deltablue/untyped/main.py` | benchmark script failed (1): static-python-perf/Benchmark/deltablue/untyped/main.py
Traceback (most recent call last):
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/types.py", line 8224, in _generic_bind
    ret_types.append(callback(el, result_types))
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/types.py", line 8236, in cb
    el.instance.bind_attr(node, visitor, type_ctx)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/types.py", line 2438, in bind_attr
    visitor.syntax_error(f"'NoneType' object has no attribute '{node.attr}'", node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 74, in syntax_error
    return self.error_sink.syntax_error(msg, self.filename, node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/errors.py", line 52, in syntax_error
    self.error(TypedSyntaxError(msg, (filename, lineno, offset, source_line)))
  File "/cinder/cinderx/PythonLib/cinderx/compiler/errors.py", line 48, in error
    raise exception
  File "static-python-perf/Benchmark/deltablue/untyped/main.py", line 593
    first.value = i
cinderx.compiler.errors.TypedSyntaxError: 'NoneType' object has no attribute 'value'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/cinder/Lib/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/cinder/Lib/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/__main__.py", line 82, in <module>
    codeobj = pycodegen.compile(
  File "/cinder/cinderx/PythonLib/cinderx/compiler/pycodegen.py", line 131, in compile
    result = make_compiler(source, filename, mode, flags, optimize, compiler, modname)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/pycodegen.py", line 172, in make_compiler
    return generator.make_code_gen(
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/__init__.py", line 301, in make_code_gen
    code_gen = compiler.code_gen(
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/compiler.py", line 535, in code_gen
    tree, s = self._bind(name, filename, tree, optimize, enable_patching)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/compiler.py", line 509, in _bind
    type_binder.visit(tree)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 458, in visitModule
    self.visit(stmt)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 628, in visitFunctionDef
    self._visitFunc(node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 616, in _visitFunc
    func.bind_function(node, self)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/types.py", line 3136, in bind_function
    terminates = visitor.visit_check_terminal(self.get_function_body())
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 1787, in visit_check_terminal
    self.visit(stmt)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 1970, in visitWhile
    terminal_level = self.visit_check_terminal(node.body)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 1787, in visit_check_terminal
    self.visit(stmt)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 859, in visitAssign
    self.visit(target)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 1522, in visitAttribute
    base.bind_attr(node, self, type_ctx)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/types.py", line 8239, in bind_attr
    self._generic_bind(node, cb, "access attribute from", visitor, type_ctx)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/types.py", line 8226, in _generic_bind
    visitor.syntax_error(f"{self.name}: {e.msg}", node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 74, in syntax_error
    return self.error_sink.syntax_error(msg, self.filename, node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/errors.py", line 52, in syntax_error
    self.error(TypedSyntaxError(msg, (filename, lineno, offset, source_line)))
  File "/cinder/cinderx/PythonLib/cinderx/compiler/errors.py", line 48, in error
    raise exception
  File "static-python-perf/Benchmark/deltablue/untyped/main.py", line 593
    first.value = i
cinderx.compiler.errors.TypedSyntaxError: Optional[__main__.Variable]: 'NoneType' object has no attribute 'value' |

## fannkuch/advanced

- Detypable targets: `1`
- Total runs: `2`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/1 | 1 | 1.9261s | 1.9261s | 1.9261s | 1.0 | yes | ok |
| 1.00 | 1/1 | 1 | 2.1778s | 2.1778s | 2.1778s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/1 | 1 | 1.9261s | 0.0334s | 1 | 8 | yes | 1.9097s | 1.9499s | `detyped_files/fannkuch/advanced/proportion_sweep/main_k00_s01.py` |  |
| 1.00 | 1/1 | 1 | 2.1778s | 0.1872s | 1 | 8 | yes | 2.0829s | 2.3101s | `detyped_files/fannkuch/advanced/proportion_sweep/main_k01_s01.py` |  |

## fannkuch/shallow

- Detypable targets: `1`
- Total runs: `2`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/1 | 1 | 0.6332s | 0.6332s | 0.6332s | 4.0 | yes | ok |
| 1.00 | 1/1 | 1 | - | - | - | - | - | 1 failed |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/1 | 1 | 0.6332s | 0.1386s | 4 | 32 | yes | 0.5929s | 0.6850s | `detyped_files/fannkuch/shallow/proportion_sweep/main_k00_s01.py` |  |
| 1.00 | 1/1 | 1 | - | - | - | - | - | - | - | `detyped_files/fannkuch/shallow/proportion_sweep/main_k01_s01.py` | benchmark script failed (1): detyped_files/fannkuch/shallow/proportion_sweep/main_k01_s01.py
docker error: container create: Cannot connect to the Docker daemon at unix:///Users/robertmorelli/.docker/run/docker.sock. Is the docker daemon running? |

## fannkuch/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.5794s | 0.5794s | 0.5794s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.5794s | 0.0007s | 1 | 8 | yes | 0.5789s | 0.5799s | `static-python-perf/Benchmark/fannkuch/untyped/main.py` |  |

## float/advanced

- Detypable targets: `5`
- Total runs: `10`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/5 | 1 | 0.4400s | 0.4400s | 0.4400s | 1.0 | yes | ok |
| 0.20 | 1/5 | 2 | 0.5638s | 0.4370s | 0.6905s | 1.0 | yes | ok |
| 0.40 | 2/5 | 2 | 0.6155s | 0.5207s | 0.7103s | 2.0 | yes | ok |
| 0.60 | 3/5 | 2 | 0.5935s | 0.4997s | 0.6872s | 1.0 | yes | ok |
| 0.80 | 4/5 | 2 | 0.6368s | 0.5231s | 0.7506s | 1.0 | yes | ok |
| 1.00 | 5/5 | 1 | 0.8091s | 0.8091s | 0.8091s | 5.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/5 | 1 | 0.4400s | 0.0039s | 1 | 8 | yes | 0.4376s | 0.4426s | `detyped_files/float/advanced/proportion_sweep/main_k00_s01.py` |  |
| 0.20 | 1/5 | 1 | 0.4370s | 0.0023s | 1 | 8 | yes | 0.4357s | 0.4386s | `detyped_files/float/advanced/proportion_sweep/main_k01_s01.py` |  |
| 0.20 | 1/5 | 2 | 0.6905s | 0.0748s | 1 | 8 | yes | 0.6613s | 0.7443s | `detyped_files/float/advanced/proportion_sweep/main_k01_s02.py` |  |
| 0.40 | 2/5 | 1 | 0.5207s | 0.0523s | 1 | 8 | yes | 0.4995s | 0.5586s | `detyped_files/float/advanced/proportion_sweep/main_k02_s01.py` |  |
| 0.40 | 2/5 | 2 | 0.7103s | 0.1128s | 3 | 24 | yes | 0.6769s | 0.7626s | `detyped_files/float/advanced/proportion_sweep/main_k02_s02.py` |  |
| 0.60 | 3/5 | 1 | 0.4997s | 0.0032s | 1 | 8 | yes | 0.4977s | 0.5019s | `detyped_files/float/advanced/proportion_sweep/main_k03_s01.py` |  |
| 0.60 | 3/5 | 2 | 0.6872s | 0.0218s | 1 | 8 | yes | 0.6761s | 0.7032s | `detyped_files/float/advanced/proportion_sweep/main_k03_s02.py` |  |
| 0.80 | 4/5 | 1 | 0.5231s | 0.0391s | 1 | 8 | yes | 0.5086s | 0.5509s | `detyped_files/float/advanced/proportion_sweep/main_k04_s01.py` |  |
| 0.80 | 4/5 | 2 | 0.7506s | 0.0248s | 1 | 8 | yes | 0.7390s | 0.7691s | `detyped_files/float/advanced/proportion_sweep/main_k04_s02.py` |  |
| 1.00 | 5/5 | 1 | 0.8091s | 0.2138s | 5 | 40 | yes | 0.7543s | 0.8847s | `detyped_files/float/advanced/proportion_sweep/main_k05_s01.py` |  |

## float/shallow

- Detypable targets: `3`
- Total runs: `6`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/3 | 1 | 0.4689s | 0.4689s | 0.4689s | 1.0 | yes | ok |
| 0.33 | 1/3 | 2 | 0.4556s | 0.4307s | 0.4806s | 1.0 | yes | ok |
| 0.67 | 2/3 | 2 | 0.4948s | 0.4774s | 0.5121s | 2.5 | yes | ok |
| 1.00 | 3/3 | 1 | 0.4929s | 0.4929s | 0.4929s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/3 | 1 | 0.4689s | 0.0040s | 1 | 8 | yes | 0.4668s | 0.4718s | `detyped_files/float/shallow/proportion_sweep/main_k00_s01.py` |  |
| 0.33 | 1/3 | 1 | 0.4307s | 0.0337s | 1 | 8 | yes | 0.4180s | 0.4547s | `detyped_files/float/shallow/proportion_sweep/main_k01_s01.py` |  |
| 0.33 | 1/3 | 2 | 0.4806s | 0.0067s | 1 | 8 | yes | 0.4772s | 0.4856s | `detyped_files/float/shallow/proportion_sweep/main_k01_s02.py` |  |
| 0.67 | 2/3 | 1 | 0.4774s | 0.0034s | 1 | 8 | yes | 0.4754s | 0.4797s | `detyped_files/float/shallow/proportion_sweep/main_k02_s01.py` |  |
| 0.67 | 2/3 | 2 | 0.5121s | 0.1085s | 4 | 32 | yes | 0.4820s | 0.5545s | `detyped_files/float/shallow/proportion_sweep/main_k02_s02.py` |  |
| 1.00 | 3/3 | 1 | 0.4929s | 0.0292s | 1 | 8 | yes | 0.4805s | 0.5141s | `detyped_files/float/shallow/proportion_sweep/main_k03_s01.py` |  |

## float/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.5135s | 0.5135s | 0.5135s | 5.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.5135s | 0.1462s | 5 | 40 | yes | 0.4751s | 0.5643s | `static-python-perf/Benchmark/float/untyped/main.py` |  |

## nbody/advanced

- Detypable targets: `6`
- Total runs: `12`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 1.5900s | 1.5900s | 1.5900s | 2.0 | yes | ok |
| 0.17 | 1/6 | 2 | 1.5243s | 1.5127s | 1.5359s | 1.5 | yes | ok |
| 0.33 | 2/6 | 2 | 2.6310s | 1.4998s | 3.7622s | 1.0 | yes | ok |
| 0.50 | 3/6 | 2 | 2.6972s | 1.5047s | 3.8897s | 1.0 | yes | ok |
| 0.67 | 4/6 | 2 | 2.6252s | 1.4878s | 3.7626s | 1.0 | yes | ok |
| 0.83 | 5/6 | 2 | 2.6465s | 1.5084s | 3.7846s | 1.5 | yes | ok |
| 1.00 | 6/6 | 1 | 3.7201s | 3.7201s | 3.7201s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 1.5900s | 0.2788s | 2 | 16 | yes | 1.4723s | 1.7357s | `detyped_files/nbody/advanced/proportion_sweep/main_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 1.5127s | 0.1576s | 1 | 8 | yes | 1.4344s | 1.6216s | `detyped_files/nbody/advanced/proportion_sweep/main_k01_s01.py` |  |
| 0.17 | 1/6 | 2 | 1.5359s | 0.2594s | 2 | 16 | yes | 1.4355s | 1.6771s | `detyped_files/nbody/advanced/proportion_sweep/main_k01_s02.py` |  |
| 0.33 | 2/6 | 1 | 1.4998s | 0.1876s | 1 | 8 | yes | 1.4264s | 1.6344s | `detyped_files/nbody/advanced/proportion_sweep/main_k02_s01.py` |  |
| 0.33 | 2/6 | 2 | 3.7622s | 0.3057s | 1 | 8 | yes | 3.5901s | 3.9746s | `detyped_files/nbody/advanced/proportion_sweep/main_k02_s02.py` |  |
| 0.50 | 3/6 | 1 | 3.8897s | 0.3795s | 1 | 8 | yes | 3.6664s | 4.1531s | `detyped_files/nbody/advanced/proportion_sweep/main_k03_s01.py` |  |
| 0.50 | 3/6 | 2 | 1.5047s | 0.1496s | 1 | 8 | yes | 1.4304s | 1.6076s | `detyped_files/nbody/advanced/proportion_sweep/main_k03_s02.py` |  |
| 0.67 | 4/6 | 1 | 3.7626s | 0.2621s | 1 | 8 | yes | 3.6082s | 3.9454s | `detyped_files/nbody/advanced/proportion_sweep/main_k04_s01.py` |  |
| 0.67 | 4/6 | 2 | 1.4878s | 0.1606s | 1 | 8 | yes | 1.4305s | 1.6016s | `detyped_files/nbody/advanced/proportion_sweep/main_k04_s02.py` |  |
| 0.83 | 5/6 | 1 | 1.5084s | 0.2145s | 2 | 16 | yes | 1.4319s | 1.6222s | `detyped_files/nbody/advanced/proportion_sweep/main_k05_s01.py` |  |
| 0.83 | 5/6 | 2 | 3.7846s | 0.2159s | 1 | 8 | yes | 3.6321s | 3.9084s | `detyped_files/nbody/advanced/proportion_sweep/main_k05_s02.py` |  |
| 1.00 | 6/6 | 1 | 3.7201s | 0.2671s | 1 | 8 | yes | 3.5750s | 3.9081s | `detyped_files/nbody/advanced/proportion_sweep/main_k06_s01.py` |  |

## nbody/shallow

- Detypable targets: `6`
- Total runs: `12`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.8755s | 0.8755s | 0.8755s | 1.0 | yes | ok |
| 0.17 | 1/6 | 2 | 0.8540s | 0.8540s | 0.8540s | 1.0 | yes | 1 failed |
| 0.33 | 2/6 | 2 | - | - | - | - | - | 2 failed |
| 0.50 | 3/6 | 2 | 0.8545s | 0.8545s | 0.8545s | 1.0 | yes | 1 failed |
| 0.67 | 4/6 | 2 | 0.9119s | 0.9119s | 0.9119s | 2.0 | yes | 1 failed |
| 0.83 | 5/6 | 2 | - | - | - | - | - | 2 failed |
| 1.00 | 6/6 | 1 | - | - | - | - | - | 1 failed |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.8755s | 0.0350s | 1 | 8 | yes | 0.8566s | 0.8996s | `detyped_files/nbody/shallow/proportion_sweep/main_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 0.8540s | 0.0057s | 1 | 8 | yes | 0.8509s | 0.8581s | `detyped_files/nbody/shallow/proportion_sweep/main_k01_s01.py` |  |
| 0.17 | 1/6 | 2 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k01_s02.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k01_s02.py
Traceback (most recent call last):
  File "/cinder/Lib/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/cinder/Lib/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/__main__.py", line 82, in <module>
    codeobj = pycodegen.compile(
  File "/cinder/cinderx/PythonLib/cinderx/compiler/pycodegen.py", line 131, in compile
    result = make_compiler(source, filename, mode, flags, optimize, compiler, modname)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/pycodegen.py", line 172, in make_compiler
    return generator.make_code_gen(
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/__init__.py", line 301, in make_code_gen
    code_gen = compiler.code_gen(
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/compiler.py", line 535, in code_gen
    tree, s = self._bind(name, filename, tree, optimize, enable_patching)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/compiler.py", line 509, in _bind
    type_binder.visit(tree)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 458, in visitModule
    self.visit(stmt)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 628, in visitFunctionDef
    self._visitFunc(node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 616, in _visitFunc
    func.bind_function(node, self)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/types.py", line 3136, in bind_function
    terminates = visitor.visit_check_terminal(self.get_function_body())
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 1787, in visit_check_terminal
    self.visit(stmt)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 803, in visitAnnAssign
    self.visitExpectedType(value, declared_type)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 1653, in visitExpectedType
    res = self.visit(node, expected)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 1484, in visitCall
    return self.get_type(node.func).bind_call(node, self, type_ctx)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/types.py", line 8846, in bind_call
    visitor.syntax_error("cast to unknown type", node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 74, in syntax_error
    return self.error_sink.syntax_error(msg, self.filename, node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/errors.py", line 52, in syntax_error
    self.error(TypedSyntaxError(msg, (filename, lineno, offset, source_line)))
  File "/cinder/cinderx/PythonLib/cinderx/compiler/errors.py", line 48, in error
    raise exception
  File "detyped_files/nbody/shallow/proportion_sweep/main_k01_s02.py", line 72
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.33 | 2/6 | 1 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k02_s01.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k02_s01.py
Traceback (most recent call last):
  File "/cinder/Lib/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/cinder/Lib/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/__main__.py", line 82, in <module>
    codeobj = pycodegen.compile(
  File "/cinder/cinderx/PythonLib/cinderx/compiler/pycodegen.py", line 131, in compile
    result = make_compiler(source, filename, mode, flags, optimize, compiler, modname)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/pycodegen.py", line 172, in make_compiler
    return generator.make_code_gen(
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/__init__.py", line 301, in make_code_gen
    code_gen = compiler.code_gen(
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/compiler.py", line 535, in code_gen
    tree, s = self._bind(name, filename, tree, optimize, enable_patching)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/compiler.py", line 509, in _bind
    type_binder.visit(tree)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 458, in visitModule
    self.visit(stmt)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 628, in visitFunctionDef
    self._visitFunc(node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 616, in _visitFunc
    func.bind_function(node, self)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/types.py", line 3136, in bind_function
    terminates = visitor.visit_check_terminal(self.get_function_body())
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 1787, in visit_check_terminal
    self.visit(stmt)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 803, in visitAnnAssign
    self.visitExpectedType(value, declared_type)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 1653, in visitExpectedType
    res = self.visit(node, expected)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 1484, in visitCall
    return self.get_type(node.func).bind_call(node, self, type_ctx)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/types.py", line 8846, in bind_call
    visitor.syntax_error("cast to unknown type", node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 74, in syntax_error
    return self.error_sink.syntax_error(msg, self.filename, node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/errors.py", line 52, in syntax_error
    self.error(TypedSyntaxError(msg, (filename, lineno, offset, source_line)))
  File "/cinder/cinderx/PythonLib/cinderx/compiler/errors.py", line 48, in error
    raise exception
  File "detyped_files/nbody/shallow/proportion_sweep/main_k02_s01.py", line 73
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.33 | 2/6 | 2 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k02_s02.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k02_s02.py
Traceback (most recent call last):
  File "/cinder/Lib/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/cinder/Lib/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/__main__.py", line 82, in <module>
    codeobj = pycodegen.compile(
  File "/cinder/cinderx/PythonLib/cinderx/compiler/pycodegen.py", line 131, in compile
    result = make_compiler(source, filename, mode, flags, optimize, compiler, modname)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/pycodegen.py", line 172, in make_compiler
    return generator.make_code_gen(
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/__init__.py", line 301, in make_code_gen
    code_gen = compiler.code_gen(
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/compiler.py", line 535, in code_gen
    tree, s = self._bind(name, filename, tree, optimize, enable_patching)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/compiler.py", line 509, in _bind
    type_binder.visit(tree)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 458, in visitModule
    self.visit(stmt)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 628, in visitFunctionDef
    self._visitFunc(node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 616, in _visitFunc
    func.bind_function(node, self)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/types.py", line 3136, in bind_function
    terminates = visitor.visit_check_terminal(self.get_function_body())
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 1787, in visit_check_terminal
    self.visit(stmt)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 803, in visitAnnAssign
    self.visitExpectedType(value, declared_type)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 1653, in visitExpectedType
    res = self.visit(node, expected)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 1484, in visitCall
    return self.get_type(node.func).bind_call(node, self, type_ctx)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/types.py", line 8846, in bind_call
    visitor.syntax_error("cast to unknown type", node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 74, in syntax_error
    return self.error_sink.syntax_error(msg, self.filename, node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/errors.py", line 52, in syntax_error
    self.error(TypedSyntaxError(msg, (filename, lineno, offset, source_line)))
  File "/cinder/cinderx/PythonLib/cinderx/compiler/errors.py", line 48, in error
    raise exception
  File "detyped_files/nbody/shallow/proportion_sweep/main_k02_s02.py", line 72
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.50 | 3/6 | 1 | 0.8545s | 0.0041s | 1 | 8 | yes | 0.8526s | 0.8576s | `detyped_files/nbody/shallow/proportion_sweep/main_k03_s01.py` |  |
| 0.50 | 3/6 | 2 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k03_s02.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k03_s02.py
Traceback (most recent call last):
  File "/cinder/Lib/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/cinder/Lib/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/__main__.py", line 82, in <module>
    codeobj = pycodegen.compile(
  File "/cinder/cinderx/PythonLib/cinderx/compiler/pycodegen.py", line 131, in compile
    result = make_compiler(source, filename, mode, flags, optimize, compiler, modname)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/pycodegen.py", line 172, in make_compiler
    return generator.make_code_gen(
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/__init__.py", line 301, in make_code_gen
    code_gen = compiler.code_gen(
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/compiler.py", line 535, in code_gen
    tree, s = self._bind(name, filename, tree, optimize, enable_patching)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/compiler.py", line 509, in _bind
    type_binder.visit(tree)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 458, in visitModule
    self.visit(stmt)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 628, in visitFunctionDef
    self._visitFunc(node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 616, in _visitFunc
    func.bind_function(node, self)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/types.py", line 3136, in bind_function
    terminates = visitor.visit_check_terminal(self.get_function_body())
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 1787, in visit_check_terminal
    self.visit(stmt)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 803, in visitAnnAssign
    self.visitExpectedType(value, declared_type)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 1653, in visitExpectedType
    res = self.visit(node, expected)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 1484, in visitCall
    return self.get_type(node.func).bind_call(node, self, type_ctx)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/types.py", line 8846, in bind_call
    visitor.syntax_error("cast to unknown type", node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 74, in syntax_error
    return self.error_sink.syntax_error(msg, self.filename, node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/errors.py", line 52, in syntax_error
    self.error(TypedSyntaxError(msg, (filename, lineno, offset, source_line)))
  File "/cinder/cinderx/PythonLib/cinderx/compiler/errors.py", line 48, in error
    raise exception
  File "detyped_files/nbody/shallow/proportion_sweep/main_k03_s02.py", line 74
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.67 | 4/6 | 1 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k04_s01.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k04_s01.py
Traceback (most recent call last):
  File "/cinder/Lib/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/cinder/Lib/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/__main__.py", line 82, in <module>
    codeobj = pycodegen.compile(
  File "/cinder/cinderx/PythonLib/cinderx/compiler/pycodegen.py", line 131, in compile
    result = make_compiler(source, filename, mode, flags, optimize, compiler, modname)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/pycodegen.py", line 172, in make_compiler
    return generator.make_code_gen(
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/__init__.py", line 301, in make_code_gen
    code_gen = compiler.code_gen(
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/compiler.py", line 535, in code_gen
    tree, s = self._bind(name, filename, tree, optimize, enable_patching)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/compiler.py", line 509, in _bind
    type_binder.visit(tree)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 458, in visitModule
    self.visit(stmt)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 628, in visitFunctionDef
    self._visitFunc(node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 616, in _visitFunc
    func.bind_function(node, self)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/types.py", line 3136, in bind_function
    terminates = visitor.visit_check_terminal(self.get_function_body())
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 1787, in visit_check_terminal
    self.visit(stmt)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 803, in visitAnnAssign
    self.visitExpectedType(value, declared_type)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 1653, in visitExpectedType
    res = self.visit(node, expected)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 1484, in visitCall
    return self.get_type(node.func).bind_call(node, self, type_ctx)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/types.py", line 8846, in bind_call
    visitor.syntax_error("cast to unknown type", node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 74, in syntax_error
    return self.error_sink.syntax_error(msg, self.filename, node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/errors.py", line 52, in syntax_error
    self.error(TypedSyntaxError(msg, (filename, lineno, offset, source_line)))
  File "/cinder/cinderx/PythonLib/cinderx/compiler/errors.py", line 48, in error
    raise exception
  File "detyped_files/nbody/shallow/proportion_sweep/main_k04_s01.py", line 75
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.67 | 4/6 | 2 | 0.9119s | 0.1200s | 2 | 16 | yes | 0.8624s | 0.9755s | `detyped_files/nbody/shallow/proportion_sweep/main_k04_s02.py` |  |
| 0.83 | 5/6 | 1 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k05_s01.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k05_s01.py
Traceback (most recent call last):
  File "/cinder/Lib/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/cinder/Lib/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/__main__.py", line 82, in <module>
    codeobj = pycodegen.compile(
  File "/cinder/cinderx/PythonLib/cinderx/compiler/pycodegen.py", line 131, in compile
    result = make_compiler(source, filename, mode, flags, optimize, compiler, modname)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/pycodegen.py", line 172, in make_compiler
    return generator.make_code_gen(
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/__init__.py", line 301, in make_code_gen
    code_gen = compiler.code_gen(
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/compiler.py", line 535, in code_gen
    tree, s = self._bind(name, filename, tree, optimize, enable_patching)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/compiler.py", line 509, in _bind
    type_binder.visit(tree)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 458, in visitModule
    self.visit(stmt)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 628, in visitFunctionDef
    self._visitFunc(node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 616, in _visitFunc
    func.bind_function(node, self)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/types.py", line 3136, in bind_function
    terminates = visitor.visit_check_terminal(self.get_function_body())
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 1787, in visit_check_terminal
    self.visit(stmt)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 803, in visitAnnAssign
    self.visitExpectedType(value, declared_type)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 1653, in visitExpectedType
    res = self.visit(node, expected)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 1484, in visitCall
    return self.get_type(node.func).bind_call(node, self, type_ctx)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/types.py", line 8846, in bind_call
    visitor.syntax_error("cast to unknown type", node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 74, in syntax_error
    return self.error_sink.syntax_error(msg, self.filename, node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/errors.py", line 52, in syntax_error
    self.error(TypedSyntaxError(msg, (filename, lineno, offset, source_line)))
  File "/cinder/cinderx/PythonLib/cinderx/compiler/errors.py", line 48, in error
    raise exception
  File "detyped_files/nbody/shallow/proportion_sweep/main_k05_s01.py", line 75
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.83 | 5/6 | 2 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k05_s02.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k05_s02.py
Traceback (most recent call last):
  File "/cinder/Lib/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/cinder/Lib/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/__main__.py", line 82, in <module>
    codeobj = pycodegen.compile(
  File "/cinder/cinderx/PythonLib/cinderx/compiler/pycodegen.py", line 131, in compile
    result = make_compiler(source, filename, mode, flags, optimize, compiler, modname)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/pycodegen.py", line 172, in make_compiler
    return generator.make_code_gen(
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/__init__.py", line 301, in make_code_gen
    code_gen = compiler.code_gen(
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/compiler.py", line 535, in code_gen
    tree, s = self._bind(name, filename, tree, optimize, enable_patching)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/compiler.py", line 509, in _bind
    type_binder.visit(tree)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 458, in visitModule
    self.visit(stmt)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 628, in visitFunctionDef
    self._visitFunc(node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 616, in _visitFunc
    func.bind_function(node, self)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/types.py", line 3136, in bind_function
    terminates = visitor.visit_check_terminal(self.get_function_body())
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 1787, in visit_check_terminal
    self.visit(stmt)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 803, in visitAnnAssign
    self.visitExpectedType(value, declared_type)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 1653, in visitExpectedType
    res = self.visit(node, expected)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 1484, in visitCall
    return self.get_type(node.func).bind_call(node, self, type_ctx)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/types.py", line 8846, in bind_call
    visitor.syntax_error("cast to unknown type", node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 74, in syntax_error
    return self.error_sink.syntax_error(msg, self.filename, node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/errors.py", line 52, in syntax_error
    self.error(TypedSyntaxError(msg, (filename, lineno, offset, source_line)))
  File "/cinder/cinderx/PythonLib/cinderx/compiler/errors.py", line 48, in error
    raise exception
  File "detyped_files/nbody/shallow/proportion_sweep/main_k05_s02.py", line 75
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 1.00 | 6/6 | 1 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k06_s01.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k06_s01.py
Traceback (most recent call last):
  File "/cinder/Lib/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/cinder/Lib/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/__main__.py", line 82, in <module>
    codeobj = pycodegen.compile(
  File "/cinder/cinderx/PythonLib/cinderx/compiler/pycodegen.py", line 131, in compile
    result = make_compiler(source, filename, mode, flags, optimize, compiler, modname)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/pycodegen.py", line 172, in make_compiler
    return generator.make_code_gen(
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/__init__.py", line 301, in make_code_gen
    code_gen = compiler.code_gen(
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/compiler.py", line 535, in code_gen
    tree, s = self._bind(name, filename, tree, optimize, enable_patching)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/compiler.py", line 509, in _bind
    type_binder.visit(tree)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 458, in visitModule
    self.visit(stmt)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 628, in visitFunctionDef
    self._visitFunc(node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 616, in _visitFunc
    func.bind_function(node, self)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/types.py", line 3136, in bind_function
    terminates = visitor.visit_check_terminal(self.get_function_body())
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 1787, in visit_check_terminal
    self.visit(stmt)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 803, in visitAnnAssign
    self.visitExpectedType(value, declared_type)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 1653, in visitExpectedType
    res = self.visit(node, expected)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 1484, in visitCall
    return self.get_type(node.func).bind_call(node, self, type_ctx)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/types.py", line 8846, in bind_call
    visitor.syntax_error("cast to unknown type", node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 74, in syntax_error
    return self.error_sink.syntax_error(msg, self.filename, node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/errors.py", line 52, in syntax_error
    self.error(TypedSyntaxError(msg, (filename, lineno, offset, source_line)))
  File "/cinder/cinderx/PythonLib/cinderx/compiler/errors.py", line 48, in error
    raise exception
  File "detyped_files/nbody/shallow/proportion_sweep/main_k06_s01.py", line 77
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |

## nbody/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.9243s | 0.9243s | 0.9243s | 2.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.9243s | 0.1603s | 2 | 16 | yes | 0.8600s | 1.0089s | `static-python-perf/Benchmark/nbody/untyped/main.py` |  |

## nqueens/advanced

- Detypable targets: `5`
- Total runs: `10`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/5 | 1 | 0.2207s | 0.2207s | 0.2207s | 2.0 | yes | ok |
| 0.20 | 1/5 | 2 | 0.2220s | 0.2085s | 0.2355s | 1.0 | yes | ok |
| 0.40 | 2/5 | 2 | 0.2310s | 0.2237s | 0.2382s | 3.0 | yes | ok |
| 0.60 | 3/5 | 2 | 0.2208s | 0.2203s | 0.2213s | 1.5 | yes | ok |
| 0.80 | 4/5 | 2 | 0.2313s | 0.2230s | 0.2395s | 1.5 | yes | ok |
| 1.00 | 5/5 | 1 | 0.2335s | 0.2335s | 0.2335s | 2.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/5 | 1 | 0.2207s | 0.0377s | 2 | 16 | yes | 0.2071s | 0.2422s | `detyped_files/nqueens/advanced/proportion_sweep/main_k00_s01.py` |  |
| 0.20 | 1/5 | 1 | 0.2085s | 0.0040s | 1 | 8 | yes | 0.2061s | 0.2111s | `detyped_files/nqueens/advanced/proportion_sweep/main_k01_s01.py` |  |
| 0.20 | 1/5 | 2 | 0.2355s | 0.0318s | 1 | 8 | yes | 0.2223s | 0.2588s | `detyped_files/nqueens/advanced/proportion_sweep/main_k01_s02.py` |  |
| 0.40 | 2/5 | 1 | 0.2237s | 0.0340s | 2 | 16 | yes | 0.2113s | 0.2427s | `detyped_files/nqueens/advanced/proportion_sweep/main_k02_s01.py` |  |
| 0.40 | 2/5 | 2 | 0.2382s | 0.0487s | 4 | 32 | yes | 0.2262s | 0.2584s | `detyped_files/nqueens/advanced/proportion_sweep/main_k02_s02.py` |  |
| 0.60 | 3/5 | 1 | 0.2213s | 0.0375s | 2 | 16 | yes | 0.2078s | 0.2427s | `detyped_files/nqueens/advanced/proportion_sweep/main_k03_s01.py` |  |
| 0.60 | 3/5 | 2 | 0.2203s | 0.0232s | 1 | 8 | yes | 0.2109s | 0.2369s | `detyped_files/nqueens/advanced/proportion_sweep/main_k03_s02.py` |  |
| 0.80 | 4/5 | 1 | 0.2395s | 0.0346s | 2 | 16 | yes | 0.2268s | 0.2583s | `detyped_files/nqueens/advanced/proportion_sweep/main_k04_s01.py` |  |
| 0.80 | 4/5 | 2 | 0.2230s | 0.0012s | 1 | 8 | yes | 0.2224s | 0.2238s | `detyped_files/nqueens/advanced/proportion_sweep/main_k04_s02.py` |  |
| 1.00 | 5/5 | 1 | 0.2335s | 0.0268s | 2 | 16 | yes | 0.2256s | 0.2477s | `detyped_files/nqueens/advanced/proportion_sweep/main_k05_s01.py` |  |

## nqueens/shallow

- Detypable targets: `3`
- Total runs: `6`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/3 | 1 | 0.2058s | 0.2058s | 0.2058s | 1.0 | yes | ok |
| 0.33 | 1/3 | 2 | 0.2070s | 0.2062s | 0.2079s | 1.0 | yes | ok |
| 0.67 | 2/3 | 2 | 0.2091s | 0.2036s | 0.2145s | 1.5 | yes | ok |
| 1.00 | 3/3 | 1 | - | - | - | - | - | 1 failed |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/3 | 1 | 0.2058s | 0.0105s | 1 | 8 | yes | 0.2012s | 0.2135s | `detyped_files/nqueens/shallow/proportion_sweep/main_k00_s01.py` |  |
| 0.33 | 1/3 | 1 | 0.2062s | 0.0085s | 1 | 8 | yes | 0.2020s | 0.2124s | `detyped_files/nqueens/shallow/proportion_sweep/main_k01_s01.py` |  |
| 0.33 | 1/3 | 2 | 0.2079s | 0.0097s | 1 | 8 | yes | 0.2033s | 0.2149s | `detyped_files/nqueens/shallow/proportion_sweep/main_k01_s02.py` |  |
| 0.67 | 2/3 | 1 | 0.2036s | 0.0033s | 1 | 8 | yes | 0.2016s | 0.2058s | `detyped_files/nqueens/shallow/proportion_sweep/main_k02_s01.py` |  |
| 0.67 | 2/3 | 2 | 0.2145s | 0.0373s | 2 | 16 | yes | 0.2044s | 0.2335s | `detyped_files/nqueens/shallow/proportion_sweep/main_k02_s02.py` |  |
| 1.00 | 3/3 | 1 | - | - | - | - | - | - | - | `detyped_files/nqueens/shallow/proportion_sweep/main_k03_s01.py` | benchmark script failed (1): detyped_files/nqueens/shallow/proportion_sweep/main_k03_s01.py
docker error: container create: Cannot connect to the Docker daemon at unix:///Users/robertmorelli/.docker/run/docker.sock. Is the docker daemon running? |

## nqueens/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.2099s | 0.2099s | 0.2099s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.2099s | 0.0062s | 1 | 8 | yes | 0.2065s | 0.2144s | `static-python-perf/Benchmark/nqueens/untyped/main.py` |  |

## pystone/advanced

- Detypable targets: `15`
- Total runs: `30`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/15 | 1 | 0.4793s | 0.4793s | 0.4793s | 1.0 | yes | ok |
| 0.07 | 1/15 | 2 | 0.4672s | 0.4594s | 0.4750s | 1.0 | yes | ok |
| 0.13 | 2/15 | 2 | 0.5983s | 0.4641s | 0.7324s | 1.5 | yes | ok |
| 0.20 | 3/15 | 2 | 0.8105s | 0.5181s | 1.1029s | 2.5 | yes | ok |
| 0.27 | 4/15 | 2 | 0.9655s | 0.6120s | 1.3190s | 2.0 | yes | ok |
| 0.33 | 5/15 | 2 | 0.4699s | 0.4622s | 0.4776s | 1.0 | yes | ok |
| 0.40 | 6/15 | 2 | 1.0560s | 0.7250s | 1.3870s | 1.0 | yes | ok |
| 0.47 | 7/15 | 2 | 1.0307s | 0.8460s | 1.2154s | 1.5 | yes | ok |
| 0.53 | 8/15 | 2 | 0.7477s | 0.6058s | 0.8895s | 2.5 | yes | ok |
| 0.60 | 9/15 | 2 | 1.0899s | 0.7088s | 1.4711s | 1.0 | yes | ok |
| 0.67 | 10/15 | 2 | 1.3111s | 1.2788s | 1.3435s | 2.0 | yes | ok |
| 0.73 | 11/15 | 2 | 1.1164s | 0.8444s | 1.3884s | 1.5 | yes | ok |
| 0.80 | 12/15 | 2 | 0.9835s | 0.8609s | 1.1060s | 1.0 | yes | ok |
| 0.87 | 13/15 | 2 | 1.2934s | 1.2055s | 1.3813s | 1.5 | yes | ok |
| 0.93 | 14/15 | 2 | 1.1097s | 1.1047s | 1.1147s | 1.0 | yes | ok |
| 1.00 | 15/15 | 1 | 1.1032s | 1.1032s | 1.1032s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/15 | 1 | 0.4793s | 0.0419s | 1 | 8 | yes | 0.4592s | 0.5105s | `detyped_files/pystone/advanced/proportion_sweep/main_k00_s01.py` |  |
| 0.07 | 1/15 | 1 | 0.4750s | 0.0211s | 1 | 8 | yes | 0.4639s | 0.4902s | `detyped_files/pystone/advanced/proportion_sweep/main_k01_s01.py` |  |
| 0.07 | 1/15 | 2 | 0.4594s | 0.0054s | 1 | 8 | yes | 0.4567s | 0.4633s | `detyped_files/pystone/advanced/proportion_sweep/main_k01_s02.py` |  |
| 0.13 | 2/15 | 1 | 0.4641s | 0.0144s | 1 | 8 | yes | 0.4568s | 0.4744s | `detyped_files/pystone/advanced/proportion_sweep/main_k02_s01.py` |  |
| 0.13 | 2/15 | 2 | 0.7324s | 0.1156s | 2 | 16 | yes | 0.6898s | 0.7963s | `detyped_files/pystone/advanced/proportion_sweep/main_k02_s02.py` |  |
| 0.20 | 3/15 | 1 | 1.1029s | 0.1781s | 2 | 16 | yes | 1.0319s | 1.1968s | `detyped_files/pystone/advanced/proportion_sweep/main_k03_s01.py` |  |
| 0.20 | 3/15 | 2 | 0.5181s | 0.1208s | 3 | 24 | yes | 0.4741s | 0.5691s | `detyped_files/pystone/advanced/proportion_sweep/main_k03_s02.py` |  |
| 0.27 | 4/15 | 1 | 0.6120s | 0.0989s | 3 | 24 | yes | 0.5785s | 0.6544s | `detyped_files/pystone/advanced/proportion_sweep/main_k04_s01.py` |  |
| 0.27 | 4/15 | 2 | 1.3190s | 0.1137s | 1 | 8 | yes | 1.2536s | 1.3976s | `detyped_files/pystone/advanced/proportion_sweep/main_k04_s02.py` |  |
| 0.33 | 5/15 | 1 | 0.4622s | 0.0057s | 1 | 8 | yes | 0.4588s | 0.4662s | `detyped_files/pystone/advanced/proportion_sweep/main_k05_s01.py` |  |
| 0.33 | 5/15 | 2 | 0.4776s | 0.0311s | 1 | 8 | yes | 0.4617s | 0.5001s | `detyped_files/pystone/advanced/proportion_sweep/main_k05_s02.py` |  |
| 0.40 | 6/15 | 1 | 0.7250s | 0.0659s | 1 | 8 | yes | 0.6899s | 0.7715s | `detyped_files/pystone/advanced/proportion_sweep/main_k06_s01.py` |  |
| 0.40 | 6/15 | 2 | 1.3870s | 0.1594s | 1 | 8 | yes | 1.2843s | 1.4957s | `detyped_files/pystone/advanced/proportion_sweep/main_k06_s02.py` |  |
| 0.47 | 7/15 | 1 | 0.8460s | 0.1438s | 2 | 16 | yes | 0.7923s | 0.9254s | `detyped_files/pystone/advanced/proportion_sweep/main_k07_s01.py` |  |
| 0.47 | 7/15 | 2 | 1.2154s | 0.1312s | 1 | 8 | yes | 1.1327s | 1.2998s | `detyped_files/pystone/advanced/proportion_sweep/main_k07_s02.py` |  |
| 0.53 | 8/15 | 1 | 0.6058s | 0.0793s | 2 | 16 | yes | 0.5706s | 0.6474s | `detyped_files/pystone/advanced/proportion_sweep/main_k08_s01.py` |  |
| 0.53 | 8/15 | 2 | 0.8895s | 0.1852s | 3 | 24 | yes | 0.8279s | 0.9706s | `detyped_files/pystone/advanced/proportion_sweep/main_k08_s02.py` |  |
| 0.60 | 9/15 | 1 | 0.7088s | 0.0359s | 1 | 8 | yes | 0.6904s | 0.7354s | `detyped_files/pystone/advanced/proportion_sweep/main_k09_s01.py` |  |
| 0.60 | 9/15 | 2 | 1.4711s | 0.1565s | 1 | 8 | yes | 1.3781s | 1.5808s | `detyped_files/pystone/advanced/proportion_sweep/main_k09_s02.py` |  |
| 0.67 | 10/15 | 1 | 1.2788s | 0.2721s | 3 | 24 | yes | 1.1799s | 1.3944s | `detyped_files/pystone/advanced/proportion_sweep/main_k10_s01.py` |  |
| 0.67 | 10/15 | 2 | 1.3435s | 0.1277s | 1 | 8 | yes | 1.2677s | 1.4318s | `detyped_files/pystone/advanced/proportion_sweep/main_k10_s02.py` |  |
| 0.73 | 11/15 | 1 | 1.3884s | 0.1939s | 2 | 16 | yes | 1.3030s | 1.4882s | `detyped_files/pystone/advanced/proportion_sweep/main_k11_s01.py` |  |
| 0.73 | 11/15 | 2 | 0.8444s | 0.0840s | 1 | 8 | yes | 0.8009s | 0.9027s | `detyped_files/pystone/advanced/proportion_sweep/main_k11_s02.py` |  |
| 0.80 | 12/15 | 1 | 1.1060s | 0.0074s | 1 | 8 | yes | 1.1015s | 1.1110s | `detyped_files/pystone/advanced/proportion_sweep/main_k12_s01.py` |  |
| 0.80 | 12/15 | 2 | 0.8609s | 0.0806s | 1 | 8 | yes | 0.8193s | 0.9181s | `detyped_files/pystone/advanced/proportion_sweep/main_k12_s02.py` |  |
| 0.87 | 13/15 | 1 | 1.3813s | 0.1638s | 1 | 8 | yes | 1.2853s | 1.4954s | `detyped_files/pystone/advanced/proportion_sweep/main_k13_s01.py` |  |
| 0.87 | 13/15 | 2 | 1.2055s | 0.1966s | 2 | 16 | yes | 1.1189s | 1.3047s | `detyped_files/pystone/advanced/proportion_sweep/main_k13_s02.py` |  |
| 0.93 | 14/15 | 1 | 1.1047s | 0.0545s | 1 | 8 | yes | 1.0747s | 1.1424s | `detyped_files/pystone/advanced/proportion_sweep/main_k14_s01.py` |  |
| 0.93 | 14/15 | 2 | 1.1147s | 0.0439s | 1 | 8 | yes | 1.0876s | 1.1451s | `detyped_files/pystone/advanced/proportion_sweep/main_k14_s02.py` |  |
| 1.00 | 15/15 | 1 | 1.1032s | 0.0614s | 1 | 8 | yes | 1.0766s | 1.1476s | `detyped_files/pystone/advanced/proportion_sweep/main_k15_s01.py` |  |

## pystone/shallow

- Detypable targets: `15`
- Total runs: `30`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/15 | 1 | 0.3951s | 0.3951s | 0.3951s | 3.0 | yes | ok |
| 0.07 | 1/15 | 2 | 0.4160s | 0.3625s | 0.4694s | 1.5 | yes | ok |
| 0.13 | 2/15 | 2 | 0.4280s | 0.3860s | 0.4699s | 2.0 | yes | ok |
| 0.20 | 3/15 | 2 | 0.6138s | 0.5811s | 0.6465s | 2.0 | yes | ok |
| 0.27 | 4/15 | 2 | 0.3882s | 0.3882s | 0.3882s | 4.0 | yes | 1 failed |
| 0.33 | 5/15 | 2 | 0.6163s | 0.3669s | 0.8656s | 1.5 | yes | ok |
| 0.40 | 6/15 | 2 | 0.6288s | 0.5983s | 0.6594s | 2.0 | yes | ok |
| 0.47 | 7/15 | 2 | 0.5063s | 0.3626s | 0.6501s | 1.0 | yes | ok |
| 0.53 | 8/15 | 2 | 0.7705s | 0.6073s | 0.9337s | 1.0 | yes | ok |
| 0.60 | 9/15 | 2 | 0.5829s | 0.5513s | 0.6145s | 1.0 | yes | ok |
| 0.67 | 10/15 | 2 | 0.7672s | 0.5829s | 0.9516s | 2.0 | yes | ok |
| 0.73 | 11/15 | 2 | 0.7714s | 0.6958s | 0.8470s | 1.0 | yes | ok |
| 0.80 | 12/15 | 2 | 0.8347s | 0.7074s | 0.9621s | 1.5 | yes | ok |
| 0.87 | 13/15 | 2 | 0.9194s | 0.9128s | 0.9261s | 1.0 | yes | ok |
| 0.93 | 14/15 | 2 | 0.9343s | 0.9335s | 0.9350s | 1.0 | yes | ok |
| 1.00 | 15/15 | 1 | 0.9390s | 0.9390s | 0.9390s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/15 | 1 | 0.3951s | 0.0847s | 3 | 24 | yes | 0.3674s | 0.4337s | `detyped_files/pystone/shallow/proportion_sweep/main_k00_s01.py` |  |
| 0.07 | 1/15 | 1 | 0.3625s | 0.0063s | 1 | 8 | yes | 0.3586s | 0.3668s | `detyped_files/pystone/shallow/proportion_sweep/main_k01_s01.py` |  |
| 0.07 | 1/15 | 2 | 0.4694s | 0.0555s | 2 | 16 | yes | 0.4521s | 0.4987s | `detyped_files/pystone/shallow/proportion_sweep/main_k01_s02.py` |  |
| 0.13 | 2/15 | 1 | 0.4699s | 0.0741s | 2 | 16 | yes | 0.4478s | 0.5087s | `detyped_files/pystone/shallow/proportion_sweep/main_k02_s01.py` |  |
| 0.13 | 2/15 | 2 | 0.3860s | 0.0569s | 2 | 16 | yes | 0.3666s | 0.4161s | `detyped_files/pystone/shallow/proportion_sweep/main_k02_s02.py` |  |
| 0.20 | 3/15 | 1 | 0.6465s | 0.0709s | 1 | 8 | yes | 0.6154s | 0.6988s | `detyped_files/pystone/shallow/proportion_sweep/main_k03_s01.py` |  |
| 0.20 | 3/15 | 2 | 0.5811s | 0.1030s | 3 | 24 | yes | 0.5505s | 0.6269s | `detyped_files/pystone/shallow/proportion_sweep/main_k03_s02.py` |  |
| 0.27 | 4/15 | 1 | - | - | - | - | - | - | - | `detyped_files/pystone/shallow/proportion_sweep/main_k04_s01.py` | benchmark script failed (1): detyped_files/pystone/shallow/proportion_sweep/main_k04_s01.py
docker error: exec attach: cannot connect to the Docker daemon. Is 'docker daemon' running on this host?: dial unix /Users/robertmorelli/.docker/run/docker.sock: connect: connection refused |
| 0.27 | 4/15 | 2 | 0.3882s | 0.0928s | 4 | 32 | yes | 0.3640s | 0.4246s | `detyped_files/pystone/shallow/proportion_sweep/main_k04_s02.py` |  |
| 0.33 | 5/15 | 1 | 0.8656s | 0.1311s | 2 | 16 | yes | 0.8096s | 0.9312s | `detyped_files/pystone/shallow/proportion_sweep/main_k05_s01.py` |  |
| 0.33 | 5/15 | 2 | 0.3669s | 0.0130s | 1 | 8 | yes | 0.3601s | 0.3764s | `detyped_files/pystone/shallow/proportion_sweep/main_k05_s02.py` |  |
| 0.40 | 6/15 | 1 | 0.5983s | 0.1076s | 3 | 24 | yes | 0.5614s | 0.6451s | `detyped_files/pystone/shallow/proportion_sweep/main_k06_s01.py` |  |
| 0.40 | 6/15 | 2 | 0.6594s | 0.0675s | 1 | 8 | yes | 0.6186s | 0.7067s | `detyped_files/pystone/shallow/proportion_sweep/main_k06_s02.py` |  |
| 0.47 | 7/15 | 1 | 0.3626s | 0.0058s | 1 | 8 | yes | 0.3592s | 0.3667s | `detyped_files/pystone/shallow/proportion_sweep/main_k07_s01.py` |  |
| 0.47 | 7/15 | 2 | 0.6501s | 0.0259s | 1 | 8 | yes | 0.6356s | 0.6680s | `detyped_files/pystone/shallow/proportion_sweep/main_k07_s02.py` |  |
| 0.53 | 8/15 | 1 | 0.6073s | 0.0044s | 1 | 8 | yes | 0.6046s | 0.6103s | `detyped_files/pystone/shallow/proportion_sweep/main_k08_s01.py` |  |
| 0.53 | 8/15 | 2 | 0.9337s | 0.1017s | 1 | 8 | yes | 0.8875s | 1.0071s | `detyped_files/pystone/shallow/proportion_sweep/main_k08_s02.py` |  |
| 0.60 | 9/15 | 1 | 0.6145s | 0.0114s | 1 | 8 | yes | 0.6081s | 0.6225s | `detyped_files/pystone/shallow/proportion_sweep/main_k09_s01.py` |  |
| 0.60 | 9/15 | 2 | 0.5513s | 0.0111s | 1 | 8 | yes | 0.5445s | 0.5587s | `detyped_files/pystone/shallow/proportion_sweep/main_k09_s02.py` |  |
| 0.67 | 10/15 | 1 | 0.9516s | 0.1229s | 2 | 16 | yes | 0.8986s | 1.0170s | `detyped_files/pystone/shallow/proportion_sweep/main_k10_s01.py` |  |
| 0.67 | 10/15 | 2 | 0.5829s | 0.0926s | 2 | 16 | yes | 0.5473s | 0.6336s | `detyped_files/pystone/shallow/proportion_sweep/main_k10_s02.py` |  |
| 0.73 | 11/15 | 1 | 0.6958s | 0.0062s | 1 | 8 | yes | 0.6921s | 0.7000s | `detyped_files/pystone/shallow/proportion_sweep/main_k11_s01.py` |  |
| 0.73 | 11/15 | 2 | 0.8470s | 0.0939s | 1 | 8 | yes | 0.7947s | 0.9212s | `detyped_files/pystone/shallow/proportion_sweep/main_k11_s02.py` |  |
| 0.80 | 12/15 | 1 | 0.9621s | 0.1331s | 1 | 8 | yes | 0.8943s | 1.0559s | `detyped_files/pystone/shallow/proportion_sweep/main_k12_s01.py` |  |
| 0.80 | 12/15 | 2 | 0.7074s | 0.1209s | 2 | 16 | yes | 0.6559s | 0.7685s | `detyped_files/pystone/shallow/proportion_sweep/main_k12_s02.py` |  |
| 0.87 | 13/15 | 1 | 0.9261s | 0.0786s | 1 | 8 | yes | 0.8847s | 0.9799s | `detyped_files/pystone/shallow/proportion_sweep/main_k13_s01.py` |  |
| 0.87 | 13/15 | 2 | 0.9128s | 0.0506s | 1 | 8 | yes | 0.8902s | 0.9494s | `detyped_files/pystone/shallow/proportion_sweep/main_k13_s02.py` |  |
| 0.93 | 14/15 | 1 | 0.9335s | 0.1162s | 1 | 8 | yes | 0.8880s | 1.0166s | `detyped_files/pystone/shallow/proportion_sweep/main_k14_s01.py` |  |
| 0.93 | 14/15 | 2 | 0.9350s | 0.0930s | 1 | 8 | yes | 0.8950s | 1.0032s | `detyped_files/pystone/shallow/proportion_sweep/main_k14_s02.py` |  |
| 1.00 | 15/15 | 1 | 0.9390s | 0.0904s | 1 | 8 | yes | 0.8874s | 1.0023s | `detyped_files/pystone/shallow/proportion_sweep/main_k15_s01.py` |  |

## pystone/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | - | - | - | - | - | 1 failed |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | - | - | - | - | - | - | - | `static-python-perf/Benchmark/pystone/untyped/main.py` | benchmark script failed (1): static-python-perf/Benchmark/pystone/untyped/main.py
Traceback (most recent call last):
  File "/cinder/Lib/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/cinder/Lib/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/__main__.py", line 82, in <module>
    codeobj = pycodegen.compile(
  File "/cinder/cinderx/PythonLib/cinderx/compiler/pycodegen.py", line 131, in compile
    result = make_compiler(source, filename, mode, flags, optimize, compiler, modname)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/pycodegen.py", line 172, in make_compiler
    return generator.make_code_gen(
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/__init__.py", line 301, in make_code_gen
    code_gen = compiler.code_gen(
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/compiler.py", line 535, in code_gen
    tree, s = self._bind(name, filename, tree, optimize, enable_patching)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/compiler.py", line 509, in _bind
    type_binder.visit(tree)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 458, in visitModule
    self.visit(stmt)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 628, in visitFunctionDef
    self._visitFunc(node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 616, in _visitFunc
    func.bind_function(node, self)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/types.py", line 3136, in bind_function
    terminates = visitor.visit_check_terminal(self.get_function_body())
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 1787, in visit_check_terminal
    self.visit(stmt)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 394, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 71, in visit
    return super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 871, in visitAssign
    self.assign_value(target, value_type, src=node.value, assignment=node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 1285, in assign_value
    self.assign_name(target, target.id, value)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 1272, in assign_name
    self.check_can_assign_from(decl_type.type.klass, value.klass, target)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/type_binder.py", line 909, in check_can_assign_from
    self.syntax_error(reason, node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/visitor.py", line 74, in syntax_error
    return self.error_sink.syntax_error(msg, self.filename, node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/errors.py", line 52, in syntax_error
    self.error(TypedSyntaxError(msg, (filename, lineno, offset, source_line)))
  File "/cinder/cinderx/PythonLib/cinderx/compiler/errors.py", line 48, in error
    raise exception
  File "static-python-perf/Benchmark/pystone/untyped/main.py", line 98
    PtrGlbNext = Record()
cinderx.compiler.errors.TypedSyntaxError: type mismatch: __main__.Record cannot be assigned to None |

## richards/advanced

- Detypable targets: `23`
- Total runs: `46`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/23 | 1 | 0.8295s | 0.8295s | 0.8295s | 1.0 | yes | ok |
| 0.04 | 1/23 | 2 | 1.8192s | 0.8323s | 2.8060s | 1.5 | yes | ok |
| 0.09 | 2/23 | 2 | 0.9093s | 0.8261s | 0.9924s | 1.0 | yes | ok |
| 0.13 | 3/23 | 2 | 2.2222s | 1.0907s | 3.3538s | 1.0 | yes | ok |
| 0.17 | 4/23 | 2 | 0.9978s | 0.9288s | 1.0667s | 2.0 | yes | ok |
| 0.22 | 5/23 | 2 | 3.2763s | 3.0421s | 3.5105s | 1.0 | yes | ok |
| 0.26 | 6/23 | 2 | 1.0581s | 0.8579s | 1.2584s | 1.5 | yes | ok |
| 0.30 | 7/23 | 2 | 1.4679s | 1.2987s | 1.6371s | 1.5 | yes | ok |
| 0.35 | 8/23 | 2 | 1.9981s | 1.0740s | 2.9223s | 1.0 | yes | ok |
| 0.39 | 9/23 | 2 | 3.2850s | 3.2353s | 3.3347s | 1.0 | yes | ok |
| 0.43 | 10/23 | 2 | 1.2825s | 1.2264s | 1.3386s | 1.0 | yes | ok |
| 0.48 | 11/23 | 2 | 2.6662s | 2.1540s | 3.1784s | 1.0 | yes | ok |
| 0.52 | 12/23 | 2 | 2.6226s | 1.8961s | 3.3491s | 1.0 | yes | ok |
| 0.57 | 13/23 | 2 | 3.1355s | 2.3775s | 3.8935s | 1.0 | yes | ok |
| 0.61 | 14/23 | 2 | 4.1105s | 3.6977s | 4.5234s | 1.0 | yes | ok |
| 0.65 | 15/23 | 2 | 3.9306s | 2.9635s | 4.8976s | 1.0 | yes | ok |
| 0.70 | 16/23 | 2 | 3.6871s | 2.8663s | 4.5080s | 1.0 | yes | ok |
| 0.74 | 17/23 | 2 | 5.0639s | 4.7357s | 5.3921s | 1.0 | yes | ok |
| 0.78 | 18/23 | 2 | 4.9295s | 4.6994s | 5.1596s | 1.0 | yes | ok |
| 0.83 | 19/23 | 2 | 5.5674s | 5.4759s | 5.6590s | 1.0 | yes | ok |
| 0.87 | 20/23 | 2 | 5.2731s | 4.9168s | 5.6295s | 1.0 | yes | ok |
| 0.91 | 21/23 | 2 | 5.2196s | 4.9272s | 5.5121s | 1.0 | yes | ok |
| 0.96 | 22/23 | 2 | 5.3466s | 4.9867s | 5.7065s | 1.0 | yes | ok |
| 1.00 | 23/23 | 1 | 5.6417s | 5.6417s | 5.6417s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/23 | 1 | 0.8295s | 0.0589s | 1 | 8 | yes | 0.7982s | 0.8715s | `detyped_files/richards/advanced/proportion_sweep/main_k00_s01.py` |  |
| 0.04 | 1/23 | 1 | 2.8060s | 0.2714s | 1 | 8 | yes | 2.6568s | 2.9986s | `detyped_files/richards/advanced/proportion_sweep/main_k01_s01.py` |  |
| 0.04 | 1/23 | 2 | 0.8323s | 0.0962s | 2 | 16 | yes | 0.7995s | 0.8844s | `detyped_files/richards/advanced/proportion_sweep/main_k01_s02.py` |  |
| 0.09 | 2/23 | 1 | 0.9924s | 0.1241s | 1 | 8 | yes | 0.9239s | 1.0859s | `detyped_files/richards/advanced/proportion_sweep/main_k02_s01.py` |  |
| 0.09 | 2/23 | 2 | 0.8261s | 0.0793s | 1 | 8 | yes | 0.7958s | 0.8830s | `detyped_files/richards/advanced/proportion_sweep/main_k02_s02.py` |  |
| 0.13 | 3/23 | 1 | 1.0907s | 0.1038s | 1 | 8 | yes | 1.0317s | 1.1697s | `detyped_files/richards/advanced/proportion_sweep/main_k03_s01.py` |  |
| 0.13 | 3/23 | 2 | 3.3538s | 0.3428s | 1 | 8 | yes | 3.1852s | 3.6085s | `detyped_files/richards/advanced/proportion_sweep/main_k03_s02.py` |  |
| 0.17 | 4/23 | 1 | 1.0667s | 0.1695s | 2 | 16 | yes | 1.0012s | 1.1578s | `detyped_files/richards/advanced/proportion_sweep/main_k04_s01.py` |  |
| 0.17 | 4/23 | 2 | 0.9288s | 0.1307s | 2 | 16 | yes | 0.8695s | 0.9952s | `detyped_files/richards/advanced/proportion_sweep/main_k04_s02.py` |  |
| 0.22 | 5/23 | 1 | 3.0421s | 0.3104s | 1 | 8 | yes | 2.8816s | 3.2675s | `detyped_files/richards/advanced/proportion_sweep/main_k05_s01.py` |  |
| 0.22 | 5/23 | 2 | 3.5105s | 0.1634s | 1 | 8 | yes | 3.4148s | 3.6254s | `detyped_files/richards/advanced/proportion_sweep/main_k05_s02.py` |  |
| 0.26 | 6/23 | 1 | 1.2584s | 0.0385s | 1 | 8 | yes | 1.2363s | 1.2859s | `detyped_files/richards/advanced/proportion_sweep/main_k06_s01.py` |  |
| 0.26 | 6/23 | 2 | 0.8579s | 0.1287s | 2 | 16 | yes | 0.8017s | 0.9238s | `detyped_files/richards/advanced/proportion_sweep/main_k06_s02.py` |  |
| 0.30 | 7/23 | 1 | 1.6371s | 0.1573s | 1 | 8 | yes | 1.5433s | 1.7434s | `detyped_files/richards/advanced/proportion_sweep/main_k07_s01.py` |  |
| 0.30 | 7/23 | 2 | 1.2987s | 0.1803s | 2 | 16 | yes | 1.2223s | 1.3885s | `detyped_files/richards/advanced/proportion_sweep/main_k07_s02.py` |  |
| 0.35 | 8/23 | 1 | 2.9223s | 0.2092s | 1 | 8 | yes | 2.8032s | 3.0694s | `detyped_files/richards/advanced/proportion_sweep/main_k08_s01.py` |  |
| 0.35 | 8/23 | 2 | 1.0740s | 0.1138s | 1 | 8 | yes | 1.0182s | 1.1543s | `detyped_files/richards/advanced/proportion_sweep/main_k08_s02.py` |  |
| 0.39 | 9/23 | 1 | 3.2353s | 0.1298s | 1 | 8 | yes | 3.1607s | 3.3277s | `detyped_files/richards/advanced/proportion_sweep/main_k09_s01.py` |  |
| 0.39 | 9/23 | 2 | 3.3347s | 0.2370s | 1 | 8 | yes | 3.2054s | 3.5063s | `detyped_files/richards/advanced/proportion_sweep/main_k09_s02.py` |  |
| 0.43 | 10/23 | 1 | 1.2264s | 0.0553s | 1 | 8 | yes | 1.2008s | 1.2666s | `detyped_files/richards/advanced/proportion_sweep/main_k10_s01.py` |  |
| 0.43 | 10/23 | 2 | 1.3386s | 0.0165s | 1 | 8 | yes | 1.3288s | 1.3500s | `detyped_files/richards/advanced/proportion_sweep/main_k10_s02.py` |  |
| 0.48 | 11/23 | 1 | 2.1540s | 0.1782s | 1 | 8 | yes | 2.0573s | 2.2819s | `detyped_files/richards/advanced/proportion_sweep/main_k11_s01.py` |  |
| 0.48 | 11/23 | 2 | 3.1784s | 0.2243s | 1 | 8 | yes | 3.0472s | 3.3350s | `detyped_files/richards/advanced/proportion_sweep/main_k11_s02.py` |  |
| 0.52 | 12/23 | 1 | 1.8961s | 0.1279s | 1 | 8 | yes | 1.8219s | 1.9838s | `detyped_files/richards/advanced/proportion_sweep/main_k12_s01.py` |  |
| 0.52 | 12/23 | 2 | 3.3491s | 0.1710s | 1 | 8 | yes | 3.2533s | 3.4716s | `detyped_files/richards/advanced/proportion_sweep/main_k12_s02.py` |  |
| 0.57 | 13/23 | 1 | 2.3775s | 0.1760s | 1 | 8 | yes | 2.2809s | 2.5025s | `detyped_files/richards/advanced/proportion_sweep/main_k13_s01.py` |  |
| 0.57 | 13/23 | 2 | 3.8935s | 0.1123s | 1 | 8 | yes | 3.8297s | 3.9732s | `detyped_files/richards/advanced/proportion_sweep/main_k13_s02.py` |  |
| 0.61 | 14/23 | 1 | 3.6977s | 0.4238s | 1 | 8 | yes | 3.4497s | 4.0066s | `detyped_files/richards/advanced/proportion_sweep/main_k14_s01.py` |  |
| 0.61 | 14/23 | 2 | 4.5234s | 0.1725s | 1 | 8 | yes | 4.4095s | 4.6321s | `detyped_files/richards/advanced/proportion_sweep/main_k14_s02.py` |  |
| 0.65 | 15/23 | 1 | 4.8976s | 0.1144s | 1 | 8 | yes | 4.8358s | 4.9792s | `detyped_files/richards/advanced/proportion_sweep/main_k15_s01.py` |  |
| 0.65 | 15/23 | 2 | 2.9635s | 0.1440s | 1 | 8 | yes | 2.8657s | 3.0578s | `detyped_files/richards/advanced/proportion_sweep/main_k15_s02.py` |  |
| 0.70 | 16/23 | 1 | 2.8663s | 0.1204s | 1 | 8 | yes | 2.7919s | 2.9498s | `detyped_files/richards/advanced/proportion_sweep/main_k16_s01.py` |  |
| 0.70 | 16/23 | 2 | 4.5080s | 0.2084s | 1 | 8 | yes | 4.3864s | 4.6537s | `detyped_files/richards/advanced/proportion_sweep/main_k16_s02.py` |  |
| 0.74 | 17/23 | 1 | 4.7357s | 0.2297s | 1 | 8 | yes | 4.5865s | 4.8848s | `detyped_files/richards/advanced/proportion_sweep/main_k17_s01.py` |  |
| 0.74 | 17/23 | 2 | 5.3921s | 0.2690s | 1 | 8 | yes | 5.2534s | 5.5872s | `detyped_files/richards/advanced/proportion_sweep/main_k17_s02.py` |  |
| 0.78 | 18/23 | 1 | 5.1596s | 0.1181s | 1 | 8 | yes | 5.0837s | 5.2353s | `detyped_files/richards/advanced/proportion_sweep/main_k18_s01.py` |  |
| 0.78 | 18/23 | 2 | 4.6994s | 0.0959s | 1 | 8 | yes | 4.6406s | 4.7649s | `detyped_files/richards/advanced/proportion_sweep/main_k18_s02.py` |  |
| 0.83 | 19/23 | 1 | 5.4759s | 0.1467s | 1 | 8 | yes | 5.3808s | 5.5722s | `detyped_files/richards/advanced/proportion_sweep/main_k19_s01.py` |  |
| 0.83 | 19/23 | 2 | 5.6590s | 0.1415s | 1 | 8 | yes | 5.5696s | 5.7509s | `detyped_files/richards/advanced/proportion_sweep/main_k19_s02.py` |  |
| 0.87 | 20/23 | 1 | 5.6295s | 0.1510s | 1 | 8 | yes | 5.5344s | 5.7310s | `detyped_files/richards/advanced/proportion_sweep/main_k20_s01.py` |  |
| 0.87 | 20/23 | 2 | 4.9168s | 0.1022s | 1 | 8 | yes | 4.8531s | 4.9856s | `detyped_files/richards/advanced/proportion_sweep/main_k20_s02.py` |  |
| 0.91 | 21/23 | 1 | 5.5121s | 0.1138s | 1 | 8 | yes | 5.4348s | 5.5823s | `detyped_files/richards/advanced/proportion_sweep/main_k21_s01.py` |  |
| 0.91 | 21/23 | 2 | 4.9272s | 0.0834s | 1 | 8 | yes | 4.8717s | 4.9798s | `detyped_files/richards/advanced/proportion_sweep/main_k21_s02.py` |  |
| 0.96 | 22/23 | 1 | 4.9867s | 0.1493s | 1 | 8 | yes | 4.8907s | 5.0811s | `detyped_files/richards/advanced/proportion_sweep/main_k22_s01.py` |  |
| 0.96 | 22/23 | 2 | 5.7065s | 0.1896s | 1 | 8 | yes | 5.5856s | 5.8314s | `detyped_files/richards/advanced/proportion_sweep/main_k22_s02.py` |  |
| 1.00 | 23/23 | 1 | 5.6417s | 0.1171s | 1 | 8 | yes | 5.5608s | 5.7133s | `detyped_files/richards/advanced/proportion_sweep/main_k23_s01.py` |  |

## richards/shallow

- Detypable targets: `23`
- Total runs: `46`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/23 | 1 | 0.8995s | 0.8995s | 0.8995s | 1.0 | yes | ok |
| 0.04 | 1/23 | 2 | 1.2788s | 1.1636s | 1.3939s | 1.0 | yes | ok |
| 0.09 | 2/23 | 2 | 0.9280s | 0.9203s | 0.9358s | 1.0 | yes | ok |
| 0.13 | 3/23 | 2 | 1.4155s | 1.3332s | 1.4979s | 1.5 | yes | ok |
| 0.17 | 4/23 | 2 | 1.9669s | 1.1655s | 2.7683s | 1.0 | yes | ok |
| 0.22 | 5/23 | 2 | 1.3940s | 1.1184s | 1.6695s | 1.5 | yes | ok |
| 0.26 | 6/23 | 2 | 1.3910s | 1.3247s | 1.4573s | 1.0 | yes | ok |
| 0.30 | 7/23 | 2 | 1.5747s | 1.2392s | 1.9103s | 1.0 | yes | ok |
| 0.35 | 8/23 | 2 | 2.2607s | 1.4012s | 3.1202s | 1.0 | yes | ok |
| 0.39 | 9/23 | 2 | 2.5896s | 1.6167s | 3.5625s | 1.0 | yes | ok |
| 0.43 | 10/23 | 2 | 1.6590s | 1.4171s | 1.9009s | 1.0 | yes | ok |
| 0.48 | 11/23 | 2 | 1.6357s | 1.4842s | 1.7873s | 1.0 | yes | ok |
| 0.52 | 12/23 | 2 | 2.9263s | 1.7252s | 4.1275s | 1.0 | yes | ok |
| 0.57 | 13/23 | 2 | 2.8394s | 2.0861s | 3.5927s | 1.0 | yes | ok |
| 0.61 | 14/23 | 2 | 3.0214s | 2.1871s | 3.8556s | 1.0 | yes | ok |
| 0.65 | 15/23 | 2 | 3.7890s | 3.6166s | 3.9614s | 1.0 | yes | ok |
| 0.70 | 16/23 | 2 | 3.6892s | 3.6827s | 3.6957s | 1.0 | yes | ok |
| 0.74 | 17/23 | 2 | 2.6140s | 1.6916s | 3.5364s | 1.0 | yes | ok |
| 0.78 | 18/23 | 2 | 3.1645s | 2.1918s | 4.1371s | 1.0 | yes | ok |
| 0.83 | 19/23 | 2 | 3.1488s | 2.4110s | 3.8866s | 1.0 | yes | ok |
| 0.87 | 20/23 | 2 | 3.9953s | 3.8785s | 4.1120s | 1.0 | yes | ok |
| 0.91 | 21/23 | 2 | 4.0595s | 3.9515s | 4.1676s | 1.0 | yes | ok |
| 0.96 | 22/23 | 2 | 4.1334s | 4.1104s | 4.1563s | 1.0 | yes | ok |
| 1.00 | 23/23 | 1 | 4.2813s | 4.2813s | 4.2813s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/23 | 1 | 0.8995s | 0.0731s | 1 | 8 | yes | 0.8709s | 0.9522s | `detyped_files/richards/shallow/proportion_sweep/main_k00_s01.py` |  |
| 0.04 | 1/23 | 1 | 1.1636s | 0.0308s | 1 | 8 | yes | 1.1448s | 1.1854s | `detyped_files/richards/shallow/proportion_sweep/main_k01_s01.py` |  |
| 0.04 | 1/23 | 2 | 1.3939s | 0.1626s | 1 | 8 | yes | 1.2977s | 1.5052s | `detyped_files/richards/shallow/proportion_sweep/main_k01_s02.py` |  |
| 0.09 | 2/23 | 1 | 0.9203s | 0.0511s | 1 | 8 | yes | 0.8969s | 0.9575s | `detyped_files/richards/shallow/proportion_sweep/main_k02_s01.py` |  |
| 0.09 | 2/23 | 2 | 0.9358s | 0.0837s | 1 | 8 | yes | 0.8992s | 0.9969s | `detyped_files/richards/shallow/proportion_sweep/main_k02_s02.py` |  |
| 0.13 | 3/23 | 1 | 1.3332s | 0.2186s | 2 | 16 | yes | 1.2351s | 1.4411s | `detyped_files/richards/shallow/proportion_sweep/main_k03_s01.py` |  |
| 0.13 | 3/23 | 2 | 1.4979s | 0.1868s | 1 | 8 | yes | 1.3875s | 1.6281s | `detyped_files/richards/shallow/proportion_sweep/main_k03_s02.py` |  |
| 0.17 | 4/23 | 1 | 2.7683s | 0.1439s | 1 | 8 | yes | 2.6791s | 2.8594s | `detyped_files/richards/shallow/proportion_sweep/main_k04_s01.py` |  |
| 0.17 | 4/23 | 2 | 1.1655s | 0.1462s | 1 | 8 | yes | 1.0778s | 1.2670s | `detyped_files/richards/shallow/proportion_sweep/main_k04_s02.py` |  |
| 0.22 | 5/23 | 1 | 1.1184s | 0.1223s | 2 | 16 | yes | 1.0723s | 1.1828s | `detyped_files/richards/shallow/proportion_sweep/main_k05_s01.py` |  |
| 0.22 | 5/23 | 2 | 1.6695s | 0.1298s | 1 | 8 | yes | 1.5926s | 1.7598s | `detyped_files/richards/shallow/proportion_sweep/main_k05_s02.py` |  |
| 0.26 | 6/23 | 1 | 1.3247s | 0.1141s | 1 | 8 | yes | 1.2554s | 1.4027s | `detyped_files/richards/shallow/proportion_sweep/main_k06_s01.py` |  |
| 0.26 | 6/23 | 2 | 1.4573s | 0.1588s | 1 | 8 | yes | 1.3729s | 1.5671s | `detyped_files/richards/shallow/proportion_sweep/main_k06_s02.py` |  |
| 0.30 | 7/23 | 1 | 1.2392s | 0.1798s | 1 | 8 | yes | 1.1263s | 1.3561s | `detyped_files/richards/shallow/proportion_sweep/main_k07_s01.py` |  |
| 0.30 | 7/23 | 2 | 1.9103s | 0.1859s | 1 | 8 | yes | 1.8126s | 2.0418s | `detyped_files/richards/shallow/proportion_sweep/main_k07_s02.py` |  |
| 0.35 | 8/23 | 1 | 3.1202s | 0.0563s | 1 | 8 | yes | 3.0871s | 3.1597s | `detyped_files/richards/shallow/proportion_sweep/main_k08_s01.py` |  |
| 0.35 | 8/23 | 2 | 1.4012s | 0.1570s | 1 | 8 | yes | 1.3017s | 1.5030s | `detyped_files/richards/shallow/proportion_sweep/main_k08_s02.py` |  |
| 0.39 | 9/23 | 1 | 1.6167s | 0.1733s | 1 | 8 | yes | 1.5152s | 1.7308s | `detyped_files/richards/shallow/proportion_sweep/main_k09_s01.py` |  |
| 0.39 | 9/23 | 2 | 3.5625s | 0.1784s | 1 | 8 | yes | 3.4559s | 3.6849s | `detyped_files/richards/shallow/proportion_sweep/main_k09_s02.py` |  |
| 0.43 | 10/23 | 1 | 1.4171s | 0.1522s | 1 | 8 | yes | 1.3235s | 1.5199s | `detyped_files/richards/shallow/proportion_sweep/main_k10_s01.py` |  |
| 0.43 | 10/23 | 2 | 1.9009s | 0.1548s | 1 | 8 | yes | 1.8141s | 2.0075s | `detyped_files/richards/shallow/proportion_sweep/main_k10_s02.py` |  |
| 0.48 | 11/23 | 1 | 1.7873s | 0.1699s | 1 | 8 | yes | 1.6969s | 1.9025s | `detyped_files/richards/shallow/proportion_sweep/main_k11_s01.py` |  |
| 0.48 | 11/23 | 2 | 1.4842s | 0.1489s | 1 | 8 | yes | 1.4053s | 1.5876s | `detyped_files/richards/shallow/proportion_sweep/main_k11_s02.py` |  |
| 0.52 | 12/23 | 1 | 1.7252s | 0.1287s | 1 | 8 | yes | 1.6487s | 1.8150s | `detyped_files/richards/shallow/proportion_sweep/main_k12_s01.py` |  |
| 0.52 | 12/23 | 2 | 4.1275s | 0.1087s | 1 | 8 | yes | 4.0544s | 4.1947s | `detyped_files/richards/shallow/proportion_sweep/main_k12_s02.py` |  |
| 0.57 | 13/23 | 1 | 2.0861s | 0.2030s | 1 | 8 | yes | 1.9622s | 2.2267s | `detyped_files/richards/shallow/proportion_sweep/main_k13_s01.py` |  |
| 0.57 | 13/23 | 2 | 3.5927s | 0.0857s | 1 | 8 | yes | 3.5338s | 3.6507s | `detyped_files/richards/shallow/proportion_sweep/main_k13_s02.py` |  |
| 0.61 | 14/23 | 1 | 2.1871s | 0.1257s | 1 | 8 | yes | 2.1116s | 2.2685s | `detyped_files/richards/shallow/proportion_sweep/main_k14_s01.py` |  |
| 0.61 | 14/23 | 2 | 3.8556s | 0.0670s | 1 | 8 | yes | 3.8144s | 3.8998s | `detyped_files/richards/shallow/proportion_sweep/main_k14_s02.py` |  |
| 0.65 | 15/23 | 1 | 3.9614s | 0.1016s | 1 | 8 | yes | 3.9051s | 4.0337s | `detyped_files/richards/shallow/proportion_sweep/main_k15_s01.py` |  |
| 0.65 | 15/23 | 2 | 3.6166s | 0.0754s | 1 | 8 | yes | 3.5651s | 3.6635s | `detyped_files/richards/shallow/proportion_sweep/main_k15_s02.py` |  |
| 0.70 | 16/23 | 1 | 3.6827s | 0.1129s | 1 | 8 | yes | 3.6123s | 3.7584s | `detyped_files/richards/shallow/proportion_sweep/main_k16_s01.py` |  |
| 0.70 | 16/23 | 2 | 3.6957s | 0.1553s | 1 | 8 | yes | 3.6093s | 3.8053s | `detyped_files/richards/shallow/proportion_sweep/main_k16_s02.py` |  |
| 0.74 | 17/23 | 1 | 3.5364s | 0.0698s | 1 | 8 | yes | 3.4910s | 3.5817s | `detyped_files/richards/shallow/proportion_sweep/main_k17_s01.py` |  |
| 0.74 | 17/23 | 2 | 1.6916s | 0.1546s | 1 | 8 | yes | 1.6001s | 1.8016s | `detyped_files/richards/shallow/proportion_sweep/main_k17_s02.py` |  |
| 0.78 | 18/23 | 1 | 2.1918s | 0.1719s | 1 | 8 | yes | 2.0810s | 2.3067s | `detyped_files/richards/shallow/proportion_sweep/main_k18_s01.py` |  |
| 0.78 | 18/23 | 2 | 4.1371s | 0.0843s | 1 | 8 | yes | 4.0810s | 4.1892s | `detyped_files/richards/shallow/proportion_sweep/main_k18_s02.py` |  |
| 0.83 | 19/23 | 1 | 3.8866s | 0.1662s | 1 | 8 | yes | 3.7942s | 4.0033s | `detyped_files/richards/shallow/proportion_sweep/main_k19_s01.py` |  |
| 0.83 | 19/23 | 2 | 2.4110s | 0.1650s | 1 | 8 | yes | 2.3129s | 2.5231s | `detyped_files/richards/shallow/proportion_sweep/main_k19_s02.py` |  |
| 0.87 | 20/23 | 1 | 4.1120s | 0.1550s | 1 | 8 | yes | 4.0076s | 4.2084s | `detyped_files/richards/shallow/proportion_sweep/main_k20_s01.py` |  |
| 0.87 | 20/23 | 2 | 3.8785s | 0.1451s | 1 | 8 | yes | 3.7930s | 3.9816s | `detyped_files/richards/shallow/proportion_sweep/main_k20_s02.py` |  |
| 0.91 | 21/23 | 1 | 3.9515s | 0.1653s | 1 | 8 | yes | 3.8547s | 4.0651s | `detyped_files/richards/shallow/proportion_sweep/main_k21_s01.py` |  |
| 0.91 | 21/23 | 2 | 4.1676s | 0.1462s | 1 | 8 | yes | 4.0676s | 4.2579s | `detyped_files/richards/shallow/proportion_sweep/main_k21_s02.py` |  |
| 0.96 | 22/23 | 1 | 4.1563s | 0.1664s | 1 | 8 | yes | 4.0533s | 4.2640s | `detyped_files/richards/shallow/proportion_sweep/main_k22_s01.py` |  |
| 0.96 | 22/23 | 2 | 4.1104s | 0.1141s | 1 | 8 | yes | 4.0344s | 4.1833s | `detyped_files/richards/shallow/proportion_sweep/main_k22_s02.py` |  |
| 1.00 | 23/23 | 1 | 4.2813s | 0.1860s | 1 | 8 | yes | 4.1582s | 4.3948s | `detyped_files/richards/shallow/proportion_sweep/main_k23_s01.py` |  |

## richards/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.7923s | 0.7923s | 0.7923s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.7923s | 0.1054s | 1 | 8 | yes | 0.7412s | 0.8669s | `static-python-perf/Benchmark/richards/untyped/main.py` |  |
