# Proportion Benchmark Report

- Generated: `2026-04-02T05:39:03-06:00`
- Benchmarks run serially: `yes`
- Iterations per detyped-count bucket: `20`
- Random seed: `0`

## call_method/advanced

- Detypable targets: `6`
- Total runs: `64`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1154s | 0.1154s | 0.1154s | 2.0 | yes | ok |
| 0.17 | 1/6 | 6 | 0.3375s | 0.1093s | 1.2412s | 1.2 | yes | ok |
| 0.33 | 2/6 | 15 | 0.5555s | 0.1258s | 1.3654s | 1.1 | yes | ok |
| 0.50 | 3/6 | 20 | 0.7882s | 0.1526s | 1.4411s | 1.0 | yes | ok |
| 0.67 | 4/6 | 15 | 1.0102s | 0.1743s | 1.4471s | 1.0 | yes | ok |
| 0.83 | 5/6 | 6 | 1.1957s | 0.3390s | 1.4221s | 1.0 | yes | ok |
| 1.00 | 6/6 | 1 | 1.4075s | 1.4075s | 1.4075s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1154s | 0.0150s | 2 | 16 | yes | 0.1084s | 0.1224s | `detyped_files/call_method/advanced/proportion_sweep/main_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 0.2782s | 0.0161s | 1 | 8 | yes | 0.2672s | 0.2879s | `detyped_files/call_method/advanced/proportion_sweep/main_k01_s01.py` |  |
| 0.17 | 1/6 | 2 | 0.1259s | 0.0192s | 2 | 16 | yes | 0.1170s | 0.1351s | `detyped_files/call_method/advanced/proportion_sweep/main_k01_s02.py` |  |
| 0.17 | 1/6 | 3 | 0.1384s | 0.0114s | 1 | 8 | yes | 0.1317s | 0.1463s | `detyped_files/call_method/advanced/proportion_sweep/main_k01_s03.py` |  |
| 0.17 | 1/6 | 4 | 1.2412s | 0.0800s | 1 | 8 | yes | 1.1931s | 1.2942s | `detyped_files/call_method/advanced/proportion_sweep/main_k01_s04.py` |  |
| 0.17 | 1/6 | 5 | 0.1317s | 0.0164s | 1 | 8 | yes | 0.1202s | 0.1416s | `detyped_files/call_method/advanced/proportion_sweep/main_k01_s05.py` |  |
| 0.17 | 1/6 | 6 | 0.1093s | 0.0071s | 1 | 8 | yes | 0.1053s | 0.1146s | `detyped_files/call_method/advanced/proportion_sweep/main_k01_s06.py` |  |
| 0.33 | 2/6 | 1 | 1.2310s | 0.0709s | 1 | 8 | yes | 1.1828s | 1.2739s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s01.py` |  |
| 0.33 | 2/6 | 2 | 0.1494s | 0.0182s | 1 | 8 | yes | 0.1368s | 0.1609s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s02.py` |  |
| 0.33 | 2/6 | 3 | 0.1258s | 0.0062s | 1 | 8 | yes | 0.1234s | 0.1303s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s03.py` |  |
| 0.33 | 2/6 | 4 | 0.1294s | 0.0111s | 1 | 8 | yes | 0.1217s | 0.1362s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s04.py` |  |
| 0.33 | 2/6 | 5 | 1.3654s | 0.0423s | 1 | 8 | yes | 1.3428s | 1.3970s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s05.py` |  |
| 0.33 | 2/6 | 6 | 0.2940s | 0.0344s | 1 | 8 | yes | 0.2709s | 0.3144s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s06.py` |  |
| 0.33 | 2/6 | 7 | 1.2124s | 0.0572s | 1 | 8 | yes | 1.1708s | 1.2443s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s07.py` |  |
| 0.33 | 2/6 | 8 | 0.2985s | 0.0148s | 1 | 8 | yes | 0.2885s | 0.3077s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s08.py` |  |
| 0.33 | 2/6 | 9 | 0.1578s | 0.0120s | 1 | 8 | yes | 0.1500s | 0.1658s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s09.py` |  |
| 0.33 | 2/6 | 10 | 0.1343s | 0.0174s | 2 | 16 | yes | 0.1270s | 0.1439s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s10.py` |  |
| 0.33 | 2/6 | 11 | 1.2606s | 0.0686s | 1 | 8 | yes | 1.2274s | 1.3115s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s11.py` |  |
| 0.33 | 2/6 | 12 | 1.2140s | 0.0514s | 1 | 8 | yes | 1.1823s | 1.2481s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s12.py` |  |
| 0.33 | 2/6 | 13 | 0.1621s | 0.0204s | 1 | 8 | yes | 0.1526s | 0.1769s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s13.py` |  |
| 0.33 | 2/6 | 14 | 0.2910s | 0.0207s | 1 | 8 | yes | 0.2789s | 0.3060s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s14.py` |  |
| 0.33 | 2/6 | 15 | 0.3072s | 0.0302s | 1 | 8 | yes | 0.2894s | 0.3274s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s15.py` |  |
| 0.50 | 3/6 | 1 | 1.2370s | 0.0778s | 1 | 8 | yes | 1.1875s | 1.2896s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s01.py` |  |
| 0.50 | 3/6 | 2 | 1.3655s | 0.0615s | 1 | 8 | yes | 1.3225s | 1.4012s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s02.py` |  |
| 0.50 | 3/6 | 3 | 0.1741s | 0.0064s | 1 | 8 | yes | 0.1707s | 0.1787s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s03.py` |  |
| 0.50 | 3/6 | 4 | 1.2981s | 0.0868s | 1 | 8 | yes | 1.2535s | 1.3619s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s04.py` |  |
| 0.50 | 3/6 | 5 | 0.3144s | 0.0422s | 1 | 8 | yes | 0.2862s | 0.3402s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s05.py` |  |
| 0.50 | 3/6 | 6 | 1.2745s | 0.0245s | 1 | 8 | yes | 1.2577s | 1.2890s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s06.py` |  |
| 0.50 | 3/6 | 7 | 0.2911s | 0.0310s | 1 | 8 | yes | 0.2701s | 0.3100s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s07.py` |  |
| 0.50 | 3/6 | 8 | 0.1581s | 0.0112s | 1 | 8 | yes | 0.1516s | 0.1657s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s08.py` |  |
| 0.50 | 3/6 | 9 | 1.2880s | 0.1054s | 1 | 8 | yes | 1.2195s | 1.3538s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s09.py` |  |
| 0.50 | 3/6 | 10 | 1.3124s | 0.0932s | 1 | 8 | yes | 1.2514s | 1.3716s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s10.py` |  |
| 0.50 | 3/6 | 11 | 0.3063s | 0.0109s | 1 | 8 | yes | 0.3006s | 0.3142s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s11.py` |  |
| 0.50 | 3/6 | 12 | 0.1566s | 0.0085s | 1 | 8 | yes | 0.1523s | 0.1627s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s12.py` |  |
| 0.50 | 3/6 | 13 | 0.1526s | 0.0212s | 1 | 8 | yes | 0.1402s | 0.1670s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s13.py` |  |
| 0.50 | 3/6 | 14 | 0.3088s | 0.0173s | 1 | 8 | yes | 0.2992s | 0.3210s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s14.py` |  |
| 0.50 | 3/6 | 15 | 1.2457s | 0.0302s | 1 | 8 | yes | 1.2250s | 1.2626s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s15.py` |  |
| 0.50 | 3/6 | 16 | 1.4028s | 0.0835s | 1 | 8 | yes | 1.3556s | 1.4635s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s16.py` |  |
| 0.50 | 3/6 | 17 | 0.3324s | 0.0392s | 1 | 8 | yes | 0.3105s | 0.3602s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s17.py` |  |
| 0.50 | 3/6 | 18 | 0.3165s | 0.0278s | 1 | 8 | yes | 0.2976s | 0.3329s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s18.py` |  |
| 0.50 | 3/6 | 19 | 1.4411s | 0.1315s | 1 | 8 | yes | 1.3721s | 1.5389s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s19.py` |  |
| 0.50 | 3/6 | 20 | 1.3887s | 0.0735s | 1 | 8 | yes | 1.3395s | 1.4349s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s20.py` |  |
| 0.67 | 4/6 | 1 | 0.3207s | 0.0332s | 1 | 8 | yes | 0.2982s | 0.3431s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s01.py` |  |
| 0.67 | 4/6 | 2 | 0.3145s | 0.0252s | 1 | 8 | yes | 0.2978s | 0.3308s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s02.py` |  |
| 0.67 | 4/6 | 3 | 1.2770s | 0.0871s | 1 | 8 | yes | 1.2219s | 1.3353s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s03.py` |  |
| 0.67 | 4/6 | 4 | 1.3787s | 0.0611s | 1 | 8 | yes | 1.3378s | 1.4170s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s04.py` |  |
| 0.67 | 4/6 | 5 | 1.2957s | 0.0624s | 1 | 8 | yes | 1.2582s | 1.3382s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s05.py` |  |
| 0.67 | 4/6 | 6 | 1.4471s | 0.1342s | 1 | 8 | yes | 1.3835s | 1.5464s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s06.py` |  |
| 0.67 | 4/6 | 7 | 1.4253s | 0.1078s | 1 | 8 | yes | 1.3582s | 1.4975s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s07.py` |  |
| 0.67 | 4/6 | 8 | 0.3420s | 0.0335s | 1 | 8 | yes | 0.3176s | 0.3606s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s08.py` |  |
| 0.67 | 4/6 | 9 | 1.2927s | 0.0736s | 1 | 8 | yes | 1.2491s | 1.3429s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s09.py` |  |
| 0.67 | 4/6 | 10 | 1.3816s | 0.0893s | 1 | 8 | yes | 1.3252s | 1.4443s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s10.py` |  |
| 0.67 | 4/6 | 11 | 1.4105s | 0.0949s | 1 | 8 | yes | 1.3520s | 1.4725s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s11.py` |  |
| 0.67 | 4/6 | 12 | 0.3368s | 0.0255s | 1 | 8 | yes | 0.3205s | 0.3525s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s12.py` |  |
| 0.67 | 4/6 | 13 | 1.4453s | 0.0490s | 1 | 8 | yes | 1.4153s | 1.4771s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s13.py` |  |
| 0.67 | 4/6 | 14 | 1.3108s | 0.1051s | 1 | 8 | yes | 1.2464s | 1.3817s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s14.py` |  |
| 0.67 | 4/6 | 15 | 0.1743s | 0.0060s | 1 | 8 | yes | 0.1710s | 0.1786s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s15.py` |  |
| 0.83 | 5/6 | 1 | 1.3987s | 0.0365s | 1 | 8 | yes | 1.3781s | 1.4245s | `detyped_files/call_method/advanced/proportion_sweep/main_k05_s01.py` |  |
| 0.83 | 5/6 | 2 | 1.2707s | 0.0686s | 1 | 8 | yes | 1.2230s | 1.3123s | `detyped_files/call_method/advanced/proportion_sweep/main_k05_s02.py` |  |
| 0.83 | 5/6 | 3 | 0.3390s | 0.0158s | 1 | 8 | yes | 0.3281s | 0.3485s | `detyped_files/call_method/advanced/proportion_sweep/main_k05_s03.py` |  |
| 0.83 | 5/6 | 4 | 1.4221s | 0.1319s | 1 | 8 | yes | 1.3491s | 1.5176s | `detyped_files/call_method/advanced/proportion_sweep/main_k05_s04.py` |  |
| 0.83 | 5/6 | 5 | 1.3728s | 0.0811s | 1 | 8 | yes | 1.3178s | 1.4222s | `detyped_files/call_method/advanced/proportion_sweep/main_k05_s05.py` |  |
| 0.83 | 5/6 | 6 | 1.3712s | 0.0616s | 1 | 8 | yes | 1.3307s | 1.4104s | `detyped_files/call_method/advanced/proportion_sweep/main_k05_s06.py` |  |
| 1.00 | 6/6 | 1 | 1.4075s | 0.0483s | 1 | 8 | yes | 1.3769s | 1.4390s | `detyped_files/call_method/advanced/proportion_sweep/main_k06_s01.py` |  |

## call_method/shallow

- Detypable targets: `6`
- Total runs: `64`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1144s | 0.1144s | 0.1144s | 2.0 | yes | ok |
| 0.17 | 1/6 | 6 | 0.3154s | 0.1101s | 1.2356s | 1.2 | yes | ok |
| 0.33 | 2/6 | 15 | 0.5182s | 0.1110s | 1.2989s | 1.3 | yes | ok |
| 0.50 | 3/6 | 20 | 0.7238s | 0.1068s | 1.4052s | 1.1 | yes | ok |
| 0.67 | 4/6 | 15 | 0.9093s | 0.1227s | 1.3281s | 1.1 | yes | ok |
| 0.83 | 5/6 | 6 | 1.1147s | 0.1893s | 1.3552s | 1.0 | yes | ok |
| 1.00 | 6/6 | 1 | 1.2894s | 1.2894s | 1.2894s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1144s | 0.0188s | 2 | 16 | yes | 0.1062s | 0.1238s | `detyped_files/call_method/shallow/proportion_sweep/main_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 1.2356s | 0.1444s | 1 | 8 | yes | 1.1581s | 1.3400s | `detyped_files/call_method/shallow/proportion_sweep/main_k01_s01.py` |  |
| 0.17 | 1/6 | 2 | 0.1956s | 0.0119s | 1 | 8 | yes | 0.1882s | 0.2035s | `detyped_files/call_method/shallow/proportion_sweep/main_k01_s02.py` |  |
| 0.17 | 1/6 | 3 | 0.1113s | 0.0147s | 1 | 8 | yes | 0.1024s | 0.1221s | `detyped_files/call_method/shallow/proportion_sweep/main_k01_s03.py` |  |
| 0.17 | 1/6 | 4 | 0.1176s | 0.0077s | 1 | 8 | yes | 0.1138s | 0.1232s | `detyped_files/call_method/shallow/proportion_sweep/main_k01_s04.py` |  |
| 0.17 | 1/6 | 5 | 0.1219s | 0.0175s | 2 | 16 | yes | 0.1141s | 0.1307s | `detyped_files/call_method/shallow/proportion_sweep/main_k01_s05.py` |  |
| 0.17 | 1/6 | 6 | 0.1101s | 0.0044s | 1 | 8 | yes | 0.1078s | 0.1132s | `detyped_files/call_method/shallow/proportion_sweep/main_k01_s06.py` |  |
| 0.33 | 2/6 | 1 | 1.2441s | 0.0729s | 1 | 8 | yes | 1.1930s | 1.2857s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s01.py` |  |
| 0.33 | 2/6 | 2 | 1.2630s | 0.0658s | 1 | 8 | yes | 1.2210s | 1.3073s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s02.py` |  |
| 0.33 | 2/6 | 3 | 0.1845s | 0.0228s | 1 | 8 | yes | 0.1708s | 0.2005s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s03.py` |  |
| 0.33 | 2/6 | 4 | 0.1851s | 0.0217s | 1 | 8 | yes | 0.1699s | 0.1989s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s04.py` |  |
| 0.33 | 2/6 | 5 | 0.1858s | 0.0155s | 1 | 8 | yes | 0.1770s | 0.1968s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s05.py` |  |
| 0.33 | 2/6 | 6 | 0.1182s | 0.0094s | 1 | 8 | yes | 0.1123s | 0.1245s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s06.py` |  |
| 0.33 | 2/6 | 7 | 0.1226s | 0.0130s | 1 | 8 | yes | 0.1153s | 0.1315s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s07.py` |  |
| 0.33 | 2/6 | 8 | 1.2989s | 0.1163s | 1 | 8 | yes | 1.2322s | 1.3799s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s08.py` |  |
| 0.33 | 2/6 | 9 | 0.1110s | 0.0178s | 2 | 16 | yes | 0.1028s | 0.1198s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s09.py` |  |
| 0.33 | 2/6 | 10 | 0.1231s | 0.0165s | 1 | 8 | yes | 0.1138s | 0.1341s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s10.py` |  |
| 0.33 | 2/6 | 11 | 1.2584s | 0.1268s | 1 | 8 | yes | 1.1828s | 1.3433s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s11.py` |  |
| 0.33 | 2/6 | 12 | 1.2439s | 0.0634s | 1 | 8 | yes | 1.2024s | 1.2827s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s12.py` |  |
| 0.33 | 2/6 | 13 | 0.1195s | 0.0145s | 2 | 16 | yes | 0.1139s | 0.1276s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s13.py` |  |
| 0.33 | 2/6 | 14 | 0.1956s | 0.0358s | 2 | 16 | yes | 0.1799s | 0.2138s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s14.py` |  |
| 0.33 | 2/6 | 15 | 0.1196s | 0.0184s | 2 | 16 | yes | 0.1116s | 0.1289s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s15.py` |  |
| 0.50 | 3/6 | 1 | 1.3174s | 0.0893s | 1 | 8 | yes | 1.2578s | 1.3741s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s01.py` |  |
| 0.50 | 3/6 | 2 | 0.2001s | 0.0214s | 1 | 8 | yes | 0.1872s | 0.2151s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s02.py` |  |
| 0.50 | 3/6 | 3 | 0.1933s | 0.0094s | 1 | 8 | yes | 0.1878s | 0.2001s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s03.py` |  |
| 0.50 | 3/6 | 4 | 0.1957s | 0.0184s | 1 | 8 | yes | 0.1839s | 0.2080s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s04.py` |  |
| 0.50 | 3/6 | 5 | 1.2310s | 0.0883s | 1 | 8 | yes | 1.1715s | 1.2860s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s05.py` |  |
| 0.50 | 3/6 | 6 | 1.4052s | 0.1443s | 1 | 8 | yes | 1.3176s | 1.5069s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s06.py` |  |
| 0.50 | 3/6 | 7 | 0.1924s | 0.0105s | 1 | 8 | yes | 0.1845s | 0.1981s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s07.py` |  |
| 0.50 | 3/6 | 8 | 0.1224s | 0.0137s | 1 | 8 | yes | 0.1146s | 0.1323s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s08.py` |  |
| 0.50 | 3/6 | 9 | 0.1251s | 0.0169s | 2 | 16 | yes | 0.1180s | 0.1342s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s09.py` |  |
| 0.50 | 3/6 | 10 | 1.2952s | 0.1154s | 1 | 8 | yes | 1.2284s | 1.3766s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s10.py` |  |
| 0.50 | 3/6 | 11 | 1.2410s | 0.0623s | 1 | 8 | yes | 1.1981s | 1.2796s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s11.py` |  |
| 0.50 | 3/6 | 12 | 1.2853s | 0.0753s | 1 | 8 | yes | 1.2338s | 1.3291s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s12.py` |  |
| 0.50 | 3/6 | 13 | 0.1068s | 0.0049s | 1 | 8 | yes | 0.1032s | 0.1090s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s13.py` |  |
| 0.50 | 3/6 | 14 | 1.3307s | 0.0535s | 1 | 8 | yes | 1.2989s | 1.3670s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s14.py` |  |
| 0.50 | 3/6 | 15 | 1.2550s | 0.0460s | 1 | 8 | yes | 1.2273s | 1.2866s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s15.py` |  |
| 0.50 | 3/6 | 16 | 1.2481s | 0.1089s | 1 | 8 | yes | 1.1938s | 1.3280s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s16.py` |  |
| 0.50 | 3/6 | 17 | 0.1765s | 0.0157s | 1 | 8 | yes | 0.1654s | 0.1853s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s17.py` |  |
| 0.50 | 3/6 | 18 | 1.2363s | 0.0529s | 1 | 8 | yes | 1.2075s | 1.2735s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s18.py` |  |
| 0.50 | 3/6 | 19 | 0.1904s | 0.0109s | 1 | 8 | yes | 0.1839s | 0.1981s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s19.py` |  |
| 0.50 | 3/6 | 20 | 0.1288s | 0.0216s | 2 | 16 | yes | 0.1197s | 0.1403s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s20.py` |  |
| 0.67 | 4/6 | 1 | 1.3004s | 0.1019s | 1 | 8 | yes | 1.2380s | 1.3664s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s01.py` |  |
| 0.67 | 4/6 | 2 | 0.1886s | 0.0183s | 1 | 8 | yes | 0.1759s | 0.1996s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s02.py` |  |
| 0.67 | 4/6 | 3 | 1.3065s | 0.0860s | 1 | 8 | yes | 1.2551s | 1.3658s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s03.py` |  |
| 0.67 | 4/6 | 4 | 0.1227s | 0.0170s | 2 | 16 | yes | 0.1147s | 0.1308s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s04.py` |  |
| 0.67 | 4/6 | 5 | 1.2766s | 0.0924s | 1 | 8 | yes | 1.2240s | 1.3403s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s05.py` |  |
| 0.67 | 4/6 | 6 | 1.3281s | 0.0724s | 1 | 8 | yes | 1.2868s | 1.3796s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s06.py` |  |
| 0.67 | 4/6 | 7 | 1.2151s | 0.0315s | 1 | 8 | yes | 1.1923s | 1.2318s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s07.py` |  |
| 0.67 | 4/6 | 8 | 0.2075s | 0.0244s | 1 | 8 | yes | 0.1934s | 0.2240s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s08.py` |  |
| 0.67 | 4/6 | 9 | 1.3060s | 0.0343s | 1 | 8 | yes | 1.2847s | 1.3288s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s09.py` |  |
| 0.67 | 4/6 | 10 | 0.2032s | 0.0271s | 1 | 8 | yes | 0.1899s | 0.2231s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s10.py` |  |
| 0.67 | 4/6 | 11 | 0.1858s | 0.0140s | 1 | 8 | yes | 0.1760s | 0.1937s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s11.py` |  |
| 0.67 | 4/6 | 12 | 1.2119s | 0.0656s | 1 | 8 | yes | 1.1719s | 1.2553s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s12.py` |  |
| 0.67 | 4/6 | 13 | 1.2594s | 0.1122s | 1 | 8 | yes | 1.1942s | 1.3362s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s13.py` |  |
| 0.67 | 4/6 | 14 | 1.2600s | 0.1166s | 1 | 8 | yes | 1.1936s | 1.3414s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s14.py` |  |
| 0.67 | 4/6 | 15 | 1.2673s | 0.0451s | 1 | 8 | yes | 1.2370s | 1.2954s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s15.py` |  |
| 0.83 | 5/6 | 1 | 1.3124s | 0.0609s | 1 | 8 | yes | 1.2787s | 1.3564s | `detyped_files/call_method/shallow/proportion_sweep/main_k05_s01.py` |  |
| 0.83 | 5/6 | 2 | 0.1893s | 0.0214s | 1 | 8 | yes | 0.1748s | 0.2032s | `detyped_files/call_method/shallow/proportion_sweep/main_k05_s02.py` |  |
| 0.83 | 5/6 | 3 | 1.2788s | 0.0908s | 1 | 8 | yes | 1.2239s | 1.3426s | `detyped_files/call_method/shallow/proportion_sweep/main_k05_s03.py` |  |
| 0.83 | 5/6 | 4 | 1.2647s | 0.0523s | 1 | 8 | yes | 1.2332s | 1.3008s | `detyped_files/call_method/shallow/proportion_sweep/main_k05_s04.py` |  |
| 0.83 | 5/6 | 5 | 1.3552s | 0.0729s | 1 | 8 | yes | 1.3091s | 1.4050s | `detyped_files/call_method/shallow/proportion_sweep/main_k05_s05.py` |  |
| 0.83 | 5/6 | 6 | 1.2875s | 0.0596s | 1 | 8 | yes | 1.2461s | 1.3246s | `detyped_files/call_method/shallow/proportion_sweep/main_k05_s06.py` |  |
| 1.00 | 6/6 | 1 | 1.2894s | 0.0603s | 1 | 8 | yes | 1.2454s | 1.3201s | `detyped_files/call_method/shallow/proportion_sweep/main_k06_s01.py` |  |

## call_method/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.1283s | 0.1283s | 0.1283s | 2.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.1283s | 0.0256s | 2 | 16 | yes | 0.1170s | 0.1410s | `static-python-perf/Benchmark/call_method/untyped/main.py` |  |

## call_method_slots/advanced

- Detypable targets: `6`
- Total runs: `64`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1103s | 0.1103s | 0.1103s | 1.0 | yes | ok |
| 0.17 | 1/6 | 6 | 0.3413s | 0.1185s | 1.2582s | 1.2 | yes | ok |
| 0.33 | 2/6 | 15 | 0.5569s | 0.1293s | 1.3875s | 1.0 | yes | ok |
| 0.50 | 3/6 | 20 | 0.7861s | 0.1513s | 1.4888s | 1.1 | yes | ok |
| 0.67 | 4/6 | 15 | 0.9973s | 0.1791s | 1.4229s | 1.0 | yes | ok |
| 0.83 | 5/6 | 6 | 1.2146s | 0.3237s | 1.4514s | 1.0 | yes | ok |
| 1.00 | 6/6 | 1 | 1.3980s | 1.3980s | 1.3980s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1103s | 0.0039s | 1 | 8 | yes | 0.1076s | 0.1127s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 0.1264s | 0.0091s | 1 | 8 | yes | 0.1206s | 0.1326s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k01_s01.py` |  |
| 0.17 | 1/6 | 2 | 0.1185s | 0.0136s | 1 | 8 | yes | 0.1105s | 0.1274s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k01_s02.py` |  |
| 0.17 | 1/6 | 3 | 0.2700s | 0.0221s | 1 | 8 | yes | 0.2542s | 0.2824s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k01_s03.py` |  |
| 0.17 | 1/6 | 4 | 0.1363s | 0.0152s | 2 | 16 | yes | 0.1302s | 0.1444s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k01_s04.py` |  |
| 0.17 | 1/6 | 5 | 1.2582s | 0.0667s | 1 | 8 | yes | 1.2200s | 1.3059s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k01_s05.py` |  |
| 0.17 | 1/6 | 6 | 0.1387s | 0.0105s | 1 | 8 | yes | 0.1329s | 0.1464s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k01_s06.py` |  |
| 0.33 | 2/6 | 1 | 1.2448s | 0.0794s | 1 | 8 | yes | 1.1927s | 1.2942s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k02_s01.py` |  |
| 0.33 | 2/6 | 2 | 0.3118s | 0.0255s | 1 | 8 | yes | 0.2973s | 0.3298s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k02_s02.py` |  |
| 0.33 | 2/6 | 3 | 1.2319s | 0.0558s | 1 | 8 | yes | 1.1955s | 1.2674s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k02_s03.py` |  |
| 0.33 | 2/6 | 4 | 0.1599s | 0.0178s | 1 | 8 | yes | 0.1516s | 0.1729s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k02_s04.py` |  |
| 0.33 | 2/6 | 5 | 0.1361s | 0.0125s | 1 | 8 | yes | 0.1295s | 0.1453s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k02_s05.py` |  |
| 0.33 | 2/6 | 6 | 1.1841s | 0.0707s | 1 | 8 | yes | 1.1379s | 1.2279s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k02_s06.py` |  |
| 0.33 | 2/6 | 7 | 1.3875s | 0.1397s | 1 | 8 | yes | 1.3013s | 1.4802s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k02_s07.py` |  |
| 0.33 | 2/6 | 8 | 0.1293s | 0.0127s | 1 | 8 | yes | 0.1200s | 0.1360s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k02_s08.py` |  |
| 0.33 | 2/6 | 9 | 0.2975s | 0.0227s | 1 | 8 | yes | 0.2825s | 0.3114s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k02_s09.py` |  |
| 0.33 | 2/6 | 10 | 1.2232s | 0.0805s | 1 | 8 | yes | 1.1725s | 1.2771s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k02_s10.py` |  |
| 0.33 | 2/6 | 11 | 0.3283s | 0.0332s | 1 | 8 | yes | 0.3091s | 0.3513s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k02_s11.py` |  |
| 0.33 | 2/6 | 12 | 0.2845s | 0.0272s | 1 | 8 | yes | 0.2664s | 0.3022s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k02_s12.py` |  |
| 0.33 | 2/6 | 13 | 0.1527s | 0.0096s | 1 | 8 | yes | 0.1458s | 0.1579s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k02_s13.py` |  |
| 0.33 | 2/6 | 14 | 0.1512s | 0.0082s | 1 | 8 | yes | 0.1471s | 0.1571s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k02_s14.py` |  |
| 0.33 | 2/6 | 15 | 0.1301s | 0.0054s | 1 | 8 | yes | 0.1268s | 0.1337s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k02_s15.py` |  |
| 0.50 | 3/6 | 1 | 1.4888s | 0.1688s | 1 | 8 | yes | 1.3821s | 1.6004s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s01.py` |  |
| 0.50 | 3/6 | 2 | 1.2220s | 0.0590s | 1 | 8 | yes | 1.1871s | 1.2620s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s02.py` |  |
| 0.50 | 3/6 | 3 | 0.3115s | 0.0249s | 1 | 8 | yes | 0.2948s | 0.3265s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s03.py` |  |
| 0.50 | 3/6 | 4 | 1.3729s | 0.0625s | 1 | 8 | yes | 1.3288s | 1.4089s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s04.py` |  |
| 0.50 | 3/6 | 5 | 0.1519s | 0.0184s | 2 | 16 | yes | 0.1437s | 0.1613s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s05.py` |  |
| 0.50 | 3/6 | 6 | 1.3286s | 0.1319s | 1 | 8 | yes | 1.2493s | 1.4198s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s06.py` |  |
| 0.50 | 3/6 | 7 | 0.3211s | 0.0261s | 1 | 8 | yes | 0.3045s | 0.3382s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s07.py` |  |
| 0.50 | 3/6 | 8 | 0.3291s | 0.0256s | 1 | 8 | yes | 0.3113s | 0.3441s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s08.py` |  |
| 0.50 | 3/6 | 9 | 0.2998s | 0.0175s | 1 | 8 | yes | 0.2873s | 0.3089s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s09.py` |  |
| 0.50 | 3/6 | 10 | 1.2852s | 0.0769s | 1 | 8 | yes | 1.2386s | 1.3361s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s10.py` |  |
| 0.50 | 3/6 | 11 | 1.3843s | 0.0549s | 1 | 8 | yes | 1.3467s | 1.4180s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s11.py` |  |
| 0.50 | 3/6 | 12 | 1.2925s | 0.0602s | 1 | 8 | yes | 1.2568s | 1.3340s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s12.py` |  |
| 0.50 | 3/6 | 13 | 0.1513s | 0.0115s | 1 | 8 | yes | 0.1429s | 0.1568s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s13.py` |  |
| 0.50 | 3/6 | 14 | 1.2639s | 0.0840s | 1 | 8 | yes | 1.2096s | 1.3186s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s14.py` |  |
| 0.50 | 3/6 | 15 | 1.2417s | 0.0253s | 1 | 8 | yes | 1.2258s | 1.2584s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s15.py` |  |
| 0.50 | 3/6 | 16 | 0.1734s | 0.0125s | 1 | 8 | yes | 0.1647s | 0.1805s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s16.py` |  |
| 0.50 | 3/6 | 17 | 0.3008s | 0.0240s | 1 | 8 | yes | 0.2855s | 0.3167s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s17.py` |  |
| 0.50 | 3/6 | 18 | 0.1560s | 0.0080s | 1 | 8 | yes | 0.1515s | 0.1617s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s18.py` |  |
| 0.50 | 3/6 | 19 | 0.2992s | 0.0309s | 1 | 8 | yes | 0.2799s | 0.3191s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s19.py` |  |
| 0.50 | 3/6 | 20 | 1.3475s | 0.0880s | 1 | 8 | yes | 1.2914s | 1.4048s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s20.py` |  |
| 0.67 | 4/6 | 1 | 1.2764s | 0.0449s | 1 | 8 | yes | 1.2471s | 1.3047s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k04_s01.py` |  |
| 0.67 | 4/6 | 2 | 1.2662s | 0.1333s | 1 | 8 | yes | 1.1967s | 1.3632s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k04_s02.py` |  |
| 0.67 | 4/6 | 3 | 1.4079s | 0.0758s | 1 | 8 | yes | 1.3640s | 1.4615s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k04_s03.py` |  |
| 0.67 | 4/6 | 4 | 1.4061s | 0.0593s | 1 | 8 | yes | 1.3759s | 1.4496s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k04_s04.py` |  |
| 0.67 | 4/6 | 5 | 0.3309s | 0.0285s | 1 | 8 | yes | 0.3123s | 0.3496s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k04_s05.py` |  |
| 0.67 | 4/6 | 6 | 0.3020s | 0.0242s | 1 | 8 | yes | 0.2862s | 0.3171s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k04_s06.py` |  |
| 0.67 | 4/6 | 7 | 1.3899s | 0.1012s | 1 | 8 | yes | 1.3280s | 1.4592s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k04_s07.py` |  |
| 0.67 | 4/6 | 8 | 1.4011s | 0.0952s | 1 | 8 | yes | 1.3396s | 1.4642s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k04_s08.py` |  |
| 0.67 | 4/6 | 9 | 1.4038s | 0.0607s | 1 | 8 | yes | 1.3656s | 1.4434s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k04_s09.py` |  |
| 0.67 | 4/6 | 10 | 1.2888s | 0.0626s | 1 | 8 | yes | 1.2463s | 1.3291s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k04_s10.py` |  |
| 0.67 | 4/6 | 11 | 0.2931s | 0.0251s | 1 | 8 | yes | 0.2761s | 0.3085s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k04_s11.py` |  |
| 0.67 | 4/6 | 12 | 0.3207s | 0.0313s | 1 | 8 | yes | 0.2988s | 0.3387s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k04_s12.py` |  |
| 0.67 | 4/6 | 13 | 1.2708s | 0.0725s | 1 | 8 | yes | 1.2250s | 1.3198s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k04_s13.py` |  |
| 0.67 | 4/6 | 14 | 0.1791s | 0.0092s | 1 | 8 | yes | 0.1736s | 0.1855s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k04_s14.py` |  |
| 0.67 | 4/6 | 15 | 1.4229s | 0.0619s | 1 | 8 | yes | 1.3912s | 1.4670s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k04_s15.py` |  |
| 0.83 | 5/6 | 1 | 0.3237s | 0.0320s | 1 | 8 | yes | 0.3013s | 0.3433s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k05_s01.py` |  |
| 0.83 | 5/6 | 2 | 1.3845s | 0.0869s | 1 | 8 | yes | 1.3335s | 1.4447s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k05_s02.py` |  |
| 0.83 | 5/6 | 3 | 1.4135s | 0.1316s | 1 | 8 | yes | 1.3314s | 1.5016s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k05_s03.py` |  |
| 0.83 | 5/6 | 4 | 1.3978s | 0.0597s | 1 | 8 | yes | 1.3602s | 1.4368s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k05_s04.py` |  |
| 0.83 | 5/6 | 5 | 1.4514s | 0.1009s | 1 | 8 | yes | 1.3885s | 1.5165s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k05_s05.py` |  |
| 0.83 | 5/6 | 6 | 1.3166s | 0.0282s | 1 | 8 | yes | 1.2986s | 1.3348s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k05_s06.py` |  |
| 1.00 | 6/6 | 1 | 1.3980s | 0.0790s | 1 | 8 | yes | 1.3460s | 1.4483s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k06_s01.py` |  |

## call_method_slots/shallow

- Detypable targets: `6`
- Total runs: `64`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1114s | 0.1114s | 0.1114s | 1.0 | yes | ok |
| 0.17 | 1/6 | 6 | 0.3195s | 0.1090s | 1.2752s | 1.0 | yes | ok |
| 0.33 | 2/6 | 15 | 0.5071s | 0.1124s | 1.2534s | 1.0 | yes | ok |
| 0.50 | 3/6 | 20 | 0.7276s | 0.1074s | 1.3512s | 1.1 | yes | ok |
| 0.67 | 4/6 | 15 | 0.9110s | 0.1157s | 1.3309s | 1.1 | yes | ok |
| 0.83 | 5/6 | 6 | 1.1177s | 0.2018s | 1.3455s | 1.0 | yes | ok |
| 1.00 | 6/6 | 1 | 1.2944s | 1.2944s | 1.2944s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1114s | 0.0068s | 1 | 8 | yes | 0.1071s | 0.1158s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 1.2752s | 0.1014s | 1 | 8 | yes | 1.2140s | 1.3421s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k01_s01.py` |  |
| 0.17 | 1/6 | 2 | 0.1890s | 0.0081s | 1 | 8 | yes | 0.1846s | 0.1949s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k01_s02.py` |  |
| 0.17 | 1/6 | 3 | 0.1158s | 0.0097s | 1 | 8 | yes | 0.1121s | 0.1227s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k01_s03.py` |  |
| 0.17 | 1/6 | 4 | 0.1186s | 0.0119s | 1 | 8 | yes | 0.1112s | 0.1266s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k01_s04.py` |  |
| 0.17 | 1/6 | 5 | 0.1090s | 0.0099s | 1 | 8 | yes | 0.1018s | 0.1143s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k01_s05.py` |  |
| 0.17 | 1/6 | 6 | 0.1092s | 0.0017s | 1 | 8 | yes | 0.1083s | 0.1105s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k01_s06.py` |  |
| 0.33 | 2/6 | 1 | 0.1918s | 0.0164s | 1 | 8 | yes | 0.1831s | 0.2032s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k02_s01.py` |  |
| 0.33 | 2/6 | 2 | 0.1825s | 0.0238s | 1 | 8 | yes | 0.1672s | 0.1975s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k02_s02.py` |  |
| 0.33 | 2/6 | 3 | 0.1124s | 0.0060s | 1 | 8 | yes | 0.1085s | 0.1164s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k02_s03.py` |  |
| 0.33 | 2/6 | 4 | 0.1208s | 0.0128s | 1 | 8 | yes | 0.1139s | 0.1301s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k02_s04.py` |  |
| 0.33 | 2/6 | 5 | 0.1183s | 0.0154s | 1 | 8 | yes | 0.1081s | 0.1282s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k02_s05.py` |  |
| 0.33 | 2/6 | 6 | 0.1949s | 0.0158s | 1 | 8 | yes | 0.1864s | 0.2062s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k02_s06.py` |  |
| 0.33 | 2/6 | 7 | 1.2534s | 0.0905s | 1 | 8 | yes | 1.1930s | 1.3105s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k02_s07.py` |  |
| 0.33 | 2/6 | 8 | 1.1996s | 0.0583s | 1 | 8 | yes | 1.1594s | 1.2347s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k02_s08.py` |  |
| 0.33 | 2/6 | 9 | 0.1946s | 0.0081s | 1 | 8 | yes | 0.1895s | 0.1997s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k02_s09.py` |  |
| 0.33 | 2/6 | 10 | 1.2244s | 0.1153s | 1 | 8 | yes | 1.1570s | 1.3046s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k02_s10.py` |  |
| 0.33 | 2/6 | 11 | 0.1197s | 0.0104s | 1 | 8 | yes | 0.1131s | 0.1266s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k02_s11.py` |  |
| 0.33 | 2/6 | 12 | 1.2042s | 0.0738s | 1 | 8 | yes | 1.1600s | 1.2531s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k02_s12.py` |  |
| 0.33 | 2/6 | 13 | 0.1130s | 0.0052s | 1 | 8 | yes | 0.1098s | 0.1164s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k02_s13.py` |  |
| 0.33 | 2/6 | 14 | 1.2488s | 0.0492s | 1 | 8 | yes | 1.2123s | 1.2751s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k02_s14.py` |  |
| 0.33 | 2/6 | 15 | 0.1277s | 0.0119s | 1 | 8 | yes | 0.1200s | 0.1355s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k02_s15.py` |  |
| 0.50 | 3/6 | 1 | 0.2138s | 0.0196s | 1 | 8 | yes | 0.2011s | 0.2263s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s01.py` |  |
| 0.50 | 3/6 | 2 | 1.2681s | 0.1115s | 1 | 8 | yes | 1.2091s | 1.3497s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s02.py` |  |
| 0.50 | 3/6 | 3 | 1.2616s | 0.0799s | 1 | 8 | yes | 1.2244s | 1.3188s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s03.py` |  |
| 0.50 | 3/6 | 4 | 0.1242s | 0.0155s | 2 | 16 | yes | 0.1175s | 0.1320s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s04.py` |  |
| 0.50 | 3/6 | 5 | 1.3512s | 0.0842s | 1 | 8 | yes | 1.3017s | 1.4079s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s05.py` |  |
| 0.50 | 3/6 | 6 | 1.2751s | 0.0620s | 1 | 8 | yes | 1.2356s | 1.3155s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s06.py` |  |
| 0.50 | 3/6 | 7 | 0.1961s | 0.0112s | 1 | 8 | yes | 0.1893s | 0.2038s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s07.py` |  |
| 0.50 | 3/6 | 8 | 1.3095s | 0.1116s | 1 | 8 | yes | 1.2402s | 1.3843s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s08.py` |  |
| 0.50 | 3/6 | 9 | 0.1921s | 0.0248s | 2 | 16 | yes | 0.1809s | 0.2046s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s09.py` |  |
| 0.50 | 3/6 | 10 | 0.1860s | 0.0197s | 1 | 8 | yes | 0.1736s | 0.2000s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s10.py` |  |
| 0.50 | 3/6 | 11 | 1.3471s | 0.1262s | 1 | 8 | yes | 1.2722s | 1.4348s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s11.py` |  |
| 0.50 | 3/6 | 12 | 0.1890s | 0.0057s | 1 | 8 | yes | 0.1854s | 0.1929s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s12.py` |  |
| 0.50 | 3/6 | 13 | 1.2746s | 0.0447s | 1 | 8 | yes | 1.2431s | 1.2991s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s13.py` |  |
| 0.50 | 3/6 | 14 | 1.2585s | 0.0785s | 1 | 8 | yes | 1.2064s | 1.3069s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s14.py` |  |
| 0.50 | 3/6 | 15 | 0.1167s | 0.0139s | 2 | 16 | yes | 0.1109s | 0.1240s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s15.py` |  |
| 0.50 | 3/6 | 16 | 1.2865s | 0.1226s | 1 | 8 | yes | 1.2123s | 1.3722s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s16.py` |  |
| 0.50 | 3/6 | 17 | 0.1222s | 0.0077s | 1 | 8 | yes | 0.1172s | 0.1272s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s17.py` |  |
| 0.50 | 3/6 | 18 | 1.2839s | 0.1032s | 1 | 8 | yes | 1.2303s | 1.3599s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s18.py` |  |
| 0.50 | 3/6 | 19 | 0.1873s | 0.0043s | 1 | 8 | yes | 0.1848s | 0.1902s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s19.py` |  |
| 0.50 | 3/6 | 20 | 0.1074s | 0.0097s | 1 | 8 | yes | 0.1003s | 0.1128s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s20.py` |  |
| 0.67 | 4/6 | 1 | 1.2944s | 0.0395s | 1 | 8 | yes | 1.2709s | 1.3211s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k04_s01.py` |  |
| 0.67 | 4/6 | 2 | 1.2585s | 0.0652s | 1 | 8 | yes | 1.2148s | 1.3014s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k04_s02.py` |  |
| 0.67 | 4/6 | 3 | 0.2059s | 0.0301s | 2 | 16 | yes | 0.1942s | 0.2217s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k04_s03.py` |  |
| 0.67 | 4/6 | 4 | 1.3023s | 0.1034s | 1 | 8 | yes | 1.2379s | 1.3706s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k04_s04.py` |  |
| 0.67 | 4/6 | 5 | 0.1157s | 0.0116s | 1 | 8 | yes | 0.1100s | 0.1241s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k04_s05.py` |  |
| 0.67 | 4/6 | 6 | 0.1958s | 0.0108s | 1 | 8 | yes | 0.1891s | 0.2031s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k04_s06.py` |  |
| 0.67 | 4/6 | 7 | 1.2119s | 0.0622s | 1 | 8 | yes | 1.1691s | 1.2486s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k04_s07.py` |  |
| 0.67 | 4/6 | 8 | 1.2230s | 0.0696s | 1 | 8 | yes | 1.1767s | 1.2667s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k04_s08.py` |  |
| 0.67 | 4/6 | 9 | 1.3309s | 0.0550s | 1 | 8 | yes | 1.3002s | 1.3707s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k04_s09.py` |  |
| 0.67 | 4/6 | 10 | 0.1907s | 0.0081s | 1 | 8 | yes | 0.1855s | 0.1961s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k04_s10.py` |  |
| 0.67 | 4/6 | 11 | 1.3069s | 0.1002s | 1 | 8 | yes | 1.2452s | 1.3745s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k04_s11.py` |  |
| 0.67 | 4/6 | 12 | 1.3009s | 0.0295s | 1 | 8 | yes | 1.2830s | 1.3210s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k04_s12.py` |  |
| 0.67 | 4/6 | 13 | 1.2602s | 0.1034s | 1 | 8 | yes | 1.2088s | 1.3374s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k04_s13.py` |  |
| 0.67 | 4/6 | 14 | 1.2707s | 0.1163s | 1 | 8 | yes | 1.2013s | 1.3514s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k04_s14.py` |  |
| 0.67 | 4/6 | 15 | 0.1977s | 0.0236s | 2 | 16 | yes | 0.1878s | 0.2099s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k04_s15.py` |  |
| 0.83 | 5/6 | 1 | 1.2655s | 0.0580s | 1 | 8 | yes | 1.2245s | 1.2982s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k05_s01.py` |  |
| 0.83 | 5/6 | 2 | 1.2913s | 0.0911s | 1 | 8 | yes | 1.2342s | 1.3505s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k05_s02.py` |  |
| 0.83 | 5/6 | 3 | 0.2018s | 0.0204s | 1 | 8 | yes | 0.1910s | 0.2160s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k05_s03.py` |  |
| 0.83 | 5/6 | 4 | 1.3131s | 0.0759s | 1 | 8 | yes | 1.2727s | 1.3692s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k05_s04.py` |  |
| 0.83 | 5/6 | 5 | 1.3455s | 0.1144s | 1 | 8 | yes | 1.2736s | 1.4207s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k05_s05.py` |  |
| 0.83 | 5/6 | 6 | 1.2889s | 0.0783s | 1 | 8 | yes | 1.2365s | 1.3375s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k05_s06.py` |  |
| 1.00 | 6/6 | 1 | 1.2944s | 0.0768s | 1 | 8 | yes | 1.2412s | 1.3416s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k06_s01.py` |  |

## call_method_slots/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.1228s | 0.1228s | 0.1228s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.1228s | 0.0139s | 1 | 8 | yes | 0.1149s | 0.1326s | `static-python-perf/Benchmark/call_method_slots/untyped/main.py` |  |

## call_simple/advanced

- Detypable targets: `6`
- Total runs: `64`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.0713s | 0.0713s | 0.0713s | 2.0 | yes | ok |
| 0.17 | 1/6 | 6 | 0.0971s | 0.0736s | 0.1594s | 1.0 | yes | ok |
| 0.33 | 2/6 | 15 | 0.1216s | 0.0731s | 0.1829s | 1.1 | yes | ok |
| 0.50 | 3/6 | 20 | 0.1498s | 0.0913s | 0.2162s | 1.2 | yes | ok |
| 0.67 | 4/6 | 15 | 0.1746s | 0.1066s | 0.2334s | 1.1 | yes | ok |
| 0.83 | 5/6 | 6 | 0.2014s | 0.1414s | 0.2290s | 1.2 | yes | ok |
| 1.00 | 6/6 | 1 | 0.2229s | 0.2229s | 0.2229s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.0713s | 0.0100s | 2 | 16 | yes | 0.0671s | 0.0765s | `detyped_files/call_simple/advanced/proportion_sweep/main_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 0.0938s | 0.0126s | 1 | 8 | yes | 0.0870s | 0.1030s | `detyped_files/call_simple/advanced/proportion_sweep/main_k01_s01.py` |  |
| 0.17 | 1/6 | 2 | 0.0736s | 0.0088s | 1 | 8 | yes | 0.0683s | 0.0797s | `detyped_files/call_simple/advanced/proportion_sweep/main_k01_s02.py` |  |
| 0.17 | 1/6 | 3 | 0.1594s | 0.0183s | 1 | 8 | yes | 0.1495s | 0.1727s | `detyped_files/call_simple/advanced/proportion_sweep/main_k01_s03.py` |  |
| 0.17 | 1/6 | 4 | 0.0906s | 0.0052s | 1 | 8 | yes | 0.0877s | 0.0942s | `detyped_files/call_simple/advanced/proportion_sweep/main_k01_s04.py` |  |
| 0.17 | 1/6 | 5 | 0.0915s | 0.0085s | 1 | 8 | yes | 0.0872s | 0.0976s | `detyped_files/call_simple/advanced/proportion_sweep/main_k01_s05.py` |  |
| 0.17 | 1/6 | 6 | 0.0736s | 0.0094s | 1 | 8 | yes | 0.0679s | 0.0801s | `detyped_files/call_simple/advanced/proportion_sweep/main_k01_s06.py` |  |
| 0.33 | 2/6 | 1 | 0.0894s | 0.0074s | 1 | 8 | yes | 0.0858s | 0.0947s | `detyped_files/call_simple/advanced/proportion_sweep/main_k02_s01.py` |  |
| 0.33 | 2/6 | 2 | 0.0924s | 0.0074s | 1 | 8 | yes | 0.0878s | 0.0972s | `detyped_files/call_simple/advanced/proportion_sweep/main_k02_s02.py` |  |
| 0.33 | 2/6 | 3 | 0.1113s | 0.0095s | 1 | 8 | yes | 0.1050s | 0.1174s | `detyped_files/call_simple/advanced/proportion_sweep/main_k02_s03.py` |  |
| 0.33 | 2/6 | 4 | 0.0944s | 0.0141s | 1 | 8 | yes | 0.0854s | 0.1031s | `detyped_files/call_simple/advanced/proportion_sweep/main_k02_s04.py` |  |
| 0.33 | 2/6 | 5 | 0.0902s | 0.0100s | 1 | 8 | yes | 0.0830s | 0.0959s | `detyped_files/call_simple/advanced/proportion_sweep/main_k02_s05.py` |  |
| 0.33 | 2/6 | 6 | 0.1114s | 0.0130s | 2 | 16 | yes | 0.1052s | 0.1174s | `detyped_files/call_simple/advanced/proportion_sweep/main_k02_s06.py` |  |
| 0.33 | 2/6 | 7 | 0.1801s | 0.0214s | 1 | 8 | yes | 0.1664s | 0.1940s | `detyped_files/call_simple/advanced/proportion_sweep/main_k02_s07.py` |  |
| 0.33 | 2/6 | 8 | 0.1572s | 0.0035s | 1 | 8 | yes | 0.1550s | 0.1596s | `detyped_files/call_simple/advanced/proportion_sweep/main_k02_s08.py` |  |
| 0.33 | 2/6 | 9 | 0.1581s | 0.0041s | 1 | 8 | yes | 0.1559s | 0.1611s | `detyped_files/call_simple/advanced/proportion_sweep/main_k02_s09.py` |  |
| 0.33 | 2/6 | 10 | 0.1162s | 0.0083s | 1 | 8 | yes | 0.1114s | 0.1219s | `detyped_files/call_simple/advanced/proportion_sweep/main_k02_s10.py` |  |
| 0.33 | 2/6 | 11 | 0.1758s | 0.0120s | 1 | 8 | yes | 0.1679s | 0.1831s | `detyped_files/call_simple/advanced/proportion_sweep/main_k02_s11.py` |  |
| 0.33 | 2/6 | 12 | 0.0910s | 0.0115s | 2 | 16 | yes | 0.0860s | 0.0968s | `detyped_files/call_simple/advanced/proportion_sweep/main_k02_s12.py` |  |
| 0.33 | 2/6 | 13 | 0.1829s | 0.0120s | 1 | 8 | yes | 0.1767s | 0.1917s | `detyped_files/call_simple/advanced/proportion_sweep/main_k02_s13.py` |  |
| 0.33 | 2/6 | 14 | 0.0731s | 0.0089s | 1 | 8 | yes | 0.0679s | 0.0793s | `detyped_files/call_simple/advanced/proportion_sweep/main_k02_s14.py` |  |
| 0.33 | 2/6 | 15 | 0.0999s | 0.0131s | 1 | 8 | yes | 0.0921s | 0.1089s | `detyped_files/call_simple/advanced/proportion_sweep/main_k02_s15.py` |  |
| 0.50 | 3/6 | 1 | 0.1276s | 0.0204s | 2 | 16 | yes | 0.1185s | 0.1377s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s01.py` |  |
| 0.50 | 3/6 | 2 | 0.1754s | 0.0085s | 1 | 8 | yes | 0.1692s | 0.1799s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s02.py` |  |
| 0.50 | 3/6 | 3 | 0.2162s | 0.0301s | 2 | 16 | yes | 0.2030s | 0.2315s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s03.py` |  |
| 0.50 | 3/6 | 4 | 0.0939s | 0.0105s | 1 | 8 | yes | 0.0876s | 0.1009s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s04.py` |  |
| 0.50 | 3/6 | 5 | 0.1141s | 0.0060s | 1 | 8 | yes | 0.1104s | 0.1181s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s05.py` |  |
| 0.50 | 3/6 | 6 | 0.1305s | 0.0024s | 1 | 8 | yes | 0.1292s | 0.1322s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s06.py` |  |
| 0.50 | 3/6 | 7 | 0.1829s | 0.0208s | 1 | 8 | yes | 0.1697s | 0.1968s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s07.py` |  |
| 0.50 | 3/6 | 8 | 0.1928s | 0.0148s | 1 | 8 | yes | 0.1836s | 0.2025s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s08.py` |  |
| 0.50 | 3/6 | 9 | 0.1882s | 0.0242s | 2 | 16 | yes | 0.1779s | 0.2003s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s09.py` |  |
| 0.50 | 3/6 | 10 | 0.1084s | 0.0053s | 1 | 8 | yes | 0.1049s | 0.1116s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s10.py` |  |
| 0.50 | 3/6 | 11 | 0.2005s | 0.0129s | 1 | 8 | yes | 0.1910s | 0.2075s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s11.py` |  |
| 0.50 | 3/6 | 12 | 0.0994s | 0.0140s | 1 | 8 | yes | 0.0908s | 0.1089s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s12.py` |  |
| 0.50 | 3/6 | 13 | 0.1973s | 0.0230s | 1 | 8 | yes | 0.1828s | 0.2126s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s13.py` |  |
| 0.50 | 3/6 | 14 | 0.1720s | 0.0132s | 1 | 8 | yes | 0.1624s | 0.1788s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s14.py` |  |
| 0.50 | 3/6 | 15 | 0.1933s | 0.0054s | 1 | 8 | yes | 0.1896s | 0.1965s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s15.py` |  |
| 0.50 | 3/6 | 16 | 0.0913s | 0.0113s | 1 | 8 | yes | 0.0858s | 0.0993s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s16.py` |  |
| 0.50 | 3/6 | 17 | 0.1145s | 0.0177s | 2 | 16 | yes | 0.1077s | 0.1239s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s17.py` |  |
| 0.50 | 3/6 | 18 | 0.1649s | 0.0242s | 2 | 16 | yes | 0.1541s | 0.1771s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s18.py` |  |
| 0.50 | 3/6 | 19 | 0.1182s | 0.0146s | 1 | 8 | yes | 0.1099s | 0.1285s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s19.py` |  |
| 0.50 | 3/6 | 20 | 0.1141s | 0.0091s | 1 | 8 | yes | 0.1085s | 0.1205s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s20.py` |  |
| 0.67 | 4/6 | 1 | 0.2043s | 0.0094s | 1 | 8 | yes | 0.1991s | 0.2112s | `detyped_files/call_simple/advanced/proportion_sweep/main_k04_s01.py` |  |
| 0.67 | 4/6 | 2 | 0.2017s | 0.0134s | 1 | 8 | yes | 0.1941s | 0.2113s | `detyped_files/call_simple/advanced/proportion_sweep/main_k04_s02.py` |  |
| 0.67 | 4/6 | 3 | 0.2125s | 0.0180s | 1 | 8 | yes | 0.2020s | 0.2251s | `detyped_files/call_simple/advanced/proportion_sweep/main_k04_s03.py` |  |
| 0.67 | 4/6 | 4 | 0.2085s | 0.0160s | 1 | 8 | yes | 0.1988s | 0.2191s | `detyped_files/call_simple/advanced/proportion_sweep/main_k04_s04.py` |  |
| 0.67 | 4/6 | 5 | 0.1138s | 0.0061s | 1 | 8 | yes | 0.1104s | 0.1182s | `detyped_files/call_simple/advanced/proportion_sweep/main_k04_s05.py` |  |
| 0.67 | 4/6 | 6 | 0.1125s | 0.0106s | 1 | 8 | yes | 0.1064s | 0.1199s | `detyped_files/call_simple/advanced/proportion_sweep/main_k04_s06.py` |  |
| 0.67 | 4/6 | 7 | 0.1892s | 0.0237s | 2 | 16 | yes | 0.1791s | 0.2016s | `detyped_files/call_simple/advanced/proportion_sweep/main_k04_s07.py` |  |
| 0.67 | 4/6 | 8 | 0.1312s | 0.0105s | 1 | 8 | yes | 0.1250s | 0.1389s | `detyped_files/call_simple/advanced/proportion_sweep/main_k04_s08.py` |  |
| 0.67 | 4/6 | 9 | 0.2334s | 0.0173s | 1 | 8 | yes | 0.2230s | 0.2452s | `detyped_files/call_simple/advanced/proportion_sweep/main_k04_s09.py` |  |
| 0.67 | 4/6 | 10 | 0.1066s | 0.0043s | 1 | 8 | yes | 0.1041s | 0.1098s | `detyped_files/call_simple/advanced/proportion_sweep/main_k04_s10.py` |  |
| 0.67 | 4/6 | 11 | 0.1992s | 0.0042s | 1 | 8 | yes | 0.1967s | 0.2022s | `detyped_files/call_simple/advanced/proportion_sweep/main_k04_s11.py` |  |
| 0.67 | 4/6 | 12 | 0.1914s | 0.0193s | 1 | 8 | yes | 0.1799s | 0.2045s | `detyped_files/call_simple/advanced/proportion_sweep/main_k04_s12.py` |  |
| 0.67 | 4/6 | 13 | 0.1794s | 0.0079s | 1 | 8 | yes | 0.1744s | 0.1846s | `detyped_files/call_simple/advanced/proportion_sweep/main_k04_s13.py` |  |
| 0.67 | 4/6 | 14 | 0.2016s | 0.0166s | 1 | 8 | yes | 0.1905s | 0.2119s | `detyped_files/call_simple/advanced/proportion_sweep/main_k04_s14.py` |  |
| 0.67 | 4/6 | 15 | 0.1343s | 0.0131s | 1 | 8 | yes | 0.1274s | 0.1439s | `detyped_files/call_simple/advanced/proportion_sweep/main_k04_s15.py` |  |
| 0.83 | 5/6 | 1 | 0.1414s | 0.0176s | 1 | 8 | yes | 0.1320s | 0.1539s | `detyped_files/call_simple/advanced/proportion_sweep/main_k05_s01.py` |  |
| 0.83 | 5/6 | 2 | 0.2290s | 0.0309s | 2 | 16 | yes | 0.2152s | 0.2448s | `detyped_files/call_simple/advanced/proportion_sweep/main_k05_s02.py` |  |
| 0.83 | 5/6 | 3 | 0.2034s | 0.0231s | 1 | 8 | yes | 0.1885s | 0.2175s | `detyped_files/call_simple/advanced/proportion_sweep/main_k05_s03.py` |  |
| 0.83 | 5/6 | 4 | 0.1993s | 0.0209s | 1 | 8 | yes | 0.1858s | 0.2130s | `detyped_files/call_simple/advanced/proportion_sweep/main_k05_s04.py` |  |
| 0.83 | 5/6 | 5 | 0.2231s | 0.0110s | 1 | 8 | yes | 0.2162s | 0.2302s | `detyped_files/call_simple/advanced/proportion_sweep/main_k05_s05.py` |  |
| 0.83 | 5/6 | 6 | 0.2122s | 0.0276s | 1 | 8 | yes | 0.1992s | 0.2323s | `detyped_files/call_simple/advanced/proportion_sweep/main_k05_s06.py` |  |
| 1.00 | 6/6 | 1 | 0.2229s | 0.0139s | 1 | 8 | yes | 0.2163s | 0.2330s | `detyped_files/call_simple/advanced/proportion_sweep/main_k06_s01.py` |  |

## call_simple/shallow

- Detypable targets: `6`
- Total runs: `64`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.0745s | 0.0745s | 0.0745s | 1.0 | yes | ok |
| 0.17 | 1/6 | 6 | 0.0712s | 0.0673s | 0.0772s | 1.2 | yes | ok |
| 0.33 | 2/6 | 15 | 0.0716s | 0.0666s | 0.0762s | 1.6 | yes | ok |
| 0.50 | 3/6 | 20 | 0.0711s | 0.0665s | 0.0818s | 1.4 | yes | ok |
| 0.67 | 4/6 | 15 | 0.0712s | 0.0672s | 0.0779s | 1.7 | yes | ok |
| 0.83 | 5/6 | 6 | 0.0712s | 0.0689s | 0.0743s | 1.3 | yes | ok |
| 1.00 | 6/6 | 1 | 0.0735s | 0.0735s | 0.0735s | 3.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.0745s | 0.0067s | 1 | 8 | yes | 0.0703s | 0.0788s | `detyped_files/call_simple/shallow/proportion_sweep/main_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 0.0772s | 0.0104s | 1 | 8 | yes | 0.0706s | 0.0842s | `detyped_files/call_simple/shallow/proportion_sweep/main_k01_s01.py` |  |
| 0.17 | 1/6 | 2 | 0.0739s | 0.0101s | 1 | 8 | yes | 0.0681s | 0.0809s | `detyped_files/call_simple/shallow/proportion_sweep/main_k01_s02.py` |  |
| 0.17 | 1/6 | 3 | 0.0691s | 0.0043s | 1 | 8 | yes | 0.0667s | 0.0722s | `detyped_files/call_simple/shallow/proportion_sweep/main_k01_s03.py` |  |
| 0.17 | 1/6 | 4 | 0.0709s | 0.0093s | 2 | 16 | yes | 0.0675s | 0.0759s | `detyped_files/call_simple/shallow/proportion_sweep/main_k01_s04.py` |  |
| 0.17 | 1/6 | 5 | 0.0685s | 0.0077s | 1 | 8 | yes | 0.0644s | 0.0742s | `detyped_files/call_simple/shallow/proportion_sweep/main_k01_s05.py` |  |
| 0.17 | 1/6 | 6 | 0.0673s | 0.0021s | 1 | 8 | yes | 0.0661s | 0.0687s | `detyped_files/call_simple/shallow/proportion_sweep/main_k01_s06.py` |  |
| 0.33 | 2/6 | 1 | 0.0762s | 0.0160s | 3 | 24 | yes | 0.0707s | 0.0830s | `detyped_files/call_simple/shallow/proportion_sweep/main_k02_s01.py` |  |
| 0.33 | 2/6 | 2 | 0.0724s | 0.0081s | 1 | 8 | yes | 0.0676s | 0.0779s | `detyped_files/call_simple/shallow/proportion_sweep/main_k02_s02.py` |  |
| 0.33 | 2/6 | 3 | 0.0666s | 0.0019s | 1 | 8 | yes | 0.0656s | 0.0680s | `detyped_files/call_simple/shallow/proportion_sweep/main_k02_s03.py` |  |
| 0.33 | 2/6 | 4 | 0.0752s | 0.0130s | 2 | 16 | yes | 0.0694s | 0.0818s | `detyped_files/call_simple/shallow/proportion_sweep/main_k02_s04.py` |  |
| 0.33 | 2/6 | 5 | 0.0736s | 0.0099s | 1 | 8 | yes | 0.0680s | 0.0805s | `detyped_files/call_simple/shallow/proportion_sweep/main_k02_s05.py` |  |
| 0.33 | 2/6 | 6 | 0.0666s | 0.0054s | 1 | 8 | yes | 0.0633s | 0.0702s | `detyped_files/call_simple/shallow/proportion_sweep/main_k02_s06.py` |  |
| 0.33 | 2/6 | 7 | 0.0706s | 0.0107s | 2 | 16 | yes | 0.0658s | 0.0758s | `detyped_files/call_simple/shallow/proportion_sweep/main_k02_s07.py` |  |
| 0.33 | 2/6 | 8 | 0.0701s | 0.0078s | 1 | 8 | yes | 0.0665s | 0.0757s | `detyped_files/call_simple/shallow/proportion_sweep/main_k02_s08.py` |  |
| 0.33 | 2/6 | 9 | 0.0724s | 0.0121s | 2 | 16 | yes | 0.0675s | 0.0791s | `detyped_files/call_simple/shallow/proportion_sweep/main_k02_s09.py` |  |
| 0.33 | 2/6 | 10 | 0.0692s | 0.0062s | 1 | 8 | yes | 0.0660s | 0.0736s | `detyped_files/call_simple/shallow/proportion_sweep/main_k02_s10.py` |  |
| 0.33 | 2/6 | 11 | 0.0730s | 0.0095s | 2 | 16 | yes | 0.0690s | 0.0779s | `detyped_files/call_simple/shallow/proportion_sweep/main_k02_s11.py` |  |
| 0.33 | 2/6 | 12 | 0.0713s | 0.0117s | 2 | 16 | yes | 0.0663s | 0.0772s | `detyped_files/call_simple/shallow/proportion_sweep/main_k02_s12.py` |  |
| 0.33 | 2/6 | 13 | 0.0721s | 0.0064s | 1 | 8 | yes | 0.0684s | 0.0765s | `detyped_files/call_simple/shallow/proportion_sweep/main_k02_s13.py` |  |
| 0.33 | 2/6 | 14 | 0.0726s | 0.0133s | 2 | 16 | yes | 0.0668s | 0.0793s | `detyped_files/call_simple/shallow/proportion_sweep/main_k02_s14.py` |  |
| 0.33 | 2/6 | 15 | 0.0719s | 0.0114s | 2 | 16 | yes | 0.0677s | 0.0783s | `detyped_files/call_simple/shallow/proportion_sweep/main_k02_s15.py` |  |
| 0.50 | 3/6 | 1 | 0.0720s | 0.0079s | 1 | 8 | yes | 0.0671s | 0.0774s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s01.py` |  |
| 0.50 | 3/6 | 2 | 0.0721s | 0.0112s | 2 | 16 | yes | 0.0680s | 0.0781s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s02.py` |  |
| 0.50 | 3/6 | 3 | 0.0693s | 0.0060s | 1 | 8 | yes | 0.0662s | 0.0736s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s03.py` |  |
| 0.50 | 3/6 | 4 | 0.0665s | 0.0037s | 1 | 8 | yes | 0.0640s | 0.0688s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s04.py` |  |
| 0.50 | 3/6 | 5 | 0.0728s | 0.0132s | 3 | 24 | yes | 0.0684s | 0.0788s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s05.py` |  |
| 0.50 | 3/6 | 6 | 0.0714s | 0.0122s | 2 | 16 | yes | 0.0673s | 0.0781s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s06.py` |  |
| 0.50 | 3/6 | 7 | 0.0696s | 0.0075s | 1 | 8 | yes | 0.0662s | 0.0751s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s07.py` |  |
| 0.50 | 3/6 | 8 | 0.0692s | 0.0058s | 1 | 8 | yes | 0.0664s | 0.0734s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s08.py` |  |
| 0.50 | 3/6 | 9 | 0.0713s | 0.0062s | 1 | 8 | yes | 0.0675s | 0.0755s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s09.py` |  |
| 0.50 | 3/6 | 10 | 0.0731s | 0.0109s | 2 | 16 | yes | 0.0685s | 0.0788s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s10.py` |  |
| 0.50 | 3/6 | 11 | 0.0694s | 0.0092s | 2 | 16 | yes | 0.0657s | 0.0742s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s11.py` |  |
| 0.50 | 3/6 | 12 | 0.0696s | 0.0036s | 1 | 8 | yes | 0.0673s | 0.0719s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s12.py` |  |
| 0.50 | 3/6 | 13 | 0.0718s | 0.0078s | 1 | 8 | yes | 0.0672s | 0.0773s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s13.py` |  |
| 0.50 | 3/6 | 14 | 0.0727s | 0.0107s | 1 | 8 | yes | 0.0666s | 0.0799s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s14.py` |  |
| 0.50 | 3/6 | 15 | 0.0735s | 0.0166s | 4 | 32 | yes | 0.0684s | 0.0797s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s15.py` |  |
| 0.50 | 3/6 | 16 | 0.0707s | 0.0064s | 1 | 8 | yes | 0.0668s | 0.0752s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s16.py` |  |
| 0.50 | 3/6 | 17 | 0.0678s | 0.0042s | 1 | 8 | yes | 0.0656s | 0.0707s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s17.py` |  |
| 0.50 | 3/6 | 18 | 0.0692s | 0.0051s | 1 | 8 | yes | 0.0662s | 0.0727s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s18.py` |  |
| 0.50 | 3/6 | 19 | 0.0818s | 0.0114s | 1 | 8 | yes | 0.0744s | 0.0889s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s19.py` |  |
| 0.50 | 3/6 | 20 | 0.0691s | 0.0041s | 1 | 8 | yes | 0.0666s | 0.0719s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s20.py` |  |
| 0.67 | 4/6 | 1 | 0.0676s | 0.0029s | 1 | 8 | yes | 0.0660s | 0.0696s | `detyped_files/call_simple/shallow/proportion_sweep/main_k04_s01.py` |  |
| 0.67 | 4/6 | 2 | 0.0712s | 0.0076s | 1 | 8 | yes | 0.0670s | 0.0766s | `detyped_files/call_simple/shallow/proportion_sweep/main_k04_s02.py` |  |
| 0.67 | 4/6 | 3 | 0.0745s | 0.0099s | 1 | 8 | yes | 0.0684s | 0.0811s | `detyped_files/call_simple/shallow/proportion_sweep/main_k04_s03.py` |  |
| 0.67 | 4/6 | 4 | 0.0779s | 0.0131s | 2 | 16 | yes | 0.0725s | 0.0849s | `detyped_files/call_simple/shallow/proportion_sweep/main_k04_s04.py` |  |
| 0.67 | 4/6 | 5 | 0.0729s | 0.0131s | 3 | 24 | yes | 0.0682s | 0.0785s | `detyped_files/call_simple/shallow/proportion_sweep/main_k04_s05.py` |  |
| 0.67 | 4/6 | 6 | 0.0696s | 0.0100s | 2 | 16 | yes | 0.0653s | 0.0750s | `detyped_files/call_simple/shallow/proportion_sweep/main_k04_s06.py` |  |
| 0.67 | 4/6 | 7 | 0.0712s | 0.0076s | 1 | 8 | yes | 0.0668s | 0.0764s | `detyped_files/call_simple/shallow/proportion_sweep/main_k04_s07.py` |  |
| 0.67 | 4/6 | 8 | 0.0737s | 0.0137s | 3 | 24 | yes | 0.0689s | 0.0797s | `detyped_files/call_simple/shallow/proportion_sweep/main_k04_s08.py` |  |
| 0.67 | 4/6 | 9 | 0.0692s | 0.0081s | 2 | 16 | yes | 0.0665s | 0.0735s | `detyped_files/call_simple/shallow/proportion_sweep/main_k04_s09.py` |  |
| 0.67 | 4/6 | 10 | 0.0672s | 0.0067s | 1 | 8 | yes | 0.0628s | 0.0713s | `detyped_files/call_simple/shallow/proportion_sweep/main_k04_s10.py` |  |
| 0.67 | 4/6 | 11 | 0.0715s | 0.0073s | 1 | 8 | yes | 0.0672s | 0.0766s | `detyped_files/call_simple/shallow/proportion_sweep/main_k04_s11.py` |  |
| 0.67 | 4/6 | 12 | 0.0691s | 0.0089s | 2 | 16 | yes | 0.0654s | 0.0737s | `detyped_files/call_simple/shallow/proportion_sweep/main_k04_s12.py` |  |
| 0.67 | 4/6 | 13 | 0.0730s | 0.0113s | 2 | 16 | yes | 0.0680s | 0.0787s | `detyped_files/call_simple/shallow/proportion_sweep/main_k04_s13.py` |  |
| 0.67 | 4/6 | 14 | 0.0712s | 0.0100s | 2 | 16 | yes | 0.0667s | 0.0762s | `detyped_files/call_simple/shallow/proportion_sweep/main_k04_s14.py` |  |
| 0.67 | 4/6 | 15 | 0.0681s | 0.0090s | 2 | 16 | yes | 0.0644s | 0.0728s | `detyped_files/call_simple/shallow/proportion_sweep/main_k04_s15.py` |  |
| 0.83 | 5/6 | 1 | 0.0697s | 0.0111s | 2 | 16 | yes | 0.0648s | 0.0751s | `detyped_files/call_simple/shallow/proportion_sweep/main_k05_s01.py` |  |
| 0.83 | 5/6 | 2 | 0.0697s | 0.0097s | 1 | 8 | yes | 0.0637s | 0.0763s | `detyped_files/call_simple/shallow/proportion_sweep/main_k05_s02.py` |  |
| 0.83 | 5/6 | 3 | 0.0719s | 0.0115s | 2 | 16 | yes | 0.0670s | 0.0777s | `detyped_files/call_simple/shallow/proportion_sweep/main_k05_s03.py` |  |
| 0.83 | 5/6 | 4 | 0.0689s | 0.0044s | 1 | 8 | yes | 0.0661s | 0.0717s | `detyped_files/call_simple/shallow/proportion_sweep/main_k05_s04.py` |  |
| 0.83 | 5/6 | 5 | 0.0729s | 0.0081s | 1 | 8 | yes | 0.0681s | 0.0785s | `detyped_files/call_simple/shallow/proportion_sweep/main_k05_s05.py` |  |
| 0.83 | 5/6 | 6 | 0.0743s | 0.0069s | 1 | 8 | yes | 0.0700s | 0.0789s | `detyped_files/call_simple/shallow/proportion_sweep/main_k05_s06.py` |  |
| 1.00 | 6/6 | 1 | 0.0735s | 0.0143s | 3 | 24 | yes | 0.0688s | 0.0797s | `detyped_files/call_simple/shallow/proportion_sweep/main_k06_s01.py` |  |

## call_simple/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.0824s | 0.0824s | 0.0824s | 4.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.0824s | 0.0193s | 4 | 32 | yes | 0.0761s | 0.0894s | `static-python-perf/Benchmark/call_simple/untyped/main.py` |  |

## chaos/advanced

- Detypable targets: `5`
- Total runs: `32`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/5 | 1 | 0.3312s | 0.3312s | 0.3312s | 1.0 | yes | ok |
| 0.20 | 1/5 | 5 | 0.3570s | 0.3249s | 0.4349s | 1.0 | yes | ok |
| 0.40 | 2/5 | 10 | 0.3741s | 0.3177s | 0.4786s | 1.0 | yes | ok |
| 0.60 | 3/5 | 10 | 0.3944s | 0.3227s | 0.4654s | 1.0 | yes | ok |
| 0.80 | 4/5 | 5 | 0.4259s | 0.3527s | 0.4552s | 1.0 | yes | ok |
| 1.00 | 5/5 | 1 | 0.4508s | 0.4508s | 0.4508s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/5 | 1 | 0.3312s | 0.0171s | 1 | 8 | yes | 0.3215s | 0.3432s | `detyped_files/chaos/advanced/proportion_sweep/main_k00_s01.py` |  |
| 0.20 | 1/5 | 1 | 0.3460s | 0.0182s | 1 | 8 | yes | 0.3352s | 0.3584s | `detyped_files/chaos/advanced/proportion_sweep/main_k01_s01.py` |  |
| 0.20 | 1/5 | 2 | 0.4349s | 0.0396s | 1 | 8 | yes | 0.4060s | 0.4535s | `detyped_files/chaos/advanced/proportion_sweep/main_k01_s02.py` |  |
| 0.20 | 1/5 | 3 | 0.3277s | 0.0256s | 1 | 8 | yes | 0.3167s | 0.3464s | `detyped_files/chaos/advanced/proportion_sweep/main_k01_s03.py` |  |
| 0.20 | 1/5 | 4 | 0.3514s | 0.0345s | 1 | 8 | yes | 0.3315s | 0.3755s | `detyped_files/chaos/advanced/proportion_sweep/main_k01_s04.py` |  |
| 0.20 | 1/5 | 5 | 0.3249s | 0.0129s | 1 | 8 | yes | 0.3162s | 0.3327s | `detyped_files/chaos/advanced/proportion_sweep/main_k01_s05.py` |  |
| 0.40 | 2/5 | 1 | 0.3177s | 0.0287s | 1 | 8 | yes | 0.2985s | 0.3362s | `detyped_files/chaos/advanced/proportion_sweep/main_k02_s01.py` |  |
| 0.40 | 2/5 | 2 | 0.4402s | 0.0166s | 1 | 8 | yes | 0.4306s | 0.4517s | `detyped_files/chaos/advanced/proportion_sweep/main_k02_s02.py` |  |
| 0.40 | 2/5 | 3 | 0.3210s | 0.0203s | 1 | 8 | yes | 0.3060s | 0.3323s | `detyped_files/chaos/advanced/proportion_sweep/main_k02_s03.py` |  |
| 0.40 | 2/5 | 4 | 0.4383s | 0.0233s | 1 | 8 | yes | 0.4227s | 0.4530s | `detyped_files/chaos/advanced/proportion_sweep/main_k02_s04.py` |  |
| 0.40 | 2/5 | 5 | 0.4786s | 0.0570s | 1 | 8 | yes | 0.4467s | 0.5195s | `detyped_files/chaos/advanced/proportion_sweep/main_k02_s05.py` |  |
| 0.40 | 2/5 | 6 | 0.3234s | 0.0424s | 1 | 8 | yes | 0.2948s | 0.3498s | `detyped_files/chaos/advanced/proportion_sweep/main_k02_s06.py` |  |
| 0.40 | 2/5 | 7 | 0.3470s | 0.0287s | 1 | 8 | yes | 0.3271s | 0.3636s | `detyped_files/chaos/advanced/proportion_sweep/main_k02_s07.py` |  |
| 0.40 | 2/5 | 8 | 0.3239s | 0.0276s | 1 | 8 | yes | 0.3059s | 0.3413s | `detyped_files/chaos/advanced/proportion_sweep/main_k02_s08.py` |  |
| 0.40 | 2/5 | 9 | 0.3291s | 0.0311s | 1 | 8 | yes | 0.3078s | 0.3470s | `detyped_files/chaos/advanced/proportion_sweep/main_k02_s09.py` |  |
| 0.40 | 2/5 | 10 | 0.4215s | 0.0391s | 1 | 8 | yes | 0.3946s | 0.4458s | `detyped_files/chaos/advanced/proportion_sweep/main_k02_s10.py` |  |
| 0.60 | 3/5 | 1 | 0.4281s | 0.0429s | 1 | 8 | yes | 0.3980s | 0.4528s | `detyped_files/chaos/advanced/proportion_sweep/main_k03_s01.py` |  |
| 0.60 | 3/5 | 2 | 0.4654s | 0.0334s | 1 | 8 | yes | 0.4497s | 0.4896s | `detyped_files/chaos/advanced/proportion_sweep/main_k03_s02.py` |  |
| 0.60 | 3/5 | 3 | 0.3278s | 0.0290s | 1 | 8 | yes | 0.3075s | 0.3451s | `detyped_files/chaos/advanced/proportion_sweep/main_k03_s03.py` |  |
| 0.60 | 3/5 | 4 | 0.3228s | 0.0241s | 1 | 8 | yes | 0.3068s | 0.3380s | `detyped_files/chaos/advanced/proportion_sweep/main_k03_s04.py` |  |
| 0.60 | 3/5 | 5 | 0.4187s | 0.0381s | 1 | 8 | yes | 0.3925s | 0.4418s | `detyped_files/chaos/advanced/proportion_sweep/main_k03_s05.py` |  |
| 0.60 | 3/5 | 6 | 0.4440s | 0.0539s | 1 | 8 | yes | 0.4072s | 0.4764s | `detyped_files/chaos/advanced/proportion_sweep/main_k03_s06.py` |  |
| 0.60 | 3/5 | 7 | 0.4351s | 0.0378s | 1 | 8 | yes | 0.4089s | 0.4567s | `detyped_files/chaos/advanced/proportion_sweep/main_k03_s07.py` |  |
| 0.60 | 3/5 | 8 | 0.3305s | 0.0229s | 1 | 8 | yes | 0.3139s | 0.3433s | `detyped_files/chaos/advanced/proportion_sweep/main_k03_s08.py` |  |
| 0.60 | 3/5 | 9 | 0.4490s | 0.0471s | 1 | 8 | yes | 0.4158s | 0.4794s | `detyped_files/chaos/advanced/proportion_sweep/main_k03_s09.py` |  |
| 0.60 | 3/5 | 10 | 0.3227s | 0.0289s | 1 | 8 | yes | 0.3039s | 0.3408s | `detyped_files/chaos/advanced/proportion_sweep/main_k03_s10.py` |  |
| 0.80 | 4/5 | 1 | 0.4263s | 0.0390s | 1 | 8 | yes | 0.4000s | 0.4499s | `detyped_files/chaos/advanced/proportion_sweep/main_k04_s01.py` |  |
| 0.80 | 4/5 | 2 | 0.3527s | 0.0315s | 1 | 8 | yes | 0.3350s | 0.3751s | `detyped_files/chaos/advanced/proportion_sweep/main_k04_s02.py` |  |
| 0.80 | 4/5 | 3 | 0.4552s | 0.0146s | 1 | 8 | yes | 0.4465s | 0.4651s | `detyped_files/chaos/advanced/proportion_sweep/main_k04_s03.py` |  |
| 0.80 | 4/5 | 4 | 0.4518s | 0.0050s | 1 | 8 | yes | 0.4484s | 0.4548s | `detyped_files/chaos/advanced/proportion_sweep/main_k04_s04.py` |  |
| 0.80 | 4/5 | 5 | 0.4436s | 0.0493s | 1 | 8 | yes | 0.4104s | 0.4733s | `detyped_files/chaos/advanced/proportion_sweep/main_k04_s05.py` |  |
| 1.00 | 5/5 | 1 | 0.4508s | 0.0656s | 1 | 8 | yes | 0.4084s | 0.4929s | `detyped_files/chaos/advanced/proportion_sweep/main_k05_s01.py` |  |

## chaos/shallow

- Detypable targets: `5`
- Total runs: `32`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/5 | 1 | 0.3166s | 0.3166s | 0.3166s | 1.0 | yes | ok |
| 0.20 | 1/5 | 5 | 0.3579s | 0.3175s | 0.4426s | 1.0 | yes | ok |
| 0.40 | 2/5 | 10 | 0.3936s | 0.3143s | 0.4786s | 1.0 | yes | ok |
| 0.60 | 3/5 | 10 | 0.4303s | 0.3437s | 0.5182s | 1.0 | yes | ok |
| 0.80 | 4/5 | 5 | 0.4628s | 0.3882s | 0.4967s | 1.0 | yes | ok |
| 1.00 | 5/5 | 1 | 0.5012s | 0.5012s | 0.5012s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/5 | 1 | 0.3166s | 0.0181s | 1 | 8 | yes | 0.3045s | 0.3277s | `detyped_files/chaos/shallow/proportion_sweep/main_k00_s01.py` |  |
| 0.20 | 1/5 | 1 | 0.3175s | 0.0269s | 1 | 8 | yes | 0.2977s | 0.3326s | `detyped_files/chaos/shallow/proportion_sweep/main_k01_s01.py` |  |
| 0.20 | 1/5 | 2 | 0.3255s | 0.0129s | 1 | 8 | yes | 0.3176s | 0.3343s | `detyped_files/chaos/shallow/proportion_sweep/main_k01_s02.py` |  |
| 0.20 | 1/5 | 3 | 0.4426s | 0.0170s | 1 | 8 | yes | 0.4329s | 0.4548s | `detyped_files/chaos/shallow/proportion_sweep/main_k01_s03.py` |  |
| 0.20 | 1/5 | 4 | 0.3844s | 0.0182s | 1 | 8 | yes | 0.3745s | 0.3974s | `detyped_files/chaos/shallow/proportion_sweep/main_k01_s04.py` |  |
| 0.20 | 1/5 | 5 | 0.3197s | 0.0256s | 1 | 8 | yes | 0.3017s | 0.3348s | `detyped_files/chaos/shallow/proportion_sweep/main_k01_s05.py` |  |
| 0.40 | 2/5 | 1 | 0.4167s | 0.0430s | 1 | 8 | yes | 0.3878s | 0.4425s | `detyped_files/chaos/shallow/proportion_sweep/main_k02_s01.py` |  |
| 0.40 | 2/5 | 2 | 0.3814s | 0.0234s | 1 | 8 | yes | 0.3661s | 0.3966s | `detyped_files/chaos/shallow/proportion_sweep/main_k02_s02.py` |  |
| 0.40 | 2/5 | 3 | 0.4664s | 0.0273s | 1 | 8 | yes | 0.4504s | 0.4855s | `detyped_files/chaos/shallow/proportion_sweep/main_k02_s03.py` |  |
| 0.40 | 2/5 | 4 | 0.3737s | 0.0386s | 1 | 8 | yes | 0.3480s | 0.3983s | `detyped_files/chaos/shallow/proportion_sweep/main_k02_s04.py` |  |
| 0.40 | 2/5 | 5 | 0.3143s | 0.0255s | 1 | 8 | yes | 0.2967s | 0.3295s | `detyped_files/chaos/shallow/proportion_sweep/main_k02_s05.py` |  |
| 0.40 | 2/5 | 6 | 0.4451s | 0.0317s | 1 | 8 | yes | 0.4233s | 0.4639s | `detyped_files/chaos/shallow/proportion_sweep/main_k02_s06.py` |  |
| 0.40 | 2/5 | 7 | 0.4786s | 0.0523s | 1 | 8 | yes | 0.4453s | 0.5108s | `detyped_files/chaos/shallow/proportion_sweep/main_k02_s07.py` |  |
| 0.40 | 2/5 | 8 | 0.3266s | 0.0273s | 1 | 8 | yes | 0.3068s | 0.3405s | `detyped_files/chaos/shallow/proportion_sweep/main_k02_s08.py` |  |
| 0.40 | 2/5 | 9 | 0.3430s | 0.0340s | 1 | 8 | yes | 0.3179s | 0.3615s | `detyped_files/chaos/shallow/proportion_sweep/main_k02_s09.py` |  |
| 0.40 | 2/5 | 10 | 0.3904s | 0.0348s | 1 | 8 | yes | 0.3662s | 0.4110s | `detyped_files/chaos/shallow/proportion_sweep/main_k02_s10.py` |  |
| 0.60 | 3/5 | 1 | 0.4988s | 0.0512s | 1 | 8 | yes | 0.4638s | 0.5288s | `detyped_files/chaos/shallow/proportion_sweep/main_k03_s01.py` |  |
| 0.60 | 3/5 | 2 | 0.3792s | 0.0307s | 1 | 8 | yes | 0.3572s | 0.3963s | `detyped_files/chaos/shallow/proportion_sweep/main_k03_s02.py` |  |
| 0.60 | 3/5 | 3 | 0.4474s | 0.0424s | 1 | 8 | yes | 0.4192s | 0.4744s | `detyped_files/chaos/shallow/proportion_sweep/main_k03_s03.py` |  |
| 0.60 | 3/5 | 4 | 0.3656s | 0.0325s | 1 | 8 | yes | 0.3445s | 0.3857s | `detyped_files/chaos/shallow/proportion_sweep/main_k03_s04.py` |  |
| 0.60 | 3/5 | 5 | 0.5015s | 0.0178s | 1 | 8 | yes | 0.4896s | 0.5128s | `detyped_files/chaos/shallow/proportion_sweep/main_k03_s05.py` |  |
| 0.60 | 3/5 | 6 | 0.5182s | 0.0158s | 1 | 8 | yes | 0.5080s | 0.5283s | `detyped_files/chaos/shallow/proportion_sweep/main_k03_s06.py` |  |
| 0.60 | 3/5 | 7 | 0.3721s | 0.0553s | 1 | 8 | yes | 0.3372s | 0.4066s | `detyped_files/chaos/shallow/proportion_sweep/main_k03_s07.py` |  |
| 0.60 | 3/5 | 8 | 0.3437s | 0.0331s | 1 | 8 | yes | 0.3225s | 0.3651s | `detyped_files/chaos/shallow/proportion_sweep/main_k03_s08.py` |  |
| 0.60 | 3/5 | 9 | 0.4256s | 0.0386s | 1 | 8 | yes | 0.4001s | 0.4488s | `detyped_files/chaos/shallow/proportion_sweep/main_k03_s09.py` |  |
| 0.60 | 3/5 | 10 | 0.4512s | 0.0298s | 1 | 8 | yes | 0.4293s | 0.4663s | `detyped_files/chaos/shallow/proportion_sweep/main_k03_s10.py` |  |
| 0.80 | 4/5 | 1 | 0.4715s | 0.0282s | 1 | 8 | yes | 0.4556s | 0.4927s | `detyped_files/chaos/shallow/proportion_sweep/main_k04_s01.py` |  |
| 0.80 | 4/5 | 2 | 0.4967s | 0.0112s | 1 | 8 | yes | 0.4891s | 0.5038s | `detyped_files/chaos/shallow/proportion_sweep/main_k04_s02.py` |  |
| 0.80 | 4/5 | 3 | 0.4872s | 0.0303s | 1 | 8 | yes | 0.4651s | 0.4998s | `detyped_files/chaos/shallow/proportion_sweep/main_k04_s03.py` |  |
| 0.80 | 4/5 | 4 | 0.3882s | 0.0306s | 1 | 8 | yes | 0.3659s | 0.4052s | `detyped_files/chaos/shallow/proportion_sweep/main_k04_s04.py` |  |
| 0.80 | 4/5 | 5 | 0.4705s | 0.0391s | 1 | 8 | yes | 0.4445s | 0.4954s | `detyped_files/chaos/shallow/proportion_sweep/main_k04_s05.py` |  |
| 1.00 | 5/5 | 1 | 0.5012s | 0.0334s | 1 | 8 | yes | 0.4781s | 0.5216s | `detyped_files/chaos/shallow/proportion_sweep/main_k05_s01.py` |  |

## chaos/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.3551s | 0.3551s | 0.3551s | 2.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.3551s | 0.0406s | 2 | 16 | yes | 0.3373s | 0.3759s | `static-python-perf/Benchmark/chaos/untyped/main.py` |  |
