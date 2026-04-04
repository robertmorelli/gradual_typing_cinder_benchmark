# Proportion Benchmark Report

- Generated: `2026-04-03T22:12:17-06:00`
- Benchmarks run serially: `yes`
- Iterations per detyped-count bucket: `20`
- Random seed: `0`

## call_method/advanced

- Detypable targets: `6`
- Total runs: `64`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1084s | 0.1084s | 0.1084s | 1.0 | yes | ok |
| 0.17 | 1/6 | 6 | 0.3314s | 0.1165s | 1.1970s | 1.2 | yes | ok |
| 0.33 | 2/6 | 15 | 0.5456s | 0.1283s | 1.3000s | 1.0 | yes | ok |
| 0.50 | 3/6 | 20 | 0.7786s | 0.1524s | 1.4476s | 1.0 | yes | ok |
| 0.67 | 4/6 | 15 | 0.9962s | 0.1742s | 1.4311s | 1.0 | yes | ok |
| 0.83 | 5/6 | 6 | 1.2104s | 0.3299s | 1.4262s | 1.0 | yes | ok |
| 1.00 | 6/6 | 1 | 1.3998s | 1.3998s | 1.3998s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1084s | 0.0126s | 1 | 8 | yes | 0.0996s | 0.1159s | `detyped_files/call_method/advanced/proportion_sweep/main_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 0.2804s | 0.0062s | 1 | 8 | yes | 0.2764s | 0.2844s | `detyped_files/call_method/advanced/proportion_sweep/main_k01_s01.py` |  |
| 0.17 | 1/6 | 2 | 0.1258s | 0.0187s | 1 | 8 | yes | 0.1137s | 0.1382s | `detyped_files/call_method/advanced/proportion_sweep/main_k01_s02.py` |  |
| 0.17 | 1/6 | 3 | 0.1364s | 0.0084s | 1 | 8 | yes | 0.1313s | 0.1421s | `detyped_files/call_method/advanced/proportion_sweep/main_k01_s03.py` |  |
| 0.17 | 1/6 | 4 | 1.1970s | 0.1255s | 2 | 16 | yes | 1.1457s | 1.2629s | `detyped_files/call_method/advanced/proportion_sweep/main_k01_s04.py` |  |
| 0.17 | 1/6 | 5 | 0.1325s | 0.0046s | 1 | 8 | yes | 0.1299s | 0.1357s | `detyped_files/call_method/advanced/proportion_sweep/main_k01_s05.py` |  |
| 0.17 | 1/6 | 6 | 0.1165s | 0.0114s | 1 | 8 | yes | 0.1095s | 0.1242s | `detyped_files/call_method/advanced/proportion_sweep/main_k01_s06.py` |  |
| 0.33 | 2/6 | 1 | 1.1973s | 0.0930s | 1 | 8 | yes | 1.1370s | 1.2582s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s01.py` |  |
| 0.33 | 2/6 | 2 | 0.1535s | 0.0106s | 1 | 8 | yes | 0.1475s | 0.1610s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s02.py` |  |
| 0.33 | 2/6 | 3 | 0.1377s | 0.0125s | 1 | 8 | yes | 0.1299s | 0.1459s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s03.py` |  |
| 0.33 | 2/6 | 4 | 0.1283s | 0.0102s | 1 | 8 | yes | 0.1213s | 0.1346s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s04.py` |  |
| 0.33 | 2/6 | 5 | 1.3000s | 0.0606s | 1 | 8 | yes | 1.2593s | 1.3373s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s05.py` |  |
| 0.33 | 2/6 | 6 | 0.2975s | 0.0291s | 1 | 8 | yes | 0.2763s | 0.3116s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s06.py` |  |
| 0.33 | 2/6 | 7 | 1.2335s | 0.0688s | 1 | 8 | yes | 1.1890s | 1.2764s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s07.py` |  |
| 0.33 | 2/6 | 8 | 0.2841s | 0.0270s | 1 | 8 | yes | 0.2657s | 0.2999s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s08.py` |  |
| 0.33 | 2/6 | 9 | 0.1551s | 0.0203s | 1 | 8 | yes | 0.1422s | 0.1684s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s09.py` |  |
| 0.33 | 2/6 | 10 | 0.1373s | 0.0110s | 1 | 8 | yes | 0.1310s | 0.1454s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s10.py` |  |
| 0.33 | 2/6 | 11 | 1.2101s | 0.0802s | 1 | 8 | yes | 1.1605s | 1.2642s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s11.py` |  |
| 0.33 | 2/6 | 12 | 1.1967s | 0.0400s | 1 | 8 | yes | 1.1675s | 1.2182s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s12.py` |  |
| 0.33 | 2/6 | 13 | 0.1521s | 0.0139s | 1 | 8 | yes | 0.1428s | 0.1608s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s13.py` |  |
| 0.33 | 2/6 | 14 | 0.2936s | 0.0402s | 1 | 8 | yes | 0.2687s | 0.3229s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s14.py` |  |
| 0.33 | 2/6 | 15 | 0.3070s | 0.0125s | 1 | 8 | yes | 0.2986s | 0.3149s | `detyped_files/call_method/advanced/proportion_sweep/main_k02_s15.py` |  |
| 0.50 | 3/6 | 1 | 1.2545s | 0.0586s | 1 | 8 | yes | 1.2187s | 1.2934s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s01.py` |  |
| 0.50 | 3/6 | 2 | 1.4476s | 0.1070s | 1 | 8 | yes | 1.3843s | 1.5261s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s02.py` |  |
| 0.50 | 3/6 | 3 | 0.1767s | 0.0106s | 1 | 8 | yes | 0.1704s | 0.1841s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s03.py` |  |
| 0.50 | 3/6 | 4 | 1.2674s | 0.0849s | 1 | 8 | yes | 1.2165s | 1.3260s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s04.py` |  |
| 0.50 | 3/6 | 5 | 0.3368s | 0.0252s | 1 | 8 | yes | 0.3226s | 0.3544s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s05.py` |  |
| 0.50 | 3/6 | 6 | 1.2915s | 0.0598s | 1 | 8 | yes | 1.2557s | 1.3331s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s06.py` |  |
| 0.50 | 3/6 | 7 | 0.3057s | 0.0258s | 1 | 8 | yes | 0.2915s | 0.3247s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s07.py` |  |
| 0.50 | 3/6 | 8 | 0.1536s | 0.0049s | 1 | 8 | yes | 0.1511s | 0.1572s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s08.py` |  |
| 0.50 | 3/6 | 9 | 1.2838s | 0.0761s | 1 | 8 | yes | 1.2327s | 1.3326s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s09.py` |  |
| 0.50 | 3/6 | 10 | 1.2232s | 0.0509s | 1 | 8 | yes | 1.1871s | 1.2519s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s10.py` |  |
| 0.50 | 3/6 | 11 | 0.3001s | 0.0237s | 1 | 8 | yes | 0.2826s | 0.3126s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s11.py` |  |
| 0.50 | 3/6 | 12 | 0.1553s | 0.0149s | 1 | 8 | yes | 0.1468s | 0.1661s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s12.py` |  |
| 0.50 | 3/6 | 13 | 0.1524s | 0.0071s | 1 | 8 | yes | 0.1482s | 0.1573s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s13.py` |  |
| 0.50 | 3/6 | 14 | 0.2920s | 0.0269s | 1 | 8 | yes | 0.2722s | 0.3073s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s14.py` |  |
| 0.50 | 3/6 | 15 | 1.2457s | 0.0292s | 1 | 8 | yes | 1.2285s | 1.2654s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s15.py` |  |
| 0.50 | 3/6 | 16 | 1.3677s | 0.0770s | 1 | 8 | yes | 1.3163s | 1.4153s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s16.py` |  |
| 0.50 | 3/6 | 17 | 0.3115s | 0.0439s | 1 | 8 | yes | 0.2845s | 0.3419s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s17.py` |  |
| 0.50 | 3/6 | 18 | 0.3283s | 0.0210s | 1 | 8 | yes | 0.3157s | 0.3424s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s18.py` |  |
| 0.50 | 3/6 | 19 | 1.3221s | 0.0687s | 1 | 8 | yes | 1.2762s | 1.3642s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s19.py` |  |
| 0.50 | 3/6 | 20 | 1.3566s | 0.0886s | 1 | 8 | yes | 1.3024s | 1.4166s | `detyped_files/call_method/advanced/proportion_sweep/main_k03_s20.py` |  |
| 0.67 | 4/6 | 1 | 0.3208s | 0.0247s | 1 | 8 | yes | 0.3027s | 0.3345s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s01.py` |  |
| 0.67 | 4/6 | 2 | 0.3129s | 0.0281s | 1 | 8 | yes | 0.2929s | 0.3302s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s02.py` |  |
| 0.67 | 4/6 | 3 | 1.2676s | 0.0661s | 1 | 8 | yes | 1.2285s | 1.3137s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s03.py` |  |
| 0.67 | 4/6 | 4 | 1.4176s | 0.1007s | 1 | 8 | yes | 1.3550s | 1.4838s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s04.py` |  |
| 0.67 | 4/6 | 5 | 1.2963s | 0.0356s | 1 | 8 | yes | 1.2734s | 1.3191s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s05.py` |  |
| 0.67 | 4/6 | 6 | 1.3303s | 0.0515s | 1 | 8 | yes | 1.2964s | 1.3632s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s06.py` |  |
| 0.67 | 4/6 | 7 | 1.4311s | 0.1386s | 1 | 8 | yes | 1.3465s | 1.5238s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s07.py` |  |
| 0.67 | 4/6 | 8 | 0.3351s | 0.0226s | 1 | 8 | yes | 0.3189s | 0.3475s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s08.py` |  |
| 0.67 | 4/6 | 9 | 1.3089s | 0.1403s | 1 | 8 | yes | 1.2245s | 1.4016s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s09.py` |  |
| 0.67 | 4/6 | 10 | 1.4131s | 0.1557s | 1 | 8 | yes | 1.3321s | 1.5271s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s10.py` |  |
| 0.67 | 4/6 | 11 | 1.3782s | 0.0677s | 1 | 8 | yes | 1.3325s | 1.4199s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s11.py` |  |
| 0.67 | 4/6 | 12 | 0.3240s | 0.0240s | 1 | 8 | yes | 0.3071s | 0.3389s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s12.py` |  |
| 0.67 | 4/6 | 13 | 1.4203s | 0.0663s | 1 | 8 | yes | 1.3739s | 1.4582s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s13.py` |  |
| 0.67 | 4/6 | 14 | 1.2119s | 0.0666s | 1 | 8 | yes | 1.1697s | 1.2554s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s14.py` |  |
| 0.67 | 4/6 | 15 | 0.1742s | 0.0133s | 1 | 8 | yes | 0.1651s | 0.1829s | `detyped_files/call_method/advanced/proportion_sweep/main_k04_s15.py` |  |
| 0.83 | 5/6 | 1 | 1.4262s | 0.0700s | 1 | 8 | yes | 1.3811s | 1.4713s | `detyped_files/call_method/advanced/proportion_sweep/main_k05_s01.py` |  |
| 0.83 | 5/6 | 2 | 1.2915s | 0.0578s | 1 | 8 | yes | 1.2499s | 1.3248s | `detyped_files/call_method/advanced/proportion_sweep/main_k05_s02.py` |  |
| 0.83 | 5/6 | 3 | 0.3299s | 0.0290s | 1 | 8 | yes | 0.3086s | 0.3447s | `detyped_files/call_method/advanced/proportion_sweep/main_k05_s03.py` |  |
| 0.83 | 5/6 | 4 | 1.4121s | 0.0919s | 1 | 8 | yes | 1.3580s | 1.4752s | `detyped_files/call_method/advanced/proportion_sweep/main_k05_s04.py` |  |
| 0.83 | 5/6 | 5 | 1.3812s | 0.0247s | 1 | 8 | yes | 1.3647s | 1.3965s | `detyped_files/call_method/advanced/proportion_sweep/main_k05_s05.py` |  |
| 0.83 | 5/6 | 6 | 1.4216s | 0.0825s | 1 | 8 | yes | 1.3652s | 1.4718s | `detyped_files/call_method/advanced/proportion_sweep/main_k05_s06.py` |  |
| 1.00 | 6/6 | 1 | 1.3998s | 0.1342s | 1 | 8 | yes | 1.3181s | 1.4901s | `detyped_files/call_method/advanced/proportion_sweep/main_k06_s01.py` |  |

## call_method/shallow

- Detypable targets: `6`
- Total runs: `64`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1066s | 0.1066s | 0.1066s | 1.0 | yes | ok |
| 0.17 | 1/6 | 6 | 0.3145s | 0.1085s | 1.2429s | 1.0 | yes | ok |
| 0.33 | 2/6 | 15 | 0.5163s | 0.1063s | 1.3629s | 1.1 | yes | ok |
| 0.50 | 3/6 | 20 | 0.7252s | 0.1106s | 1.3850s | 1.1 | yes | ok |
| 0.67 | 4/6 | 15 | 0.9090s | 0.1194s | 1.3553s | 1.1 | yes | ok |
| 0.83 | 5/6 | 6 | 1.0982s | 0.1998s | 1.3191s | 1.2 | yes | ok |
| 1.00 | 6/6 | 1 | 1.2548s | 1.2548s | 1.2548s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1066s | 0.0117s | 1 | 8 | yes | 0.0987s | 0.1135s | `detyped_files/call_method/shallow/proportion_sweep/main_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 1.2429s | 0.0672s | 1 | 8 | yes | 1.2031s | 1.2897s | `detyped_files/call_method/shallow/proportion_sweep/main_k01_s01.py` |  |
| 0.17 | 1/6 | 2 | 0.1958s | 0.0167s | 1 | 8 | yes | 0.1861s | 0.2073s | `detyped_files/call_method/shallow/proportion_sweep/main_k01_s02.py` |  |
| 0.17 | 1/6 | 3 | 0.1085s | 0.0054s | 1 | 8 | yes | 0.1046s | 0.1112s | `detyped_files/call_method/shallow/proportion_sweep/main_k01_s03.py` |  |
| 0.17 | 1/6 | 4 | 0.1206s | 0.0128s | 1 | 8 | yes | 0.1138s | 0.1297s | `detyped_files/call_method/shallow/proportion_sweep/main_k01_s04.py` |  |
| 0.17 | 1/6 | 5 | 0.1091s | 0.0095s | 1 | 8 | yes | 0.1021s | 0.1143s | `detyped_files/call_method/shallow/proportion_sweep/main_k01_s05.py` |  |
| 0.17 | 1/6 | 6 | 0.1104s | 0.0082s | 1 | 8 | yes | 0.1057s | 0.1162s | `detyped_files/call_method/shallow/proportion_sweep/main_k01_s06.py` |  |
| 0.33 | 2/6 | 1 | 1.2287s | 0.0524s | 1 | 8 | yes | 1.1968s | 1.2647s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s01.py` |  |
| 0.33 | 2/6 | 2 | 1.2632s | 0.1265s | 1 | 8 | yes | 1.1833s | 1.3466s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s02.py` |  |
| 0.33 | 2/6 | 3 | 0.1972s | 0.0148s | 1 | 8 | yes | 0.1886s | 0.2075s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s03.py` |  |
| 0.33 | 2/6 | 4 | 0.1921s | 0.0103s | 1 | 8 | yes | 0.1858s | 0.1990s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s04.py` |  |
| 0.33 | 2/6 | 5 | 0.1941s | 0.0108s | 1 | 8 | yes | 0.1876s | 0.2016s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s05.py` |  |
| 0.33 | 2/6 | 6 | 0.1228s | 0.0143s | 1 | 8 | yes | 0.1140s | 0.1323s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s06.py` |  |
| 0.33 | 2/6 | 7 | 0.1063s | 0.0106s | 1 | 8 | yes | 0.0986s | 0.1121s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s07.py` |  |
| 0.33 | 2/6 | 8 | 1.3629s | 0.0946s | 1 | 8 | yes | 1.3059s | 1.4267s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s08.py` |  |
| 0.33 | 2/6 | 9 | 0.1108s | 0.0023s | 1 | 8 | yes | 0.1093s | 0.1123s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s09.py` |  |
| 0.33 | 2/6 | 10 | 0.1114s | 0.0037s | 1 | 8 | yes | 0.1089s | 0.1136s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s10.py` |  |
| 0.33 | 2/6 | 11 | 1.2088s | 0.1049s | 1 | 8 | yes | 1.1460s | 1.2807s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s11.py` |  |
| 0.33 | 2/6 | 12 | 1.2129s | 0.0651s | 1 | 8 | yes | 1.1714s | 1.2545s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s12.py` |  |
| 0.33 | 2/6 | 13 | 0.1141s | 0.0028s | 1 | 8 | yes | 0.1123s | 0.1159s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s13.py` |  |
| 0.33 | 2/6 | 14 | 0.1983s | 0.0302s | 2 | 16 | yes | 0.1847s | 0.2133s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s14.py` |  |
| 0.33 | 2/6 | 15 | 0.1208s | 0.0223s | 2 | 16 | yes | 0.1109s | 0.1317s | `detyped_files/call_method/shallow/proportion_sweep/main_k02_s15.py` |  |
| 0.50 | 3/6 | 1 | 1.2665s | 0.0683s | 1 | 8 | yes | 1.2207s | 1.3075s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s01.py` |  |
| 0.50 | 3/6 | 2 | 0.1886s | 0.0089s | 1 | 8 | yes | 0.1837s | 0.1948s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s02.py` |  |
| 0.50 | 3/6 | 3 | 0.1980s | 0.0260s | 2 | 16 | yes | 0.1866s | 0.2112s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s03.py` |  |
| 0.50 | 3/6 | 4 | 0.1932s | 0.0140s | 1 | 8 | yes | 0.1838s | 0.2017s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s04.py` |  |
| 0.50 | 3/6 | 5 | 1.2402s | 0.0432s | 1 | 8 | yes | 1.2191s | 1.2717s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s05.py` |  |
| 0.50 | 3/6 | 6 | 1.3773s | 0.1017s | 1 | 8 | yes | 1.3134s | 1.4468s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s06.py` |  |
| 0.50 | 3/6 | 7 | 0.1926s | 0.0084s | 1 | 8 | yes | 0.1885s | 0.1985s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s07.py` |  |
| 0.50 | 3/6 | 8 | 0.1203s | 0.0112s | 1 | 8 | yes | 0.1134s | 0.1279s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s08.py` |  |
| 0.50 | 3/6 | 9 | 0.1106s | 0.0084s | 1 | 8 | yes | 0.1048s | 0.1154s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s09.py` |  |
| 0.50 | 3/6 | 10 | 1.2246s | 0.0746s | 1 | 8 | yes | 1.1769s | 1.2735s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s10.py` |  |
| 0.50 | 3/6 | 11 | 1.2725s | 0.0328s | 1 | 8 | yes | 1.2523s | 1.2943s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s11.py` |  |
| 0.50 | 3/6 | 12 | 1.3191s | 0.1208s | 1 | 8 | yes | 1.2403s | 1.3953s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s12.py` |  |
| 0.50 | 3/6 | 13 | 0.1176s | 0.0160s | 2 | 16 | yes | 0.1108s | 0.1258s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s13.py` |  |
| 0.50 | 3/6 | 14 | 1.3850s | 0.0854s | 1 | 8 | yes | 1.3340s | 1.4421s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s14.py` |  |
| 0.50 | 3/6 | 15 | 1.2707s | 0.1075s | 1 | 8 | yes | 1.1998s | 1.3400s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s15.py` |  |
| 0.50 | 3/6 | 16 | 1.2614s | 0.1069s | 1 | 8 | yes | 1.2006s | 1.3385s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s16.py` |  |
| 0.50 | 3/6 | 17 | 0.1996s | 0.0190s | 1 | 8 | yes | 0.1887s | 0.2132s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s17.py` |  |
| 0.50 | 3/6 | 18 | 1.2525s | 0.0532s | 1 | 8 | yes | 1.2196s | 1.2881s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s18.py` |  |
| 0.50 | 3/6 | 19 | 0.1887s | 0.0109s | 1 | 8 | yes | 0.1828s | 0.1965s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s19.py` |  |
| 0.50 | 3/6 | 20 | 0.1251s | 0.0243s | 2 | 16 | yes | 0.1145s | 0.1375s | `detyped_files/call_method/shallow/proportion_sweep/main_k03_s20.py` |  |
| 0.67 | 4/6 | 1 | 1.3159s | 0.0641s | 1 | 8 | yes | 1.2783s | 1.3595s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s01.py` |  |
| 0.67 | 4/6 | 2 | 0.1872s | 0.0160s | 1 | 8 | yes | 0.1766s | 0.1975s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s02.py` |  |
| 0.67 | 4/6 | 3 | 1.3553s | 0.1098s | 1 | 8 | yes | 1.2860s | 1.4264s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s03.py` |  |
| 0.67 | 4/6 | 4 | 0.1194s | 0.0099s | 1 | 8 | yes | 0.1138s | 0.1262s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s04.py` |  |
| 0.67 | 4/6 | 5 | 1.2717s | 0.1085s | 1 | 8 | yes | 1.2065s | 1.3474s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s05.py` |  |
| 0.67 | 4/6 | 6 | 1.2405s | 0.0552s | 1 | 8 | yes | 1.2033s | 1.2744s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s06.py` |  |
| 0.67 | 4/6 | 7 | 1.2274s | 0.0832s | 1 | 8 | yes | 1.1741s | 1.2819s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s07.py` |  |
| 0.67 | 4/6 | 8 | 0.1989s | 0.0107s | 1 | 8 | yes | 0.1919s | 0.2059s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s08.py` |  |
| 0.67 | 4/6 | 9 | 1.3085s | 0.0847s | 1 | 8 | yes | 1.2582s | 1.3650s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s09.py` |  |
| 0.67 | 4/6 | 10 | 0.1927s | 0.0115s | 1 | 8 | yes | 0.1865s | 0.2009s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s10.py` |  |
| 0.67 | 4/6 | 11 | 0.1874s | 0.0164s | 1 | 8 | yes | 0.1770s | 0.1979s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s11.py` |  |
| 0.67 | 4/6 | 12 | 1.2703s | 0.0659s | 1 | 8 | yes | 1.2270s | 1.3118s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s12.py` |  |
| 0.67 | 4/6 | 13 | 1.2256s | 0.0780s | 1 | 8 | yes | 1.1750s | 1.2741s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s13.py` |  |
| 0.67 | 4/6 | 14 | 1.1912s | 0.0619s | 1 | 8 | yes | 1.1498s | 1.2293s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s14.py` |  |
| 0.67 | 4/6 | 15 | 1.3435s | 0.1722s | 2 | 16 | yes | 1.2727s | 1.4324s | `detyped_files/call_method/shallow/proportion_sweep/main_k04_s15.py` |  |
| 0.83 | 5/6 | 1 | 1.2972s | 0.0928s | 1 | 8 | yes | 1.2378s | 1.3559s | `detyped_files/call_method/shallow/proportion_sweep/main_k05_s01.py` |  |
| 0.83 | 5/6 | 2 | 0.1998s | 0.0217s | 2 | 16 | yes | 0.1915s | 0.2118s | `detyped_files/call_method/shallow/proportion_sweep/main_k05_s02.py` |  |
| 0.83 | 5/6 | 3 | 1.2679s | 0.0517s | 1 | 8 | yes | 1.2374s | 1.3036s | `detyped_files/call_method/shallow/proportion_sweep/main_k05_s03.py` |  |
| 0.83 | 5/6 | 4 | 1.2559s | 0.0951s | 1 | 8 | yes | 1.1962s | 1.3207s | `detyped_files/call_method/shallow/proportion_sweep/main_k05_s04.py` |  |
| 0.83 | 5/6 | 5 | 1.3191s | 0.0461s | 1 | 8 | yes | 1.2886s | 1.3483s | `detyped_files/call_method/shallow/proportion_sweep/main_k05_s05.py` |  |
| 0.83 | 5/6 | 6 | 1.2495s | 0.0508s | 1 | 8 | yes | 1.2166s | 1.2826s | `detyped_files/call_method/shallow/proportion_sweep/main_k05_s06.py` |  |
| 1.00 | 6/6 | 1 | 1.2548s | 0.0548s | 1 | 8 | yes | 1.2185s | 1.2890s | `detyped_files/call_method/shallow/proportion_sweep/main_k06_s01.py` |  |

## call_method/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.1322s | 0.1322s | 0.1322s | 3.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.1322s | 0.0259s | 3 | 24 | yes | 0.1224s | 0.1424s | `static-python-perf/Benchmark/call_method/untyped/main.py` |  |

## call_method_slots/advanced

- Detypable targets: `6`
- Total runs: `64`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1127s | 0.1127s | 0.1127s | 1.0 | yes | ok |
| 0.17 | 1/6 | 6 | 0.3380s | 0.1082s | 1.2373s | 1.0 | yes | ok |
| 0.33 | 2/6 | 15 | 0.5705s | 0.1282s | 1.4138s | 1.1 | yes | ok |
| 0.50 | 3/6 | 20 | 0.7904s | 0.1464s | 1.4733s | 1.0 | yes | ok |
| 0.67 | 4/6 | 15 | 1.0079s | 0.1608s | 1.4367s | 1.1 | yes | ok |
| 0.83 | 5/6 | 6 | 1.2017s | 0.3369s | 1.4025s | 1.0 | yes | ok |
| 1.00 | 6/6 | 1 | 1.3668s | 1.3668s | 1.3668s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1127s | 0.0076s | 1 | 8 | yes | 0.1084s | 0.1181s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 0.1276s | 0.0139s | 1 | 8 | yes | 0.1178s | 0.1353s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k01_s01.py` |  |
| 0.17 | 1/6 | 2 | 0.1082s | 0.0016s | 1 | 8 | yes | 0.1075s | 0.1094s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k01_s02.py` |  |
| 0.17 | 1/6 | 3 | 0.2747s | 0.0354s | 1 | 8 | yes | 0.2506s | 0.2964s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k01_s03.py` |  |
| 0.17 | 1/6 | 4 | 0.1291s | 0.0154s | 1 | 8 | yes | 0.1189s | 0.1387s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k01_s04.py` |  |
| 0.17 | 1/6 | 5 | 1.2373s | 0.0615s | 1 | 8 | yes | 1.1991s | 1.2781s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k01_s05.py` |  |
| 0.17 | 1/6 | 6 | 0.1513s | 0.0202s | 1 | 8 | yes | 0.1391s | 0.1651s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k01_s06.py` |  |
| 0.33 | 2/6 | 1 | 1.2771s | 0.0960s | 1 | 8 | yes | 1.2274s | 1.3485s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k02_s01.py` |  |
| 0.33 | 2/6 | 2 | 0.3189s | 0.0404s | 1 | 8 | yes | 0.2939s | 0.3456s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k02_s02.py` |  |
| 0.33 | 2/6 | 3 | 1.2404s | 0.0938s | 1 | 8 | yes | 1.1830s | 1.3040s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k02_s03.py` |  |
| 0.33 | 2/6 | 4 | 0.1542s | 0.0077s | 1 | 8 | yes | 0.1489s | 0.1590s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k02_s04.py` |  |
| 0.33 | 2/6 | 5 | 0.1282s | 0.0102s | 1 | 8 | yes | 0.1207s | 0.1327s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k02_s05.py` |  |
| 0.33 | 2/6 | 6 | 1.2379s | 0.0825s | 1 | 8 | yes | 1.1806s | 1.2876s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k02_s06.py` |  |
| 0.33 | 2/6 | 7 | 1.4138s | 0.0783s | 1 | 8 | yes | 1.3720s | 1.4704s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k02_s07.py` |  |
| 0.33 | 2/6 | 8 | 0.1397s | 0.0132s | 1 | 8 | yes | 0.1326s | 0.1492s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k02_s08.py` |  |
| 0.33 | 2/6 | 9 | 0.2985s | 0.0196s | 1 | 8 | yes | 0.2860s | 0.3109s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k02_s09.py` |  |
| 0.33 | 2/6 | 10 | 1.3040s | 0.0467s | 1 | 8 | yes | 1.2745s | 1.3349s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k02_s10.py` |  |
| 0.33 | 2/6 | 11 | 0.3284s | 0.0405s | 1 | 8 | yes | 0.3050s | 0.3565s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k02_s11.py` |  |
| 0.33 | 2/6 | 12 | 0.2788s | 0.0261s | 1 | 8 | yes | 0.2601s | 0.2940s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k02_s12.py` |  |
| 0.33 | 2/6 | 13 | 0.1615s | 0.0260s | 2 | 16 | yes | 0.1504s | 0.1748s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k02_s13.py` |  |
| 0.33 | 2/6 | 14 | 0.1470s | 0.0106s | 1 | 8 | yes | 0.1396s | 0.1536s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k02_s14.py` |  |
| 0.33 | 2/6 | 15 | 0.1284s | 0.0059s | 1 | 8 | yes | 0.1253s | 0.1327s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k02_s15.py` |  |
| 0.50 | 3/6 | 1 | 1.4733s | 0.1579s | 1 | 8 | yes | 1.3767s | 1.5752s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s01.py` |  |
| 0.50 | 3/6 | 2 | 1.2753s | 0.0706s | 1 | 8 | yes | 1.2339s | 1.3253s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s02.py` |  |
| 0.50 | 3/6 | 3 | 0.2904s | 0.0277s | 1 | 8 | yes | 0.2709s | 0.3059s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s03.py` |  |
| 0.50 | 3/6 | 4 | 1.3926s | 0.0965s | 1 | 8 | yes | 1.3302s | 1.4528s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s04.py` |  |
| 0.50 | 3/6 | 5 | 0.1464s | 0.0113s | 1 | 8 | yes | 0.1381s | 0.1528s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s05.py` |  |
| 0.50 | 3/6 | 6 | 1.2411s | 0.0597s | 1 | 8 | yes | 1.1994s | 1.2771s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s06.py` |  |
| 0.50 | 3/6 | 7 | 0.3168s | 0.0062s | 1 | 8 | yes | 0.3128s | 0.3208s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s07.py` |  |
| 0.50 | 3/6 | 8 | 0.3068s | 0.0352s | 1 | 8 | yes | 0.2835s | 0.3298s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s08.py` |  |
| 0.50 | 3/6 | 9 | 0.3034s | 0.0224s | 1 | 8 | yes | 0.2883s | 0.3171s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s09.py` |  |
| 0.50 | 3/6 | 10 | 1.2871s | 0.1107s | 1 | 8 | yes | 1.2173s | 1.3578s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s10.py` |  |
| 0.50 | 3/6 | 11 | 1.3910s | 0.0786s | 1 | 8 | yes | 1.3374s | 1.4398s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s11.py` |  |
| 0.50 | 3/6 | 12 | 1.3196s | 0.0906s | 1 | 8 | yes | 1.2680s | 1.3836s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s12.py` |  |
| 0.50 | 3/6 | 13 | 0.1597s | 0.0085s | 1 | 8 | yes | 0.1548s | 0.1654s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s13.py` |  |
| 0.50 | 3/6 | 14 | 1.3103s | 0.1106s | 1 | 8 | yes | 1.2409s | 1.3846s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s14.py` |  |
| 0.50 | 3/6 | 15 | 1.2520s | 0.0968s | 1 | 8 | yes | 1.1888s | 1.3141s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s15.py` |  |
| 0.50 | 3/6 | 16 | 0.1775s | 0.0085s | 1 | 8 | yes | 0.1726s | 0.1835s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s16.py` |  |
| 0.50 | 3/6 | 17 | 0.2885s | 0.0315s | 1 | 8 | yes | 0.2673s | 0.3079s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s17.py` |  |
| 0.50 | 3/6 | 18 | 0.1513s | 0.0024s | 1 | 8 | yes | 0.1500s | 0.1530s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s18.py` |  |
| 0.50 | 3/6 | 19 | 0.2911s | 0.0336s | 1 | 8 | yes | 0.2693s | 0.3124s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s19.py` |  |
| 0.50 | 3/6 | 20 | 1.4333s | 0.0831s | 1 | 8 | yes | 1.3839s | 1.4903s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k03_s20.py` |  |
| 0.67 | 4/6 | 1 | 1.2688s | 0.0767s | 1 | 8 | yes | 1.2204s | 1.3210s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k04_s01.py` |  |
| 0.67 | 4/6 | 2 | 1.2780s | 0.0665s | 1 | 8 | yes | 1.2332s | 1.3180s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k04_s02.py` |  |
| 0.67 | 4/6 | 3 | 1.4257s | 0.1667s | 1 | 8 | yes | 1.3386s | 1.5472s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k04_s03.py` |  |
| 0.67 | 4/6 | 4 | 1.4240s | 0.0857s | 1 | 8 | yes | 1.3661s | 1.4777s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k04_s04.py` |  |
| 0.67 | 4/6 | 5 | 0.3297s | 0.0249s | 1 | 8 | yes | 0.3127s | 0.3451s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k04_s05.py` |  |
| 0.67 | 4/6 | 6 | 0.3228s | 0.0259s | 1 | 8 | yes | 0.3038s | 0.3364s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k04_s06.py` |  |
| 0.67 | 4/6 | 7 | 1.4195s | 0.0804s | 1 | 8 | yes | 1.3695s | 1.4723s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k04_s07.py` |  |
| 0.67 | 4/6 | 8 | 1.4367s | 0.1464s | 1 | 8 | yes | 1.3521s | 1.5415s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k04_s08.py` |  |
| 0.67 | 4/6 | 9 | 1.4102s | 0.0798s | 1 | 8 | yes | 1.3631s | 1.4666s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k04_s09.py` |  |
| 0.67 | 4/6 | 10 | 1.2643s | 0.0992s | 1 | 8 | yes | 1.2032s | 1.3310s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k04_s10.py` |  |
| 0.67 | 4/6 | 11 | 0.3199s | 0.0275s | 1 | 8 | yes | 0.3001s | 0.3349s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k04_s11.py` |  |
| 0.67 | 4/6 | 12 | 0.3455s | 0.0305s | 1 | 8 | yes | 0.3236s | 0.3632s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k04_s12.py` |  |
| 0.67 | 4/6 | 13 | 1.3101s | 0.1640s | 2 | 16 | yes | 1.2510s | 1.3978s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k04_s13.py` |  |
| 0.67 | 4/6 | 14 | 0.1608s | 0.0142s | 1 | 8 | yes | 0.1511s | 0.1692s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k04_s14.py` |  |
| 0.67 | 4/6 | 15 | 1.4024s | 0.0973s | 1 | 8 | yes | 1.3367s | 1.4624s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k04_s15.py` |  |
| 0.83 | 5/6 | 1 | 0.3369s | 0.0206s | 1 | 8 | yes | 0.3222s | 0.3488s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k05_s01.py` |  |
| 0.83 | 5/6 | 2 | 1.3787s | 0.0751s | 1 | 8 | yes | 1.3300s | 1.4267s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k05_s02.py` |  |
| 0.83 | 5/6 | 3 | 1.4007s | 0.0606s | 1 | 8 | yes | 1.3566s | 1.4337s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k05_s03.py` |  |
| 0.83 | 5/6 | 4 | 1.3986s | 0.0725s | 1 | 8 | yes | 1.3552s | 1.4487s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k05_s04.py` |  |
| 0.83 | 5/6 | 5 | 1.4025s | 0.0795s | 1 | 8 | yes | 1.3485s | 1.4498s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k05_s05.py` |  |
| 0.83 | 5/6 | 6 | 1.2924s | 0.0564s | 1 | 8 | yes | 1.2586s | 1.3318s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k05_s06.py` |  |
| 1.00 | 6/6 | 1 | 1.3668s | 0.0972s | 1 | 8 | yes | 1.3053s | 1.4293s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_k06_s01.py` |  |

## call_method_slots/shallow

- Detypable targets: `6`
- Total runs: `64`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1069s | 0.1069s | 0.1069s | 1.0 | yes | ok |
| 0.17 | 1/6 | 6 | 0.3143s | 0.1127s | 1.2250s | 1.0 | yes | ok |
| 0.33 | 2/6 | 15 | 0.5135s | 0.1123s | 1.3015s | 1.4 | yes | ok |
| 0.50 | 3/6 | 20 | 0.7172s | 0.1117s | 1.3516s | 1.0 | yes | ok |
| 0.67 | 4/6 | 15 | 0.8997s | 0.1183s | 1.2953s | 1.1 | yes | ok |
| 0.83 | 5/6 | 6 | 1.0922s | 0.1928s | 1.3393s | 1.0 | yes | ok |
| 1.00 | 6/6 | 1 | 1.2979s | 1.2979s | 1.2979s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1069s | 0.0108s | 1 | 8 | yes | 0.0990s | 0.1134s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 1.2250s | 0.0898s | 1 | 8 | yes | 1.1714s | 1.2898s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k01_s01.py` |  |
| 0.17 | 1/6 | 2 | 0.1904s | 0.0092s | 1 | 8 | yes | 0.1852s | 0.1970s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k01_s02.py` |  |
| 0.17 | 1/6 | 3 | 0.1145s | 0.0040s | 1 | 8 | yes | 0.1124s | 0.1173s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k01_s03.py` |  |
| 0.17 | 1/6 | 4 | 0.1183s | 0.0108s | 1 | 8 | yes | 0.1115s | 0.1254s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k01_s04.py` |  |
| 0.17 | 1/6 | 5 | 0.1127s | 0.0079s | 1 | 8 | yes | 0.1078s | 0.1182s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k01_s05.py` |  |
| 0.17 | 1/6 | 6 | 0.1248s | 0.0185s | 1 | 8 | yes | 0.1134s | 0.1369s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k01_s06.py` |  |
| 0.33 | 2/6 | 1 | 0.1901s | 0.0093s | 1 | 8 | yes | 0.1847s | 0.1965s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k02_s01.py` |  |
| 0.33 | 2/6 | 2 | 0.1889s | 0.0252s | 2 | 16 | yes | 0.1783s | 0.2017s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k02_s02.py` |  |
| 0.33 | 2/6 | 3 | 0.1141s | 0.0107s | 1 | 8 | yes | 0.1071s | 0.1214s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k02_s03.py` |  |
| 0.33 | 2/6 | 4 | 0.1123s | 0.0049s | 1 | 8 | yes | 0.1088s | 0.1151s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k02_s04.py` |  |
| 0.33 | 2/6 | 5 | 0.1225s | 0.0267s | 4 | 32 | yes | 0.1149s | 0.1327s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k02_s05.py` |  |
| 0.33 | 2/6 | 6 | 0.1967s | 0.0190s | 1 | 8 | yes | 0.1856s | 0.2101s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k02_s06.py` |  |
| 0.33 | 2/6 | 7 | 1.3015s | 0.1118s | 1 | 8 | yes | 1.2333s | 1.3778s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k02_s07.py` |  |
| 0.33 | 2/6 | 8 | 1.2487s | 0.0389s | 1 | 8 | yes | 1.2246s | 1.2748s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k02_s08.py` |  |
| 0.33 | 2/6 | 9 | 0.1827s | 0.0199s | 1 | 8 | yes | 0.1699s | 0.1950s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k02_s09.py` |  |
| 0.33 | 2/6 | 10 | 1.2398s | 0.0728s | 1 | 8 | yes | 1.1945s | 1.2867s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k02_s10.py` |  |
| 0.33 | 2/6 | 11 | 0.1152s | 0.0089s | 1 | 8 | yes | 0.1104s | 0.1217s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k02_s11.py` |  |
| 0.33 | 2/6 | 12 | 1.2025s | 0.0919s | 1 | 8 | yes | 1.1467s | 1.2667s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k02_s12.py` |  |
| 0.33 | 2/6 | 13 | 0.1235s | 0.0200s | 2 | 16 | yes | 0.1147s | 0.1337s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k02_s13.py` |  |
| 0.33 | 2/6 | 14 | 1.2433s | 0.0500s | 1 | 8 | yes | 1.2109s | 1.2759s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k02_s14.py` |  |
| 0.33 | 2/6 | 15 | 0.1202s | 0.0198s | 2 | 16 | yes | 0.1116s | 0.1301s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k02_s15.py` |  |
| 0.50 | 3/6 | 1 | 0.1943s | 0.0095s | 1 | 8 | yes | 0.1885s | 0.2006s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s01.py` |  |
| 0.50 | 3/6 | 2 | 1.2605s | 0.0642s | 1 | 8 | yes | 1.2198s | 1.3016s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s02.py` |  |
| 0.50 | 3/6 | 3 | 1.2481s | 0.1121s | 1 | 8 | yes | 1.1798s | 1.3222s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s03.py` |  |
| 0.50 | 3/6 | 4 | 0.1181s | 0.0161s | 1 | 8 | yes | 0.1080s | 0.1290s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s04.py` |  |
| 0.50 | 3/6 | 5 | 1.3516s | 0.0743s | 1 | 8 | yes | 1.3044s | 1.4005s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s05.py` |  |
| 0.50 | 3/6 | 6 | 1.2515s | 0.0783s | 1 | 8 | yes | 1.2055s | 1.3067s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s06.py` |  |
| 0.50 | 3/6 | 7 | 0.1789s | 0.0177s | 1 | 8 | yes | 0.1667s | 0.1897s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s07.py` |  |
| 0.50 | 3/6 | 8 | 1.3334s | 0.0815s | 1 | 8 | yes | 1.2828s | 1.3861s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s08.py` |  |
| 0.50 | 3/6 | 9 | 0.1894s | 0.0150s | 1 | 8 | yes | 0.1792s | 0.1993s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s09.py` |  |
| 0.50 | 3/6 | 10 | 0.1916s | 0.0136s | 1 | 8 | yes | 0.1835s | 0.2008s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s10.py` |  |
| 0.50 | 3/6 | 11 | 1.2311s | 0.0689s | 1 | 8 | yes | 1.1851s | 1.2755s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s11.py` |  |
| 0.50 | 3/6 | 12 | 0.1991s | 0.0198s | 1 | 8 | yes | 0.1888s | 0.2134s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s12.py` |  |
| 0.50 | 3/6 | 13 | 1.2847s | 0.0847s | 1 | 8 | yes | 1.2311s | 1.3402s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s13.py` |  |
| 0.50 | 3/6 | 14 | 1.2650s | 0.0366s | 1 | 8 | yes | 1.2411s | 1.2882s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s14.py` |  |
| 0.50 | 3/6 | 15 | 0.1165s | 0.0080s | 1 | 8 | yes | 0.1118s | 0.1221s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s15.py` |  |
| 0.50 | 3/6 | 16 | 1.2670s | 0.0767s | 1 | 8 | yes | 1.2206s | 1.3167s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s16.py` |  |
| 0.50 | 3/6 | 17 | 0.1270s | 0.0155s | 1 | 8 | yes | 0.1176s | 0.1375s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s17.py` |  |
| 0.50 | 3/6 | 18 | 1.2405s | 0.0155s | 1 | 8 | yes | 1.2303s | 1.2506s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s18.py` |  |
| 0.50 | 3/6 | 19 | 0.1837s | 0.0088s | 1 | 8 | yes | 0.1777s | 0.1887s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s19.py` |  |
| 0.50 | 3/6 | 20 | 0.1117s | 0.0083s | 1 | 8 | yes | 0.1064s | 0.1171s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k03_s20.py` |  |
| 0.67 | 4/6 | 1 | 1.2953s | 0.0521s | 1 | 8 | yes | 1.2624s | 1.3298s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k04_s01.py` |  |
| 0.67 | 4/6 | 2 | 1.2411s | 0.0543s | 1 | 8 | yes | 1.2014s | 1.2714s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k04_s02.py` |  |
| 0.67 | 4/6 | 3 | 0.1971s | 0.0184s | 1 | 8 | yes | 0.1867s | 0.2104s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k04_s03.py` |  |
| 0.67 | 4/6 | 4 | 1.2674s | 0.0586s | 1 | 8 | yes | 1.2246s | 1.2971s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k04_s04.py` |  |
| 0.67 | 4/6 | 5 | 0.1183s | 0.0136s | 1 | 8 | yes | 0.1104s | 0.1284s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k04_s05.py` |  |
| 0.67 | 4/6 | 6 | 0.1926s | 0.0186s | 1 | 8 | yes | 0.1836s | 0.2065s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k04_s06.py` |  |
| 0.67 | 4/6 | 7 | 1.2296s | 0.1071s | 1 | 8 | yes | 1.1647s | 1.3012s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k04_s07.py` |  |
| 0.67 | 4/6 | 8 | 1.2413s | 0.0361s | 1 | 8 | yes | 1.2191s | 1.2656s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k04_s08.py` |  |
| 0.67 | 4/6 | 9 | 1.2617s | 0.0718s | 1 | 8 | yes | 1.2173s | 1.3103s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k04_s09.py` |  |
| 0.67 | 4/6 | 10 | 0.1846s | 0.0147s | 1 | 8 | yes | 0.1748s | 0.1938s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k04_s10.py` |  |
| 0.67 | 4/6 | 11 | 1.2772s | 0.0650s | 1 | 8 | yes | 1.2345s | 1.3174s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k04_s11.py` |  |
| 0.67 | 4/6 | 12 | 1.2727s | 0.0998s | 1 | 8 | yes | 1.2070s | 1.3354s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k04_s12.py` |  |
| 0.67 | 4/6 | 13 | 1.2412s | 0.0608s | 1 | 8 | yes | 1.2097s | 1.2862s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k04_s13.py` |  |
| 0.67 | 4/6 | 14 | 1.2779s | 0.0854s | 1 | 8 | yes | 1.2214s | 1.3315s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k04_s14.py` |  |
| 0.67 | 4/6 | 15 | 0.1971s | 0.0321s | 3 | 24 | yes | 0.1854s | 0.2104s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k04_s15.py` |  |
| 0.83 | 5/6 | 1 | 1.2318s | 0.0494s | 1 | 8 | yes | 1.1989s | 1.2629s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k05_s01.py` |  |
| 0.83 | 5/6 | 2 | 1.2583s | 0.0630s | 1 | 8 | yes | 1.2149s | 1.2967s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k05_s02.py` |  |
| 0.83 | 5/6 | 3 | 0.1928s | 0.0092s | 1 | 8 | yes | 0.1883s | 0.1995s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k05_s03.py` |  |
| 0.83 | 5/6 | 4 | 1.3070s | 0.0358s | 1 | 8 | yes | 1.2862s | 1.3323s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k05_s04.py` |  |
| 0.83 | 5/6 | 5 | 1.3393s | 0.0853s | 1 | 8 | yes | 1.2904s | 1.3984s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k05_s05.py` |  |
| 0.83 | 5/6 | 6 | 1.2238s | 0.0929s | 1 | 8 | yes | 1.1651s | 1.2835s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k05_s06.py` |  |
| 1.00 | 6/6 | 1 | 1.2979s | 0.1034s | 1 | 8 | yes | 1.2323s | 1.3657s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_k06_s01.py` |  |

## call_method_slots/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.1292s | 0.1292s | 0.1292s | 3.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.1292s | 0.0258s | 3 | 24 | yes | 0.1193s | 0.1398s | `static-python-perf/Benchmark/call_method_slots/untyped/main.py` |  |

## call_simple/advanced

- Detypable targets: `6`
- Total runs: `64`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.0732s | 0.0732s | 0.0732s | 2.0 | yes | ok |
| 0.17 | 1/6 | 6 | 0.0961s | 0.0733s | 0.1555s | 1.7 | yes | ok |
| 0.33 | 2/6 | 15 | 0.1235s | 0.0701s | 0.1868s | 1.3 | yes | ok |
| 0.50 | 3/6 | 20 | 0.1516s | 0.0929s | 0.2176s | 1.4 | yes | ok |
| 0.67 | 4/6 | 15 | 0.1734s | 0.1117s | 0.2296s | 1.1 | yes | ok |
| 0.83 | 5/6 | 6 | 0.1971s | 0.1390s | 0.2271s | 1.2 | yes | ok |
| 1.00 | 6/6 | 1 | 0.2265s | 0.2265s | 0.2265s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.0732s | 0.0147s | 2 | 16 | yes | 0.0666s | 0.0803s | `detyped_files/call_simple/advanced/proportion_sweep/main_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 0.0915s | 0.0062s | 1 | 8 | yes | 0.0876s | 0.0956s | `detyped_files/call_simple/advanced/proportion_sweep/main_k01_s01.py` |  |
| 0.17 | 1/6 | 2 | 0.0733s | 0.0140s | 3 | 24 | yes | 0.0682s | 0.0792s | `detyped_files/call_simple/advanced/proportion_sweep/main_k01_s02.py` |  |
| 0.17 | 1/6 | 3 | 0.1555s | 0.0113s | 1 | 8 | yes | 0.1473s | 0.1617s | `detyped_files/call_simple/advanced/proportion_sweep/main_k01_s03.py` |  |
| 0.17 | 1/6 | 4 | 0.0874s | 0.0079s | 1 | 8 | yes | 0.0823s | 0.0931s | `detyped_files/call_simple/advanced/proportion_sweep/main_k01_s04.py` |  |
| 0.17 | 1/6 | 5 | 0.0946s | 0.0164s | 2 | 16 | yes | 0.0893s | 0.1035s | `detyped_files/call_simple/advanced/proportion_sweep/main_k01_s05.py` |  |
| 0.17 | 1/6 | 6 | 0.0740s | 0.0107s | 2 | 16 | yes | 0.0695s | 0.0795s | `detyped_files/call_simple/advanced/proportion_sweep/main_k01_s06.py` |  |
| 0.33 | 2/6 | 1 | 0.0919s | 0.0111s | 1 | 8 | yes | 0.0856s | 0.1001s | `detyped_files/call_simple/advanced/proportion_sweep/main_k02_s01.py` |  |
| 0.33 | 2/6 | 2 | 0.0923s | 0.0161s | 2 | 16 | yes | 0.0867s | 0.1010s | `detyped_files/call_simple/advanced/proportion_sweep/main_k02_s02.py` |  |
| 0.33 | 2/6 | 3 | 0.1053s | 0.0059s | 1 | 8 | yes | 0.1009s | 0.1079s | `detyped_files/call_simple/advanced/proportion_sweep/main_k02_s03.py` |  |
| 0.33 | 2/6 | 4 | 0.0928s | 0.0109s | 1 | 8 | yes | 0.0874s | 0.1007s | `detyped_files/call_simple/advanced/proportion_sweep/main_k02_s04.py` |  |
| 0.33 | 2/6 | 5 | 0.1002s | 0.0174s | 2 | 16 | yes | 0.0929s | 0.1092s | `detyped_files/call_simple/advanced/proportion_sweep/main_k02_s05.py` |  |
| 0.33 | 2/6 | 6 | 0.1149s | 0.0141s | 1 | 8 | yes | 0.1072s | 0.1248s | `detyped_files/call_simple/advanced/proportion_sweep/main_k02_s06.py` |  |
| 0.33 | 2/6 | 7 | 0.1792s | 0.0084s | 1 | 8 | yes | 0.1740s | 0.1849s | `detyped_files/call_simple/advanced/proportion_sweep/main_k02_s07.py` |  |
| 0.33 | 2/6 | 8 | 0.1694s | 0.0174s | 1 | 8 | yes | 0.1587s | 0.1815s | `detyped_files/call_simple/advanced/proportion_sweep/main_k02_s08.py` |  |
| 0.33 | 2/6 | 9 | 0.1556s | 0.0067s | 1 | 8 | yes | 0.1507s | 0.1592s | `detyped_files/call_simple/advanced/proportion_sweep/main_k02_s09.py` |  |
| 0.33 | 2/6 | 10 | 0.1178s | 0.0093s | 1 | 8 | yes | 0.1124s | 0.1244s | `detyped_files/call_simple/advanced/proportion_sweep/main_k02_s10.py` |  |
| 0.33 | 2/6 | 11 | 0.1854s | 0.0192s | 1 | 8 | yes | 0.1723s | 0.1975s | `detyped_files/call_simple/advanced/proportion_sweep/main_k02_s11.py` |  |
| 0.33 | 2/6 | 12 | 0.0983s | 0.0172s | 2 | 16 | yes | 0.0907s | 0.1069s | `detyped_files/call_simple/advanced/proportion_sweep/main_k02_s12.py` |  |
| 0.33 | 2/6 | 13 | 0.1868s | 0.0151s | 1 | 8 | yes | 0.1783s | 0.1974s | `detyped_files/call_simple/advanced/proportion_sweep/main_k02_s13.py` |  |
| 0.33 | 2/6 | 14 | 0.0701s | 0.0107s | 2 | 16 | yes | 0.0666s | 0.0759s | `detyped_files/call_simple/advanced/proportion_sweep/main_k02_s14.py` |  |
| 0.33 | 2/6 | 15 | 0.0929s | 0.0096s | 1 | 8 | yes | 0.0875s | 0.0998s | `detyped_files/call_simple/advanced/proportion_sweep/main_k02_s15.py` |  |
| 0.50 | 3/6 | 1 | 0.1189s | 0.0146s | 1 | 8 | yes | 0.1112s | 0.1295s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s01.py` |  |
| 0.50 | 3/6 | 2 | 0.1818s | 0.0137s | 1 | 8 | yes | 0.1734s | 0.1911s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s02.py` |  |
| 0.50 | 3/6 | 3 | 0.2176s | 0.0338s | 2 | 16 | yes | 0.2029s | 0.2346s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s03.py` |  |
| 0.50 | 3/6 | 4 | 0.0929s | 0.0072s | 1 | 8 | yes | 0.0885s | 0.0978s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s04.py` |  |
| 0.50 | 3/6 | 5 | 0.1196s | 0.0107s | 1 | 8 | yes | 0.1128s | 0.1266s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s05.py` |  |
| 0.50 | 3/6 | 6 | 0.1364s | 0.0180s | 1 | 8 | yes | 0.1293s | 0.1493s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s06.py` |  |
| 0.50 | 3/6 | 7 | 0.1937s | 0.0359s | 3 | 24 | yes | 0.1815s | 0.2090s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s07.py` |  |
| 0.50 | 3/6 | 8 | 0.1923s | 0.0125s | 1 | 8 | yes | 0.1842s | 0.2003s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s08.py` |  |
| 0.50 | 3/6 | 9 | 0.1787s | 0.0046s | 1 | 8 | yes | 0.1757s | 0.1816s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s09.py` |  |
| 0.50 | 3/6 | 10 | 0.1125s | 0.0075s | 1 | 8 | yes | 0.1080s | 0.1175s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s10.py` |  |
| 0.50 | 3/6 | 11 | 0.2082s | 0.0227s | 1 | 8 | yes | 0.1952s | 0.2236s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s11.py` |  |
| 0.50 | 3/6 | 12 | 0.0934s | 0.0094s | 1 | 8 | yes | 0.0889s | 0.1004s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s12.py` |  |
| 0.50 | 3/6 | 13 | 0.1890s | 0.0278s | 2 | 16 | yes | 0.1785s | 0.2041s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s13.py` |  |
| 0.50 | 3/6 | 14 | 0.1833s | 0.0309s | 3 | 24 | yes | 0.1725s | 0.1962s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s14.py` |  |
| 0.50 | 3/6 | 15 | 0.2062s | 0.0220s | 1 | 8 | yes | 0.1957s | 0.2219s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s15.py` |  |
| 0.50 | 3/6 | 16 | 0.0934s | 0.0120s | 1 | 8 | yes | 0.0869s | 0.1019s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s16.py` |  |
| 0.50 | 3/6 | 17 | 0.1133s | 0.0139s | 1 | 8 | yes | 0.1058s | 0.1234s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s17.py` |  |
| 0.50 | 3/6 | 18 | 0.1641s | 0.0120s | 1 | 8 | yes | 0.1567s | 0.1723s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s18.py` |  |
| 0.50 | 3/6 | 19 | 0.1225s | 0.0176s | 2 | 16 | yes | 0.1147s | 0.1314s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s19.py` |  |
| 0.50 | 3/6 | 20 | 0.1148s | 0.0077s | 1 | 8 | yes | 0.1104s | 0.1203s | `detyped_files/call_simple/advanced/proportion_sweep/main_k03_s20.py` |  |
| 0.67 | 4/6 | 1 | 0.2028s | 0.0282s | 1 | 8 | yes | 0.1853s | 0.2217s | `detyped_files/call_simple/advanced/proportion_sweep/main_k04_s01.py` |  |
| 0.67 | 4/6 | 2 | 0.2086s | 0.0225s | 1 | 8 | yes | 0.1938s | 0.2228s | `detyped_files/call_simple/advanced/proportion_sweep/main_k04_s02.py` |  |
| 0.67 | 4/6 | 3 | 0.1924s | 0.0093s | 1 | 8 | yes | 0.1861s | 0.1981s | `detyped_files/call_simple/advanced/proportion_sweep/main_k04_s03.py` |  |
| 0.67 | 4/6 | 4 | 0.2145s | 0.0276s | 1 | 8 | yes | 0.1974s | 0.2332s | `detyped_files/call_simple/advanced/proportion_sweep/main_k04_s04.py` |  |
| 0.67 | 4/6 | 5 | 0.1117s | 0.0129s | 1 | 8 | yes | 0.1030s | 0.1193s | `detyped_files/call_simple/advanced/proportion_sweep/main_k04_s05.py` |  |
| 0.67 | 4/6 | 6 | 0.1196s | 0.0232s | 2 | 16 | yes | 0.1097s | 0.1314s | `detyped_files/call_simple/advanced/proportion_sweep/main_k04_s06.py` |  |
| 0.67 | 4/6 | 7 | 0.1684s | 0.0149s | 1 | 8 | yes | 0.1582s | 0.1768s | `detyped_files/call_simple/advanced/proportion_sweep/main_k04_s07.py` |  |
| 0.67 | 4/6 | 8 | 0.1379s | 0.0108s | 1 | 8 | yes | 0.1320s | 0.1458s | `detyped_files/call_simple/advanced/proportion_sweep/main_k04_s08.py` |  |
| 0.67 | 4/6 | 9 | 0.2296s | 0.0197s | 1 | 8 | yes | 0.2165s | 0.2424s | `detyped_files/call_simple/advanced/proportion_sweep/main_k04_s09.py` |  |
| 0.67 | 4/6 | 10 | 0.1132s | 0.0132s | 1 | 8 | yes | 0.1061s | 0.1227s | `detyped_files/call_simple/advanced/proportion_sweep/main_k04_s10.py` |  |
| 0.67 | 4/6 | 11 | 0.2041s | 0.0065s | 1 | 8 | yes | 0.2000s | 0.2083s | `detyped_files/call_simple/advanced/proportion_sweep/main_k04_s11.py` |  |
| 0.67 | 4/6 | 12 | 0.1856s | 0.0086s | 1 | 8 | yes | 0.1802s | 0.1914s | `detyped_files/call_simple/advanced/proportion_sweep/main_k04_s12.py` |  |
| 0.67 | 4/6 | 13 | 0.1790s | 0.0225s | 1 | 8 | yes | 0.1643s | 0.1934s | `detyped_files/call_simple/advanced/proportion_sweep/main_k04_s13.py` |  |
| 0.67 | 4/6 | 14 | 0.1981s | 0.0098s | 1 | 8 | yes | 0.1929s | 0.2050s | `detyped_files/call_simple/advanced/proportion_sweep/main_k04_s14.py` |  |
| 0.67 | 4/6 | 15 | 0.1361s | 0.0183s | 1 | 8 | yes | 0.1250s | 0.1487s | `detyped_files/call_simple/advanced/proportion_sweep/main_k04_s15.py` |  |
| 0.83 | 5/6 | 1 | 0.1390s | 0.0179s | 1 | 8 | yes | 0.1289s | 0.1519s | `detyped_files/call_simple/advanced/proportion_sweep/main_k05_s01.py` |  |
| 0.83 | 5/6 | 2 | 0.2179s | 0.0027s | 1 | 8 | yes | 0.2162s | 0.2196s | `detyped_files/call_simple/advanced/proportion_sweep/main_k05_s02.py` |  |
| 0.83 | 5/6 | 3 | 0.2038s | 0.0284s | 2 | 16 | yes | 0.1931s | 0.2194s | `detyped_files/call_simple/advanced/proportion_sweep/main_k05_s03.py` |  |
| 0.83 | 5/6 | 4 | 0.2000s | 0.0101s | 1 | 8 | yes | 0.1925s | 0.2052s | `detyped_files/call_simple/advanced/proportion_sweep/main_k05_s04.py` |  |
| 0.83 | 5/6 | 5 | 0.2271s | 0.0168s | 1 | 8 | yes | 0.2174s | 0.2385s | `detyped_files/call_simple/advanced/proportion_sweep/main_k05_s05.py` |  |
| 0.83 | 5/6 | 6 | 0.1949s | 0.0183s | 1 | 8 | yes | 0.1815s | 0.2053s | `detyped_files/call_simple/advanced/proportion_sweep/main_k05_s06.py` |  |
| 1.00 | 6/6 | 1 | 0.2265s | 0.0143s | 1 | 8 | yes | 0.2183s | 0.2363s | `detyped_files/call_simple/advanced/proportion_sweep/main_k06_s01.py` |  |

## call_simple/shallow

- Detypable targets: `6`
- Total runs: `64`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.0676s | 0.0676s | 0.0676s | 1.0 | yes | ok |
| 0.17 | 1/6 | 6 | 0.0712s | 0.0659s | 0.0746s | 1.5 | yes | ok |
| 0.33 | 2/6 | 15 | 0.0717s | 0.0666s | 0.0754s | 1.5 | yes | ok |
| 0.50 | 3/6 | 20 | 0.0711s | 0.0665s | 0.0748s | 1.4 | yes | ok |
| 0.67 | 4/6 | 15 | 0.0728s | 0.0651s | 0.0873s | 1.6 | yes | ok |
| 0.83 | 5/6 | 6 | 0.0719s | 0.0689s | 0.0742s | 1.2 | yes | ok |
| 1.00 | 6/6 | 1 | 0.0680s | 0.0680s | 0.0680s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.0676s | 0.0020s | 1 | 8 | yes | 0.0664s | 0.0689s | `detyped_files/call_simple/shallow/proportion_sweep/main_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 0.0722s | 0.0097s | 2 | 16 | yes | 0.0679s | 0.0772s | `detyped_files/call_simple/shallow/proportion_sweep/main_k01_s01.py` |  |
| 0.17 | 1/6 | 2 | 0.0739s | 0.0093s | 1 | 8 | yes | 0.0684s | 0.0802s | `detyped_files/call_simple/shallow/proportion_sweep/main_k01_s02.py` |  |
| 0.17 | 1/6 | 3 | 0.0659s | 0.0007s | 1 | 8 | yes | 0.0655s | 0.0664s | `detyped_files/call_simple/shallow/proportion_sweep/main_k01_s03.py` |  |
| 0.17 | 1/6 | 4 | 0.0683s | 0.0053s | 1 | 8 | yes | 0.0657s | 0.0722s | `detyped_files/call_simple/shallow/proportion_sweep/main_k01_s04.py` |  |
| 0.17 | 1/6 | 5 | 0.0746s | 0.0137s | 2 | 16 | yes | 0.0693s | 0.0818s | `detyped_files/call_simple/shallow/proportion_sweep/main_k01_s05.py` |  |
| 0.17 | 1/6 | 6 | 0.0723s | 0.0117s | 2 | 16 | yes | 0.0676s | 0.0784s | `detyped_files/call_simple/shallow/proportion_sweep/main_k01_s06.py` |  |
| 0.33 | 2/6 | 1 | 0.0673s | 0.0016s | 1 | 8 | yes | 0.0663s | 0.0683s | `detyped_files/call_simple/shallow/proportion_sweep/main_k02_s01.py` |  |
| 0.33 | 2/6 | 2 | 0.0717s | 0.0098s | 1 | 8 | yes | 0.0667s | 0.0787s | `detyped_files/call_simple/shallow/proportion_sweep/main_k02_s02.py` |  |
| 0.33 | 2/6 | 3 | 0.0742s | 0.0084s | 1 | 8 | yes | 0.0689s | 0.0798s | `detyped_files/call_simple/shallow/proportion_sweep/main_k02_s03.py` |  |
| 0.33 | 2/6 | 4 | 0.0711s | 0.0096s | 1 | 8 | yes | 0.0669s | 0.0781s | `detyped_files/call_simple/shallow/proportion_sweep/main_k02_s04.py` |  |
| 0.33 | 2/6 | 5 | 0.0754s | 0.0092s | 1 | 8 | yes | 0.0698s | 0.0816s | `detyped_files/call_simple/shallow/proportion_sweep/main_k02_s05.py` |  |
| 0.33 | 2/6 | 6 | 0.0666s | 0.0021s | 1 | 8 | yes | 0.0653s | 0.0680s | `detyped_files/call_simple/shallow/proportion_sweep/main_k02_s06.py` |  |
| 0.33 | 2/6 | 7 | 0.0736s | 0.0122s | 2 | 16 | yes | 0.0687s | 0.0800s | `detyped_files/call_simple/shallow/proportion_sweep/main_k02_s07.py` |  |
| 0.33 | 2/6 | 8 | 0.0703s | 0.0099s | 2 | 16 | yes | 0.0657s | 0.0751s | `detyped_files/call_simple/shallow/proportion_sweep/main_k02_s08.py` |  |
| 0.33 | 2/6 | 9 | 0.0729s | 0.0091s | 2 | 16 | yes | 0.0691s | 0.0778s | `detyped_files/call_simple/shallow/proportion_sweep/main_k02_s09.py` |  |
| 0.33 | 2/6 | 10 | 0.0722s | 0.0109s | 2 | 16 | yes | 0.0674s | 0.0777s | `detyped_files/call_simple/shallow/proportion_sweep/main_k02_s10.py` |  |
| 0.33 | 2/6 | 11 | 0.0699s | 0.0103s | 2 | 16 | yes | 0.0655s | 0.0751s | `detyped_files/call_simple/shallow/proportion_sweep/main_k02_s11.py` |  |
| 0.33 | 2/6 | 12 | 0.0714s | 0.0087s | 1 | 8 | yes | 0.0664s | 0.0774s | `detyped_files/call_simple/shallow/proportion_sweep/main_k02_s12.py` |  |
| 0.33 | 2/6 | 13 | 0.0735s | 0.0113s | 2 | 16 | yes | 0.0687s | 0.0793s | `detyped_files/call_simple/shallow/proportion_sweep/main_k02_s13.py` |  |
| 0.33 | 2/6 | 14 | 0.0709s | 0.0070s | 1 | 8 | yes | 0.0676s | 0.0760s | `detyped_files/call_simple/shallow/proportion_sweep/main_k02_s14.py` |  |
| 0.33 | 2/6 | 15 | 0.0745s | 0.0134s | 2 | 16 | yes | 0.0693s | 0.0816s | `detyped_files/call_simple/shallow/proportion_sweep/main_k02_s15.py` |  |
| 0.50 | 3/6 | 1 | 0.0727s | 0.0124s | 2 | 16 | yes | 0.0678s | 0.0793s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s01.py` |  |
| 0.50 | 3/6 | 2 | 0.0741s | 0.0130s | 2 | 16 | yes | 0.0685s | 0.0807s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s02.py` |  |
| 0.50 | 3/6 | 3 | 0.0748s | 0.0076s | 1 | 8 | yes | 0.0700s | 0.0798s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s03.py` |  |
| 0.50 | 3/6 | 4 | 0.0708s | 0.0061s | 1 | 8 | yes | 0.0674s | 0.0751s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s04.py` |  |
| 0.50 | 3/6 | 5 | 0.0731s | 0.0082s | 1 | 8 | yes | 0.0682s | 0.0788s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s05.py` |  |
| 0.50 | 3/6 | 6 | 0.0691s | 0.0061s | 1 | 8 | yes | 0.0662s | 0.0735s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s06.py` |  |
| 0.50 | 3/6 | 7 | 0.0677s | 0.0020s | 1 | 8 | yes | 0.0665s | 0.0691s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s07.py` |  |
| 0.50 | 3/6 | 8 | 0.0665s | 0.0016s | 1 | 8 | yes | 0.0657s | 0.0677s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s08.py` |  |
| 0.50 | 3/6 | 9 | 0.0714s | 0.0096s | 1 | 8 | yes | 0.0666s | 0.0784s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s09.py` |  |
| 0.50 | 3/6 | 10 | 0.0716s | 0.0100s | 1 | 8 | yes | 0.0660s | 0.0784s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s10.py` |  |
| 0.50 | 3/6 | 11 | 0.0695s | 0.0037s | 1 | 8 | yes | 0.0673s | 0.0721s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s11.py` |  |
| 0.50 | 3/6 | 12 | 0.0700s | 0.0073s | 1 | 8 | yes | 0.0662s | 0.0750s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s12.py` |  |
| 0.50 | 3/6 | 13 | 0.0704s | 0.0145s | 3 | 24 | yes | 0.0657s | 0.0768s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s13.py` |  |
| 0.50 | 3/6 | 14 | 0.0713s | 0.0060s | 1 | 8 | yes | 0.0680s | 0.0756s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s14.py` |  |
| 0.50 | 3/6 | 15 | 0.0746s | 0.0110s | 2 | 16 | yes | 0.0697s | 0.0802s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s15.py` |  |
| 0.50 | 3/6 | 16 | 0.0726s | 0.0084s | 1 | 8 | yes | 0.0684s | 0.0789s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s16.py` |  |
| 0.50 | 3/6 | 17 | 0.0738s | 0.0130s | 2 | 16 | yes | 0.0679s | 0.0803s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s17.py` |  |
| 0.50 | 3/6 | 18 | 0.0677s | 0.0032s | 1 | 8 | yes | 0.0658s | 0.0700s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s18.py` |  |
| 0.50 | 3/6 | 19 | 0.0701s | 0.0095s | 2 | 16 | yes | 0.0670s | 0.0753s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s19.py` |  |
| 0.50 | 3/6 | 20 | 0.0696s | 0.0059s | 1 | 8 | yes | 0.0662s | 0.0736s | `detyped_files/call_simple/shallow/proportion_sweep/main_k03_s20.py` |  |
| 0.67 | 4/6 | 1 | 0.0755s | 0.0167s | 3 | 24 | yes | 0.0696s | 0.0825s | `detyped_files/call_simple/shallow/proportion_sweep/main_k04_s01.py` |  |
| 0.67 | 4/6 | 2 | 0.0756s | 0.0145s | 2 | 16 | yes | 0.0690s | 0.0826s | `detyped_files/call_simple/shallow/proportion_sweep/main_k04_s02.py` |  |
| 0.67 | 4/6 | 3 | 0.0698s | 0.0079s | 1 | 8 | yes | 0.0655s | 0.0754s | `detyped_files/call_simple/shallow/proportion_sweep/main_k04_s03.py` |  |
| 0.67 | 4/6 | 4 | 0.0651s | 0.0052s | 1 | 8 | yes | 0.0613s | 0.0679s | `detyped_files/call_simple/shallow/proportion_sweep/main_k04_s04.py` |  |
| 0.67 | 4/6 | 5 | 0.0754s | 0.0130s | 2 | 16 | yes | 0.0701s | 0.0822s | `detyped_files/call_simple/shallow/proportion_sweep/main_k04_s05.py` |  |
| 0.67 | 4/6 | 6 | 0.0698s | 0.0069s | 1 | 8 | yes | 0.0660s | 0.0748s | `detyped_files/call_simple/shallow/proportion_sweep/main_k04_s06.py` |  |
| 0.67 | 4/6 | 7 | 0.0729s | 0.0130s | 2 | 16 | yes | 0.0673s | 0.0797s | `detyped_files/call_simple/shallow/proportion_sweep/main_k04_s07.py` |  |
| 0.67 | 4/6 | 8 | 0.0742s | 0.0089s | 1 | 8 | yes | 0.0687s | 0.0801s | `detyped_files/call_simple/shallow/proportion_sweep/main_k04_s08.py` |  |
| 0.67 | 4/6 | 9 | 0.0873s | 0.0173s | 2 | 16 | yes | 0.0794s | 0.0956s | `detyped_files/call_simple/shallow/proportion_sweep/main_k04_s09.py` |  |
| 0.67 | 4/6 | 10 | 0.0753s | 0.0140s | 3 | 24 | yes | 0.0702s | 0.0809s | `detyped_files/call_simple/shallow/proportion_sweep/main_k04_s10.py` |  |
| 0.67 | 4/6 | 11 | 0.0707s | 0.0085s | 2 | 16 | yes | 0.0671s | 0.0752s | `detyped_files/call_simple/shallow/proportion_sweep/main_k04_s11.py` |  |
| 0.67 | 4/6 | 12 | 0.0702s | 0.0053s | 1 | 8 | yes | 0.0670s | 0.0739s | `detyped_files/call_simple/shallow/proportion_sweep/main_k04_s12.py` |  |
| 0.67 | 4/6 | 13 | 0.0697s | 0.0093s | 1 | 8 | yes | 0.0658s | 0.0764s | `detyped_files/call_simple/shallow/proportion_sweep/main_k04_s13.py` |  |
| 0.67 | 4/6 | 14 | 0.0729s | 0.0102s | 1 | 8 | yes | 0.0669s | 0.0801s | `detyped_files/call_simple/shallow/proportion_sweep/main_k04_s14.py` |  |
| 0.67 | 4/6 | 15 | 0.0686s | 0.0032s | 1 | 8 | yes | 0.0666s | 0.0708s | `detyped_files/call_simple/shallow/proportion_sweep/main_k04_s15.py` |  |
| 0.83 | 5/6 | 1 | 0.0709s | 0.0090s | 1 | 8 | yes | 0.0656s | 0.0774s | `detyped_files/call_simple/shallow/proportion_sweep/main_k05_s01.py` |  |
| 0.83 | 5/6 | 2 | 0.0711s | 0.0063s | 1 | 8 | yes | 0.0673s | 0.0755s | `detyped_files/call_simple/shallow/proportion_sweep/main_k05_s02.py` |  |
| 0.83 | 5/6 | 3 | 0.0723s | 0.0116s | 2 | 16 | yes | 0.0673s | 0.0781s | `detyped_files/call_simple/shallow/proportion_sweep/main_k05_s03.py` |  |
| 0.83 | 5/6 | 4 | 0.0740s | 0.0089s | 1 | 8 | yes | 0.0690s | 0.0802s | `detyped_files/call_simple/shallow/proportion_sweep/main_k05_s04.py` |  |
| 0.83 | 5/6 | 5 | 0.0742s | 0.0106s | 1 | 8 | yes | 0.0679s | 0.0815s | `detyped_files/call_simple/shallow/proportion_sweep/main_k05_s05.py` |  |
| 0.83 | 5/6 | 6 | 0.0689s | 0.0026s | 1 | 8 | yes | 0.0673s | 0.0706s | `detyped_files/call_simple/shallow/proportion_sweep/main_k05_s06.py` |  |
| 1.00 | 6/6 | 1 | 0.0680s | 0.0029s | 1 | 8 | yes | 0.0663s | 0.0700s | `detyped_files/call_simple/shallow/proportion_sweep/main_k06_s01.py` |  |

## call_simple/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.0756s | 0.0756s | 0.0756s | 2.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.0756s | 0.0141s | 2 | 16 | yes | 0.0696s | 0.0830s | `static-python-perf/Benchmark/call_simple/untyped/main.py` |  |

## chaos/advanced

- Detypable targets: `5`
- Total runs: `32`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/5 | 1 | 0.3075s | 0.3075s | 0.3075s | 1.0 | yes | ok |
| 0.20 | 1/5 | 5 | 0.3589s | 0.3257s | 0.4473s | 1.0 | yes | ok |
| 0.40 | 2/5 | 10 | 0.3732s | 0.3141s | 0.4534s | 1.0 | yes | ok |
| 0.60 | 3/5 | 10 | 0.4007s | 0.3252s | 0.4670s | 1.0 | yes | ok |
| 0.80 | 4/5 | 5 | 0.4304s | 0.3419s | 0.4622s | 1.0 | yes | ok |
| 1.00 | 5/5 | 1 | 0.4480s | 0.4480s | 0.4480s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/5 | 1 | 0.3075s | 0.0148s | 1 | 8 | yes | 0.2966s | 0.3161s | `detyped_files/chaos/advanced/proportion_sweep/main_k00_s01.py` |  |
| 0.20 | 1/5 | 1 | 0.3461s | 0.0489s | 1 | 8 | yes | 0.3169s | 0.3807s | `detyped_files/chaos/advanced/proportion_sweep/main_k01_s01.py` |  |
| 0.20 | 1/5 | 2 | 0.4473s | 0.0376s | 1 | 8 | yes | 0.4223s | 0.4713s | `detyped_files/chaos/advanced/proportion_sweep/main_k01_s02.py` |  |
| 0.20 | 1/5 | 3 | 0.3383s | 0.0434s | 1 | 8 | yes | 0.3138s | 0.3691s | `detyped_files/chaos/advanced/proportion_sweep/main_k01_s03.py` |  |
| 0.20 | 1/5 | 4 | 0.3257s | 0.0257s | 1 | 8 | yes | 0.3097s | 0.3426s | `detyped_files/chaos/advanced/proportion_sweep/main_k01_s04.py` |  |
| 0.20 | 1/5 | 5 | 0.3370s | 0.0249s | 1 | 8 | yes | 0.3232s | 0.3550s | `detyped_files/chaos/advanced/proportion_sweep/main_k01_s05.py` |  |
| 0.40 | 2/5 | 1 | 0.3141s | 0.0207s | 1 | 8 | yes | 0.2994s | 0.3250s | `detyped_files/chaos/advanced/proportion_sweep/main_k02_s01.py` |  |
| 0.40 | 2/5 | 2 | 0.4292s | 0.0226s | 1 | 8 | yes | 0.4133s | 0.4411s | `detyped_files/chaos/advanced/proportion_sweep/main_k02_s02.py` |  |
| 0.40 | 2/5 | 3 | 0.3181s | 0.0263s | 1 | 8 | yes | 0.2992s | 0.3340s | `detyped_files/chaos/advanced/proportion_sweep/main_k02_s03.py` |  |
| 0.40 | 2/5 | 4 | 0.4403s | 0.0253s | 1 | 8 | yes | 0.4224s | 0.4547s | `detyped_files/chaos/advanced/proportion_sweep/main_k02_s04.py` |  |
| 0.40 | 2/5 | 5 | 0.4533s | 0.0492s | 1 | 8 | yes | 0.4248s | 0.4892s | `detyped_files/chaos/advanced/proportion_sweep/main_k02_s05.py` |  |
| 0.40 | 2/5 | 6 | 0.3184s | 0.0326s | 1 | 8 | yes | 0.2960s | 0.3380s | `detyped_files/chaos/advanced/proportion_sweep/main_k02_s06.py` |  |
| 0.40 | 2/5 | 7 | 0.3267s | 0.0379s | 1 | 8 | yes | 0.3012s | 0.3497s | `detyped_files/chaos/advanced/proportion_sweep/main_k02_s07.py` |  |
| 0.40 | 2/5 | 8 | 0.3395s | 0.0099s | 1 | 8 | yes | 0.3333s | 0.3463s | `detyped_files/chaos/advanced/proportion_sweep/main_k02_s08.py` |  |
| 0.40 | 2/5 | 9 | 0.3388s | 0.0208s | 1 | 8 | yes | 0.3249s | 0.3523s | `detyped_files/chaos/advanced/proportion_sweep/main_k02_s09.py` |  |
| 0.40 | 2/5 | 10 | 0.4534s | 0.0261s | 1 | 8 | yes | 0.4348s | 0.4682s | `detyped_files/chaos/advanced/proportion_sweep/main_k02_s10.py` |  |
| 0.60 | 3/5 | 1 | 0.4601s | 0.0151s | 1 | 8 | yes | 0.4513s | 0.4707s | `detyped_files/chaos/advanced/proportion_sweep/main_k03_s01.py` |  |
| 0.60 | 3/5 | 2 | 0.4417s | 0.0345s | 1 | 8 | yes | 0.4171s | 0.4628s | `detyped_files/chaos/advanced/proportion_sweep/main_k03_s02.py` |  |
| 0.60 | 3/5 | 3 | 0.3252s | 0.0264s | 1 | 8 | yes | 0.3060s | 0.3390s | `detyped_files/chaos/advanced/proportion_sweep/main_k03_s03.py` |  |
| 0.60 | 3/5 | 4 | 0.3457s | 0.0287s | 1 | 8 | yes | 0.3269s | 0.3638s | `detyped_files/chaos/advanced/proportion_sweep/main_k03_s04.py` |  |
| 0.60 | 3/5 | 5 | 0.4401s | 0.0280s | 1 | 8 | yes | 0.4198s | 0.4535s | `detyped_files/chaos/advanced/proportion_sweep/main_k03_s05.py` |  |
| 0.60 | 3/5 | 6 | 0.4277s | 0.0390s | 1 | 8 | yes | 0.4019s | 0.4517s | `detyped_files/chaos/advanced/proportion_sweep/main_k03_s06.py` |  |
| 0.60 | 3/5 | 7 | 0.4434s | 0.0374s | 1 | 8 | yes | 0.4164s | 0.4643s | `detyped_files/chaos/advanced/proportion_sweep/main_k03_s07.py` |  |
| 0.60 | 3/5 | 8 | 0.3281s | 0.0372s | 1 | 8 | yes | 0.3055s | 0.3530s | `detyped_files/chaos/advanced/proportion_sweep/main_k03_s08.py` |  |
| 0.60 | 3/5 | 9 | 0.4670s | 0.0131s | 1 | 8 | yes | 0.4579s | 0.4749s | `detyped_files/chaos/advanced/proportion_sweep/main_k03_s09.py` |  |
| 0.60 | 3/5 | 10 | 0.3280s | 0.0118s | 1 | 8 | yes | 0.3195s | 0.3346s | `detyped_files/chaos/advanced/proportion_sweep/main_k03_s10.py` |  |
| 0.80 | 4/5 | 1 | 0.4622s | 0.0435s | 1 | 8 | yes | 0.4341s | 0.4898s | `detyped_files/chaos/advanced/proportion_sweep/main_k04_s01.py` |  |
| 0.80 | 4/5 | 2 | 0.3419s | 0.0118s | 1 | 8 | yes | 0.3353s | 0.3504s | `detyped_files/chaos/advanced/proportion_sweep/main_k04_s02.py` |  |
| 0.80 | 4/5 | 3 | 0.4522s | 0.0313s | 1 | 8 | yes | 0.4291s | 0.4669s | `detyped_files/chaos/advanced/proportion_sweep/main_k04_s03.py` |  |
| 0.80 | 4/5 | 4 | 0.4537s | 0.0344s | 1 | 8 | yes | 0.4294s | 0.4753s | `detyped_files/chaos/advanced/proportion_sweep/main_k04_s04.py` |  |
| 0.80 | 4/5 | 5 | 0.4420s | 0.0400s | 1 | 8 | yes | 0.4140s | 0.4636s | `detyped_files/chaos/advanced/proportion_sweep/main_k04_s05.py` |  |
| 1.00 | 5/5 | 1 | 0.4480s | 0.0237s | 1 | 8 | yes | 0.4310s | 0.4618s | `detyped_files/chaos/advanced/proportion_sweep/main_k05_s01.py` |  |

## chaos/shallow

- Detypable targets: `5`
- Total runs: `32`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/5 | 1 | 0.3231s | 0.3231s | 0.3231s | 1.0 | yes | ok |
| 0.20 | 1/5 | 5 | 0.3518s | 0.2986s | 0.4317s | 1.0 | yes | ok |
| 0.40 | 2/5 | 10 | 0.3866s | 0.3167s | 0.4985s | 1.0 | yes | ok |
| 0.60 | 3/5 | 10 | 0.4258s | 0.3260s | 0.4858s | 1.0 | yes | ok |
| 0.80 | 4/5 | 5 | 0.4570s | 0.3480s | 0.5201s | 1.0 | yes | ok |
| 1.00 | 5/5 | 1 | 0.5185s | 0.5185s | 0.5185s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/5 | 1 | 0.3231s | 0.0087s | 1 | 8 | yes | 0.3172s | 0.3285s | `detyped_files/chaos/shallow/proportion_sweep/main_k00_s01.py` |  |
| 0.20 | 1/5 | 1 | 0.3036s | 0.0386s | 1 | 8 | yes | 0.2785s | 0.3281s | `detyped_files/chaos/shallow/proportion_sweep/main_k01_s01.py` |  |
| 0.20 | 1/5 | 2 | 0.2986s | 0.0260s | 1 | 8 | yes | 0.2813s | 0.3142s | `detyped_files/chaos/shallow/proportion_sweep/main_k01_s02.py` |  |
| 0.20 | 1/5 | 3 | 0.4317s | 0.0370s | 1 | 8 | yes | 0.4082s | 0.4557s | `detyped_files/chaos/shallow/proportion_sweep/main_k01_s03.py` |  |
| 0.20 | 1/5 | 4 | 0.3965s | 0.0285s | 1 | 8 | yes | 0.3788s | 0.4153s | `detyped_files/chaos/shallow/proportion_sweep/main_k01_s04.py` |  |
| 0.20 | 1/5 | 5 | 0.3288s | 0.0344s | 1 | 8 | yes | 0.3082s | 0.3519s | `detyped_files/chaos/shallow/proportion_sweep/main_k01_s05.py` |  |
| 0.40 | 2/5 | 1 | 0.4065s | 0.0383s | 1 | 8 | yes | 0.3818s | 0.4304s | `detyped_files/chaos/shallow/proportion_sweep/main_k02_s01.py` |  |
| 0.40 | 2/5 | 2 | 0.3700s | 0.0306s | 1 | 8 | yes | 0.3481s | 0.3866s | `detyped_files/chaos/shallow/proportion_sweep/main_k02_s02.py` |  |
| 0.40 | 2/5 | 3 | 0.4244s | 0.0417s | 1 | 8 | yes | 0.3970s | 0.4495s | `detyped_files/chaos/shallow/proportion_sweep/main_k02_s03.py` |  |
| 0.40 | 2/5 | 4 | 0.3908s | 0.0512s | 1 | 8 | yes | 0.3589s | 0.4254s | `detyped_files/chaos/shallow/proportion_sweep/main_k02_s04.py` |  |
| 0.40 | 2/5 | 5 | 0.3167s | 0.0212s | 1 | 8 | yes | 0.3020s | 0.3295s | `detyped_files/chaos/shallow/proportion_sweep/main_k02_s05.py` |  |
| 0.40 | 2/5 | 6 | 0.4370s | 0.0358s | 1 | 8 | yes | 0.4134s | 0.4601s | `detyped_files/chaos/shallow/proportion_sweep/main_k02_s06.py` |  |
| 0.40 | 2/5 | 7 | 0.4985s | 0.0334s | 1 | 8 | yes | 0.4736s | 0.5152s | `detyped_files/chaos/shallow/proportion_sweep/main_k02_s07.py` |  |
| 0.40 | 2/5 | 8 | 0.3177s | 0.0335s | 1 | 8 | yes | 0.2940s | 0.3378s | `detyped_files/chaos/shallow/proportion_sweep/main_k02_s08.py` |  |
| 0.40 | 2/5 | 9 | 0.3315s | 0.0323s | 1 | 8 | yes | 0.3092s | 0.3507s | `detyped_files/chaos/shallow/proportion_sweep/main_k02_s09.py` |  |
| 0.40 | 2/5 | 10 | 0.3726s | 0.0459s | 1 | 8 | yes | 0.3442s | 0.4030s | `detyped_files/chaos/shallow/proportion_sweep/main_k02_s10.py` |  |
| 0.60 | 3/5 | 1 | 0.4728s | 0.0469s | 1 | 8 | yes | 0.4411s | 0.5022s | `detyped_files/chaos/shallow/proportion_sweep/main_k03_s01.py` |  |
| 0.60 | 3/5 | 2 | 0.3968s | 0.0568s | 1 | 8 | yes | 0.3622s | 0.4345s | `detyped_files/chaos/shallow/proportion_sweep/main_k03_s02.py` |  |
| 0.60 | 3/5 | 3 | 0.4598s | 0.0574s | 1 | 8 | yes | 0.4232s | 0.4978s | `detyped_files/chaos/shallow/proportion_sweep/main_k03_s03.py` |  |
| 0.60 | 3/5 | 4 | 0.3809s | 0.0390s | 1 | 8 | yes | 0.3535s | 0.4036s | `detyped_files/chaos/shallow/proportion_sweep/main_k03_s04.py` |  |
| 0.60 | 3/5 | 5 | 0.4858s | 0.0536s | 1 | 8 | yes | 0.4515s | 0.5198s | `detyped_files/chaos/shallow/proportion_sweep/main_k03_s05.py` |  |
| 0.60 | 3/5 | 6 | 0.4829s | 0.0408s | 1 | 8 | yes | 0.4532s | 0.5056s | `detyped_files/chaos/shallow/proportion_sweep/main_k03_s06.py` |  |
| 0.60 | 3/5 | 7 | 0.3567s | 0.0391s | 1 | 8 | yes | 0.3307s | 0.3812s | `detyped_files/chaos/shallow/proportion_sweep/main_k03_s07.py` |  |
| 0.60 | 3/5 | 8 | 0.3260s | 0.0314s | 1 | 8 | yes | 0.3046s | 0.3443s | `detyped_files/chaos/shallow/proportion_sweep/main_k03_s08.py` |  |
| 0.60 | 3/5 | 9 | 0.4438s | 0.0105s | 1 | 8 | yes | 0.4375s | 0.4510s | `detyped_files/chaos/shallow/proportion_sweep/main_k03_s09.py` |  |
| 0.60 | 3/5 | 10 | 0.4522s | 0.0342s | 1 | 8 | yes | 0.4309s | 0.4752s | `detyped_files/chaos/shallow/proportion_sweep/main_k03_s10.py` |  |
| 0.80 | 4/5 | 1 | 0.4353s | 0.0355s | 1 | 8 | yes | 0.4120s | 0.4575s | `detyped_files/chaos/shallow/proportion_sweep/main_k04_s01.py` |  |
| 0.80 | 4/5 | 2 | 0.4664s | 0.0480s | 1 | 8 | yes | 0.4350s | 0.4963s | `detyped_files/chaos/shallow/proportion_sweep/main_k04_s02.py` |  |
| 0.80 | 4/5 | 3 | 0.5152s | 0.0428s | 1 | 8 | yes | 0.4933s | 0.5465s | `detyped_files/chaos/shallow/proportion_sweep/main_k04_s03.py` |  |
| 0.80 | 4/5 | 4 | 0.3480s | 0.0273s | 1 | 8 | yes | 0.3317s | 0.3661s | `detyped_files/chaos/shallow/proportion_sweep/main_k04_s04.py` |  |
| 0.80 | 4/5 | 5 | 0.5201s | 0.0304s | 1 | 8 | yes | 0.5003s | 0.5403s | `detyped_files/chaos/shallow/proportion_sweep/main_k04_s05.py` |  |
| 1.00 | 5/5 | 1 | 0.5185s | 0.0226s | 1 | 8 | yes | 0.5040s | 0.5332s | `detyped_files/chaos/shallow/proportion_sweep/main_k05_s01.py` |  |

## chaos/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.3463s | 0.3463s | 0.3463s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.3463s | 0.0214s | 1 | 8 | yes | 0.3328s | 0.3602s | `static-python-perf/Benchmark/chaos/untyped/main.py` |  |

## deltablue/advanced

- Detypable targets: `34`
- Total runs: `662`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/34 | 1 | 1.4081s | 1.4081s | 1.4081s | 1.0 | yes | ok |
| 0.03 | 1/34 | 20 | 1.4527s | 1.3396s | 1.9638s | 1.0 | yes | ok |
| 0.06 | 2/34 | 20 | 1.9263s | 1.3235s | 6.6590s | 1.0 | yes | ok |
| 0.09 | 3/34 | 20 | 2.0032s | 1.3514s | 6.8733s | 1.0 | yes | ok |
| 0.12 | 4/34 | 20 | 2.6317s | 1.3739s | 8.0091s | 1.0 | yes | ok |
| 0.15 | 5/34 | 20 | 2.2033s | 1.3849s | 7.9108s | 1.0 | yes | ok |
| 0.18 | 6/34 | 20 | 2.4562s | 1.3776s | 8.3286s | 1.0 | yes | ok |
| 0.21 | 7/34 | 20 | 3.2347s | 1.4114s | 8.1839s | 1.0 | yes | ok |
| 0.24 | 8/34 | 20 | 3.3779s | 1.4000s | 8.4536s | 1.0 | yes | ok |
| 0.26 | 9/34 | 20 | 3.5675s | 1.4249s | 8.3068s | 1.0 | yes | ok |
| 0.29 | 10/34 | 20 | 2.9833s | 1.3794s | 7.9868s | 1.0 | yes | ok |
| 0.32 | 11/34 | 20 | 3.9219s | 1.4489s | 9.5005s | 1.0 | yes | ok |
| 0.35 | 12/34 | 20 | 4.0664s | 1.5762s | 9.7218s | 1.0 | yes | ok |
| 0.38 | 13/34 | 20 | 4.6555s | 1.4736s | 8.6620s | 1.0 | yes | ok |
| 0.41 | 14/34 | 20 | 5.6781s | 1.5932s | 8.7419s | 1.0 | yes | ok |
| 0.44 | 15/34 | 20 | 4.1750s | 1.5849s | 9.1879s | 1.0 | yes | ok |
| 0.47 | 16/34 | 20 | 4.5891s | 1.5980s | 9.7532s | 1.0 | yes | ok |
| 0.50 | 17/34 | 20 | 6.1825s | 1.7838s | 9.1524s | 1.0 | yes | ok |
| 0.53 | 18/34 | 20 | 5.3631s | 1.6277s | 9.7206s | 1.0 | yes | ok |
| 0.56 | 19/34 | 20 | 4.4342s | 1.6253s | 9.6356s | 1.0 | yes | ok |
| 0.59 | 20/34 | 20 | 7.1398s | 1.5308s | 10.2722s | 1.0 | yes | ok |
| 0.62 | 21/34 | 20 | 6.3488s | 2.1971s | 9.7990s | 1.0 | yes | ok |
| 0.65 | 22/34 | 20 | 7.6584s | 2.2272s | 10.2159s | 1.0 | yes | ok |
| 0.68 | 23/34 | 20 | 6.5739s | 2.0012s | 10.0604s | 1.0 | yes | ok |
| 0.71 | 24/34 | 20 | 7.4346s | 1.5820s | 10.2414s | 1.0 | yes | ok |
| 0.74 | 25/34 | 20 | 7.4055s | 2.1419s | 10.1998s | 1.0 | yes | ok |
| 0.76 | 26/34 | 20 | 8.0533s | 2.3342s | 10.3329s | 1.0 | yes | ok |
| 0.79 | 27/34 | 20 | 7.5891s | 1.8603s | 10.3381s | 1.0 | yes | ok |
| 0.82 | 28/34 | 20 | 8.4916s | 2.1723s | 10.3178s | 1.0 | yes | ok |
| 0.85 | 29/34 | 20 | 8.6980s | 2.6911s | 10.2546s | 1.0 | yes | ok |
| 0.88 | 30/34 | 20 | 9.8481s | 8.9110s | 10.3106s | 1.0 | yes | ok |
| 0.91 | 31/34 | 20 | 9.1816s | 2.3123s | 10.3689s | 1.0 | yes | ok |
| 0.94 | 32/34 | 20 | 9.8103s | 2.7522s | 10.3672s | 1.0 | yes | ok |
| 0.97 | 33/34 | 20 | 10.2106s | 9.8144s | 10.3679s | 1.0 | yes | ok |
| 1.00 | 34/34 | 1 | 10.3295s | 10.3295s | 10.3295s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/34 | 1 | 1.4081s | 0.0489s | 1 | 8 | yes | 1.3817s | 1.4429s | `detyped_files/deltablue/advanced/proportion_sweep/main_k00_s01.py` |  |
| 0.03 | 1/34 | 1 | 1.3817s | 0.0711s | 1 | 8 | yes | 1.3374s | 1.4294s | `detyped_files/deltablue/advanced/proportion_sweep/main_k01_s01.py` |  |
| 0.03 | 1/34 | 2 | 1.3747s | 0.1084s | 1 | 8 | yes | 1.3066s | 1.4457s | `detyped_files/deltablue/advanced/proportion_sweep/main_k01_s02.py` |  |
| 0.03 | 1/34 | 3 | 1.3976s | 0.0583s | 1 | 8 | yes | 1.3603s | 1.4353s | `detyped_files/deltablue/advanced/proportion_sweep/main_k01_s03.py` |  |
| 0.03 | 1/34 | 4 | 1.3835s | 0.0429s | 1 | 8 | yes | 1.3530s | 1.4074s | `detyped_files/deltablue/advanced/proportion_sweep/main_k01_s04.py` |  |
| 0.03 | 1/34 | 5 | 1.4143s | 0.0886s | 1 | 8 | yes | 1.3583s | 1.4713s | `detyped_files/deltablue/advanced/proportion_sweep/main_k01_s05.py` |  |
| 0.03 | 1/34 | 6 | 1.9638s | 0.0937s | 1 | 8 | yes | 1.9160s | 2.0318s | `detyped_files/deltablue/advanced/proportion_sweep/main_k01_s06.py` |  |
| 0.03 | 1/34 | 7 | 1.4392s | 0.1335s | 1 | 8 | yes | 1.3636s | 1.5354s | `detyped_files/deltablue/advanced/proportion_sweep/main_k01_s07.py` |  |
| 0.03 | 1/34 | 8 | 1.3540s | 0.0734s | 1 | 8 | yes | 1.3072s | 1.4017s | `detyped_files/deltablue/advanced/proportion_sweep/main_k01_s08.py` |  |
| 0.03 | 1/34 | 9 | 1.4090s | 0.0786s | 1 | 8 | yes | 1.3572s | 1.4585s | `detyped_files/deltablue/advanced/proportion_sweep/main_k01_s09.py` |  |
| 0.03 | 1/34 | 10 | 1.4001s | 0.0746s | 1 | 8 | yes | 1.3533s | 1.4504s | `detyped_files/deltablue/advanced/proportion_sweep/main_k01_s10.py` |  |
| 0.03 | 1/34 | 11 | 1.8872s | 0.0871s | 1 | 8 | yes | 1.8338s | 1.9450s | `detyped_files/deltablue/advanced/proportion_sweep/main_k01_s11.py` |  |
| 0.03 | 1/34 | 12 | 1.3396s | 0.0548s | 1 | 8 | yes | 1.3017s | 1.3721s | `detyped_files/deltablue/advanced/proportion_sweep/main_k01_s12.py` |  |
| 0.03 | 1/34 | 13 | 1.4383s | 0.0894s | 1 | 8 | yes | 1.3821s | 1.4971s | `detyped_files/deltablue/advanced/proportion_sweep/main_k01_s13.py` |  |
| 0.03 | 1/34 | 14 | 1.3505s | 0.0699s | 1 | 8 | yes | 1.3053s | 1.3948s | `detyped_files/deltablue/advanced/proportion_sweep/main_k01_s14.py` |  |
| 0.03 | 1/34 | 15 | 1.4649s | 0.0852s | 1 | 8 | yes | 1.4107s | 1.5221s | `detyped_files/deltablue/advanced/proportion_sweep/main_k01_s15.py` |  |
| 0.03 | 1/34 | 16 | 1.4516s | 0.0971s | 1 | 8 | yes | 1.3897s | 1.5170s | `detyped_files/deltablue/advanced/proportion_sweep/main_k01_s16.py` |  |
| 0.03 | 1/34 | 17 | 1.4473s | 0.0360s | 1 | 8 | yes | 1.4215s | 1.4669s | `detyped_files/deltablue/advanced/proportion_sweep/main_k01_s17.py` |  |
| 0.03 | 1/34 | 18 | 1.3731s | 0.0168s | 1 | 8 | yes | 1.3621s | 1.3838s | `detyped_files/deltablue/advanced/proportion_sweep/main_k01_s18.py` |  |
| 0.03 | 1/34 | 19 | 1.3602s | 0.0756s | 1 | 8 | yes | 1.3105s | 1.4066s | `detyped_files/deltablue/advanced/proportion_sweep/main_k01_s19.py` |  |
| 0.03 | 1/34 | 20 | 1.4224s | 0.0873s | 1 | 8 | yes | 1.3700s | 1.4810s | `detyped_files/deltablue/advanced/proportion_sweep/main_k01_s20.py` |  |
| 0.06 | 2/34 | 1 | 1.3993s | 0.0697s | 1 | 8 | yes | 1.3584s | 1.4491s | `detyped_files/deltablue/advanced/proportion_sweep/main_k02_s01.py` |  |
| 0.06 | 2/34 | 2 | 1.3727s | 0.0824s | 1 | 8 | yes | 1.3212s | 1.4272s | `detyped_files/deltablue/advanced/proportion_sweep/main_k02_s02.py` |  |
| 0.06 | 2/34 | 3 | 1.4129s | 0.1181s | 1 | 8 | yes | 1.3430s | 1.4942s | `detyped_files/deltablue/advanced/proportion_sweep/main_k02_s03.py` |  |
| 0.06 | 2/34 | 4 | 1.4222s | 0.0727s | 1 | 8 | yes | 1.3770s | 1.4699s | `detyped_files/deltablue/advanced/proportion_sweep/main_k02_s04.py` |  |
| 0.06 | 2/34 | 5 | 1.4144s | 0.1294s | 1 | 8 | yes | 1.3339s | 1.5003s | `detyped_files/deltablue/advanced/proportion_sweep/main_k02_s05.py` |  |
| 0.06 | 2/34 | 6 | 1.4011s | 0.0885s | 1 | 8 | yes | 1.3455s | 1.4601s | `detyped_files/deltablue/advanced/proportion_sweep/main_k02_s06.py` |  |
| 0.06 | 2/34 | 7 | 1.5034s | 0.0537s | 1 | 8 | yes | 1.4655s | 1.5360s | `detyped_files/deltablue/advanced/proportion_sweep/main_k02_s07.py` |  |
| 0.06 | 2/34 | 8 | 1.4527s | 0.0665s | 1 | 8 | yes | 1.4068s | 1.4930s | `detyped_files/deltablue/advanced/proportion_sweep/main_k02_s08.py` |  |
| 0.06 | 2/34 | 9 | 1.3428s | 0.0685s | 1 | 8 | yes | 1.2962s | 1.3861s | `detyped_files/deltablue/advanced/proportion_sweep/main_k02_s09.py` |  |
| 0.06 | 2/34 | 10 | 1.4116s | 0.1218s | 1 | 8 | yes | 1.3332s | 1.4897s | `detyped_files/deltablue/advanced/proportion_sweep/main_k02_s10.py` |  |
| 0.06 | 2/34 | 11 | 1.3837s | 0.0742s | 1 | 8 | yes | 1.3352s | 1.4314s | `detyped_files/deltablue/advanced/proportion_sweep/main_k02_s11.py` |  |
| 0.06 | 2/34 | 12 | 1.4140s | 0.0600s | 1 | 8 | yes | 1.3751s | 1.4534s | `detyped_files/deltablue/advanced/proportion_sweep/main_k02_s12.py` |  |
| 0.06 | 2/34 | 13 | 1.3235s | 0.0529s | 1 | 8 | yes | 1.2910s | 1.3596s | `detyped_files/deltablue/advanced/proportion_sweep/main_k02_s13.py` |  |
| 0.06 | 2/34 | 14 | 1.3923s | 0.0613s | 1 | 8 | yes | 1.3506s | 1.4294s | `detyped_files/deltablue/advanced/proportion_sweep/main_k02_s14.py` |  |
| 0.06 | 2/34 | 15 | 1.3459s | 0.0579s | 1 | 8 | yes | 1.3064s | 1.3807s | `detyped_files/deltablue/advanced/proportion_sweep/main_k02_s15.py` |  |
| 0.06 | 2/34 | 16 | 1.4887s | 0.1162s | 1 | 8 | yes | 1.4103s | 1.5618s | `detyped_files/deltablue/advanced/proportion_sweep/main_k02_s16.py` |  |
| 0.06 | 2/34 | 17 | 1.3501s | 0.0854s | 1 | 8 | yes | 1.2949s | 1.4064s | `detyped_files/deltablue/advanced/proportion_sweep/main_k02_s17.py` |  |
| 0.06 | 2/34 | 18 | 6.6590s | 0.0889s | 1 | 8 | yes | 6.6006s | 6.7138s | `detyped_files/deltablue/advanced/proportion_sweep/main_k02_s18.py` |  |
| 0.06 | 2/34 | 19 | 6.6527s | 0.0951s | 1 | 8 | yes | 6.5957s | 6.7182s | `detyped_files/deltablue/advanced/proportion_sweep/main_k02_s19.py` |  |
| 0.06 | 2/34 | 20 | 1.3825s | 0.0558s | 1 | 8 | yes | 1.3456s | 1.4179s | `detyped_files/deltablue/advanced/proportion_sweep/main_k02_s20.py` |  |
| 0.09 | 3/34 | 1 | 1.4434s | 0.0580s | 1 | 8 | yes | 1.4024s | 1.4757s | `detyped_files/deltablue/advanced/proportion_sweep/main_k03_s01.py` |  |
| 0.09 | 3/34 | 2 | 1.3514s | 0.0590s | 1 | 8 | yes | 1.3131s | 1.3895s | `detyped_files/deltablue/advanced/proportion_sweep/main_k03_s02.py` |  |
| 0.09 | 3/34 | 3 | 1.3582s | 0.0844s | 1 | 8 | yes | 1.3049s | 1.4143s | `detyped_files/deltablue/advanced/proportion_sweep/main_k03_s03.py` |  |
| 0.09 | 3/34 | 4 | 6.7464s | 0.0959s | 1 | 8 | yes | 6.6858s | 6.8092s | `detyped_files/deltablue/advanced/proportion_sweep/main_k03_s04.py` |  |
| 0.09 | 3/34 | 5 | 1.3667s | 0.0781s | 1 | 8 | yes | 1.3156s | 1.4158s | `detyped_files/deltablue/advanced/proportion_sweep/main_k03_s05.py` |  |
| 0.09 | 3/34 | 6 | 1.4034s | 0.0596s | 1 | 8 | yes | 1.3661s | 1.4437s | `detyped_files/deltablue/advanced/proportion_sweep/main_k03_s06.py` |  |
| 0.09 | 3/34 | 7 | 1.4030s | 0.0915s | 1 | 8 | yes | 1.3441s | 1.4622s | `detyped_files/deltablue/advanced/proportion_sweep/main_k03_s07.py` |  |
| 0.09 | 3/34 | 8 | 1.8844s | 0.0639s | 1 | 8 | yes | 1.8432s | 1.9262s | `detyped_files/deltablue/advanced/proportion_sweep/main_k03_s08.py` |  |
| 0.09 | 3/34 | 9 | 1.4037s | 0.0738s | 1 | 8 | yes | 1.3572s | 1.4533s | `detyped_files/deltablue/advanced/proportion_sweep/main_k03_s09.py` |  |
| 0.09 | 3/34 | 10 | 6.8733s | 0.0964s | 1 | 8 | yes | 6.8158s | 6.9407s | `detyped_files/deltablue/advanced/proportion_sweep/main_k03_s10.py` |  |
| 0.09 | 3/34 | 11 | 1.4857s | 0.0861s | 1 | 8 | yes | 1.4317s | 1.5418s | `detyped_files/deltablue/advanced/proportion_sweep/main_k03_s11.py` |  |
| 0.09 | 3/34 | 12 | 1.3933s | 0.0942s | 1 | 8 | yes | 1.3343s | 1.4557s | `detyped_files/deltablue/advanced/proportion_sweep/main_k03_s12.py` |  |
| 0.09 | 3/34 | 13 | 1.5667s | 0.0536s | 1 | 8 | yes | 1.5277s | 1.5895s | `detyped_files/deltablue/advanced/proportion_sweep/main_k03_s13.py` |  |
| 0.09 | 3/34 | 14 | 1.7897s | 0.0532s | 1 | 8 | yes | 1.7579s | 1.8259s | `detyped_files/deltablue/advanced/proportion_sweep/main_k03_s14.py` |  |
| 0.09 | 3/34 | 15 | 1.4542s | 0.0580s | 1 | 8 | yes | 1.4175s | 1.4913s | `detyped_files/deltablue/advanced/proportion_sweep/main_k03_s15.py` |  |
| 0.09 | 3/34 | 16 | 1.3797s | 0.0808s | 1 | 8 | yes | 1.3283s | 1.4323s | `detyped_files/deltablue/advanced/proportion_sweep/main_k03_s16.py` |  |
| 0.09 | 3/34 | 17 | 1.4359s | 0.0780s | 1 | 8 | yes | 1.3861s | 1.4859s | `detyped_files/deltablue/advanced/proportion_sweep/main_k03_s17.py` |  |
| 0.09 | 3/34 | 18 | 1.5089s | 0.0582s | 1 | 8 | yes | 1.4724s | 1.5471s | `detyped_files/deltablue/advanced/proportion_sweep/main_k03_s18.py` |  |
| 0.09 | 3/34 | 19 | 1.3620s | 0.1833s | 1 | 8 | yes | 1.2693s | 1.4974s | `detyped_files/deltablue/advanced/proportion_sweep/main_k03_s19.py` |  |
| 0.09 | 3/34 | 20 | 1.4548s | 0.0681s | 1 | 8 | yes | 1.4140s | 1.5017s | `detyped_files/deltablue/advanced/proportion_sweep/main_k03_s20.py` |  |
| 0.12 | 4/34 | 1 | 6.6113s | 0.0664s | 1 | 8 | yes | 6.5705s | 6.6555s | `detyped_files/deltablue/advanced/proportion_sweep/main_k04_s01.py` |  |
| 0.12 | 4/34 | 2 | 1.4348s | 0.1308s | 1 | 8 | yes | 1.3547s | 1.5261s | `detyped_files/deltablue/advanced/proportion_sweep/main_k04_s02.py` |  |
| 0.12 | 4/34 | 3 | 1.3992s | 0.0789s | 1 | 8 | yes | 1.3447s | 1.4478s | `detyped_files/deltablue/advanced/proportion_sweep/main_k04_s03.py` |  |
| 0.12 | 4/34 | 4 | 1.3865s | 0.0589s | 1 | 8 | yes | 1.3483s | 1.4226s | `detyped_files/deltablue/advanced/proportion_sweep/main_k04_s04.py` |  |
| 0.12 | 4/34 | 5 | 1.4131s | 0.1350s | 1 | 8 | yes | 1.3293s | 1.5059s | `detyped_files/deltablue/advanced/proportion_sweep/main_k04_s05.py` |  |
| 0.12 | 4/34 | 6 | 6.7324s | 0.1584s | 1 | 8 | yes | 6.6313s | 6.8363s | `detyped_files/deltablue/advanced/proportion_sweep/main_k04_s06.py` |  |
| 0.12 | 4/34 | 7 | 1.4402s | 0.0655s | 1 | 8 | yes | 1.3952s | 1.4797s | `detyped_files/deltablue/advanced/proportion_sweep/main_k04_s07.py` |  |
| 0.12 | 4/34 | 8 | 1.8590s | 0.0642s | 1 | 8 | yes | 1.8176s | 1.8997s | `detyped_files/deltablue/advanced/proportion_sweep/main_k04_s08.py` |  |
| 0.12 | 4/34 | 9 | 1.8397s | 0.0873s | 1 | 8 | yes | 1.7865s | 1.8980s | `detyped_files/deltablue/advanced/proportion_sweep/main_k04_s09.py` |  |
| 0.12 | 4/34 | 10 | 1.4104s | 0.1045s | 1 | 8 | yes | 1.3418s | 1.4770s | `detyped_files/deltablue/advanced/proportion_sweep/main_k04_s10.py` |  |
| 0.12 | 4/34 | 11 | 1.5131s | 0.0584s | 1 | 8 | yes | 1.4760s | 1.5514s | `detyped_files/deltablue/advanced/proportion_sweep/main_k04_s11.py` |  |
| 0.12 | 4/34 | 12 | 1.4232s | 0.0424s | 1 | 8 | yes | 1.3939s | 1.4480s | `detyped_files/deltablue/advanced/proportion_sweep/main_k04_s12.py` |  |
| 0.12 | 4/34 | 13 | 1.5469s | 0.1118s | 1 | 8 | yes | 1.4787s | 1.6208s | `detyped_files/deltablue/advanced/proportion_sweep/main_k04_s13.py` |  |
| 0.12 | 4/34 | 14 | 1.8259s | 0.0840s | 1 | 8 | yes | 1.7679s | 1.8753s | `detyped_files/deltablue/advanced/proportion_sweep/main_k04_s14.py` |  |
| 0.12 | 4/34 | 15 | 1.4017s | 0.0489s | 1 | 8 | yes | 1.3725s | 1.4355s | `detyped_files/deltablue/advanced/proportion_sweep/main_k04_s15.py` |  |
| 0.12 | 4/34 | 16 | 1.4799s | 0.0743s | 1 | 8 | yes | 1.4330s | 1.5278s | `detyped_files/deltablue/advanced/proportion_sweep/main_k04_s16.py` |  |
| 0.12 | 4/34 | 17 | 1.8673s | 0.0465s | 1 | 8 | yes | 1.8400s | 1.8991s | `detyped_files/deltablue/advanced/proportion_sweep/main_k04_s17.py` |  |
| 0.12 | 4/34 | 18 | 8.0091s | 0.1088s | 1 | 8 | yes | 7.9441s | 8.0825s | `detyped_files/deltablue/advanced/proportion_sweep/main_k04_s18.py` |  |
| 0.12 | 4/34 | 19 | 1.3739s | 0.1265s | 1 | 8 | yes | 1.3021s | 1.4637s | `detyped_files/deltablue/advanced/proportion_sweep/main_k04_s19.py` |  |
| 0.12 | 4/34 | 20 | 6.6660s | 0.0924s | 1 | 8 | yes | 6.6040s | 6.7245s | `detyped_files/deltablue/advanced/proportion_sweep/main_k04_s20.py` |  |
| 0.15 | 5/34 | 1 | 1.5799s | 0.0234s | 1 | 8 | yes | 1.5651s | 1.5956s | `detyped_files/deltablue/advanced/proportion_sweep/main_k05_s01.py` |  |
| 0.15 | 5/34 | 2 | 1.3849s | 0.0764s | 1 | 8 | yes | 1.3352s | 1.4329s | `detyped_files/deltablue/advanced/proportion_sweep/main_k05_s02.py` |  |
| 0.15 | 5/34 | 3 | 1.4674s | 0.0664s | 1 | 8 | yes | 1.4208s | 1.5072s | `detyped_files/deltablue/advanced/proportion_sweep/main_k05_s03.py` |  |
| 0.15 | 5/34 | 4 | 1.5284s | 0.0686s | 1 | 8 | yes | 1.4835s | 1.5711s | `detyped_files/deltablue/advanced/proportion_sweep/main_k05_s04.py` |  |
| 0.15 | 5/34 | 5 | 1.4837s | 0.0690s | 1 | 8 | yes | 1.4375s | 1.5259s | `detyped_files/deltablue/advanced/proportion_sweep/main_k05_s05.py` |  |
| 0.15 | 5/34 | 6 | 1.4590s | 0.0768s | 1 | 8 | yes | 1.4065s | 1.5066s | `detyped_files/deltablue/advanced/proportion_sweep/main_k05_s06.py` |  |
| 0.15 | 5/34 | 7 | 1.7867s | 0.0864s | 1 | 8 | yes | 1.7292s | 1.8398s | `detyped_files/deltablue/advanced/proportion_sweep/main_k05_s07.py` |  |
| 0.15 | 5/34 | 8 | 2.3922s | 0.0822s | 1 | 8 | yes | 2.3386s | 2.4429s | `detyped_files/deltablue/advanced/proportion_sweep/main_k05_s08.py` |  |
| 0.15 | 5/34 | 9 | 1.7761s | 0.0855s | 1 | 8 | yes | 1.7195s | 1.8310s | `detyped_files/deltablue/advanced/proportion_sweep/main_k05_s09.py` |  |
| 0.15 | 5/34 | 10 | 1.4167s | 0.1070s | 1 | 8 | yes | 1.3543s | 1.4891s | `detyped_files/deltablue/advanced/proportion_sweep/main_k05_s10.py` |  |
| 0.15 | 5/34 | 11 | 6.6137s | 0.1401s | 1 | 8 | yes | 6.5368s | 6.7170s | `detyped_files/deltablue/advanced/proportion_sweep/main_k05_s11.py` |  |
| 0.15 | 5/34 | 12 | 1.9735s | 0.1033s | 1 | 8 | yes | 1.9074s | 2.0416s | `detyped_files/deltablue/advanced/proportion_sweep/main_k05_s12.py` |  |
| 0.15 | 5/34 | 13 | 1.5434s | 0.0707s | 1 | 8 | yes | 1.4991s | 1.5909s | `detyped_files/deltablue/advanced/proportion_sweep/main_k05_s13.py` |  |
| 0.15 | 5/34 | 14 | 1.4962s | 0.0615s | 1 | 8 | yes | 1.4544s | 1.5331s | `detyped_files/deltablue/advanced/proportion_sweep/main_k05_s14.py` |  |
| 0.15 | 5/34 | 15 | 2.0412s | 0.0885s | 1 | 8 | yes | 1.9789s | 2.0949s | `detyped_files/deltablue/advanced/proportion_sweep/main_k05_s15.py` |  |
| 0.15 | 5/34 | 16 | 1.4155s | 0.0994s | 1 | 8 | yes | 1.3518s | 1.4784s | `detyped_files/deltablue/advanced/proportion_sweep/main_k05_s16.py` |  |
| 0.15 | 5/34 | 17 | 1.9281s | 0.0916s | 1 | 8 | yes | 1.8677s | 1.9875s | `detyped_files/deltablue/advanced/proportion_sweep/main_k05_s17.py` |  |
| 0.15 | 5/34 | 18 | 1.4337s | 0.0483s | 1 | 8 | yes | 1.4040s | 1.4659s | `detyped_files/deltablue/advanced/proportion_sweep/main_k05_s18.py` |  |
| 0.15 | 5/34 | 19 | 7.9108s | 0.1209s | 1 | 8 | yes | 7.8319s | 7.9862s | `detyped_files/deltablue/advanced/proportion_sweep/main_k05_s19.py` |  |
| 0.15 | 5/34 | 20 | 1.4354s | 0.0673s | 1 | 8 | yes | 1.3907s | 1.4768s | `detyped_files/deltablue/advanced/proportion_sweep/main_k05_s20.py` |  |
| 0.18 | 6/34 | 1 | 1.5720s | 0.0946s | 1 | 8 | yes | 1.5128s | 1.6354s | `detyped_files/deltablue/advanced/proportion_sweep/main_k06_s01.py` |  |
| 0.18 | 6/34 | 2 | 1.9094s | 0.0974s | 1 | 8 | yes | 1.8551s | 1.9789s | `detyped_files/deltablue/advanced/proportion_sweep/main_k06_s02.py` |  |
| 0.18 | 6/34 | 3 | 1.4418s | 0.0796s | 1 | 8 | yes | 1.3954s | 1.4958s | `detyped_files/deltablue/advanced/proportion_sweep/main_k06_s03.py` |  |
| 0.18 | 6/34 | 4 | 1.5479s | 0.0611s | 1 | 8 | yes | 1.5039s | 1.5822s | `detyped_files/deltablue/advanced/proportion_sweep/main_k06_s04.py` |  |
| 0.18 | 6/34 | 5 | 1.5541s | 0.1266s | 1 | 8 | yes | 1.4787s | 1.6389s | `detyped_files/deltablue/advanced/proportion_sweep/main_k06_s05.py` |  |
| 0.18 | 6/34 | 6 | 1.5189s | 0.0718s | 1 | 8 | yes | 1.4712s | 1.5649s | `detyped_files/deltablue/advanced/proportion_sweep/main_k06_s06.py` |  |
| 0.18 | 6/34 | 7 | 1.5206s | 0.0953s | 1 | 8 | yes | 1.4579s | 1.5804s | `detyped_files/deltablue/advanced/proportion_sweep/main_k06_s07.py` |  |
| 0.18 | 6/34 | 8 | 6.7756s | 0.0810s | 1 | 8 | yes | 6.7233s | 6.8271s | `detyped_files/deltablue/advanced/proportion_sweep/main_k06_s08.py` |  |
| 0.18 | 6/34 | 9 | 1.5292s | 0.0684s | 1 | 8 | yes | 1.4853s | 1.5732s | `detyped_files/deltablue/advanced/proportion_sweep/main_k06_s09.py` |  |
| 0.18 | 6/34 | 10 | 1.8048s | 0.0956s | 1 | 8 | yes | 1.7458s | 1.8709s | `detyped_files/deltablue/advanced/proportion_sweep/main_k06_s10.py` |  |
| 0.18 | 6/34 | 11 | 8.3286s | 0.1309s | 1 | 8 | yes | 8.2502s | 8.4189s | `detyped_files/deltablue/advanced/proportion_sweep/main_k06_s11.py` |  |
| 0.18 | 6/34 | 12 | 2.3162s | 0.1418s | 1 | 8 | yes | 2.2306s | 2.4134s | `detyped_files/deltablue/advanced/proportion_sweep/main_k06_s12.py` |  |
| 0.18 | 6/34 | 13 | 1.5228s | 0.0763s | 1 | 8 | yes | 1.4738s | 1.5706s | `detyped_files/deltablue/advanced/proportion_sweep/main_k06_s13.py` |  |
| 0.18 | 6/34 | 14 | 1.3776s | 0.0823s | 1 | 8 | yes | 1.3240s | 1.4292s | `detyped_files/deltablue/advanced/proportion_sweep/main_k06_s14.py` |  |
| 0.18 | 6/34 | 15 | 1.4606s | 0.0782s | 1 | 8 | yes | 1.4089s | 1.5107s | `detyped_files/deltablue/advanced/proportion_sweep/main_k06_s15.py` |  |
| 0.18 | 6/34 | 16 | 6.5945s | 0.0544s | 1 | 8 | yes | 6.5594s | 6.6294s | `detyped_files/deltablue/advanced/proportion_sweep/main_k06_s16.py` |  |
| 0.18 | 6/34 | 17 | 1.9832s | 0.0793s | 1 | 8 | yes | 1.9297s | 2.0322s | `detyped_files/deltablue/advanced/proportion_sweep/main_k06_s17.py` |  |
| 0.18 | 6/34 | 18 | 1.3821s | 0.0723s | 1 | 8 | yes | 1.3351s | 1.4277s | `detyped_files/deltablue/advanced/proportion_sweep/main_k06_s18.py` |  |
| 0.18 | 6/34 | 19 | 1.6000s | 0.1640s | 1 | 8 | yes | 1.5065s | 1.7166s | `detyped_files/deltablue/advanced/proportion_sweep/main_k06_s19.py` |  |
| 0.18 | 6/34 | 20 | 1.3838s | 0.0619s | 1 | 8 | yes | 1.3403s | 1.4195s | `detyped_files/deltablue/advanced/proportion_sweep/main_k06_s20.py` |  |
| 0.21 | 7/34 | 1 | 1.9446s | 0.1060s | 1 | 8 | yes | 1.8754s | 2.0132s | `detyped_files/deltablue/advanced/proportion_sweep/main_k07_s01.py` |  |
| 0.21 | 7/34 | 2 | 1.9553s | 0.0583s | 1 | 8 | yes | 1.9161s | 1.9916s | `detyped_files/deltablue/advanced/proportion_sweep/main_k07_s02.py` |  |
| 0.21 | 7/34 | 3 | 1.9525s | 0.1197s | 1 | 8 | yes | 1.8835s | 2.0347s | `detyped_files/deltablue/advanced/proportion_sweep/main_k07_s03.py` |  |
| 0.21 | 7/34 | 4 | 2.0216s | 0.1282s | 1 | 8 | yes | 1.9372s | 2.1041s | `detyped_files/deltablue/advanced/proportion_sweep/main_k07_s04.py` |  |
| 0.21 | 7/34 | 5 | 7.9059s | 0.0575s | 1 | 8 | yes | 7.8660s | 7.9403s | `detyped_files/deltablue/advanced/proportion_sweep/main_k07_s05.py` |  |
| 0.21 | 7/34 | 6 | 6.7902s | 0.0649s | 1 | 8 | yes | 6.7479s | 6.8305s | `detyped_files/deltablue/advanced/proportion_sweep/main_k07_s06.py` |  |
| 0.21 | 7/34 | 7 | 8.0596s | 0.0568s | 1 | 8 | yes | 8.0235s | 8.0969s | `detyped_files/deltablue/advanced/proportion_sweep/main_k07_s07.py` |  |
| 0.21 | 7/34 | 8 | 1.4114s | 0.0728s | 1 | 8 | yes | 1.3628s | 1.4556s | `detyped_files/deltablue/advanced/proportion_sweep/main_k07_s08.py` |  |
| 0.21 | 7/34 | 9 | 1.7727s | 0.0530s | 1 | 8 | yes | 1.7374s | 1.8051s | `detyped_files/deltablue/advanced/proportion_sweep/main_k07_s09.py` |  |
| 0.21 | 7/34 | 10 | 8.1839s | 0.1134s | 1 | 8 | yes | 8.1107s | 8.2558s | `detyped_files/deltablue/advanced/proportion_sweep/main_k07_s10.py` |  |
| 0.21 | 7/34 | 11 | 1.5048s | 0.0561s | 1 | 8 | yes | 1.4695s | 1.5420s | `detyped_files/deltablue/advanced/proportion_sweep/main_k07_s11.py` |  |
| 0.21 | 7/34 | 12 | 6.6861s | 0.0877s | 1 | 8 | yes | 6.6298s | 6.7419s | `detyped_files/deltablue/advanced/proportion_sweep/main_k07_s12.py` |  |
| 0.21 | 7/34 | 13 | 1.8216s | 0.1332s | 1 | 8 | yes | 1.7352s | 1.9050s | `detyped_files/deltablue/advanced/proportion_sweep/main_k07_s13.py` |  |
| 0.21 | 7/34 | 14 | 1.9285s | 0.0875s | 1 | 8 | yes | 1.8672s | 1.9804s | `detyped_files/deltablue/advanced/proportion_sweep/main_k07_s14.py` |  |
| 0.21 | 7/34 | 15 | 1.9340s | 0.0924s | 1 | 8 | yes | 1.8721s | 1.9907s | `detyped_files/deltablue/advanced/proportion_sweep/main_k07_s15.py` |  |
| 0.21 | 7/34 | 16 | 1.6535s | 0.0762s | 1 | 8 | yes | 1.6036s | 1.7014s | `detyped_files/deltablue/advanced/proportion_sweep/main_k07_s16.py` |  |
| 0.21 | 7/34 | 17 | 1.9387s | 0.0861s | 1 | 8 | yes | 1.8869s | 2.0000s | `detyped_files/deltablue/advanced/proportion_sweep/main_k07_s17.py` |  |
| 0.21 | 7/34 | 18 | 1.4953s | 0.0742s | 1 | 8 | yes | 1.4472s | 1.5428s | `detyped_files/deltablue/advanced/proportion_sweep/main_k07_s18.py` |  |
| 0.21 | 7/34 | 19 | 1.7978s | 0.0495s | 1 | 8 | yes | 1.7664s | 1.8300s | `detyped_files/deltablue/advanced/proportion_sweep/main_k07_s19.py` |  |
| 0.21 | 7/34 | 20 | 1.9362s | 0.0364s | 1 | 8 | yes | 1.9121s | 1.9587s | `detyped_files/deltablue/advanced/proportion_sweep/main_k07_s20.py` |  |
| 0.24 | 8/34 | 1 | 1.9870s | 0.0831s | 1 | 8 | yes | 1.9342s | 2.0423s | `detyped_files/deltablue/advanced/proportion_sweep/main_k08_s01.py` |  |
| 0.24 | 8/34 | 2 | 1.9473s | 0.0933s | 1 | 8 | yes | 1.8838s | 2.0049s | `detyped_files/deltablue/advanced/proportion_sweep/main_k08_s02.py` |  |
| 0.24 | 8/34 | 3 | 1.5053s | 0.0718s | 1 | 8 | yes | 1.4522s | 1.5452s | `detyped_files/deltablue/advanced/proportion_sweep/main_k08_s03.py` |  |
| 0.24 | 8/34 | 4 | 7.4709s | 0.1153s | 1 | 8 | yes | 7.3956s | 7.5447s | `detyped_files/deltablue/advanced/proportion_sweep/main_k08_s04.py` |  |
| 0.24 | 8/34 | 5 | 6.6072s | 0.0883s | 1 | 8 | yes | 6.5521s | 6.6644s | `detyped_files/deltablue/advanced/proportion_sweep/main_k08_s05.py` |  |
| 0.24 | 8/34 | 6 | 1.9595s | 0.0553s | 1 | 8 | yes | 1.9208s | 1.9918s | `detyped_files/deltablue/advanced/proportion_sweep/main_k08_s06.py` |  |
| 0.24 | 8/34 | 7 | 1.5914s | 0.0834s | 1 | 8 | yes | 1.5402s | 1.6484s | `detyped_files/deltablue/advanced/proportion_sweep/main_k08_s07.py` |  |
| 0.24 | 8/34 | 8 | 2.0420s | 0.1500s | 1 | 8 | yes | 1.9490s | 2.1401s | `detyped_files/deltablue/advanced/proportion_sweep/main_k08_s08.py` |  |
| 0.24 | 8/34 | 9 | 1.9989s | 0.0783s | 1 | 8 | yes | 1.9483s | 2.0515s | `detyped_files/deltablue/advanced/proportion_sweep/main_k08_s09.py` |  |
| 0.24 | 8/34 | 10 | 6.8185s | 0.0803s | 1 | 8 | yes | 6.7701s | 6.8737s | `detyped_files/deltablue/advanced/proportion_sweep/main_k08_s10.py` |  |
| 0.24 | 8/34 | 11 | 6.7261s | 0.0474s | 1 | 8 | yes | 6.6956s | 6.7567s | `detyped_files/deltablue/advanced/proportion_sweep/main_k08_s11.py` |  |
| 0.24 | 8/34 | 12 | 1.4000s | 0.0837s | 1 | 8 | yes | 1.3485s | 1.4573s | `detyped_files/deltablue/advanced/proportion_sweep/main_k08_s12.py` |  |
| 0.24 | 8/34 | 13 | 2.0173s | 0.1641s | 1 | 8 | yes | 1.9196s | 2.1320s | `detyped_files/deltablue/advanced/proportion_sweep/main_k08_s13.py` |  |
| 0.24 | 8/34 | 14 | 1.8459s | 0.0670s | 1 | 8 | yes | 1.7983s | 1.8830s | `detyped_files/deltablue/advanced/proportion_sweep/main_k08_s14.py` |  |
| 0.24 | 8/34 | 15 | 1.5172s | 0.0460s | 1 | 8 | yes | 1.4856s | 1.5455s | `detyped_files/deltablue/advanced/proportion_sweep/main_k08_s15.py` |  |
| 0.24 | 8/34 | 16 | 1.4719s | 0.0321s | 1 | 8 | yes | 1.4548s | 1.4951s | `detyped_files/deltablue/advanced/proportion_sweep/main_k08_s16.py` |  |
| 0.24 | 8/34 | 17 | 8.4536s | 0.1237s | 1 | 8 | yes | 8.3723s | 8.5306s | `detyped_files/deltablue/advanced/proportion_sweep/main_k08_s17.py` |  |
| 0.24 | 8/34 | 18 | 2.0882s | 0.1156s | 1 | 8 | yes | 2.0239s | 2.1696s | `detyped_files/deltablue/advanced/proportion_sweep/main_k08_s18.py` |  |
| 0.24 | 8/34 | 19 | 6.6452s | 0.1095s | 1 | 8 | yes | 6.5746s | 6.7177s | `detyped_files/deltablue/advanced/proportion_sweep/main_k08_s19.py` |  |
| 0.24 | 8/34 | 20 | 1.4653s | 0.0561s | 1 | 8 | yes | 1.4310s | 1.5044s | `detyped_files/deltablue/advanced/proportion_sweep/main_k08_s20.py` |  |
| 0.26 | 9/34 | 1 | 2.3586s | 0.1099s | 1 | 8 | yes | 2.2970s | 2.4374s | `detyped_files/deltablue/advanced/proportion_sweep/main_k09_s01.py` |  |
| 0.26 | 9/34 | 2 | 7.2013s | 0.1089s | 1 | 8 | yes | 7.1363s | 7.2759s | `detyped_files/deltablue/advanced/proportion_sweep/main_k09_s02.py` |  |
| 0.26 | 9/34 | 3 | 7.1710s | 0.0533s | 1 | 8 | yes | 7.1350s | 7.2045s | `detyped_files/deltablue/advanced/proportion_sweep/main_k09_s03.py` |  |
| 0.26 | 9/34 | 4 | 7.1223s | 0.1262s | 1 | 8 | yes | 7.0498s | 7.2107s | `detyped_files/deltablue/advanced/proportion_sweep/main_k09_s04.py` |  |
| 0.26 | 9/34 | 5 | 8.3068s | 0.0810s | 1 | 8 | yes | 8.2561s | 8.3603s | `detyped_files/deltablue/advanced/proportion_sweep/main_k09_s05.py` |  |
| 0.26 | 9/34 | 6 | 7.8195s | 0.0911s | 1 | 8 | yes | 7.7536s | 7.8695s | `detyped_files/deltablue/advanced/proportion_sweep/main_k09_s06.py` |  |
| 0.26 | 9/34 | 7 | 1.5321s | 0.0487s | 1 | 8 | yes | 1.4993s | 1.5619s | `detyped_files/deltablue/advanced/proportion_sweep/main_k09_s07.py` |  |
| 0.26 | 9/34 | 8 | 8.2379s | 0.2433s | 1 | 8 | yes | 8.1115s | 8.4181s | `detyped_files/deltablue/advanced/proportion_sweep/main_k09_s08.py` |  |
| 0.26 | 9/34 | 9 | 2.0882s | 0.0582s | 1 | 8 | yes | 2.0522s | 2.1278s | `detyped_files/deltablue/advanced/proportion_sweep/main_k09_s09.py` |  |
| 0.26 | 9/34 | 10 | 1.9087s | 0.0694s | 1 | 8 | yes | 1.8630s | 1.9522s | `detyped_files/deltablue/advanced/proportion_sweep/main_k09_s10.py` |  |
| 0.26 | 9/34 | 11 | 1.5406s | 0.0864s | 1 | 8 | yes | 1.4834s | 1.5954s | `detyped_files/deltablue/advanced/proportion_sweep/main_k09_s11.py` |  |
| 0.26 | 9/34 | 12 | 1.9220s | 0.0758s | 1 | 8 | yes | 1.8748s | 1.9722s | `detyped_files/deltablue/advanced/proportion_sweep/main_k09_s12.py` |  |
| 0.26 | 9/34 | 13 | 1.8874s | 0.0457s | 1 | 8 | yes | 1.8564s | 1.9144s | `detyped_files/deltablue/advanced/proportion_sweep/main_k09_s13.py` |  |
| 0.26 | 9/34 | 14 | 1.5314s | 0.0942s | 1 | 8 | yes | 1.4741s | 1.5957s | `detyped_files/deltablue/advanced/proportion_sweep/main_k09_s14.py` |  |
| 0.26 | 9/34 | 15 | 1.8454s | 0.0631s | 1 | 8 | yes | 1.8032s | 1.8856s | `detyped_files/deltablue/advanced/proportion_sweep/main_k09_s15.py` |  |
| 0.26 | 9/34 | 16 | 2.2850s | 0.1188s | 1 | 8 | yes | 2.2090s | 2.3627s | `detyped_files/deltablue/advanced/proportion_sweep/main_k09_s16.py` |  |
| 0.26 | 9/34 | 17 | 1.4249s | 0.0814s | 1 | 8 | yes | 1.3702s | 1.4743s | `detyped_files/deltablue/advanced/proportion_sweep/main_k09_s17.py` |  |
| 0.26 | 9/34 | 18 | 1.9542s | 0.0483s | 1 | 8 | yes | 1.9253s | 1.9870s | `detyped_files/deltablue/advanced/proportion_sweep/main_k09_s18.py` |  |
| 0.26 | 9/34 | 19 | 1.4411s | 0.0464s | 1 | 8 | yes | 1.4086s | 1.4663s | `detyped_files/deltablue/advanced/proportion_sweep/main_k09_s19.py` |  |
| 0.26 | 9/34 | 20 | 1.7720s | 0.1213s | 1 | 8 | yes | 1.7023s | 1.8564s | `detyped_files/deltablue/advanced/proportion_sweep/main_k09_s20.py` |  |
| 0.29 | 10/34 | 1 | 1.5288s | 0.1016s | 1 | 8 | yes | 1.4605s | 1.5916s | `detyped_files/deltablue/advanced/proportion_sweep/main_k10_s01.py` |  |
| 0.29 | 10/34 | 2 | 2.1160s | 0.0911s | 1 | 8 | yes | 2.0553s | 2.1733s | `detyped_files/deltablue/advanced/proportion_sweep/main_k10_s02.py` |  |
| 0.29 | 10/34 | 3 | 2.3628s | 0.1204s | 1 | 8 | yes | 2.2868s | 2.4413s | `detyped_files/deltablue/advanced/proportion_sweep/main_k10_s03.py` |  |
| 0.29 | 10/34 | 4 | 1.9989s | 0.1204s | 1 | 8 | yes | 1.9267s | 2.0830s | `detyped_files/deltablue/advanced/proportion_sweep/main_k10_s04.py` |  |
| 0.29 | 10/34 | 5 | 7.3459s | 0.0868s | 1 | 8 | yes | 7.2962s | 7.4081s | `detyped_files/deltablue/advanced/proportion_sweep/main_k10_s05.py` |  |
| 0.29 | 10/34 | 6 | 1.5272s | 0.0809s | 1 | 8 | yes | 1.4754s | 1.5792s | `detyped_files/deltablue/advanced/proportion_sweep/main_k10_s06.py` |  |
| 0.29 | 10/34 | 7 | 7.6696s | 0.1535s | 1 | 8 | yes | 7.5727s | 7.7715s | `detyped_files/deltablue/advanced/proportion_sweep/main_k10_s07.py` |  |
| 0.29 | 10/34 | 8 | 1.5026s | 0.1811s | 1 | 8 | yes | 1.3969s | 1.6286s | `detyped_files/deltablue/advanced/proportion_sweep/main_k10_s08.py` |  |
| 0.29 | 10/34 | 9 | 1.4504s | 0.0712s | 1 | 8 | yes | 1.4024s | 1.4940s | `detyped_files/deltablue/advanced/proportion_sweep/main_k10_s09.py` |  |
| 0.29 | 10/34 | 10 | 7.7534s | 0.0937s | 1 | 8 | yes | 7.6899s | 7.8122s | `detyped_files/deltablue/advanced/proportion_sweep/main_k10_s10.py` |  |
| 0.29 | 10/34 | 11 | 2.0335s | 0.0757s | 1 | 8 | yes | 1.9815s | 2.0794s | `detyped_files/deltablue/advanced/proportion_sweep/main_k10_s11.py` |  |
| 0.29 | 10/34 | 12 | 1.9671s | 0.0715s | 1 | 8 | yes | 1.9183s | 2.0106s | `detyped_files/deltablue/advanced/proportion_sweep/main_k10_s12.py` |  |
| 0.29 | 10/34 | 13 | 1.9939s | 0.1021s | 1 | 8 | yes | 1.9307s | 2.0608s | `detyped_files/deltablue/advanced/proportion_sweep/main_k10_s13.py` |  |
| 0.29 | 10/34 | 14 | 1.6535s | 0.0769s | 1 | 8 | yes | 1.6050s | 1.7035s | `detyped_files/deltablue/advanced/proportion_sweep/main_k10_s14.py` |  |
| 0.29 | 10/34 | 15 | 2.0687s | 0.0613s | 1 | 8 | yes | 2.0308s | 2.1091s | `detyped_files/deltablue/advanced/proportion_sweep/main_k10_s15.py` |  |
| 0.29 | 10/34 | 16 | 7.9868s | 0.1482s | 1 | 8 | yes | 7.8938s | 8.0814s | `detyped_files/deltablue/advanced/proportion_sweep/main_k10_s16.py` |  |
| 0.29 | 10/34 | 17 | 1.3985s | 0.0564s | 1 | 8 | yes | 1.3575s | 1.4293s | `detyped_files/deltablue/advanced/proportion_sweep/main_k10_s17.py` |  |
| 0.29 | 10/34 | 18 | 1.9478s | 0.0742s | 1 | 8 | yes | 1.8978s | 1.9941s | `detyped_files/deltablue/advanced/proportion_sweep/main_k10_s18.py` |  |
| 0.29 | 10/34 | 19 | 1.3794s | 0.0790s | 1 | 8 | yes | 1.3274s | 1.4306s | `detyped_files/deltablue/advanced/proportion_sweep/main_k10_s19.py` |  |
| 0.29 | 10/34 | 20 | 1.9811s | 0.0393s | 1 | 8 | yes | 1.9574s | 2.0080s | `detyped_files/deltablue/advanced/proportion_sweep/main_k10_s20.py` |  |
| 0.32 | 11/34 | 1 | 8.3769s | 0.0851s | 1 | 8 | yes | 8.3233s | 8.4311s | `detyped_files/deltablue/advanced/proportion_sweep/main_k11_s01.py` |  |
| 0.32 | 11/34 | 2 | 1.6902s | 0.0578s | 1 | 8 | yes | 1.6517s | 1.7264s | `detyped_files/deltablue/advanced/proportion_sweep/main_k11_s02.py` |  |
| 0.32 | 11/34 | 3 | 6.6388s | 0.0537s | 1 | 8 | yes | 6.6055s | 6.6743s | `detyped_files/deltablue/advanced/proportion_sweep/main_k11_s03.py` |  |
| 0.32 | 11/34 | 4 | 1.6203s | 0.0903s | 1 | 8 | yes | 1.5714s | 1.6858s | `detyped_files/deltablue/advanced/proportion_sweep/main_k11_s04.py` |  |
| 0.32 | 11/34 | 5 | 1.8923s | 0.0773s | 1 | 8 | yes | 1.8433s | 1.9434s | `detyped_files/deltablue/advanced/proportion_sweep/main_k11_s05.py` |  |
| 0.32 | 11/34 | 6 | 1.4489s | 0.0649s | 1 | 8 | yes | 1.4064s | 1.4915s | `detyped_files/deltablue/advanced/proportion_sweep/main_k11_s06.py` |  |
| 0.32 | 11/34 | 7 | 2.0541s | 0.1014s | 1 | 8 | yes | 1.9875s | 2.1192s | `detyped_files/deltablue/advanced/proportion_sweep/main_k11_s07.py` |  |
| 0.32 | 11/34 | 8 | 2.0208s | 0.1143s | 1 | 8 | yes | 1.9460s | 2.0950s | `detyped_files/deltablue/advanced/proportion_sweep/main_k11_s08.py` |  |
| 0.32 | 11/34 | 9 | 8.2157s | 0.0553s | 1 | 8 | yes | 8.1797s | 8.2518s | `detyped_files/deltablue/advanced/proportion_sweep/main_k11_s09.py` |  |
| 0.32 | 11/34 | 10 | 7.1847s | 0.1294s | 1 | 8 | yes | 7.1043s | 7.2710s | `detyped_files/deltablue/advanced/proportion_sweep/main_k11_s10.py` |  |
| 0.32 | 11/34 | 11 | 7.1716s | 0.1282s | 1 | 8 | yes | 7.0903s | 7.2576s | `detyped_files/deltablue/advanced/proportion_sweep/main_k11_s11.py` |  |
| 0.32 | 11/34 | 12 | 1.4707s | 0.0861s | 1 | 8 | yes | 1.4168s | 1.5281s | `detyped_files/deltablue/advanced/proportion_sweep/main_k11_s12.py` |  |
| 0.32 | 11/34 | 13 | 1.6409s | 0.0946s | 1 | 8 | yes | 1.5789s | 1.7007s | `detyped_files/deltablue/advanced/proportion_sweep/main_k11_s13.py` |  |
| 0.32 | 11/34 | 14 | 7.2929s | 0.1859s | 1 | 8 | yes | 7.1705s | 7.4108s | `detyped_files/deltablue/advanced/proportion_sweep/main_k11_s14.py` |  |
| 0.32 | 11/34 | 15 | 2.0211s | 0.0786s | 1 | 8 | yes | 1.9715s | 2.0736s | `detyped_files/deltablue/advanced/proportion_sweep/main_k11_s15.py` |  |
| 0.32 | 11/34 | 16 | 1.5673s | 0.0642s | 1 | 8 | yes | 1.5227s | 1.6064s | `detyped_files/deltablue/advanced/proportion_sweep/main_k11_s16.py` |  |
| 0.32 | 11/34 | 17 | 9.5005s | 0.1491s | 1 | 8 | yes | 9.4081s | 9.6012s | `detyped_files/deltablue/advanced/proportion_sweep/main_k11_s17.py` |  |
| 0.32 | 11/34 | 18 | 2.1509s | 0.0850s | 1 | 8 | yes | 2.0985s | 2.2080s | `detyped_files/deltablue/advanced/proportion_sweep/main_k11_s18.py` |  |
| 0.32 | 11/34 | 19 | 2.4579s | 0.0618s | 1 | 8 | yes | 2.4167s | 2.4959s | `detyped_files/deltablue/advanced/proportion_sweep/main_k11_s19.py` |  |
| 0.32 | 11/34 | 20 | 2.0206s | 0.0535s | 1 | 8 | yes | 1.9839s | 2.0533s | `detyped_files/deltablue/advanced/proportion_sweep/main_k11_s20.py` |  |
| 0.35 | 12/34 | 1 | 2.0104s | 0.1171s | 1 | 8 | yes | 1.9341s | 2.0878s | `detyped_files/deltablue/advanced/proportion_sweep/main_k12_s01.py` |  |
| 0.35 | 12/34 | 2 | 2.5409s | 0.0754s | 1 | 8 | yes | 2.4909s | 2.5878s | `detyped_files/deltablue/advanced/proportion_sweep/main_k12_s02.py` |  |
| 0.35 | 12/34 | 3 | 6.9845s | 0.0992s | 1 | 8 | yes | 6.9185s | 7.0451s | `detyped_files/deltablue/advanced/proportion_sweep/main_k12_s03.py` |  |
| 0.35 | 12/34 | 4 | 8.2893s | 0.0990s | 1 | 8 | yes | 8.2250s | 8.3526s | `detyped_files/deltablue/advanced/proportion_sweep/main_k12_s04.py` |  |
| 0.35 | 12/34 | 5 | 2.2421s | 0.1116s | 1 | 8 | yes | 2.1738s | 2.3200s | `detyped_files/deltablue/advanced/proportion_sweep/main_k12_s05.py` |  |
| 0.35 | 12/34 | 6 | 1.7064s | 0.0415s | 1 | 8 | yes | 1.6773s | 1.7317s | `detyped_files/deltablue/advanced/proportion_sweep/main_k12_s06.py` |  |
| 0.35 | 12/34 | 7 | 7.5996s | 0.1221s | 1 | 8 | yes | 7.5212s | 7.6781s | `detyped_files/deltablue/advanced/proportion_sweep/main_k12_s07.py` |  |
| 0.35 | 12/34 | 8 | 1.5762s | 0.0587s | 1 | 8 | yes | 1.5354s | 1.6120s | `detyped_files/deltablue/advanced/proportion_sweep/main_k12_s08.py` |  |
| 0.35 | 12/34 | 9 | 7.0641s | 0.0715s | 1 | 8 | yes | 7.0209s | 7.1124s | `detyped_files/deltablue/advanced/proportion_sweep/main_k12_s09.py` |  |
| 0.35 | 12/34 | 10 | 2.0196s | 0.0603s | 1 | 8 | yes | 1.9828s | 2.0607s | `detyped_files/deltablue/advanced/proportion_sweep/main_k12_s10.py` |  |
| 0.35 | 12/34 | 11 | 2.0004s | 0.0425s | 1 | 8 | yes | 1.9736s | 2.0280s | `detyped_files/deltablue/advanced/proportion_sweep/main_k12_s11.py` |  |
| 0.35 | 12/34 | 12 | 6.7010s | 0.0778s | 1 | 8 | yes | 6.6448s | 6.7386s | `detyped_files/deltablue/advanced/proportion_sweep/main_k12_s12.py` |  |
| 0.35 | 12/34 | 13 | 7.9302s | 0.1471s | 1 | 8 | yes | 7.8436s | 8.0291s | `detyped_files/deltablue/advanced/proportion_sweep/main_k12_s13.py` |  |
| 0.35 | 12/34 | 14 | 1.9329s | 0.0616s | 1 | 8 | yes | 1.8931s | 1.9730s | `detyped_files/deltablue/advanced/proportion_sweep/main_k12_s14.py` |  |
| 0.35 | 12/34 | 15 | 1.9793s | 0.0782s | 1 | 8 | yes | 1.9280s | 2.0295s | `detyped_files/deltablue/advanced/proportion_sweep/main_k12_s15.py` |  |
| 0.35 | 12/34 | 16 | 2.0697s | 0.1069s | 1 | 8 | yes | 1.9973s | 2.1347s | `detyped_files/deltablue/advanced/proportion_sweep/main_k12_s16.py` |  |
| 0.35 | 12/34 | 17 | 2.4935s | 0.0913s | 1 | 8 | yes | 2.4444s | 2.5601s | `detyped_files/deltablue/advanced/proportion_sweep/main_k12_s17.py` |  |
| 0.35 | 12/34 | 18 | 1.9792s | 0.0782s | 1 | 8 | yes | 1.9271s | 2.0275s | `detyped_files/deltablue/advanced/proportion_sweep/main_k12_s18.py` |  |
| 0.35 | 12/34 | 19 | 2.4876s | 0.1277s | 1 | 8 | yes | 2.4061s | 2.5688s | `detyped_files/deltablue/advanced/proportion_sweep/main_k12_s19.py` |  |
| 0.35 | 12/34 | 20 | 9.7218s | 0.0774s | 1 | 8 | yes | 9.6740s | 9.7742s | `detyped_files/deltablue/advanced/proportion_sweep/main_k12_s20.py` |  |
| 0.38 | 13/34 | 1 | 8.4628s | 0.1129s | 1 | 8 | yes | 8.3898s | 8.5362s | `detyped_files/deltablue/advanced/proportion_sweep/main_k13_s01.py` |  |
| 0.38 | 13/34 | 2 | 1.4736s | 0.0900s | 1 | 8 | yes | 1.4160s | 1.5317s | `detyped_files/deltablue/advanced/proportion_sweep/main_k13_s02.py` |  |
| 0.38 | 13/34 | 3 | 6.8338s | 0.0926s | 1 | 8 | yes | 6.7704s | 6.8876s | `detyped_files/deltablue/advanced/proportion_sweep/main_k13_s03.py` |  |
| 0.38 | 13/34 | 4 | 8.3801s | 0.0909s | 1 | 8 | yes | 8.3185s | 8.4357s | `detyped_files/deltablue/advanced/proportion_sweep/main_k13_s04.py` |  |
| 0.38 | 13/34 | 5 | 1.8373s | 0.0615s | 1 | 8 | yes | 1.7978s | 1.8779s | `detyped_files/deltablue/advanced/proportion_sweep/main_k13_s05.py` |  |
| 0.38 | 13/34 | 6 | 1.6773s | 0.1070s | 1 | 8 | yes | 1.6088s | 1.7456s | `detyped_files/deltablue/advanced/proportion_sweep/main_k13_s06.py` |  |
| 0.38 | 13/34 | 7 | 8.6620s | 0.0640s | 1 | 8 | yes | 8.6222s | 8.7047s | `detyped_files/deltablue/advanced/proportion_sweep/main_k13_s07.py` |  |
| 0.38 | 13/34 | 8 | 1.7279s | 0.0775s | 1 | 8 | yes | 1.6803s | 1.7792s | `detyped_files/deltablue/advanced/proportion_sweep/main_k13_s08.py` |  |
| 0.38 | 13/34 | 9 | 2.0306s | 0.0566s | 1 | 8 | yes | 1.9955s | 2.0680s | `detyped_files/deltablue/advanced/proportion_sweep/main_k13_s09.py` |  |
| 0.38 | 13/34 | 10 | 6.7725s | 0.1215s | 1 | 8 | yes | 6.6939s | 6.8516s | `detyped_files/deltablue/advanced/proportion_sweep/main_k13_s10.py` |  |
| 0.38 | 13/34 | 11 | 1.9519s | 0.0790s | 1 | 8 | yes | 1.9013s | 2.0034s | `detyped_files/deltablue/advanced/proportion_sweep/main_k13_s11.py` |  |
| 0.38 | 13/34 | 12 | 2.4023s | 0.0813s | 1 | 8 | yes | 2.3540s | 2.4621s | `detyped_files/deltablue/advanced/proportion_sweep/main_k13_s12.py` |  |
| 0.38 | 13/34 | 13 | 2.0577s | 0.1589s | 1 | 8 | yes | 1.9677s | 2.1740s | `detyped_files/deltablue/advanced/proportion_sweep/main_k13_s13.py` |  |
| 0.38 | 13/34 | 14 | 2.5173s | 0.0500s | 1 | 8 | yes | 2.4861s | 2.5503s | `detyped_files/deltablue/advanced/proportion_sweep/main_k13_s14.py` |  |
| 0.38 | 13/34 | 15 | 7.2393s | 0.1208s | 1 | 8 | yes | 7.1677s | 7.3222s | `detyped_files/deltablue/advanced/proportion_sweep/main_k13_s15.py` |  |
| 0.38 | 13/34 | 16 | 8.1470s | 0.1420s | 1 | 8 | yes | 8.0557s | 8.2395s | `detyped_files/deltablue/advanced/proportion_sweep/main_k13_s16.py` |  |
| 0.38 | 13/34 | 17 | 8.5686s | 0.0961s | 1 | 8 | yes | 8.5084s | 8.6321s | `detyped_files/deltablue/advanced/proportion_sweep/main_k13_s17.py` |  |
| 0.38 | 13/34 | 18 | 8.4598s | 0.1824s | 1 | 8 | yes | 8.3542s | 8.5913s | `detyped_files/deltablue/advanced/proportion_sweep/main_k13_s18.py` |  |
| 0.38 | 13/34 | 19 | 1.8748s | 0.0769s | 1 | 8 | yes | 1.8250s | 1.9245s | `detyped_files/deltablue/advanced/proportion_sweep/main_k13_s19.py` |  |
| 0.38 | 13/34 | 20 | 2.0329s | 0.0463s | 1 | 8 | yes | 2.0036s | 2.0632s | `detyped_files/deltablue/advanced/proportion_sweep/main_k13_s20.py` |  |
| 0.41 | 14/34 | 1 | 1.7387s | 0.0931s | 1 | 8 | yes | 1.6771s | 1.7984s | `detyped_files/deltablue/advanced/proportion_sweep/main_k14_s01.py` |  |
| 0.41 | 14/34 | 2 | 7.8295s | 0.0737s | 1 | 8 | yes | 7.7841s | 7.8766s | `detyped_files/deltablue/advanced/proportion_sweep/main_k14_s02.py` |  |
| 0.41 | 14/34 | 3 | 8.0351s | 0.0568s | 1 | 8 | yes | 7.9990s | 8.0726s | `detyped_files/deltablue/advanced/proportion_sweep/main_k14_s03.py` |  |
| 0.41 | 14/34 | 4 | 7.8224s | 0.1077s | 1 | 8 | yes | 7.7543s | 7.8959s | `detyped_files/deltablue/advanced/proportion_sweep/main_k14_s04.py` |  |
| 0.41 | 14/34 | 5 | 8.6193s | 0.1146s | 1 | 8 | yes | 8.5428s | 8.6895s | `detyped_files/deltablue/advanced/proportion_sweep/main_k14_s05.py` |  |
| 0.41 | 14/34 | 6 | 2.1931s | 0.0961s | 1 | 8 | yes | 2.1421s | 2.2625s | `detyped_files/deltablue/advanced/proportion_sweep/main_k14_s06.py` |  |
| 0.41 | 14/34 | 7 | 8.2773s | 0.0829s | 1 | 8 | yes | 8.2285s | 8.3357s | `detyped_files/deltablue/advanced/proportion_sweep/main_k14_s07.py` |  |
| 0.41 | 14/34 | 8 | 1.9566s | 0.1897s | 1 | 8 | yes | 1.8607s | 2.0958s | `detyped_files/deltablue/advanced/proportion_sweep/main_k14_s08.py` |  |
| 0.41 | 14/34 | 9 | 7.2242s | 0.1101s | 1 | 8 | yes | 7.1538s | 7.2935s | `detyped_files/deltablue/advanced/proportion_sweep/main_k14_s09.py` |  |
| 0.41 | 14/34 | 10 | 7.8557s | 0.0733s | 1 | 8 | yes | 7.8073s | 7.9013s | `detyped_files/deltablue/advanced/proportion_sweep/main_k14_s10.py` |  |
| 0.41 | 14/34 | 11 | 2.5321s | 0.1647s | 1 | 8 | yes | 2.4272s | 2.6396s | `detyped_files/deltablue/advanced/proportion_sweep/main_k14_s11.py` |  |
| 0.41 | 14/34 | 12 | 1.5932s | 0.0416s | 1 | 8 | yes | 1.5654s | 1.6185s | `detyped_files/deltablue/advanced/proportion_sweep/main_k14_s12.py` |  |
| 0.41 | 14/34 | 13 | 7.2813s | 0.1367s | 1 | 8 | yes | 7.1960s | 7.3698s | `detyped_files/deltablue/advanced/proportion_sweep/main_k14_s13.py` |  |
| 0.41 | 14/34 | 14 | 8.5093s | 0.1684s | 1 | 8 | yes | 8.4084s | 8.6282s | `detyped_files/deltablue/advanced/proportion_sweep/main_k14_s14.py` |  |
| 0.41 | 14/34 | 15 | 8.0827s | 0.1148s | 1 | 8 | yes | 8.0145s | 8.1623s | `detyped_files/deltablue/advanced/proportion_sweep/main_k14_s15.py` |  |
| 0.41 | 14/34 | 16 | 2.1854s | 0.0706s | 1 | 8 | yes | 2.1370s | 2.2278s | `detyped_files/deltablue/advanced/proportion_sweep/main_k14_s16.py` |  |
| 0.41 | 14/34 | 17 | 2.0489s | 0.1268s | 1 | 8 | yes | 1.9704s | 2.1369s | `detyped_files/deltablue/advanced/proportion_sweep/main_k14_s17.py` |  |
| 0.41 | 14/34 | 18 | 8.5197s | 0.1357s | 1 | 8 | yes | 8.4343s | 8.6100s | `detyped_files/deltablue/advanced/proportion_sweep/main_k14_s18.py` |  |
| 0.41 | 14/34 | 19 | 2.5164s | 0.0909s | 1 | 8 | yes | 2.4570s | 2.5743s | `detyped_files/deltablue/advanced/proportion_sweep/main_k14_s19.py` |  |
| 0.41 | 14/34 | 20 | 8.7419s | 0.0744s | 1 | 8 | yes | 8.6899s | 8.7857s | `detyped_files/deltablue/advanced/proportion_sweep/main_k14_s20.py` |  |
| 0.44 | 15/34 | 1 | 7.9776s | 0.0685s | 1 | 8 | yes | 7.9308s | 8.0185s | `detyped_files/deltablue/advanced/proportion_sweep/main_k15_s01.py` |  |
| 0.44 | 15/34 | 2 | 1.7708s | 0.1129s | 1 | 8 | yes | 1.6936s | 1.8403s | `detyped_files/deltablue/advanced/proportion_sweep/main_k15_s02.py` |  |
| 0.44 | 15/34 | 3 | 1.5882s | 0.0418s | 1 | 8 | yes | 1.5622s | 1.6161s | `detyped_files/deltablue/advanced/proportion_sweep/main_k15_s03.py` |  |
| 0.44 | 15/34 | 4 | 2.1743s | 0.0823s | 1 | 8 | yes | 2.1199s | 2.2285s | `detyped_files/deltablue/advanced/proportion_sweep/main_k15_s04.py` |  |
| 0.44 | 15/34 | 5 | 9.1879s | 0.0996s | 1 | 8 | yes | 9.1294s | 9.2584s | `detyped_files/deltablue/advanced/proportion_sweep/main_k15_s05.py` |  |
| 0.44 | 15/34 | 6 | 1.6237s | 0.0308s | 1 | 8 | yes | 1.6037s | 1.6434s | `detyped_files/deltablue/advanced/proportion_sweep/main_k15_s06.py` |  |
| 0.44 | 15/34 | 7 | 1.5849s | 0.1105s | 1 | 8 | yes | 1.5168s | 1.6597s | `detyped_files/deltablue/advanced/proportion_sweep/main_k15_s07.py` |  |
| 0.44 | 15/34 | 8 | 1.9933s | 0.0783s | 1 | 8 | yes | 1.9490s | 2.0493s | `detyped_files/deltablue/advanced/proportion_sweep/main_k15_s08.py` |  |
| 0.44 | 15/34 | 9 | 8.6527s | 0.2001s | 1 | 8 | yes | 8.5436s | 8.7861s | `detyped_files/deltablue/advanced/proportion_sweep/main_k15_s09.py` |  |
| 0.44 | 15/34 | 10 | 1.9784s | 0.0801s | 1 | 8 | yes | 1.9255s | 2.0290s | `detyped_files/deltablue/advanced/proportion_sweep/main_k15_s10.py` |  |
| 0.44 | 15/34 | 11 | 9.1816s | 0.1043s | 1 | 8 | yes | 9.1176s | 9.2514s | `detyped_files/deltablue/advanced/proportion_sweep/main_k15_s11.py` |  |
| 0.44 | 15/34 | 12 | 6.9615s | 0.2651s | 1 | 8 | yes | 6.8037s | 7.1413s | `detyped_files/deltablue/advanced/proportion_sweep/main_k15_s12.py` |  |
| 0.44 | 15/34 | 13 | 2.3970s | 0.0886s | 1 | 8 | yes | 2.3410s | 2.4550s | `detyped_files/deltablue/advanced/proportion_sweep/main_k15_s13.py` |  |
| 0.44 | 15/34 | 14 | 2.1510s | 0.1176s | 1 | 8 | yes | 2.0731s | 2.2244s | `detyped_files/deltablue/advanced/proportion_sweep/main_k15_s14.py` |  |
| 0.44 | 15/34 | 15 | 1.8572s | 0.0952s | 1 | 8 | yes | 1.8042s | 1.9268s | `detyped_files/deltablue/advanced/proportion_sweep/main_k15_s15.py` |  |
| 0.44 | 15/34 | 16 | 8.5717s | 0.1391s | 1 | 8 | yes | 8.4818s | 8.6641s | `detyped_files/deltablue/advanced/proportion_sweep/main_k15_s16.py` |  |
| 0.44 | 15/34 | 17 | 1.6768s | 0.0795s | 1 | 8 | yes | 1.6254s | 1.7271s | `detyped_files/deltablue/advanced/proportion_sweep/main_k15_s17.py` |  |
| 0.44 | 15/34 | 18 | 2.0788s | 0.1050s | 1 | 8 | yes | 2.0096s | 2.1467s | `detyped_files/deltablue/advanced/proportion_sweep/main_k15_s18.py` |  |
| 0.44 | 15/34 | 19 | 8.0007s | 0.0281s | 1 | 8 | yes | 7.9818s | 8.0181s | `detyped_files/deltablue/advanced/proportion_sweep/main_k15_s19.py` |  |
| 0.44 | 15/34 | 20 | 2.0921s | 0.1280s | 1 | 8 | yes | 2.0168s | 2.1828s | `detyped_files/deltablue/advanced/proportion_sweep/main_k15_s20.py` |  |
| 0.47 | 16/34 | 1 | 2.0247s | 0.1007s | 1 | 8 | yes | 1.9553s | 2.0853s | `detyped_files/deltablue/advanced/proportion_sweep/main_k16_s01.py` |  |
| 0.47 | 16/34 | 2 | 8.8198s | 0.1214s | 1 | 8 | yes | 8.7404s | 8.8977s | `detyped_files/deltablue/advanced/proportion_sweep/main_k16_s02.py` |  |
| 0.47 | 16/34 | 3 | 1.5980s | 0.1083s | 1 | 8 | yes | 1.5322s | 1.6701s | `detyped_files/deltablue/advanced/proportion_sweep/main_k16_s03.py` |  |
| 0.47 | 16/34 | 4 | 1.7172s | 0.1220s | 1 | 8 | yes | 1.6434s | 1.7995s | `detyped_files/deltablue/advanced/proportion_sweep/main_k16_s04.py` |  |
| 0.47 | 16/34 | 5 | 2.1689s | 0.0713s | 1 | 8 | yes | 2.1238s | 2.2149s | `detyped_files/deltablue/advanced/proportion_sweep/main_k16_s05.py` |  |
| 0.47 | 16/34 | 6 | 1.7387s | 0.1456s | 1 | 8 | yes | 1.6537s | 1.8412s | `detyped_files/deltablue/advanced/proportion_sweep/main_k16_s06.py` |  |
| 0.47 | 16/34 | 7 | 2.3281s | 0.0633s | 1 | 8 | yes | 2.2868s | 2.3681s | `detyped_files/deltablue/advanced/proportion_sweep/main_k16_s07.py` |  |
| 0.47 | 16/34 | 8 | 2.1699s | 0.1121s | 1 | 8 | yes | 2.1018s | 2.2468s | `detyped_files/deltablue/advanced/proportion_sweep/main_k16_s08.py` |  |
| 0.47 | 16/34 | 9 | 7.1974s | 0.1573s | 1 | 8 | yes | 7.0938s | 7.2976s | `detyped_files/deltablue/advanced/proportion_sweep/main_k16_s09.py` |  |
| 0.47 | 16/34 | 10 | 2.1440s | 0.1156s | 1 | 8 | yes | 2.0710s | 2.2217s | `detyped_files/deltablue/advanced/proportion_sweep/main_k16_s10.py` |  |
| 0.47 | 16/34 | 11 | 2.3693s | 0.1088s | 1 | 8 | yes | 2.2976s | 2.4403s | `detyped_files/deltablue/advanced/proportion_sweep/main_k16_s11.py` |  |
| 0.47 | 16/34 | 12 | 8.4525s | 0.0621s | 1 | 8 | yes | 8.4132s | 8.4937s | `detyped_files/deltablue/advanced/proportion_sweep/main_k16_s12.py` |  |
| 0.47 | 16/34 | 13 | 9.7532s | 0.2355s | 1 | 8 | yes | 9.6378s | 9.9244s | `detyped_files/deltablue/advanced/proportion_sweep/main_k16_s13.py` |  |
| 0.47 | 16/34 | 14 | 8.7760s | 0.1343s | 1 | 8 | yes | 8.7046s | 8.8755s | `detyped_files/deltablue/advanced/proportion_sweep/main_k16_s14.py` |  |
| 0.47 | 16/34 | 15 | 8.9961s | 0.2177s | 1 | 8 | yes | 8.8663s | 9.1488s | `detyped_files/deltablue/advanced/proportion_sweep/main_k16_s15.py` |  |
| 0.47 | 16/34 | 16 | 8.5737s | 0.0982s | 1 | 8 | yes | 8.5086s | 8.6342s | `detyped_files/deltablue/advanced/proportion_sweep/main_k16_s16.py` |  |
| 0.47 | 16/34 | 17 | 2.1093s | 0.0887s | 1 | 8 | yes | 2.0508s | 2.1666s | `detyped_files/deltablue/advanced/proportion_sweep/main_k16_s17.py` |  |
| 0.47 | 16/34 | 18 | 6.7120s | 0.0963s | 1 | 8 | yes | 6.6486s | 6.7737s | `detyped_files/deltablue/advanced/proportion_sweep/main_k16_s18.py` |  |
| 0.47 | 16/34 | 19 | 2.0980s | 0.1150s | 1 | 8 | yes | 2.0273s | 2.1733s | `detyped_files/deltablue/advanced/proportion_sweep/main_k16_s19.py` |  |
| 0.47 | 16/34 | 20 | 2.0345s | 0.0725s | 1 | 8 | yes | 1.9914s | 2.0854s | `detyped_files/deltablue/advanced/proportion_sweep/main_k16_s20.py` |  |
| 0.50 | 17/34 | 1 | 7.7538s | 0.1722s | 1 | 8 | yes | 7.6515s | 7.8689s | `detyped_files/deltablue/advanced/proportion_sweep/main_k17_s01.py` |  |
| 0.50 | 17/34 | 2 | 1.7838s | 0.0640s | 1 | 8 | yes | 1.7438s | 1.8263s | `detyped_files/deltablue/advanced/proportion_sweep/main_k17_s02.py` |  |
| 0.50 | 17/34 | 3 | 8.3687s | 0.1232s | 1 | 8 | yes | 8.2960s | 8.4540s | `detyped_files/deltablue/advanced/proportion_sweep/main_k17_s03.py` |  |
| 0.50 | 17/34 | 4 | 8.5057s | 0.1031s | 1 | 8 | yes | 8.4501s | 8.5795s | `detyped_files/deltablue/advanced/proportion_sweep/main_k17_s04.py` |  |
| 0.50 | 17/34 | 5 | 2.1509s | 0.0772s | 1 | 8 | yes | 2.1008s | 2.1994s | `detyped_files/deltablue/advanced/proportion_sweep/main_k17_s05.py` |  |
| 0.50 | 17/34 | 6 | 6.7849s | 0.0807s | 1 | 8 | yes | 6.7289s | 6.8324s | `detyped_files/deltablue/advanced/proportion_sweep/main_k17_s06.py` |  |
| 0.50 | 17/34 | 7 | 8.9030s | 0.1511s | 1 | 8 | yes | 8.8122s | 9.0054s | `detyped_files/deltablue/advanced/proportion_sweep/main_k17_s07.py` |  |
| 0.50 | 17/34 | 8 | 8.3011s | 0.1484s | 1 | 8 | yes | 8.2161s | 8.4051s | `detyped_files/deltablue/advanced/proportion_sweep/main_k17_s08.py` |  |
| 0.50 | 17/34 | 9 | 2.6097s | 0.1054s | 1 | 8 | yes | 2.5431s | 2.6792s | `detyped_files/deltablue/advanced/proportion_sweep/main_k17_s09.py` |  |
| 0.50 | 17/34 | 10 | 2.4988s | 0.1253s | 1 | 8 | yes | 2.4231s | 2.5868s | `detyped_files/deltablue/advanced/proportion_sweep/main_k17_s10.py` |  |
| 0.50 | 17/34 | 11 | 8.4886s | 0.0861s | 1 | 8 | yes | 8.4337s | 8.5434s | `detyped_files/deltablue/advanced/proportion_sweep/main_k17_s11.py` |  |
| 0.50 | 17/34 | 12 | 8.7351s | 0.1199s | 1 | 8 | yes | 8.6618s | 8.8185s | `detyped_files/deltablue/advanced/proportion_sweep/main_k17_s12.py` |  |
| 0.50 | 17/34 | 13 | 8.2616s | 0.0972s | 1 | 8 | yes | 8.2038s | 8.3275s | `detyped_files/deltablue/advanced/proportion_sweep/main_k17_s13.py` |  |
| 0.50 | 17/34 | 14 | 9.0383s | 0.1000s | 1 | 8 | yes | 8.9820s | 9.1094s | `detyped_files/deltablue/advanced/proportion_sweep/main_k17_s14.py` |  |
| 0.50 | 17/34 | 15 | 2.0329s | 0.0694s | 1 | 8 | yes | 1.9889s | 2.0780s | `detyped_files/deltablue/advanced/proportion_sweep/main_k17_s15.py` |  |
| 0.50 | 17/34 | 16 | 9.1524s | 0.0892s | 1 | 8 | yes | 9.0947s | 9.2114s | `detyped_files/deltablue/advanced/proportion_sweep/main_k17_s16.py` |  |
| 0.50 | 17/34 | 17 | 7.9986s | 0.1259s | 1 | 8 | yes | 7.9149s | 8.0783s | `detyped_files/deltablue/advanced/proportion_sweep/main_k17_s17.py` |  |
| 0.50 | 17/34 | 18 | 1.9508s | 0.0399s | 1 | 8 | yes | 1.9246s | 1.9760s | `detyped_files/deltablue/advanced/proportion_sweep/main_k17_s18.py` |  |
| 0.50 | 17/34 | 19 | 1.9354s | 0.0691s | 1 | 8 | yes | 1.8949s | 1.9836s | `detyped_files/deltablue/advanced/proportion_sweep/main_k17_s19.py` |  |
| 0.50 | 17/34 | 20 | 8.3967s | 0.1035s | 1 | 8 | yes | 8.3351s | 8.4695s | `detyped_files/deltablue/advanced/proportion_sweep/main_k17_s20.py` |  |
| 0.53 | 18/34 | 1 | 7.9856s | 0.0764s | 1 | 8 | yes | 7.9380s | 8.0377s | `detyped_files/deltablue/advanced/proportion_sweep/main_k18_s01.py` |  |
| 0.53 | 18/34 | 2 | 2.3857s | 0.0580s | 1 | 8 | yes | 2.3457s | 2.4179s | `detyped_files/deltablue/advanced/proportion_sweep/main_k18_s02.py` |  |
| 0.53 | 18/34 | 3 | 1.6277s | 0.0794s | 1 | 8 | yes | 1.5762s | 1.6790s | `detyped_files/deltablue/advanced/proportion_sweep/main_k18_s03.py` |  |
| 0.53 | 18/34 | 4 | 8.1201s | 0.1459s | 1 | 8 | yes | 8.0269s | 8.2163s | `detyped_files/deltablue/advanced/proportion_sweep/main_k18_s04.py` |  |
| 0.53 | 18/34 | 5 | 2.1974s | 0.1247s | 1 | 8 | yes | 2.1173s | 2.2800s | `detyped_files/deltablue/advanced/proportion_sweep/main_k18_s05.py` |  |
| 0.53 | 18/34 | 6 | 7.7643s | 0.1286s | 1 | 8 | yes | 7.6867s | 7.8514s | `detyped_files/deltablue/advanced/proportion_sweep/main_k18_s06.py` |  |
| 0.53 | 18/34 | 7 | 1.7170s | 0.0835s | 1 | 8 | yes | 1.6630s | 1.7707s | `detyped_files/deltablue/advanced/proportion_sweep/main_k18_s07.py` |  |
| 0.53 | 18/34 | 8 | 9.2626s | 0.2494s | 1 | 8 | yes | 9.1406s | 9.4431s | `detyped_files/deltablue/advanced/proportion_sweep/main_k18_s08.py` |  |
| 0.53 | 18/34 | 9 | 9.6138s | 0.0965s | 1 | 8 | yes | 9.5534s | 9.6784s | `detyped_files/deltablue/advanced/proportion_sweep/main_k18_s09.py` |  |
| 0.53 | 18/34 | 10 | 2.2173s | 0.0272s | 1 | 8 | yes | 2.2014s | 2.2362s | `detyped_files/deltablue/advanced/proportion_sweep/main_k18_s10.py` |  |
| 0.53 | 18/34 | 11 | 1.6380s | 0.0662s | 1 | 8 | yes | 1.5940s | 1.6777s | `detyped_files/deltablue/advanced/proportion_sweep/main_k18_s11.py` |  |
| 0.53 | 18/34 | 12 | 9.7206s | 0.0773s | 1 | 8 | yes | 9.6699s | 9.7701s | `detyped_files/deltablue/advanced/proportion_sweep/main_k18_s12.py` |  |
| 0.53 | 18/34 | 13 | 2.0538s | 0.0849s | 1 | 8 | yes | 2.0020s | 2.1110s | `detyped_files/deltablue/advanced/proportion_sweep/main_k18_s13.py` |  |
| 0.53 | 18/34 | 14 | 9.1318s | 0.1035s | 1 | 8 | yes | 9.0621s | 9.1957s | `detyped_files/deltablue/advanced/proportion_sweep/main_k18_s14.py` |  |
| 0.53 | 18/34 | 15 | 9.1300s | 0.1041s | 1 | 8 | yes | 9.0653s | 9.1993s | `detyped_files/deltablue/advanced/proportion_sweep/main_k18_s15.py` |  |
| 0.53 | 18/34 | 16 | 2.1328s | 0.1160s | 1 | 8 | yes | 2.0588s | 2.2098s | `detyped_files/deltablue/advanced/proportion_sweep/main_k18_s16.py` |  |
| 0.53 | 18/34 | 17 | 9.1698s | 0.0846s | 1 | 8 | yes | 9.1168s | 9.2256s | `detyped_files/deltablue/advanced/proportion_sweep/main_k18_s17.py` |  |
| 0.53 | 18/34 | 18 | 2.1192s | 0.0864s | 1 | 8 | yes | 2.0605s | 2.1719s | `detyped_files/deltablue/advanced/proportion_sweep/main_k18_s18.py` |  |
| 0.53 | 18/34 | 19 | 7.2335s | 0.0867s | 1 | 8 | yes | 7.1761s | 7.2873s | `detyped_files/deltablue/advanced/proportion_sweep/main_k18_s19.py` |  |
| 0.53 | 18/34 | 20 | 2.0417s | 0.0890s | 1 | 8 | yes | 1.9887s | 2.1025s | `detyped_files/deltablue/advanced/proportion_sweep/main_k18_s20.py` |  |
| 0.56 | 19/34 | 1 | 8.5240s | 0.0857s | 1 | 8 | yes | 8.4643s | 8.5720s | `detyped_files/deltablue/advanced/proportion_sweep/main_k19_s01.py` |  |
| 0.56 | 19/34 | 2 | 1.9645s | 0.0960s | 1 | 8 | yes | 1.9032s | 2.0257s | `detyped_files/deltablue/advanced/proportion_sweep/main_k19_s02.py` |  |
| 0.56 | 19/34 | 3 | 1.6253s | 0.0801s | 1 | 8 | yes | 1.5685s | 1.6727s | `detyped_files/deltablue/advanced/proportion_sweep/main_k19_s03.py` |  |
| 0.56 | 19/34 | 4 | 2.2400s | 0.1050s | 1 | 8 | yes | 2.1754s | 2.3086s | `detyped_files/deltablue/advanced/proportion_sweep/main_k19_s04.py` |  |
| 0.56 | 19/34 | 5 | 2.6570s | 0.0763s | 1 | 8 | yes | 2.6039s | 2.7011s | `detyped_files/deltablue/advanced/proportion_sweep/main_k19_s05.py` |  |
| 0.56 | 19/34 | 6 | 7.2891s | 0.0364s | 1 | 8 | yes | 7.2671s | 7.3140s | `detyped_files/deltablue/advanced/proportion_sweep/main_k19_s06.py` |  |
| 0.56 | 19/34 | 7 | 9.6356s | 0.0839s | 1 | 8 | yes | 9.5830s | 9.6919s | `detyped_files/deltablue/advanced/proportion_sweep/main_k19_s07.py` |  |
| 0.56 | 19/34 | 8 | 2.1890s | 0.0439s | 1 | 8 | yes | 2.1565s | 2.2116s | `detyped_files/deltablue/advanced/proportion_sweep/main_k19_s08.py` |  |
| 0.56 | 19/34 | 9 | 1.7216s | 0.0358s | 1 | 8 | yes | 1.6985s | 1.7445s | `detyped_files/deltablue/advanced/proportion_sweep/main_k19_s09.py` |  |
| 0.56 | 19/34 | 10 | 7.3726s | 0.1194s | 1 | 8 | yes | 7.3042s | 7.4576s | `detyped_files/deltablue/advanced/proportion_sweep/main_k19_s10.py` |  |
| 0.56 | 19/34 | 11 | 2.1465s | 0.0793s | 1 | 8 | yes | 2.0970s | 2.1983s | `detyped_files/deltablue/advanced/proportion_sweep/main_k19_s11.py` |  |
| 0.56 | 19/34 | 12 | 7.5503s | 0.0841s | 1 | 8 | yes | 7.4926s | 7.6008s | `detyped_files/deltablue/advanced/proportion_sweep/main_k19_s12.py` |  |
| 0.56 | 19/34 | 13 | 2.1172s | 0.1085s | 1 | 8 | yes | 2.0435s | 2.1834s | `detyped_files/deltablue/advanced/proportion_sweep/main_k19_s13.py` |  |
| 0.56 | 19/34 | 14 | 1.6411s | 0.0457s | 1 | 8 | yes | 1.6160s | 1.6748s | `detyped_files/deltablue/advanced/proportion_sweep/main_k19_s14.py` |  |
| 0.56 | 19/34 | 15 | 2.6925s | 0.0919s | 1 | 8 | yes | 2.6331s | 2.7487s | `detyped_files/deltablue/advanced/proportion_sweep/main_k19_s15.py` |  |
| 0.56 | 19/34 | 16 | 2.6826s | 0.0626s | 1 | 8 | yes | 2.6433s | 2.7225s | `detyped_files/deltablue/advanced/proportion_sweep/main_k19_s16.py` |  |
| 0.56 | 19/34 | 17 | 8.4660s | 0.0507s | 1 | 8 | yes | 8.4339s | 8.5003s | `detyped_files/deltablue/advanced/proportion_sweep/main_k19_s17.py` |  |
| 0.56 | 19/34 | 18 | 2.0975s | 0.0819s | 1 | 8 | yes | 2.0474s | 2.1546s | `detyped_files/deltablue/advanced/proportion_sweep/main_k19_s18.py` |  |
| 0.56 | 19/34 | 19 | 6.8923s | 0.0997s | 1 | 8 | yes | 6.8308s | 6.9581s | `detyped_files/deltablue/advanced/proportion_sweep/main_k19_s19.py` |  |
| 0.56 | 19/34 | 20 | 7.1786s | 0.1027s | 1 | 8 | yes | 7.1144s | 7.2475s | `detyped_files/deltablue/advanced/proportion_sweep/main_k19_s20.py` |  |
| 0.59 | 20/34 | 1 | 10.2722s | 0.1241s | 1 | 8 | yes | 10.1970s | 10.3553s | `detyped_files/deltablue/advanced/proportion_sweep/main_k20_s01.py` |  |
| 0.59 | 20/34 | 2 | 8.8457s | 0.0661s | 1 | 8 | yes | 8.7995s | 8.8849s | `detyped_files/deltablue/advanced/proportion_sweep/main_k20_s02.py` |  |
| 0.59 | 20/34 | 3 | 2.4548s | 0.0889s | 1 | 8 | yes | 2.4002s | 2.5149s | `detyped_files/deltablue/advanced/proportion_sweep/main_k20_s03.py` |  |
| 0.59 | 20/34 | 4 | 9.3276s | 0.1089s | 1 | 8 | yes | 9.2637s | 9.4032s | `detyped_files/deltablue/advanced/proportion_sweep/main_k20_s04.py` |  |
| 0.59 | 20/34 | 5 | 8.5312s | 0.0852s | 1 | 8 | yes | 8.4802s | 8.5904s | `detyped_files/deltablue/advanced/proportion_sweep/main_k20_s05.py` |  |
| 0.59 | 20/34 | 6 | 8.3865s | 0.0921s | 1 | 8 | yes | 8.3314s | 8.4505s | `detyped_files/deltablue/advanced/proportion_sweep/main_k20_s06.py` |  |
| 0.59 | 20/34 | 7 | 1.6106s | 0.1325s | 1 | 8 | yes | 1.5296s | 1.6997s | `detyped_files/deltablue/advanced/proportion_sweep/main_k20_s07.py` |  |
| 0.59 | 20/34 | 8 | 10.1255s | 0.1846s | 1 | 8 | yes | 10.0128s | 10.2507s | `detyped_files/deltablue/advanced/proportion_sweep/main_k20_s08.py` |  |
| 0.59 | 20/34 | 9 | 9.5555s | 0.1457s | 1 | 8 | yes | 9.4648s | 9.6505s | `detyped_files/deltablue/advanced/proportion_sweep/main_k20_s09.py` |  |
| 0.59 | 20/34 | 10 | 2.6609s | 0.0907s | 1 | 8 | yes | 2.5988s | 2.7145s | `detyped_files/deltablue/advanced/proportion_sweep/main_k20_s10.py` |  |
| 0.59 | 20/34 | 11 | 7.3038s | 0.1576s | 1 | 8 | yes | 7.2121s | 7.4134s | `detyped_files/deltablue/advanced/proportion_sweep/main_k20_s11.py` |  |
| 0.59 | 20/34 | 12 | 9.2336s | 0.1048s | 1 | 8 | yes | 9.1665s | 9.3015s | `detyped_files/deltablue/advanced/proportion_sweep/main_k20_s12.py` |  |
| 0.59 | 20/34 | 13 | 1.5308s | 0.0929s | 1 | 8 | yes | 1.4877s | 1.5991s | `detyped_files/deltablue/advanced/proportion_sweep/main_k20_s13.py` |  |
| 0.59 | 20/34 | 14 | 8.3395s | 0.0771s | 1 | 8 | yes | 8.2914s | 8.3911s | `detyped_files/deltablue/advanced/proportion_sweep/main_k20_s14.py` |  |
| 0.59 | 20/34 | 15 | 8.4599s | 0.0728s | 1 | 8 | yes | 8.4147s | 8.5121s | `detyped_files/deltablue/advanced/proportion_sweep/main_k20_s15.py` |  |
| 0.59 | 20/34 | 16 | 8.3157s | 0.0989s | 1 | 8 | yes | 8.2556s | 8.3834s | `detyped_files/deltablue/advanced/proportion_sweep/main_k20_s16.py` |  |
| 0.59 | 20/34 | 17 | 9.5582s | 0.0948s | 1 | 8 | yes | 9.4948s | 9.6176s | `detyped_files/deltablue/advanced/proportion_sweep/main_k20_s17.py` |  |
| 0.59 | 20/34 | 18 | 2.1533s | 0.0787s | 1 | 8 | yes | 2.1019s | 2.2039s | `detyped_files/deltablue/advanced/proportion_sweep/main_k20_s18.py` |  |
| 0.59 | 20/34 | 19 | 8.1625s | 0.1325s | 1 | 8 | yes | 8.0798s | 8.2481s | `detyped_files/deltablue/advanced/proportion_sweep/main_k20_s19.py` |  |
| 0.59 | 20/34 | 20 | 7.9692s | 0.1644s | 1 | 8 | yes | 7.8734s | 8.0898s | `detyped_files/deltablue/advanced/proportion_sweep/main_k20_s20.py` |  |
| 0.62 | 21/34 | 1 | 2.2548s | 0.0903s | 1 | 8 | yes | 2.2010s | 2.3158s | `detyped_files/deltablue/advanced/proportion_sweep/main_k21_s01.py` |  |
| 0.62 | 21/34 | 2 | 8.3137s | 0.1100s | 1 | 8 | yes | 8.2436s | 8.3852s | `detyped_files/deltablue/advanced/proportion_sweep/main_k21_s02.py` |  |
| 0.62 | 21/34 | 3 | 7.3019s | 0.0963s | 1 | 8 | yes | 7.2405s | 7.3653s | `detyped_files/deltablue/advanced/proportion_sweep/main_k21_s03.py` |  |
| 0.62 | 21/34 | 4 | 7.9909s | 0.1059s | 1 | 8 | yes | 7.9229s | 8.0588s | `detyped_files/deltablue/advanced/proportion_sweep/main_k21_s04.py` |  |
| 0.62 | 21/34 | 5 | 2.5871s | 0.0890s | 1 | 8 | yes | 2.5291s | 2.6424s | `detyped_files/deltablue/advanced/proportion_sweep/main_k21_s05.py` |  |
| 0.62 | 21/34 | 6 | 2.5498s | 0.0524s | 1 | 8 | yes | 2.5133s | 2.5810s | `detyped_files/deltablue/advanced/proportion_sweep/main_k21_s06.py` |  |
| 0.62 | 21/34 | 7 | 6.8012s | 0.0634s | 1 | 8 | yes | 6.7611s | 6.8424s | `detyped_files/deltablue/advanced/proportion_sweep/main_k21_s07.py` |  |
| 0.62 | 21/34 | 8 | 2.5518s | 0.0927s | 1 | 8 | yes | 2.4882s | 2.6085s | `detyped_files/deltablue/advanced/proportion_sweep/main_k21_s08.py` |  |
| 0.62 | 21/34 | 9 | 2.2855s | 0.0976s | 1 | 8 | yes | 2.2206s | 2.3448s | `detyped_files/deltablue/advanced/proportion_sweep/main_k21_s09.py` |  |
| 0.62 | 21/34 | 10 | 2.1971s | 0.0668s | 1 | 8 | yes | 2.1544s | 2.2393s | `detyped_files/deltablue/advanced/proportion_sweep/main_k21_s10.py` |  |
| 0.62 | 21/34 | 11 | 9.7990s | 0.1333s | 1 | 8 | yes | 9.7140s | 9.8855s | `detyped_files/deltablue/advanced/proportion_sweep/main_k21_s11.py` |  |
| 0.62 | 21/34 | 12 | 8.6640s | 0.1457s | 1 | 8 | yes | 8.5717s | 8.7615s | `detyped_files/deltablue/advanced/proportion_sweep/main_k21_s12.py` |  |
| 0.62 | 21/34 | 13 | 9.2982s | 0.1151s | 1 | 8 | yes | 9.2214s | 9.3695s | `detyped_files/deltablue/advanced/proportion_sweep/main_k21_s13.py` |  |
| 0.62 | 21/34 | 14 | 9.3662s | 0.0650s | 1 | 8 | yes | 9.3257s | 9.4095s | `detyped_files/deltablue/advanced/proportion_sweep/main_k21_s14.py` |  |
| 0.62 | 21/34 | 15 | 8.4516s | 0.1067s | 1 | 8 | yes | 8.3813s | 8.5187s | `detyped_files/deltablue/advanced/proportion_sweep/main_k21_s15.py` |  |
| 0.62 | 21/34 | 16 | 8.3215s | 0.0640s | 1 | 8 | yes | 8.2806s | 8.3625s | `detyped_files/deltablue/advanced/proportion_sweep/main_k21_s16.py` |  |
| 0.62 | 21/34 | 17 | 8.3596s | 0.0674s | 1 | 8 | yes | 8.3173s | 8.4033s | `detyped_files/deltablue/advanced/proportion_sweep/main_k21_s17.py` |  |
| 0.62 | 21/34 | 18 | 2.4480s | 0.0822s | 1 | 8 | yes | 2.3933s | 2.4994s | `detyped_files/deltablue/advanced/proportion_sweep/main_k21_s18.py` |  |
| 0.62 | 21/34 | 19 | 8.0737s | 0.1110s | 1 | 8 | yes | 8.0073s | 8.1483s | `detyped_files/deltablue/advanced/proportion_sweep/main_k21_s19.py` |  |
| 0.62 | 21/34 | 20 | 9.3612s | 0.0977s | 1 | 8 | yes | 9.3014s | 9.4285s | `detyped_files/deltablue/advanced/proportion_sweep/main_k21_s20.py` |  |
| 0.65 | 22/34 | 1 | 7.2932s | 0.1511s | 1 | 8 | yes | 7.2001s | 7.3927s | `detyped_files/deltablue/advanced/proportion_sweep/main_k22_s01.py` |  |
| 0.65 | 22/34 | 2 | 8.4976s | 0.0890s | 1 | 8 | yes | 8.4397s | 8.5560s | `detyped_files/deltablue/advanced/proportion_sweep/main_k22_s02.py` |  |
| 0.65 | 22/34 | 3 | 7.6631s | 0.1346s | 1 | 8 | yes | 7.5761s | 7.7526s | `detyped_files/deltablue/advanced/proportion_sweep/main_k22_s03.py` |  |
| 0.65 | 22/34 | 4 | 9.4147s | 0.1571s | 1 | 8 | yes | 9.3322s | 9.5278s | `detyped_files/deltablue/advanced/proportion_sweep/main_k22_s04.py` |  |
| 0.65 | 22/34 | 5 | 2.8036s | 0.1597s | 1 | 8 | yes | 2.7110s | 2.9182s | `detyped_files/deltablue/advanced/proportion_sweep/main_k22_s05.py` |  |
| 0.65 | 22/34 | 6 | 8.9426s | 0.1057s | 1 | 8 | yes | 8.8774s | 9.0124s | `detyped_files/deltablue/advanced/proportion_sweep/main_k22_s06.py` |  |
| 0.65 | 22/34 | 7 | 2.2272s | 0.0776s | 1 | 8 | yes | 2.1763s | 2.2783s | `detyped_files/deltablue/advanced/proportion_sweep/main_k22_s07.py` |  |
| 0.65 | 22/34 | 8 | 8.5326s | 0.1254s | 1 | 8 | yes | 8.4576s | 8.6204s | `detyped_files/deltablue/advanced/proportion_sweep/main_k22_s08.py` |  |
| 0.65 | 22/34 | 9 | 7.6520s | 0.0687s | 1 | 8 | yes | 7.6126s | 7.7028s | `detyped_files/deltablue/advanced/proportion_sweep/main_k22_s09.py` |  |
| 0.65 | 22/34 | 10 | 10.0844s | 0.1216s | 1 | 8 | yes | 10.0040s | 10.1604s | `detyped_files/deltablue/advanced/proportion_sweep/main_k22_s10.py` |  |
| 0.65 | 22/34 | 11 | 9.7667s | 0.1052s | 1 | 8 | yes | 9.6999s | 9.8343s | `detyped_files/deltablue/advanced/proportion_sweep/main_k22_s11.py` |  |
| 0.65 | 22/34 | 12 | 7.9526s | 0.1014s | 1 | 8 | yes | 7.8870s | 8.0174s | `detyped_files/deltablue/advanced/proportion_sweep/main_k22_s12.py` |  |
| 0.65 | 22/34 | 13 | 9.7027s | 0.0682s | 1 | 8 | yes | 9.6614s | 9.7501s | `detyped_files/deltablue/advanced/proportion_sweep/main_k22_s13.py` |  |
| 0.65 | 22/34 | 14 | 10.0773s | 0.0958s | 1 | 8 | yes | 10.0132s | 10.1370s | `detyped_files/deltablue/advanced/proportion_sweep/main_k22_s14.py` |  |
| 0.65 | 22/34 | 15 | 2.2639s | 0.0728s | 1 | 8 | yes | 2.2199s | 2.3144s | `detyped_files/deltablue/advanced/proportion_sweep/main_k22_s15.py` |  |
| 0.65 | 22/34 | 16 | 9.7706s | 0.1386s | 1 | 8 | yes | 9.6714s | 9.8539s | `detyped_files/deltablue/advanced/proportion_sweep/main_k22_s16.py` |  |
| 0.65 | 22/34 | 17 | 10.2159s | 0.1301s | 1 | 8 | yes | 10.1565s | 10.3099s | `detyped_files/deltablue/advanced/proportion_sweep/main_k22_s17.py` |  |
| 0.65 | 22/34 | 18 | 8.9550s | 0.0739s | 1 | 8 | yes | 8.9062s | 9.0010s | `detyped_files/deltablue/advanced/proportion_sweep/main_k22_s18.py` |  |
| 0.65 | 22/34 | 19 | 2.7806s | 0.1080s | 1 | 8 | yes | 2.7121s | 2.8518s | `detyped_files/deltablue/advanced/proportion_sweep/main_k22_s19.py` |  |
| 0.65 | 22/34 | 20 | 8.5713s | 0.1399s | 1 | 8 | yes | 8.4889s | 8.6705s | `detyped_files/deltablue/advanced/proportion_sweep/main_k22_s20.py` |  |
| 0.68 | 23/34 | 1 | 8.8952s | 0.0979s | 1 | 8 | yes | 8.8338s | 8.9597s | `detyped_files/deltablue/advanced/proportion_sweep/main_k23_s01.py` |  |
| 0.68 | 23/34 | 2 | 2.1743s | 0.1352s | 1 | 8 | yes | 2.0953s | 2.2721s | `detyped_files/deltablue/advanced/proportion_sweep/main_k23_s02.py` |  |
| 0.68 | 23/34 | 3 | 2.7286s | 0.0772s | 1 | 8 | yes | 2.6792s | 2.7776s | `detyped_files/deltablue/advanced/proportion_sweep/main_k23_s03.py` |  |
| 0.68 | 23/34 | 4 | 2.4324s | 0.0739s | 1 | 8 | yes | 2.3871s | 2.4819s | `detyped_files/deltablue/advanced/proportion_sweep/main_k23_s04.py` |  |
| 0.68 | 23/34 | 5 | 9.8664s | 0.1998s | 1 | 8 | yes | 9.7621s | 10.0152s | `detyped_files/deltablue/advanced/proportion_sweep/main_k23_s05.py` |  |
| 0.68 | 23/34 | 6 | 8.0117s | 0.0696s | 1 | 8 | yes | 7.9657s | 8.0546s | `detyped_files/deltablue/advanced/proportion_sweep/main_k23_s06.py` |  |
| 0.68 | 23/34 | 7 | 7.3754s | 0.0694s | 1 | 8 | yes | 7.3282s | 7.4168s | `detyped_files/deltablue/advanced/proportion_sweep/main_k23_s07.py` |  |
| 0.68 | 23/34 | 8 | 2.8105s | 0.1163s | 1 | 8 | yes | 2.7350s | 2.8840s | `detyped_files/deltablue/advanced/proportion_sweep/main_k23_s08.py` |  |
| 0.68 | 23/34 | 9 | 8.5405s | 0.1109s | 1 | 8 | yes | 8.4689s | 8.6148s | `detyped_files/deltablue/advanced/proportion_sweep/main_k23_s09.py` |  |
| 0.68 | 23/34 | 10 | 10.0604s | 0.1415s | 1 | 8 | yes | 9.9623s | 10.1437s | `detyped_files/deltablue/advanced/proportion_sweep/main_k23_s10.py` |  |
| 0.68 | 23/34 | 11 | 8.6631s | 0.0781s | 1 | 8 | yes | 8.6165s | 8.7165s | `detyped_files/deltablue/advanced/proportion_sweep/main_k23_s11.py` |  |
| 0.68 | 23/34 | 12 | 8.7170s | 0.1622s | 1 | 8 | yes | 8.6219s | 8.8311s | `detyped_files/deltablue/advanced/proportion_sweep/main_k23_s12.py` |  |
| 0.68 | 23/34 | 13 | 7.7546s | 0.1426s | 1 | 8 | yes | 7.6691s | 7.8496s | `detyped_files/deltablue/advanced/proportion_sweep/main_k23_s13.py` |  |
| 0.68 | 23/34 | 14 | 2.6569s | 0.1224s | 1 | 8 | yes | 2.5811s | 2.7399s | `detyped_files/deltablue/advanced/proportion_sweep/main_k23_s14.py` |  |
| 0.68 | 23/34 | 15 | 9.8011s | 0.1231s | 1 | 8 | yes | 9.7186s | 9.8765s | `detyped_files/deltablue/advanced/proportion_sweep/main_k23_s15.py` |  |
| 0.68 | 23/34 | 16 | 2.6486s | 0.0823s | 1 | 8 | yes | 2.5949s | 2.7021s | `detyped_files/deltablue/advanced/proportion_sweep/main_k23_s16.py` |  |
| 0.68 | 23/34 | 17 | 8.5641s | 0.1603s | 1 | 8 | yes | 8.4662s | 8.6751s | `detyped_files/deltablue/advanced/proportion_sweep/main_k23_s17.py` |  |
| 0.68 | 23/34 | 18 | 9.3921s | 0.0861s | 1 | 8 | yes | 9.3329s | 9.4458s | `detyped_files/deltablue/advanced/proportion_sweep/main_k23_s18.py` |  |
| 0.68 | 23/34 | 19 | 2.0012s | 0.0498s | 1 | 8 | yes | 1.9670s | 2.0313s | `detyped_files/deltablue/advanced/proportion_sweep/main_k23_s19.py` |  |
| 0.68 | 23/34 | 20 | 8.3836s | 0.0805s | 1 | 8 | yes | 8.3337s | 8.4374s | `detyped_files/deltablue/advanced/proportion_sweep/main_k23_s20.py` |  |
| 0.71 | 24/34 | 1 | 8.9382s | 0.1307s | 1 | 8 | yes | 8.8500s | 9.0207s | `detyped_files/deltablue/advanced/proportion_sweep/main_k24_s01.py` |  |
| 0.71 | 24/34 | 2 | 10.1526s | 0.1018s | 1 | 8 | yes | 10.1001s | 10.2263s | `detyped_files/deltablue/advanced/proportion_sweep/main_k24_s02.py` |  |
| 0.71 | 24/34 | 3 | 8.3932s | 0.0957s | 1 | 8 | yes | 8.3441s | 8.4634s | `detyped_files/deltablue/advanced/proportion_sweep/main_k24_s03.py` |  |
| 0.71 | 24/34 | 4 | 9.2741s | 0.0428s | 1 | 8 | yes | 9.2476s | 9.3027s | `detyped_files/deltablue/advanced/proportion_sweep/main_k24_s04.py` |  |
| 0.71 | 24/34 | 5 | 9.7874s | 0.0956s | 1 | 8 | yes | 9.7246s | 9.8489s | `detyped_files/deltablue/advanced/proportion_sweep/main_k24_s05.py` |  |
| 0.71 | 24/34 | 6 | 9.0258s | 0.1252s | 1 | 8 | yes | 8.9489s | 9.1081s | `detyped_files/deltablue/advanced/proportion_sweep/main_k24_s06.py` |  |
| 0.71 | 24/34 | 7 | 9.0182s | 0.1246s | 1 | 8 | yes | 8.9419s | 9.1033s | `detyped_files/deltablue/advanced/proportion_sweep/main_k24_s07.py` |  |
| 0.71 | 24/34 | 8 | 2.1960s | 0.0665s | 1 | 8 | yes | 2.1522s | 2.2364s | `detyped_files/deltablue/advanced/proportion_sweep/main_k24_s08.py` |  |
| 0.71 | 24/34 | 9 | 7.7088s | 0.0537s | 1 | 8 | yes | 7.6734s | 7.7426s | `detyped_files/deltablue/advanced/proportion_sweep/main_k24_s09.py` |  |
| 0.71 | 24/34 | 10 | 10.2247s | 0.1346s | 1 | 8 | yes | 10.1488s | 10.3242s | `detyped_files/deltablue/advanced/proportion_sweep/main_k24_s10.py` |  |
| 0.71 | 24/34 | 11 | 2.2804s | 0.0496s | 1 | 8 | yes | 2.2492s | 2.3134s | `detyped_files/deltablue/advanced/proportion_sweep/main_k24_s11.py` |  |
| 0.71 | 24/34 | 12 | 9.7569s | 0.0964s | 1 | 8 | yes | 9.7040s | 9.8271s | `detyped_files/deltablue/advanced/proportion_sweep/main_k24_s12.py` |  |
| 0.71 | 24/34 | 13 | 1.5820s | 0.0940s | 1 | 8 | yes | 1.5214s | 1.6421s | `detyped_files/deltablue/advanced/proportion_sweep/main_k24_s13.py` |  |
| 0.71 | 24/34 | 14 | 8.5055s | 0.0875s | 1 | 8 | yes | 8.4452s | 8.5595s | `detyped_files/deltablue/advanced/proportion_sweep/main_k24_s14.py` |  |
| 0.71 | 24/34 | 15 | 9.4045s | 0.0622s | 1 | 8 | yes | 9.3648s | 9.4435s | `detyped_files/deltablue/advanced/proportion_sweep/main_k24_s15.py` |  |
| 0.71 | 24/34 | 16 | 2.7203s | 0.0800s | 1 | 8 | yes | 2.6707s | 2.7737s | `detyped_files/deltablue/advanced/proportion_sweep/main_k24_s16.py` |  |
| 0.71 | 24/34 | 17 | 9.3025s | 0.1677s | 1 | 8 | yes | 9.2134s | 9.4223s | `detyped_files/deltablue/advanced/proportion_sweep/main_k24_s17.py` |  |
| 0.71 | 24/34 | 18 | 7.6585s | 0.0571s | 1 | 8 | yes | 7.6214s | 7.6950s | `detyped_files/deltablue/advanced/proportion_sweep/main_k24_s18.py` |  |
| 0.71 | 24/34 | 19 | 2.5207s | 0.1187s | 1 | 8 | yes | 2.4476s | 2.6018s | `detyped_files/deltablue/advanced/proportion_sweep/main_k24_s19.py` |  |
| 0.71 | 24/34 | 20 | 10.2414s | 0.1878s | 1 | 8 | yes | 10.1326s | 10.3724s | `detyped_files/deltablue/advanced/proportion_sweep/main_k24_s20.py` |  |
| 0.74 | 25/34 | 1 | 2.2505s | 0.0538s | 1 | 8 | yes | 2.2163s | 2.2868s | `detyped_files/deltablue/advanced/proportion_sweep/main_k25_s01.py` |  |
| 0.74 | 25/34 | 2 | 2.1419s | 0.0765s | 1 | 8 | yes | 2.0909s | 2.1893s | `detyped_files/deltablue/advanced/proportion_sweep/main_k25_s02.py` |  |
| 0.74 | 25/34 | 3 | 9.8103s | 0.1007s | 1 | 8 | yes | 9.7460s | 9.8757s | `detyped_files/deltablue/advanced/proportion_sweep/main_k25_s03.py` |  |
| 0.74 | 25/34 | 4 | 7.8486s | 0.1316s | 1 | 8 | yes | 7.7640s | 7.9347s | `detyped_files/deltablue/advanced/proportion_sweep/main_k25_s04.py` |  |
| 0.74 | 25/34 | 5 | 9.9661s | 0.1390s | 1 | 8 | yes | 9.8697s | 10.0511s | `detyped_files/deltablue/advanced/proportion_sweep/main_k25_s05.py` |  |
| 0.74 | 25/34 | 6 | 10.1998s | 0.0761s | 1 | 8 | yes | 10.1505s | 10.2481s | `detyped_files/deltablue/advanced/proportion_sweep/main_k25_s06.py` |  |
| 0.74 | 25/34 | 7 | 7.6533s | 0.0854s | 1 | 8 | yes | 7.5967s | 7.7071s | `detyped_files/deltablue/advanced/proportion_sweep/main_k25_s07.py` |  |
| 0.74 | 25/34 | 8 | 2.6141s | 0.0985s | 1 | 8 | yes | 2.5576s | 2.6850s | `detyped_files/deltablue/advanced/proportion_sweep/main_k25_s08.py` |  |
| 0.74 | 25/34 | 9 | 8.5922s | 0.0872s | 1 | 8 | yes | 8.5324s | 8.6442s | `detyped_files/deltablue/advanced/proportion_sweep/main_k25_s09.py` |  |
| 0.74 | 25/34 | 10 | 8.8803s | 0.1140s | 1 | 8 | yes | 8.8048s | 8.9507s | `detyped_files/deltablue/advanced/proportion_sweep/main_k25_s10.py` |  |
| 0.74 | 25/34 | 11 | 10.1850s | 0.1370s | 1 | 8 | yes | 10.0981s | 10.2725s | `detyped_files/deltablue/advanced/proportion_sweep/main_k25_s11.py` |  |
| 0.74 | 25/34 | 12 | 7.7569s | 0.1142s | 1 | 8 | yes | 7.6818s | 7.8288s | `detyped_files/deltablue/advanced/proportion_sweep/main_k25_s12.py` |  |
| 0.74 | 25/34 | 13 | 2.3127s | 0.0481s | 1 | 8 | yes | 2.2792s | 2.3413s | `detyped_files/deltablue/advanced/proportion_sweep/main_k25_s13.py` |  |
| 0.74 | 25/34 | 14 | 10.1799s | 0.0850s | 1 | 8 | yes | 10.1258s | 10.2348s | `detyped_files/deltablue/advanced/proportion_sweep/main_k25_s14.py` |  |
| 0.74 | 25/34 | 15 | 8.6736s | 0.0965s | 1 | 8 | yes | 8.6163s | 8.7428s | `detyped_files/deltablue/advanced/proportion_sweep/main_k25_s15.py` |  |
| 0.74 | 25/34 | 16 | 9.6416s | 0.1145s | 1 | 8 | yes | 9.5691s | 9.7188s | `detyped_files/deltablue/advanced/proportion_sweep/main_k25_s16.py` |  |
| 0.74 | 25/34 | 17 | 7.3352s | 0.1089s | 1 | 8 | yes | 7.2647s | 7.4058s | `detyped_files/deltablue/advanced/proportion_sweep/main_k25_s17.py` |  |
| 0.74 | 25/34 | 18 | 9.0729s | 0.0948s | 1 | 8 | yes | 9.0136s | 9.1361s | `detyped_files/deltablue/advanced/proportion_sweep/main_k25_s18.py` |  |
| 0.74 | 25/34 | 19 | 2.8424s | 0.1822s | 1 | 8 | yes | 2.7410s | 2.9698s | `detyped_files/deltablue/advanced/proportion_sweep/main_k25_s19.py` |  |
| 0.74 | 25/34 | 20 | 10.1519s | 0.1827s | 1 | 8 | yes | 10.0551s | 10.2883s | `detyped_files/deltablue/advanced/proportion_sweep/main_k25_s20.py` |  |
| 0.76 | 26/34 | 1 | 10.2569s | 0.1666s | 1 | 8 | yes | 10.1520s | 10.3661s | `detyped_files/deltablue/advanced/proportion_sweep/main_k26_s01.py` |  |
| 0.76 | 26/34 | 2 | 2.6673s | 0.1593s | 1 | 8 | yes | 2.5825s | 2.7835s | `detyped_files/deltablue/advanced/proportion_sweep/main_k26_s02.py` |  |
| 0.76 | 26/34 | 3 | 8.4624s | 0.1262s | 1 | 8 | yes | 8.3883s | 8.5525s | `detyped_files/deltablue/advanced/proportion_sweep/main_k26_s03.py` |  |
| 0.76 | 26/34 | 4 | 10.0304s | 0.1559s | 1 | 8 | yes | 9.9371s | 10.1377s | `detyped_files/deltablue/advanced/proportion_sweep/main_k26_s04.py` |  |
| 0.76 | 26/34 | 5 | 9.1194s | 0.1222s | 1 | 8 | yes | 9.0389s | 9.1970s | `detyped_files/deltablue/advanced/proportion_sweep/main_k26_s05.py` |  |
| 0.76 | 26/34 | 6 | 8.6001s | 0.1059s | 1 | 8 | yes | 8.5301s | 8.6661s | `detyped_files/deltablue/advanced/proportion_sweep/main_k26_s06.py` |  |
| 0.76 | 26/34 | 7 | 8.5978s | 0.1150s | 1 | 8 | yes | 8.5300s | 8.6759s | `detyped_files/deltablue/advanced/proportion_sweep/main_k26_s07.py` |  |
| 0.76 | 26/34 | 8 | 8.9273s | 0.1293s | 1 | 8 | yes | 8.8438s | 9.0084s | `detyped_files/deltablue/advanced/proportion_sweep/main_k26_s08.py` |  |
| 0.76 | 26/34 | 9 | 7.4504s | 0.0832s | 1 | 8 | yes | 7.3929s | 7.5010s | `detyped_files/deltablue/advanced/proportion_sweep/main_k26_s09.py` |  |
| 0.76 | 26/34 | 10 | 9.8029s | 0.0565s | 1 | 8 | yes | 9.7715s | 9.8432s | `detyped_files/deltablue/advanced/proportion_sweep/main_k26_s10.py` |  |
| 0.76 | 26/34 | 11 | 2.5474s | 0.1268s | 1 | 8 | yes | 2.4693s | 2.6321s | `detyped_files/deltablue/advanced/proportion_sweep/main_k26_s11.py` |  |
| 0.76 | 26/34 | 12 | 2.3342s | 0.1213s | 1 | 8 | yes | 2.2580s | 2.4137s | `detyped_files/deltablue/advanced/proportion_sweep/main_k26_s12.py` |  |
| 0.76 | 26/34 | 13 | 10.2209s | 0.1542s | 1 | 8 | yes | 10.1197s | 10.3177s | `detyped_files/deltablue/advanced/proportion_sweep/main_k26_s13.py` |  |
| 0.76 | 26/34 | 14 | 10.1995s | 0.1018s | 1 | 8 | yes | 10.1385s | 10.2665s | `detyped_files/deltablue/advanced/proportion_sweep/main_k26_s14.py` |  |
| 0.76 | 26/34 | 15 | 10.3329s | 0.1743s | 1 | 8 | yes | 10.2298s | 10.4542s | `detyped_files/deltablue/advanced/proportion_sweep/main_k26_s15.py` |  |
| 0.76 | 26/34 | 16 | 10.1832s | 0.1271s | 1 | 8 | yes | 10.1009s | 10.2651s | `detyped_files/deltablue/advanced/proportion_sweep/main_k26_s16.py` |  |
| 0.76 | 26/34 | 17 | 10.1370s | 0.1495s | 1 | 8 | yes | 10.0406s | 10.2334s | `detyped_files/deltablue/advanced/proportion_sweep/main_k26_s17.py` |  |
| 0.76 | 26/34 | 18 | 8.5834s | 0.1109s | 1 | 8 | yes | 8.5192s | 8.6620s | `detyped_files/deltablue/advanced/proportion_sweep/main_k26_s18.py` |  |
| 0.76 | 26/34 | 19 | 2.4291s | 0.1063s | 1 | 8 | yes | 2.3707s | 2.5063s | `detyped_files/deltablue/advanced/proportion_sweep/main_k26_s19.py` |  |
| 0.76 | 26/34 | 20 | 10.1844s | 0.0668s | 1 | 8 | yes | 10.1431s | 10.2290s | `detyped_files/deltablue/advanced/proportion_sweep/main_k26_s20.py` |  |
| 0.79 | 27/34 | 1 | 9.0497s | 0.0597s | 1 | 8 | yes | 9.0094s | 9.0856s | `detyped_files/deltablue/advanced/proportion_sweep/main_k27_s01.py` |  |
| 0.79 | 27/34 | 2 | 2.6470s | 0.1154s | 1 | 8 | yes | 2.5750s | 2.7246s | `detyped_files/deltablue/advanced/proportion_sweep/main_k27_s02.py` |  |
| 0.79 | 27/34 | 3 | 9.7409s | 0.1081s | 1 | 8 | yes | 9.6851s | 9.8197s | `detyped_files/deltablue/advanced/proportion_sweep/main_k27_s03.py` |  |
| 0.79 | 27/34 | 4 | 10.1541s | 0.1157s | 1 | 8 | yes | 10.0754s | 10.2240s | `detyped_files/deltablue/advanced/proportion_sweep/main_k27_s04.py` |  |
| 0.79 | 27/34 | 5 | 10.1763s | 0.2082s | 1 | 8 | yes | 10.0647s | 10.3284s | `detyped_files/deltablue/advanced/proportion_sweep/main_k27_s05.py` |  |
| 0.79 | 27/34 | 6 | 10.3381s | 0.2794s | 1 | 8 | yes | 10.1766s | 10.5309s | `detyped_files/deltablue/advanced/proportion_sweep/main_k27_s06.py` |  |
| 0.79 | 27/34 | 7 | 8.8772s | 0.2085s | 1 | 8 | yes | 8.7604s | 9.0258s | `detyped_files/deltablue/advanced/proportion_sweep/main_k27_s07.py` |  |
| 0.79 | 27/34 | 8 | 2.7516s | 0.2152s | 1 | 8 | yes | 2.6446s | 2.9084s | `detyped_files/deltablue/advanced/proportion_sweep/main_k27_s08.py` |  |
| 0.79 | 27/34 | 9 | 2.5610s | 0.1009s | 1 | 8 | yes | 2.4993s | 2.6287s | `detyped_files/deltablue/advanced/proportion_sweep/main_k27_s09.py` |  |
| 0.79 | 27/34 | 10 | 2.5313s | 0.1042s | 1 | 8 | yes | 2.4691s | 2.6012s | `detyped_files/deltablue/advanced/proportion_sweep/main_k27_s10.py` |  |
| 0.79 | 27/34 | 11 | 9.6761s | 0.0781s | 1 | 8 | yes | 9.6258s | 9.7264s | `detyped_files/deltablue/advanced/proportion_sweep/main_k27_s11.py` |  |
| 0.79 | 27/34 | 12 | 1.8603s | 0.1161s | 1 | 8 | yes | 1.7884s | 1.9387s | `detyped_files/deltablue/advanced/proportion_sweep/main_k27_s12.py` |  |
| 0.79 | 27/34 | 13 | 2.6673s | 0.1201s | 1 | 8 | yes | 2.5957s | 2.7507s | `detyped_files/deltablue/advanced/proportion_sweep/main_k27_s13.py` |  |
| 0.79 | 27/34 | 14 | 10.2868s | 0.1126s | 1 | 8 | yes | 10.2174s | 10.3613s | `detyped_files/deltablue/advanced/proportion_sweep/main_k27_s14.py` |  |
| 0.79 | 27/34 | 15 | 10.1447s | 0.1997s | 1 | 8 | yes | 10.0257s | 10.2779s | `detyped_files/deltablue/advanced/proportion_sweep/main_k27_s15.py` |  |
| 0.79 | 27/34 | 16 | 10.2533s | 0.1938s | 1 | 8 | yes | 10.1339s | 10.3824s | `detyped_files/deltablue/advanced/proportion_sweep/main_k27_s16.py` |  |
| 0.79 | 27/34 | 17 | 9.0530s | 0.1419s | 1 | 8 | yes | 8.9633s | 9.1464s | `detyped_files/deltablue/advanced/proportion_sweep/main_k27_s17.py` |  |
| 0.79 | 27/34 | 18 | 9.0062s | 0.0891s | 1 | 8 | yes | 8.9491s | 9.0638s | `detyped_files/deltablue/advanced/proportion_sweep/main_k27_s18.py` |  |
| 0.79 | 27/34 | 19 | 10.1514s | 0.2047s | 1 | 8 | yes | 10.0302s | 10.2912s | `detyped_files/deltablue/advanced/proportion_sweep/main_k27_s19.py` |  |
| 0.79 | 27/34 | 20 | 9.8562s | 0.0941s | 1 | 8 | yes | 9.7963s | 9.9165s | `detyped_files/deltablue/advanced/proportion_sweep/main_k27_s20.py` |  |
| 0.82 | 28/34 | 1 | 9.7509s | 0.1154s | 1 | 8 | yes | 9.6744s | 9.8243s | `detyped_files/deltablue/advanced/proportion_sweep/main_k28_s01.py` |  |
| 0.82 | 28/34 | 2 | 7.7478s | 0.1445s | 1 | 8 | yes | 7.6538s | 7.8411s | `detyped_files/deltablue/advanced/proportion_sweep/main_k28_s02.py` |  |
| 0.82 | 28/34 | 3 | 2.5925s | 0.0935s | 1 | 8 | yes | 2.5364s | 2.6571s | `detyped_files/deltablue/advanced/proportion_sweep/main_k28_s03.py` |  |
| 0.82 | 28/34 | 4 | 9.4201s | 0.1163s | 1 | 8 | yes | 9.3463s | 9.4965s | `detyped_files/deltablue/advanced/proportion_sweep/main_k28_s04.py` |  |
| 0.82 | 28/34 | 5 | 8.9292s | 0.1783s | 1 | 8 | yes | 8.8257s | 9.0544s | `detyped_files/deltablue/advanced/proportion_sweep/main_k28_s05.py` |  |
| 0.82 | 28/34 | 6 | 10.3178s | 0.1538s | 1 | 8 | yes | 10.2248s | 10.4200s | `detyped_files/deltablue/advanced/proportion_sweep/main_k28_s06.py` |  |
| 0.82 | 28/34 | 7 | 9.4333s | 0.1199s | 1 | 8 | yes | 9.3517s | 9.5064s | `detyped_files/deltablue/advanced/proportion_sweep/main_k28_s07.py` |  |
| 0.82 | 28/34 | 8 | 10.3142s | 0.1379s | 1 | 8 | yes | 10.2355s | 10.4117s | `detyped_files/deltablue/advanced/proportion_sweep/main_k28_s08.py` |  |
| 0.82 | 28/34 | 9 | 10.2107s | 0.0846s | 1 | 8 | yes | 10.1596s | 10.2671s | `detyped_files/deltablue/advanced/proportion_sweep/main_k28_s09.py` |  |
| 0.82 | 28/34 | 10 | 8.7103s | 0.2102s | 1 | 8 | yes | 8.5771s | 8.8483s | `detyped_files/deltablue/advanced/proportion_sweep/main_k28_s10.py` |  |
| 0.82 | 28/34 | 11 | 9.6544s | 0.1306s | 1 | 8 | yes | 9.5757s | 9.7444s | `detyped_files/deltablue/advanced/proportion_sweep/main_k28_s11.py` |  |
| 0.82 | 28/34 | 12 | 10.1641s | 0.0726s | 1 | 8 | yes | 10.1211s | 10.2126s | `detyped_files/deltablue/advanced/proportion_sweep/main_k28_s12.py` |  |
| 0.82 | 28/34 | 13 | 10.2335s | 0.1556s | 1 | 8 | yes | 10.1394s | 10.3393s | `detyped_files/deltablue/advanced/proportion_sweep/main_k28_s13.py` |  |
| 0.82 | 28/34 | 14 | 9.8741s | 0.1013s | 1 | 8 | yes | 9.8095s | 9.9394s | `detyped_files/deltablue/advanced/proportion_sweep/main_k28_s14.py` |  |
| 0.82 | 28/34 | 15 | 9.7354s | 0.1533s | 1 | 8 | yes | 9.6410s | 9.8400s | `detyped_files/deltablue/advanced/proportion_sweep/main_k28_s15.py` |  |
| 0.82 | 28/34 | 16 | 10.2822s | 0.0669s | 1 | 8 | yes | 10.2343s | 10.3229s | `detyped_files/deltablue/advanced/proportion_sweep/main_k28_s16.py` |  |
| 0.82 | 28/34 | 17 | 2.3675s | 0.0567s | 1 | 8 | yes | 2.3364s | 2.4083s | `detyped_files/deltablue/advanced/proportion_sweep/main_k28_s17.py` |  |
| 0.82 | 28/34 | 18 | 9.1517s | 0.0756s | 1 | 8 | yes | 9.1011s | 9.1979s | `detyped_files/deltablue/advanced/proportion_sweep/main_k28_s18.py` |  |
| 0.82 | 28/34 | 19 | 2.1723s | 0.1015s | 1 | 8 | yes | 2.1098s | 2.2398s | `detyped_files/deltablue/advanced/proportion_sweep/main_k28_s19.py` |  |
| 0.82 | 28/34 | 20 | 8.7704s | 0.1791s | 1 | 8 | yes | 8.6726s | 8.8958s | `detyped_files/deltablue/advanced/proportion_sweep/main_k28_s20.py` |  |
| 0.85 | 29/34 | 1 | 10.1251s | 0.1337s | 1 | 8 | yes | 10.0413s | 10.2100s | `detyped_files/deltablue/advanced/proportion_sweep/main_k29_s01.py` |  |
| 0.85 | 29/34 | 2 | 8.9110s | 0.0952s | 1 | 8 | yes | 8.8491s | 8.9714s | `detyped_files/deltablue/advanced/proportion_sweep/main_k29_s02.py` |  |
| 0.85 | 29/34 | 3 | 9.0553s | 0.0589s | 1 | 8 | yes | 9.0151s | 9.0910s | `detyped_files/deltablue/advanced/proportion_sweep/main_k29_s03.py` |  |
| 0.85 | 29/34 | 4 | 9.4158s | 0.0690s | 1 | 8 | yes | 9.3729s | 9.4616s | `detyped_files/deltablue/advanced/proportion_sweep/main_k29_s04.py` |  |
| 0.85 | 29/34 | 5 | 9.7895s | 0.1482s | 1 | 8 | yes | 9.6968s | 9.8893s | `detyped_files/deltablue/advanced/proportion_sweep/main_k29_s05.py` |  |
| 0.85 | 29/34 | 6 | 10.2049s | 0.1185s | 1 | 8 | yes | 10.1300s | 10.2824s | `detyped_files/deltablue/advanced/proportion_sweep/main_k29_s06.py` |  |
| 0.85 | 29/34 | 7 | 8.4709s | 0.1541s | 1 | 8 | yes | 8.3884s | 8.5778s | `detyped_files/deltablue/advanced/proportion_sweep/main_k29_s07.py` |  |
| 0.85 | 29/34 | 8 | 9.7307s | 0.0583s | 1 | 8 | yes | 9.6939s | 9.7691s | `detyped_files/deltablue/advanced/proportion_sweep/main_k29_s08.py` |  |
| 0.85 | 29/34 | 9 | 10.2430s | 0.1047s | 1 | 8 | yes | 10.1707s | 10.3041s | `detyped_files/deltablue/advanced/proportion_sweep/main_k29_s09.py` |  |
| 0.85 | 29/34 | 10 | 8.9380s | 0.1100s | 1 | 8 | yes | 8.8671s | 9.0096s | `detyped_files/deltablue/advanced/proportion_sweep/main_k29_s10.py` |  |
| 0.85 | 29/34 | 11 | 2.7307s | 0.0985s | 1 | 8 | yes | 2.6671s | 2.7941s | `detyped_files/deltablue/advanced/proportion_sweep/main_k29_s11.py` |  |
| 0.85 | 29/34 | 12 | 10.1967s | 0.1234s | 1 | 8 | yes | 10.1247s | 10.2837s | `detyped_files/deltablue/advanced/proportion_sweep/main_k29_s12.py` |  |
| 0.85 | 29/34 | 13 | 10.2507s | 0.0786s | 1 | 8 | yes | 10.2029s | 10.3037s | `detyped_files/deltablue/advanced/proportion_sweep/main_k29_s13.py` |  |
| 0.85 | 29/34 | 14 | 2.7239s | 0.1171s | 1 | 8 | yes | 2.6533s | 2.8021s | `detyped_files/deltablue/advanced/proportion_sweep/main_k29_s14.py` |  |
| 0.85 | 29/34 | 15 | 10.2229s | 0.2248s | 1 | 8 | yes | 10.0892s | 10.3783s | `detyped_files/deltablue/advanced/proportion_sweep/main_k29_s15.py` |  |
| 0.85 | 29/34 | 16 | 10.1205s | 0.0640s | 1 | 8 | yes | 10.0784s | 10.1607s | `detyped_files/deltablue/advanced/proportion_sweep/main_k29_s16.py` |  |
| 0.85 | 29/34 | 17 | 10.2546s | 0.1057s | 1 | 8 | yes | 10.1950s | 10.3289s | `detyped_files/deltablue/advanced/proportion_sweep/main_k29_s17.py` |  |
| 0.85 | 29/34 | 18 | 10.1659s | 0.1087s | 1 | 8 | yes | 10.0963s | 10.2342s | `detyped_files/deltablue/advanced/proportion_sweep/main_k29_s18.py` |  |
| 0.85 | 29/34 | 19 | 9.7193s | 0.0869s | 1 | 8 | yes | 9.6682s | 9.7796s | `detyped_files/deltablue/advanced/proportion_sweep/main_k29_s19.py` |  |
| 0.85 | 29/34 | 20 | 2.6911s | 0.0822s | 1 | 8 | yes | 2.6385s | 2.7447s | `detyped_files/deltablue/advanced/proportion_sweep/main_k29_s20.py` |  |
| 0.88 | 30/34 | 1 | 8.9595s | 0.2214s | 1 | 8 | yes | 8.8240s | 9.1133s | `detyped_files/deltablue/advanced/proportion_sweep/main_k30_s01.py` |  |
| 0.88 | 30/34 | 2 | 9.0590s | 0.1084s | 1 | 8 | yes | 8.9938s | 9.1349s | `detyped_files/deltablue/advanced/proportion_sweep/main_k30_s02.py` |  |
| 0.88 | 30/34 | 3 | 10.2260s | 0.1073s | 1 | 8 | yes | 10.1601s | 10.2992s | `detyped_files/deltablue/advanced/proportion_sweep/main_k30_s03.py` |  |
| 0.88 | 30/34 | 4 | 8.9160s | 0.1090s | 1 | 8 | yes | 8.8483s | 8.9869s | `detyped_files/deltablue/advanced/proportion_sweep/main_k30_s04.py` |  |
| 0.88 | 30/34 | 5 | 8.9571s | 0.1319s | 1 | 8 | yes | 8.8732s | 9.0431s | `detyped_files/deltablue/advanced/proportion_sweep/main_k30_s05.py` |  |
| 0.88 | 30/34 | 6 | 8.9110s | 0.1231s | 1 | 8 | yes | 8.8292s | 8.9864s | `detyped_files/deltablue/advanced/proportion_sweep/main_k30_s06.py` |  |
| 0.88 | 30/34 | 7 | 9.8859s | 0.0540s | 1 | 8 | yes | 9.8500s | 9.9197s | `detyped_files/deltablue/advanced/proportion_sweep/main_k30_s07.py` |  |
| 0.88 | 30/34 | 8 | 10.2461s | 0.1408s | 1 | 8 | yes | 10.1490s | 10.3300s | `detyped_files/deltablue/advanced/proportion_sweep/main_k30_s08.py` |  |
| 0.88 | 30/34 | 9 | 10.1498s | 0.1029s | 1 | 8 | yes | 10.0865s | 10.2194s | `detyped_files/deltablue/advanced/proportion_sweep/main_k30_s09.py` |  |
| 0.88 | 30/34 | 10 | 10.1101s | 0.0767s | 1 | 8 | yes | 10.0566s | 10.1546s | `detyped_files/deltablue/advanced/proportion_sweep/main_k30_s10.py` |  |
| 0.88 | 30/34 | 11 | 9.8225s | 0.0953s | 1 | 8 | yes | 9.7640s | 9.8866s | `detyped_files/deltablue/advanced/proportion_sweep/main_k30_s11.py` |  |
| 0.88 | 30/34 | 12 | 10.1373s | 0.1350s | 1 | 8 | yes | 10.0562s | 10.2313s | `detyped_files/deltablue/advanced/proportion_sweep/main_k30_s12.py` |  |
| 0.88 | 30/34 | 13 | 10.2252s | 0.1071s | 1 | 8 | yes | 10.1528s | 10.2906s | `detyped_files/deltablue/advanced/proportion_sweep/main_k30_s13.py` |  |
| 0.88 | 30/34 | 14 | 10.3106s | 0.0578s | 1 | 8 | yes | 10.2726s | 10.3475s | `detyped_files/deltablue/advanced/proportion_sweep/main_k30_s14.py` |  |
| 0.88 | 30/34 | 15 | 10.2063s | 0.1389s | 1 | 8 | yes | 10.1187s | 10.2969s | `detyped_files/deltablue/advanced/proportion_sweep/main_k30_s15.py` |  |
| 0.88 | 30/34 | 16 | 10.2375s | 0.1355s | 1 | 8 | yes | 10.1503s | 10.3264s | `detyped_files/deltablue/advanced/proportion_sweep/main_k30_s16.py` |  |
| 0.88 | 30/34 | 17 | 10.2785s | 0.1757s | 1 | 8 | yes | 10.1690s | 10.3942s | `detyped_files/deltablue/advanced/proportion_sweep/main_k30_s17.py` |  |
| 0.88 | 30/34 | 18 | 10.2979s | 0.1326s | 1 | 8 | yes | 10.2214s | 10.3897s | `detyped_files/deltablue/advanced/proportion_sweep/main_k30_s18.py` |  |
| 0.88 | 30/34 | 19 | 9.8021s | 0.0858s | 1 | 8 | yes | 9.7448s | 9.8542s | `detyped_files/deltablue/advanced/proportion_sweep/main_k30_s19.py` |  |
| 0.88 | 30/34 | 20 | 10.2244s | 0.0907s | 1 | 8 | yes | 10.1627s | 10.2778s | `detyped_files/deltablue/advanced/proportion_sweep/main_k30_s20.py` |  |
| 0.91 | 31/34 | 1 | 10.2193s | 0.0942s | 1 | 8 | yes | 10.1608s | 10.2829s | `detyped_files/deltablue/advanced/proportion_sweep/main_k31_s01.py` |  |
| 0.91 | 31/34 | 2 | 2.3123s | 0.0919s | 1 | 8 | yes | 2.2610s | 2.3764s | `detyped_files/deltablue/advanced/proportion_sweep/main_k31_s02.py` |  |
| 0.91 | 31/34 | 3 | 10.1919s | 0.0946s | 1 | 8 | yes | 10.1342s | 10.2557s | `detyped_files/deltablue/advanced/proportion_sweep/main_k31_s03.py` |  |
| 0.91 | 31/34 | 4 | 10.1951s | 0.0910s | 1 | 8 | yes | 10.1386s | 10.2567s | `detyped_files/deltablue/advanced/proportion_sweep/main_k31_s04.py` |  |
| 0.91 | 31/34 | 5 | 10.2492s | 0.1687s | 1 | 8 | yes | 10.1557s | 10.3673s | `detyped_files/deltablue/advanced/proportion_sweep/main_k31_s05.py` |  |
| 0.91 | 31/34 | 6 | 2.8062s | 0.0609s | 1 | 8 | yes | 2.7619s | 2.8403s | `detyped_files/deltablue/advanced/proportion_sweep/main_k31_s06.py` |  |
| 0.91 | 31/34 | 7 | 9.7362s | 0.0893s | 1 | 8 | yes | 9.6842s | 9.7986s | `detyped_files/deltablue/advanced/proportion_sweep/main_k31_s07.py` |  |
| 0.91 | 31/34 | 8 | 7.7807s | 0.0378s | 1 | 8 | yes | 7.7541s | 7.8033s | `detyped_files/deltablue/advanced/proportion_sweep/main_k31_s08.py` |  |
| 0.91 | 31/34 | 9 | 10.3026s | 0.0750s | 1 | 8 | yes | 10.2545s | 10.3507s | `detyped_files/deltablue/advanced/proportion_sweep/main_k31_s09.py` |  |
| 0.91 | 31/34 | 10 | 10.3331s | 0.1690s | 1 | 8 | yes | 10.2317s | 10.4481s | `detyped_files/deltablue/advanced/proportion_sweep/main_k31_s10.py` |  |
| 0.91 | 31/34 | 11 | 10.2787s | 0.0996s | 1 | 8 | yes | 10.2118s | 10.3410s | `detyped_files/deltablue/advanced/proportion_sweep/main_k31_s11.py` |  |
| 0.91 | 31/34 | 12 | 10.3689s | 0.1987s | 1 | 8 | yes | 10.2418s | 10.5027s | `detyped_files/deltablue/advanced/proportion_sweep/main_k31_s12.py` |  |
| 0.91 | 31/34 | 13 | 9.3966s | 0.0874s | 1 | 8 | yes | 9.3397s | 9.4529s | `detyped_files/deltablue/advanced/proportion_sweep/main_k31_s13.py` |  |
| 0.91 | 31/34 | 14 | 10.2516s | 0.1141s | 1 | 8 | yes | 10.1823s | 10.3308s | `detyped_files/deltablue/advanced/proportion_sweep/main_k31_s14.py` |  |
| 0.91 | 31/34 | 15 | 10.2571s | 0.0440s | 1 | 8 | yes | 10.2286s | 10.2854s | `detyped_files/deltablue/advanced/proportion_sweep/main_k31_s15.py` |  |
| 0.91 | 31/34 | 16 | 9.0241s | 0.1838s | 1 | 8 | yes | 8.9273s | 9.1567s | `detyped_files/deltablue/advanced/proportion_sweep/main_k31_s16.py` |  |
| 0.91 | 31/34 | 17 | 10.2501s | 0.1672s | 1 | 8 | yes | 10.1519s | 10.3622s | `detyped_files/deltablue/advanced/proportion_sweep/main_k31_s17.py` |  |
| 0.91 | 31/34 | 18 | 10.3155s | 0.1486s | 1 | 8 | yes | 10.2257s | 10.4184s | `detyped_files/deltablue/advanced/proportion_sweep/main_k31_s18.py` |  |
| 0.91 | 31/34 | 19 | 9.1284s | 0.1098s | 1 | 8 | yes | 9.0568s | 9.2018s | `detyped_files/deltablue/advanced/proportion_sweep/main_k31_s19.py` |  |
| 0.91 | 31/34 | 20 | 10.2344s | 0.0999s | 1 | 8 | yes | 10.1625s | 10.2969s | `detyped_files/deltablue/advanced/proportion_sweep/main_k31_s20.py` |  |
| 0.94 | 32/34 | 1 | 10.1711s | 0.0873s | 1 | 8 | yes | 10.1146s | 10.2261s | `detyped_files/deltablue/advanced/proportion_sweep/main_k32_s01.py` |  |
| 0.94 | 32/34 | 2 | 10.2529s | 0.1117s | 1 | 8 | yes | 10.1817s | 10.3277s | `detyped_files/deltablue/advanced/proportion_sweep/main_k32_s02.py` |  |
| 0.94 | 32/34 | 3 | 10.1977s | 0.0559s | 1 | 8 | yes | 10.1622s | 10.2349s | `detyped_files/deltablue/advanced/proportion_sweep/main_k32_s03.py` |  |
| 0.94 | 32/34 | 4 | 10.3672s | 0.1113s | 1 | 8 | yes | 10.3082s | 10.4479s | `detyped_files/deltablue/advanced/proportion_sweep/main_k32_s04.py` |  |
| 0.94 | 32/34 | 5 | 10.2587s | 0.0980s | 1 | 8 | yes | 10.2000s | 10.3249s | `detyped_files/deltablue/advanced/proportion_sweep/main_k32_s05.py` |  |
| 0.94 | 32/34 | 6 | 10.3274s | 0.1910s | 1 | 8 | yes | 10.2113s | 10.4557s | `detyped_files/deltablue/advanced/proportion_sweep/main_k32_s06.py` |  |
| 0.94 | 32/34 | 7 | 8.9946s | 0.0728s | 1 | 8 | yes | 8.9526s | 9.0449s | `detyped_files/deltablue/advanced/proportion_sweep/main_k32_s07.py` |  |
| 0.94 | 32/34 | 8 | 10.3503s | 0.0799s | 1 | 8 | yes | 10.2988s | 10.4004s | `detyped_files/deltablue/advanced/proportion_sweep/main_k32_s08.py` |  |
| 0.94 | 32/34 | 9 | 10.2722s | 0.2628s | 1 | 8 | yes | 10.1222s | 10.4632s | `detyped_files/deltablue/advanced/proportion_sweep/main_k32_s09.py` |  |
| 0.94 | 32/34 | 10 | 10.2075s | 0.0799s | 1 | 8 | yes | 10.1553s | 10.2566s | `detyped_files/deltablue/advanced/proportion_sweep/main_k32_s10.py` |  |
| 0.94 | 32/34 | 11 | 10.3489s | 0.1347s | 1 | 8 | yes | 10.2664s | 10.4368s | `detyped_files/deltablue/advanced/proportion_sweep/main_k32_s11.py` |  |
| 0.94 | 32/34 | 12 | 10.3056s | 0.1663s | 1 | 8 | yes | 10.1986s | 10.4129s | `detyped_files/deltablue/advanced/proportion_sweep/main_k32_s12.py` |  |
| 0.94 | 32/34 | 13 | 10.2930s | 0.0785s | 1 | 8 | yes | 10.2449s | 10.3472s | `detyped_files/deltablue/advanced/proportion_sweep/main_k32_s13.py` |  |
| 0.94 | 32/34 | 14 | 9.8597s | 0.1210s | 1 | 8 | yes | 9.7845s | 9.9411s | `detyped_files/deltablue/advanced/proportion_sweep/main_k32_s14.py` |  |
| 0.94 | 32/34 | 15 | 10.2704s | 0.2196s | 1 | 8 | yes | 10.1584s | 10.4347s | `detyped_files/deltablue/advanced/proportion_sweep/main_k32_s15.py` |  |
| 0.94 | 32/34 | 16 | 10.2174s | 0.0652s | 1 | 8 | yes | 10.1742s | 10.2595s | `detyped_files/deltablue/advanced/proportion_sweep/main_k32_s16.py` |  |
| 0.94 | 32/34 | 17 | 10.2911s | 0.1834s | 1 | 8 | yes | 10.1963s | 10.4234s | `detyped_files/deltablue/advanced/proportion_sweep/main_k32_s17.py` |  |
| 0.94 | 32/34 | 18 | 2.7522s | 0.0484s | 1 | 8 | yes | 2.7204s | 2.7822s | `detyped_files/deltablue/advanced/proportion_sweep/main_k32_s18.py` |  |
| 0.94 | 32/34 | 19 | 10.2420s | 0.0612s | 1 | 8 | yes | 10.2012s | 10.2800s | `detyped_files/deltablue/advanced/proportion_sweep/main_k32_s19.py` |  |
| 0.94 | 32/34 | 20 | 10.2256s | 0.1044s | 1 | 8 | yes | 10.1614s | 10.2954s | `detyped_files/deltablue/advanced/proportion_sweep/main_k32_s20.py` |  |
| 0.97 | 33/34 | 1 | 10.1978s | 0.0978s | 1 | 8 | yes | 10.1363s | 10.2644s | `detyped_files/deltablue/advanced/proportion_sweep/main_k33_s01.py` |  |
| 0.97 | 33/34 | 2 | 10.2776s | 0.1400s | 1 | 8 | yes | 10.1989s | 10.3743s | `detyped_files/deltablue/advanced/proportion_sweep/main_k33_s02.py` |  |
| 0.97 | 33/34 | 3 | 10.2500s | 0.0907s | 1 | 8 | yes | 10.1915s | 10.3095s | `detyped_files/deltablue/advanced/proportion_sweep/main_k33_s03.py` |  |
| 0.97 | 33/34 | 4 | 10.2509s | 0.0986s | 1 | 8 | yes | 10.1934s | 10.3196s | `detyped_files/deltablue/advanced/proportion_sweep/main_k33_s04.py` |  |
| 0.97 | 33/34 | 5 | 10.2992s | 0.1345s | 1 | 8 | yes | 10.2097s | 10.3824s | `detyped_files/deltablue/advanced/proportion_sweep/main_k33_s05.py` |  |
| 0.97 | 33/34 | 6 | 10.3648s | 0.1368s | 1 | 8 | yes | 10.2857s | 10.4604s | `detyped_files/deltablue/advanced/proportion_sweep/main_k33_s06.py` |  |
| 0.97 | 33/34 | 7 | 10.2368s | 0.1533s | 1 | 8 | yes | 10.1320s | 10.3303s | `detyped_files/deltablue/advanced/proportion_sweep/main_k33_s07.py` |  |
| 0.97 | 33/34 | 8 | 10.1938s | 0.1304s | 1 | 8 | yes | 10.1099s | 10.2781s | `detyped_files/deltablue/advanced/proportion_sweep/main_k33_s08.py` |  |
| 0.97 | 33/34 | 9 | 10.2461s | 0.1409s | 1 | 8 | yes | 10.1603s | 10.3407s | `detyped_files/deltablue/advanced/proportion_sweep/main_k33_s09.py` |  |
| 0.97 | 33/34 | 10 | 10.3679s | 0.1316s | 1 | 8 | yes | 10.2778s | 10.4461s | `detyped_files/deltablue/advanced/proportion_sweep/main_k33_s10.py` |  |
| 0.97 | 33/34 | 11 | 10.2521s | 0.1081s | 1 | 8 | yes | 10.1801s | 10.3177s | `detyped_files/deltablue/advanced/proportion_sweep/main_k33_s11.py` |  |
| 0.97 | 33/34 | 12 | 9.8144s | 0.0867s | 1 | 8 | yes | 9.7578s | 9.8702s | `detyped_files/deltablue/advanced/proportion_sweep/main_k33_s12.py` |  |
| 0.97 | 33/34 | 13 | 10.2259s | 0.0846s | 1 | 8 | yes | 10.1697s | 10.2795s | `detyped_files/deltablue/advanced/proportion_sweep/main_k33_s13.py` |  |
| 0.97 | 33/34 | 14 | 10.1956s | 0.1386s | 1 | 8 | yes | 10.1123s | 10.2900s | `detyped_files/deltablue/advanced/proportion_sweep/main_k33_s14.py` |  |
| 0.97 | 33/34 | 15 | 10.2384s | 0.1195s | 1 | 8 | yes | 10.1726s | 10.3257s | `detyped_files/deltablue/advanced/proportion_sweep/main_k33_s15.py` |  |
| 0.97 | 33/34 | 16 | 10.2414s | 0.1652s | 1 | 8 | yes | 10.1454s | 10.3571s | `detyped_files/deltablue/advanced/proportion_sweep/main_k33_s16.py` |  |
| 0.97 | 33/34 | 17 | 10.2456s | 0.0677s | 1 | 8 | yes | 10.2059s | 10.2930s | `detyped_files/deltablue/advanced/proportion_sweep/main_k33_s17.py` |  |
| 0.97 | 33/34 | 18 | 10.2352s | 0.0707s | 1 | 8 | yes | 10.1965s | 10.2850s | `detyped_files/deltablue/advanced/proportion_sweep/main_k33_s18.py` |  |
| 0.97 | 33/34 | 19 | 9.8280s | 0.0654s | 1 | 8 | yes | 9.7888s | 9.8727s | `detyped_files/deltablue/advanced/proportion_sweep/main_k33_s19.py` |  |
| 0.97 | 33/34 | 20 | 10.2516s | 0.0925s | 1 | 8 | yes | 10.1943s | 10.3133s | `detyped_files/deltablue/advanced/proportion_sweep/main_k33_s20.py` |  |
| 1.00 | 34/34 | 1 | 10.3295s | 0.1360s | 1 | 8 | yes | 10.2390s | 10.4155s | `detyped_files/deltablue/advanced/proportion_sweep/main_k34_s01.py` |  |

## deltablue/shallow

- Detypable targets: `35`
- Total runs: `682`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/35 | 1 | 1.1016s | 1.1016s | 1.1016s | 1.0 | yes | ok |
| 0.03 | 1/35 | 20 | 1.1626s | 1.0338s | 1.6371s | 1.0 | yes | ok |
| 0.06 | 2/35 | 20 | 1.2110s | 1.0698s | 1.6261s | 1.0 | yes | ok |
| 0.09 | 3/35 | 20 | 1.2258s | 1.0754s | 1.4193s | 1.0 | yes | ok |
| 0.11 | 4/35 | 20 | 1.4005s | 1.0813s | 1.7812s | 1.0 | yes | ok |
| 0.14 | 5/35 | 20 | 1.3287s | 1.1022s | 1.6694s | 1.0 | yes | ok |
| 0.17 | 6/35 | 20 | 1.4297s | 1.0982s | 2.0250s | 1.0 | yes | ok |
| 0.20 | 7/35 | 20 | 1.4010s | 1.0649s | 1.7991s | 1.0 | yes | ok |
| 0.23 | 8/35 | 20 | 1.4338s | 1.1328s | 2.2600s | 1.0 | yes | ok |
| 0.26 | 9/35 | 20 | 1.5656s | 1.1143s | 2.2770s | 1.0 | yes | ok |
| 0.29 | 10/35 | 20 | 1.5813s | 1.1370s | 2.3186s | 1.0 | yes | ok |
| 0.31 | 11/35 | 20 | 1.6369s | 1.1918s | 2.2353s | 1.0 | yes | ok |
| 0.34 | 12/35 | 20 | 1.6587s | 1.1908s | 2.1457s | 1.0 | yes | ok |
| 0.37 | 13/35 | 20 | 1.6870s | 1.2111s | 2.2878s | 1.0 | yes | ok |
| 0.40 | 14/35 | 20 | 1.7144s | 1.1301s | 2.2195s | 1.0 | yes | ok |
| 0.43 | 15/35 | 20 | 1.7921s | 1.1684s | 2.4467s | 1.0 | yes | ok |
| 0.46 | 16/35 | 20 | 1.8803s | 1.2800s | 2.4574s | 1.0 | yes | ok |
| 0.49 | 17/35 | 20 | 1.9597s | 1.3140s | 2.2948s | 1.0 | yes | ok |
| 0.51 | 18/35 | 20 | 1.9190s | 1.3915s | 2.4326s | 1.0 | yes | ok |
| 0.54 | 19/35 | 20 | 1.9724s | 1.2009s | 2.5595s | 1.0 | yes | ok |
| 0.57 | 20/35 | 20 | 2.0380s | 1.4133s | 2.4864s | 1.0 | yes | ok |
| 0.60 | 21/35 | 20 | 1.9992s | 1.3242s | 2.4692s | 1.0 | yes | ok |
| 0.63 | 22/35 | 20 | 2.1515s | 1.6567s | 2.6163s | 1.0 | yes | ok |
| 0.66 | 23/35 | 20 | 2.1132s | 1.4080s | 2.5756s | 1.0 | yes | ok |
| 0.69 | 24/35 | 20 | 2.2337s | 1.4737s | 2.5999s | 1.0 | yes | ok |
| 0.71 | 25/35 | 20 | 2.2775s | 1.9215s | 2.6548s | 1.0 | yes | ok |
| 0.74 | 26/35 | 20 | 2.2177s | 1.4329s | 2.6453s | 1.0 | yes | ok |
| 0.77 | 27/35 | 20 | 2.2700s | 1.5881s | 2.6274s | 1.0 | yes | ok |
| 0.80 | 28/35 | 20 | 2.2689s | 1.6776s | 2.6209s | 1.0 | yes | ok |
| 0.83 | 29/35 | 20 | 2.4017s | 2.0736s | 2.7543s | 1.0 | yes | ok |
| 0.86 | 30/35 | 20 | 2.3963s | 1.7899s | 2.6407s | 1.0 | yes | ok |
| 0.89 | 31/35 | 20 | 2.4355s | 1.6623s | 2.7292s | 1.0 | yes | ok |
| 0.91 | 32/35 | 20 | 2.4833s | 2.2373s | 2.6822s | 1.0 | yes | ok |
| 0.94 | 33/35 | 20 | 2.5298s | 2.0913s | 2.6980s | 1.0 | yes | ok |
| 0.97 | 34/35 | 20 | 2.5986s | 2.2019s | 2.6822s | 1.0 | yes | ok |
| 1.00 | 35/35 | 1 | 2.6334s | 2.6334s | 2.6334s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/35 | 1 | 1.1016s | 0.0773s | 1 | 8 | yes | 1.0530s | 1.1549s | `detyped_files/deltablue/shallow/proportion_sweep/main_k00_s01.py` |  |
| 0.03 | 1/35 | 1 | 1.1847s | 0.0860s | 1 | 8 | yes | 1.1339s | 1.2439s | `detyped_files/deltablue/shallow/proportion_sweep/main_k01_s01.py` |  |
| 0.03 | 1/35 | 2 | 1.1399s | 0.0388s | 1 | 8 | yes | 1.1142s | 1.1644s | `detyped_files/deltablue/shallow/proportion_sweep/main_k01_s02.py` |  |
| 0.03 | 1/35 | 3 | 1.1314s | 0.0675s | 1 | 8 | yes | 1.0918s | 1.1769s | `detyped_files/deltablue/shallow/proportion_sweep/main_k01_s03.py` |  |
| 0.03 | 1/35 | 4 | 1.0816s | 0.0426s | 1 | 8 | yes | 1.0510s | 1.1054s | `detyped_files/deltablue/shallow/proportion_sweep/main_k01_s04.py` |  |
| 0.03 | 1/35 | 5 | 1.0695s | 0.0858s | 1 | 8 | yes | 1.0168s | 1.1262s | `detyped_files/deltablue/shallow/proportion_sweep/main_k01_s05.py` |  |
| 0.03 | 1/35 | 6 | 1.3050s | 0.0644s | 1 | 8 | yes | 1.2677s | 1.3502s | `detyped_files/deltablue/shallow/proportion_sweep/main_k01_s06.py` |  |
| 0.03 | 1/35 | 7 | 1.2357s | 0.0857s | 1 | 8 | yes | 1.1879s | 1.2973s | `detyped_files/deltablue/shallow/proportion_sweep/main_k01_s07.py` |  |
| 0.03 | 1/35 | 8 | 1.1261s | 0.0650s | 1 | 8 | yes | 1.0877s | 1.1703s | `detyped_files/deltablue/shallow/proportion_sweep/main_k01_s08.py` |  |
| 0.03 | 1/35 | 9 | 1.1033s | 0.0821s | 1 | 8 | yes | 1.0538s | 1.1577s | `detyped_files/deltablue/shallow/proportion_sweep/main_k01_s09.py` |  |
| 0.03 | 1/35 | 10 | 1.0734s | 0.0536s | 1 | 8 | yes | 1.0361s | 1.1048s | `detyped_files/deltablue/shallow/proportion_sweep/main_k01_s10.py` |  |
| 0.03 | 1/35 | 11 | 1.1205s | 0.0609s | 1 | 8 | yes | 1.0805s | 1.1602s | `detyped_files/deltablue/shallow/proportion_sweep/main_k01_s11.py` |  |
| 0.03 | 1/35 | 12 | 1.0338s | 0.0517s | 1 | 8 | yes | 0.9999s | 1.0669s | `detyped_files/deltablue/shallow/proportion_sweep/main_k01_s12.py` |  |
| 0.03 | 1/35 | 13 | 1.1500s | 0.1004s | 1 | 8 | yes | 1.0864s | 1.2145s | `detyped_files/deltablue/shallow/proportion_sweep/main_k01_s13.py` |  |
| 0.03 | 1/35 | 14 | 1.6371s | 0.1493s | 1 | 8 | yes | 1.5490s | 1.7409s | `detyped_files/deltablue/shallow/proportion_sweep/main_k01_s14.py` |  |
| 0.03 | 1/35 | 15 | 1.1287s | 0.0840s | 1 | 8 | yes | 1.0719s | 1.1809s | `detyped_files/deltablue/shallow/proportion_sweep/main_k01_s15.py` |  |
| 0.03 | 1/35 | 16 | 1.1650s | 0.0537s | 1 | 8 | yes | 1.1252s | 1.1946s | `detyped_files/deltablue/shallow/proportion_sweep/main_k01_s16.py` |  |
| 0.03 | 1/35 | 17 | 1.0785s | 0.0796s | 1 | 8 | yes | 1.0264s | 1.1294s | `detyped_files/deltablue/shallow/proportion_sweep/main_k01_s17.py` |  |
| 0.03 | 1/35 | 18 | 1.0918s | 0.0675s | 1 | 8 | yes | 1.0461s | 1.1343s | `detyped_files/deltablue/shallow/proportion_sweep/main_k01_s18.py` |  |
| 0.03 | 1/35 | 19 | 1.2897s | 0.0505s | 1 | 8 | yes | 1.2548s | 1.3207s | `detyped_files/deltablue/shallow/proportion_sweep/main_k01_s19.py` |  |
| 0.03 | 1/35 | 20 | 1.1065s | 0.0510s | 1 | 8 | yes | 1.0708s | 1.1361s | `detyped_files/deltablue/shallow/proportion_sweep/main_k01_s20.py` |  |
| 0.06 | 2/35 | 1 | 1.5080s | 0.0605s | 1 | 8 | yes | 1.4680s | 1.5457s | `detyped_files/deltablue/shallow/proportion_sweep/main_k02_s01.py` |  |
| 0.06 | 2/35 | 2 | 1.2874s | 0.1016s | 1 | 8 | yes | 1.2210s | 1.3535s | `detyped_files/deltablue/shallow/proportion_sweep/main_k02_s02.py` |  |
| 0.06 | 2/35 | 3 | 1.0698s | 0.1025s | 1 | 8 | yes | 1.0102s | 1.1416s | `detyped_files/deltablue/shallow/proportion_sweep/main_k02_s03.py` |  |
| 0.06 | 2/35 | 4 | 1.1201s | 0.0478s | 1 | 8 | yes | 1.0923s | 1.1530s | `detyped_files/deltablue/shallow/proportion_sweep/main_k02_s04.py` |  |
| 0.06 | 2/35 | 5 | 1.2197s | 0.0925s | 1 | 8 | yes | 1.1671s | 1.2859s | `detyped_files/deltablue/shallow/proportion_sweep/main_k02_s05.py` |  |
| 0.06 | 2/35 | 6 | 1.1231s | 0.0558s | 1 | 8 | yes | 1.0836s | 1.1571s | `detyped_files/deltablue/shallow/proportion_sweep/main_k02_s06.py` |  |
| 0.06 | 2/35 | 7 | 1.1531s | 0.0868s | 1 | 8 | yes | 1.1008s | 1.2114s | `detyped_files/deltablue/shallow/proportion_sweep/main_k02_s07.py` |  |
| 0.06 | 2/35 | 8 | 1.1303s | 0.0818s | 1 | 8 | yes | 1.0801s | 1.1860s | `detyped_files/deltablue/shallow/proportion_sweep/main_k02_s08.py` |  |
| 0.06 | 2/35 | 9 | 1.1610s | 0.1478s | 1 | 8 | yes | 1.0760s | 1.2661s | `detyped_files/deltablue/shallow/proportion_sweep/main_k02_s09.py` |  |
| 0.06 | 2/35 | 10 | 1.1132s | 0.1240s | 1 | 8 | yes | 1.0446s | 1.2012s | `detyped_files/deltablue/shallow/proportion_sweep/main_k02_s10.py` |  |
| 0.06 | 2/35 | 11 | 1.1738s | 0.0583s | 1 | 8 | yes | 1.1340s | 1.2097s | `detyped_files/deltablue/shallow/proportion_sweep/main_k02_s11.py` |  |
| 0.06 | 2/35 | 12 | 1.1257s | 0.0437s | 1 | 8 | yes | 1.0965s | 1.1551s | `detyped_files/deltablue/shallow/proportion_sweep/main_k02_s12.py` |  |
| 0.06 | 2/35 | 13 | 1.2434s | 0.0974s | 1 | 8 | yes | 1.1855s | 1.3097s | `detyped_files/deltablue/shallow/proportion_sweep/main_k02_s13.py` |  |
| 0.06 | 2/35 | 14 | 1.2425s | 0.0813s | 1 | 8 | yes | 1.1888s | 1.2941s | `detyped_files/deltablue/shallow/proportion_sweep/main_k02_s14.py` |  |
| 0.06 | 2/35 | 15 | 1.0971s | 0.0562s | 1 | 8 | yes | 1.0587s | 1.1310s | `detyped_files/deltablue/shallow/proportion_sweep/main_k02_s15.py` |  |
| 0.06 | 2/35 | 16 | 1.2076s | 0.0684s | 1 | 8 | yes | 1.1658s | 1.2547s | `detyped_files/deltablue/shallow/proportion_sweep/main_k02_s16.py` |  |
| 0.06 | 2/35 | 17 | 1.6261s | 0.0921s | 1 | 8 | yes | 1.5704s | 1.6922s | `detyped_files/deltablue/shallow/proportion_sweep/main_k02_s17.py` |  |
| 0.06 | 2/35 | 18 | 1.1373s | 0.1264s | 1 | 8 | yes | 1.0671s | 1.2289s | `detyped_files/deltablue/shallow/proportion_sweep/main_k02_s18.py` |  |
| 0.06 | 2/35 | 19 | 1.1979s | 0.1389s | 1 | 8 | yes | 1.1234s | 1.2987s | `detyped_files/deltablue/shallow/proportion_sweep/main_k02_s19.py` |  |
| 0.06 | 2/35 | 20 | 1.2822s | 0.0729s | 1 | 8 | yes | 1.2345s | 1.3288s | `detyped_files/deltablue/shallow/proportion_sweep/main_k02_s20.py` |  |
| 0.09 | 3/35 | 1 | 1.1055s | 0.1489s | 1 | 8 | yes | 1.0317s | 1.2142s | `detyped_files/deltablue/shallow/proportion_sweep/main_k03_s01.py` |  |
| 0.09 | 3/35 | 2 | 1.3315s | 0.0559s | 1 | 8 | yes | 1.2992s | 1.3700s | `detyped_files/deltablue/shallow/proportion_sweep/main_k03_s02.py` |  |
| 0.09 | 3/35 | 3 | 1.0836s | 0.0433s | 1 | 8 | yes | 1.0547s | 1.1101s | `detyped_files/deltablue/shallow/proportion_sweep/main_k03_s03.py` |  |
| 0.09 | 3/35 | 4 | 1.0754s | 0.0688s | 1 | 8 | yes | 1.0291s | 1.1147s | `detyped_files/deltablue/shallow/proportion_sweep/main_k03_s04.py` |  |
| 0.09 | 3/35 | 5 | 1.1050s | 0.0586s | 1 | 8 | yes | 1.0709s | 1.1458s | `detyped_files/deltablue/shallow/proportion_sweep/main_k03_s05.py` |  |
| 0.09 | 3/35 | 6 | 1.1417s | 0.0984s | 1 | 8 | yes | 1.0793s | 1.2053s | `detyped_files/deltablue/shallow/proportion_sweep/main_k03_s06.py` |  |
| 0.09 | 3/35 | 7 | 1.3583s | 0.1061s | 1 | 8 | yes | 1.2959s | 1.4314s | `detyped_files/deltablue/shallow/proportion_sweep/main_k03_s07.py` |  |
| 0.09 | 3/35 | 8 | 1.1626s | 0.0906s | 1 | 8 | yes | 1.1059s | 1.2225s | `detyped_files/deltablue/shallow/proportion_sweep/main_k03_s08.py` |  |
| 0.09 | 3/35 | 9 | 1.2150s | 0.1222s | 1 | 8 | yes | 1.1429s | 1.3003s | `detyped_files/deltablue/shallow/proportion_sweep/main_k03_s09.py` |  |
| 0.09 | 3/35 | 10 | 1.4193s | 0.1124s | 1 | 8 | yes | 1.3502s | 1.4966s | `detyped_files/deltablue/shallow/proportion_sweep/main_k03_s10.py` |  |
| 0.09 | 3/35 | 11 | 1.1637s | 0.0411s | 1 | 8 | yes | 1.1368s | 1.1906s | `detyped_files/deltablue/shallow/proportion_sweep/main_k03_s11.py` |  |
| 0.09 | 3/35 | 12 | 1.3008s | 0.1173s | 1 | 8 | yes | 1.2302s | 1.3820s | `detyped_files/deltablue/shallow/proportion_sweep/main_k03_s12.py` |  |
| 0.09 | 3/35 | 13 | 1.2090s | 0.1070s | 1 | 8 | yes | 1.1442s | 1.2835s | `detyped_files/deltablue/shallow/proportion_sweep/main_k03_s13.py` |  |
| 0.09 | 3/35 | 14 | 1.2665s | 0.0839s | 1 | 8 | yes | 1.2129s | 1.3220s | `detyped_files/deltablue/shallow/proportion_sweep/main_k03_s14.py` |  |
| 0.09 | 3/35 | 15 | 1.2822s | 0.0917s | 1 | 8 | yes | 1.2283s | 1.3469s | `detyped_files/deltablue/shallow/proportion_sweep/main_k03_s15.py` |  |
| 0.09 | 3/35 | 16 | 1.2179s | 0.0811s | 1 | 8 | yes | 1.1723s | 1.2748s | `detyped_files/deltablue/shallow/proportion_sweep/main_k03_s16.py` |  |
| 0.09 | 3/35 | 17 | 1.2755s | 0.0804s | 1 | 8 | yes | 1.2222s | 1.3252s | `detyped_files/deltablue/shallow/proportion_sweep/main_k03_s17.py` |  |
| 0.09 | 3/35 | 18 | 1.3176s | 0.0715s | 1 | 8 | yes | 1.2753s | 1.3661s | `detyped_files/deltablue/shallow/proportion_sweep/main_k03_s18.py` |  |
| 0.09 | 3/35 | 19 | 1.2120s | 0.0928s | 1 | 8 | yes | 1.1574s | 1.2763s | `detyped_files/deltablue/shallow/proportion_sweep/main_k03_s19.py` |  |
| 0.09 | 3/35 | 20 | 1.2720s | 0.0687s | 1 | 8 | yes | 1.2210s | 1.3064s | `detyped_files/deltablue/shallow/proportion_sweep/main_k03_s20.py` |  |
| 0.11 | 4/35 | 1 | 1.4855s | 0.0294s | 1 | 8 | yes | 1.4649s | 1.5021s | `detyped_files/deltablue/shallow/proportion_sweep/main_k04_s01.py` |  |
| 0.11 | 4/35 | 2 | 1.4045s | 0.0893s | 1 | 8 | yes | 1.3537s | 1.4682s | `detyped_files/deltablue/shallow/proportion_sweep/main_k04_s02.py` |  |
| 0.11 | 4/35 | 3 | 1.2254s | 0.0725s | 1 | 8 | yes | 1.1764s | 1.2711s | `detyped_files/deltablue/shallow/proportion_sweep/main_k04_s03.py` |  |
| 0.11 | 4/35 | 4 | 1.4620s | 0.0672s | 1 | 8 | yes | 1.4227s | 1.5070s | `detyped_files/deltablue/shallow/proportion_sweep/main_k04_s04.py` |  |
| 0.11 | 4/35 | 5 | 1.6886s | 0.0517s | 1 | 8 | yes | 1.6517s | 1.7164s | `detyped_files/deltablue/shallow/proportion_sweep/main_k04_s05.py` |  |
| 0.11 | 4/35 | 6 | 1.3480s | 0.0626s | 1 | 8 | yes | 1.3038s | 1.3845s | `detyped_files/deltablue/shallow/proportion_sweep/main_k04_s06.py` |  |
| 0.11 | 4/35 | 7 | 1.3586s | 0.0718s | 1 | 8 | yes | 1.3103s | 1.4017s | `detyped_files/deltablue/shallow/proportion_sweep/main_k04_s07.py` |  |
| 0.11 | 4/35 | 8 | 1.3819s | 0.0751s | 1 | 8 | yes | 1.3303s | 1.4276s | `detyped_files/deltablue/shallow/proportion_sweep/main_k04_s08.py` |  |
| 0.11 | 4/35 | 9 | 1.2395s | 0.0744s | 1 | 8 | yes | 1.1977s | 1.2901s | `detyped_files/deltablue/shallow/proportion_sweep/main_k04_s09.py` |  |
| 0.11 | 4/35 | 10 | 1.3159s | 0.0565s | 1 | 8 | yes | 1.2838s | 1.3572s | `detyped_files/deltablue/shallow/proportion_sweep/main_k04_s10.py` |  |
| 0.11 | 4/35 | 11 | 1.5536s | 0.0679s | 1 | 8 | yes | 1.5067s | 1.5947s | `detyped_files/deltablue/shallow/proportion_sweep/main_k04_s11.py` |  |
| 0.11 | 4/35 | 12 | 1.2597s | 0.0806s | 1 | 8 | yes | 1.2063s | 1.3118s | `detyped_files/deltablue/shallow/proportion_sweep/main_k04_s12.py` |  |
| 0.11 | 4/35 | 13 | 1.7812s | 0.0687s | 1 | 8 | yes | 1.7356s | 1.8234s | `detyped_files/deltablue/shallow/proportion_sweep/main_k04_s13.py` |  |
| 0.11 | 4/35 | 14 | 1.3498s | 0.1115s | 1 | 8 | yes | 1.2808s | 1.4237s | `detyped_files/deltablue/shallow/proportion_sweep/main_k04_s14.py` |  |
| 0.11 | 4/35 | 15 | 1.2606s | 0.0713s | 1 | 8 | yes | 1.2130s | 1.3028s | `detyped_files/deltablue/shallow/proportion_sweep/main_k04_s15.py` |  |
| 0.11 | 4/35 | 16 | 1.7526s | 0.0869s | 1 | 8 | yes | 1.6958s | 1.8071s | `detyped_files/deltablue/shallow/proportion_sweep/main_k04_s16.py` |  |
| 0.11 | 4/35 | 17 | 1.0813s | 0.0625s | 1 | 8 | yes | 1.0396s | 1.1199s | `detyped_files/deltablue/shallow/proportion_sweep/main_k04_s17.py` |  |
| 0.11 | 4/35 | 18 | 1.2344s | 0.0738s | 1 | 8 | yes | 1.1878s | 1.2830s | `detyped_files/deltablue/shallow/proportion_sweep/main_k04_s18.py` |  |
| 0.11 | 4/35 | 19 | 1.5680s | 0.1080s | 1 | 8 | yes | 1.5026s | 1.6411s | `detyped_files/deltablue/shallow/proportion_sweep/main_k04_s19.py` |  |
| 0.11 | 4/35 | 20 | 1.2583s | 0.0449s | 1 | 8 | yes | 1.2285s | 1.2868s | `detyped_files/deltablue/shallow/proportion_sweep/main_k04_s20.py` |  |
| 0.14 | 5/35 | 1 | 1.2931s | 0.1463s | 1 | 8 | yes | 1.2234s | 1.4004s | `detyped_files/deltablue/shallow/proportion_sweep/main_k05_s01.py` |  |
| 0.14 | 5/35 | 2 | 1.6694s | 0.0654s | 1 | 8 | yes | 1.6244s | 1.7107s | `detyped_files/deltablue/shallow/proportion_sweep/main_k05_s02.py` |  |
| 0.14 | 5/35 | 3 | 1.6621s | 0.0831s | 1 | 8 | yes | 1.6141s | 1.7223s | `detyped_files/deltablue/shallow/proportion_sweep/main_k05_s03.py` |  |
| 0.14 | 5/35 | 4 | 1.2835s | 0.0991s | 1 | 8 | yes | 1.2368s | 1.3565s | `detyped_files/deltablue/shallow/proportion_sweep/main_k05_s04.py` |  |
| 0.14 | 5/35 | 5 | 1.2412s | 0.0566s | 1 | 8 | yes | 1.2051s | 1.2781s | `detyped_files/deltablue/shallow/proportion_sweep/main_k05_s05.py` |  |
| 0.14 | 5/35 | 6 | 1.1022s | 0.0580s | 1 | 8 | yes | 1.0649s | 1.1393s | `detyped_files/deltablue/shallow/proportion_sweep/main_k05_s06.py` |  |
| 0.14 | 5/35 | 7 | 1.2271s | 0.0541s | 1 | 8 | yes | 1.1901s | 1.2614s | `detyped_files/deltablue/shallow/proportion_sweep/main_k05_s07.py` |  |
| 0.14 | 5/35 | 8 | 1.1161s | 0.0668s | 1 | 8 | yes | 1.0713s | 1.1579s | `detyped_files/deltablue/shallow/proportion_sweep/main_k05_s08.py` |  |
| 0.14 | 5/35 | 9 | 1.1428s | 0.0789s | 1 | 8 | yes | 1.0899s | 1.1921s | `detyped_files/deltablue/shallow/proportion_sweep/main_k05_s09.py` |  |
| 0.14 | 5/35 | 10 | 1.4091s | 0.0983s | 1 | 8 | yes | 1.3453s | 1.4716s | `detyped_files/deltablue/shallow/proportion_sweep/main_k05_s10.py` |  |
| 0.14 | 5/35 | 11 | 1.4178s | 0.0977s | 1 | 8 | yes | 1.3549s | 1.4811s | `detyped_files/deltablue/shallow/proportion_sweep/main_k05_s11.py` |  |
| 0.14 | 5/35 | 12 | 1.6087s | 0.1151s | 1 | 8 | yes | 1.5392s | 1.6866s | `detyped_files/deltablue/shallow/proportion_sweep/main_k05_s12.py` |  |
| 0.14 | 5/35 | 13 | 1.1482s | 0.0616s | 1 | 8 | yes | 1.1109s | 1.1907s | `detyped_files/deltablue/shallow/proportion_sweep/main_k05_s13.py` |  |
| 0.14 | 5/35 | 14 | 1.1364s | 0.0516s | 1 | 8 | yes | 1.0996s | 1.1638s | `detyped_files/deltablue/shallow/proportion_sweep/main_k05_s14.py` |  |
| 0.14 | 5/35 | 15 | 1.3649s | 0.0651s | 1 | 8 | yes | 1.3217s | 1.4052s | `detyped_files/deltablue/shallow/proportion_sweep/main_k05_s15.py` |  |
| 0.14 | 5/35 | 16 | 1.1591s | 0.0681s | 1 | 8 | yes | 1.1143s | 1.2008s | `detyped_files/deltablue/shallow/proportion_sweep/main_k05_s16.py` |  |
| 0.14 | 5/35 | 17 | 1.2111s | 0.0801s | 1 | 8 | yes | 1.1636s | 1.2663s | `detyped_files/deltablue/shallow/proportion_sweep/main_k05_s17.py` |  |
| 0.14 | 5/35 | 18 | 1.4047s | 0.0564s | 1 | 8 | yes | 1.3694s | 1.4430s | `detyped_files/deltablue/shallow/proportion_sweep/main_k05_s18.py` |  |
| 0.14 | 5/35 | 19 | 1.3207s | 0.0692s | 1 | 8 | yes | 1.2718s | 1.3597s | `detyped_files/deltablue/shallow/proportion_sweep/main_k05_s19.py` |  |
| 0.14 | 5/35 | 20 | 1.6549s | 0.0609s | 1 | 8 | yes | 1.6128s | 1.6912s | `detyped_files/deltablue/shallow/proportion_sweep/main_k05_s20.py` |  |
| 0.17 | 6/35 | 1 | 1.8916s | 0.0621s | 1 | 8 | yes | 1.8533s | 1.9330s | `detyped_files/deltablue/shallow/proportion_sweep/main_k06_s01.py` |  |
| 0.17 | 6/35 | 2 | 1.1327s | 0.0608s | 1 | 8 | yes | 1.0948s | 1.1728s | `detyped_files/deltablue/shallow/proportion_sweep/main_k06_s02.py` |  |
| 0.17 | 6/35 | 3 | 1.2964s | 0.0612s | 1 | 8 | yes | 1.2536s | 1.3324s | `detyped_files/deltablue/shallow/proportion_sweep/main_k06_s03.py` |  |
| 0.17 | 6/35 | 4 | 1.6776s | 0.0692s | 1 | 8 | yes | 1.6328s | 1.7215s | `detyped_files/deltablue/shallow/proportion_sweep/main_k06_s04.py` |  |
| 0.17 | 6/35 | 5 | 1.5446s | 0.0810s | 1 | 8 | yes | 1.4952s | 1.5977s | `detyped_files/deltablue/shallow/proportion_sweep/main_k06_s05.py` |  |
| 0.17 | 6/35 | 6 | 1.5393s | 0.0778s | 1 | 8 | yes | 1.4875s | 1.5877s | `detyped_files/deltablue/shallow/proportion_sweep/main_k06_s06.py` |  |
| 0.17 | 6/35 | 7 | 1.6514s | 0.0890s | 1 | 8 | yes | 1.5923s | 1.7087s | `detyped_files/deltablue/shallow/proportion_sweep/main_k06_s07.py` |  |
| 0.17 | 6/35 | 8 | 2.0250s | 0.0932s | 1 | 8 | yes | 1.9651s | 2.0860s | `detyped_files/deltablue/shallow/proportion_sweep/main_k06_s08.py` |  |
| 0.17 | 6/35 | 9 | 1.1211s | 0.0749s | 1 | 8 | yes | 1.0727s | 1.1692s | `detyped_files/deltablue/shallow/proportion_sweep/main_k06_s09.py` |  |
| 0.17 | 6/35 | 10 | 1.8124s | 0.1380s | 1 | 8 | yes | 1.7404s | 1.9138s | `detyped_files/deltablue/shallow/proportion_sweep/main_k06_s10.py` |  |
| 0.17 | 6/35 | 11 | 1.3239s | 0.0849s | 1 | 8 | yes | 1.2685s | 1.3780s | `detyped_files/deltablue/shallow/proportion_sweep/main_k06_s11.py` |  |
| 0.17 | 6/35 | 12 | 1.3201s | 0.1031s | 1 | 8 | yes | 1.2590s | 1.3924s | `detyped_files/deltablue/shallow/proportion_sweep/main_k06_s12.py` |  |
| 0.17 | 6/35 | 13 | 1.3047s | 0.1147s | 1 | 8 | yes | 1.2472s | 1.3869s | `detyped_files/deltablue/shallow/proportion_sweep/main_k06_s13.py` |  |
| 0.17 | 6/35 | 14 | 1.4853s | 0.0720s | 1 | 8 | yes | 1.4344s | 1.5289s | `detyped_files/deltablue/shallow/proportion_sweep/main_k06_s14.py` |  |
| 0.17 | 6/35 | 15 | 1.2955s | 0.1084s | 1 | 8 | yes | 1.2323s | 1.3695s | `detyped_files/deltablue/shallow/proportion_sweep/main_k06_s15.py` |  |
| 0.17 | 6/35 | 16 | 1.5935s | 0.0651s | 1 | 8 | yes | 1.5493s | 1.6324s | `detyped_files/deltablue/shallow/proportion_sweep/main_k06_s16.py` |  |
| 0.17 | 6/35 | 17 | 1.0982s | 0.0648s | 1 | 8 | yes | 1.0566s | 1.1406s | `detyped_files/deltablue/shallow/proportion_sweep/main_k06_s17.py` |  |
| 0.17 | 6/35 | 18 | 1.1129s | 0.0831s | 1 | 8 | yes | 1.0626s | 1.1720s | `detyped_files/deltablue/shallow/proportion_sweep/main_k06_s18.py` |  |
| 0.17 | 6/35 | 19 | 1.1778s | 0.0426s | 1 | 8 | yes | 1.1497s | 1.2046s | `detyped_files/deltablue/shallow/proportion_sweep/main_k06_s19.py` |  |
| 0.17 | 6/35 | 20 | 1.1891s | 0.1474s | 1 | 8 | yes | 1.0928s | 1.2835s | `detyped_files/deltablue/shallow/proportion_sweep/main_k06_s20.py` |  |
| 0.20 | 7/35 | 1 | 1.1298s | 0.0515s | 1 | 8 | yes | 1.0928s | 1.1582s | `detyped_files/deltablue/shallow/proportion_sweep/main_k07_s01.py` |  |
| 0.20 | 7/35 | 2 | 1.1601s | 0.0358s | 1 | 8 | yes | 1.1399s | 1.1857s | `detyped_files/deltablue/shallow/proportion_sweep/main_k07_s02.py` |  |
| 0.20 | 7/35 | 3 | 1.4302s | 0.0367s | 1 | 8 | yes | 1.4058s | 1.4527s | `detyped_files/deltablue/shallow/proportion_sweep/main_k07_s03.py` |  |
| 0.20 | 7/35 | 4 | 1.3797s | 0.0762s | 1 | 8 | yes | 1.3324s | 1.4304s | `detyped_files/deltablue/shallow/proportion_sweep/main_k07_s04.py` |  |
| 0.20 | 7/35 | 5 | 1.3305s | 0.1008s | 1 | 8 | yes | 1.2738s | 1.4006s | `detyped_files/deltablue/shallow/proportion_sweep/main_k07_s05.py` |  |
| 0.20 | 7/35 | 6 | 1.2633s | 0.0509s | 1 | 8 | yes | 1.2316s | 1.2980s | `detyped_files/deltablue/shallow/proportion_sweep/main_k07_s06.py` |  |
| 0.20 | 7/35 | 7 | 1.6837s | 0.0794s | 1 | 8 | yes | 1.6324s | 1.7339s | `detyped_files/deltablue/shallow/proportion_sweep/main_k07_s07.py` |  |
| 0.20 | 7/35 | 8 | 1.7478s | 0.0936s | 1 | 8 | yes | 1.6862s | 1.8071s | `detyped_files/deltablue/shallow/proportion_sweep/main_k07_s08.py` |  |
| 0.20 | 7/35 | 9 | 1.1714s | 0.0990s | 1 | 8 | yes | 1.1034s | 1.2320s | `detyped_files/deltablue/shallow/proportion_sweep/main_k07_s09.py` |  |
| 0.20 | 7/35 | 10 | 1.5725s | 0.1731s | 1 | 8 | yes | 1.4891s | 1.7009s | `detyped_files/deltablue/shallow/proportion_sweep/main_k07_s10.py` |  |
| 0.20 | 7/35 | 11 | 1.1523s | 0.0589s | 1 | 8 | yes | 1.1165s | 1.1917s | `detyped_files/deltablue/shallow/proportion_sweep/main_k07_s11.py` |  |
| 0.20 | 7/35 | 12 | 1.6599s | 0.1175s | 1 | 8 | yes | 1.5951s | 1.7429s | `detyped_files/deltablue/shallow/proportion_sweep/main_k07_s12.py` |  |
| 0.20 | 7/35 | 13 | 1.6942s | 0.0661s | 1 | 8 | yes | 1.6544s | 1.7398s | `detyped_files/deltablue/shallow/proportion_sweep/main_k07_s13.py` |  |
| 0.20 | 7/35 | 14 | 1.2889s | 0.0791s | 1 | 8 | yes | 1.2418s | 1.3417s | `detyped_files/deltablue/shallow/proportion_sweep/main_k07_s14.py` |  |
| 0.20 | 7/35 | 15 | 1.0649s | 0.0511s | 1 | 8 | yes | 1.0298s | 1.0955s | `detyped_files/deltablue/shallow/proportion_sweep/main_k07_s15.py` |  |
| 0.20 | 7/35 | 16 | 1.1950s | 0.0450s | 1 | 8 | yes | 1.1646s | 1.2227s | `detyped_files/deltablue/shallow/proportion_sweep/main_k07_s16.py` |  |
| 0.20 | 7/35 | 17 | 1.5509s | 0.0194s | 1 | 8 | yes | 1.5383s | 1.5636s | `detyped_files/deltablue/shallow/proportion_sweep/main_k07_s17.py` |  |
| 0.20 | 7/35 | 18 | 1.2958s | 0.1122s | 1 | 8 | yes | 1.2227s | 1.3687s | `detyped_files/deltablue/shallow/proportion_sweep/main_k07_s18.py` |  |
| 0.20 | 7/35 | 19 | 1.4493s | 0.0892s | 1 | 8 | yes | 1.3925s | 1.5071s | `detyped_files/deltablue/shallow/proportion_sweep/main_k07_s19.py` |  |
| 0.20 | 7/35 | 20 | 1.7991s | 0.0704s | 1 | 8 | yes | 1.7634s | 1.8507s | `detyped_files/deltablue/shallow/proportion_sweep/main_k07_s20.py` |  |
| 0.23 | 8/35 | 1 | 1.8289s | 0.0367s | 1 | 8 | yes | 1.8059s | 1.8537s | `detyped_files/deltablue/shallow/proportion_sweep/main_k08_s01.py` |  |
| 0.23 | 8/35 | 2 | 1.8368s | 0.0460s | 1 | 8 | yes | 1.8040s | 1.8626s | `detyped_files/deltablue/shallow/proportion_sweep/main_k08_s02.py` |  |
| 0.23 | 8/35 | 3 | 1.3623s | 0.1084s | 1 | 8 | yes | 1.2955s | 1.4362s | `detyped_files/deltablue/shallow/proportion_sweep/main_k08_s03.py` |  |
| 0.23 | 8/35 | 4 | 1.1843s | 0.0986s | 1 | 8 | yes | 1.1224s | 1.2483s | `detyped_files/deltablue/shallow/proportion_sweep/main_k08_s04.py` |  |
| 0.23 | 8/35 | 5 | 1.2819s | 0.0587s | 1 | 8 | yes | 1.2430s | 1.3175s | `detyped_files/deltablue/shallow/proportion_sweep/main_k08_s05.py` |  |
| 0.23 | 8/35 | 6 | 1.1328s | 0.0531s | 1 | 8 | yes | 1.0949s | 1.1642s | `detyped_files/deltablue/shallow/proportion_sweep/main_k08_s06.py` |  |
| 0.23 | 8/35 | 7 | 1.3969s | 0.0703s | 1 | 8 | yes | 1.3481s | 1.4391s | `detyped_files/deltablue/shallow/proportion_sweep/main_k08_s07.py` |  |
| 0.23 | 8/35 | 8 | 1.4452s | 0.0492s | 1 | 8 | yes | 1.4153s | 1.4793s | `detyped_files/deltablue/shallow/proportion_sweep/main_k08_s08.py` |  |
| 0.23 | 8/35 | 9 | 1.5957s | 0.0673s | 1 | 8 | yes | 1.5512s | 1.6373s | `detyped_files/deltablue/shallow/proportion_sweep/main_k08_s09.py` |  |
| 0.23 | 8/35 | 10 | 1.7174s | 0.1418s | 1 | 8 | yes | 1.6346s | 1.8150s | `detyped_files/deltablue/shallow/proportion_sweep/main_k08_s10.py` |  |
| 0.23 | 8/35 | 11 | 1.1629s | 0.0554s | 1 | 8 | yes | 1.1297s | 1.1998s | `detyped_files/deltablue/shallow/proportion_sweep/main_k08_s11.py` |  |
| 0.23 | 8/35 | 12 | 1.3005s | 0.1021s | 1 | 8 | yes | 1.2353s | 1.3670s | `detyped_files/deltablue/shallow/proportion_sweep/main_k08_s12.py` |  |
| 0.23 | 8/35 | 13 | 1.1834s | 0.0645s | 1 | 8 | yes | 1.1424s | 1.2261s | `detyped_files/deltablue/shallow/proportion_sweep/main_k08_s13.py` |  |
| 0.23 | 8/35 | 14 | 1.1370s | 0.1184s | 1 | 8 | yes | 1.0632s | 1.2153s | `detyped_files/deltablue/shallow/proportion_sweep/main_k08_s14.py` |  |
| 0.23 | 8/35 | 15 | 1.1431s | 0.0629s | 1 | 8 | yes | 1.1048s | 1.1848s | `detyped_files/deltablue/shallow/proportion_sweep/main_k08_s15.py` |  |
| 0.23 | 8/35 | 16 | 1.5778s | 0.1119s | 1 | 8 | yes | 1.5088s | 1.6521s | `detyped_files/deltablue/shallow/proportion_sweep/main_k08_s16.py` |  |
| 0.23 | 8/35 | 17 | 1.3963s | 0.0949s | 1 | 8 | yes | 1.3339s | 1.4572s | `detyped_files/deltablue/shallow/proportion_sweep/main_k08_s17.py` |  |
| 0.23 | 8/35 | 18 | 2.2600s | 0.0975s | 1 | 8 | yes | 2.1995s | 2.3272s | `detyped_files/deltablue/shallow/proportion_sweep/main_k08_s18.py` |  |
| 0.23 | 8/35 | 19 | 1.1654s | 0.0465s | 1 | 8 | yes | 1.1350s | 1.1948s | `detyped_files/deltablue/shallow/proportion_sweep/main_k08_s19.py` |  |
| 0.23 | 8/35 | 20 | 1.5681s | 0.0736s | 1 | 8 | yes | 1.5181s | 1.6122s | `detyped_files/deltablue/shallow/proportion_sweep/main_k08_s20.py` |  |
| 0.26 | 9/35 | 1 | 1.4003s | 0.0908s | 1 | 8 | yes | 1.3435s | 1.4606s | `detyped_files/deltablue/shallow/proportion_sweep/main_k09_s01.py` |  |
| 0.26 | 9/35 | 2 | 1.2449s | 0.0437s | 1 | 8 | yes | 1.2149s | 1.2696s | `detyped_files/deltablue/shallow/proportion_sweep/main_k09_s02.py` |  |
| 0.26 | 9/35 | 3 | 1.6794s | 0.0657s | 1 | 8 | yes | 1.6393s | 1.7222s | `detyped_files/deltablue/shallow/proportion_sweep/main_k09_s03.py` |  |
| 0.26 | 9/35 | 4 | 1.2735s | 0.0842s | 1 | 8 | yes | 1.2174s | 1.3263s | `detyped_files/deltablue/shallow/proportion_sweep/main_k09_s04.py` |  |
| 0.26 | 9/35 | 5 | 1.5173s | 0.0404s | 1 | 8 | yes | 1.4909s | 1.5423s | `detyped_files/deltablue/shallow/proportion_sweep/main_k09_s05.py` |  |
| 0.26 | 9/35 | 6 | 1.1357s | 0.1089s | 1 | 8 | yes | 1.0662s | 1.2078s | `detyped_files/deltablue/shallow/proportion_sweep/main_k09_s06.py` |  |
| 0.26 | 9/35 | 7 | 1.2724s | 0.0868s | 1 | 8 | yes | 1.2193s | 1.3323s | `detyped_files/deltablue/shallow/proportion_sweep/main_k09_s07.py` |  |
| 0.26 | 9/35 | 8 | 2.0434s | 0.0468s | 1 | 8 | yes | 2.0125s | 2.0735s | `detyped_files/deltablue/shallow/proportion_sweep/main_k09_s08.py` |  |
| 0.26 | 9/35 | 9 | 1.4587s | 0.0822s | 1 | 8 | yes | 1.4069s | 1.5128s | `detyped_files/deltablue/shallow/proportion_sweep/main_k09_s09.py` |  |
| 0.26 | 9/35 | 10 | 1.3512s | 0.0683s | 1 | 8 | yes | 1.3092s | 1.3934s | `detyped_files/deltablue/shallow/proportion_sweep/main_k09_s10.py` |  |
| 0.26 | 9/35 | 11 | 1.4140s | 0.0912s | 1 | 8 | yes | 1.3630s | 1.4788s | `detyped_files/deltablue/shallow/proportion_sweep/main_k09_s11.py` |  |
| 0.26 | 9/35 | 12 | 1.7574s | 0.1041s | 1 | 8 | yes | 1.6945s | 1.8289s | `detyped_files/deltablue/shallow/proportion_sweep/main_k09_s12.py` |  |
| 0.26 | 9/35 | 13 | 1.1143s | 0.0592s | 1 | 8 | yes | 1.0717s | 1.1491s | `detyped_files/deltablue/shallow/proportion_sweep/main_k09_s13.py` |  |
| 0.26 | 9/35 | 14 | 2.2770s | 0.0356s | 1 | 8 | yes | 2.2528s | 2.2986s | `detyped_files/deltablue/shallow/proportion_sweep/main_k09_s14.py` |  |
| 0.26 | 9/35 | 15 | 1.9604s | 0.0602s | 1 | 8 | yes | 1.9243s | 2.0013s | `detyped_files/deltablue/shallow/proportion_sweep/main_k09_s15.py` |  |
| 0.26 | 9/35 | 16 | 2.1065s | 0.0552s | 1 | 8 | yes | 2.0719s | 2.1422s | `detyped_files/deltablue/shallow/proportion_sweep/main_k09_s16.py` |  |
| 0.26 | 9/35 | 17 | 1.6488s | 0.1100s | 1 | 8 | yes | 1.5813s | 1.7212s | `detyped_files/deltablue/shallow/proportion_sweep/main_k09_s17.py` |  |
| 0.26 | 9/35 | 18 | 1.6707s | 0.0600s | 1 | 8 | yes | 1.6305s | 1.7077s | `detyped_files/deltablue/shallow/proportion_sweep/main_k09_s18.py` |  |
| 0.26 | 9/35 | 19 | 1.4494s | 0.1171s | 1 | 8 | yes | 1.3869s | 1.5324s | `detyped_files/deltablue/shallow/proportion_sweep/main_k09_s19.py` |  |
| 0.26 | 9/35 | 20 | 1.5371s | 0.0590s | 1 | 8 | yes | 1.4980s | 1.5765s | `detyped_files/deltablue/shallow/proportion_sweep/main_k09_s20.py` |  |
| 0.29 | 10/35 | 1 | 1.3214s | 0.0743s | 1 | 8 | yes | 1.2730s | 1.3707s | `detyped_files/deltablue/shallow/proportion_sweep/main_k10_s01.py` |  |
| 0.29 | 10/35 | 2 | 1.4593s | 0.0936s | 1 | 8 | yes | 1.4015s | 1.5230s | `detyped_files/deltablue/shallow/proportion_sweep/main_k10_s02.py` |  |
| 0.29 | 10/35 | 3 | 1.8735s | 0.1380s | 1 | 8 | yes | 1.8028s | 1.9719s | `detyped_files/deltablue/shallow/proportion_sweep/main_k10_s03.py` |  |
| 0.29 | 10/35 | 4 | 1.6993s | 0.0769s | 1 | 8 | yes | 1.6514s | 1.7512s | `detyped_files/deltablue/shallow/proportion_sweep/main_k10_s04.py` |  |
| 0.29 | 10/35 | 5 | 1.2728s | 0.0704s | 1 | 8 | yes | 1.2316s | 1.3216s | `detyped_files/deltablue/shallow/proportion_sweep/main_k10_s05.py` |  |
| 0.29 | 10/35 | 6 | 1.6388s | 0.0458s | 1 | 8 | yes | 1.6081s | 1.6671s | `detyped_files/deltablue/shallow/proportion_sweep/main_k10_s06.py` |  |
| 0.29 | 10/35 | 7 | 1.7915s | 0.0889s | 1 | 8 | yes | 1.7328s | 1.8506s | `detyped_files/deltablue/shallow/proportion_sweep/main_k10_s07.py` |  |
| 0.29 | 10/35 | 8 | 1.4913s | 0.0942s | 1 | 8 | yes | 1.4314s | 1.5543s | `detyped_files/deltablue/shallow/proportion_sweep/main_k10_s08.py` |  |
| 0.29 | 10/35 | 9 | 1.1476s | 0.1133s | 1 | 8 | yes | 1.0707s | 1.2192s | `detyped_files/deltablue/shallow/proportion_sweep/main_k10_s09.py` |  |
| 0.29 | 10/35 | 10 | 1.8511s | 0.0879s | 1 | 8 | yes | 1.7905s | 1.9046s | `detyped_files/deltablue/shallow/proportion_sweep/main_k10_s10.py` |  |
| 0.29 | 10/35 | 11 | 1.1378s | 0.0877s | 1 | 8 | yes | 1.0800s | 1.1930s | `detyped_files/deltablue/shallow/proportion_sweep/main_k10_s11.py` |  |
| 0.29 | 10/35 | 12 | 1.4023s | 0.0661s | 1 | 8 | yes | 1.3597s | 1.4427s | `detyped_files/deltablue/shallow/proportion_sweep/main_k10_s12.py` |  |
| 0.29 | 10/35 | 13 | 1.1370s | 0.0507s | 1 | 8 | yes | 1.1091s | 1.1738s | `detyped_files/deltablue/shallow/proportion_sweep/main_k10_s13.py` |  |
| 0.29 | 10/35 | 14 | 1.7770s | 0.1739s | 1 | 8 | yes | 1.6802s | 1.9090s | `detyped_files/deltablue/shallow/proportion_sweep/main_k10_s14.py` |  |
| 0.29 | 10/35 | 15 | 1.7151s | 0.1124s | 1 | 8 | yes | 1.6422s | 1.7892s | `detyped_files/deltablue/shallow/proportion_sweep/main_k10_s15.py` |  |
| 0.29 | 10/35 | 16 | 2.3186s | 0.0678s | 1 | 8 | yes | 2.2717s | 2.3586s | `detyped_files/deltablue/shallow/proportion_sweep/main_k10_s16.py` |  |
| 0.29 | 10/35 | 17 | 1.5005s | 0.0699s | 1 | 8 | yes | 1.4544s | 1.5448s | `detyped_files/deltablue/shallow/proportion_sweep/main_k10_s17.py` |  |
| 0.29 | 10/35 | 18 | 1.7339s | 0.1174s | 1 | 8 | yes | 1.6642s | 1.8178s | `detyped_files/deltablue/shallow/proportion_sweep/main_k10_s18.py` |  |
| 0.29 | 10/35 | 19 | 1.9066s | 0.1406s | 1 | 8 | yes | 1.8270s | 2.0075s | `detyped_files/deltablue/shallow/proportion_sweep/main_k10_s19.py` |  |
| 0.29 | 10/35 | 20 | 1.4515s | 0.0642s | 1 | 8 | yes | 1.4089s | 1.4904s | `detyped_files/deltablue/shallow/proportion_sweep/main_k10_s20.py` |  |
| 0.31 | 11/35 | 1 | 1.2675s | 0.0794s | 1 | 8 | yes | 1.2164s | 1.3173s | `detyped_files/deltablue/shallow/proportion_sweep/main_k11_s01.py` |  |
| 0.31 | 11/35 | 2 | 1.6805s | 0.0756s | 1 | 8 | yes | 1.6293s | 1.7281s | `detyped_files/deltablue/shallow/proportion_sweep/main_k11_s02.py` |  |
| 0.31 | 11/35 | 3 | 1.5016s | 0.0471s | 1 | 8 | yes | 1.4707s | 1.5309s | `detyped_files/deltablue/shallow/proportion_sweep/main_k11_s03.py` |  |
| 0.31 | 11/35 | 4 | 1.8641s | 0.1162s | 1 | 8 | yes | 1.7878s | 1.9356s | `detyped_files/deltablue/shallow/proportion_sweep/main_k11_s04.py` |  |
| 0.31 | 11/35 | 5 | 1.5928s | 0.0987s | 1 | 8 | yes | 1.5345s | 1.6598s | `detyped_files/deltablue/shallow/proportion_sweep/main_k11_s05.py` |  |
| 0.31 | 11/35 | 6 | 1.7186s | 0.0770s | 1 | 8 | yes | 1.6666s | 1.7667s | `detyped_files/deltablue/shallow/proportion_sweep/main_k11_s06.py` |  |
| 0.31 | 11/35 | 7 | 1.1918s | 0.1274s | 1 | 8 | yes | 1.1165s | 1.2821s | `detyped_files/deltablue/shallow/proportion_sweep/main_k11_s07.py` |  |
| 0.31 | 11/35 | 8 | 1.7955s | 0.1378s | 1 | 8 | yes | 1.7181s | 1.8937s | `detyped_files/deltablue/shallow/proportion_sweep/main_k11_s08.py` |  |
| 0.31 | 11/35 | 9 | 1.8159s | 0.1134s | 1 | 8 | yes | 1.7419s | 1.8896s | `detyped_files/deltablue/shallow/proportion_sweep/main_k11_s09.py` |  |
| 0.31 | 11/35 | 10 | 1.6839s | 0.0959s | 1 | 8 | yes | 1.6213s | 1.7458s | `detyped_files/deltablue/shallow/proportion_sweep/main_k11_s10.py` |  |
| 0.31 | 11/35 | 11 | 1.7364s | 0.0830s | 1 | 8 | yes | 1.6794s | 1.7860s | `detyped_files/deltablue/shallow/proportion_sweep/main_k11_s11.py` |  |
| 0.31 | 11/35 | 12 | 1.3123s | 0.0485s | 1 | 8 | yes | 1.2793s | 1.3424s | `detyped_files/deltablue/shallow/proportion_sweep/main_k11_s12.py` |  |
| 0.31 | 11/35 | 13 | 1.9676s | 0.0449s | 1 | 8 | yes | 1.9386s | 1.9962s | `detyped_files/deltablue/shallow/proportion_sweep/main_k11_s13.py` |  |
| 0.31 | 11/35 | 14 | 1.8066s | 0.1009s | 1 | 8 | yes | 1.7423s | 1.8732s | `detyped_files/deltablue/shallow/proportion_sweep/main_k11_s14.py` |  |
| 0.31 | 11/35 | 15 | 1.6884s | 0.0971s | 1 | 8 | yes | 1.6284s | 1.7532s | `detyped_files/deltablue/shallow/proportion_sweep/main_k11_s15.py` |  |
| 0.31 | 11/35 | 16 | 1.2785s | 0.0653s | 1 | 8 | yes | 1.2448s | 1.3265s | `detyped_files/deltablue/shallow/proportion_sweep/main_k11_s16.py` |  |
| 0.31 | 11/35 | 17 | 1.8512s | 0.0648s | 1 | 8 | yes | 1.8095s | 1.8929s | `detyped_files/deltablue/shallow/proportion_sweep/main_k11_s17.py` |  |
| 0.31 | 11/35 | 18 | 1.4843s | 0.0555s | 1 | 8 | yes | 1.4488s | 1.5202s | `detyped_files/deltablue/shallow/proportion_sweep/main_k11_s18.py` |  |
| 0.31 | 11/35 | 19 | 2.2353s | 0.1480s | 1 | 8 | yes | 2.1465s | 2.3359s | `detyped_files/deltablue/shallow/proportion_sweep/main_k11_s19.py` |  |
| 0.31 | 11/35 | 20 | 1.2643s | 0.0876s | 1 | 8 | yes | 1.2075s | 1.3212s | `detyped_files/deltablue/shallow/proportion_sweep/main_k11_s20.py` |  |
| 0.34 | 12/35 | 1 | 1.8869s | 0.0415s | 1 | 8 | yes | 1.8584s | 1.9118s | `detyped_files/deltablue/shallow/proportion_sweep/main_k12_s01.py` |  |
| 0.34 | 12/35 | 2 | 1.4370s | 0.0896s | 1 | 8 | yes | 1.3811s | 1.4970s | `detyped_files/deltablue/shallow/proportion_sweep/main_k12_s02.py` |  |
| 0.34 | 12/35 | 3 | 1.8913s | 0.1047s | 1 | 8 | yes | 1.8243s | 1.9594s | `detyped_files/deltablue/shallow/proportion_sweep/main_k12_s03.py` |  |
| 0.34 | 12/35 | 4 | 1.8231s | 0.1346s | 1 | 8 | yes | 1.7452s | 1.9161s | `detyped_files/deltablue/shallow/proportion_sweep/main_k12_s04.py` |  |
| 0.34 | 12/35 | 5 | 1.2316s | 0.1066s | 1 | 8 | yes | 1.1647s | 1.3021s | `detyped_files/deltablue/shallow/proportion_sweep/main_k12_s05.py` |  |
| 0.34 | 12/35 | 6 | 1.5483s | 0.0889s | 1 | 8 | yes | 1.4924s | 1.6046s | `detyped_files/deltablue/shallow/proportion_sweep/main_k12_s06.py` |  |
| 0.34 | 12/35 | 7 | 1.9623s | 0.0871s | 1 | 8 | yes | 1.9074s | 2.0209s | `detyped_files/deltablue/shallow/proportion_sweep/main_k12_s07.py` |  |
| 0.34 | 12/35 | 8 | 1.6888s | 0.0427s | 1 | 8 | yes | 1.6590s | 1.7142s | `detyped_files/deltablue/shallow/proportion_sweep/main_k12_s08.py` |  |
| 0.34 | 12/35 | 9 | 1.5160s | 0.0470s | 1 | 8 | yes | 1.4872s | 1.5478s | `detyped_files/deltablue/shallow/proportion_sweep/main_k12_s09.py` |  |
| 0.34 | 12/35 | 10 | 1.8342s | 0.0759s | 1 | 8 | yes | 1.7846s | 1.8814s | `detyped_files/deltablue/shallow/proportion_sweep/main_k12_s10.py` |  |
| 0.34 | 12/35 | 11 | 1.1908s | 0.0809s | 1 | 8 | yes | 1.1441s | 1.2453s | `detyped_files/deltablue/shallow/proportion_sweep/main_k12_s11.py` |  |
| 0.34 | 12/35 | 12 | 1.2303s | 0.0567s | 1 | 8 | yes | 1.1936s | 1.2654s | `detyped_files/deltablue/shallow/proportion_sweep/main_k12_s12.py` |  |
| 0.34 | 12/35 | 13 | 2.1457s | 0.0955s | 1 | 8 | yes | 2.0888s | 2.2131s | `detyped_files/deltablue/shallow/proportion_sweep/main_k12_s13.py` |  |
| 0.34 | 12/35 | 14 | 1.8767s | 0.0294s | 1 | 8 | yes | 1.8575s | 1.8951s | `detyped_files/deltablue/shallow/proportion_sweep/main_k12_s14.py` |  |
| 0.34 | 12/35 | 15 | 1.3986s | 0.1231s | 1 | 8 | yes | 1.3226s | 1.4869s | `detyped_files/deltablue/shallow/proportion_sweep/main_k12_s15.py` |  |
| 0.34 | 12/35 | 16 | 1.7775s | 0.0952s | 1 | 8 | yes | 1.7129s | 1.8344s | `detyped_files/deltablue/shallow/proportion_sweep/main_k12_s16.py` |  |
| 0.34 | 12/35 | 17 | 1.4854s | 0.0582s | 1 | 8 | yes | 1.4492s | 1.5239s | `detyped_files/deltablue/shallow/proportion_sweep/main_k12_s17.py` |  |
| 0.34 | 12/35 | 18 | 1.7225s | 0.0646s | 1 | 8 | yes | 1.6800s | 1.7618s | `detyped_files/deltablue/shallow/proportion_sweep/main_k12_s18.py` |  |
| 0.34 | 12/35 | 19 | 1.6396s | 0.1246s | 1 | 8 | yes | 1.5634s | 1.7251s | `detyped_files/deltablue/shallow/proportion_sweep/main_k12_s19.py` |  |
| 0.34 | 12/35 | 20 | 1.8872s | 0.0851s | 1 | 8 | yes | 1.8351s | 1.9464s | `detyped_files/deltablue/shallow/proportion_sweep/main_k12_s20.py` |  |
| 0.37 | 13/35 | 1 | 1.2872s | 0.0576s | 1 | 8 | yes | 1.2495s | 1.3237s | `detyped_files/deltablue/shallow/proportion_sweep/main_k13_s01.py` |  |
| 0.37 | 13/35 | 2 | 1.4742s | 0.0583s | 1 | 8 | yes | 1.4372s | 1.5121s | `detyped_files/deltablue/shallow/proportion_sweep/main_k13_s02.py` |  |
| 0.37 | 13/35 | 3 | 1.3536s | 0.0560s | 1 | 8 | yes | 1.3178s | 1.3894s | `detyped_files/deltablue/shallow/proportion_sweep/main_k13_s03.py` |  |
| 0.37 | 13/35 | 4 | 2.2878s | 0.0956s | 1 | 8 | yes | 2.2261s | 2.3483s | `detyped_files/deltablue/shallow/proportion_sweep/main_k13_s04.py` |  |
| 0.37 | 13/35 | 5 | 1.6957s | 0.0875s | 1 | 8 | yes | 1.6404s | 1.7514s | `detyped_files/deltablue/shallow/proportion_sweep/main_k13_s05.py` |  |
| 0.37 | 13/35 | 6 | 1.7557s | 0.1298s | 1 | 8 | yes | 1.6819s | 1.8499s | `detyped_files/deltablue/shallow/proportion_sweep/main_k13_s06.py` |  |
| 0.37 | 13/35 | 7 | 2.2829s | 0.0657s | 1 | 8 | yes | 2.2384s | 2.3231s | `detyped_files/deltablue/shallow/proportion_sweep/main_k13_s07.py` |  |
| 0.37 | 13/35 | 8 | 1.8415s | 0.0700s | 1 | 8 | yes | 1.7964s | 1.8867s | `detyped_files/deltablue/shallow/proportion_sweep/main_k13_s08.py` |  |
| 0.37 | 13/35 | 9 | 1.7320s | 0.0666s | 1 | 8 | yes | 1.6882s | 1.7754s | `detyped_files/deltablue/shallow/proportion_sweep/main_k13_s09.py` |  |
| 0.37 | 13/35 | 10 | 2.1785s | 0.2106s | 1 | 8 | yes | 2.0539s | 2.3201s | `detyped_files/deltablue/shallow/proportion_sweep/main_k13_s10.py` |  |
| 0.37 | 13/35 | 11 | 1.2111s | 0.0874s | 1 | 8 | yes | 1.1644s | 1.2719s | `detyped_files/deltablue/shallow/proportion_sweep/main_k13_s11.py` |  |
| 0.37 | 13/35 | 12 | 1.2930s | 0.0873s | 1 | 8 | yes | 1.2376s | 1.3506s | `detyped_files/deltablue/shallow/proportion_sweep/main_k13_s12.py` |  |
| 0.37 | 13/35 | 13 | 1.3351s | 0.0800s | 1 | 8 | yes | 1.2819s | 1.3847s | `detyped_files/deltablue/shallow/proportion_sweep/main_k13_s13.py` |  |
| 0.37 | 13/35 | 14 | 1.9296s | 0.0538s | 1 | 8 | yes | 1.8950s | 1.9643s | `detyped_files/deltablue/shallow/proportion_sweep/main_k13_s14.py` |  |
| 0.37 | 13/35 | 15 | 1.3390s | 0.0797s | 1 | 8 | yes | 1.2884s | 1.3932s | `detyped_files/deltablue/shallow/proportion_sweep/main_k13_s15.py` |  |
| 0.37 | 13/35 | 16 | 1.9826s | 0.1764s | 1 | 8 | yes | 1.8861s | 2.1074s | `detyped_files/deltablue/shallow/proportion_sweep/main_k13_s16.py` |  |
| 0.37 | 13/35 | 17 | 1.4461s | 0.1336s | 1 | 8 | yes | 1.3652s | 1.5367s | `detyped_files/deltablue/shallow/proportion_sweep/main_k13_s17.py` |  |
| 0.37 | 13/35 | 18 | 2.2318s | 0.0559s | 1 | 8 | yes | 2.1927s | 2.2648s | `detyped_files/deltablue/shallow/proportion_sweep/main_k13_s18.py` |  |
| 0.37 | 13/35 | 19 | 1.4401s | 0.0599s | 1 | 8 | yes | 1.4016s | 1.4787s | `detyped_files/deltablue/shallow/proportion_sweep/main_k13_s19.py` |  |
| 0.37 | 13/35 | 20 | 1.6428s | 0.0630s | 1 | 8 | yes | 1.6035s | 1.6845s | `detyped_files/deltablue/shallow/proportion_sweep/main_k13_s20.py` |  |
| 0.40 | 14/35 | 1 | 1.4306s | 0.0594s | 1 | 8 | yes | 1.3936s | 1.4713s | `detyped_files/deltablue/shallow/proportion_sweep/main_k14_s01.py` |  |
| 0.40 | 14/35 | 2 | 1.4788s | 0.0553s | 1 | 8 | yes | 1.4424s | 1.5137s | `detyped_files/deltablue/shallow/proportion_sweep/main_k14_s02.py` |  |
| 0.40 | 14/35 | 3 | 1.8963s | 0.0514s | 1 | 8 | yes | 1.8613s | 1.9271s | `detyped_files/deltablue/shallow/proportion_sweep/main_k14_s03.py` |  |
| 0.40 | 14/35 | 4 | 1.8114s | 0.0747s | 1 | 8 | yes | 1.7607s | 1.8560s | `detyped_files/deltablue/shallow/proportion_sweep/main_k14_s04.py` |  |
| 0.40 | 14/35 | 5 | 1.8417s | 0.0786s | 1 | 8 | yes | 1.7920s | 1.8935s | `detyped_files/deltablue/shallow/proportion_sweep/main_k14_s05.py` |  |
| 0.40 | 14/35 | 6 | 1.4441s | 0.0394s | 1 | 8 | yes | 1.4182s | 1.4686s | `detyped_files/deltablue/shallow/proportion_sweep/main_k14_s06.py` |  |
| 0.40 | 14/35 | 7 | 1.7052s | 0.0297s | 1 | 8 | yes | 1.6864s | 1.7254s | `detyped_files/deltablue/shallow/proportion_sweep/main_k14_s07.py` |  |
| 0.40 | 14/35 | 8 | 1.8682s | 0.0675s | 1 | 8 | yes | 1.8249s | 1.9108s | `detyped_files/deltablue/shallow/proportion_sweep/main_k14_s08.py` |  |
| 0.40 | 14/35 | 9 | 1.9419s | 0.0418s | 1 | 8 | yes | 1.9141s | 1.9676s | `detyped_files/deltablue/shallow/proportion_sweep/main_k14_s09.py` |  |
| 0.40 | 14/35 | 10 | 1.8465s | 0.0835s | 1 | 8 | yes | 1.7926s | 1.8995s | `detyped_files/deltablue/shallow/proportion_sweep/main_k14_s10.py` |  |
| 0.40 | 14/35 | 11 | 1.1301s | 0.0923s | 1 | 8 | yes | 1.0716s | 1.1903s | `detyped_files/deltablue/shallow/proportion_sweep/main_k14_s11.py` |  |
| 0.40 | 14/35 | 12 | 2.1303s | 0.1912s | 1 | 8 | yes | 2.0215s | 2.2667s | `detyped_files/deltablue/shallow/proportion_sweep/main_k14_s12.py` |  |
| 0.40 | 14/35 | 13 | 2.1612s | 0.0438s | 1 | 8 | yes | 2.1325s | 2.1874s | `detyped_files/deltablue/shallow/proportion_sweep/main_k14_s13.py` |  |
| 0.40 | 14/35 | 14 | 1.5084s | 0.1372s | 1 | 8 | yes | 1.4221s | 1.5992s | `detyped_files/deltablue/shallow/proportion_sweep/main_k14_s14.py` |  |
| 0.40 | 14/35 | 15 | 1.9317s | 0.1120s | 1 | 8 | yes | 1.8624s | 2.0047s | `detyped_files/deltablue/shallow/proportion_sweep/main_k14_s15.py` |  |
| 0.40 | 14/35 | 16 | 2.2195s | 0.0638s | 1 | 8 | yes | 2.1758s | 2.2599s | `detyped_files/deltablue/shallow/proportion_sweep/main_k14_s16.py` |  |
| 0.40 | 14/35 | 17 | 1.4173s | 0.0429s | 1 | 8 | yes | 1.3882s | 1.4432s | `detyped_files/deltablue/shallow/proportion_sweep/main_k14_s17.py` |  |
| 0.40 | 14/35 | 18 | 1.9040s | 0.1600s | 1 | 8 | yes | 1.8081s | 2.0111s | `detyped_files/deltablue/shallow/proportion_sweep/main_k14_s18.py` |  |
| 0.40 | 14/35 | 19 | 1.2201s | 0.0995s | 1 | 8 | yes | 1.1548s | 1.2830s | `detyped_files/deltablue/shallow/proportion_sweep/main_k14_s19.py` |  |
| 0.40 | 14/35 | 20 | 1.4001s | 0.0654s | 1 | 8 | yes | 1.3589s | 1.4430s | `detyped_files/deltablue/shallow/proportion_sweep/main_k14_s20.py` |  |
| 0.43 | 15/35 | 1 | 1.9739s | 0.1303s | 1 | 8 | yes | 1.8920s | 2.0635s | `detyped_files/deltablue/shallow/proportion_sweep/main_k15_s01.py` |  |
| 0.43 | 15/35 | 2 | 1.7232s | 0.0953s | 1 | 8 | yes | 1.6605s | 1.7846s | `detyped_files/deltablue/shallow/proportion_sweep/main_k15_s02.py` |  |
| 0.43 | 15/35 | 3 | 1.8777s | 0.0277s | 1 | 8 | yes | 1.8600s | 1.8957s | `detyped_files/deltablue/shallow/proportion_sweep/main_k15_s03.py` |  |
| 0.43 | 15/35 | 4 | 1.7326s | 0.0855s | 1 | 8 | yes | 1.6761s | 1.7866s | `detyped_files/deltablue/shallow/proportion_sweep/main_k15_s04.py` |  |
| 0.43 | 15/35 | 5 | 1.2162s | 0.0575s | 1 | 8 | yes | 1.1814s | 1.2548s | `detyped_files/deltablue/shallow/proportion_sweep/main_k15_s05.py` |  |
| 0.43 | 15/35 | 6 | 1.2631s | 0.0295s | 1 | 8 | yes | 1.2438s | 1.2817s | `detyped_files/deltablue/shallow/proportion_sweep/main_k15_s06.py` |  |
| 0.43 | 15/35 | 7 | 2.2385s | 0.0712s | 1 | 8 | yes | 2.1927s | 2.2838s | `detyped_files/deltablue/shallow/proportion_sweep/main_k15_s07.py` |  |
| 0.43 | 15/35 | 8 | 1.8083s | 0.0487s | 1 | 8 | yes | 1.7764s | 1.8387s | `detyped_files/deltablue/shallow/proportion_sweep/main_k15_s08.py` |  |
| 0.43 | 15/35 | 9 | 1.8721s | 0.0636s | 1 | 8 | yes | 1.8341s | 1.9168s | `detyped_files/deltablue/shallow/proportion_sweep/main_k15_s09.py` |  |
| 0.43 | 15/35 | 10 | 2.1261s | 0.0438s | 1 | 8 | yes | 2.0981s | 2.1546s | `detyped_files/deltablue/shallow/proportion_sweep/main_k15_s10.py` |  |
| 0.43 | 15/35 | 11 | 1.7495s | 0.0520s | 1 | 8 | yes | 1.7145s | 1.7832s | `detyped_files/deltablue/shallow/proportion_sweep/main_k15_s11.py` |  |
| 0.43 | 15/35 | 12 | 2.1949s | 0.0434s | 1 | 8 | yes | 2.1666s | 2.2231s | `detyped_files/deltablue/shallow/proportion_sweep/main_k15_s12.py` |  |
| 0.43 | 15/35 | 13 | 1.9977s | 0.0820s | 1 | 8 | yes | 1.9499s | 2.0547s | `detyped_files/deltablue/shallow/proportion_sweep/main_k15_s13.py` |  |
| 0.43 | 15/35 | 14 | 1.9726s | 0.0884s | 1 | 8 | yes | 1.9158s | 2.0331s | `detyped_files/deltablue/shallow/proportion_sweep/main_k15_s14.py` |  |
| 0.43 | 15/35 | 15 | 2.3283s | 0.0755s | 1 | 8 | yes | 2.2798s | 2.3778s | `detyped_files/deltablue/shallow/proportion_sweep/main_k15_s15.py` |  |
| 0.43 | 15/35 | 16 | 2.4467s | 0.0843s | 1 | 8 | yes | 2.3921s | 2.5013s | `detyped_files/deltablue/shallow/proportion_sweep/main_k15_s16.py` |  |
| 0.43 | 15/35 | 17 | 1.1684s | 0.0569s | 1 | 8 | yes | 1.1350s | 1.2056s | `detyped_files/deltablue/shallow/proportion_sweep/main_k15_s17.py` |  |
| 0.43 | 15/35 | 18 | 1.3755s | 0.0833s | 1 | 8 | yes | 1.3225s | 1.4315s | `detyped_files/deltablue/shallow/proportion_sweep/main_k15_s18.py` |  |
| 0.43 | 15/35 | 19 | 1.2470s | 0.0542s | 1 | 8 | yes | 1.2112s | 1.2817s | `detyped_files/deltablue/shallow/proportion_sweep/main_k15_s19.py` |  |
| 0.43 | 15/35 | 20 | 1.5291s | 0.0643s | 1 | 8 | yes | 1.4898s | 1.5733s | `detyped_files/deltablue/shallow/proportion_sweep/main_k15_s20.py` |  |
| 0.46 | 16/35 | 1 | 2.0961s | 0.1222s | 1 | 8 | yes | 2.0184s | 2.1777s | `detyped_files/deltablue/shallow/proportion_sweep/main_k16_s01.py` |  |
| 0.46 | 16/35 | 2 | 1.2800s | 0.0687s | 1 | 8 | yes | 1.2357s | 1.3246s | `detyped_files/deltablue/shallow/proportion_sweep/main_k16_s02.py` |  |
| 0.46 | 16/35 | 3 | 1.9663s | 0.0898s | 1 | 8 | yes | 1.9132s | 2.0276s | `detyped_files/deltablue/shallow/proportion_sweep/main_k16_s03.py` |  |
| 0.46 | 16/35 | 4 | 1.8323s | 0.0415s | 1 | 8 | yes | 1.8062s | 1.8590s | `detyped_files/deltablue/shallow/proportion_sweep/main_k16_s04.py` |  |
| 0.46 | 16/35 | 5 | 1.6294s | 0.0862s | 1 | 8 | yes | 1.5760s | 1.6873s | `detyped_files/deltablue/shallow/proportion_sweep/main_k16_s05.py` |  |
| 0.46 | 16/35 | 6 | 1.8852s | 0.0630s | 1 | 8 | yes | 1.8448s | 1.9259s | `detyped_files/deltablue/shallow/proportion_sweep/main_k16_s06.py` |  |
| 0.46 | 16/35 | 7 | 1.6319s | 0.0657s | 1 | 8 | yes | 1.5875s | 1.6714s | `detyped_files/deltablue/shallow/proportion_sweep/main_k16_s07.py` |  |
| 0.46 | 16/35 | 8 | 1.3817s | 0.0725s | 1 | 8 | yes | 1.3355s | 1.4288s | `detyped_files/deltablue/shallow/proportion_sweep/main_k16_s08.py` |  |
| 0.46 | 16/35 | 9 | 1.9628s | 0.1329s | 1 | 8 | yes | 1.8780s | 2.0490s | `detyped_files/deltablue/shallow/proportion_sweep/main_k16_s09.py` |  |
| 0.46 | 16/35 | 10 | 1.7246s | 0.0986s | 1 | 8 | yes | 1.6686s | 1.7939s | `detyped_files/deltablue/shallow/proportion_sweep/main_k16_s10.py` |  |
| 0.46 | 16/35 | 11 | 2.0857s | 0.0524s | 1 | 8 | yes | 2.0551s | 2.1221s | `detyped_files/deltablue/shallow/proportion_sweep/main_k16_s11.py` |  |
| 0.46 | 16/35 | 12 | 2.2125s | 0.0429s | 1 | 8 | yes | 2.1845s | 2.2405s | `detyped_files/deltablue/shallow/proportion_sweep/main_k16_s12.py` |  |
| 0.46 | 16/35 | 13 | 2.3386s | 0.0697s | 1 | 8 | yes | 2.2932s | 2.3821s | `detyped_files/deltablue/shallow/proportion_sweep/main_k16_s13.py` |  |
| 0.46 | 16/35 | 14 | 1.7420s | 0.0959s | 1 | 8 | yes | 1.6840s | 1.8062s | `detyped_files/deltablue/shallow/proportion_sweep/main_k16_s14.py` |  |
| 0.46 | 16/35 | 15 | 1.8470s | 0.0773s | 1 | 8 | yes | 1.7946s | 1.8940s | `detyped_files/deltablue/shallow/proportion_sweep/main_k16_s15.py` |  |
| 0.46 | 16/35 | 16 | 2.0985s | 0.0591s | 1 | 8 | yes | 2.0610s | 2.1372s | `detyped_files/deltablue/shallow/proportion_sweep/main_k16_s16.py` |  |
| 0.46 | 16/35 | 17 | 2.1710s | 0.0636s | 1 | 8 | yes | 2.1300s | 2.2120s | `detyped_files/deltablue/shallow/proportion_sweep/main_k16_s17.py` |  |
| 0.46 | 16/35 | 18 | 2.4574s | 0.1091s | 1 | 8 | yes | 2.3952s | 2.5328s | `detyped_files/deltablue/shallow/proportion_sweep/main_k16_s18.py` |  |
| 0.46 | 16/35 | 19 | 1.7565s | 0.0407s | 1 | 8 | yes | 1.7279s | 1.7809s | `detyped_files/deltablue/shallow/proportion_sweep/main_k16_s19.py` |  |
| 0.46 | 16/35 | 20 | 1.5058s | 0.0399s | 1 | 8 | yes | 1.4807s | 1.5315s | `detyped_files/deltablue/shallow/proportion_sweep/main_k16_s20.py` |  |
| 0.49 | 17/35 | 1 | 1.9000s | 0.0813s | 1 | 8 | yes | 1.8478s | 1.9535s | `detyped_files/deltablue/shallow/proportion_sweep/main_k17_s01.py` |  |
| 0.49 | 17/35 | 2 | 1.5887s | 0.1178s | 1 | 8 | yes | 1.5191s | 1.6702s | `detyped_files/deltablue/shallow/proportion_sweep/main_k17_s02.py` |  |
| 0.49 | 17/35 | 3 | 1.8556s | 0.1122s | 1 | 8 | yes | 1.7849s | 1.9324s | `detyped_files/deltablue/shallow/proportion_sweep/main_k17_s03.py` |  |
| 0.49 | 17/35 | 4 | 2.1582s | 0.0905s | 1 | 8 | yes | 2.0987s | 2.2154s | `detyped_files/deltablue/shallow/proportion_sweep/main_k17_s04.py` |  |
| 0.49 | 17/35 | 5 | 2.2682s | 0.1292s | 1 | 8 | yes | 2.1778s | 2.3461s | `detyped_files/deltablue/shallow/proportion_sweep/main_k17_s05.py` |  |
| 0.49 | 17/35 | 6 | 2.2839s | 0.0625s | 1 | 8 | yes | 2.2413s | 2.3225s | `detyped_files/deltablue/shallow/proportion_sweep/main_k17_s06.py` |  |
| 0.49 | 17/35 | 7 | 1.3140s | 0.0463s | 1 | 8 | yes | 1.2848s | 1.3443s | `detyped_files/deltablue/shallow/proportion_sweep/main_k17_s07.py` |  |
| 0.49 | 17/35 | 8 | 1.7029s | 0.0363s | 1 | 8 | yes | 1.6776s | 1.7240s | `detyped_files/deltablue/shallow/proportion_sweep/main_k17_s08.py` |  |
| 0.49 | 17/35 | 9 | 2.2023s | 0.1066s | 1 | 8 | yes | 2.1383s | 2.2739s | `detyped_files/deltablue/shallow/proportion_sweep/main_k17_s09.py` |  |
| 0.49 | 17/35 | 10 | 1.9329s | 0.0561s | 1 | 8 | yes | 1.8949s | 1.9665s | `detyped_files/deltablue/shallow/proportion_sweep/main_k17_s10.py` |  |
| 0.49 | 17/35 | 11 | 2.2700s | 0.0954s | 1 | 8 | yes | 2.2102s | 2.3328s | `detyped_files/deltablue/shallow/proportion_sweep/main_k17_s11.py` |  |
| 0.49 | 17/35 | 12 | 1.9778s | 0.0617s | 1 | 8 | yes | 1.9388s | 2.0184s | `detyped_files/deltablue/shallow/proportion_sweep/main_k17_s12.py` |  |
| 0.49 | 17/35 | 13 | 2.0433s | 0.0804s | 1 | 8 | yes | 1.9949s | 2.0987s | `detyped_files/deltablue/shallow/proportion_sweep/main_k17_s13.py` |  |
| 0.49 | 17/35 | 14 | 1.9021s | 0.0732s | 1 | 8 | yes | 1.8576s | 1.9521s | `detyped_files/deltablue/shallow/proportion_sweep/main_k17_s14.py` |  |
| 0.49 | 17/35 | 15 | 2.0990s | 0.0693s | 1 | 8 | yes | 2.0536s | 2.1436s | `detyped_files/deltablue/shallow/proportion_sweep/main_k17_s15.py` |  |
| 0.49 | 17/35 | 16 | 1.9259s | 0.1119s | 1 | 8 | yes | 1.8549s | 2.0002s | `detyped_files/deltablue/shallow/proportion_sweep/main_k17_s16.py` |  |
| 0.49 | 17/35 | 17 | 2.2948s | 0.0919s | 1 | 8 | yes | 2.2396s | 2.3570s | `detyped_files/deltablue/shallow/proportion_sweep/main_k17_s17.py` |  |
| 0.49 | 17/35 | 18 | 2.0330s | 0.0977s | 1 | 8 | yes | 1.9694s | 2.0936s | `detyped_files/deltablue/shallow/proportion_sweep/main_k17_s18.py` |  |
| 0.49 | 17/35 | 19 | 1.9536s | 0.0831s | 1 | 8 | yes | 1.8997s | 2.0065s | `detyped_files/deltablue/shallow/proportion_sweep/main_k17_s19.py` |  |
| 0.49 | 17/35 | 20 | 1.4873s | 0.0638s | 1 | 8 | yes | 1.4453s | 1.5269s | `detyped_files/deltablue/shallow/proportion_sweep/main_k17_s20.py` |  |
| 0.51 | 18/35 | 1 | 2.0570s | 0.0957s | 1 | 8 | yes | 1.9953s | 2.1194s | `detyped_files/deltablue/shallow/proportion_sweep/main_k18_s01.py` |  |
| 0.51 | 18/35 | 2 | 2.4058s | 0.1251s | 1 | 8 | yes | 2.3293s | 2.4918s | `detyped_files/deltablue/shallow/proportion_sweep/main_k18_s02.py` |  |
| 0.51 | 18/35 | 3 | 1.7320s | 0.0520s | 1 | 8 | yes | 1.6951s | 1.7621s | `detyped_files/deltablue/shallow/proportion_sweep/main_k18_s03.py` |  |
| 0.51 | 18/35 | 4 | 1.6851s | 0.0389s | 1 | 8 | yes | 1.6597s | 1.7093s | `detyped_files/deltablue/shallow/proportion_sweep/main_k18_s04.py` |  |
| 0.51 | 18/35 | 5 | 1.5648s | 0.1077s | 1 | 8 | yes | 1.4990s | 1.6392s | `detyped_files/deltablue/shallow/proportion_sweep/main_k18_s05.py` |  |
| 0.51 | 18/35 | 6 | 2.0736s | 0.0976s | 1 | 8 | yes | 2.0142s | 2.1398s | `detyped_files/deltablue/shallow/proportion_sweep/main_k18_s06.py` |  |
| 0.51 | 18/35 | 7 | 1.4454s | 0.0345s | 1 | 8 | yes | 1.4246s | 1.4687s | `detyped_files/deltablue/shallow/proportion_sweep/main_k18_s07.py` |  |
| 0.51 | 18/35 | 8 | 2.0581s | 0.0529s | 1 | 8 | yes | 2.0263s | 2.0944s | `detyped_files/deltablue/shallow/proportion_sweep/main_k18_s08.py` |  |
| 0.51 | 18/35 | 9 | 1.3915s | 0.0553s | 1 | 8 | yes | 1.3534s | 1.4245s | `detyped_files/deltablue/shallow/proportion_sweep/main_k18_s09.py` |  |
| 0.51 | 18/35 | 10 | 1.4483s | 0.0550s | 1 | 8 | yes | 1.4149s | 1.4854s | `detyped_files/deltablue/shallow/proportion_sweep/main_k18_s10.py` |  |
| 0.51 | 18/35 | 11 | 2.3766s | 0.0614s | 1 | 8 | yes | 2.3382s | 2.4179s | `detyped_files/deltablue/shallow/proportion_sweep/main_k18_s11.py` |  |
| 0.51 | 18/35 | 12 | 2.2048s | 0.0857s | 1 | 8 | yes | 2.1459s | 2.2579s | `detyped_files/deltablue/shallow/proportion_sweep/main_k18_s12.py` |  |
| 0.51 | 18/35 | 13 | 1.8635s | 0.0426s | 1 | 8 | yes | 1.8399s | 1.8943s | `detyped_files/deltablue/shallow/proportion_sweep/main_k18_s13.py` |  |
| 0.51 | 18/35 | 14 | 2.4326s | 0.0396s | 1 | 8 | yes | 2.4053s | 2.4562s | `detyped_files/deltablue/shallow/proportion_sweep/main_k18_s14.py` |  |
| 0.51 | 18/35 | 15 | 1.9676s | 0.0877s | 1 | 8 | yes | 1.9139s | 2.0254s | `detyped_files/deltablue/shallow/proportion_sweep/main_k18_s15.py` |  |
| 0.51 | 18/35 | 16 | 2.3470s | 0.1530s | 1 | 8 | yes | 2.2551s | 2.4530s | `detyped_files/deltablue/shallow/proportion_sweep/main_k18_s16.py` |  |
| 0.51 | 18/35 | 17 | 2.3213s | 0.0850s | 1 | 8 | yes | 2.2671s | 2.3754s | `detyped_files/deltablue/shallow/proportion_sweep/main_k18_s17.py` |  |
| 0.51 | 18/35 | 18 | 1.4713s | 0.0760s | 1 | 8 | yes | 1.4215s | 1.5202s | `detyped_files/deltablue/shallow/proportion_sweep/main_k18_s18.py` |  |
| 0.51 | 18/35 | 19 | 2.0871s | 0.1099s | 1 | 8 | yes | 2.0195s | 2.1611s | `detyped_files/deltablue/shallow/proportion_sweep/main_k18_s19.py` |  |
| 0.51 | 18/35 | 20 | 1.4461s | 0.0736s | 1 | 8 | yes | 1.3954s | 1.4886s | `detyped_files/deltablue/shallow/proportion_sweep/main_k18_s20.py` |  |
| 0.54 | 19/35 | 1 | 1.9149s | 0.0929s | 1 | 8 | yes | 1.8556s | 1.9732s | `detyped_files/deltablue/shallow/proportion_sweep/main_k19_s01.py` |  |
| 0.54 | 19/35 | 2 | 2.0079s | 0.0895s | 1 | 8 | yes | 1.9450s | 2.0622s | `detyped_files/deltablue/shallow/proportion_sweep/main_k19_s02.py` |  |
| 0.54 | 19/35 | 3 | 2.0473s | 0.0947s | 1 | 8 | yes | 1.9903s | 2.1136s | `detyped_files/deltablue/shallow/proportion_sweep/main_k19_s03.py` |  |
| 0.54 | 19/35 | 4 | 2.1501s | 0.0707s | 1 | 8 | yes | 2.1025s | 2.1929s | `detyped_files/deltablue/shallow/proportion_sweep/main_k19_s04.py` |  |
| 0.54 | 19/35 | 5 | 1.4157s | 0.1030s | 1 | 8 | yes | 1.3519s | 1.4838s | `detyped_files/deltablue/shallow/proportion_sweep/main_k19_s05.py` |  |
| 0.54 | 19/35 | 6 | 1.5096s | 0.0552s | 1 | 8 | yes | 1.4738s | 1.5450s | `detyped_files/deltablue/shallow/proportion_sweep/main_k19_s06.py` |  |
| 0.54 | 19/35 | 7 | 1.6814s | 0.0522s | 1 | 8 | yes | 1.6458s | 1.7120s | `detyped_files/deltablue/shallow/proportion_sweep/main_k19_s07.py` |  |
| 0.54 | 19/35 | 8 | 1.2009s | 0.0793s | 1 | 8 | yes | 1.1529s | 1.2558s | `detyped_files/deltablue/shallow/proportion_sweep/main_k19_s08.py` |  |
| 0.54 | 19/35 | 9 | 1.5100s | 0.0443s | 1 | 8 | yes | 1.4846s | 1.5409s | `detyped_files/deltablue/shallow/proportion_sweep/main_k19_s09.py` |  |
| 0.54 | 19/35 | 10 | 2.1638s | 0.1235s | 1 | 8 | yes | 2.0932s | 2.2560s | `detyped_files/deltablue/shallow/proportion_sweep/main_k19_s10.py` |  |
| 0.54 | 19/35 | 11 | 2.5595s | 0.1168s | 1 | 8 | yes | 2.4916s | 2.6422s | `detyped_files/deltablue/shallow/proportion_sweep/main_k19_s11.py` |  |
| 0.54 | 19/35 | 12 | 1.8525s | 0.0537s | 1 | 8 | yes | 1.8164s | 1.8834s | `detyped_files/deltablue/shallow/proportion_sweep/main_k19_s12.py` |  |
| 0.54 | 19/35 | 13 | 1.8759s | 0.0632s | 1 | 8 | yes | 1.8387s | 1.9176s | `detyped_files/deltablue/shallow/proportion_sweep/main_k19_s13.py` |  |
| 0.54 | 19/35 | 14 | 2.0257s | 0.1071s | 1 | 8 | yes | 1.9567s | 2.0950s | `detyped_files/deltablue/shallow/proportion_sweep/main_k19_s14.py` |  |
| 0.54 | 19/35 | 15 | 2.3049s | 0.1526s | 1 | 8 | yes | 2.2217s | 2.4170s | `detyped_files/deltablue/shallow/proportion_sweep/main_k19_s15.py` |  |
| 0.54 | 19/35 | 16 | 2.3474s | 0.0697s | 1 | 8 | yes | 2.3007s | 2.3911s | `detyped_files/deltablue/shallow/proportion_sweep/main_k19_s16.py` |  |
| 0.54 | 19/35 | 17 | 2.0079s | 0.2070s | 1 | 8 | yes | 1.8887s | 2.1532s | `detyped_files/deltablue/shallow/proportion_sweep/main_k19_s17.py` |  |
| 0.54 | 19/35 | 18 | 2.4857s | 0.1227s | 1 | 8 | yes | 2.4099s | 2.5692s | `detyped_files/deltablue/shallow/proportion_sweep/main_k19_s18.py` |  |
| 0.54 | 19/35 | 19 | 2.2908s | 0.0750s | 1 | 8 | yes | 2.2452s | 2.3415s | `detyped_files/deltablue/shallow/proportion_sweep/main_k19_s19.py` |  |
| 0.54 | 19/35 | 20 | 2.0959s | 0.1650s | 1 | 8 | yes | 1.9968s | 2.2106s | `detyped_files/deltablue/shallow/proportion_sweep/main_k19_s20.py` |  |
| 0.57 | 20/35 | 1 | 1.4133s | 0.0761s | 1 | 8 | yes | 1.3638s | 1.4629s | `detyped_files/deltablue/shallow/proportion_sweep/main_k20_s01.py` |  |
| 0.57 | 20/35 | 2 | 2.3660s | 0.0937s | 1 | 8 | yes | 2.3053s | 2.4272s | `detyped_files/deltablue/shallow/proportion_sweep/main_k20_s02.py` |  |
| 0.57 | 20/35 | 3 | 2.0290s | 0.0902s | 1 | 8 | yes | 1.9728s | 2.0882s | `detyped_files/deltablue/shallow/proportion_sweep/main_k20_s03.py` |  |
| 0.57 | 20/35 | 4 | 2.2003s | 0.0983s | 1 | 8 | yes | 2.1483s | 2.2729s | `detyped_files/deltablue/shallow/proportion_sweep/main_k20_s04.py` |  |
| 0.57 | 20/35 | 5 | 1.4700s | 0.0973s | 1 | 8 | yes | 1.4090s | 1.5322s | `detyped_files/deltablue/shallow/proportion_sweep/main_k20_s05.py` |  |
| 0.57 | 20/35 | 6 | 2.3916s | 0.0601s | 1 | 8 | yes | 2.3535s | 2.4319s | `detyped_files/deltablue/shallow/proportion_sweep/main_k20_s06.py` |  |
| 0.57 | 20/35 | 7 | 2.1544s | 0.0688s | 1 | 8 | yes | 2.1131s | 2.2017s | `detyped_files/deltablue/shallow/proportion_sweep/main_k20_s07.py` |  |
| 0.57 | 20/35 | 8 | 2.0753s | 0.1025s | 1 | 8 | yes | 2.0116s | 2.1439s | `detyped_files/deltablue/shallow/proportion_sweep/main_k20_s08.py` |  |
| 0.57 | 20/35 | 9 | 2.3085s | 0.0937s | 1 | 8 | yes | 2.2493s | 2.3696s | `detyped_files/deltablue/shallow/proportion_sweep/main_k20_s09.py` |  |
| 0.57 | 20/35 | 10 | 1.8588s | 0.0860s | 1 | 8 | yes | 1.8040s | 1.9165s | `detyped_files/deltablue/shallow/proportion_sweep/main_k20_s10.py` |  |
| 0.57 | 20/35 | 11 | 1.7804s | 0.0558s | 1 | 8 | yes | 1.7419s | 1.8138s | `detyped_files/deltablue/shallow/proportion_sweep/main_k20_s11.py` |  |
| 0.57 | 20/35 | 12 | 1.8458s | 0.0707s | 1 | 8 | yes | 1.8016s | 1.8920s | `detyped_files/deltablue/shallow/proportion_sweep/main_k20_s12.py` |  |
| 0.57 | 20/35 | 13 | 1.8954s | 0.1038s | 1 | 8 | yes | 1.8300s | 1.9601s | `detyped_files/deltablue/shallow/proportion_sweep/main_k20_s13.py` |  |
| 0.57 | 20/35 | 14 | 1.5825s | 0.0635s | 1 | 8 | yes | 1.5394s | 1.6211s | `detyped_files/deltablue/shallow/proportion_sweep/main_k20_s14.py` |  |
| 0.57 | 20/35 | 15 | 2.4341s | 0.1523s | 1 | 8 | yes | 2.3562s | 2.5454s | `detyped_files/deltablue/shallow/proportion_sweep/main_k20_s15.py` |  |
| 0.57 | 20/35 | 16 | 2.2247s | 0.0632s | 1 | 8 | yes | 2.1815s | 2.2633s | `detyped_files/deltablue/shallow/proportion_sweep/main_k20_s16.py` |  |
| 0.57 | 20/35 | 17 | 2.0917s | 0.0230s | 1 | 8 | yes | 2.0775s | 2.1072s | `detyped_files/deltablue/shallow/proportion_sweep/main_k20_s17.py` |  |
| 0.57 | 20/35 | 18 | 1.9290s | 0.0909s | 1 | 8 | yes | 1.8682s | 1.9849s | `detyped_files/deltablue/shallow/proportion_sweep/main_k20_s18.py` |  |
| 0.57 | 20/35 | 19 | 2.4864s | 0.1175s | 1 | 8 | yes | 2.4083s | 2.5633s | `detyped_files/deltablue/shallow/proportion_sweep/main_k20_s19.py` |  |
| 0.57 | 20/35 | 20 | 2.2235s | 0.0889s | 1 | 8 | yes | 2.1659s | 2.2818s | `detyped_files/deltablue/shallow/proportion_sweep/main_k20_s20.py` |  |
| 0.60 | 21/35 | 1 | 1.9714s | 0.1204s | 1 | 8 | yes | 1.8917s | 2.0452s | `detyped_files/deltablue/shallow/proportion_sweep/main_k21_s01.py` |  |
| 0.60 | 21/35 | 2 | 1.8147s | 0.0757s | 1 | 8 | yes | 1.7648s | 1.8625s | `detyped_files/deltablue/shallow/proportion_sweep/main_k21_s02.py` |  |
| 0.60 | 21/35 | 3 | 1.6572s | 0.0550s | 1 | 8 | yes | 1.6207s | 1.6913s | `detyped_files/deltablue/shallow/proportion_sweep/main_k21_s03.py` |  |
| 0.60 | 21/35 | 4 | 2.1647s | 0.0904s | 1 | 8 | yes | 2.1132s | 2.2275s | `detyped_files/deltablue/shallow/proportion_sweep/main_k21_s04.py` |  |
| 0.60 | 21/35 | 5 | 2.3554s | 0.1430s | 1 | 8 | yes | 2.2748s | 2.4589s | `detyped_files/deltablue/shallow/proportion_sweep/main_k21_s05.py` |  |
| 0.60 | 21/35 | 6 | 1.3242s | 0.0567s | 1 | 8 | yes | 1.2844s | 1.3568s | `detyped_files/deltablue/shallow/proportion_sweep/main_k21_s06.py` |  |
| 0.60 | 21/35 | 7 | 2.2085s | 0.0911s | 1 | 8 | yes | 2.1431s | 2.2616s | `detyped_files/deltablue/shallow/proportion_sweep/main_k21_s07.py` |  |
| 0.60 | 21/35 | 8 | 2.0558s | 0.1132s | 1 | 8 | yes | 1.9838s | 2.1304s | `detyped_files/deltablue/shallow/proportion_sweep/main_k21_s08.py` |  |
| 0.60 | 21/35 | 9 | 1.4534s | 0.0889s | 1 | 8 | yes | 1.3960s | 1.5095s | `detyped_files/deltablue/shallow/proportion_sweep/main_k21_s09.py` |  |
| 0.60 | 21/35 | 10 | 2.1434s | 0.0963s | 1 | 8 | yes | 2.0876s | 2.2119s | `detyped_files/deltablue/shallow/proportion_sweep/main_k21_s10.py` |  |
| 0.60 | 21/35 | 11 | 1.9639s | 0.0772s | 1 | 8 | yes | 1.9146s | 2.0138s | `detyped_files/deltablue/shallow/proportion_sweep/main_k21_s11.py` |  |
| 0.60 | 21/35 | 12 | 1.8929s | 0.0716s | 1 | 8 | yes | 1.8448s | 1.9385s | `detyped_files/deltablue/shallow/proportion_sweep/main_k21_s12.py` |  |
| 0.60 | 21/35 | 13 | 2.4692s | 0.1104s | 1 | 8 | yes | 2.4015s | 2.5452s | `detyped_files/deltablue/shallow/proportion_sweep/main_k21_s13.py` |  |
| 0.60 | 21/35 | 14 | 2.4397s | 0.0717s | 1 | 8 | yes | 2.3931s | 2.4857s | `detyped_files/deltablue/shallow/proportion_sweep/main_k21_s14.py` |  |
| 0.60 | 21/35 | 15 | 2.2319s | 0.0757s | 1 | 8 | yes | 2.1807s | 2.2772s | `detyped_files/deltablue/shallow/proportion_sweep/main_k21_s15.py` |  |
| 0.60 | 21/35 | 16 | 2.2541s | 0.0426s | 1 | 8 | yes | 2.2264s | 2.2813s | `detyped_files/deltablue/shallow/proportion_sweep/main_k21_s16.py` |  |
| 0.60 | 21/35 | 17 | 1.7427s | 0.1174s | 1 | 8 | yes | 1.6689s | 1.8180s | `detyped_files/deltablue/shallow/proportion_sweep/main_k21_s17.py` |  |
| 0.60 | 21/35 | 18 | 1.9135s | 0.0691s | 1 | 8 | yes | 1.8646s | 1.9546s | `detyped_files/deltablue/shallow/proportion_sweep/main_k21_s18.py` |  |
| 0.60 | 21/35 | 19 | 1.8438s | 0.0662s | 1 | 8 | yes | 1.8015s | 1.8877s | `detyped_files/deltablue/shallow/proportion_sweep/main_k21_s19.py` |  |
| 0.60 | 21/35 | 20 | 2.0836s | 0.0514s | 1 | 8 | yes | 2.0583s | 2.1212s | `detyped_files/deltablue/shallow/proportion_sweep/main_k21_s20.py` |  |
| 0.63 | 22/35 | 1 | 1.9252s | 0.0516s | 1 | 8 | yes | 1.8906s | 1.9569s | `detyped_files/deltablue/shallow/proportion_sweep/main_k22_s01.py` |  |
| 0.63 | 22/35 | 2 | 1.7837s | 0.0935s | 1 | 8 | yes | 1.7229s | 1.8452s | `detyped_files/deltablue/shallow/proportion_sweep/main_k22_s02.py` |  |
| 0.63 | 22/35 | 3 | 2.2575s | 0.1167s | 1 | 8 | yes | 2.1931s | 2.3419s | `detyped_files/deltablue/shallow/proportion_sweep/main_k22_s03.py` |  |
| 0.63 | 22/35 | 4 | 2.3161s | 0.0956s | 1 | 8 | yes | 2.2591s | 2.3815s | `detyped_files/deltablue/shallow/proportion_sweep/main_k22_s04.py` |  |
| 0.63 | 22/35 | 5 | 2.1820s | 0.0757s | 1 | 8 | yes | 2.1327s | 2.2319s | `detyped_files/deltablue/shallow/proportion_sweep/main_k22_s05.py` |  |
| 0.63 | 22/35 | 6 | 2.4249s | 0.0816s | 1 | 8 | yes | 2.3696s | 2.4754s | `detyped_files/deltablue/shallow/proportion_sweep/main_k22_s06.py` |  |
| 0.63 | 22/35 | 7 | 2.1006s | 0.0939s | 1 | 8 | yes | 2.0376s | 2.1583s | `detyped_files/deltablue/shallow/proportion_sweep/main_k22_s07.py` |  |
| 0.63 | 22/35 | 8 | 1.6567s | 0.0901s | 1 | 8 | yes | 1.5960s | 1.7137s | `detyped_files/deltablue/shallow/proportion_sweep/main_k22_s08.py` |  |
| 0.63 | 22/35 | 9 | 2.1032s | 0.0665s | 1 | 8 | yes | 2.0559s | 2.1413s | `detyped_files/deltablue/shallow/proportion_sweep/main_k22_s09.py` |  |
| 0.63 | 22/35 | 10 | 2.1338s | 0.0924s | 1 | 8 | yes | 2.0762s | 2.1957s | `detyped_files/deltablue/shallow/proportion_sweep/main_k22_s10.py` |  |
| 0.63 | 22/35 | 11 | 2.1040s | 0.0778s | 1 | 8 | yes | 2.0531s | 2.1523s | `detyped_files/deltablue/shallow/proportion_sweep/main_k22_s11.py` |  |
| 0.63 | 22/35 | 12 | 2.0204s | 0.0701s | 1 | 8 | yes | 1.9718s | 2.0634s | `detyped_files/deltablue/shallow/proportion_sweep/main_k22_s12.py` |  |
| 0.63 | 22/35 | 13 | 2.1182s | 0.0879s | 1 | 8 | yes | 2.0680s | 2.1814s | `detyped_files/deltablue/shallow/proportion_sweep/main_k22_s13.py` |  |
| 0.63 | 22/35 | 14 | 2.1469s | 0.1000s | 1 | 8 | yes | 2.0843s | 2.2121s | `detyped_files/deltablue/shallow/proportion_sweep/main_k22_s14.py` |  |
| 0.63 | 22/35 | 15 | 2.2823s | 0.0854s | 1 | 8 | yes | 2.2298s | 2.3402s | `detyped_files/deltablue/shallow/proportion_sweep/main_k22_s15.py` |  |
| 0.63 | 22/35 | 16 | 1.9602s | 0.0866s | 1 | 8 | yes | 1.9112s | 2.0242s | `detyped_files/deltablue/shallow/proportion_sweep/main_k22_s16.py` |  |
| 0.63 | 22/35 | 17 | 2.6163s | 0.1163s | 1 | 8 | yes | 2.5429s | 2.6935s | `detyped_files/deltablue/shallow/proportion_sweep/main_k22_s17.py` |  |
| 0.63 | 22/35 | 18 | 2.4908s | 0.1004s | 1 | 8 | yes | 2.4347s | 2.5623s | `detyped_files/deltablue/shallow/proportion_sweep/main_k22_s18.py` |  |
| 0.63 | 22/35 | 19 | 2.3036s | 0.0948s | 1 | 8 | yes | 2.2449s | 2.3671s | `detyped_files/deltablue/shallow/proportion_sweep/main_k22_s19.py` |  |
| 0.63 | 22/35 | 20 | 2.1032s | 0.0337s | 1 | 8 | yes | 2.0819s | 2.1257s | `detyped_files/deltablue/shallow/proportion_sweep/main_k22_s20.py` |  |
| 0.66 | 23/35 | 1 | 2.3491s | 0.0757s | 1 | 8 | yes | 2.3021s | 2.3981s | `detyped_files/deltablue/shallow/proportion_sweep/main_k23_s01.py` |  |
| 0.66 | 23/35 | 2 | 2.0109s | 0.1430s | 1 | 8 | yes | 1.9248s | 2.1112s | `detyped_files/deltablue/shallow/proportion_sweep/main_k23_s02.py` |  |
| 0.66 | 23/35 | 3 | 2.0501s | 0.1003s | 1 | 8 | yes | 1.9851s | 2.1141s | `detyped_files/deltablue/shallow/proportion_sweep/main_k23_s03.py` |  |
| 0.66 | 23/35 | 4 | 2.5756s | 0.1219s | 1 | 8 | yes | 2.4968s | 2.6554s | `detyped_files/deltablue/shallow/proportion_sweep/main_k23_s04.py` |  |
| 0.66 | 23/35 | 5 | 1.7363s | 0.0620s | 1 | 8 | yes | 1.7042s | 1.7816s | `detyped_files/deltablue/shallow/proportion_sweep/main_k23_s05.py` |  |
| 0.66 | 23/35 | 6 | 2.4754s | 0.0406s | 1 | 8 | yes | 2.4468s | 2.4990s | `detyped_files/deltablue/shallow/proportion_sweep/main_k23_s06.py` |  |
| 0.66 | 23/35 | 7 | 2.0922s | 0.0965s | 1 | 8 | yes | 2.0304s | 2.1542s | `detyped_files/deltablue/shallow/proportion_sweep/main_k23_s07.py` |  |
| 0.66 | 23/35 | 8 | 2.0736s | 0.1173s | 1 | 8 | yes | 2.0078s | 2.1587s | `detyped_files/deltablue/shallow/proportion_sweep/main_k23_s08.py` |  |
| 0.66 | 23/35 | 9 | 2.3241s | 0.0844s | 1 | 8 | yes | 2.2714s | 2.3797s | `detyped_files/deltablue/shallow/proportion_sweep/main_k23_s09.py` |  |
| 0.66 | 23/35 | 10 | 1.4080s | 0.0570s | 1 | 8 | yes | 1.3711s | 1.4449s | `detyped_files/deltablue/shallow/proportion_sweep/main_k23_s10.py` |  |
| 0.66 | 23/35 | 11 | 2.1462s | 0.0550s | 1 | 8 | yes | 2.1094s | 2.1790s | `detyped_files/deltablue/shallow/proportion_sweep/main_k23_s11.py` |  |
| 0.66 | 23/35 | 12 | 1.9915s | 0.1046s | 1 | 8 | yes | 1.9330s | 2.0644s | `detyped_files/deltablue/shallow/proportion_sweep/main_k23_s12.py` |  |
| 0.66 | 23/35 | 13 | 2.0271s | 0.0290s | 1 | 8 | yes | 2.0065s | 2.0435s | `detyped_files/deltablue/shallow/proportion_sweep/main_k23_s13.py` |  |
| 0.66 | 23/35 | 14 | 2.1005s | 0.0797s | 1 | 8 | yes | 2.0505s | 2.1531s | `detyped_files/deltablue/shallow/proportion_sweep/main_k23_s14.py` |  |
| 0.66 | 23/35 | 15 | 2.0761s | 0.1514s | 1 | 8 | yes | 1.9882s | 2.1819s | `detyped_files/deltablue/shallow/proportion_sweep/main_k23_s15.py` |  |
| 0.66 | 23/35 | 16 | 2.1560s | 0.0830s | 1 | 8 | yes | 2.1047s | 2.2128s | `detyped_files/deltablue/shallow/proportion_sweep/main_k23_s16.py` |  |
| 0.66 | 23/35 | 17 | 2.1940s | 0.0669s | 1 | 8 | yes | 2.1498s | 2.2365s | `detyped_files/deltablue/shallow/proportion_sweep/main_k23_s17.py` |  |
| 0.66 | 23/35 | 18 | 2.2289s | 0.0587s | 1 | 8 | yes | 2.1903s | 2.2668s | `detyped_files/deltablue/shallow/proportion_sweep/main_k23_s18.py` |  |
| 0.66 | 23/35 | 19 | 2.4451s | 0.0897s | 1 | 8 | yes | 2.3851s | 2.5002s | `detyped_files/deltablue/shallow/proportion_sweep/main_k23_s19.py` |  |
| 0.66 | 23/35 | 20 | 1.8038s | 0.0774s | 1 | 8 | yes | 1.7522s | 1.8525s | `detyped_files/deltablue/shallow/proportion_sweep/main_k23_s20.py` |  |
| 0.69 | 24/35 | 1 | 1.9385s | 0.0688s | 1 | 8 | yes | 1.8954s | 1.9839s | `detyped_files/deltablue/shallow/proportion_sweep/main_k24_s01.py` |  |
| 0.69 | 24/35 | 2 | 2.2862s | 0.1219s | 1 | 8 | yes | 2.2122s | 2.3674s | `detyped_files/deltablue/shallow/proportion_sweep/main_k24_s02.py` |  |
| 0.69 | 24/35 | 3 | 2.5952s | 0.0901s | 1 | 8 | yes | 2.5401s | 2.6579s | `detyped_files/deltablue/shallow/proportion_sweep/main_k24_s03.py` |  |
| 0.69 | 24/35 | 4 | 2.5352s | 0.0216s | 1 | 8 | yes | 2.5212s | 2.5491s | `detyped_files/deltablue/shallow/proportion_sweep/main_k24_s04.py` |  |
| 0.69 | 24/35 | 5 | 2.2644s | 0.1309s | 1 | 8 | yes | 2.1840s | 2.3527s | `detyped_files/deltablue/shallow/proportion_sweep/main_k24_s05.py` |  |
| 0.69 | 24/35 | 6 | 2.1629s | 0.0473s | 1 | 8 | yes | 2.1355s | 2.1956s | `detyped_files/deltablue/shallow/proportion_sweep/main_k24_s06.py` |  |
| 0.69 | 24/35 | 7 | 2.2182s | 0.0950s | 1 | 8 | yes | 2.1574s | 2.2781s | `detyped_files/deltablue/shallow/proportion_sweep/main_k24_s07.py` |  |
| 0.69 | 24/35 | 8 | 2.5999s | 0.1228s | 1 | 8 | yes | 2.5369s | 2.6883s | `detyped_files/deltablue/shallow/proportion_sweep/main_k24_s08.py` |  |
| 0.69 | 24/35 | 9 | 2.4985s | 0.0643s | 1 | 8 | yes | 2.4587s | 2.5421s | `detyped_files/deltablue/shallow/proportion_sweep/main_k24_s09.py` |  |
| 0.69 | 24/35 | 10 | 2.4955s | 0.0611s | 1 | 8 | yes | 2.4559s | 2.5354s | `detyped_files/deltablue/shallow/proportion_sweep/main_k24_s10.py` |  |
| 0.69 | 24/35 | 11 | 2.2140s | 0.0963s | 1 | 8 | yes | 2.1512s | 2.2739s | `detyped_files/deltablue/shallow/proportion_sweep/main_k24_s11.py` |  |
| 0.69 | 24/35 | 12 | 2.4363s | 0.0774s | 1 | 8 | yes | 2.3856s | 2.4863s | `detyped_files/deltablue/shallow/proportion_sweep/main_k24_s12.py` |  |
| 0.69 | 24/35 | 13 | 2.0938s | 0.1510s | 1 | 8 | yes | 2.0144s | 2.2040s | `detyped_files/deltablue/shallow/proportion_sweep/main_k24_s13.py` |  |
| 0.69 | 24/35 | 14 | 1.4737s | 0.0952s | 1 | 8 | yes | 1.4171s | 1.5382s | `detyped_files/deltablue/shallow/proportion_sweep/main_k24_s14.py` |  |
| 0.69 | 24/35 | 15 | 2.1932s | 0.0698s | 1 | 8 | yes | 2.1481s | 2.2391s | `detyped_files/deltablue/shallow/proportion_sweep/main_k24_s15.py` |  |
| 0.69 | 24/35 | 16 | 2.4525s | 0.0491s | 1 | 8 | yes | 2.4212s | 2.4859s | `detyped_files/deltablue/shallow/proportion_sweep/main_k24_s16.py` |  |
| 0.69 | 24/35 | 17 | 1.8311s | 0.1142s | 1 | 8 | yes | 1.7704s | 1.9155s | `detyped_files/deltablue/shallow/proportion_sweep/main_k24_s17.py` |  |
| 0.69 | 24/35 | 18 | 2.4764s | 0.0785s | 1 | 8 | yes | 2.4312s | 2.5311s | `detyped_files/deltablue/shallow/proportion_sweep/main_k24_s18.py` |  |
| 0.69 | 24/35 | 19 | 1.7268s | 0.0906s | 1 | 8 | yes | 1.6692s | 1.7817s | `detyped_files/deltablue/shallow/proportion_sweep/main_k24_s19.py` |  |
| 0.69 | 24/35 | 20 | 2.1818s | 0.1209s | 1 | 8 | yes | 2.1165s | 2.2636s | `detyped_files/deltablue/shallow/proportion_sweep/main_k24_s20.py` |  |
| 0.71 | 25/35 | 1 | 2.6514s | 0.1422s | 1 | 8 | yes | 2.5626s | 2.7486s | `detyped_files/deltablue/shallow/proportion_sweep/main_k25_s01.py` |  |
| 0.71 | 25/35 | 2 | 2.0719s | 0.0451s | 1 | 8 | yes | 2.0418s | 2.1005s | `detyped_files/deltablue/shallow/proportion_sweep/main_k25_s02.py` |  |
| 0.71 | 25/35 | 3 | 1.9465s | 0.1117s | 1 | 8 | yes | 1.8748s | 2.0202s | `detyped_files/deltablue/shallow/proportion_sweep/main_k25_s03.py` |  |
| 0.71 | 25/35 | 4 | 1.9428s | 0.0909s | 1 | 8 | yes | 1.8878s | 2.0021s | `detyped_files/deltablue/shallow/proportion_sweep/main_k25_s04.py` |  |
| 0.71 | 25/35 | 5 | 2.2266s | 0.1081s | 1 | 8 | yes | 2.1637s | 2.3001s | `detyped_files/deltablue/shallow/proportion_sweep/main_k25_s05.py` |  |
| 0.71 | 25/35 | 6 | 2.2543s | 0.0443s | 1 | 8 | yes | 2.2241s | 2.2813s | `detyped_files/deltablue/shallow/proportion_sweep/main_k25_s06.py` |  |
| 0.71 | 25/35 | 7 | 2.5655s | 0.1551s | 1 | 8 | yes | 2.4745s | 2.6749s | `detyped_files/deltablue/shallow/proportion_sweep/main_k25_s07.py` |  |
| 0.71 | 25/35 | 8 | 2.1858s | 0.0794s | 1 | 8 | yes | 2.1336s | 2.2345s | `detyped_files/deltablue/shallow/proportion_sweep/main_k25_s08.py` |  |
| 0.71 | 25/35 | 9 | 2.3606s | 0.0723s | 1 | 8 | yes | 2.3136s | 2.4088s | `detyped_files/deltablue/shallow/proportion_sweep/main_k25_s09.py` |  |
| 0.71 | 25/35 | 10 | 2.1920s | 0.0810s | 1 | 8 | yes | 2.1390s | 2.2429s | `detyped_files/deltablue/shallow/proportion_sweep/main_k25_s10.py` |  |
| 0.71 | 25/35 | 11 | 2.4739s | 0.0956s | 1 | 8 | yes | 2.4193s | 2.5414s | `detyped_files/deltablue/shallow/proportion_sweep/main_k25_s11.py` |  |
| 0.71 | 25/35 | 12 | 2.3660s | 0.0995s | 1 | 8 | yes | 2.3048s | 2.4339s | `detyped_files/deltablue/shallow/proportion_sweep/main_k25_s12.py` |  |
| 0.71 | 25/35 | 13 | 2.3964s | 0.0759s | 1 | 8 | yes | 2.3533s | 2.4491s | `detyped_files/deltablue/shallow/proportion_sweep/main_k25_s13.py` |  |
| 0.71 | 25/35 | 14 | 1.9215s | 0.1204s | 1 | 8 | yes | 1.8463s | 1.9997s | `detyped_files/deltablue/shallow/proportion_sweep/main_k25_s14.py` |  |
| 0.71 | 25/35 | 15 | 1.9969s | 0.0849s | 1 | 8 | yes | 1.9422s | 2.0521s | `detyped_files/deltablue/shallow/proportion_sweep/main_k25_s15.py` |  |
| 0.71 | 25/35 | 16 | 2.1352s | 0.1302s | 1 | 8 | yes | 2.0582s | 2.2240s | `detyped_files/deltablue/shallow/proportion_sweep/main_k25_s16.py` |  |
| 0.71 | 25/35 | 17 | 2.3583s | 0.0865s | 1 | 8 | yes | 2.3027s | 2.4130s | `detyped_files/deltablue/shallow/proportion_sweep/main_k25_s17.py` |  |
| 0.71 | 25/35 | 18 | 2.5020s | 0.1046s | 1 | 8 | yes | 2.4359s | 2.5690s | `detyped_files/deltablue/shallow/proportion_sweep/main_k25_s18.py` |  |
| 0.71 | 25/35 | 19 | 2.6548s | 0.1123s | 1 | 8 | yes | 2.5822s | 2.7299s | `detyped_files/deltablue/shallow/proportion_sweep/main_k25_s19.py` |  |
| 0.71 | 25/35 | 20 | 2.3471s | 0.0730s | 1 | 8 | yes | 2.2974s | 2.3911s | `detyped_files/deltablue/shallow/proportion_sweep/main_k25_s20.py` |  |
| 0.74 | 26/35 | 1 | 2.1203s | 0.1096s | 1 | 8 | yes | 2.0558s | 2.1953s | `detyped_files/deltablue/shallow/proportion_sweep/main_k26_s01.py` |  |
| 0.74 | 26/35 | 2 | 2.6083s | 0.1363s | 1 | 8 | yes | 2.5249s | 2.7006s | `detyped_files/deltablue/shallow/proportion_sweep/main_k26_s02.py` |  |
| 0.74 | 26/35 | 3 | 2.5179s | 0.0550s | 1 | 8 | yes | 2.4811s | 2.5524s | `detyped_files/deltablue/shallow/proportion_sweep/main_k26_s03.py` |  |
| 0.74 | 26/35 | 4 | 1.5996s | 0.0756s | 1 | 8 | yes | 1.5479s | 1.6452s | `detyped_files/deltablue/shallow/proportion_sweep/main_k26_s04.py` |  |
| 0.74 | 26/35 | 5 | 2.6453s | 0.1577s | 1 | 8 | yes | 2.5510s | 2.7506s | `detyped_files/deltablue/shallow/proportion_sweep/main_k26_s05.py` |  |
| 0.74 | 26/35 | 6 | 2.4387s | 0.1387s | 1 | 8 | yes | 2.3545s | 2.5336s | `detyped_files/deltablue/shallow/proportion_sweep/main_k26_s06.py` |  |
| 0.74 | 26/35 | 7 | 2.5549s | 0.1121s | 1 | 8 | yes | 2.4983s | 2.6352s | `detyped_files/deltablue/shallow/proportion_sweep/main_k26_s07.py` |  |
| 0.74 | 26/35 | 8 | 2.0510s | 0.1102s | 1 | 8 | yes | 1.9865s | 2.1284s | `detyped_files/deltablue/shallow/proportion_sweep/main_k26_s08.py` |  |
| 0.74 | 26/35 | 9 | 2.4446s | 0.1158s | 1 | 8 | yes | 2.3801s | 2.5289s | `detyped_files/deltablue/shallow/proportion_sweep/main_k26_s09.py` |  |
| 0.74 | 26/35 | 10 | 2.1410s | 0.1272s | 1 | 8 | yes | 2.0738s | 2.2330s | `detyped_files/deltablue/shallow/proportion_sweep/main_k26_s10.py` |  |
| 0.74 | 26/35 | 11 | 2.4168s | 0.0974s | 1 | 8 | yes | 2.3532s | 2.4797s | `detyped_files/deltablue/shallow/proportion_sweep/main_k26_s11.py` |  |
| 0.74 | 26/35 | 12 | 1.9586s | 0.0625s | 1 | 8 | yes | 1.9191s | 2.0010s | `detyped_files/deltablue/shallow/proportion_sweep/main_k26_s12.py` |  |
| 0.74 | 26/35 | 13 | 2.4138s | 0.0864s | 1 | 8 | yes | 2.3604s | 2.4712s | `detyped_files/deltablue/shallow/proportion_sweep/main_k26_s13.py` |  |
| 0.74 | 26/35 | 14 | 1.4329s | 0.0729s | 1 | 8 | yes | 1.3841s | 1.4780s | `detyped_files/deltablue/shallow/proportion_sweep/main_k26_s14.py` |  |
| 0.74 | 26/35 | 15 | 2.6018s | 0.0899s | 1 | 8 | yes | 2.5416s | 2.6587s | `detyped_files/deltablue/shallow/proportion_sweep/main_k26_s15.py` |  |
| 0.74 | 26/35 | 16 | 2.4057s | 0.0305s | 1 | 8 | yes | 2.3869s | 2.4256s | `detyped_files/deltablue/shallow/proportion_sweep/main_k26_s16.py` |  |
| 0.74 | 26/35 | 17 | 1.9194s | 0.0579s | 1 | 8 | yes | 1.8819s | 1.9578s | `detyped_files/deltablue/shallow/proportion_sweep/main_k26_s17.py` |  |
| 0.74 | 26/35 | 18 | 1.4833s | 0.0726s | 1 | 8 | yes | 1.4379s | 1.5318s | `detyped_files/deltablue/shallow/proportion_sweep/main_k26_s18.py` |  |
| 0.74 | 26/35 | 19 | 2.4423s | 0.0922s | 1 | 8 | yes | 2.3859s | 2.5049s | `detyped_files/deltablue/shallow/proportion_sweep/main_k26_s19.py` |  |
| 0.74 | 26/35 | 20 | 2.1585s | 0.0229s | 1 | 8 | yes | 2.1432s | 2.1730s | `detyped_files/deltablue/shallow/proportion_sweep/main_k26_s20.py` |  |
| 0.77 | 27/35 | 1 | 2.5921s | 0.0982s | 1 | 8 | yes | 2.5305s | 2.6570s | `detyped_files/deltablue/shallow/proportion_sweep/main_k27_s01.py` |  |
| 0.77 | 27/35 | 2 | 2.1329s | 0.0868s | 1 | 8 | yes | 2.0815s | 2.1945s | `detyped_files/deltablue/shallow/proportion_sweep/main_k27_s02.py` |  |
| 0.77 | 27/35 | 3 | 2.1383s | 0.1167s | 1 | 8 | yes | 2.0588s | 2.2103s | `detyped_files/deltablue/shallow/proportion_sweep/main_k27_s03.py` |  |
| 0.77 | 27/35 | 4 | 1.5881s | 0.0932s | 1 | 8 | yes | 1.5293s | 1.6493s | `detyped_files/deltablue/shallow/proportion_sweep/main_k27_s04.py` |  |
| 0.77 | 27/35 | 5 | 2.6068s | 0.0543s | 1 | 8 | yes | 2.5755s | 2.6446s | `detyped_files/deltablue/shallow/proportion_sweep/main_k27_s05.py` |  |
| 0.77 | 27/35 | 6 | 2.2669s | 0.0709s | 1 | 8 | yes | 2.2256s | 2.3177s | `detyped_files/deltablue/shallow/proportion_sweep/main_k27_s06.py` |  |
| 0.77 | 27/35 | 7 | 1.8805s | 0.0687s | 1 | 8 | yes | 1.8367s | 1.9256s | `detyped_files/deltablue/shallow/proportion_sweep/main_k27_s07.py` |  |
| 0.77 | 27/35 | 8 | 2.6030s | 0.2253s | 1 | 8 | yes | 2.4753s | 2.7621s | `detyped_files/deltablue/shallow/proportion_sweep/main_k27_s08.py` |  |
| 0.77 | 27/35 | 9 | 2.3955s | 0.0645s | 1 | 8 | yes | 2.3593s | 2.4414s | `detyped_files/deltablue/shallow/proportion_sweep/main_k27_s09.py` |  |
| 0.77 | 27/35 | 10 | 2.2222s | 0.0948s | 1 | 8 | yes | 2.1699s | 2.2898s | `detyped_files/deltablue/shallow/proportion_sweep/main_k27_s10.py` |  |
| 0.77 | 27/35 | 11 | 2.1172s | 0.1089s | 1 | 8 | yes | 2.0576s | 2.1958s | `detyped_files/deltablue/shallow/proportion_sweep/main_k27_s11.py` |  |
| 0.77 | 27/35 | 12 | 2.5462s | 0.0774s | 1 | 8 | yes | 2.4960s | 2.5964s | `detyped_files/deltablue/shallow/proportion_sweep/main_k27_s12.py` |  |
| 0.77 | 27/35 | 13 | 2.4461s | 0.0849s | 1 | 8 | yes | 2.3850s | 2.4969s | `detyped_files/deltablue/shallow/proportion_sweep/main_k27_s13.py` |  |
| 0.77 | 27/35 | 14 | 1.9833s | 0.0721s | 1 | 8 | yes | 1.9376s | 2.0316s | `detyped_files/deltablue/shallow/proportion_sweep/main_k27_s14.py` |  |
| 0.77 | 27/35 | 15 | 2.5106s | 0.0995s | 1 | 8 | yes | 2.4452s | 2.5741s | `detyped_files/deltablue/shallow/proportion_sweep/main_k27_s15.py` |  |
| 0.77 | 27/35 | 16 | 2.5019s | 0.0210s | 1 | 8 | yes | 2.4888s | 2.5162s | `detyped_files/deltablue/shallow/proportion_sweep/main_k27_s16.py` |  |
| 0.77 | 27/35 | 17 | 2.0687s | 0.0719s | 1 | 8 | yes | 2.0226s | 2.1172s | `detyped_files/deltablue/shallow/proportion_sweep/main_k27_s17.py` |  |
| 0.77 | 27/35 | 18 | 2.6274s | 0.0928s | 1 | 8 | yes | 2.5707s | 2.6904s | `detyped_files/deltablue/shallow/proportion_sweep/main_k27_s18.py` |  |
| 0.77 | 27/35 | 19 | 2.0563s | 0.0626s | 1 | 8 | yes | 2.0169s | 2.0967s | `detyped_files/deltablue/shallow/proportion_sweep/main_k27_s19.py` |  |
| 0.77 | 27/35 | 20 | 2.1151s | 0.0726s | 1 | 8 | yes | 2.0668s | 2.1604s | `detyped_files/deltablue/shallow/proportion_sweep/main_k27_s20.py` |  |
| 0.80 | 28/35 | 1 | 2.6209s | 0.0662s | 1 | 8 | yes | 2.5779s | 2.6633s | `detyped_files/deltablue/shallow/proportion_sweep/main_k28_s01.py` |  |
| 0.80 | 28/35 | 2 | 2.3873s | 0.1162s | 1 | 8 | yes | 2.3230s | 2.4709s | `detyped_files/deltablue/shallow/proportion_sweep/main_k28_s02.py` |  |
| 0.80 | 28/35 | 3 | 2.5344s | 0.0696s | 1 | 8 | yes | 2.4922s | 2.5804s | `detyped_files/deltablue/shallow/proportion_sweep/main_k28_s03.py` |  |
| 0.80 | 28/35 | 4 | 2.1067s | 0.0761s | 1 | 8 | yes | 2.0633s | 2.1597s | `detyped_files/deltablue/shallow/proportion_sweep/main_k28_s04.py` |  |
| 0.80 | 28/35 | 5 | 2.2529s | 0.0756s | 1 | 8 | yes | 2.2003s | 2.2988s | `detyped_files/deltablue/shallow/proportion_sweep/main_k28_s05.py` |  |
| 0.80 | 28/35 | 6 | 2.0317s | 0.0596s | 1 | 8 | yes | 1.9883s | 2.0654s | `detyped_files/deltablue/shallow/proportion_sweep/main_k28_s06.py` |  |
| 0.80 | 28/35 | 7 | 2.1198s | 0.0881s | 1 | 8 | yes | 2.0704s | 2.1831s | `detyped_files/deltablue/shallow/proportion_sweep/main_k28_s07.py` |  |
| 0.80 | 28/35 | 8 | 2.3150s | 0.1262s | 1 | 8 | yes | 2.2377s | 2.3987s | `detyped_files/deltablue/shallow/proportion_sweep/main_k28_s08.py` |  |
| 0.80 | 28/35 | 9 | 2.0101s | 0.0594s | 1 | 8 | yes | 1.9683s | 2.0438s | `detyped_files/deltablue/shallow/proportion_sweep/main_k28_s09.py` |  |
| 0.80 | 28/35 | 10 | 2.0431s | 0.1003s | 1 | 8 | yes | 1.9775s | 2.1081s | `detyped_files/deltablue/shallow/proportion_sweep/main_k28_s10.py` |  |
| 0.80 | 28/35 | 11 | 2.2081s | 0.1430s | 1 | 8 | yes | 2.1239s | 2.3093s | `detyped_files/deltablue/shallow/proportion_sweep/main_k28_s11.py` |  |
| 0.80 | 28/35 | 12 | 1.6776s | 0.1195s | 1 | 8 | yes | 1.6124s | 1.7630s | `detyped_files/deltablue/shallow/proportion_sweep/main_k28_s12.py` |  |
| 0.80 | 28/35 | 13 | 2.5123s | 0.0515s | 1 | 8 | yes | 2.4765s | 2.5409s | `detyped_files/deltablue/shallow/proportion_sweep/main_k28_s13.py` |  |
| 0.80 | 28/35 | 14 | 2.1154s | 0.0558s | 1 | 8 | yes | 2.0773s | 2.1495s | `detyped_files/deltablue/shallow/proportion_sweep/main_k28_s14.py` |  |
| 0.80 | 28/35 | 15 | 2.5328s | 0.0959s | 1 | 8 | yes | 2.4733s | 2.5968s | `detyped_files/deltablue/shallow/proportion_sweep/main_k28_s15.py` |  |
| 0.80 | 28/35 | 16 | 2.5663s | 0.1056s | 1 | 8 | yes | 2.5078s | 2.6430s | `detyped_files/deltablue/shallow/proportion_sweep/main_k28_s16.py` |  |
| 0.80 | 28/35 | 17 | 2.5223s | 0.0669s | 1 | 8 | yes | 2.4842s | 2.5701s | `detyped_files/deltablue/shallow/proportion_sweep/main_k28_s17.py` |  |
| 0.80 | 28/35 | 18 | 2.5940s | 0.0754s | 1 | 8 | yes | 2.5478s | 2.6443s | `detyped_files/deltablue/shallow/proportion_sweep/main_k28_s18.py` |  |
| 0.80 | 28/35 | 19 | 2.1161s | 0.0659s | 1 | 8 | yes | 2.0780s | 2.1637s | `detyped_files/deltablue/shallow/proportion_sweep/main_k28_s19.py` |  |
| 0.80 | 28/35 | 20 | 2.1119s | 0.0726s | 1 | 8 | yes | 2.0653s | 2.1585s | `detyped_files/deltablue/shallow/proportion_sweep/main_k28_s20.py` |  |
| 0.83 | 29/35 | 1 | 2.4815s | 0.1117s | 1 | 8 | yes | 2.4137s | 2.5587s | `detyped_files/deltablue/shallow/proportion_sweep/main_k29_s01.py` |  |
| 0.83 | 29/35 | 2 | 2.0736s | 0.0793s | 1 | 8 | yes | 2.0253s | 2.1267s | `detyped_files/deltablue/shallow/proportion_sweep/main_k29_s02.py` |  |
| 0.83 | 29/35 | 3 | 2.5170s | 0.1001s | 1 | 8 | yes | 2.4602s | 2.5872s | `detyped_files/deltablue/shallow/proportion_sweep/main_k29_s03.py` |  |
| 0.83 | 29/35 | 4 | 2.4148s | 0.0594s | 1 | 8 | yes | 2.3766s | 2.4539s | `detyped_files/deltablue/shallow/proportion_sweep/main_k29_s04.py` |  |
| 0.83 | 29/35 | 5 | 2.1144s | 0.1066s | 1 | 8 | yes | 2.0582s | 2.1922s | `detyped_files/deltablue/shallow/proportion_sweep/main_k29_s05.py` |  |
| 0.83 | 29/35 | 6 | 2.5573s | 0.0909s | 1 | 8 | yes | 2.4983s | 2.6153s | `detyped_files/deltablue/shallow/proportion_sweep/main_k29_s06.py` |  |
| 0.83 | 29/35 | 7 | 2.6492s | 0.1481s | 1 | 8 | yes | 2.5593s | 2.7494s | `detyped_files/deltablue/shallow/proportion_sweep/main_k29_s07.py` |  |
| 0.83 | 29/35 | 8 | 2.3397s | 0.0977s | 1 | 8 | yes | 2.2730s | 2.3997s | `detyped_files/deltablue/shallow/proportion_sweep/main_k29_s08.py` |  |
| 0.83 | 29/35 | 9 | 2.5010s | 0.1003s | 1 | 8 | yes | 2.4357s | 2.5646s | `detyped_files/deltablue/shallow/proportion_sweep/main_k29_s09.py` |  |
| 0.83 | 29/35 | 10 | 2.6842s | 0.1072s | 1 | 8 | yes | 2.6262s | 2.7610s | `detyped_files/deltablue/shallow/proportion_sweep/main_k29_s10.py` |  |
| 0.83 | 29/35 | 11 | 2.3920s | 0.1468s | 1 | 8 | yes | 2.3026s | 2.4913s | `detyped_files/deltablue/shallow/proportion_sweep/main_k29_s11.py` |  |
| 0.83 | 29/35 | 12 | 2.5341s | 0.1079s | 1 | 8 | yes | 2.4654s | 2.6037s | `detyped_files/deltablue/shallow/proportion_sweep/main_k29_s12.py` |  |
| 0.83 | 29/35 | 13 | 2.4595s | 0.0593s | 1 | 8 | yes | 2.4216s | 2.4983s | `detyped_files/deltablue/shallow/proportion_sweep/main_k29_s13.py` |  |
| 0.83 | 29/35 | 14 | 2.2315s | 0.1292s | 1 | 8 | yes | 2.1582s | 2.3215s | `detyped_files/deltablue/shallow/proportion_sweep/main_k29_s14.py` |  |
| 0.83 | 29/35 | 15 | 2.0994s | 0.0899s | 1 | 8 | yes | 2.0414s | 2.1553s | `detyped_files/deltablue/shallow/proportion_sweep/main_k29_s15.py` |  |
| 0.83 | 29/35 | 16 | 2.5451s | 0.1331s | 1 | 8 | yes | 2.4594s | 2.6300s | `detyped_files/deltablue/shallow/proportion_sweep/main_k29_s16.py` |  |
| 0.83 | 29/35 | 17 | 2.1596s | 0.0905s | 1 | 8 | yes | 2.1031s | 2.2211s | `detyped_files/deltablue/shallow/proportion_sweep/main_k29_s17.py` |  |
| 0.83 | 29/35 | 18 | 2.3394s | 0.0679s | 1 | 8 | yes | 2.2940s | 2.3812s | `detyped_files/deltablue/shallow/proportion_sweep/main_k29_s18.py` |  |
| 0.83 | 29/35 | 19 | 2.1870s | 0.0650s | 1 | 8 | yes | 2.1450s | 2.2288s | `detyped_files/deltablue/shallow/proportion_sweep/main_k29_s19.py` |  |
| 0.83 | 29/35 | 20 | 2.7543s | 0.2839s | 1 | 8 | yes | 2.6074s | 2.9627s | `detyped_files/deltablue/shallow/proportion_sweep/main_k29_s20.py` |  |
| 0.86 | 30/35 | 1 | 2.6268s | 0.1339s | 1 | 8 | yes | 2.5468s | 2.7190s | `detyped_files/deltablue/shallow/proportion_sweep/main_k30_s01.py` |  |
| 0.86 | 30/35 | 2 | 2.5099s | 0.1396s | 1 | 8 | yes | 2.4340s | 2.6094s | `detyped_files/deltablue/shallow/proportion_sweep/main_k30_s02.py` |  |
| 0.86 | 30/35 | 3 | 2.5578s | 0.0530s | 1 | 8 | yes | 2.5247s | 2.5931s | `detyped_files/deltablue/shallow/proportion_sweep/main_k30_s03.py` |  |
| 0.86 | 30/35 | 4 | 1.9602s | 0.0694s | 1 | 8 | yes | 1.9138s | 2.0040s | `detyped_files/deltablue/shallow/proportion_sweep/main_k30_s04.py` |  |
| 0.86 | 30/35 | 5 | 2.6407s | 0.1049s | 1 | 8 | yes | 2.5794s | 2.7140s | `detyped_files/deltablue/shallow/proportion_sweep/main_k30_s05.py` |  |
| 0.86 | 30/35 | 6 | 2.4811s | 0.1321s | 1 | 8 | yes | 2.4021s | 2.5711s | `detyped_files/deltablue/shallow/proportion_sweep/main_k30_s06.py` |  |
| 0.86 | 30/35 | 7 | 2.4769s | 0.0452s | 1 | 8 | yes | 2.4475s | 2.5059s | `detyped_files/deltablue/shallow/proportion_sweep/main_k30_s07.py` |  |
| 0.86 | 30/35 | 8 | 2.6190s | 0.0894s | 1 | 8 | yes | 2.5643s | 2.6784s | `detyped_files/deltablue/shallow/proportion_sweep/main_k30_s08.py` |  |
| 0.86 | 30/35 | 9 | 2.5315s | 0.1164s | 1 | 8 | yes | 2.4655s | 2.6130s | `detyped_files/deltablue/shallow/proportion_sweep/main_k30_s09.py` |  |
| 0.86 | 30/35 | 10 | 1.7899s | 0.0853s | 1 | 8 | yes | 1.7389s | 1.8505s | `detyped_files/deltablue/shallow/proportion_sweep/main_k30_s10.py` |  |
| 0.86 | 30/35 | 11 | 2.5047s | 0.0689s | 1 | 8 | yes | 2.4583s | 2.5474s | `detyped_files/deltablue/shallow/proportion_sweep/main_k30_s11.py` |  |
| 0.86 | 30/35 | 12 | 2.0987s | 0.1075s | 1 | 8 | yes | 2.0325s | 2.1697s | `detyped_files/deltablue/shallow/proportion_sweep/main_k30_s12.py` |  |
| 0.86 | 30/35 | 13 | 2.0594s | 0.0791s | 1 | 8 | yes | 2.0088s | 2.1102s | `detyped_files/deltablue/shallow/proportion_sweep/main_k30_s13.py` |  |
| 0.86 | 30/35 | 14 | 2.2387s | 0.0799s | 1 | 8 | yes | 2.1892s | 2.2919s | `detyped_files/deltablue/shallow/proportion_sweep/main_k30_s14.py` |  |
| 0.86 | 30/35 | 15 | 2.6251s | 0.0917s | 1 | 8 | yes | 2.5686s | 2.6866s | `detyped_files/deltablue/shallow/proportion_sweep/main_k30_s15.py` |  |
| 0.86 | 30/35 | 16 | 2.5918s | 0.0392s | 1 | 8 | yes | 2.5684s | 2.6188s | `detyped_files/deltablue/shallow/proportion_sweep/main_k30_s16.py` |  |
| 0.86 | 30/35 | 17 | 2.6252s | 0.1338s | 1 | 8 | yes | 2.5419s | 2.7138s | `detyped_files/deltablue/shallow/proportion_sweep/main_k30_s17.py` |  |
| 0.86 | 30/35 | 18 | 2.5183s | 0.1182s | 1 | 8 | yes | 2.4445s | 2.5982s | `detyped_files/deltablue/shallow/proportion_sweep/main_k30_s18.py` |  |
| 0.86 | 30/35 | 19 | 2.3904s | 0.0633s | 1 | 8 | yes | 2.3508s | 2.4310s | `detyped_files/deltablue/shallow/proportion_sweep/main_k30_s19.py` |  |
| 0.86 | 30/35 | 20 | 2.0797s | 0.0452s | 1 | 8 | yes | 2.0476s | 2.1063s | `detyped_files/deltablue/shallow/proportion_sweep/main_k30_s20.py` |  |
| 0.89 | 31/35 | 1 | 2.5184s | 0.0598s | 1 | 8 | yes | 2.4770s | 2.5532s | `detyped_files/deltablue/shallow/proportion_sweep/main_k31_s01.py` |  |
| 0.89 | 31/35 | 2 | 2.5667s | 0.1164s | 1 | 8 | yes | 2.4961s | 2.6466s | `detyped_files/deltablue/shallow/proportion_sweep/main_k31_s02.py` |  |
| 0.89 | 31/35 | 3 | 2.6289s | 0.0657s | 1 | 8 | yes | 2.5902s | 2.6746s | `detyped_files/deltablue/shallow/proportion_sweep/main_k31_s03.py` |  |
| 0.89 | 31/35 | 4 | 2.6404s | 0.1236s | 1 | 8 | yes | 2.5558s | 2.7160s | `detyped_files/deltablue/shallow/proportion_sweep/main_k31_s04.py` |  |
| 0.89 | 31/35 | 5 | 2.7292s | 0.1715s | 1 | 8 | yes | 2.6267s | 2.8435s | `detyped_files/deltablue/shallow/proportion_sweep/main_k31_s05.py` |  |
| 0.89 | 31/35 | 6 | 2.6458s | 0.0977s | 1 | 8 | yes | 2.5804s | 2.7076s | `detyped_files/deltablue/shallow/proportion_sweep/main_k31_s06.py` |  |
| 0.89 | 31/35 | 7 | 2.5827s | 0.1238s | 1 | 8 | yes | 2.5055s | 2.6670s | `detyped_files/deltablue/shallow/proportion_sweep/main_k31_s07.py` |  |
| 0.89 | 31/35 | 8 | 2.3218s | 0.0885s | 1 | 8 | yes | 2.2649s | 2.3784s | `detyped_files/deltablue/shallow/proportion_sweep/main_k31_s08.py` |  |
| 0.89 | 31/35 | 9 | 2.2381s | 0.1031s | 1 | 8 | yes | 2.1904s | 2.3130s | `detyped_files/deltablue/shallow/proportion_sweep/main_k31_s09.py` |  |
| 0.89 | 31/35 | 10 | 2.6704s | 0.1179s | 1 | 8 | yes | 2.5990s | 2.7521s | `detyped_files/deltablue/shallow/proportion_sweep/main_k31_s10.py` |  |
| 0.89 | 31/35 | 11 | 1.6623s | 0.0671s | 1 | 8 | yes | 1.6185s | 1.7037s | `detyped_files/deltablue/shallow/proportion_sweep/main_k31_s11.py` |  |
| 0.89 | 31/35 | 12 | 2.1695s | 0.0643s | 1 | 8 | yes | 2.1297s | 2.2113s | `detyped_files/deltablue/shallow/proportion_sweep/main_k31_s12.py` |  |
| 0.89 | 31/35 | 13 | 2.5631s | 0.0607s | 1 | 8 | yes | 2.5233s | 2.6006s | `detyped_files/deltablue/shallow/proportion_sweep/main_k31_s13.py` |  |
| 0.89 | 31/35 | 14 | 2.4194s | 0.1074s | 1 | 8 | yes | 2.3556s | 2.4938s | `detyped_files/deltablue/shallow/proportion_sweep/main_k31_s14.py` |  |
| 0.89 | 31/35 | 15 | 2.4896s | 0.1072s | 1 | 8 | yes | 2.4220s | 2.5630s | `detyped_files/deltablue/shallow/proportion_sweep/main_k31_s15.py` |  |
| 0.89 | 31/35 | 16 | 2.3832s | 0.1005s | 1 | 8 | yes | 2.3172s | 2.4458s | `detyped_files/deltablue/shallow/proportion_sweep/main_k31_s16.py` |  |
| 0.89 | 31/35 | 17 | 2.6113s | 0.0516s | 1 | 8 | yes | 2.5734s | 2.6380s | `detyped_files/deltablue/shallow/proportion_sweep/main_k31_s17.py` |  |
| 0.89 | 31/35 | 18 | 2.5412s | 0.0986s | 1 | 8 | yes | 2.4774s | 2.6039s | `detyped_files/deltablue/shallow/proportion_sweep/main_k31_s18.py` |  |
| 0.89 | 31/35 | 19 | 2.1050s | 0.0877s | 1 | 8 | yes | 2.0425s | 2.1574s | `detyped_files/deltablue/shallow/proportion_sweep/main_k31_s19.py` |  |
| 0.89 | 31/35 | 20 | 2.2229s | 0.0976s | 1 | 8 | yes | 2.1704s | 2.2950s | `detyped_files/deltablue/shallow/proportion_sweep/main_k31_s20.py` |  |
| 0.91 | 32/35 | 1 | 2.5273s | 0.1001s | 1 | 8 | yes | 2.4627s | 2.5916s | `detyped_files/deltablue/shallow/proportion_sweep/main_k32_s01.py` |  |
| 0.91 | 32/35 | 2 | 2.6507s | 0.1070s | 1 | 8 | yes | 2.5789s | 2.7179s | `detyped_files/deltablue/shallow/proportion_sweep/main_k32_s02.py` |  |
| 0.91 | 32/35 | 3 | 2.6393s | 0.1054s | 1 | 8 | yes | 2.5743s | 2.7108s | `detyped_files/deltablue/shallow/proportion_sweep/main_k32_s03.py` |  |
| 0.91 | 32/35 | 4 | 2.5903s | 0.0915s | 1 | 8 | yes | 2.5351s | 2.6537s | `detyped_files/deltablue/shallow/proportion_sweep/main_k32_s04.py` |  |
| 0.91 | 32/35 | 5 | 2.4970s | 0.0930s | 1 | 8 | yes | 2.4367s | 2.5576s | `detyped_files/deltablue/shallow/proportion_sweep/main_k32_s05.py` |  |
| 0.91 | 32/35 | 6 | 2.5648s | 0.0414s | 1 | 8 | yes | 2.5374s | 2.5913s | `detyped_files/deltablue/shallow/proportion_sweep/main_k32_s06.py` |  |
| 0.91 | 32/35 | 7 | 2.3821s | 0.0376s | 1 | 8 | yes | 2.3545s | 2.4023s | `detyped_files/deltablue/shallow/proportion_sweep/main_k32_s07.py` |  |
| 0.91 | 32/35 | 8 | 2.4932s | 0.0726s | 1 | 8 | yes | 2.4414s | 2.5375s | `detyped_files/deltablue/shallow/proportion_sweep/main_k32_s08.py` |  |
| 0.91 | 32/35 | 9 | 2.4969s | 0.0845s | 1 | 8 | yes | 2.4407s | 2.5506s | `detyped_files/deltablue/shallow/proportion_sweep/main_k32_s09.py` |  |
| 0.91 | 32/35 | 10 | 2.3995s | 0.0757s | 1 | 8 | yes | 2.3528s | 2.4510s | `detyped_files/deltablue/shallow/proportion_sweep/main_k32_s10.py` |  |
| 0.91 | 32/35 | 11 | 2.4993s | 0.0497s | 1 | 8 | yes | 2.4709s | 2.5355s | `detyped_files/deltablue/shallow/proportion_sweep/main_k32_s11.py` |  |
| 0.91 | 32/35 | 12 | 2.4654s | 0.0735s | 1 | 8 | yes | 2.4206s | 2.5175s | `detyped_files/deltablue/shallow/proportion_sweep/main_k32_s12.py` |  |
| 0.91 | 32/35 | 13 | 2.2606s | 0.1235s | 1 | 8 | yes | 2.1811s | 2.3407s | `detyped_files/deltablue/shallow/proportion_sweep/main_k32_s13.py` |  |
| 0.91 | 32/35 | 14 | 2.4545s | 0.1139s | 1 | 8 | yes | 2.3820s | 2.5312s | `detyped_files/deltablue/shallow/proportion_sweep/main_k32_s14.py` |  |
| 0.91 | 32/35 | 15 | 2.3200s | 0.1265s | 1 | 8 | yes | 2.2448s | 2.4058s | `detyped_files/deltablue/shallow/proportion_sweep/main_k32_s15.py` |  |
| 0.91 | 32/35 | 16 | 2.6822s | 0.1700s | 1 | 8 | yes | 2.5876s | 2.8044s | `detyped_files/deltablue/shallow/proportion_sweep/main_k32_s16.py` |  |
| 0.91 | 32/35 | 17 | 2.5817s | 0.1055s | 1 | 8 | yes | 2.5190s | 2.6531s | `detyped_files/deltablue/shallow/proportion_sweep/main_k32_s17.py` |  |
| 0.91 | 32/35 | 18 | 2.4866s | 0.0740s | 1 | 8 | yes | 2.4414s | 2.5378s | `detyped_files/deltablue/shallow/proportion_sweep/main_k32_s18.py` |  |
| 0.91 | 32/35 | 19 | 2.4368s | 0.0669s | 1 | 8 | yes | 2.3886s | 2.4737s | `detyped_files/deltablue/shallow/proportion_sweep/main_k32_s19.py` |  |
| 0.91 | 32/35 | 20 | 2.2373s | 0.1207s | 1 | 8 | yes | 2.1603s | 2.3155s | `detyped_files/deltablue/shallow/proportion_sweep/main_k32_s20.py` |  |
| 0.94 | 33/35 | 1 | 2.2935s | 0.1005s | 1 | 8 | yes | 2.2381s | 2.3683s | `detyped_files/deltablue/shallow/proportion_sweep/main_k33_s01.py` |  |
| 0.94 | 33/35 | 2 | 2.6678s | 0.1055s | 1 | 8 | yes | 2.6036s | 2.7416s | `detyped_files/deltablue/shallow/proportion_sweep/main_k33_s02.py` |  |
| 0.94 | 33/35 | 3 | 2.5152s | 0.0696s | 1 | 8 | yes | 2.4733s | 2.5624s | `detyped_files/deltablue/shallow/proportion_sweep/main_k33_s03.py` |  |
| 0.94 | 33/35 | 4 | 2.5328s | 0.0434s | 1 | 8 | yes | 2.5037s | 2.5599s | `detyped_files/deltablue/shallow/proportion_sweep/main_k33_s04.py` |  |
| 0.94 | 33/35 | 5 | 2.1603s | 0.0807s | 1 | 8 | yes | 2.1087s | 2.2130s | `detyped_files/deltablue/shallow/proportion_sweep/main_k33_s05.py` |  |
| 0.94 | 33/35 | 6 | 2.6516s | 0.1589s | 1 | 8 | yes | 2.5541s | 2.7593s | `detyped_files/deltablue/shallow/proportion_sweep/main_k33_s06.py` |  |
| 0.94 | 33/35 | 7 | 2.4155s | 0.0734s | 1 | 8 | yes | 2.3690s | 2.4635s | `detyped_files/deltablue/shallow/proportion_sweep/main_k33_s07.py` |  |
| 0.94 | 33/35 | 8 | 2.6426s | 0.0967s | 1 | 8 | yes | 2.5826s | 2.7069s | `detyped_files/deltablue/shallow/proportion_sweep/main_k33_s08.py` |  |
| 0.94 | 33/35 | 9 | 2.6509s | 0.0667s | 1 | 8 | yes | 2.6090s | 2.6952s | `detyped_files/deltablue/shallow/proportion_sweep/main_k33_s09.py` |  |
| 0.94 | 33/35 | 10 | 2.6482s | 0.1124s | 1 | 8 | yes | 2.5902s | 2.7263s | `detyped_files/deltablue/shallow/proportion_sweep/main_k33_s10.py` |  |
| 0.94 | 33/35 | 11 | 2.6596s | 0.1286s | 1 | 8 | yes | 2.5940s | 2.7556s | `detyped_files/deltablue/shallow/proportion_sweep/main_k33_s11.py` |  |
| 0.94 | 33/35 | 12 | 2.6980s | 0.1509s | 1 | 8 | yes | 2.6030s | 2.7952s | `detyped_files/deltablue/shallow/proportion_sweep/main_k33_s12.py` |  |
| 0.94 | 33/35 | 13 | 2.0913s | 0.0856s | 1 | 8 | yes | 2.0407s | 2.1516s | `detyped_files/deltablue/shallow/proportion_sweep/main_k33_s13.py` |  |
| 0.94 | 33/35 | 14 | 2.4291s | 0.0725s | 1 | 8 | yes | 2.3786s | 2.4716s | `detyped_files/deltablue/shallow/proportion_sweep/main_k33_s14.py` |  |
| 0.94 | 33/35 | 15 | 2.4244s | 0.0453s | 1 | 8 | yes | 2.3924s | 2.4500s | `detyped_files/deltablue/shallow/proportion_sweep/main_k33_s15.py` |  |
| 0.94 | 33/35 | 16 | 2.6202s | 0.1074s | 1 | 8 | yes | 2.5520s | 2.6928s | `detyped_files/deltablue/shallow/proportion_sweep/main_k33_s16.py` |  |
| 0.94 | 33/35 | 17 | 2.5970s | 0.1138s | 1 | 8 | yes | 2.5256s | 2.6723s | `detyped_files/deltablue/shallow/proportion_sweep/main_k33_s17.py` |  |
| 0.94 | 33/35 | 18 | 2.6113s | 0.0631s | 1 | 8 | yes | 2.5712s | 2.6525s | `detyped_files/deltablue/shallow/proportion_sweep/main_k33_s18.py` |  |
| 0.94 | 33/35 | 19 | 2.6969s | 0.1353s | 1 | 8 | yes | 2.6111s | 2.7889s | `detyped_files/deltablue/shallow/proportion_sweep/main_k33_s19.py` |  |
| 0.94 | 33/35 | 20 | 2.5904s | 0.0676s | 1 | 8 | yes | 2.5470s | 2.6341s | `detyped_files/deltablue/shallow/proportion_sweep/main_k33_s20.py` |  |
| 0.97 | 34/35 | 1 | 2.5903s | 0.0771s | 1 | 8 | yes | 2.5444s | 2.6416s | `detyped_files/deltablue/shallow/proportion_sweep/main_k34_s01.py` |  |
| 0.97 | 34/35 | 2 | 2.6620s | 0.1133s | 1 | 8 | yes | 2.5916s | 2.7359s | `detyped_files/deltablue/shallow/proportion_sweep/main_k34_s02.py` |  |
| 0.97 | 34/35 | 3 | 2.5244s | 0.0320s | 1 | 8 | yes | 2.5044s | 2.5456s | `detyped_files/deltablue/shallow/proportion_sweep/main_k34_s03.py` |  |
| 0.97 | 34/35 | 4 | 2.6822s | 0.0965s | 1 | 8 | yes | 2.6215s | 2.7468s | `detyped_files/deltablue/shallow/proportion_sweep/main_k34_s04.py` |  |
| 0.97 | 34/35 | 5 | 2.6073s | 0.0531s | 1 | 8 | yes | 2.5695s | 2.6372s | `detyped_files/deltablue/shallow/proportion_sweep/main_k34_s05.py` |  |
| 0.97 | 34/35 | 6 | 2.6604s | 0.1086s | 1 | 8 | yes | 2.5864s | 2.7270s | `detyped_files/deltablue/shallow/proportion_sweep/main_k34_s06.py` |  |
| 0.97 | 34/35 | 7 | 2.5652s | 0.0731s | 1 | 8 | yes | 2.5150s | 2.6093s | `detyped_files/deltablue/shallow/proportion_sweep/main_k34_s07.py` |  |
| 0.97 | 34/35 | 8 | 2.6350s | 0.0870s | 1 | 8 | yes | 2.5784s | 2.6916s | `detyped_files/deltablue/shallow/proportion_sweep/main_k34_s08.py` |  |
| 0.97 | 34/35 | 9 | 2.6008s | 0.0947s | 1 | 8 | yes | 2.5412s | 2.6629s | `detyped_files/deltablue/shallow/proportion_sweep/main_k34_s09.py` |  |
| 0.97 | 34/35 | 10 | 2.6463s | 0.0816s | 1 | 8 | yes | 2.5937s | 2.6988s | `detyped_files/deltablue/shallow/proportion_sweep/main_k34_s10.py` |  |
| 0.97 | 34/35 | 11 | 2.6405s | 0.1054s | 1 | 8 | yes | 2.5741s | 2.7117s | `detyped_files/deltablue/shallow/proportion_sweep/main_k34_s11.py` |  |
| 0.97 | 34/35 | 12 | 2.5957s | 0.0494s | 1 | 8 | yes | 2.5638s | 2.6279s | `detyped_files/deltablue/shallow/proportion_sweep/main_k34_s12.py` |  |
| 0.97 | 34/35 | 13 | 2.6049s | 0.0746s | 1 | 8 | yes | 2.5579s | 2.6538s | `detyped_files/deltablue/shallow/proportion_sweep/main_k34_s13.py` |  |
| 0.97 | 34/35 | 14 | 2.5174s | 0.1002s | 1 | 8 | yes | 2.4576s | 2.5865s | `detyped_files/deltablue/shallow/proportion_sweep/main_k34_s14.py` |  |
| 0.97 | 34/35 | 15 | 2.2019s | 0.0694s | 1 | 8 | yes | 2.1628s | 2.2511s | `detyped_files/deltablue/shallow/proportion_sweep/main_k34_s15.py` |  |
| 0.97 | 34/35 | 16 | 2.6781s | 0.1440s | 1 | 8 | yes | 2.5916s | 2.7726s | `detyped_files/deltablue/shallow/proportion_sweep/main_k34_s16.py` |  |
| 0.97 | 34/35 | 17 | 2.6197s | 0.0603s | 1 | 8 | yes | 2.5843s | 2.6605s | `detyped_files/deltablue/shallow/proportion_sweep/main_k34_s17.py` |  |
| 0.97 | 34/35 | 18 | 2.6675s | 0.1062s | 1 | 8 | yes | 2.6018s | 2.7394s | `detyped_files/deltablue/shallow/proportion_sweep/main_k34_s18.py` |  |
| 0.97 | 34/35 | 19 | 2.6631s | 0.1166s | 1 | 8 | yes | 2.5883s | 2.7369s | `detyped_files/deltablue/shallow/proportion_sweep/main_k34_s19.py` |  |
| 0.97 | 34/35 | 20 | 2.6088s | 0.1259s | 1 | 8 | yes | 2.5313s | 2.6931s | `detyped_files/deltablue/shallow/proportion_sweep/main_k34_s20.py` |  |
| 1.00 | 35/35 | 1 | 2.6334s | 0.1319s | 1 | 8 | yes | 2.5445s | 2.7132s | `detyped_files/deltablue/shallow/proportion_sweep/main_k35_s01.py` |  |

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
| 0.00 | 0/1 | 1 | 2.0313s | 2.0313s | 2.0313s | 1.0 | yes | ok |
| 1.00 | 1/1 | 1 | 2.3144s | 2.3144s | 2.3144s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/1 | 1 | 2.0313s | 0.0979s | 1 | 8 | yes | 1.9704s | 2.0953s | `detyped_files/fannkuch/advanced/proportion_sweep/main_k00_s01.py` |  |
| 1.00 | 1/1 | 1 | 2.3144s | 0.1166s | 1 | 8 | yes | 2.2457s | 2.3943s | `detyped_files/fannkuch/advanced/proportion_sweep/main_k01_s01.py` |  |

## fannkuch/shallow

- Detypable targets: `1`
- Total runs: `2`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/1 | 1 | 0.8169s | 0.8169s | 0.8169s | 1.0 | yes | ok |
| 1.00 | 1/1 | 1 | 0.8070s | 0.8070s | 0.8070s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/1 | 1 | 0.8169s | 0.0671s | 1 | 8 | yes | 0.7681s | 0.8558s | `detyped_files/fannkuch/shallow/proportion_sweep/main_k00_s01.py` |  |
| 1.00 | 1/1 | 1 | 0.8070s | 0.0604s | 1 | 8 | yes | 0.7651s | 0.8425s | `detyped_files/fannkuch/shallow/proportion_sweep/main_k01_s01.py` |  |

## fannkuch/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.8828s | 0.8828s | 0.8828s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.8828s | 0.0235s | 1 | 8 | yes | 0.8690s | 0.8991s | `static-python-perf/Benchmark/fannkuch/untyped/main.py` |  |

## float/advanced

- Detypable targets: `5`
- Total runs: `32`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/5 | 1 | 0.4817s | 0.4817s | 0.4817s | 1.0 | yes | ok |
| 0.20 | 1/5 | 5 | 0.5416s | 0.4395s | 0.7239s | 1.0 | yes | ok |
| 0.40 | 2/5 | 10 | 0.6360s | 0.4658s | 0.8267s | 1.0 | yes | ok |
| 0.60 | 3/5 | 10 | 0.7287s | 0.4895s | 0.9350s | 1.0 | yes | ok |
| 0.80 | 4/5 | 5 | 0.8211s | 0.5845s | 0.9243s | 1.0 | yes | ok |
| 1.00 | 5/5 | 1 | 0.8842s | 0.8842s | 0.8842s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/5 | 1 | 0.4817s | 0.0268s | 1 | 8 | yes | 0.4629s | 0.4964s | `detyped_files/float/advanced/proportion_sweep/main_k00_s01.py` |  |
| 0.20 | 1/5 | 1 | 0.7239s | 0.0687s | 1 | 8 | yes | 0.6803s | 0.7690s | `detyped_files/float/advanced/proportion_sweep/main_k01_s01.py` |  |
| 0.20 | 1/5 | 2 | 0.4823s | 0.0310s | 1 | 8 | yes | 0.4608s | 0.5017s | `detyped_files/float/advanced/proportion_sweep/main_k01_s02.py` |  |
| 0.20 | 1/5 | 3 | 0.5039s | 0.0564s | 1 | 8 | yes | 0.4672s | 0.5400s | `detyped_files/float/advanced/proportion_sweep/main_k01_s03.py` |  |
| 0.20 | 1/5 | 4 | 0.4395s | 0.0360s | 1 | 8 | yes | 0.4157s | 0.4623s | `detyped_files/float/advanced/proportion_sweep/main_k01_s04.py` |  |
| 0.20 | 1/5 | 5 | 0.5585s | 0.0668s | 1 | 8 | yes | 0.5148s | 0.5998s | `detyped_files/float/advanced/proportion_sweep/main_k01_s05.py` |  |
| 0.40 | 2/5 | 1 | 0.5735s | 0.0759s | 1 | 8 | yes | 0.5268s | 0.6257s | `detyped_files/float/advanced/proportion_sweep/main_k02_s01.py` |  |
| 0.40 | 2/5 | 2 | 0.4842s | 0.0242s | 1 | 8 | yes | 0.4676s | 0.4990s | `detyped_files/float/advanced/proportion_sweep/main_k02_s02.py` |  |
| 0.40 | 2/5 | 3 | 0.7295s | 0.0509s | 1 | 8 | yes | 0.6959s | 0.7615s | `detyped_files/float/advanced/proportion_sweep/main_k02_s03.py` |  |
| 0.40 | 2/5 | 4 | 0.5092s | 0.0437s | 1 | 8 | yes | 0.4839s | 0.5398s | `detyped_files/float/advanced/proportion_sweep/main_k02_s04.py` |  |
| 0.40 | 2/5 | 5 | 0.8093s | 0.0782s | 1 | 8 | yes | 0.7599s | 0.8605s | `detyped_files/float/advanced/proportion_sweep/main_k02_s05.py` |  |
| 0.40 | 2/5 | 6 | 0.6152s | 0.0331s | 1 | 8 | yes | 0.5920s | 0.6345s | `detyped_files/float/advanced/proportion_sweep/main_k02_s06.py` |  |
| 0.40 | 2/5 | 7 | 0.5991s | 0.0230s | 1 | 8 | yes | 0.5848s | 0.6147s | `detyped_files/float/advanced/proportion_sweep/main_k02_s07.py` |  |
| 0.40 | 2/5 | 8 | 0.7474s | 0.0580s | 1 | 8 | yes | 0.7101s | 0.7842s | `detyped_files/float/advanced/proportion_sweep/main_k02_s08.py` |  |
| 0.40 | 2/5 | 9 | 0.8267s | 0.0558s | 1 | 8 | yes | 0.7887s | 0.8600s | `detyped_files/float/advanced/proportion_sweep/main_k02_s09.py` |  |
| 0.40 | 2/5 | 10 | 0.4658s | 0.0229s | 1 | 8 | yes | 0.4504s | 0.4791s | `detyped_files/float/advanced/proportion_sweep/main_k02_s10.py` |  |
| 0.60 | 3/5 | 1 | 0.8045s | 0.0236s | 1 | 8 | yes | 0.7897s | 0.8208s | `detyped_files/float/advanced/proportion_sweep/main_k03_s01.py` |  |
| 0.60 | 3/5 | 2 | 0.7874s | 0.0706s | 1 | 8 | yes | 0.7415s | 0.8320s | `detyped_files/float/advanced/proportion_sweep/main_k03_s02.py` |  |
| 0.60 | 3/5 | 3 | 0.9350s | 0.0697s | 1 | 8 | yes | 0.8858s | 0.9751s | `detyped_files/float/advanced/proportion_sweep/main_k03_s03.py` |  |
| 0.60 | 3/5 | 4 | 0.5830s | 0.0632s | 1 | 8 | yes | 0.5410s | 0.6225s | `detyped_files/float/advanced/proportion_sweep/main_k03_s04.py` |  |
| 0.60 | 3/5 | 5 | 0.8488s | 0.0444s | 1 | 8 | yes | 0.8191s | 0.8765s | `detyped_files/float/advanced/proportion_sweep/main_k03_s05.py` |  |
| 0.60 | 3/5 | 6 | 0.6384s | 0.0383s | 1 | 8 | yes | 0.6165s | 0.6662s | `detyped_files/float/advanced/proportion_sweep/main_k03_s06.py` |  |
| 0.60 | 3/5 | 7 | 0.7667s | 0.0666s | 1 | 8 | yes | 0.7226s | 0.8095s | `detyped_files/float/advanced/proportion_sweep/main_k03_s07.py` |  |
| 0.60 | 3/5 | 8 | 0.8323s | 0.0691s | 1 | 8 | yes | 0.7913s | 0.8812s | `detyped_files/float/advanced/proportion_sweep/main_k03_s08.py` |  |
| 0.60 | 3/5 | 9 | 0.4895s | 0.0380s | 1 | 8 | yes | 0.4623s | 0.5110s | `detyped_files/float/advanced/proportion_sweep/main_k03_s09.py` |  |
| 0.60 | 3/5 | 10 | 0.6015s | 0.0412s | 1 | 8 | yes | 0.5751s | 0.6278s | `detyped_files/float/advanced/proportion_sweep/main_k03_s10.py` |  |
| 0.80 | 4/5 | 1 | 0.9243s | 0.0870s | 1 | 8 | yes | 0.8758s | 0.9868s | `detyped_files/float/advanced/proportion_sweep/main_k04_s01.py` |  |
| 0.80 | 4/5 | 2 | 0.8279s | 0.0782s | 1 | 8 | yes | 0.7771s | 0.8757s | `detyped_files/float/advanced/proportion_sweep/main_k04_s02.py` |  |
| 0.80 | 4/5 | 3 | 0.5845s | 0.0509s | 1 | 8 | yes | 0.5489s | 0.6148s | `detyped_files/float/advanced/proportion_sweep/main_k04_s03.py` |  |
| 0.80 | 4/5 | 4 | 0.9035s | 0.0776s | 1 | 8 | yes | 0.8540s | 0.9534s | `detyped_files/float/advanced/proportion_sweep/main_k04_s04.py` |  |
| 0.80 | 4/5 | 5 | 0.8651s | 0.0496s | 1 | 8 | yes | 0.8340s | 0.8979s | `detyped_files/float/advanced/proportion_sweep/main_k04_s05.py` |  |
| 1.00 | 5/5 | 1 | 0.8842s | 0.0722s | 1 | 8 | yes | 0.8359s | 0.9303s | `detyped_files/float/advanced/proportion_sweep/main_k05_s01.py` |  |

## float/shallow

- Detypable targets: `3`
- Total runs: `8`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/3 | 1 | 0.4747s | 0.4747s | 0.4747s | 1.0 | yes | ok |
| 0.33 | 1/3 | 3 | 0.4909s | 0.4605s | 0.5452s | 1.0 | yes | ok |
| 0.67 | 2/3 | 3 | 0.5354s | 0.4704s | 0.5778s | 1.0 | yes | ok |
| 1.00 | 3/3 | 1 | 0.5736s | 0.5736s | 0.5736s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/3 | 1 | 0.4747s | 0.0316s | 1 | 8 | yes | 0.4535s | 0.4939s | `detyped_files/float/shallow/proportion_sweep/main_k00_s01.py` |  |
| 0.33 | 1/3 | 1 | 0.4670s | 0.0271s | 1 | 8 | yes | 0.4467s | 0.4811s | `detyped_files/float/shallow/proportion_sweep/main_k01_s01.py` |  |
| 0.33 | 1/3 | 2 | 0.5452s | 0.0490s | 1 | 8 | yes | 0.5093s | 0.5730s | `detyped_files/float/shallow/proportion_sweep/main_k01_s02.py` |  |
| 0.33 | 1/3 | 3 | 0.4605s | 0.0432s | 1 | 8 | yes | 0.4323s | 0.4875s | `detyped_files/float/shallow/proportion_sweep/main_k01_s03.py` |  |
| 0.67 | 2/3 | 1 | 0.5778s | 0.0649s | 1 | 8 | yes | 0.5333s | 0.6177s | `detyped_files/float/shallow/proportion_sweep/main_k02_s01.py` |  |
| 0.67 | 2/3 | 2 | 0.4704s | 0.0175s | 1 | 8 | yes | 0.4575s | 0.4795s | `detyped_files/float/shallow/proportion_sweep/main_k02_s02.py` |  |
| 0.67 | 2/3 | 3 | 0.5580s | 0.0787s | 1 | 8 | yes | 0.5128s | 0.6133s | `detyped_files/float/shallow/proportion_sweep/main_k02_s03.py` |  |
| 1.00 | 3/3 | 1 | 0.5736s | 0.0422s | 1 | 8 | yes | 0.5454s | 0.6002s | `detyped_files/float/shallow/proportion_sweep/main_k03_s01.py` |  |

## float/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.4902s | 0.4902s | 0.4902s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.4902s | 0.0374s | 1 | 8 | yes | 0.4670s | 0.5140s | `static-python-perf/Benchmark/float/untyped/main.py` |  |

## nbody/advanced

- Detypable targets: `6`
- Total runs: `64`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 1.5859s | 1.5859s | 1.5859s | 1.0 | yes | ok |
| 0.17 | 1/6 | 6 | 1.9633s | 1.4911s | 4.1303s | 1.0 | yes | ok |
| 0.33 | 2/6 | 15 | 2.3754s | 1.4458s | 4.1484s | 1.0 | yes | ok |
| 0.50 | 3/6 | 20 | 2.7880s | 1.4525s | 4.1764s | 1.1 | yes | ok |
| 0.67 | 4/6 | 15 | 3.2335s | 1.4614s | 4.2180s | 1.0 | yes | ok |
| 0.83 | 5/6 | 6 | 3.6214s | 1.4863s | 4.0980s | 1.0 | yes | ok |
| 1.00 | 6/6 | 1 | 4.0219s | 4.0219s | 4.0219s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 1.5859s | 0.1233s | 1 | 8 | yes | 1.5077s | 1.6681s | `detyped_files/nbody/advanced/proportion_sweep/main_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 1.5688s | 0.0970s | 1 | 8 | yes | 1.5100s | 1.6359s | `detyped_files/nbody/advanced/proportion_sweep/main_k01_s01.py` |  |
| 0.17 | 1/6 | 2 | 1.4911s | 0.0685s | 1 | 8 | yes | 1.4495s | 1.5355s | `detyped_files/nbody/advanced/proportion_sweep/main_k01_s02.py` |  |
| 0.17 | 1/6 | 3 | 4.1303s | 0.1192s | 1 | 8 | yes | 4.0543s | 4.2096s | `detyped_files/nbody/advanced/proportion_sweep/main_k01_s03.py` |  |
| 0.17 | 1/6 | 4 | 1.5238s | 0.0965s | 1 | 8 | yes | 1.4629s | 1.5877s | `detyped_files/nbody/advanced/proportion_sweep/main_k01_s04.py` |  |
| 0.17 | 1/6 | 5 | 1.5335s | 0.0584s | 1 | 8 | yes | 1.4950s | 1.5725s | `detyped_files/nbody/advanced/proportion_sweep/main_k01_s05.py` |  |
| 0.17 | 1/6 | 6 | 1.5324s | 0.0407s | 1 | 8 | yes | 1.5061s | 1.5584s | `detyped_files/nbody/advanced/proportion_sweep/main_k01_s06.py` |  |
| 0.33 | 2/6 | 1 | 1.5833s | 0.1168s | 1 | 8 | yes | 1.5215s | 1.6709s | `detyped_files/nbody/advanced/proportion_sweep/main_k02_s01.py` |  |
| 0.33 | 2/6 | 2 | 1.4752s | 0.0620s | 1 | 8 | yes | 1.4360s | 1.5151s | `detyped_files/nbody/advanced/proportion_sweep/main_k02_s02.py` |  |
| 0.33 | 2/6 | 3 | 1.5554s | 0.1900s | 1 | 8 | yes | 1.4603s | 1.6930s | `detyped_files/nbody/advanced/proportion_sweep/main_k02_s03.py` |  |
| 0.33 | 2/6 | 4 | 4.1484s | 0.1289s | 1 | 8 | yes | 4.0698s | 4.2350s | `detyped_files/nbody/advanced/proportion_sweep/main_k02_s04.py` |  |
| 0.33 | 2/6 | 5 | 1.4926s | 0.0705s | 1 | 8 | yes | 1.4497s | 1.5416s | `detyped_files/nbody/advanced/proportion_sweep/main_k02_s05.py` |  |
| 0.33 | 2/6 | 6 | 4.0587s | 0.0793s | 1 | 8 | yes | 4.0132s | 4.1147s | `detyped_files/nbody/advanced/proportion_sweep/main_k02_s06.py` |  |
| 0.33 | 2/6 | 7 | 1.4989s | 0.1000s | 1 | 8 | yes | 1.4400s | 1.5660s | `detyped_files/nbody/advanced/proportion_sweep/main_k02_s07.py` |  |
| 0.33 | 2/6 | 8 | 4.1426s | 0.1228s | 1 | 8 | yes | 4.0615s | 4.2166s | `detyped_files/nbody/advanced/proportion_sweep/main_k02_s08.py` |  |
| 0.33 | 2/6 | 9 | 1.5167s | 0.0809s | 1 | 8 | yes | 1.4749s | 1.5757s | `detyped_files/nbody/advanced/proportion_sweep/main_k02_s09.py` |  |
| 0.33 | 2/6 | 10 | 1.5116s | 0.0909s | 1 | 8 | yes | 1.4604s | 1.5754s | `detyped_files/nbody/advanced/proportion_sweep/main_k02_s10.py` |  |
| 0.33 | 2/6 | 11 | 1.5310s | 0.0718s | 1 | 8 | yes | 1.4819s | 1.5752s | `detyped_files/nbody/advanced/proportion_sweep/main_k02_s11.py` |  |
| 0.33 | 2/6 | 12 | 1.4458s | 0.1033s | 1 | 8 | yes | 1.3862s | 1.5200s | `detyped_files/nbody/advanced/proportion_sweep/main_k02_s12.py` |  |
| 0.33 | 2/6 | 13 | 4.0966s | 0.1407s | 1 | 8 | yes | 4.0088s | 4.1887s | `detyped_files/nbody/advanced/proportion_sweep/main_k02_s13.py` |  |
| 0.33 | 2/6 | 14 | 4.0520s | 0.0601s | 1 | 8 | yes | 4.0103s | 4.0883s | `detyped_files/nbody/advanced/proportion_sweep/main_k02_s14.py` |  |
| 0.33 | 2/6 | 15 | 1.5217s | 0.1417s | 1 | 8 | yes | 1.4363s | 1.6221s | `detyped_files/nbody/advanced/proportion_sweep/main_k02_s15.py` |  |
| 0.50 | 3/6 | 1 | 1.4591s | 0.0825s | 1 | 8 | yes | 1.4059s | 1.5129s | `detyped_files/nbody/advanced/proportion_sweep/main_k03_s01.py` |  |
| 0.50 | 3/6 | 2 | 4.0726s | 0.1365s | 1 | 8 | yes | 3.9894s | 4.1648s | `detyped_files/nbody/advanced/proportion_sweep/main_k03_s02.py` |  |
| 0.50 | 3/6 | 3 | 1.4525s | 0.1544s | 2 | 16 | yes | 1.3917s | 1.5348s | `detyped_files/nbody/advanced/proportion_sweep/main_k03_s03.py` |  |
| 0.50 | 3/6 | 4 | 1.5164s | 0.0553s | 1 | 8 | yes | 1.4804s | 1.5512s | `detyped_files/nbody/advanced/proportion_sweep/main_k03_s04.py` |  |
| 0.50 | 3/6 | 5 | 1.4848s | 0.1060s | 1 | 8 | yes | 1.4162s | 1.5531s | `detyped_files/nbody/advanced/proportion_sweep/main_k03_s05.py` |  |
| 0.50 | 3/6 | 6 | 4.1413s | 0.0602s | 1 | 8 | yes | 4.1018s | 4.1787s | `detyped_files/nbody/advanced/proportion_sweep/main_k03_s06.py` |  |
| 0.50 | 3/6 | 7 | 4.0813s | 0.1258s | 1 | 8 | yes | 4.0049s | 4.1668s | `detyped_files/nbody/advanced/proportion_sweep/main_k03_s07.py` |  |
| 0.50 | 3/6 | 8 | 4.1123s | 0.1876s | 1 | 8 | yes | 3.9969s | 4.2411s | `detyped_files/nbody/advanced/proportion_sweep/main_k03_s08.py` |  |
| 0.50 | 3/6 | 9 | 1.4754s | 0.0985s | 1 | 8 | yes | 1.4135s | 1.5422s | `detyped_files/nbody/advanced/proportion_sweep/main_k03_s09.py` |  |
| 0.50 | 3/6 | 10 | 1.4935s | 0.0719s | 1 | 8 | yes | 1.4452s | 1.5391s | `detyped_files/nbody/advanced/proportion_sweep/main_k03_s10.py` |  |
| 0.50 | 3/6 | 11 | 4.1764s | 0.1361s | 1 | 8 | yes | 4.0902s | 4.2635s | `detyped_files/nbody/advanced/proportion_sweep/main_k03_s11.py` |  |
| 0.50 | 3/6 | 12 | 4.1272s | 0.1057s | 1 | 8 | yes | 4.0579s | 4.1924s | `detyped_files/nbody/advanced/proportion_sweep/main_k03_s12.py` |  |
| 0.50 | 3/6 | 13 | 1.5066s | 0.0577s | 1 | 8 | yes | 1.4726s | 1.5470s | `detyped_files/nbody/advanced/proportion_sweep/main_k03_s13.py` |  |
| 0.50 | 3/6 | 14 | 4.0282s | 0.1236s | 1 | 8 | yes | 3.9496s | 4.1108s | `detyped_files/nbody/advanced/proportion_sweep/main_k03_s14.py` |  |
| 0.50 | 3/6 | 15 | 1.4818s | 0.0461s | 1 | 8 | yes | 1.4508s | 1.5105s | `detyped_files/nbody/advanced/proportion_sweep/main_k03_s15.py` |  |
| 0.50 | 3/6 | 16 | 4.0637s | 0.1263s | 1 | 8 | yes | 3.9857s | 4.1474s | `detyped_files/nbody/advanced/proportion_sweep/main_k03_s16.py` |  |
| 0.50 | 3/6 | 17 | 1.5065s | 0.0783s | 1 | 8 | yes | 1.4551s | 1.5566s | `detyped_files/nbody/advanced/proportion_sweep/main_k03_s17.py` |  |
| 0.50 | 3/6 | 18 | 4.0788s | 0.1053s | 1 | 8 | yes | 4.0076s | 4.1414s | `detyped_files/nbody/advanced/proportion_sweep/main_k03_s18.py` |  |
| 0.50 | 3/6 | 19 | 1.4794s | 0.1128s | 1 | 8 | yes | 1.4075s | 1.5527s | `detyped_files/nbody/advanced/proportion_sweep/main_k03_s19.py` |  |
| 0.50 | 3/6 | 20 | 4.0226s | 0.1508s | 1 | 8 | yes | 3.9322s | 4.1267s | `detyped_files/nbody/advanced/proportion_sweep/main_k03_s20.py` |  |
| 0.67 | 4/6 | 1 | 1.4968s | 0.0771s | 1 | 8 | yes | 1.4510s | 1.5495s | `detyped_files/nbody/advanced/proportion_sweep/main_k04_s01.py` |  |
| 0.67 | 4/6 | 2 | 1.4987s | 0.0653s | 1 | 8 | yes | 1.4588s | 1.5437s | `detyped_files/nbody/advanced/proportion_sweep/main_k04_s02.py` |  |
| 0.67 | 4/6 | 3 | 4.2180s | 0.2232s | 1 | 8 | yes | 4.0778s | 4.3632s | `detyped_files/nbody/advanced/proportion_sweep/main_k04_s03.py` |  |
| 0.67 | 4/6 | 4 | 1.4933s | 0.0649s | 1 | 8 | yes | 1.4466s | 1.5281s | `detyped_files/nbody/advanced/proportion_sweep/main_k04_s04.py` |  |
| 0.67 | 4/6 | 5 | 4.0860s | 0.1058s | 1 | 8 | yes | 4.0149s | 4.1531s | `detyped_files/nbody/advanced/proportion_sweep/main_k04_s05.py` |  |
| 0.67 | 4/6 | 6 | 1.4614s | 0.0726s | 1 | 8 | yes | 1.4146s | 1.5078s | `detyped_files/nbody/advanced/proportion_sweep/main_k04_s06.py` |  |
| 0.67 | 4/6 | 7 | 4.0428s | 0.0845s | 1 | 8 | yes | 3.9884s | 4.0974s | `detyped_files/nbody/advanced/proportion_sweep/main_k04_s07.py` |  |
| 0.67 | 4/6 | 8 | 1.5878s | 0.1524s | 1 | 8 | yes | 1.4937s | 1.6888s | `detyped_files/nbody/advanced/proportion_sweep/main_k04_s08.py` |  |
| 0.67 | 4/6 | 9 | 4.1043s | 0.0990s | 1 | 8 | yes | 4.0399s | 4.1657s | `detyped_files/nbody/advanced/proportion_sweep/main_k04_s09.py` |  |
| 0.67 | 4/6 | 10 | 4.1889s | 0.2291s | 1 | 8 | yes | 4.0670s | 4.3530s | `detyped_files/nbody/advanced/proportion_sweep/main_k04_s10.py` |  |
| 0.67 | 4/6 | 11 | 4.1146s | 0.1591s | 1 | 8 | yes | 4.0117s | 4.2179s | `detyped_files/nbody/advanced/proportion_sweep/main_k04_s11.py` |  |
| 0.67 | 4/6 | 12 | 4.0149s | 0.0984s | 1 | 8 | yes | 3.9562s | 4.0812s | `detyped_files/nbody/advanced/proportion_sweep/main_k04_s12.py` |  |
| 0.67 | 4/6 | 13 | 4.0256s | 0.1507s | 1 | 8 | yes | 3.9289s | 4.1216s | `detyped_files/nbody/advanced/proportion_sweep/main_k04_s13.py` |  |
| 0.67 | 4/6 | 14 | 4.0449s | 0.1180s | 1 | 8 | yes | 3.9811s | 4.1314s | `detyped_files/nbody/advanced/proportion_sweep/main_k04_s14.py` |  |
| 0.67 | 4/6 | 15 | 4.1246s | 0.1292s | 1 | 8 | yes | 4.0508s | 4.2166s | `detyped_files/nbody/advanced/proportion_sweep/main_k04_s15.py` |  |
| 0.83 | 5/6 | 1 | 1.4863s | 0.0879s | 1 | 8 | yes | 1.4354s | 1.5490s | `detyped_files/nbody/advanced/proportion_sweep/main_k05_s01.py` |  |
| 0.83 | 5/6 | 2 | 4.0980s | 0.1803s | 1 | 8 | yes | 3.9967s | 4.2270s | `detyped_files/nbody/advanced/proportion_sweep/main_k05_s02.py` |  |
| 0.83 | 5/6 | 3 | 4.0686s | 0.2112s | 1 | 8 | yes | 3.9514s | 4.2205s | `detyped_files/nbody/advanced/proportion_sweep/main_k05_s03.py` |  |
| 0.83 | 5/6 | 4 | 4.0357s | 0.1310s | 1 | 8 | yes | 3.9518s | 4.1213s | `detyped_files/nbody/advanced/proportion_sweep/main_k05_s04.py` |  |
| 0.83 | 5/6 | 5 | 4.0010s | 0.1026s | 1 | 8 | yes | 3.9306s | 4.0641s | `detyped_files/nbody/advanced/proportion_sweep/main_k05_s05.py` |  |
| 0.83 | 5/6 | 6 | 4.0387s | 0.1155s | 1 | 8 | yes | 3.9647s | 4.1122s | `detyped_files/nbody/advanced/proportion_sweep/main_k05_s06.py` |  |
| 1.00 | 6/6 | 1 | 4.0219s | 0.1096s | 1 | 8 | yes | 3.9528s | 4.0934s | `detyped_files/nbody/advanced/proportion_sweep/main_k06_s01.py` |  |

## nbody/shallow

- Detypable targets: `6`
- Total runs: `64`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.9873s | 0.9873s | 0.9873s | 1.0 | yes | ok |
| 0.17 | 1/6 | 6 | 1.0034s | 0.9942s | 1.0215s | 1.0 | yes | 1 failed |
| 0.33 | 2/6 | 15 | 1.0138s | 0.9892s | 1.0512s | 1.0 | yes | 5 failed |
| 0.50 | 3/6 | 20 | 1.0312s | 0.9710s | 1.1057s | 1.0 | yes | 10 failed |
| 0.67 | 4/6 | 15 | 1.0200s | 0.9805s | 1.0483s | 1.0 | yes | 10 failed |
| 0.83 | 5/6 | 6 | 0.9842s | 0.9842s | 0.9842s | 1.0 | yes | 5 failed |
| 1.00 | 6/6 | 1 | - | - | - | - | - | 1 failed |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.9873s | 0.0711s | 1 | 8 | yes | 0.9363s | 1.0297s | `detyped_files/nbody/shallow/proportion_sweep/main_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k01_s01.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k01_s01.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_k01_s01.py", line 72
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.17 | 1/6 | 2 | 1.0031s | 0.0588s | 1 | 8 | yes | 0.9635s | 1.0383s | `detyped_files/nbody/shallow/proportion_sweep/main_k01_s02.py` |  |
| 0.17 | 1/6 | 3 | 1.0008s | 0.0556s | 1 | 8 | yes | 0.9603s | 1.0305s | `detyped_files/nbody/shallow/proportion_sweep/main_k01_s03.py` |  |
| 0.17 | 1/6 | 4 | 1.0215s | 0.0422s | 1 | 8 | yes | 0.9974s | 1.0518s | `detyped_files/nbody/shallow/proportion_sweep/main_k01_s04.py` |  |
| 0.17 | 1/6 | 5 | 0.9942s | 0.0679s | 1 | 8 | yes | 0.9490s | 1.0360s | `detyped_files/nbody/shallow/proportion_sweep/main_k01_s05.py` |  |
| 0.17 | 1/6 | 6 | 0.9976s | 0.0456s | 1 | 8 | yes | 0.9685s | 1.0267s | `detyped_files/nbody/shallow/proportion_sweep/main_k01_s06.py` |  |
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_k02_s01.py", line 74
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.33 | 2/6 | 2 | 0.9892s | 0.0607s | 1 | 8 | yes | 0.9473s | 1.0258s | `detyped_files/nbody/shallow/proportion_sweep/main_k02_s02.py` |  |
| 0.33 | 2/6 | 3 | 1.0130s | 0.0377s | 1 | 8 | yes | 0.9862s | 1.0349s | `detyped_files/nbody/shallow/proportion_sweep/main_k02_s03.py` |  |
| 0.33 | 2/6 | 4 | 1.0279s | 0.1052s | 1 | 8 | yes | 0.9636s | 1.1004s | `detyped_files/nbody/shallow/proportion_sweep/main_k02_s04.py` |  |
| 0.33 | 2/6 | 5 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k02_s05.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k02_s05.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_k02_s05.py", line 74
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.33 | 2/6 | 6 | 1.0029s | 0.0835s | 1 | 8 | yes | 0.9485s | 1.0564s | `detyped_files/nbody/shallow/proportion_sweep/main_k02_s06.py` |  |
| 0.33 | 2/6 | 7 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k02_s07.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k02_s07.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_k02_s07.py", line 73
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.33 | 2/6 | 8 | 1.0245s | 0.0932s | 1 | 8 | yes | 0.9643s | 1.0848s | `detyped_files/nbody/shallow/proportion_sweep/main_k02_s08.py` |  |
| 0.33 | 2/6 | 9 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k02_s09.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k02_s09.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_k02_s09.py", line 72
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.33 | 2/6 | 10 | 1.0512s | 0.1026s | 1 | 8 | yes | 0.9900s | 1.1242s | `detyped_files/nbody/shallow/proportion_sweep/main_k02_s10.py` |  |
| 0.33 | 2/6 | 11 | 1.0089s | 0.0733s | 1 | 8 | yes | 0.9644s | 1.0582s | `detyped_files/nbody/shallow/proportion_sweep/main_k02_s11.py` |  |
| 0.33 | 2/6 | 12 | 1.0095s | 0.0845s | 1 | 8 | yes | 0.9530s | 1.0648s | `detyped_files/nbody/shallow/proportion_sweep/main_k02_s12.py` |  |
| 0.33 | 2/6 | 13 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k02_s13.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k02_s13.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_k02_s13.py", line 72
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.33 | 2/6 | 14 | 1.0161s | 0.0557s | 1 | 8 | yes | 0.9802s | 1.0528s | `detyped_files/nbody/shallow/proportion_sweep/main_k02_s14.py` |  |
| 0.33 | 2/6 | 15 | 0.9953s | 0.0852s | 1 | 8 | yes | 0.9418s | 1.0503s | `detyped_files/nbody/shallow/proportion_sweep/main_k02_s15.py` |  |
| 0.50 | 3/6 | 1 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k03_s01.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k03_s01.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_k03_s01.py", line 74
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.50 | 3/6 | 2 | 1.0280s | 0.0497s | 1 | 8 | yes | 0.9963s | 1.0617s | `detyped_files/nbody/shallow/proportion_sweep/main_k03_s02.py` |  |
| 0.50 | 3/6 | 3 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k03_s03.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k03_s03.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_k03_s03.py", line 76
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.50 | 3/6 | 4 | 1.0189s | 0.0203s | 1 | 8 | yes | 1.0057s | 1.0316s | `detyped_files/nbody/shallow/proportion_sweep/main_k03_s04.py` |  |
| 0.50 | 3/6 | 5 | 1.0399s | 0.0877s | 1 | 8 | yes | 0.9841s | 1.0987s | `detyped_files/nbody/shallow/proportion_sweep/main_k03_s05.py` |  |
| 0.50 | 3/6 | 6 | 1.0374s | 0.0748s | 1 | 8 | yes | 0.9943s | 1.0911s | `detyped_files/nbody/shallow/proportion_sweep/main_k03_s06.py` |  |
| 0.50 | 3/6 | 7 | 0.9958s | 0.1063s | 1 | 8 | yes | 0.9354s | 1.0702s | `detyped_files/nbody/shallow/proportion_sweep/main_k03_s07.py` |  |
| 0.50 | 3/6 | 8 | 0.9710s | 0.0733s | 1 | 8 | yes | 0.9293s | 1.0233s | `detyped_files/nbody/shallow/proportion_sweep/main_k03_s08.py` |  |
| 0.50 | 3/6 | 9 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k03_s09.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k03_s09.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_k03_s09.py", line 75
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.50 | 3/6 | 10 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k03_s10.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k03_s10.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_k03_s10.py", line 73
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.50 | 3/6 | 11 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k03_s11.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k03_s11.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_k03_s11.py", line 75
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.50 | 3/6 | 12 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k03_s12.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k03_s12.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_k03_s12.py", line 74
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.50 | 3/6 | 13 | 1.0026s | 0.0709s | 1 | 8 | yes | 0.9541s | 1.0473s | `detyped_files/nbody/shallow/proportion_sweep/main_k03_s13.py` |  |
| 0.50 | 3/6 | 14 | 1.0361s | 0.0457s | 1 | 8 | yes | 1.0063s | 1.0647s | `detyped_files/nbody/shallow/proportion_sweep/main_k03_s14.py` |  |
| 0.50 | 3/6 | 15 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k03_s15.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k03_s15.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_k03_s15.py", line 74
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.50 | 3/6 | 16 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k03_s16.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k03_s16.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_k03_s16.py", line 74
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.50 | 3/6 | 17 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k03_s17.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k03_s17.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_k03_s17.py", line 72
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.50 | 3/6 | 18 | 1.0770s | 0.0887s | 1 | 8 | yes | 1.0249s | 1.1371s | `detyped_files/nbody/shallow/proportion_sweep/main_k03_s18.py` |  |
| 0.50 | 3/6 | 19 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k03_s19.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k03_s19.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_k03_s19.py", line 73
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.50 | 3/6 | 20 | 1.1057s | 0.0964s | 1 | 8 | yes | 1.0514s | 1.1728s | `detyped_files/nbody/shallow/proportion_sweep/main_k03_s20.py` |  |
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_k04_s01.py", line 76
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.67 | 4/6 | 2 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k04_s02.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k04_s02.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_k04_s02.py", line 75
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.67 | 4/6 | 3 | 0.9805s | 0.0992s | 1 | 8 | yes | 0.9224s | 1.0476s | `detyped_files/nbody/shallow/proportion_sweep/main_k04_s03.py` |  |
| 0.67 | 4/6 | 4 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k04_s04.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k04_s04.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_k04_s04.py", line 73
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.67 | 4/6 | 5 | 1.0028s | 0.0525s | 1 | 8 | yes | 0.9655s | 1.0327s | `detyped_files/nbody/shallow/proportion_sweep/main_k04_s05.py` |  |
| 0.67 | 4/6 | 6 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k04_s06.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k04_s06.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_k04_s06.py", line 77
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.67 | 4/6 | 7 | 1.0317s | 0.0721s | 1 | 8 | yes | 0.9851s | 1.0777s | `detyped_files/nbody/shallow/proportion_sweep/main_k04_s07.py` |  |
| 0.67 | 4/6 | 8 | 1.0483s | 0.0985s | 1 | 8 | yes | 0.9872s | 1.1142s | `detyped_files/nbody/shallow/proportion_sweep/main_k04_s08.py` |  |
| 0.67 | 4/6 | 9 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k04_s09.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k04_s09.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_k04_s09.py", line 74
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.67 | 4/6 | 10 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k04_s10.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k04_s10.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_k04_s10.py", line 75
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.67 | 4/6 | 11 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k04_s11.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k04_s11.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_k04_s11.py", line 74
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.67 | 4/6 | 12 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k04_s12.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k04_s12.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_k04_s12.py", line 75
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.67 | 4/6 | 13 | 1.0369s | 0.0956s | 1 | 8 | yes | 0.9768s | 1.0988s | `detyped_files/nbody/shallow/proportion_sweep/main_k04_s13.py` |  |
| 0.67 | 4/6 | 14 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k04_s14.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k04_s14.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_k04_s14.py", line 75
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.67 | 4/6 | 15 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k04_s15.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k04_s15.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_k04_s15.py", line 76
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_k05_s01.py", line 76
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_k05_s02.py", line 77
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.83 | 5/6 | 3 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k05_s03.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k05_s03.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_k05_s03.py", line 75
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.83 | 5/6 | 4 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k05_s04.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k05_s04.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_k05_s04.py", line 75
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.83 | 5/6 | 5 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_k05_s05.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_k05_s05.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_k05_s05.py", line 77
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.83 | 5/6 | 6 | 0.9842s | 0.0481s | 1 | 8 | yes | 0.9535s | 1.0153s | `detyped_files/nbody/shallow/proportion_sweep/main_k05_s06.py` |  |
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
| 0.00 | 0/0 | 1 | 1.0549s | 1.0549s | 1.0549s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 1.0549s | 0.0579s | 1 | 8 | yes | 1.0208s | 1.0963s | `static-python-perf/Benchmark/nbody/untyped/main.py` |  |

## nqueens/advanced

- Detypable targets: `5`
- Total runs: `32`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/5 | 1 | 0.2149s | 0.2149s | 0.2149s | 1.0 | yes | ok |
| 0.20 | 1/5 | 5 | 0.2237s | 0.2134s | 0.2456s | 1.0 | yes | ok |
| 0.40 | 2/5 | 10 | 0.2327s | 0.2160s | 0.2611s | 1.2 | yes | ok |
| 0.60 | 3/5 | 10 | 0.2442s | 0.2184s | 0.2678s | 1.0 | yes | ok |
| 0.80 | 4/5 | 5 | 0.2518s | 0.2394s | 0.2651s | 1.2 | yes | ok |
| 1.00 | 5/5 | 1 | 0.2662s | 0.2662s | 0.2662s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/5 | 1 | 0.2149s | 0.0172s | 1 | 8 | yes | 0.2036s | 0.2259s | `detyped_files/nqueens/advanced/proportion_sweep/main_k00_s01.py` |  |
| 0.20 | 1/5 | 1 | 0.2456s | 0.0083s | 1 | 8 | yes | 0.2405s | 0.2511s | `detyped_files/nqueens/advanced/proportion_sweep/main_k01_s01.py` |  |
| 0.20 | 1/5 | 2 | 0.2143s | 0.0298s | 1 | 8 | yes | 0.1955s | 0.2336s | `detyped_files/nqueens/advanced/proportion_sweep/main_k01_s02.py` |  |
| 0.20 | 1/5 | 3 | 0.2134s | 0.0057s | 1 | 8 | yes | 0.2094s | 0.2167s | `detyped_files/nqueens/advanced/proportion_sweep/main_k01_s03.py` |  |
| 0.20 | 1/5 | 4 | 0.2257s | 0.0220s | 1 | 8 | yes | 0.2148s | 0.2415s | `detyped_files/nqueens/advanced/proportion_sweep/main_k01_s04.py` |  |
| 0.20 | 1/5 | 5 | 0.2196s | 0.0137s | 1 | 8 | yes | 0.2101s | 0.2280s | `detyped_files/nqueens/advanced/proportion_sweep/main_k01_s05.py` |  |
| 0.40 | 2/5 | 1 | 0.2234s | 0.0200s | 1 | 8 | yes | 0.2107s | 0.2360s | `detyped_files/nqueens/advanced/proportion_sweep/main_k02_s01.py` |  |
| 0.40 | 2/5 | 2 | 0.2237s | 0.0219s | 1 | 8 | yes | 0.2087s | 0.2367s | `detyped_files/nqueens/advanced/proportion_sweep/main_k02_s02.py` |  |
| 0.40 | 2/5 | 3 | 0.2366s | 0.0159s | 1 | 8 | yes | 0.2253s | 0.2460s | `detyped_files/nqueens/advanced/proportion_sweep/main_k02_s03.py` |  |
| 0.40 | 2/5 | 4 | 0.2483s | 0.0301s | 2 | 16 | yes | 0.2356s | 0.2637s | `detyped_files/nqueens/advanced/proportion_sweep/main_k02_s04.py` |  |
| 0.40 | 2/5 | 5 | 0.2498s | 0.0247s | 1 | 8 | yes | 0.2363s | 0.2678s | `detyped_files/nqueens/advanced/proportion_sweep/main_k02_s05.py` |  |
| 0.40 | 2/5 | 6 | 0.2184s | 0.0253s | 1 | 8 | yes | 0.2016s | 0.2343s | `detyped_files/nqueens/advanced/proportion_sweep/main_k02_s06.py` |  |
| 0.40 | 2/5 | 7 | 0.2611s | 0.0336s | 2 | 16 | yes | 0.2458s | 0.2778s | `detyped_files/nqueens/advanced/proportion_sweep/main_k02_s07.py` |  |
| 0.40 | 2/5 | 8 | 0.2160s | 0.0088s | 1 | 8 | yes | 0.2103s | 0.2217s | `detyped_files/nqueens/advanced/proportion_sweep/main_k02_s08.py` |  |
| 0.40 | 2/5 | 9 | 0.2272s | 0.0108s | 1 | 8 | yes | 0.2210s | 0.2346s | `detyped_files/nqueens/advanced/proportion_sweep/main_k02_s09.py` |  |
| 0.40 | 2/5 | 10 | 0.2225s | 0.0150s | 1 | 8 | yes | 0.2126s | 0.2323s | `detyped_files/nqueens/advanced/proportion_sweep/main_k02_s10.py` |  |
| 0.60 | 3/5 | 1 | 0.2678s | 0.0327s | 1 | 8 | yes | 0.2515s | 0.2916s | `detyped_files/nqueens/advanced/proportion_sweep/main_k03_s01.py` |  |
| 0.60 | 3/5 | 2 | 0.2580s | 0.0165s | 1 | 8 | yes | 0.2474s | 0.2682s | `detyped_files/nqueens/advanced/proportion_sweep/main_k03_s02.py` |  |
| 0.60 | 3/5 | 3 | 0.2570s | 0.0362s | 1 | 8 | yes | 0.2350s | 0.2823s | `detyped_files/nqueens/advanced/proportion_sweep/main_k03_s03.py` |  |
| 0.60 | 3/5 | 4 | 0.2528s | 0.0160s | 1 | 8 | yes | 0.2429s | 0.2634s | `detyped_files/nqueens/advanced/proportion_sweep/main_k03_s04.py` |  |
| 0.60 | 3/5 | 5 | 0.2228s | 0.0141s | 1 | 8 | yes | 0.2148s | 0.2328s | `detyped_files/nqueens/advanced/proportion_sweep/main_k03_s05.py` |  |
| 0.60 | 3/5 | 6 | 0.2184s | 0.0107s | 1 | 8 | yes | 0.2106s | 0.2236s | `detyped_files/nqueens/advanced/proportion_sweep/main_k03_s06.py` |  |
| 0.60 | 3/5 | 7 | 0.2464s | 0.0043s | 1 | 8 | yes | 0.2437s | 0.2491s | `detyped_files/nqueens/advanced/proportion_sweep/main_k03_s07.py` |  |
| 0.60 | 3/5 | 8 | 0.2296s | 0.0242s | 1 | 8 | yes | 0.2135s | 0.2452s | `detyped_files/nqueens/advanced/proportion_sweep/main_k03_s08.py` |  |
| 0.60 | 3/5 | 9 | 0.2448s | 0.0223s | 1 | 8 | yes | 0.2301s | 0.2590s | `detyped_files/nqueens/advanced/proportion_sweep/main_k03_s09.py` |  |
| 0.60 | 3/5 | 10 | 0.2446s | 0.0201s | 1 | 8 | yes | 0.2316s | 0.2579s | `detyped_files/nqueens/advanced/proportion_sweep/main_k03_s10.py` |  |
| 0.80 | 4/5 | 1 | 0.2651s | 0.0227s | 1 | 8 | yes | 0.2513s | 0.2801s | `detyped_files/nqueens/advanced/proportion_sweep/main_k04_s01.py` |  |
| 0.80 | 4/5 | 2 | 0.2520s | 0.0333s | 2 | 16 | yes | 0.2388s | 0.2696s | `detyped_files/nqueens/advanced/proportion_sweep/main_k04_s02.py` |  |
| 0.80 | 4/5 | 3 | 0.2410s | 0.0151s | 1 | 8 | yes | 0.2304s | 0.2501s | `detyped_files/nqueens/advanced/proportion_sweep/main_k04_s03.py` |  |
| 0.80 | 4/5 | 4 | 0.2616s | 0.0215s | 1 | 8 | yes | 0.2500s | 0.2770s | `detyped_files/nqueens/advanced/proportion_sweep/main_k04_s04.py` |  |
| 0.80 | 4/5 | 5 | 0.2394s | 0.0184s | 1 | 8 | yes | 0.2293s | 0.2527s | `detyped_files/nqueens/advanced/proportion_sweep/main_k04_s05.py` |  |
| 1.00 | 5/5 | 1 | 0.2662s | 0.0100s | 1 | 8 | yes | 0.2596s | 0.2724s | `detyped_files/nqueens/advanced/proportion_sweep/main_k05_s01.py` |  |

## nqueens/shallow

- Detypable targets: `3`
- Total runs: `8`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/3 | 1 | 0.2272s | 0.2272s | 0.2272s | 1.0 | yes | ok |
| 0.33 | 1/3 | 3 | 0.2344s | 0.2323s | 0.2370s | 1.3 | yes | ok |
| 0.67 | 2/3 | 3 | 0.2350s | 0.2283s | 0.2420s | 1.0 | yes | ok |
| 1.00 | 3/3 | 1 | 0.2351s | 0.2351s | 0.2351s | 2.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/3 | 1 | 0.2272s | 0.0036s | 1 | 8 | yes | 0.2247s | 0.2294s | `detyped_files/nqueens/shallow/proportion_sweep/main_k00_s01.py` |  |
| 0.33 | 1/3 | 1 | 0.2341s | 0.0255s | 1 | 8 | yes | 0.2195s | 0.2523s | `detyped_files/nqueens/shallow/proportion_sweep/main_k01_s01.py` |  |
| 0.33 | 1/3 | 2 | 0.2370s | 0.0315s | 2 | 16 | yes | 0.2250s | 0.2540s | `detyped_files/nqueens/shallow/proportion_sweep/main_k01_s02.py` |  |
| 0.33 | 1/3 | 3 | 0.2323s | 0.0123s | 1 | 8 | yes | 0.2251s | 0.2410s | `detyped_files/nqueens/shallow/proportion_sweep/main_k01_s03.py` |  |
| 0.67 | 2/3 | 1 | 0.2283s | 0.0279s | 1 | 8 | yes | 0.2094s | 0.2463s | `detyped_files/nqueens/shallow/proportion_sweep/main_k02_s01.py` |  |
| 0.67 | 2/3 | 2 | 0.2420s | 0.0196s | 1 | 8 | yes | 0.2306s | 0.2555s | `detyped_files/nqueens/shallow/proportion_sweep/main_k02_s02.py` |  |
| 0.67 | 2/3 | 3 | 0.2348s | 0.0212s | 1 | 8 | yes | 0.2209s | 0.2481s | `detyped_files/nqueens/shallow/proportion_sweep/main_k02_s03.py` |  |
| 1.00 | 3/3 | 1 | 0.2351s | 0.0273s | 2 | 16 | yes | 0.2238s | 0.2498s | `detyped_files/nqueens/shallow/proportion_sweep/main_k03_s01.py` |  |

## nqueens/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.2516s | 0.2516s | 0.2516s | 2.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.2516s | 0.0319s | 2 | 16 | yes | 0.2388s | 0.2687s | `static-python-perf/Benchmark/nqueens/untyped/main.py` |  |

## pystone/advanced

- Detypable targets: `15`
- Total runs: `272`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/15 | 1 | 0.6725s | 0.6725s | 0.6725s | 1.0 | yes | ok |
| 0.07 | 1/15 | 15 | 0.7700s | 0.6705s | 1.5331s | 1.0 | yes | ok |
| 0.13 | 2/15 | 20 | 0.8020s | 0.6369s | 1.5132s | 1.0 | yes | ok |
| 0.20 | 3/15 | 20 | 0.9019s | 0.6372s | 1.6103s | 1.0 | yes | ok |
| 0.27 | 4/15 | 20 | 0.8174s | 0.6423s | 1.5123s | 1.0 | yes | ok |
| 0.33 | 5/15 | 20 | 1.2739s | 0.6795s | 1.9597s | 1.0 | yes | ok |
| 0.40 | 6/15 | 20 | 1.0866s | 0.6489s | 1.8658s | 1.1 | yes | ok |
| 0.47 | 7/15 | 20 | 1.1814s | 0.6466s | 1.9085s | 1.0 | yes | ok |
| 0.53 | 8/15 | 20 | 1.3972s | 0.6730s | 1.9450s | 1.0 | yes | ok |
| 0.60 | 9/15 | 20 | 1.4597s | 0.6804s | 1.9339s | 1.0 | yes | ok |
| 0.67 | 10/15 | 20 | 1.4228s | 0.6644s | 1.9653s | 1.0 | yes | ok |
| 0.73 | 11/15 | 20 | 1.5372s | 0.8347s | 2.0036s | 1.0 | yes | ok |
| 0.80 | 12/15 | 20 | 1.6966s | 1.0680s | 1.9761s | 1.0 | yes | ok |
| 0.87 | 13/15 | 20 | 1.7149s | 0.9397s | 1.9869s | 1.0 | yes | ok |
| 0.93 | 14/15 | 15 | 1.8391s | 1.1134s | 1.9659s | 1.0 | yes | ok |
| 1.00 | 15/15 | 1 | 1.9370s | 1.9370s | 1.9370s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/15 | 1 | 0.6725s | 0.0700s | 1 | 8 | yes | 0.6259s | 0.7164s | `detyped_files/pystone/advanced/proportion_sweep/main_k00_s01.py` |  |
| 0.07 | 1/15 | 1 | 0.6821s | 0.0724s | 1 | 8 | yes | 0.6344s | 0.7259s | `detyped_files/pystone/advanced/proportion_sweep/main_k01_s01.py` |  |
| 0.07 | 1/15 | 2 | 0.6858s | 0.0675s | 1 | 8 | yes | 0.6425s | 0.7294s | `detyped_files/pystone/advanced/proportion_sweep/main_k01_s02.py` |  |
| 0.07 | 1/15 | 3 | 0.7091s | 0.0370s | 1 | 8 | yes | 0.6878s | 0.7354s | `detyped_files/pystone/advanced/proportion_sweep/main_k01_s03.py` |  |
| 0.07 | 1/15 | 4 | 0.6705s | 0.0610s | 1 | 8 | yes | 0.6280s | 0.7057s | `detyped_files/pystone/advanced/proportion_sweep/main_k01_s04.py` |  |
| 0.07 | 1/15 | 5 | 1.5331s | 0.0461s | 1 | 8 | yes | 1.5054s | 1.5644s | `detyped_files/pystone/advanced/proportion_sweep/main_k01_s05.py` |  |
| 0.07 | 1/15 | 6 | 0.9694s | 0.0956s | 1 | 8 | yes | 0.9104s | 1.0316s | `detyped_files/pystone/advanced/proportion_sweep/main_k01_s06.py` |  |
| 0.07 | 1/15 | 7 | 0.8412s | 0.0730s | 1 | 8 | yes | 0.7928s | 0.8886s | `detyped_files/pystone/advanced/proportion_sweep/main_k01_s07.py` |  |
| 0.07 | 1/15 | 8 | 0.6888s | 0.0378s | 1 | 8 | yes | 0.6627s | 0.7109s | `detyped_files/pystone/advanced/proportion_sweep/main_k01_s08.py` |  |
| 0.07 | 1/15 | 9 | 0.6753s | 0.0674s | 1 | 8 | yes | 0.6326s | 0.7185s | `detyped_files/pystone/advanced/proportion_sweep/main_k01_s09.py` |  |
| 0.07 | 1/15 | 10 | 0.6926s | 0.0343s | 1 | 8 | yes | 0.6697s | 0.7126s | `detyped_files/pystone/advanced/proportion_sweep/main_k01_s10.py` |  |
| 0.07 | 1/15 | 11 | 0.6923s | 0.0579s | 1 | 8 | yes | 0.6556s | 0.7296s | `detyped_files/pystone/advanced/proportion_sweep/main_k01_s11.py` |  |
| 0.07 | 1/15 | 12 | 0.6853s | 0.0518s | 1 | 8 | yes | 0.6477s | 0.7135s | `detyped_files/pystone/advanced/proportion_sweep/main_k01_s12.py` |  |
| 0.07 | 1/15 | 13 | 0.6743s | 0.0580s | 1 | 8 | yes | 0.6335s | 0.7080s | `detyped_files/pystone/advanced/proportion_sweep/main_k01_s13.py` |  |
| 0.07 | 1/15 | 14 | 0.6754s | 0.0506s | 1 | 8 | yes | 0.6416s | 0.7056s | `detyped_files/pystone/advanced/proportion_sweep/main_k01_s14.py` |  |
| 0.07 | 1/15 | 15 | 0.6746s | 0.0571s | 1 | 8 | yes | 0.6363s | 0.7095s | `detyped_files/pystone/advanced/proportion_sweep/main_k01_s15.py` |  |
| 0.13 | 2/15 | 1 | 0.9627s | 0.0788s | 1 | 8 | yes | 0.9118s | 1.0129s | `detyped_files/pystone/advanced/proportion_sweep/main_k02_s01.py` |  |
| 0.13 | 2/15 | 2 | 0.6592s | 0.0563s | 1 | 8 | yes | 0.6206s | 0.6929s | `detyped_files/pystone/advanced/proportion_sweep/main_k02_s02.py` |  |
| 0.13 | 2/15 | 3 | 0.7071s | 0.0643s | 1 | 8 | yes | 0.6655s | 0.7491s | `detyped_files/pystone/advanced/proportion_sweep/main_k02_s03.py` |  |
| 0.13 | 2/15 | 4 | 0.9883s | 0.0992s | 1 | 8 | yes | 0.9301s | 1.0551s | `detyped_files/pystone/advanced/proportion_sweep/main_k02_s04.py` |  |
| 0.13 | 2/15 | 5 | 0.6786s | 0.0619s | 1 | 8 | yes | 0.6367s | 0.7165s | `detyped_files/pystone/advanced/proportion_sweep/main_k02_s05.py` |  |
| 0.13 | 2/15 | 6 | 0.7103s | 0.0423s | 1 | 8 | yes | 0.6821s | 0.7372s | `detyped_files/pystone/advanced/proportion_sweep/main_k02_s06.py` |  |
| 0.13 | 2/15 | 7 | 0.8142s | 0.0827s | 1 | 8 | yes | 0.7640s | 0.8696s | `detyped_files/pystone/advanced/proportion_sweep/main_k02_s07.py` |  |
| 0.13 | 2/15 | 8 | 0.7028s | 0.0392s | 1 | 8 | yes | 0.6763s | 0.7258s | `detyped_files/pystone/advanced/proportion_sweep/main_k02_s08.py` |  |
| 0.13 | 2/15 | 9 | 0.6474s | 0.0731s | 1 | 8 | yes | 0.6052s | 0.6989s | `detyped_files/pystone/advanced/proportion_sweep/main_k02_s09.py` |  |
| 0.13 | 2/15 | 10 | 0.7240s | 0.0382s | 1 | 8 | yes | 0.7021s | 0.7507s | `detyped_files/pystone/advanced/proportion_sweep/main_k02_s10.py` |  |
| 0.13 | 2/15 | 11 | 0.6992s | 0.0461s | 1 | 8 | yes | 0.6656s | 0.7234s | `detyped_files/pystone/advanced/proportion_sweep/main_k02_s11.py` |  |
| 0.13 | 2/15 | 12 | 1.5132s | 0.0444s | 1 | 8 | yes | 1.4858s | 1.5431s | `detyped_files/pystone/advanced/proportion_sweep/main_k02_s12.py` |  |
| 0.13 | 2/15 | 13 | 0.7247s | 0.0368s | 1 | 8 | yes | 0.7020s | 0.7498s | `detyped_files/pystone/advanced/proportion_sweep/main_k02_s13.py` |  |
| 0.13 | 2/15 | 14 | 0.8549s | 0.0707s | 1 | 8 | yes | 0.8102s | 0.9002s | `detyped_files/pystone/advanced/proportion_sweep/main_k02_s14.py` |  |
| 0.13 | 2/15 | 15 | 0.6369s | 0.0462s | 1 | 8 | yes | 0.6069s | 0.6663s | `detyped_files/pystone/advanced/proportion_sweep/main_k02_s15.py` |  |
| 0.13 | 2/15 | 16 | 0.6630s | 0.0730s | 1 | 8 | yes | 0.6152s | 0.7084s | `detyped_files/pystone/advanced/proportion_sweep/main_k02_s16.py` |  |
| 0.13 | 2/15 | 17 | 0.9562s | 0.0525s | 1 | 8 | yes | 0.9213s | 0.9887s | `detyped_files/pystone/advanced/proportion_sweep/main_k02_s17.py` |  |
| 0.13 | 2/15 | 18 | 0.6888s | 0.0370s | 1 | 8 | yes | 0.6644s | 0.7122s | `detyped_files/pystone/advanced/proportion_sweep/main_k02_s18.py` |  |
| 0.13 | 2/15 | 19 | 0.7106s | 0.0678s | 1 | 8 | yes | 0.6654s | 0.7513s | `detyped_files/pystone/advanced/proportion_sweep/main_k02_s19.py` |  |
| 0.13 | 2/15 | 20 | 0.9979s | 0.0826s | 1 | 8 | yes | 0.9458s | 1.0531s | `detyped_files/pystone/advanced/proportion_sweep/main_k02_s20.py` |  |
| 0.20 | 3/15 | 1 | 0.6874s | 0.0225s | 1 | 8 | yes | 0.6734s | 0.7028s | `detyped_files/pystone/advanced/proportion_sweep/main_k03_s01.py` |  |
| 0.20 | 3/15 | 2 | 1.6103s | 0.0949s | 1 | 8 | yes | 1.5500s | 1.6745s | `detyped_files/pystone/advanced/proportion_sweep/main_k03_s02.py` |  |
| 0.20 | 3/15 | 3 | 0.6749s | 0.0643s | 1 | 8 | yes | 0.6302s | 0.7126s | `detyped_files/pystone/advanced/proportion_sweep/main_k03_s03.py` |  |
| 0.20 | 3/15 | 4 | 1.5559s | 0.0587s | 1 | 8 | yes | 1.5162s | 1.5920s | `detyped_files/pystone/advanced/proportion_sweep/main_k03_s04.py` |  |
| 0.20 | 3/15 | 5 | 0.6899s | 0.0525s | 1 | 8 | yes | 0.6576s | 0.7250s | `detyped_files/pystone/advanced/proportion_sweep/main_k03_s05.py` |  |
| 0.20 | 3/15 | 6 | 0.6603s | 0.0475s | 1 | 8 | yes | 0.6296s | 0.6910s | `detyped_files/pystone/advanced/proportion_sweep/main_k03_s06.py` |  |
| 0.20 | 3/15 | 7 | 0.7063s | 0.0629s | 1 | 8 | yes | 0.6623s | 0.7444s | `detyped_files/pystone/advanced/proportion_sweep/main_k03_s07.py` |  |
| 0.20 | 3/15 | 8 | 0.9916s | 0.0405s | 1 | 8 | yes | 0.9661s | 1.0178s | `detyped_files/pystone/advanced/proportion_sweep/main_k03_s08.py` |  |
| 0.20 | 3/15 | 9 | 0.6793s | 0.0600s | 1 | 8 | yes | 0.6394s | 0.7161s | `detyped_files/pystone/advanced/proportion_sweep/main_k03_s09.py` |  |
| 0.20 | 3/15 | 10 | 0.6805s | 0.0428s | 1 | 8 | yes | 0.6525s | 0.7072s | `detyped_files/pystone/advanced/proportion_sweep/main_k03_s10.py` |  |
| 0.20 | 3/15 | 11 | 0.6372s | 0.0636s | 1 | 8 | yes | 0.5955s | 0.6770s | `detyped_files/pystone/advanced/proportion_sweep/main_k03_s11.py` |  |
| 0.20 | 3/15 | 12 | 1.0006s | 0.0299s | 1 | 8 | yes | 0.9818s | 1.0203s | `detyped_files/pystone/advanced/proportion_sweep/main_k03_s12.py` |  |
| 0.20 | 3/15 | 13 | 1.4652s | 0.0371s | 1 | 8 | yes | 1.4416s | 1.4895s | `detyped_files/pystone/advanced/proportion_sweep/main_k03_s13.py` |  |
| 0.20 | 3/15 | 14 | 1.4968s | 0.0768s | 1 | 8 | yes | 1.4521s | 1.5495s | `detyped_files/pystone/advanced/proportion_sweep/main_k03_s14.py` |  |
| 0.20 | 3/15 | 15 | 0.6955s | 0.0176s | 1 | 8 | yes | 0.6843s | 0.7065s | `detyped_files/pystone/advanced/proportion_sweep/main_k03_s15.py` |  |
| 0.20 | 3/15 | 16 | 0.6972s | 0.0647s | 1 | 8 | yes | 0.6568s | 0.7400s | `detyped_files/pystone/advanced/proportion_sweep/main_k03_s16.py` |  |
| 0.20 | 3/15 | 17 | 0.6675s | 0.0714s | 1 | 8 | yes | 0.6225s | 0.7146s | `detyped_files/pystone/advanced/proportion_sweep/main_k03_s17.py` |  |
| 0.20 | 3/15 | 18 | 0.8052s | 0.0694s | 1 | 8 | yes | 0.7590s | 0.8484s | `detyped_files/pystone/advanced/proportion_sweep/main_k03_s18.py` |  |
| 0.20 | 3/15 | 19 | 0.6499s | 0.0488s | 1 | 8 | yes | 0.6166s | 0.6798s | `detyped_files/pystone/advanced/proportion_sweep/main_k03_s19.py` |  |
| 0.20 | 3/15 | 20 | 0.9863s | 0.0497s | 1 | 8 | yes | 0.9569s | 1.0212s | `detyped_files/pystone/advanced/proportion_sweep/main_k03_s20.py` |  |
| 0.27 | 4/15 | 1 | 0.7073s | 0.0561s | 1 | 8 | yes | 0.6654s | 0.7374s | `detyped_files/pystone/advanced/proportion_sweep/main_k04_s01.py` |  |
| 0.27 | 4/15 | 2 | 0.9860s | 0.0377s | 1 | 8 | yes | 0.9614s | 1.0093s | `detyped_files/pystone/advanced/proportion_sweep/main_k04_s02.py` |  |
| 0.27 | 4/15 | 3 | 0.7208s | 0.0385s | 1 | 8 | yes | 0.6969s | 0.7460s | `detyped_files/pystone/advanced/proportion_sweep/main_k04_s03.py` |  |
| 0.27 | 4/15 | 4 | 1.0055s | 0.1017s | 1 | 8 | yes | 0.9383s | 1.0694s | `detyped_files/pystone/advanced/proportion_sweep/main_k04_s04.py` |  |
| 0.27 | 4/15 | 5 | 0.7126s | 0.0354s | 1 | 8 | yes | 0.6904s | 0.7356s | `detyped_files/pystone/advanced/proportion_sweep/main_k04_s05.py` |  |
| 0.27 | 4/15 | 6 | 0.9472s | 0.0614s | 1 | 8 | yes | 0.9059s | 0.9845s | `detyped_files/pystone/advanced/proportion_sweep/main_k04_s06.py` |  |
| 0.27 | 4/15 | 7 | 0.6935s | 0.0308s | 1 | 8 | yes | 0.6751s | 0.7144s | `detyped_files/pystone/advanced/proportion_sweep/main_k04_s07.py` |  |
| 0.27 | 4/15 | 8 | 1.5123s | 0.1366s | 1 | 8 | yes | 1.4248s | 1.6034s | `detyped_files/pystone/advanced/proportion_sweep/main_k04_s08.py` |  |
| 0.27 | 4/15 | 9 | 0.8115s | 0.0600s | 1 | 8 | yes | 0.7709s | 0.8480s | `detyped_files/pystone/advanced/proportion_sweep/main_k04_s09.py` |  |
| 0.27 | 4/15 | 10 | 0.6478s | 0.0774s | 1 | 8 | yes | 0.5991s | 0.6996s | `detyped_files/pystone/advanced/proportion_sweep/main_k04_s10.py` |  |
| 0.27 | 4/15 | 11 | 0.7009s | 0.0503s | 1 | 8 | yes | 0.6682s | 0.7321s | `detyped_files/pystone/advanced/proportion_sweep/main_k04_s11.py` |  |
| 0.27 | 4/15 | 12 | 0.9522s | 0.0691s | 1 | 8 | yes | 0.9108s | 0.9977s | `detyped_files/pystone/advanced/proportion_sweep/main_k04_s12.py` |  |
| 0.27 | 4/15 | 13 | 0.6644s | 0.0461s | 1 | 8 | yes | 0.6324s | 0.6910s | `detyped_files/pystone/advanced/proportion_sweep/main_k04_s13.py` |  |
| 0.27 | 4/15 | 14 | 0.6862s | 0.0971s | 1 | 8 | yes | 0.6256s | 0.7518s | `detyped_files/pystone/advanced/proportion_sweep/main_k04_s14.py` |  |
| 0.27 | 4/15 | 15 | 0.6423s | 0.0531s | 1 | 8 | yes | 0.6062s | 0.6743s | `detyped_files/pystone/advanced/proportion_sweep/main_k04_s15.py` |  |
| 0.27 | 4/15 | 16 | 0.8224s | 0.0663s | 1 | 8 | yes | 0.7811s | 0.8660s | `detyped_files/pystone/advanced/proportion_sweep/main_k04_s16.py` |  |
| 0.27 | 4/15 | 17 | 0.6615s | 0.0499s | 1 | 8 | yes | 0.6259s | 0.6904s | `detyped_files/pystone/advanced/proportion_sweep/main_k04_s17.py` |  |
| 0.27 | 4/15 | 18 | 0.6633s | 0.0692s | 1 | 8 | yes | 0.6165s | 0.7064s | `detyped_files/pystone/advanced/proportion_sweep/main_k04_s18.py` |  |
| 0.27 | 4/15 | 19 | 0.8276s | 0.0707s | 1 | 8 | yes | 0.7795s | 0.8700s | `detyped_files/pystone/advanced/proportion_sweep/main_k04_s19.py` |  |
| 0.27 | 4/15 | 20 | 0.9825s | 0.0561s | 1 | 8 | yes | 0.9448s | 1.0185s | `detyped_files/pystone/advanced/proportion_sweep/main_k04_s20.py` |  |
| 0.33 | 5/15 | 1 | 1.9597s | 0.1072s | 1 | 8 | yes | 1.9028s | 2.0388s | `detyped_files/pystone/advanced/proportion_sweep/main_k05_s01.py` |  |
| 0.33 | 5/15 | 2 | 0.6795s | 0.0776s | 1 | 8 | yes | 0.6236s | 0.7254s | `detyped_files/pystone/advanced/proportion_sweep/main_k05_s02.py` |  |
| 0.33 | 5/15 | 3 | 1.4885s | 0.1167s | 1 | 8 | yes | 1.4149s | 1.5649s | `detyped_files/pystone/advanced/proportion_sweep/main_k05_s03.py` |  |
| 0.33 | 5/15 | 4 | 1.8032s | 0.0558s | 1 | 8 | yes | 1.7639s | 1.8364s | `detyped_files/pystone/advanced/proportion_sweep/main_k05_s04.py` |  |
| 0.33 | 5/15 | 5 | 0.9737s | 0.0928s | 1 | 8 | yes | 0.9221s | 1.0401s | `detyped_files/pystone/advanced/proportion_sweep/main_k05_s05.py` |  |
| 0.33 | 5/15 | 6 | 0.9520s | 0.1061s | 1 | 8 | yes | 0.8879s | 1.0241s | `detyped_files/pystone/advanced/proportion_sweep/main_k05_s06.py` |  |
| 0.33 | 5/15 | 7 | 0.9880s | 0.0377s | 1 | 8 | yes | 0.9628s | 1.0117s | `detyped_files/pystone/advanced/proportion_sweep/main_k05_s07.py` |  |
| 0.33 | 5/15 | 8 | 1.5115s | 0.0818s | 1 | 8 | yes | 1.4605s | 1.5664s | `detyped_files/pystone/advanced/proportion_sweep/main_k05_s08.py` |  |
| 0.33 | 5/15 | 9 | 1.8407s | 0.0702s | 1 | 8 | yes | 1.7951s | 1.8852s | `detyped_files/pystone/advanced/proportion_sweep/main_k05_s09.py` |  |
| 0.33 | 5/15 | 10 | 0.7864s | 0.0340s | 1 | 8 | yes | 0.7635s | 0.8071s | `detyped_files/pystone/advanced/proportion_sweep/main_k05_s10.py` |  |
| 0.33 | 5/15 | 11 | 1.7664s | 0.1064s | 1 | 8 | yes | 1.7012s | 1.8393s | `detyped_files/pystone/advanced/proportion_sweep/main_k05_s11.py` |  |
| 0.33 | 5/15 | 12 | 0.8373s | 0.0897s | 1 | 8 | yes | 0.7817s | 0.8970s | `detyped_files/pystone/advanced/proportion_sweep/main_k05_s12.py` |  |
| 0.33 | 5/15 | 13 | 1.5051s | 0.0772s | 1 | 8 | yes | 1.4592s | 1.5595s | `detyped_files/pystone/advanced/proportion_sweep/main_k05_s13.py` |  |
| 0.33 | 5/15 | 14 | 1.8396s | 0.1335s | 1 | 8 | yes | 1.7592s | 1.9311s | `detyped_files/pystone/advanced/proportion_sweep/main_k05_s14.py` |  |
| 0.33 | 5/15 | 15 | 0.9805s | 0.0667s | 1 | 8 | yes | 0.9417s | 1.0279s | `detyped_files/pystone/advanced/proportion_sweep/main_k05_s15.py` |  |
| 0.33 | 5/15 | 16 | 1.5005s | 0.0720s | 1 | 8 | yes | 1.4520s | 1.5454s | `detyped_files/pystone/advanced/proportion_sweep/main_k05_s16.py` |  |
| 0.33 | 5/15 | 17 | 1.4902s | 0.0845s | 1 | 8 | yes | 1.4326s | 1.5415s | `detyped_files/pystone/advanced/proportion_sweep/main_k05_s17.py` |  |
| 0.33 | 5/15 | 18 | 0.6957s | 0.0467s | 1 | 8 | yes | 0.6649s | 0.7261s | `detyped_files/pystone/advanced/proportion_sweep/main_k05_s18.py` |  |
| 0.33 | 5/15 | 19 | 1.0951s | 0.0629s | 1 | 8 | yes | 1.0571s | 1.1393s | `detyped_files/pystone/advanced/proportion_sweep/main_k05_s19.py` |  |
| 0.33 | 5/15 | 20 | 0.7836s | 0.0472s | 1 | 8 | yes | 0.7533s | 0.8142s | `detyped_files/pystone/advanced/proportion_sweep/main_k05_s20.py` |  |
| 0.40 | 6/15 | 1 | 0.6842s | 0.0542s | 1 | 8 | yes | 0.6452s | 0.7138s | `detyped_files/pystone/advanced/proportion_sweep/main_k06_s01.py` |  |
| 0.40 | 6/15 | 2 | 1.8194s | 0.0555s | 1 | 8 | yes | 1.7849s | 1.8558s | `detyped_files/pystone/advanced/proportion_sweep/main_k06_s02.py` |  |
| 0.40 | 6/15 | 3 | 1.5869s | 0.1005s | 1 | 8 | yes | 1.5240s | 1.6527s | `detyped_files/pystone/advanced/proportion_sweep/main_k06_s03.py` |  |
| 0.40 | 6/15 | 4 | 0.6489s | 0.0590s | 1 | 8 | yes | 0.6121s | 0.6878s | `detyped_files/pystone/advanced/proportion_sweep/main_k06_s04.py` |  |
| 0.40 | 6/15 | 5 | 1.8658s | 0.2289s | 1 | 8 | yes | 1.7389s | 2.0289s | `detyped_files/pystone/advanced/proportion_sweep/main_k06_s05.py` |  |
| 0.40 | 6/15 | 6 | 0.7248s | 0.0542s | 1 | 8 | yes | 0.6916s | 0.7613s | `detyped_files/pystone/advanced/proportion_sweep/main_k06_s06.py` |  |
| 0.40 | 6/15 | 7 | 1.4725s | 0.0572s | 1 | 8 | yes | 1.4347s | 1.5092s | `detyped_files/pystone/advanced/proportion_sweep/main_k06_s07.py` |  |
| 0.40 | 6/15 | 8 | 1.4657s | 0.0417s | 1 | 8 | yes | 1.4404s | 1.4935s | `detyped_files/pystone/advanced/proportion_sweep/main_k06_s08.py` |  |
| 0.40 | 6/15 | 9 | 0.6760s | 0.0565s | 1 | 8 | yes | 0.6342s | 0.7066s | `detyped_files/pystone/advanced/proportion_sweep/main_k06_s09.py` |  |
| 0.40 | 6/15 | 10 | 0.8209s | 0.0402s | 1 | 8 | yes | 0.7935s | 0.8446s | `detyped_files/pystone/advanced/proportion_sweep/main_k06_s10.py` |  |
| 0.40 | 6/15 | 11 | 1.8188s | 0.0963s | 1 | 8 | yes | 1.7637s | 1.8875s | `detyped_files/pystone/advanced/proportion_sweep/main_k06_s11.py` |  |
| 0.40 | 6/15 | 12 | 1.4874s | 0.0629s | 1 | 8 | yes | 1.4450s | 1.5254s | `detyped_files/pystone/advanced/proportion_sweep/main_k06_s12.py` |  |
| 0.40 | 6/15 | 13 | 0.9869s | 0.0177s | 1 | 8 | yes | 0.9762s | 0.9989s | `detyped_files/pystone/advanced/proportion_sweep/main_k06_s13.py` |  |
| 0.40 | 6/15 | 14 | 0.7680s | 0.0603s | 1 | 8 | yes | 0.7326s | 0.8111s | `detyped_files/pystone/advanced/proportion_sweep/main_k06_s14.py` |  |
| 0.40 | 6/15 | 15 | 1.5185s | 0.0515s | 1 | 8 | yes | 1.4862s | 1.5522s | `detyped_files/pystone/advanced/proportion_sweep/main_k06_s15.py` |  |
| 0.40 | 6/15 | 16 | 0.6750s | 0.0677s | 1 | 8 | yes | 0.6314s | 0.7191s | `detyped_files/pystone/advanced/proportion_sweep/main_k06_s16.py` |  |
| 0.40 | 6/15 | 17 | 0.6900s | 0.0279s | 1 | 8 | yes | 0.6738s | 0.7098s | `detyped_files/pystone/advanced/proportion_sweep/main_k06_s17.py` |  |
| 0.40 | 6/15 | 18 | 0.6695s | 0.0887s | 2 | 16 | yes | 0.6276s | 0.7125s | `detyped_files/pystone/advanced/proportion_sweep/main_k06_s18.py` |  |
| 0.40 | 6/15 | 19 | 0.6690s | 0.0728s | 1 | 8 | yes | 0.6226s | 0.7167s | `detyped_files/pystone/advanced/proportion_sweep/main_k06_s19.py` |  |
| 0.40 | 6/15 | 20 | 0.6838s | 0.0617s | 1 | 8 | yes | 0.6431s | 0.7219s | `detyped_files/pystone/advanced/proportion_sweep/main_k06_s20.py` |  |
| 0.47 | 7/15 | 1 | 1.4697s | 0.0728s | 1 | 8 | yes | 1.4230s | 1.5152s | `detyped_files/pystone/advanced/proportion_sweep/main_k07_s01.py` |  |
| 0.47 | 7/15 | 2 | 1.0918s | 0.0488s | 1 | 8 | yes | 1.0583s | 1.1196s | `detyped_files/pystone/advanced/proportion_sweep/main_k07_s02.py` |  |
| 0.47 | 7/15 | 3 | 0.9573s | 0.0908s | 1 | 8 | yes | 0.8970s | 1.0132s | `detyped_files/pystone/advanced/proportion_sweep/main_k07_s03.py` |  |
| 0.47 | 7/15 | 4 | 0.6981s | 0.0437s | 1 | 8 | yes | 0.6682s | 0.7261s | `detyped_files/pystone/advanced/proportion_sweep/main_k07_s04.py` |  |
| 0.47 | 7/15 | 5 | 0.6466s | 0.0949s | 1 | 8 | yes | 0.5851s | 0.7074s | `detyped_files/pystone/advanced/proportion_sweep/main_k07_s05.py` |  |
| 0.47 | 7/15 | 6 | 0.9877s | 0.0678s | 1 | 8 | yes | 0.9385s | 1.0232s | `detyped_files/pystone/advanced/proportion_sweep/main_k07_s06.py` |  |
| 0.47 | 7/15 | 7 | 1.6568s | 0.1775s | 1 | 8 | yes | 1.5540s | 1.7793s | `detyped_files/pystone/advanced/proportion_sweep/main_k07_s07.py` |  |
| 0.47 | 7/15 | 8 | 1.9085s | 0.0563s | 1 | 8 | yes | 1.8713s | 1.9424s | `detyped_files/pystone/advanced/proportion_sweep/main_k07_s08.py` |  |
| 0.47 | 7/15 | 9 | 1.1055s | 0.0425s | 1 | 8 | yes | 1.0797s | 1.1353s | `detyped_files/pystone/advanced/proportion_sweep/main_k07_s09.py` |  |
| 0.47 | 7/15 | 10 | 0.6663s | 0.0728s | 1 | 8 | yes | 0.6186s | 0.7133s | `detyped_files/pystone/advanced/proportion_sweep/main_k07_s10.py` |  |
| 0.47 | 7/15 | 11 | 1.8166s | 0.0756s | 1 | 8 | yes | 1.7681s | 1.8668s | `detyped_files/pystone/advanced/proportion_sweep/main_k07_s11.py` |  |
| 0.47 | 7/15 | 12 | 0.8025s | 0.0455s | 1 | 8 | yes | 0.7730s | 0.8311s | `detyped_files/pystone/advanced/proportion_sweep/main_k07_s12.py` |  |
| 0.47 | 7/15 | 13 | 1.4759s | 0.0544s | 1 | 8 | yes | 1.4411s | 1.5112s | `detyped_files/pystone/advanced/proportion_sweep/main_k07_s13.py` |  |
| 0.47 | 7/15 | 14 | 1.5860s | 0.0758s | 1 | 8 | yes | 1.5407s | 1.6387s | `detyped_files/pystone/advanced/proportion_sweep/main_k07_s14.py` |  |
| 0.47 | 7/15 | 15 | 0.8445s | 0.0970s | 1 | 8 | yes | 0.7826s | 0.9087s | `detyped_files/pystone/advanced/proportion_sweep/main_k07_s15.py` |  |
| 0.47 | 7/15 | 16 | 1.5097s | 0.0788s | 1 | 8 | yes | 1.4699s | 1.5668s | `detyped_files/pystone/advanced/proportion_sweep/main_k07_s16.py` |  |
| 0.47 | 7/15 | 17 | 0.7012s | 0.0695s | 1 | 8 | yes | 0.6514s | 0.7375s | `detyped_files/pystone/advanced/proportion_sweep/main_k07_s17.py` |  |
| 0.47 | 7/15 | 18 | 0.6581s | 0.0562s | 1 | 8 | yes | 0.6230s | 0.6940s | `detyped_files/pystone/advanced/proportion_sweep/main_k07_s18.py` |  |
| 0.47 | 7/15 | 19 | 1.1406s | 0.0841s | 1 | 8 | yes | 1.0833s | 1.1907s | `detyped_files/pystone/advanced/proportion_sweep/main_k07_s19.py` |  |
| 0.47 | 7/15 | 20 | 1.9047s | 0.0521s | 1 | 8 | yes | 1.8717s | 1.9379s | `detyped_files/pystone/advanced/proportion_sweep/main_k07_s20.py` |  |
| 0.53 | 8/15 | 1 | 1.6695s | 0.0908s | 1 | 8 | yes | 1.6061s | 1.7228s | `detyped_files/pystone/advanced/proportion_sweep/main_k08_s01.py` |  |
| 0.53 | 8/15 | 2 | 0.6923s | 0.0597s | 1 | 8 | yes | 0.6519s | 0.7291s | `detyped_files/pystone/advanced/proportion_sweep/main_k08_s02.py` |  |
| 0.53 | 8/15 | 3 | 0.9483s | 0.0888s | 1 | 8 | yes | 0.8935s | 1.0076s | `detyped_files/pystone/advanced/proportion_sweep/main_k08_s03.py` |  |
| 0.53 | 8/15 | 4 | 1.5927s | 0.0966s | 1 | 8 | yes | 1.5322s | 1.6568s | `detyped_files/pystone/advanced/proportion_sweep/main_k08_s04.py` |  |
| 0.53 | 8/15 | 5 | 1.4924s | 0.0820s | 1 | 8 | yes | 1.4354s | 1.5408s | `detyped_files/pystone/advanced/proportion_sweep/main_k08_s05.py` |  |
| 0.53 | 8/15 | 6 | 0.6730s | 0.0718s | 1 | 8 | yes | 0.6220s | 0.7157s | `detyped_files/pystone/advanced/proportion_sweep/main_k08_s06.py` |  |
| 0.53 | 8/15 | 7 | 1.5754s | 0.0683s | 1 | 8 | yes | 1.5295s | 1.6187s | `detyped_files/pystone/advanced/proportion_sweep/main_k08_s07.py` |  |
| 0.53 | 8/15 | 8 | 1.1213s | 0.0542s | 1 | 8 | yes | 1.0906s | 1.1596s | `detyped_files/pystone/advanced/proportion_sweep/main_k08_s08.py` |  |
| 0.53 | 8/15 | 9 | 1.4612s | 0.1026s | 1 | 8 | yes | 1.3982s | 1.5295s | `detyped_files/pystone/advanced/proportion_sweep/main_k08_s09.py` |  |
| 0.53 | 8/15 | 10 | 1.5028s | 0.1232s | 1 | 8 | yes | 1.4261s | 1.5848s | `detyped_files/pystone/advanced/proportion_sweep/main_k08_s10.py` |  |
| 0.53 | 8/15 | 11 | 1.6595s | 0.0871s | 1 | 8 | yes | 1.6036s | 1.7150s | `detyped_files/pystone/advanced/proportion_sweep/main_k08_s11.py` |  |
| 0.53 | 8/15 | 12 | 1.8371s | 0.0970s | 1 | 8 | yes | 1.7754s | 1.9012s | `detyped_files/pystone/advanced/proportion_sweep/main_k08_s12.py` |  |
| 0.53 | 8/15 | 13 | 1.5127s | 0.1132s | 1 | 8 | yes | 1.4628s | 1.5958s | `detyped_files/pystone/advanced/proportion_sweep/main_k08_s13.py` |  |
| 0.53 | 8/15 | 14 | 1.0894s | 0.0570s | 1 | 8 | yes | 1.0536s | 1.1267s | `detyped_files/pystone/advanced/proportion_sweep/main_k08_s14.py` |  |
| 0.53 | 8/15 | 15 | 1.7718s | 0.1107s | 1 | 8 | yes | 1.7026s | 1.8462s | `detyped_files/pystone/advanced/proportion_sweep/main_k08_s15.py` |  |
| 0.53 | 8/15 | 16 | 1.4930s | 0.1033s | 1 | 8 | yes | 1.4246s | 1.5576s | `detyped_files/pystone/advanced/proportion_sweep/main_k08_s16.py` |  |
| 0.53 | 8/15 | 17 | 1.0964s | 0.0735s | 1 | 8 | yes | 1.0528s | 1.1463s | `detyped_files/pystone/advanced/proportion_sweep/main_k08_s17.py` |  |
| 0.53 | 8/15 | 18 | 1.0628s | 0.0725s | 1 | 8 | yes | 1.0177s | 1.1109s | `detyped_files/pystone/advanced/proportion_sweep/main_k08_s18.py` |  |
| 0.53 | 8/15 | 19 | 1.9450s | 0.0867s | 1 | 8 | yes | 1.8966s | 2.0079s | `detyped_files/pystone/advanced/proportion_sweep/main_k08_s19.py` |  |
| 0.53 | 8/15 | 20 | 1.7484s | 0.1026s | 1 | 8 | yes | 1.6850s | 1.8186s | `detyped_files/pystone/advanced/proportion_sweep/main_k08_s20.py` |  |
| 0.60 | 9/15 | 1 | 1.1222s | 0.0474s | 1 | 8 | yes | 1.0925s | 1.1525s | `detyped_files/pystone/advanced/proportion_sweep/main_k09_s01.py` |  |
| 0.60 | 9/15 | 2 | 1.6442s | 0.0461s | 1 | 8 | yes | 1.6154s | 1.6754s | `detyped_files/pystone/advanced/proportion_sweep/main_k09_s02.py` |  |
| 0.60 | 9/15 | 3 | 0.6804s | 0.0418s | 1 | 8 | yes | 0.6527s | 0.7060s | `detyped_files/pystone/advanced/proportion_sweep/main_k09_s03.py` |  |
| 0.60 | 9/15 | 4 | 1.7725s | 0.0909s | 1 | 8 | yes | 1.7163s | 1.8322s | `detyped_files/pystone/advanced/proportion_sweep/main_k09_s04.py` |  |
| 0.60 | 9/15 | 5 | 1.9307s | 0.0919s | 1 | 8 | yes | 1.8701s | 1.9905s | `detyped_files/pystone/advanced/proportion_sweep/main_k09_s05.py` |  |
| 0.60 | 9/15 | 6 | 1.4529s | 0.0743s | 1 | 8 | yes | 1.4053s | 1.4996s | `detyped_files/pystone/advanced/proportion_sweep/main_k09_s06.py` |  |
| 0.60 | 9/15 | 7 | 1.0852s | 0.0327s | 1 | 8 | yes | 1.0622s | 1.1039s | `detyped_files/pystone/advanced/proportion_sweep/main_k09_s07.py` |  |
| 0.60 | 9/15 | 8 | 1.4946s | 0.1297s | 1 | 8 | yes | 1.4167s | 1.5849s | `detyped_files/pystone/advanced/proportion_sweep/main_k09_s08.py` |  |
| 0.60 | 9/15 | 9 | 1.5115s | 0.0618s | 1 | 8 | yes | 1.4723s | 1.5528s | `detyped_files/pystone/advanced/proportion_sweep/main_k09_s09.py` |  |
| 0.60 | 9/15 | 10 | 1.7714s | 0.0698s | 1 | 8 | yes | 1.7243s | 1.8152s | `detyped_files/pystone/advanced/proportion_sweep/main_k09_s10.py` |  |
| 0.60 | 9/15 | 11 | 1.9339s | 0.0803s | 1 | 8 | yes | 1.8815s | 1.9888s | `detyped_files/pystone/advanced/proportion_sweep/main_k09_s11.py` |  |
| 0.60 | 9/15 | 12 | 0.9835s | 0.0888s | 1 | 8 | yes | 0.9302s | 1.0439s | `detyped_files/pystone/advanced/proportion_sweep/main_k09_s12.py` |  |
| 0.60 | 9/15 | 13 | 0.8195s | 0.0858s | 1 | 8 | yes | 0.7634s | 0.8756s | `detyped_files/pystone/advanced/proportion_sweep/main_k09_s13.py` |  |
| 0.60 | 9/15 | 14 | 1.6270s | 0.1537s | 1 | 8 | yes | 1.5424s | 1.7375s | `detyped_files/pystone/advanced/proportion_sweep/main_k09_s14.py` |  |
| 0.60 | 9/15 | 15 | 1.6108s | 0.0362s | 1 | 8 | yes | 1.5886s | 1.6354s | `detyped_files/pystone/advanced/proportion_sweep/main_k09_s15.py` |  |
| 0.60 | 9/15 | 16 | 1.5954s | 0.1065s | 1 | 8 | yes | 1.5281s | 1.6654s | `detyped_files/pystone/advanced/proportion_sweep/main_k09_s16.py` |  |
| 0.60 | 9/15 | 17 | 1.0552s | 0.0863s | 1 | 8 | yes | 0.9976s | 1.1125s | `detyped_files/pystone/advanced/proportion_sweep/main_k09_s17.py` |  |
| 0.60 | 9/15 | 18 | 1.5968s | 0.0765s | 1 | 8 | yes | 1.5476s | 1.6460s | `detyped_files/pystone/advanced/proportion_sweep/main_k09_s18.py` |  |
| 0.60 | 9/15 | 19 | 1.5929s | 0.0865s | 1 | 8 | yes | 1.5370s | 1.6478s | `detyped_files/pystone/advanced/proportion_sweep/main_k09_s19.py` |  |
| 0.60 | 9/15 | 20 | 1.9144s | 0.0912s | 1 | 8 | yes | 1.8570s | 1.9750s | `detyped_files/pystone/advanced/proportion_sweep/main_k09_s20.py` |  |
| 0.67 | 10/15 | 1 | 0.8503s | 0.0487s | 1 | 8 | yes | 0.8155s | 0.8775s | `detyped_files/pystone/advanced/proportion_sweep/main_k10_s01.py` |  |
| 0.67 | 10/15 | 2 | 1.7647s | 0.0852s | 1 | 8 | yes | 1.7038s | 1.8135s | `detyped_files/pystone/advanced/proportion_sweep/main_k10_s02.py` |  |
| 0.67 | 10/15 | 3 | 1.0260s | 0.0397s | 1 | 8 | yes | 1.0013s | 1.0520s | `detyped_files/pystone/advanced/proportion_sweep/main_k10_s03.py` |  |
| 0.67 | 10/15 | 4 | 1.0935s | 0.0750s | 1 | 8 | yes | 1.0458s | 1.1422s | `detyped_files/pystone/advanced/proportion_sweep/main_k10_s04.py` |  |
| 0.67 | 10/15 | 5 | 1.9537s | 0.1162s | 1 | 8 | yes | 1.8819s | 2.0318s | `detyped_files/pystone/advanced/proportion_sweep/main_k10_s05.py` |  |
| 0.67 | 10/15 | 6 | 0.6742s | 0.0881s | 1 | 8 | yes | 0.6186s | 0.7304s | `detyped_files/pystone/advanced/proportion_sweep/main_k10_s06.py` |  |
| 0.67 | 10/15 | 7 | 1.8169s | 0.1419s | 1 | 8 | yes | 1.7324s | 1.9146s | `detyped_files/pystone/advanced/proportion_sweep/main_k10_s07.py` |  |
| 0.67 | 10/15 | 8 | 1.9330s | 0.0832s | 1 | 8 | yes | 1.8769s | 1.9844s | `detyped_files/pystone/advanced/proportion_sweep/main_k10_s08.py` |  |
| 0.67 | 10/15 | 9 | 1.8012s | 0.0881s | 1 | 8 | yes | 1.7427s | 1.8555s | `detyped_files/pystone/advanced/proportion_sweep/main_k10_s09.py` |  |
| 0.67 | 10/15 | 10 | 1.7925s | 0.0932s | 1 | 8 | yes | 1.7296s | 1.8523s | `detyped_files/pystone/advanced/proportion_sweep/main_k10_s10.py` |  |
| 0.67 | 10/15 | 11 | 1.9357s | 0.0486s | 1 | 8 | yes | 1.9036s | 1.9670s | `detyped_files/pystone/advanced/proportion_sweep/main_k10_s11.py` |  |
| 0.67 | 10/15 | 12 | 1.7549s | 0.0760s | 1 | 8 | yes | 1.7014s | 1.7973s | `detyped_files/pystone/advanced/proportion_sweep/main_k10_s12.py` |  |
| 0.67 | 10/15 | 13 | 1.9653s | 0.1006s | 1 | 8 | yes | 1.8993s | 2.0305s | `detyped_files/pystone/advanced/proportion_sweep/main_k10_s13.py` |  |
| 0.67 | 10/15 | 14 | 1.1538s | 0.0877s | 1 | 8 | yes | 1.1049s | 1.2163s | `detyped_files/pystone/advanced/proportion_sweep/main_k10_s14.py` |  |
| 0.67 | 10/15 | 15 | 1.6379s | 0.0595s | 1 | 8 | yes | 1.6022s | 1.6778s | `detyped_files/pystone/advanced/proportion_sweep/main_k10_s15.py` |  |
| 0.67 | 10/15 | 16 | 1.8077s | 0.1606s | 1 | 8 | yes | 1.7133s | 1.9164s | `detyped_files/pystone/advanced/proportion_sweep/main_k10_s16.py` |  |
| 0.67 | 10/15 | 17 | 0.6995s | 0.0535s | 1 | 8 | yes | 0.6607s | 0.7264s | `detyped_files/pystone/advanced/proportion_sweep/main_k10_s17.py` |  |
| 0.67 | 10/15 | 18 | 0.6760s | 0.0590s | 1 | 8 | yes | 0.6354s | 0.7116s | `detyped_files/pystone/advanced/proportion_sweep/main_k10_s18.py` |  |
| 0.67 | 10/15 | 19 | 0.6644s | 0.0574s | 1 | 8 | yes | 0.6250s | 0.6992s | `detyped_files/pystone/advanced/proportion_sweep/main_k10_s19.py` |  |
| 0.67 | 10/15 | 20 | 1.4543s | 0.0770s | 1 | 8 | yes | 1.4030s | 1.5032s | `detyped_files/pystone/advanced/proportion_sweep/main_k10_s20.py` |  |
| 0.73 | 11/15 | 1 | 1.9048s | 0.0729s | 1 | 8 | yes | 1.8651s | 1.9564s | `detyped_files/pystone/advanced/proportion_sweep/main_k11_s01.py` |  |
| 0.73 | 11/15 | 2 | 0.9454s | 0.0665s | 1 | 8 | yes | 0.8982s | 0.9845s | `detyped_files/pystone/advanced/proportion_sweep/main_k11_s02.py` |  |
| 0.73 | 11/15 | 3 | 1.9489s | 0.1243s | 1 | 8 | yes | 1.8702s | 2.0293s | `detyped_files/pystone/advanced/proportion_sweep/main_k11_s03.py` |  |
| 0.73 | 11/15 | 4 | 1.8206s | 0.1201s | 1 | 8 | yes | 1.7455s | 1.9011s | `detyped_files/pystone/advanced/proportion_sweep/main_k11_s04.py` |  |
| 0.73 | 11/15 | 5 | 1.9084s | 0.0482s | 1 | 8 | yes | 1.8783s | 1.9400s | `detyped_files/pystone/advanced/proportion_sweep/main_k11_s05.py` |  |
| 0.73 | 11/15 | 6 | 1.9304s | 0.0853s | 1 | 8 | yes | 1.8720s | 1.9829s | `detyped_files/pystone/advanced/proportion_sweep/main_k11_s06.py` |  |
| 0.73 | 11/15 | 7 | 2.0036s | 0.0948s | 1 | 8 | yes | 1.9407s | 2.0631s | `detyped_files/pystone/advanced/proportion_sweep/main_k11_s07.py` |  |
| 0.73 | 11/15 | 8 | 1.0759s | 0.0781s | 1 | 8 | yes | 1.0246s | 1.1275s | `detyped_files/pystone/advanced/proportion_sweep/main_k11_s08.py` |  |
| 0.73 | 11/15 | 9 | 0.9669s | 0.0572s | 1 | 8 | yes | 0.9287s | 1.0033s | `detyped_files/pystone/advanced/proportion_sweep/main_k11_s09.py` |  |
| 0.73 | 11/15 | 10 | 1.6062s | 0.0674s | 1 | 8 | yes | 1.5684s | 1.6531s | `detyped_files/pystone/advanced/proportion_sweep/main_k11_s10.py` |  |
| 0.73 | 11/15 | 11 | 1.5949s | 0.0812s | 1 | 8 | yes | 1.5402s | 1.6456s | `detyped_files/pystone/advanced/proportion_sweep/main_k11_s11.py` |  |
| 0.73 | 11/15 | 12 | 0.9879s | 0.0232s | 1 | 8 | yes | 0.9713s | 1.0014s | `detyped_files/pystone/advanced/proportion_sweep/main_k11_s12.py` |  |
| 0.73 | 11/15 | 13 | 1.8107s | 0.0995s | 1 | 8 | yes | 1.7525s | 1.8789s | `detyped_files/pystone/advanced/proportion_sweep/main_k11_s13.py` |  |
| 0.73 | 11/15 | 14 | 1.9304s | 0.0788s | 1 | 8 | yes | 1.8750s | 1.9754s | `detyped_files/pystone/advanced/proportion_sweep/main_k11_s14.py` |  |
| 0.73 | 11/15 | 15 | 1.4993s | 0.0702s | 1 | 8 | yes | 1.4533s | 1.5447s | `detyped_files/pystone/advanced/proportion_sweep/main_k11_s15.py` |  |
| 0.73 | 11/15 | 16 | 1.9386s | 0.1099s | 1 | 8 | yes | 1.8656s | 2.0074s | `detyped_files/pystone/advanced/proportion_sweep/main_k11_s16.py` |  |
| 0.73 | 11/15 | 17 | 1.0887s | 0.0824s | 1 | 8 | yes | 1.0361s | 1.1416s | `detyped_files/pystone/advanced/proportion_sweep/main_k11_s17.py` |  |
| 0.73 | 11/15 | 18 | 1.8657s | 0.0714s | 1 | 8 | yes | 1.8208s | 1.9132s | `detyped_files/pystone/advanced/proportion_sweep/main_k11_s18.py` |  |
| 0.73 | 11/15 | 19 | 1.0814s | 0.0646s | 1 | 8 | yes | 1.0372s | 1.1205s | `detyped_files/pystone/advanced/proportion_sweep/main_k11_s19.py` |  |
| 0.73 | 11/15 | 20 | 0.8347s | 0.0476s | 1 | 8 | yes | 0.8066s | 0.8684s | `detyped_files/pystone/advanced/proportion_sweep/main_k11_s20.py` |  |
| 0.80 | 12/15 | 1 | 1.9761s | 0.0839s | 1 | 8 | yes | 1.9260s | 2.0340s | `detyped_files/pystone/advanced/proportion_sweep/main_k12_s01.py` |  |
| 0.80 | 12/15 | 2 | 1.0680s | 0.0941s | 1 | 8 | yes | 1.0116s | 1.1316s | `detyped_files/pystone/advanced/proportion_sweep/main_k12_s02.py` |  |
| 0.80 | 12/15 | 3 | 1.8914s | 0.0494s | 1 | 8 | yes | 1.8595s | 1.9227s | `detyped_files/pystone/advanced/proportion_sweep/main_k12_s03.py` |  |
| 0.80 | 12/15 | 4 | 1.9379s | 0.0581s | 1 | 8 | yes | 1.9024s | 1.9775s | `detyped_files/pystone/advanced/proportion_sweep/main_k12_s04.py` |  |
| 0.80 | 12/15 | 5 | 1.1062s | 0.0956s | 1 | 8 | yes | 1.0496s | 1.1720s | `detyped_files/pystone/advanced/proportion_sweep/main_k12_s05.py` |  |
| 0.80 | 12/15 | 6 | 1.9454s | 0.1556s | 1 | 8 | yes | 1.8529s | 2.0515s | `detyped_files/pystone/advanced/proportion_sweep/main_k12_s06.py` |  |
| 0.80 | 12/15 | 7 | 1.6305s | 0.1318s | 1 | 8 | yes | 1.5483s | 1.7170s | `detyped_files/pystone/advanced/proportion_sweep/main_k12_s07.py` |  |
| 0.80 | 12/15 | 8 | 1.1177s | 0.0237s | 1 | 8 | yes | 1.1031s | 1.1333s | `detyped_files/pystone/advanced/proportion_sweep/main_k12_s08.py` |  |
| 0.80 | 12/15 | 9 | 1.9302s | 0.0553s | 1 | 8 | yes | 1.8962s | 1.9667s | `detyped_files/pystone/advanced/proportion_sweep/main_k12_s09.py` |  |
| 0.80 | 12/15 | 10 | 1.7778s | 0.0820s | 1 | 8 | yes | 1.7247s | 1.8306s | `detyped_files/pystone/advanced/proportion_sweep/main_k12_s10.py` |  |
| 0.80 | 12/15 | 11 | 1.9098s | 0.0599s | 1 | 8 | yes | 1.8713s | 1.9492s | `detyped_files/pystone/advanced/proportion_sweep/main_k12_s11.py` |  |
| 0.80 | 12/15 | 12 | 1.7659s | 0.1018s | 1 | 8 | yes | 1.7023s | 1.8339s | `detyped_files/pystone/advanced/proportion_sweep/main_k12_s12.py` |  |
| 0.80 | 12/15 | 13 | 1.0875s | 0.0655s | 1 | 8 | yes | 1.0444s | 1.1288s | `detyped_files/pystone/advanced/proportion_sweep/main_k12_s13.py` |  |
| 0.80 | 12/15 | 14 | 1.5861s | 0.0382s | 1 | 8 | yes | 1.5617s | 1.6114s | `detyped_files/pystone/advanced/proportion_sweep/main_k12_s14.py` |  |
| 0.80 | 12/15 | 15 | 1.6391s | 0.1092s | 1 | 8 | yes | 1.5742s | 1.7173s | `detyped_files/pystone/advanced/proportion_sweep/main_k12_s15.py` |  |
| 0.80 | 12/15 | 16 | 1.9520s | 0.0799s | 1 | 8 | yes | 1.9046s | 2.0063s | `detyped_files/pystone/advanced/proportion_sweep/main_k12_s16.py` |  |
| 0.80 | 12/15 | 17 | 1.8041s | 0.0844s | 1 | 8 | yes | 1.7513s | 1.8612s | `detyped_files/pystone/advanced/proportion_sweep/main_k12_s17.py` |  |
| 0.80 | 12/15 | 18 | 1.9284s | 0.0673s | 1 | 8 | yes | 1.8907s | 1.9750s | `detyped_files/pystone/advanced/proportion_sweep/main_k12_s18.py` |  |
| 0.80 | 12/15 | 19 | 1.9184s | 0.0606s | 1 | 8 | yes | 1.8777s | 1.9550s | `detyped_files/pystone/advanced/proportion_sweep/main_k12_s19.py` |  |
| 0.80 | 12/15 | 20 | 1.9597s | 0.0524s | 1 | 8 | yes | 1.9267s | 1.9935s | `detyped_files/pystone/advanced/proportion_sweep/main_k12_s20.py` |  |
| 0.87 | 13/15 | 1 | 1.9451s | 0.0523s | 1 | 8 | yes | 1.9095s | 1.9772s | `detyped_files/pystone/advanced/proportion_sweep/main_k13_s01.py` |  |
| 0.87 | 13/15 | 2 | 1.6239s | 0.0332s | 1 | 8 | yes | 1.6026s | 1.6460s | `detyped_files/pystone/advanced/proportion_sweep/main_k13_s02.py` |  |
| 0.87 | 13/15 | 3 | 1.7486s | 0.0799s | 1 | 8 | yes | 1.6928s | 1.7949s | `detyped_files/pystone/advanced/proportion_sweep/main_k13_s03.py` |  |
| 0.87 | 13/15 | 4 | 1.9178s | 0.0651s | 1 | 8 | yes | 1.8725s | 1.9560s | `detyped_files/pystone/advanced/proportion_sweep/main_k13_s04.py` |  |
| 0.87 | 13/15 | 5 | 1.9869s | 0.1315s | 1 | 8 | yes | 1.9043s | 2.0733s | `detyped_files/pystone/advanced/proportion_sweep/main_k13_s05.py` |  |
| 0.87 | 13/15 | 6 | 1.7763s | 0.0854s | 1 | 8 | yes | 1.7190s | 1.8285s | `detyped_files/pystone/advanced/proportion_sweep/main_k13_s06.py` |  |
| 0.87 | 13/15 | 7 | 1.9267s | 0.0246s | 1 | 8 | yes | 1.9108s | 1.9423s | `detyped_files/pystone/advanced/proportion_sweep/main_k13_s07.py` |  |
| 0.87 | 13/15 | 8 | 1.8988s | 0.0837s | 1 | 8 | yes | 1.8465s | 1.9552s | `detyped_files/pystone/advanced/proportion_sweep/main_k13_s08.py` |  |
| 0.87 | 13/15 | 9 | 1.0501s | 0.0637s | 1 | 8 | yes | 1.0076s | 1.0894s | `detyped_files/pystone/advanced/proportion_sweep/main_k13_s09.py` |  |
| 0.87 | 13/15 | 10 | 1.9180s | 0.0300s | 1 | 8 | yes | 1.8982s | 1.9363s | `detyped_files/pystone/advanced/proportion_sweep/main_k13_s10.py` |  |
| 0.87 | 13/15 | 11 | 1.9465s | 0.0692s | 1 | 8 | yes | 1.9001s | 1.9889s | `detyped_files/pystone/advanced/proportion_sweep/main_k13_s11.py` |  |
| 0.87 | 13/15 | 12 | 1.9066s | 0.1027s | 1 | 8 | yes | 1.8399s | 1.9716s | `detyped_files/pystone/advanced/proportion_sweep/main_k13_s12.py` |  |
| 0.87 | 13/15 | 13 | 1.9504s | 0.1171s | 1 | 8 | yes | 1.8782s | 2.0273s | `detyped_files/pystone/advanced/proportion_sweep/main_k13_s13.py` |  |
| 0.87 | 13/15 | 14 | 1.9457s | 0.1176s | 1 | 8 | yes | 1.8758s | 2.0250s | `detyped_files/pystone/advanced/proportion_sweep/main_k13_s14.py` |  |
| 0.87 | 13/15 | 15 | 1.9069s | 0.0905s | 1 | 8 | yes | 1.8508s | 1.9671s | `detyped_files/pystone/advanced/proportion_sweep/main_k13_s15.py` |  |
| 0.87 | 13/15 | 16 | 1.0975s | 0.0694s | 1 | 8 | yes | 1.0520s | 1.1422s | `detyped_files/pystone/advanced/proportion_sweep/main_k13_s16.py` |  |
| 0.87 | 13/15 | 17 | 0.9397s | 0.0448s | 1 | 8 | yes | 0.9104s | 0.9683s | `detyped_files/pystone/advanced/proportion_sweep/main_k13_s17.py` |  |
| 0.87 | 13/15 | 18 | 1.0654s | 0.0477s | 1 | 8 | yes | 1.0329s | 1.0929s | `detyped_files/pystone/advanced/proportion_sweep/main_k13_s18.py` |  |
| 0.87 | 13/15 | 19 | 1.9650s | 0.0811s | 1 | 8 | yes | 1.9176s | 2.0213s | `detyped_files/pystone/advanced/proportion_sweep/main_k13_s19.py` |  |
| 0.87 | 13/15 | 20 | 1.7820s | 0.0997s | 1 | 8 | yes | 1.7203s | 1.8460s | `detyped_files/pystone/advanced/proportion_sweep/main_k13_s20.py` |  |
| 0.93 | 14/15 | 1 | 1.9081s | 0.1172s | 1 | 8 | yes | 1.8308s | 1.9848s | `detyped_files/pystone/advanced/proportion_sweep/main_k14_s01.py` |  |
| 0.93 | 14/15 | 2 | 1.9281s | 0.0541s | 1 | 8 | yes | 1.8924s | 1.9620s | `detyped_files/pystone/advanced/proportion_sweep/main_k14_s02.py` |  |
| 0.93 | 14/15 | 3 | 1.9228s | 0.0713s | 1 | 8 | yes | 1.8785s | 1.9710s | `detyped_files/pystone/advanced/proportion_sweep/main_k14_s03.py` |  |
| 0.93 | 14/15 | 4 | 1.9291s | 0.0910s | 1 | 8 | yes | 1.8666s | 1.9849s | `detyped_files/pystone/advanced/proportion_sweep/main_k14_s04.py` |  |
| 0.93 | 14/15 | 5 | 1.9234s | 0.0563s | 1 | 8 | yes | 1.8897s | 1.9635s | `detyped_files/pystone/advanced/proportion_sweep/main_k14_s05.py` |  |
| 0.93 | 14/15 | 6 | 1.8721s | 0.0742s | 1 | 8 | yes | 1.8247s | 1.9176s | `detyped_files/pystone/advanced/proportion_sweep/main_k14_s06.py` |  |
| 0.93 | 14/15 | 7 | 1.8727s | 0.0813s | 1 | 8 | yes | 1.8182s | 1.9241s | `detyped_files/pystone/advanced/proportion_sweep/main_k14_s07.py` |  |
| 0.93 | 14/15 | 8 | 1.9416s | 0.0824s | 1 | 8 | yes | 1.8900s | 1.9953s | `detyped_files/pystone/advanced/proportion_sweep/main_k14_s08.py` |  |
| 0.93 | 14/15 | 9 | 1.1134s | 0.0733s | 1 | 8 | yes | 1.0736s | 1.1677s | `detyped_files/pystone/advanced/proportion_sweep/main_k14_s09.py` |  |
| 0.93 | 14/15 | 10 | 1.9659s | 0.1198s | 1 | 8 | yes | 1.8970s | 2.0493s | `detyped_files/pystone/advanced/proportion_sweep/main_k14_s10.py` |  |
| 0.93 | 14/15 | 11 | 1.6337s | 0.0922s | 1 | 8 | yes | 1.5685s | 1.6858s | `detyped_files/pystone/advanced/proportion_sweep/main_k14_s11.py` |  |
| 0.93 | 14/15 | 12 | 1.7614s | 0.0759s | 1 | 8 | yes | 1.7079s | 1.8064s | `detyped_files/pystone/advanced/proportion_sweep/main_k14_s12.py` |  |
| 0.93 | 14/15 | 13 | 1.9379s | 0.0633s | 1 | 8 | yes | 1.8976s | 1.9787s | `detyped_files/pystone/advanced/proportion_sweep/main_k14_s13.py` |  |
| 0.93 | 14/15 | 14 | 1.9319s | 0.0595s | 1 | 8 | yes | 1.8932s | 1.9696s | `detyped_files/pystone/advanced/proportion_sweep/main_k14_s14.py` |  |
| 0.93 | 14/15 | 15 | 1.9452s | 0.0618s | 1 | 8 | yes | 1.9067s | 1.9857s | `detyped_files/pystone/advanced/proportion_sweep/main_k14_s15.py` |  |
| 1.00 | 15/15 | 1 | 1.9370s | 0.0830s | 1 | 8 | yes | 1.8849s | 1.9923s | `detyped_files/pystone/advanced/proportion_sweep/main_k15_s01.py` |  |

## pystone/shallow

- Detypable targets: `15`
- Total runs: `272`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/15 | 1 | 0.6288s | 0.6288s | 0.6288s | 1.0 | yes | ok |
| 0.07 | 1/15 | 15 | 0.7124s | 0.6378s | 1.0526s | 1.0 | yes | ok |
| 0.13 | 2/15 | 20 | 0.7609s | 0.6316s | 1.1038s | 1.0 | yes | ok |
| 0.20 | 3/15 | 20 | 0.9010s | 0.6667s | 1.3438s | 1.0 | yes | ok |
| 0.27 | 4/15 | 20 | 0.8927s | 0.6444s | 1.1962s | 1.0 | yes | ok |
| 0.33 | 5/15 | 20 | 1.0193s | 0.6422s | 1.4786s | 1.0 | yes | ok |
| 0.40 | 6/15 | 20 | 1.0243s | 0.6243s | 1.4660s | 1.0 | yes | ok |
| 0.47 | 7/15 | 20 | 1.0088s | 0.6756s | 1.5513s | 1.1 | yes | ok |
| 0.53 | 8/15 | 20 | 0.9684s | 0.6472s | 1.4659s | 1.0 | yes | ok |
| 0.60 | 9/15 | 20 | 1.0700s | 0.7808s | 1.5300s | 1.0 | yes | ok |
| 0.67 | 10/15 | 20 | 1.1748s | 0.8082s | 1.5084s | 1.0 | yes | ok |
| 0.73 | 11/15 | 20 | 1.2692s | 0.9376s | 1.5309s | 1.0 | yes | ok |
| 0.80 | 12/15 | 20 | 1.2265s | 0.7996s | 1.5136s | 1.0 | yes | ok |
| 0.87 | 13/15 | 20 | 1.3887s | 1.0504s | 1.5788s | 1.0 | yes | ok |
| 0.93 | 14/15 | 15 | 1.4474s | 1.0852s | 1.5373s | 1.0 | yes | ok |
| 1.00 | 15/15 | 1 | 1.4967s | 1.4967s | 1.4967s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/15 | 1 | 0.6288s | 0.0634s | 1 | 8 | yes | 0.5873s | 0.6696s | `detyped_files/pystone/shallow/proportion_sweep/main_k00_s01.py` |  |
| 0.07 | 1/15 | 1 | 0.9367s | 0.0372s | 1 | 8 | yes | 0.9146s | 0.9626s | `detyped_files/pystone/shallow/proportion_sweep/main_k01_s01.py` |  |
| 0.07 | 1/15 | 2 | 0.6489s | 0.0798s | 1 | 8 | yes | 0.5985s | 0.7012s | `detyped_files/pystone/shallow/proportion_sweep/main_k01_s02.py` |  |
| 0.07 | 1/15 | 3 | 0.6475s | 0.0565s | 1 | 8 | yes | 0.6083s | 0.6800s | `detyped_files/pystone/shallow/proportion_sweep/main_k01_s03.py` |  |
| 0.07 | 1/15 | 4 | 0.7995s | 0.0265s | 1 | 8 | yes | 0.7820s | 0.8158s | `detyped_files/pystone/shallow/proportion_sweep/main_k01_s04.py` |  |
| 0.07 | 1/15 | 5 | 0.6452s | 0.0855s | 1 | 8 | yes | 0.5881s | 0.6996s | `detyped_files/pystone/shallow/proportion_sweep/main_k01_s05.py` |  |
| 0.07 | 1/15 | 6 | 0.6378s | 0.0605s | 1 | 8 | yes | 0.5995s | 0.6772s | `detyped_files/pystone/shallow/proportion_sweep/main_k01_s06.py` |  |
| 0.07 | 1/15 | 7 | 0.6636s | 0.0441s | 1 | 8 | yes | 0.6315s | 0.6888s | `detyped_files/pystone/shallow/proportion_sweep/main_k01_s07.py` |  |
| 0.07 | 1/15 | 8 | 0.6469s | 0.0526s | 1 | 8 | yes | 0.6101s | 0.6776s | `detyped_files/pystone/shallow/proportion_sweep/main_k01_s08.py` |  |
| 0.07 | 1/15 | 9 | 1.0526s | 0.0586s | 1 | 8 | yes | 1.0123s | 1.0882s | `detyped_files/pystone/shallow/proportion_sweep/main_k01_s09.py` |  |
| 0.07 | 1/15 | 10 | 0.6649s | 0.0706s | 1 | 8 | yes | 0.6178s | 0.7081s | `detyped_files/pystone/shallow/proportion_sweep/main_k01_s10.py` |  |
| 0.07 | 1/15 | 11 | 0.6520s | 0.0505s | 1 | 8 | yes | 0.6188s | 0.6836s | `detyped_files/pystone/shallow/proportion_sweep/main_k01_s11.py` |  |
| 0.07 | 1/15 | 12 | 0.6643s | 0.0479s | 1 | 8 | yes | 0.6325s | 0.6944s | `detyped_files/pystone/shallow/proportion_sweep/main_k01_s12.py` |  |
| 0.07 | 1/15 | 13 | 0.6639s | 0.0559s | 1 | 8 | yes | 0.6267s | 0.6973s | `detyped_files/pystone/shallow/proportion_sweep/main_k01_s13.py` |  |
| 0.07 | 1/15 | 14 | 0.6933s | 0.0380s | 1 | 8 | yes | 0.6672s | 0.7163s | `detyped_files/pystone/shallow/proportion_sweep/main_k01_s14.py` |  |
| 0.07 | 1/15 | 15 | 0.6687s | 0.0678s | 1 | 8 | yes | 0.6190s | 0.7061s | `detyped_files/pystone/shallow/proportion_sweep/main_k01_s15.py` |  |
| 0.13 | 2/15 | 1 | 0.6764s | 0.0923s | 1 | 8 | yes | 0.6166s | 0.7341s | `detyped_files/pystone/shallow/proportion_sweep/main_k02_s01.py` |  |
| 0.13 | 2/15 | 2 | 1.0947s | 0.0716s | 1 | 8 | yes | 1.0467s | 1.1397s | `detyped_files/pystone/shallow/proportion_sweep/main_k02_s02.py` |  |
| 0.13 | 2/15 | 3 | 1.1038s | 0.0348s | 1 | 8 | yes | 1.0816s | 1.1256s | `detyped_files/pystone/shallow/proportion_sweep/main_k02_s03.py` |  |
| 0.13 | 2/15 | 4 | 0.6980s | 0.0498s | 1 | 8 | yes | 0.6632s | 0.7271s | `detyped_files/pystone/shallow/proportion_sweep/main_k02_s04.py` |  |
| 0.13 | 2/15 | 5 | 0.6754s | 0.0399s | 1 | 8 | yes | 0.6505s | 0.7006s | `detyped_files/pystone/shallow/proportion_sweep/main_k02_s05.py` |  |
| 0.13 | 2/15 | 6 | 0.7903s | 0.0615s | 1 | 8 | yes | 0.7489s | 0.8283s | `detyped_files/pystone/shallow/proportion_sweep/main_k02_s06.py` |  |
| 0.13 | 2/15 | 7 | 0.6815s | 0.0335s | 1 | 8 | yes | 0.6601s | 0.7034s | `detyped_files/pystone/shallow/proportion_sweep/main_k02_s07.py` |  |
| 0.13 | 2/15 | 8 | 0.7947s | 0.0825s | 1 | 8 | yes | 0.7389s | 0.8452s | `detyped_files/pystone/shallow/proportion_sweep/main_k02_s08.py` |  |
| 0.13 | 2/15 | 9 | 0.9601s | 0.0649s | 1 | 8 | yes | 0.9131s | 0.9954s | `detyped_files/pystone/shallow/proportion_sweep/main_k02_s09.py` |  |
| 0.13 | 2/15 | 10 | 0.6316s | 0.0668s | 1 | 8 | yes | 0.5866s | 0.6744s | `detyped_files/pystone/shallow/proportion_sweep/main_k02_s10.py` |  |
| 0.13 | 2/15 | 11 | 0.6574s | 0.0470s | 1 | 8 | yes | 0.6270s | 0.6881s | `detyped_files/pystone/shallow/proportion_sweep/main_k02_s11.py` |  |
| 0.13 | 2/15 | 12 | 0.6709s | 0.0611s | 1 | 8 | yes | 0.6306s | 0.7092s | `detyped_files/pystone/shallow/proportion_sweep/main_k02_s12.py` |  |
| 0.13 | 2/15 | 13 | 0.6969s | 0.0432s | 1 | 8 | yes | 0.6756s | 0.7285s | `detyped_files/pystone/shallow/proportion_sweep/main_k02_s13.py` |  |
| 0.13 | 2/15 | 14 | 0.6766s | 0.0597s | 1 | 8 | yes | 0.6377s | 0.7150s | `detyped_files/pystone/shallow/proportion_sweep/main_k02_s14.py` |  |
| 0.13 | 2/15 | 15 | 1.0832s | 0.0751s | 1 | 8 | yes | 1.0333s | 1.1278s | `detyped_files/pystone/shallow/proportion_sweep/main_k02_s15.py` |  |
| 0.13 | 2/15 | 16 | 0.6617s | 0.0587s | 1 | 8 | yes | 0.6197s | 0.6961s | `detyped_files/pystone/shallow/proportion_sweep/main_k02_s16.py` |  |
| 0.13 | 2/15 | 17 | 0.6993s | 0.0496s | 1 | 8 | yes | 0.6713s | 0.7337s | `detyped_files/pystone/shallow/proportion_sweep/main_k02_s17.py` |  |
| 0.13 | 2/15 | 18 | 0.6726s | 0.0648s | 1 | 8 | yes | 0.6291s | 0.7119s | `detyped_files/pystone/shallow/proportion_sweep/main_k02_s18.py` |  |
| 0.13 | 2/15 | 19 | 0.6448s | 0.0727s | 1 | 8 | yes | 0.5954s | 0.6904s | `detyped_files/pystone/shallow/proportion_sweep/main_k02_s19.py` |  |
| 0.13 | 2/15 | 20 | 0.6481s | 0.0884s | 1 | 8 | yes | 0.5954s | 0.7085s | `detyped_files/pystone/shallow/proportion_sweep/main_k02_s20.py` |  |
| 0.20 | 3/15 | 1 | 0.8369s | 0.0755s | 1 | 8 | yes | 0.7892s | 0.8873s | `detyped_files/pystone/shallow/proportion_sweep/main_k03_s01.py` |  |
| 0.20 | 3/15 | 2 | 0.6667s | 0.0499s | 1 | 8 | yes | 0.6350s | 0.7007s | `detyped_files/pystone/shallow/proportion_sweep/main_k03_s02.py` |  |
| 0.20 | 3/15 | 3 | 1.0927s | 0.0855s | 1 | 8 | yes | 1.0349s | 1.1459s | `detyped_files/pystone/shallow/proportion_sweep/main_k03_s03.py` |  |
| 0.20 | 3/15 | 4 | 0.7314s | 0.0814s | 1 | 8 | yes | 0.6826s | 0.7861s | `detyped_files/pystone/shallow/proportion_sweep/main_k03_s04.py` |  |
| 0.20 | 3/15 | 5 | 0.8347s | 0.0672s | 1 | 8 | yes | 0.7898s | 0.8751s | `detyped_files/pystone/shallow/proportion_sweep/main_k03_s05.py` |  |
| 0.20 | 3/15 | 6 | 0.9942s | 0.0839s | 1 | 8 | yes | 0.9430s | 1.0499s | `detyped_files/pystone/shallow/proportion_sweep/main_k03_s06.py` |  |
| 0.20 | 3/15 | 7 | 1.0625s | 0.0336s | 1 | 8 | yes | 1.0385s | 1.0806s | `detyped_files/pystone/shallow/proportion_sweep/main_k03_s07.py` |  |
| 0.20 | 3/15 | 8 | 1.0895s | 0.0930s | 1 | 8 | yes | 1.0354s | 1.1531s | `detyped_files/pystone/shallow/proportion_sweep/main_k03_s08.py` |  |
| 0.20 | 3/15 | 9 | 0.6867s | 0.0343s | 1 | 8 | yes | 0.6663s | 0.7103s | `detyped_files/pystone/shallow/proportion_sweep/main_k03_s09.py` |  |
| 0.20 | 3/15 | 10 | 0.6914s | 0.0590s | 1 | 8 | yes | 0.6533s | 0.7301s | `detyped_files/pystone/shallow/proportion_sweep/main_k03_s10.py` |  |
| 0.20 | 3/15 | 11 | 0.8224s | 0.0146s | 1 | 8 | yes | 0.8124s | 0.8316s | `detyped_files/pystone/shallow/proportion_sweep/main_k03_s11.py` |  |
| 0.20 | 3/15 | 12 | 1.0205s | 0.0480s | 1 | 8 | yes | 0.9887s | 1.0504s | `detyped_files/pystone/shallow/proportion_sweep/main_k03_s12.py` |  |
| 0.20 | 3/15 | 13 | 1.2049s | 0.0339s | 1 | 8 | yes | 1.1819s | 1.2254s | `detyped_files/pystone/shallow/proportion_sweep/main_k03_s13.py` |  |
| 0.20 | 3/15 | 14 | 0.6766s | 0.0645s | 1 | 8 | yes | 0.6316s | 0.7143s | `detyped_files/pystone/shallow/proportion_sweep/main_k03_s14.py` |  |
| 0.20 | 3/15 | 15 | 1.1248s | 0.1060s | 1 | 8 | yes | 1.0561s | 1.1934s | `detyped_files/pystone/shallow/proportion_sweep/main_k03_s15.py` |  |
| 0.20 | 3/15 | 16 | 0.6747s | 0.0538s | 1 | 8 | yes | 0.6384s | 0.7088s | `detyped_files/pystone/shallow/proportion_sweep/main_k03_s16.py` |  |
| 0.20 | 3/15 | 17 | 0.9519s | 0.0316s | 1 | 8 | yes | 0.9303s | 0.9716s | `detyped_files/pystone/shallow/proportion_sweep/main_k03_s17.py` |  |
| 0.20 | 3/15 | 18 | 0.6807s | 0.0418s | 1 | 8 | yes | 0.6527s | 0.7068s | `detyped_files/pystone/shallow/proportion_sweep/main_k03_s18.py` |  |
| 0.20 | 3/15 | 19 | 0.8333s | 0.0821s | 1 | 8 | yes | 0.7762s | 0.8823s | `detyped_files/pystone/shallow/proportion_sweep/main_k03_s19.py` |  |
| 0.20 | 3/15 | 20 | 1.3438s | 0.0921s | 1 | 8 | yes | 1.2822s | 1.4014s | `detyped_files/pystone/shallow/proportion_sweep/main_k03_s20.py` |  |
| 0.27 | 4/15 | 1 | 0.8403s | 0.0597s | 1 | 8 | yes | 0.8047s | 0.8816s | `detyped_files/pystone/shallow/proportion_sweep/main_k04_s01.py` |  |
| 0.27 | 4/15 | 2 | 1.0513s | 0.0538s | 1 | 8 | yes | 1.0160s | 1.0853s | `detyped_files/pystone/shallow/proportion_sweep/main_k04_s02.py` |  |
| 0.27 | 4/15 | 3 | 0.9591s | 0.0939s | 1 | 8 | yes | 0.9006s | 1.0214s | `detyped_files/pystone/shallow/proportion_sweep/main_k04_s03.py` |  |
| 0.27 | 4/15 | 4 | 0.6444s | 0.0610s | 1 | 8 | yes | 0.6043s | 0.6840s | `detyped_files/pystone/shallow/proportion_sweep/main_k04_s04.py` |  |
| 0.27 | 4/15 | 5 | 0.6564s | 0.0613s | 1 | 8 | yes | 0.6178s | 0.6940s | `detyped_files/pystone/shallow/proportion_sweep/main_k04_s05.py` |  |
| 0.27 | 4/15 | 6 | 0.6769s | 0.0535s | 1 | 8 | yes | 0.6381s | 0.7067s | `detyped_files/pystone/shallow/proportion_sweep/main_k04_s06.py` |  |
| 0.27 | 4/15 | 7 | 1.1962s | 0.0836s | 1 | 8 | yes | 1.1447s | 1.2530s | `detyped_files/pystone/shallow/proportion_sweep/main_k04_s07.py` |  |
| 0.27 | 4/15 | 8 | 0.6898s | 0.0636s | 1 | 8 | yes | 0.6461s | 0.7284s | `detyped_files/pystone/shallow/proportion_sweep/main_k04_s08.py` |  |
| 0.27 | 4/15 | 9 | 0.6948s | 0.0447s | 1 | 8 | yes | 0.6731s | 0.7271s | `detyped_files/pystone/shallow/proportion_sweep/main_k04_s09.py` |  |
| 0.27 | 4/15 | 10 | 0.6562s | 0.0685s | 1 | 8 | yes | 0.6093s | 0.6960s | `detyped_files/pystone/shallow/proportion_sweep/main_k04_s10.py` |  |
| 0.27 | 4/15 | 11 | 0.9431s | 0.0802s | 1 | 8 | yes | 0.8938s | 0.9976s | `detyped_files/pystone/shallow/proportion_sweep/main_k04_s11.py` |  |
| 0.27 | 4/15 | 12 | 1.1018s | 0.0861s | 1 | 8 | yes | 1.0476s | 1.1586s | `detyped_files/pystone/shallow/proportion_sweep/main_k04_s12.py` |  |
| 0.27 | 4/15 | 13 | 0.6788s | 0.0422s | 1 | 8 | yes | 0.6507s | 0.7047s | `detyped_files/pystone/shallow/proportion_sweep/main_k04_s13.py` |  |
| 0.27 | 4/15 | 14 | 1.1497s | 0.0550s | 1 | 8 | yes | 1.1142s | 1.1860s | `detyped_files/pystone/shallow/proportion_sweep/main_k04_s14.py` |  |
| 0.27 | 4/15 | 15 | 0.9595s | 0.0642s | 1 | 8 | yes | 0.9149s | 0.9956s | `detyped_files/pystone/shallow/proportion_sweep/main_k04_s15.py` |  |
| 0.27 | 4/15 | 16 | 1.1035s | 0.0998s | 1 | 8 | yes | 1.0460s | 1.1721s | `detyped_files/pystone/shallow/proportion_sweep/main_k04_s16.py` |  |
| 0.27 | 4/15 | 17 | 0.7618s | 0.0636s | 1 | 8 | yes | 0.7210s | 0.8004s | `detyped_files/pystone/shallow/proportion_sweep/main_k04_s17.py` |  |
| 0.27 | 4/15 | 18 | 1.0836s | 0.1034s | 1 | 8 | yes | 1.0163s | 1.1496s | `detyped_files/pystone/shallow/proportion_sweep/main_k04_s18.py` |  |
| 0.27 | 4/15 | 19 | 0.9371s | 0.0514s | 1 | 8 | yes | 0.9011s | 0.9674s | `detyped_files/pystone/shallow/proportion_sweep/main_k04_s19.py` |  |
| 0.27 | 4/15 | 20 | 1.0704s | 0.1169s | 1 | 8 | yes | 0.9980s | 1.1507s | `detyped_files/pystone/shallow/proportion_sweep/main_k04_s20.py` |  |
| 0.33 | 5/15 | 1 | 0.6597s | 0.0504s | 1 | 8 | yes | 0.6257s | 0.6910s | `detyped_files/pystone/shallow/proportion_sweep/main_k05_s01.py` |  |
| 0.33 | 5/15 | 2 | 0.9426s | 0.1029s | 1 | 8 | yes | 0.8789s | 1.0128s | `detyped_files/pystone/shallow/proportion_sweep/main_k05_s02.py` |  |
| 0.33 | 5/15 | 3 | 0.8160s | 0.0652s | 1 | 8 | yes | 0.7727s | 0.8562s | `detyped_files/pystone/shallow/proportion_sweep/main_k05_s03.py` |  |
| 0.33 | 5/15 | 4 | 0.6422s | 0.0701s | 1 | 8 | yes | 0.5979s | 0.6860s | `detyped_files/pystone/shallow/proportion_sweep/main_k05_s04.py` |  |
| 0.33 | 5/15 | 5 | 1.4026s | 0.0681s | 1 | 8 | yes | 1.3602s | 1.4490s | `detyped_files/pystone/shallow/proportion_sweep/main_k05_s05.py` |  |
| 0.33 | 5/15 | 6 | 1.0783s | 0.0490s | 1 | 8 | yes | 1.0511s | 1.1125s | `detyped_files/pystone/shallow/proportion_sweep/main_k05_s06.py` |  |
| 0.33 | 5/15 | 7 | 0.9727s | 0.1121s | 1 | 8 | yes | 0.8980s | 1.0421s | `detyped_files/pystone/shallow/proportion_sweep/main_k05_s07.py` |  |
| 0.33 | 5/15 | 8 | 1.0971s | 0.0310s | 1 | 8 | yes | 1.0777s | 1.1171s | `detyped_files/pystone/shallow/proportion_sweep/main_k05_s08.py` |  |
| 0.33 | 5/15 | 9 | 1.0260s | 0.0706s | 1 | 8 | yes | 0.9831s | 1.0755s | `detyped_files/pystone/shallow/proportion_sweep/main_k05_s09.py` |  |
| 0.33 | 5/15 | 10 | 1.1175s | 0.0787s | 1 | 8 | yes | 1.0626s | 1.1630s | `detyped_files/pystone/shallow/proportion_sweep/main_k05_s10.py` |  |
| 0.33 | 5/15 | 11 | 0.8450s | 0.0522s | 1 | 8 | yes | 0.8164s | 0.8812s | `detyped_files/pystone/shallow/proportion_sweep/main_k05_s11.py` |  |
| 0.33 | 5/15 | 12 | 0.8597s | 0.0477s | 1 | 8 | yes | 0.8294s | 0.8917s | `detyped_files/pystone/shallow/proportion_sweep/main_k05_s12.py` |  |
| 0.33 | 5/15 | 13 | 0.9808s | 0.0915s | 1 | 8 | yes | 0.9195s | 1.0379s | `detyped_files/pystone/shallow/proportion_sweep/main_k05_s13.py` |  |
| 0.33 | 5/15 | 14 | 1.2115s | 0.0873s | 1 | 8 | yes | 1.1539s | 1.2682s | `detyped_files/pystone/shallow/proportion_sweep/main_k05_s14.py` |  |
| 0.33 | 5/15 | 15 | 0.6614s | 0.0670s | 1 | 8 | yes | 0.6158s | 0.7026s | `detyped_files/pystone/shallow/proportion_sweep/main_k05_s15.py` |  |
| 0.33 | 5/15 | 16 | 1.4198s | 0.0853s | 1 | 8 | yes | 1.3687s | 1.4793s | `detyped_files/pystone/shallow/proportion_sweep/main_k05_s16.py` |  |
| 0.33 | 5/15 | 17 | 0.9686s | 0.0592s | 1 | 8 | yes | 0.9278s | 1.0026s | `detyped_files/pystone/shallow/proportion_sweep/main_k05_s17.py` |  |
| 0.33 | 5/15 | 18 | 1.2260s | 0.0336s | 1 | 8 | yes | 1.2054s | 1.2489s | `detyped_files/pystone/shallow/proportion_sweep/main_k05_s18.py` |  |
| 0.33 | 5/15 | 19 | 1.4786s | 0.0707s | 1 | 8 | yes | 1.4337s | 1.5250s | `detyped_files/pystone/shallow/proportion_sweep/main_k05_s19.py` |  |
| 0.33 | 5/15 | 20 | 0.9789s | 0.0633s | 1 | 8 | yes | 0.9343s | 1.0147s | `detyped_files/pystone/shallow/proportion_sweep/main_k05_s20.py` |  |
| 0.40 | 6/15 | 1 | 1.1526s | 0.1025s | 1 | 8 | yes | 1.0892s | 1.2230s | `detyped_files/pystone/shallow/proportion_sweep/main_k06_s01.py` |  |
| 0.40 | 6/15 | 2 | 0.6243s | 0.0631s | 1 | 8 | yes | 0.5831s | 0.6657s | `detyped_files/pystone/shallow/proportion_sweep/main_k06_s02.py` |  |
| 0.40 | 6/15 | 3 | 0.8214s | 0.0568s | 1 | 8 | yes | 0.7834s | 0.8581s | `detyped_files/pystone/shallow/proportion_sweep/main_k06_s03.py` |  |
| 0.40 | 6/15 | 4 | 0.7774s | 0.0545s | 1 | 8 | yes | 0.7410s | 0.8117s | `detyped_files/pystone/shallow/proportion_sweep/main_k06_s04.py` |  |
| 0.40 | 6/15 | 5 | 0.6617s | 0.0743s | 1 | 8 | yes | 0.6094s | 0.7059s | `detyped_files/pystone/shallow/proportion_sweep/main_k06_s05.py` |  |
| 0.40 | 6/15 | 6 | 1.1692s | 0.0809s | 1 | 8 | yes | 1.1157s | 1.2205s | `detyped_files/pystone/shallow/proportion_sweep/main_k06_s06.py` |  |
| 0.40 | 6/15 | 7 | 1.3660s | 0.0923s | 1 | 8 | yes | 1.3099s | 1.4305s | `detyped_files/pystone/shallow/proportion_sweep/main_k06_s07.py` |  |
| 0.40 | 6/15 | 8 | 0.9702s | 0.0242s | 1 | 8 | yes | 0.9552s | 0.9867s | `detyped_files/pystone/shallow/proportion_sweep/main_k06_s08.py` |  |
| 0.40 | 6/15 | 9 | 0.9922s | 0.0814s | 1 | 8 | yes | 0.9505s | 1.0511s | `detyped_files/pystone/shallow/proportion_sweep/main_k06_s09.py` |  |
| 0.40 | 6/15 | 10 | 0.8118s | 0.0518s | 1 | 8 | yes | 0.7767s | 0.8432s | `detyped_files/pystone/shallow/proportion_sweep/main_k06_s10.py` |  |
| 0.40 | 6/15 | 11 | 1.0738s | 0.0793s | 1 | 8 | yes | 1.0256s | 1.1279s | `detyped_files/pystone/shallow/proportion_sweep/main_k06_s11.py` |  |
| 0.40 | 6/15 | 12 | 1.4660s | 0.0268s | 1 | 8 | yes | 1.4487s | 1.4839s | `detyped_files/pystone/shallow/proportion_sweep/main_k06_s12.py` |  |
| 0.40 | 6/15 | 13 | 1.0903s | 0.1063s | 1 | 8 | yes | 1.0292s | 1.1637s | `detyped_files/pystone/shallow/proportion_sweep/main_k06_s13.py` |  |
| 0.40 | 6/15 | 14 | 0.9897s | 0.0488s | 1 | 8 | yes | 0.9574s | 1.0212s | `detyped_files/pystone/shallow/proportion_sweep/main_k06_s14.py` |  |
| 0.40 | 6/15 | 15 | 1.1062s | 0.0693s | 1 | 8 | yes | 1.0656s | 1.1540s | `detyped_files/pystone/shallow/proportion_sweep/main_k06_s15.py` |  |
| 0.40 | 6/15 | 16 | 0.7897s | 0.0802s | 1 | 8 | yes | 0.7370s | 0.8408s | `detyped_files/pystone/shallow/proportion_sweep/main_k06_s16.py` |  |
| 0.40 | 6/15 | 17 | 1.0797s | 0.0430s | 1 | 8 | yes | 1.0506s | 1.1057s | `detyped_files/pystone/shallow/proportion_sweep/main_k06_s17.py` |  |
| 0.40 | 6/15 | 18 | 1.0922s | 0.0890s | 1 | 8 | yes | 1.0373s | 1.1512s | `detyped_files/pystone/shallow/proportion_sweep/main_k06_s18.py` |  |
| 0.40 | 6/15 | 19 | 1.3594s | 0.0771s | 1 | 8 | yes | 1.3104s | 1.4081s | `detyped_files/pystone/shallow/proportion_sweep/main_k06_s19.py` |  |
| 0.40 | 6/15 | 20 | 1.0928s | 0.1350s | 1 | 8 | yes | 1.0134s | 1.1851s | `detyped_files/pystone/shallow/proportion_sweep/main_k06_s20.py` |  |
| 0.47 | 7/15 | 1 | 0.9307s | 0.0694s | 1 | 8 | yes | 0.8851s | 0.9749s | `detyped_files/pystone/shallow/proportion_sweep/main_k07_s01.py` |  |
| 0.47 | 7/15 | 2 | 1.5513s | 0.0526s | 1 | 8 | yes | 1.5173s | 1.5854s | `detyped_files/pystone/shallow/proportion_sweep/main_k07_s02.py` |  |
| 0.47 | 7/15 | 3 | 0.6800s | 0.0839s | 2 | 16 | yes | 0.6399s | 0.7191s | `detyped_files/pystone/shallow/proportion_sweep/main_k07_s03.py` |  |
| 0.47 | 7/15 | 4 | 1.0936s | 0.0562s | 1 | 8 | yes | 1.0559s | 1.1283s | `detyped_files/pystone/shallow/proportion_sweep/main_k07_s04.py` |  |
| 0.47 | 7/15 | 5 | 1.4877s | 0.1135s | 1 | 8 | yes | 1.4144s | 1.5587s | `detyped_files/pystone/shallow/proportion_sweep/main_k07_s05.py` |  |
| 0.47 | 7/15 | 6 | 0.9485s | 0.1000s | 1 | 8 | yes | 0.8888s | 1.0161s | `detyped_files/pystone/shallow/proportion_sweep/main_k07_s06.py` |  |
| 0.47 | 7/15 | 7 | 0.9235s | 0.0737s | 1 | 8 | yes | 0.8766s | 0.9726s | `detyped_files/pystone/shallow/proportion_sweep/main_k07_s07.py` |  |
| 0.47 | 7/15 | 8 | 0.6967s | 0.0194s | 1 | 8 | yes | 0.6854s | 0.7102s | `detyped_files/pystone/shallow/proportion_sweep/main_k07_s08.py` |  |
| 0.47 | 7/15 | 9 | 1.3509s | 0.0525s | 1 | 8 | yes | 1.3137s | 1.3810s | `detyped_files/pystone/shallow/proportion_sweep/main_k07_s09.py` |  |
| 0.47 | 7/15 | 10 | 0.7046s | 0.0557s | 1 | 8 | yes | 0.6684s | 0.7413s | `detyped_files/pystone/shallow/proportion_sweep/main_k07_s10.py` |  |
| 0.47 | 7/15 | 11 | 0.8156s | 0.0583s | 1 | 8 | yes | 0.7772s | 0.8515s | `detyped_files/pystone/shallow/proportion_sweep/main_k07_s11.py` |  |
| 0.47 | 7/15 | 12 | 0.6756s | 0.0649s | 1 | 8 | yes | 0.6299s | 0.7153s | `detyped_files/pystone/shallow/proportion_sweep/main_k07_s12.py` |  |
| 0.47 | 7/15 | 13 | 0.9342s | 0.0647s | 1 | 8 | yes | 0.8912s | 0.9747s | `detyped_files/pystone/shallow/proportion_sweep/main_k07_s13.py` |  |
| 0.47 | 7/15 | 14 | 0.9938s | 0.1000s | 1 | 8 | yes | 0.9333s | 1.0625s | `detyped_files/pystone/shallow/proportion_sweep/main_k07_s14.py` |  |
| 0.47 | 7/15 | 15 | 0.6857s | 0.0141s | 1 | 8 | yes | 0.6761s | 0.6944s | `detyped_files/pystone/shallow/proportion_sweep/main_k07_s15.py` |  |
| 0.47 | 7/15 | 16 | 1.0604s | 0.0819s | 1 | 8 | yes | 1.0086s | 1.1149s | `detyped_files/pystone/shallow/proportion_sweep/main_k07_s16.py` |  |
| 0.47 | 7/15 | 17 | 1.0777s | 0.0728s | 1 | 8 | yes | 1.0296s | 1.1244s | `detyped_files/pystone/shallow/proportion_sweep/main_k07_s17.py` |  |
| 0.47 | 7/15 | 18 | 1.3800s | 0.0580s | 1 | 8 | yes | 1.3407s | 1.4167s | `detyped_files/pystone/shallow/proportion_sweep/main_k07_s18.py` |  |
| 0.47 | 7/15 | 19 | 1.0745s | 0.0912s | 1 | 8 | yes | 1.0156s | 1.1347s | `detyped_files/pystone/shallow/proportion_sweep/main_k07_s19.py` |  |
| 0.47 | 7/15 | 20 | 1.1100s | 0.0802s | 1 | 8 | yes | 1.0561s | 1.1596s | `detyped_files/pystone/shallow/proportion_sweep/main_k07_s20.py` |  |
| 0.53 | 8/15 | 1 | 0.6643s | 0.0594s | 1 | 8 | yes | 0.6238s | 0.7015s | `detyped_files/pystone/shallow/proportion_sweep/main_k08_s01.py` |  |
| 0.53 | 8/15 | 2 | 1.1320s | 0.1275s | 1 | 8 | yes | 1.0587s | 1.2182s | `detyped_files/pystone/shallow/proportion_sweep/main_k08_s02.py` |  |
| 0.53 | 8/15 | 3 | 1.4062s | 0.1100s | 1 | 8 | yes | 1.3381s | 1.4809s | `detyped_files/pystone/shallow/proportion_sweep/main_k08_s03.py` |  |
| 0.53 | 8/15 | 4 | 0.8025s | 0.0664s | 1 | 8 | yes | 0.7625s | 0.8482s | `detyped_files/pystone/shallow/proportion_sweep/main_k08_s04.py` |  |
| 0.53 | 8/15 | 5 | 0.8365s | 0.0576s | 1 | 8 | yes | 0.7997s | 0.8737s | `detyped_files/pystone/shallow/proportion_sweep/main_k08_s05.py` |  |
| 0.53 | 8/15 | 6 | 0.9365s | 0.0616s | 1 | 8 | yes | 0.8962s | 0.9753s | `detyped_files/pystone/shallow/proportion_sweep/main_k08_s06.py` |  |
| 0.53 | 8/15 | 7 | 0.6787s | 0.0347s | 1 | 8 | yes | 0.6532s | 0.6973s | `detyped_files/pystone/shallow/proportion_sweep/main_k08_s07.py` |  |
| 0.53 | 8/15 | 8 | 1.0144s | 0.0777s | 1 | 8 | yes | 0.9667s | 1.0669s | `detyped_files/pystone/shallow/proportion_sweep/main_k08_s08.py` |  |
| 0.53 | 8/15 | 9 | 0.6472s | 0.0898s | 1 | 8 | yes | 0.5926s | 0.7075s | `detyped_files/pystone/shallow/proportion_sweep/main_k08_s09.py` |  |
| 0.53 | 8/15 | 10 | 1.0532s | 0.1089s | 1 | 8 | yes | 0.9890s | 1.1278s | `detyped_files/pystone/shallow/proportion_sweep/main_k08_s10.py` |  |
| 0.53 | 8/15 | 11 | 1.1249s | 0.0673s | 1 | 8 | yes | 1.0907s | 1.1738s | `detyped_files/pystone/shallow/proportion_sweep/main_k08_s11.py` |  |
| 0.53 | 8/15 | 12 | 0.9343s | 0.0482s | 1 | 8 | yes | 0.9019s | 0.9644s | `detyped_files/pystone/shallow/proportion_sweep/main_k08_s12.py` |  |
| 0.53 | 8/15 | 13 | 1.4659s | 0.0504s | 1 | 8 | yes | 1.4321s | 1.4965s | `detyped_files/pystone/shallow/proportion_sweep/main_k08_s13.py` |  |
| 0.53 | 8/15 | 14 | 0.6584s | 0.0675s | 1 | 8 | yes | 0.6126s | 0.7004s | `detyped_files/pystone/shallow/proportion_sweep/main_k08_s14.py` |  |
| 0.53 | 8/15 | 15 | 1.0702s | 0.0511s | 1 | 8 | yes | 1.0358s | 1.1012s | `detyped_files/pystone/shallow/proportion_sweep/main_k08_s15.py` |  |
| 0.53 | 8/15 | 16 | 1.3647s | 0.1131s | 1 | 8 | yes | 1.3007s | 1.4476s | `detyped_files/pystone/shallow/proportion_sweep/main_k08_s16.py` |  |
| 0.53 | 8/15 | 17 | 0.9767s | 0.0815s | 1 | 8 | yes | 0.9204s | 1.0239s | `detyped_files/pystone/shallow/proportion_sweep/main_k08_s17.py` |  |
| 0.53 | 8/15 | 18 | 0.7605s | 0.0762s | 1 | 8 | yes | 0.7095s | 0.8100s | `detyped_files/pystone/shallow/proportion_sweep/main_k08_s18.py` |  |
| 0.53 | 8/15 | 19 | 0.6715s | 0.0706s | 1 | 8 | yes | 0.6233s | 0.7136s | `detyped_files/pystone/shallow/proportion_sweep/main_k08_s19.py` |  |
| 0.53 | 8/15 | 20 | 1.1704s | 0.1006s | 1 | 8 | yes | 1.1091s | 1.2410s | `detyped_files/pystone/shallow/proportion_sweep/main_k08_s20.py` |  |
| 0.60 | 9/15 | 1 | 0.9762s | 0.1081s | 1 | 8 | yes | 0.9093s | 1.0492s | `detyped_files/pystone/shallow/proportion_sweep/main_k09_s01.py` |  |
| 0.60 | 9/15 | 2 | 1.5300s | 0.1154s | 1 | 8 | yes | 1.4575s | 1.6094s | `detyped_files/pystone/shallow/proportion_sweep/main_k09_s02.py` |  |
| 0.60 | 9/15 | 3 | 0.7808s | 0.0777s | 1 | 8 | yes | 0.7294s | 0.8289s | `detyped_files/pystone/shallow/proportion_sweep/main_k09_s03.py` |  |
| 0.60 | 9/15 | 4 | 0.7955s | 0.0533s | 1 | 8 | yes | 0.7600s | 0.8285s | `detyped_files/pystone/shallow/proportion_sweep/main_k09_s04.py` |  |
| 0.60 | 9/15 | 5 | 0.9758s | 0.0601s | 1 | 8 | yes | 0.9429s | 1.0202s | `detyped_files/pystone/shallow/proportion_sweep/main_k09_s05.py` |  |
| 0.60 | 9/15 | 6 | 1.1418s | 0.0767s | 1 | 8 | yes | 1.0957s | 1.1952s | `detyped_files/pystone/shallow/proportion_sweep/main_k09_s06.py` |  |
| 0.60 | 9/15 | 7 | 1.5000s | 0.0847s | 1 | 8 | yes | 1.4474s | 1.5573s | `detyped_files/pystone/shallow/proportion_sweep/main_k09_s07.py` |  |
| 0.60 | 9/15 | 8 | 0.9398s | 0.0358s | 1 | 8 | yes | 0.9162s | 0.9630s | `detyped_files/pystone/shallow/proportion_sweep/main_k09_s08.py` |  |
| 0.60 | 9/15 | 9 | 1.1023s | 0.0910s | 1 | 8 | yes | 1.0420s | 1.1588s | `detyped_files/pystone/shallow/proportion_sweep/main_k09_s09.py` |  |
| 0.60 | 9/15 | 10 | 0.9269s | 0.0659s | 1 | 8 | yes | 0.8828s | 0.9677s | `detyped_files/pystone/shallow/proportion_sweep/main_k09_s10.py` |  |
| 0.60 | 9/15 | 11 | 1.0908s | 0.0532s | 1 | 8 | yes | 1.0621s | 1.1291s | `detyped_files/pystone/shallow/proportion_sweep/main_k09_s11.py` |  |
| 0.60 | 9/15 | 12 | 1.3208s | 0.0703s | 1 | 8 | yes | 1.2763s | 1.3660s | `detyped_files/pystone/shallow/proportion_sweep/main_k09_s12.py` |  |
| 0.60 | 9/15 | 13 | 0.8058s | 0.0400s | 1 | 8 | yes | 0.7772s | 0.8275s | `detyped_files/pystone/shallow/proportion_sweep/main_k09_s13.py` |  |
| 0.60 | 9/15 | 14 | 0.7894s | 0.0762s | 1 | 8 | yes | 0.7394s | 0.8370s | `detyped_files/pystone/shallow/proportion_sweep/main_k09_s14.py` |  |
| 0.60 | 9/15 | 15 | 0.9416s | 0.0782s | 1 | 8 | yes | 0.8874s | 0.9884s | `detyped_files/pystone/shallow/proportion_sweep/main_k09_s15.py` |  |
| 0.60 | 9/15 | 16 | 1.0976s | 0.0485s | 1 | 8 | yes | 1.0684s | 1.1304s | `detyped_files/pystone/shallow/proportion_sweep/main_k09_s16.py` |  |
| 0.60 | 9/15 | 17 | 1.4869s | 0.0857s | 1 | 8 | yes | 1.4339s | 1.5408s | `detyped_files/pystone/shallow/proportion_sweep/main_k09_s17.py` |  |
| 0.60 | 9/15 | 18 | 0.8217s | 0.0829s | 1 | 8 | yes | 0.7670s | 0.8723s | `detyped_files/pystone/shallow/proportion_sweep/main_k09_s18.py` |  |
| 0.60 | 9/15 | 19 | 1.0134s | 0.0581s | 1 | 8 | yes | 0.9789s | 1.0541s | `detyped_files/pystone/shallow/proportion_sweep/main_k09_s19.py` |  |
| 0.60 | 9/15 | 20 | 1.3621s | 0.1059s | 1 | 8 | yes | 1.2961s | 1.4319s | `detyped_files/pystone/shallow/proportion_sweep/main_k09_s20.py` |  |
| 0.67 | 10/15 | 1 | 1.0217s | 0.0575s | 1 | 8 | yes | 0.9844s | 1.0595s | `detyped_files/pystone/shallow/proportion_sweep/main_k10_s01.py` |  |
| 0.67 | 10/15 | 2 | 1.2503s | 0.0629s | 1 | 8 | yes | 1.2086s | 1.2897s | `detyped_files/pystone/shallow/proportion_sweep/main_k10_s02.py` |  |
| 0.67 | 10/15 | 3 | 1.3623s | 0.1175s | 1 | 8 | yes | 1.2963s | 1.4439s | `detyped_files/pystone/shallow/proportion_sweep/main_k10_s03.py` |  |
| 0.67 | 10/15 | 4 | 1.2920s | 0.0622s | 1 | 8 | yes | 1.2525s | 1.3314s | `detyped_files/pystone/shallow/proportion_sweep/main_k10_s04.py` |  |
| 0.67 | 10/15 | 5 | 0.8082s | 0.0435s | 1 | 8 | yes | 0.7773s | 0.8316s | `detyped_files/pystone/shallow/proportion_sweep/main_k10_s05.py` |  |
| 0.67 | 10/15 | 6 | 1.0338s | 0.0850s | 1 | 8 | yes | 0.9782s | 1.0876s | `detyped_files/pystone/shallow/proportion_sweep/main_k10_s06.py` |  |
| 0.67 | 10/15 | 7 | 1.3755s | 0.0967s | 1 | 8 | yes | 1.3108s | 1.4374s | `detyped_files/pystone/shallow/proportion_sweep/main_k10_s07.py` |  |
| 0.67 | 10/15 | 8 | 1.2522s | 0.1172s | 1 | 8 | yes | 1.1785s | 1.3296s | `detyped_files/pystone/shallow/proportion_sweep/main_k10_s08.py` |  |
| 0.67 | 10/15 | 9 | 1.3177s | 0.0618s | 1 | 8 | yes | 1.2757s | 1.3560s | `detyped_files/pystone/shallow/proportion_sweep/main_k10_s09.py` |  |
| 0.67 | 10/15 | 10 | 1.4583s | 0.0608s | 1 | 8 | yes | 1.4204s | 1.4993s | `detyped_files/pystone/shallow/proportion_sweep/main_k10_s10.py` |  |
| 0.67 | 10/15 | 11 | 1.1602s | 0.0638s | 1 | 8 | yes | 1.1177s | 1.2006s | `detyped_files/pystone/shallow/proportion_sweep/main_k10_s11.py` |  |
| 0.67 | 10/15 | 12 | 0.9844s | 0.0916s | 1 | 8 | yes | 0.9238s | 1.0433s | `detyped_files/pystone/shallow/proportion_sweep/main_k10_s12.py` |  |
| 0.67 | 10/15 | 13 | 1.5084s | 0.0851s | 1 | 8 | yes | 1.4530s | 1.5648s | `detyped_files/pystone/shallow/proportion_sweep/main_k10_s13.py` |  |
| 0.67 | 10/15 | 14 | 0.9485s | 0.0675s | 1 | 8 | yes | 0.9043s | 0.9947s | `detyped_files/pystone/shallow/proportion_sweep/main_k10_s14.py` |  |
| 0.67 | 10/15 | 15 | 1.2498s | 0.0801s | 1 | 8 | yes | 1.1946s | 1.2998s | `detyped_files/pystone/shallow/proportion_sweep/main_k10_s15.py` |  |
| 0.67 | 10/15 | 16 | 1.0793s | 0.0631s | 1 | 8 | yes | 1.0418s | 1.1239s | `detyped_files/pystone/shallow/proportion_sweep/main_k10_s16.py` |  |
| 0.67 | 10/15 | 17 | 1.0542s | 0.0809s | 1 | 8 | yes | 1.0033s | 1.1080s | `detyped_files/pystone/shallow/proportion_sweep/main_k10_s17.py` |  |
| 0.67 | 10/15 | 18 | 1.0501s | 0.0690s | 1 | 8 | yes | 1.0073s | 1.0941s | `detyped_files/pystone/shallow/proportion_sweep/main_k10_s18.py` |  |
| 0.67 | 10/15 | 19 | 1.0954s | 0.0508s | 1 | 8 | yes | 1.0653s | 1.1293s | `detyped_files/pystone/shallow/proportion_sweep/main_k10_s19.py` |  |
| 0.67 | 10/15 | 20 | 1.1945s | 0.0620s | 1 | 8 | yes | 1.1534s | 1.2340s | `detyped_files/pystone/shallow/proportion_sweep/main_k10_s20.py` |  |
| 0.73 | 11/15 | 1 | 1.4917s | 0.1283s | 1 | 8 | yes | 1.4228s | 1.5875s | `detyped_files/pystone/shallow/proportion_sweep/main_k11_s01.py` |  |
| 0.73 | 11/15 | 2 | 1.1546s | 0.0538s | 1 | 8 | yes | 1.1209s | 1.1897s | `detyped_files/pystone/shallow/proportion_sweep/main_k11_s02.py` |  |
| 0.73 | 11/15 | 3 | 1.1340s | 0.0725s | 1 | 8 | yes | 1.0873s | 1.1816s | `detyped_files/pystone/shallow/proportion_sweep/main_k11_s03.py` |  |
| 0.73 | 11/15 | 4 | 1.1977s | 0.0810s | 1 | 8 | yes | 1.1483s | 1.2516s | `detyped_files/pystone/shallow/proportion_sweep/main_k11_s04.py` |  |
| 0.73 | 11/15 | 5 | 1.2124s | 0.0567s | 1 | 8 | yes | 1.1820s | 1.2545s | `detyped_files/pystone/shallow/proportion_sweep/main_k11_s05.py` |  |
| 0.73 | 11/15 | 6 | 1.5309s | 0.1118s | 1 | 8 | yes | 1.4598s | 1.6052s | `detyped_files/pystone/shallow/proportion_sweep/main_k11_s06.py` |  |
| 0.73 | 11/15 | 7 | 0.9376s | 0.0568s | 1 | 8 | yes | 0.8989s | 0.9724s | `detyped_files/pystone/shallow/proportion_sweep/main_k11_s07.py` |  |
| 0.73 | 11/15 | 8 | 1.0765s | 0.0735s | 1 | 8 | yes | 1.0289s | 1.1237s | `detyped_files/pystone/shallow/proportion_sweep/main_k11_s08.py` |  |
| 0.73 | 11/15 | 9 | 1.3898s | 0.1531s | 1 | 8 | yes | 1.3049s | 1.4994s | `detyped_files/pystone/shallow/proportion_sweep/main_k11_s09.py` |  |
| 0.73 | 11/15 | 10 | 1.3354s | 0.0783s | 1 | 8 | yes | 1.2866s | 1.3874s | `detyped_files/pystone/shallow/proportion_sweep/main_k11_s10.py` |  |
| 0.73 | 11/15 | 11 | 1.0579s | 0.0972s | 1 | 8 | yes | 0.9986s | 1.1255s | `detyped_files/pystone/shallow/proportion_sweep/main_k11_s11.py` |  |
| 0.73 | 11/15 | 12 | 1.2377s | 0.0657s | 1 | 8 | yes | 1.1976s | 1.2825s | `detyped_files/pystone/shallow/proportion_sweep/main_k11_s12.py` |  |
| 0.73 | 11/15 | 13 | 1.4974s | 0.0923s | 1 | 8 | yes | 1.4385s | 1.5569s | `detyped_files/pystone/shallow/proportion_sweep/main_k11_s13.py` |  |
| 0.73 | 11/15 | 14 | 1.5009s | 0.0743s | 1 | 8 | yes | 1.4565s | 1.5524s | `detyped_files/pystone/shallow/proportion_sweep/main_k11_s14.py` |  |
| 0.73 | 11/15 | 15 | 1.3390s | 0.0393s | 1 | 8 | yes | 1.3113s | 1.3620s | `detyped_files/pystone/shallow/proportion_sweep/main_k11_s15.py` |  |
| 0.73 | 11/15 | 16 | 1.4895s | 0.0524s | 1 | 8 | yes | 1.4544s | 1.5221s | `detyped_files/pystone/shallow/proportion_sweep/main_k11_s16.py` |  |
| 0.73 | 11/15 | 17 | 1.4777s | 0.0848s | 1 | 8 | yes | 1.4235s | 1.5334s | `detyped_files/pystone/shallow/proportion_sweep/main_k11_s17.py` |  |
| 0.73 | 11/15 | 18 | 1.0287s | 0.0698s | 1 | 8 | yes | 0.9847s | 1.0738s | `detyped_files/pystone/shallow/proportion_sweep/main_k11_s18.py` |  |
| 0.73 | 11/15 | 19 | 1.0630s | 0.0705s | 1 | 8 | yes | 1.0159s | 1.1070s | `detyped_files/pystone/shallow/proportion_sweep/main_k11_s19.py` |  |
| 0.73 | 11/15 | 20 | 1.2319s | 0.0856s | 1 | 8 | yes | 1.1845s | 1.2925s | `detyped_files/pystone/shallow/proportion_sweep/main_k11_s20.py` |  |
| 0.80 | 12/15 | 1 | 1.1866s | 0.0547s | 1 | 8 | yes | 1.1475s | 1.2170s | `detyped_files/pystone/shallow/proportion_sweep/main_k12_s01.py` |  |
| 0.80 | 12/15 | 2 | 1.3919s | 0.1243s | 1 | 8 | yes | 1.3153s | 1.4739s | `detyped_files/pystone/shallow/proportion_sweep/main_k12_s02.py` |  |
| 0.80 | 12/15 | 3 | 1.1827s | 0.0601s | 1 | 8 | yes | 1.1434s | 1.2212s | `detyped_files/pystone/shallow/proportion_sweep/main_k12_s03.py` |  |
| 0.80 | 12/15 | 4 | 0.7996s | 0.0729s | 1 | 8 | yes | 0.7514s | 0.8460s | `detyped_files/pystone/shallow/proportion_sweep/main_k12_s04.py` |  |
| 0.80 | 12/15 | 5 | 1.0929s | 0.0450s | 1 | 8 | yes | 1.0619s | 1.1202s | `detyped_files/pystone/shallow/proportion_sweep/main_k12_s05.py` |  |
| 0.80 | 12/15 | 6 | 1.2137s | 0.0826s | 1 | 8 | yes | 1.1669s | 1.2704s | `detyped_files/pystone/shallow/proportion_sweep/main_k12_s06.py` |  |
| 0.80 | 12/15 | 7 | 1.4676s | 0.0745s | 1 | 8 | yes | 1.4159s | 1.5118s | `detyped_files/pystone/shallow/proportion_sweep/main_k12_s07.py` |  |
| 0.80 | 12/15 | 8 | 1.4870s | 0.0373s | 1 | 8 | yes | 1.4612s | 1.5100s | `detyped_files/pystone/shallow/proportion_sweep/main_k12_s08.py` |  |
| 0.80 | 12/15 | 9 | 0.8107s | 0.0786s | 1 | 8 | yes | 0.7584s | 0.8609s | `detyped_files/pystone/shallow/proportion_sweep/main_k12_s09.py` |  |
| 0.80 | 12/15 | 10 | 1.5009s | 0.0552s | 1 | 8 | yes | 1.4655s | 1.5368s | `detyped_files/pystone/shallow/proportion_sweep/main_k12_s10.py` |  |
| 0.80 | 12/15 | 11 | 1.5081s | 0.0796s | 1 | 8 | yes | 1.4583s | 1.5594s | `detyped_files/pystone/shallow/proportion_sweep/main_k12_s11.py` |  |
| 0.80 | 12/15 | 12 | 1.0716s | 0.0438s | 1 | 8 | yes | 1.0435s | 1.1002s | `detyped_files/pystone/shallow/proportion_sweep/main_k12_s12.py` |  |
| 0.80 | 12/15 | 13 | 1.1389s | 0.0737s | 1 | 8 | yes | 1.1008s | 1.1918s | `detyped_files/pystone/shallow/proportion_sweep/main_k12_s13.py` |  |
| 0.80 | 12/15 | 14 | 1.4803s | 0.0932s | 1 | 8 | yes | 1.4205s | 1.5390s | `detyped_files/pystone/shallow/proportion_sweep/main_k12_s14.py` |  |
| 0.80 | 12/15 | 15 | 1.5004s | 0.0288s | 1 | 8 | yes | 1.4849s | 1.5212s | `detyped_files/pystone/shallow/proportion_sweep/main_k12_s15.py` |  |
| 0.80 | 12/15 | 16 | 1.1100s | 0.0571s | 1 | 8 | yes | 1.0734s | 1.1473s | `detyped_files/pystone/shallow/proportion_sweep/main_k12_s16.py` |  |
| 0.80 | 12/15 | 17 | 1.5136s | 0.0338s | 1 | 8 | yes | 1.4927s | 1.5357s | `detyped_files/pystone/shallow/proportion_sweep/main_k12_s17.py` |  |
| 0.80 | 12/15 | 18 | 1.0698s | 0.0493s | 1 | 8 | yes | 1.0344s | 1.0988s | `detyped_files/pystone/shallow/proportion_sweep/main_k12_s18.py` |  |
| 0.80 | 12/15 | 19 | 0.8037s | 0.0714s | 1 | 8 | yes | 0.7577s | 0.8508s | `detyped_files/pystone/shallow/proportion_sweep/main_k12_s19.py` |  |
| 0.80 | 12/15 | 20 | 1.2007s | 0.0840s | 1 | 8 | yes | 1.1471s | 1.2554s | `detyped_files/pystone/shallow/proportion_sweep/main_k12_s20.py` |  |
| 0.87 | 13/15 | 1 | 1.0504s | 0.0942s | 1 | 8 | yes | 0.9908s | 1.1118s | `detyped_files/pystone/shallow/proportion_sweep/main_k13_s01.py` |  |
| 0.87 | 13/15 | 2 | 1.4692s | 0.0524s | 1 | 8 | yes | 1.4354s | 1.5013s | `detyped_files/pystone/shallow/proportion_sweep/main_k13_s02.py` |  |
| 0.87 | 13/15 | 3 | 1.5069s | 0.0267s | 1 | 8 | yes | 1.4909s | 1.5251s | `detyped_files/pystone/shallow/proportion_sweep/main_k13_s03.py` |  |
| 0.87 | 13/15 | 4 | 1.0775s | 0.0900s | 1 | 8 | yes | 1.0178s | 1.1347s | `detyped_files/pystone/shallow/proportion_sweep/main_k13_s04.py` |  |
| 0.87 | 13/15 | 5 | 1.5245s | 0.0749s | 1 | 8 | yes | 1.4746s | 1.5710s | `detyped_files/pystone/shallow/proportion_sweep/main_k13_s05.py` |  |
| 0.87 | 13/15 | 6 | 1.5108s | 0.0652s | 1 | 8 | yes | 1.4746s | 1.5568s | `detyped_files/pystone/shallow/proportion_sweep/main_k13_s06.py` |  |
| 0.87 | 13/15 | 7 | 1.5094s | 0.0776s | 1 | 8 | yes | 1.4594s | 1.5603s | `detyped_files/pystone/shallow/proportion_sweep/main_k13_s07.py` |  |
| 0.87 | 13/15 | 8 | 1.5788s | 0.0931s | 1 | 8 | yes | 1.5189s | 1.6386s | `detyped_files/pystone/shallow/proportion_sweep/main_k13_s08.py` |  |
| 0.87 | 13/15 | 9 | 1.0852s | 0.1070s | 1 | 8 | yes | 1.0147s | 1.1555s | `detyped_files/pystone/shallow/proportion_sweep/main_k13_s09.py` |  |
| 0.87 | 13/15 | 10 | 1.2906s | 0.1212s | 1 | 8 | yes | 1.2179s | 1.3748s | `detyped_files/pystone/shallow/proportion_sweep/main_k13_s10.py` |  |
| 0.87 | 13/15 | 11 | 1.2225s | 0.0853s | 1 | 8 | yes | 1.1701s | 1.2794s | `detyped_files/pystone/shallow/proportion_sweep/main_k13_s11.py` |  |
| 0.87 | 13/15 | 12 | 1.5140s | 0.0444s | 1 | 8 | yes | 1.4849s | 1.5418s | `detyped_files/pystone/shallow/proportion_sweep/main_k13_s12.py` |  |
| 0.87 | 13/15 | 13 | 1.4877s | 0.0876s | 1 | 8 | yes | 1.4353s | 1.5483s | `detyped_files/pystone/shallow/proportion_sweep/main_k13_s13.py` |  |
| 0.87 | 13/15 | 14 | 1.5014s | 0.1022s | 1 | 8 | yes | 1.4340s | 1.5676s | `detyped_files/pystone/shallow/proportion_sweep/main_k13_s14.py` |  |
| 0.87 | 13/15 | 15 | 1.1862s | 0.0551s | 1 | 8 | yes | 1.1466s | 1.2173s | `detyped_files/pystone/shallow/proportion_sweep/main_k13_s15.py` |  |
| 0.87 | 13/15 | 16 | 1.4735s | 0.0958s | 1 | 8 | yes | 1.4150s | 1.5380s | `detyped_files/pystone/shallow/proportion_sweep/main_k13_s16.py` |  |
| 0.87 | 13/15 | 17 | 1.4635s | 0.0123s | 1 | 8 | yes | 1.4556s | 1.4713s | `detyped_files/pystone/shallow/proportion_sweep/main_k13_s17.py` |  |
| 0.87 | 13/15 | 18 | 1.4503s | 0.0608s | 1 | 8 | yes | 1.4092s | 1.4882s | `detyped_files/pystone/shallow/proportion_sweep/main_k13_s18.py` |  |
| 0.87 | 13/15 | 19 | 1.4250s | 0.0966s | 1 | 8 | yes | 1.3670s | 1.4910s | `detyped_files/pystone/shallow/proportion_sweep/main_k13_s19.py` |  |
| 0.87 | 13/15 | 20 | 1.4473s | 0.0623s | 1 | 8 | yes | 1.4047s | 1.4833s | `detyped_files/pystone/shallow/proportion_sweep/main_k13_s20.py` |  |
| 0.93 | 14/15 | 1 | 1.2185s | 0.0638s | 1 | 8 | yes | 1.1812s | 1.2637s | `detyped_files/pystone/shallow/proportion_sweep/main_k14_s01.py` |  |
| 0.93 | 14/15 | 2 | 1.4907s | 0.1237s | 1 | 8 | yes | 1.4196s | 1.5782s | `detyped_files/pystone/shallow/proportion_sweep/main_k14_s02.py` |  |
| 0.93 | 14/15 | 3 | 1.4891s | 0.1218s | 1 | 8 | yes | 1.4120s | 1.5713s | `detyped_files/pystone/shallow/proportion_sweep/main_k14_s03.py` |  |
| 0.93 | 14/15 | 4 | 1.5273s | 0.1200s | 1 | 8 | yes | 1.4514s | 1.6060s | `detyped_files/pystone/shallow/proportion_sweep/main_k14_s04.py` |  |
| 0.93 | 14/15 | 5 | 1.5373s | 0.0910s | 1 | 8 | yes | 1.4747s | 1.5929s | `detyped_files/pystone/shallow/proportion_sweep/main_k14_s05.py` |  |
| 0.93 | 14/15 | 6 | 1.4696s | 0.0318s | 1 | 8 | yes | 1.4499s | 1.4907s | `detyped_files/pystone/shallow/proportion_sweep/main_k14_s06.py` |  |
| 0.93 | 14/15 | 7 | 1.4955s | 0.0769s | 1 | 8 | yes | 1.4391s | 1.5392s | `detyped_files/pystone/shallow/proportion_sweep/main_k14_s07.py` |  |
| 0.93 | 14/15 | 8 | 1.4827s | 0.0890s | 1 | 8 | yes | 1.4279s | 1.5431s | `detyped_files/pystone/shallow/proportion_sweep/main_k14_s08.py` |  |
| 0.93 | 14/15 | 9 | 1.5061s | 0.0670s | 1 | 8 | yes | 1.4605s | 1.5460s | `detyped_files/pystone/shallow/proportion_sweep/main_k14_s09.py` |  |
| 0.93 | 14/15 | 10 | 1.3655s | 0.1030s | 1 | 8 | yes | 1.3015s | 1.4374s | `detyped_files/pystone/shallow/proportion_sweep/main_k14_s10.py` |  |
| 0.93 | 14/15 | 11 | 1.5198s | 0.1476s | 1 | 8 | yes | 1.4375s | 1.6218s | `detyped_files/pystone/shallow/proportion_sweep/main_k14_s11.py` |  |
| 0.93 | 14/15 | 12 | 1.5288s | 0.0797s | 1 | 8 | yes | 1.4795s | 1.5809s | `detyped_files/pystone/shallow/proportion_sweep/main_k14_s12.py` |  |
| 0.93 | 14/15 | 13 | 1.5273s | 0.0466s | 1 | 8 | yes | 1.4979s | 1.5571s | `detyped_files/pystone/shallow/proportion_sweep/main_k14_s13.py` |  |
| 0.93 | 14/15 | 14 | 1.0852s | 0.0699s | 1 | 8 | yes | 1.0381s | 1.1286s | `detyped_files/pystone/shallow/proportion_sweep/main_k14_s14.py` |  |
| 0.93 | 14/15 | 15 | 1.4681s | 0.0647s | 1 | 8 | yes | 1.4282s | 1.5118s | `detyped_files/pystone/shallow/proportion_sweep/main_k14_s15.py` |  |
| 1.00 | 15/15 | 1 | 1.4967s | 0.0949s | 1 | 8 | yes | 1.4394s | 1.5604s | `detyped_files/pystone/shallow/proportion_sweep/main_k15_s01.py` |  |

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
- Total runs: `442`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/23 | 1 | 1.1938s | 1.1938s | 1.1938s | 1.0 | yes | ok |
| 0.04 | 1/23 | 20 | 1.4421s | 1.1337s | 3.8618s | 1.0 | yes | ok |
| 0.09 | 2/23 | 20 | 1.8771s | 1.1781s | 3.8380s | 1.0 | yes | ok |
| 0.13 | 3/23 | 20 | 2.2191s | 1.1980s | 4.1090s | 1.0 | yes | ok |
| 0.17 | 4/23 | 20 | 2.2444s | 1.2798s | 4.6361s | 1.0 | yes | ok |
| 0.22 | 5/23 | 20 | 2.3662s | 1.2561s | 4.3687s | 1.0 | yes | ok |
| 0.26 | 6/23 | 20 | 2.4975s | 1.3617s | 4.6468s | 1.0 | yes | ok |
| 0.30 | 7/23 | 20 | 2.5682s | 1.4545s | 5.0479s | 1.0 | yes | ok |
| 0.35 | 8/23 | 20 | 3.1064s | 1.5764s | 5.1420s | 1.0 | yes | ok |
| 0.39 | 9/23 | 20 | 3.8108s | 2.0969s | 5.3382s | 1.0 | yes | ok |
| 0.43 | 10/23 | 20 | 3.5120s | 1.7903s | 5.2414s | 1.0 | yes | ok |
| 0.48 | 11/23 | 20 | 4.1008s | 2.0376s | 5.5819s | 1.0 | yes | ok |
| 0.52 | 12/23 | 20 | 4.1421s | 2.0833s | 5.7424s | 1.0 | yes | ok |
| 0.57 | 13/23 | 20 | 4.3769s | 2.3219s | 5.9988s | 1.0 | yes | ok |
| 0.61 | 14/23 | 20 | 4.1174s | 2.2168s | 5.9204s | 1.0 | yes | ok |
| 0.65 | 15/23 | 20 | 4.8596s | 2.5326s | 6.1360s | 1.0 | yes | ok |
| 0.70 | 16/23 | 20 | 4.2457s | 2.2900s | 6.0222s | 1.0 | yes | ok |
| 0.74 | 17/23 | 20 | 5.1237s | 2.8319s | 6.1115s | 1.0 | yes | ok |
| 0.78 | 18/23 | 20 | 4.5652s | 2.9585s | 6.2124s | 1.0 | yes | ok |
| 0.83 | 19/23 | 20 | 5.4645s | 3.5104s | 6.1559s | 1.0 | yes | ok |
| 0.87 | 20/23 | 20 | 5.4363s | 3.4134s | 6.3406s | 1.0 | yes | ok |
| 0.91 | 21/23 | 20 | 5.9750s | 3.7020s | 6.3070s | 1.0 | yes | ok |
| 0.96 | 22/23 | 20 | 6.1474s | 5.5041s | 6.3551s | 1.0 | yes | ok |
| 1.00 | 23/23 | 1 | 6.2335s | 6.2335s | 6.2335s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/23 | 1 | 1.1938s | 0.1152s | 1 | 8 | yes | 1.1270s | 1.2743s | `detyped_files/richards/advanced/proportion_sweep/main_k00_s01.py` |  |
| 0.04 | 1/23 | 1 | 1.2242s | 0.0501s | 1 | 8 | yes | 1.1874s | 1.2501s | `detyped_files/richards/advanced/proportion_sweep/main_k01_s01.py` |  |
| 0.04 | 1/23 | 2 | 1.2396s | 0.0397s | 1 | 8 | yes | 1.2170s | 1.2670s | `detyped_files/richards/advanced/proportion_sweep/main_k01_s02.py` |  |
| 0.04 | 1/23 | 3 | 1.3463s | 0.1277s | 1 | 8 | yes | 1.2656s | 1.4325s | `detyped_files/richards/advanced/proportion_sweep/main_k01_s03.py` |  |
| 0.04 | 1/23 | 4 | 3.8618s | 0.1185s | 1 | 8 | yes | 3.7849s | 3.9375s | `detyped_files/richards/advanced/proportion_sweep/main_k01_s04.py` |  |
| 0.04 | 1/23 | 5 | 1.2943s | 0.0214s | 1 | 8 | yes | 1.2814s | 1.3089s | `detyped_files/richards/advanced/proportion_sweep/main_k01_s05.py` |  |
| 0.04 | 1/23 | 6 | 1.3434s | 0.0502s | 1 | 8 | yes | 1.3094s | 1.3740s | `detyped_files/richards/advanced/proportion_sweep/main_k01_s06.py` |  |
| 0.04 | 1/23 | 7 | 1.1337s | 0.0684s | 1 | 8 | yes | 1.0915s | 1.1788s | `detyped_files/richards/advanced/proportion_sweep/main_k01_s07.py` |  |
| 0.04 | 1/23 | 8 | 1.1786s | 0.0895s | 1 | 8 | yes | 1.1264s | 1.2412s | `detyped_files/richards/advanced/proportion_sweep/main_k01_s08.py` |  |
| 0.04 | 1/23 | 9 | 1.2023s | 0.0634s | 1 | 8 | yes | 1.1556s | 1.2361s | `detyped_files/richards/advanced/proportion_sweep/main_k01_s09.py` |  |
| 0.04 | 1/23 | 10 | 1.2112s | 0.0719s | 1 | 8 | yes | 1.1675s | 1.2599s | `detyped_files/richards/advanced/proportion_sweep/main_k01_s10.py` |  |
| 0.04 | 1/23 | 11 | 1.1906s | 0.0774s | 1 | 8 | yes | 1.1374s | 1.2362s | `detyped_files/richards/advanced/proportion_sweep/main_k01_s11.py` |  |
| 0.04 | 1/23 | 12 | 1.3438s | 0.0926s | 1 | 8 | yes | 1.2837s | 1.4010s | `detyped_files/richards/advanced/proportion_sweep/main_k01_s12.py` |  |
| 0.04 | 1/23 | 13 | 1.2092s | 0.0705s | 1 | 8 | yes | 1.1649s | 1.2550s | `detyped_files/richards/advanced/proportion_sweep/main_k01_s13.py` |  |
| 0.04 | 1/23 | 14 | 1.6941s | 0.0653s | 1 | 8 | yes | 1.6525s | 1.7364s | `detyped_files/richards/advanced/proportion_sweep/main_k01_s14.py` |  |
| 0.04 | 1/23 | 15 | 1.5705s | 0.1062s | 1 | 8 | yes | 1.5133s | 1.6487s | `detyped_files/richards/advanced/proportion_sweep/main_k01_s15.py` |  |
| 0.04 | 1/23 | 16 | 1.1835s | 0.0708s | 1 | 8 | yes | 1.1399s | 1.2310s | `detyped_files/richards/advanced/proportion_sweep/main_k01_s16.py` |  |
| 0.04 | 1/23 | 17 | 1.1767s | 0.0571s | 1 | 8 | yes | 1.1392s | 1.2134s | `detyped_files/richards/advanced/proportion_sweep/main_k01_s17.py` |  |
| 0.04 | 1/23 | 18 | 1.1980s | 0.0969s | 1 | 8 | yes | 1.1345s | 1.2608s | `detyped_files/richards/advanced/proportion_sweep/main_k01_s18.py` |  |
| 0.04 | 1/23 | 19 | 1.1724s | 0.0746s | 1 | 8 | yes | 1.1311s | 1.2260s | `detyped_files/richards/advanced/proportion_sweep/main_k01_s19.py` |  |
| 0.04 | 1/23 | 20 | 2.0681s | 0.0917s | 1 | 8 | yes | 2.0050s | 2.1236s | `detyped_files/richards/advanced/proportion_sweep/main_k01_s20.py` |  |
| 0.09 | 2/23 | 1 | 1.5135s | 0.0682s | 1 | 8 | yes | 1.4686s | 1.5571s | `detyped_files/richards/advanced/proportion_sweep/main_k02_s01.py` |  |
| 0.09 | 2/23 | 2 | 2.0244s | 0.0903s | 1 | 8 | yes | 1.9833s | 2.0908s | `detyped_files/richards/advanced/proportion_sweep/main_k02_s02.py` |  |
| 0.09 | 2/23 | 3 | 3.8380s | 0.0774s | 1 | 8 | yes | 3.7911s | 3.8908s | `detyped_files/richards/advanced/proportion_sweep/main_k02_s03.py` |  |
| 0.09 | 2/23 | 4 | 1.7546s | 0.1493s | 1 | 8 | yes | 1.6672s | 1.8576s | `detyped_files/richards/advanced/proportion_sweep/main_k02_s04.py` |  |
| 0.09 | 2/23 | 5 | 1.3363s | 0.1155s | 1 | 8 | yes | 1.2692s | 1.4181s | `detyped_files/richards/advanced/proportion_sweep/main_k02_s05.py` |  |
| 0.09 | 2/23 | 6 | 1.5332s | 0.1151s | 1 | 8 | yes | 1.4619s | 1.6116s | `detyped_files/richards/advanced/proportion_sweep/main_k02_s06.py` |  |
| 0.09 | 2/23 | 7 | 1.9476s | 0.0533s | 1 | 8 | yes | 1.9169s | 1.9843s | `detyped_files/richards/advanced/proportion_sweep/main_k02_s07.py` |  |
| 0.09 | 2/23 | 8 | 3.8304s | 0.0887s | 1 | 8 | yes | 3.7801s | 3.8901s | `detyped_files/richards/advanced/proportion_sweep/main_k02_s08.py` |  |
| 0.09 | 2/23 | 9 | 1.5467s | 0.0584s | 1 | 8 | yes | 1.5116s | 1.5871s | `detyped_files/richards/advanced/proportion_sweep/main_k02_s09.py` |  |
| 0.09 | 2/23 | 10 | 3.7655s | 0.1376s | 1 | 8 | yes | 3.6869s | 3.8670s | `detyped_files/richards/advanced/proportion_sweep/main_k02_s10.py` |  |
| 0.09 | 2/23 | 11 | 1.3680s | 0.0870s | 1 | 8 | yes | 1.3129s | 1.4253s | `detyped_files/richards/advanced/proportion_sweep/main_k02_s11.py` |  |
| 0.09 | 2/23 | 12 | 1.2151s | 0.0746s | 1 | 8 | yes | 1.1608s | 1.2587s | `detyped_files/richards/advanced/proportion_sweep/main_k02_s12.py` |  |
| 0.09 | 2/23 | 13 | 1.7543s | 0.1126s | 1 | 8 | yes | 1.6873s | 1.8307s | `detyped_files/richards/advanced/proportion_sweep/main_k02_s13.py` |  |
| 0.09 | 2/23 | 14 | 1.7252s | 0.0810s | 1 | 8 | yes | 1.6733s | 1.7797s | `detyped_files/richards/advanced/proportion_sweep/main_k02_s14.py` |  |
| 0.09 | 2/23 | 15 | 1.2921s | 0.0578s | 1 | 8 | yes | 1.2551s | 1.3295s | `detyped_files/richards/advanced/proportion_sweep/main_k02_s15.py` |  |
| 0.09 | 2/23 | 16 | 1.3385s | 0.0745s | 1 | 8 | yes | 1.2940s | 1.3911s | `detyped_files/richards/advanced/proportion_sweep/main_k02_s16.py` |  |
| 0.09 | 2/23 | 17 | 1.7152s | 0.0998s | 1 | 8 | yes | 1.6515s | 1.7805s | `detyped_files/richards/advanced/proportion_sweep/main_k02_s17.py` |  |
| 0.09 | 2/23 | 18 | 1.1781s | 0.0898s | 1 | 8 | yes | 1.1199s | 1.2357s | `detyped_files/richards/advanced/proportion_sweep/main_k02_s18.py` |  |
| 0.09 | 2/23 | 19 | 1.5538s | 0.0674s | 1 | 8 | yes | 1.5127s | 1.5993s | `detyped_files/richards/advanced/proportion_sweep/main_k02_s19.py` |  |
| 0.09 | 2/23 | 20 | 1.3118s | 0.0815s | 1 | 8 | yes | 1.2577s | 1.3626s | `detyped_files/richards/advanced/proportion_sweep/main_k02_s20.py` |  |
| 0.13 | 3/23 | 1 | 1.4860s | 0.1207s | 1 | 8 | yes | 1.4254s | 1.5758s | `detyped_files/richards/advanced/proportion_sweep/main_k03_s01.py` |  |
| 0.13 | 3/23 | 2 | 3.7553s | 0.1377s | 1 | 8 | yes | 3.6755s | 3.8508s | `detyped_files/richards/advanced/proportion_sweep/main_k03_s02.py` |  |
| 0.13 | 3/23 | 3 | 2.4365s | 0.1537s | 1 | 8 | yes | 2.3396s | 2.5380s | `detyped_files/richards/advanced/proportion_sweep/main_k03_s03.py` |  |
| 0.13 | 3/23 | 4 | 1.3491s | 0.0630s | 1 | 8 | yes | 1.3054s | 1.3890s | `detyped_files/richards/advanced/proportion_sweep/main_k03_s04.py` |  |
| 0.13 | 3/23 | 5 | 1.2641s | 0.0944s | 1 | 8 | yes | 1.2075s | 1.3291s | `detyped_files/richards/advanced/proportion_sweep/main_k03_s05.py` |  |
| 0.13 | 3/23 | 6 | 1.4756s | 0.0759s | 1 | 8 | yes | 1.4255s | 1.5240s | `detyped_files/richards/advanced/proportion_sweep/main_k03_s06.py` |  |
| 0.13 | 3/23 | 7 | 1.4805s | 0.0760s | 1 | 8 | yes | 1.4312s | 1.5297s | `detyped_files/richards/advanced/proportion_sweep/main_k03_s07.py` |  |
| 0.13 | 3/23 | 8 | 4.0268s | 0.1076s | 1 | 8 | yes | 3.9576s | 4.0966s | `detyped_files/richards/advanced/proportion_sweep/main_k03_s08.py` |  |
| 0.13 | 3/23 | 9 | 1.3214s | 0.1110s | 1 | 8 | yes | 1.2570s | 1.4031s | `detyped_files/richards/advanced/proportion_sweep/main_k03_s09.py` |  |
| 0.13 | 3/23 | 10 | 1.7261s | 0.0454s | 1 | 8 | yes | 1.6982s | 1.7566s | `detyped_files/richards/advanced/proportion_sweep/main_k03_s10.py` |  |
| 0.13 | 3/23 | 11 | 2.0525s | 0.0327s | 1 | 8 | yes | 2.0325s | 2.0753s | `detyped_files/richards/advanced/proportion_sweep/main_k03_s11.py` |  |
| 0.13 | 3/23 | 12 | 1.3648s | 0.0511s | 1 | 8 | yes | 1.3335s | 1.3993s | `detyped_files/richards/advanced/proportion_sweep/main_k03_s12.py` |  |
| 0.13 | 3/23 | 13 | 3.8744s | 0.0836s | 1 | 8 | yes | 3.8290s | 3.9356s | `detyped_files/richards/advanced/proportion_sweep/main_k03_s13.py` |  |
| 0.13 | 3/23 | 14 | 1.1980s | 0.0603s | 1 | 8 | yes | 1.1564s | 1.2336s | `detyped_files/richards/advanced/proportion_sweep/main_k03_s14.py` |  |
| 0.13 | 3/23 | 15 | 1.9785s | 0.0558s | 1 | 8 | yes | 1.9409s | 2.0125s | `detyped_files/richards/advanced/proportion_sweep/main_k03_s15.py` |  |
| 0.13 | 3/23 | 16 | 2.0455s | 0.0822s | 1 | 8 | yes | 1.9909s | 2.0945s | `detyped_files/richards/advanced/proportion_sweep/main_k03_s16.py` |  |
| 0.13 | 3/23 | 17 | 2.0955s | 0.1089s | 1 | 8 | yes | 2.0337s | 2.1736s | `detyped_files/richards/advanced/proportion_sweep/main_k03_s17.py` |  |
| 0.13 | 3/23 | 18 | 1.2703s | 0.1216s | 1 | 8 | yes | 1.1983s | 1.3513s | `detyped_files/richards/advanced/proportion_sweep/main_k03_s18.py` |  |
| 0.13 | 3/23 | 19 | 4.0715s | 0.0686s | 1 | 8 | yes | 4.0345s | 4.1207s | `detyped_files/richards/advanced/proportion_sweep/main_k03_s19.py` |  |
| 0.13 | 3/23 | 20 | 4.1090s | 0.1611s | 1 | 8 | yes | 4.0008s | 4.2053s | `detyped_files/richards/advanced/proportion_sweep/main_k03_s20.py` |  |
| 0.17 | 4/23 | 1 | 1.6414s | 0.0807s | 1 | 8 | yes | 1.5913s | 1.6969s | `detyped_files/richards/advanced/proportion_sweep/main_k04_s01.py` |  |
| 0.17 | 4/23 | 2 | 2.4629s | 0.1841s | 1 | 8 | yes | 2.3742s | 2.5999s | `detyped_files/richards/advanced/proportion_sweep/main_k04_s02.py` |  |
| 0.17 | 4/23 | 3 | 3.8466s | 0.0896s | 1 | 8 | yes | 3.7932s | 3.9082s | `detyped_files/richards/advanced/proportion_sweep/main_k04_s03.py` |  |
| 0.17 | 4/23 | 4 | 1.3713s | 0.0783s | 1 | 8 | yes | 1.3229s | 1.4240s | `detyped_files/richards/advanced/proportion_sweep/main_k04_s04.py` |  |
| 0.17 | 4/23 | 5 | 3.9347s | 0.1528s | 1 | 8 | yes | 3.8454s | 4.0409s | `detyped_files/richards/advanced/proportion_sweep/main_k04_s05.py` |  |
| 0.17 | 4/23 | 6 | 1.6095s | 0.0540s | 1 | 8 | yes | 1.5750s | 1.6455s | `detyped_files/richards/advanced/proportion_sweep/main_k04_s06.py` |  |
| 0.17 | 4/23 | 7 | 1.3722s | 0.0724s | 1 | 8 | yes | 1.3291s | 1.4218s | `detyped_files/richards/advanced/proportion_sweep/main_k04_s07.py` |  |
| 0.17 | 4/23 | 8 | 4.5595s | 0.0968s | 1 | 8 | yes | 4.4913s | 4.6152s | `detyped_files/richards/advanced/proportion_sweep/main_k04_s08.py` |  |
| 0.17 | 4/23 | 9 | 2.0416s | 0.0857s | 1 | 8 | yes | 1.9856s | 2.0966s | `detyped_files/richards/advanced/proportion_sweep/main_k04_s09.py` |  |
| 0.17 | 4/23 | 10 | 1.2798s | 0.1009s | 1 | 8 | yes | 1.2185s | 1.3465s | `detyped_files/richards/advanced/proportion_sweep/main_k04_s10.py` |  |
| 0.17 | 4/23 | 11 | 4.6361s | 0.1448s | 1 | 8 | yes | 4.5448s | 4.7318s | `detyped_files/richards/advanced/proportion_sweep/main_k04_s11.py` |  |
| 0.17 | 4/23 | 12 | 4.4112s | 0.1221s | 1 | 8 | yes | 4.3329s | 4.4898s | `detyped_files/richards/advanced/proportion_sweep/main_k04_s12.py` |  |
| 0.17 | 4/23 | 13 | 1.4208s | 0.0737s | 1 | 8 | yes | 1.3737s | 1.4685s | `detyped_files/richards/advanced/proportion_sweep/main_k04_s13.py` |  |
| 0.17 | 4/23 | 14 | 1.4754s | 0.1089s | 1 | 8 | yes | 1.4023s | 1.5409s | `detyped_files/richards/advanced/proportion_sweep/main_k04_s14.py` |  |
| 0.17 | 4/23 | 15 | 1.4338s | 0.0823s | 1 | 8 | yes | 1.3798s | 1.4860s | `detyped_files/richards/advanced/proportion_sweep/main_k04_s15.py` |  |
| 0.17 | 4/23 | 16 | 1.3280s | 0.0905s | 1 | 8 | yes | 1.2727s | 1.3884s | `detyped_files/richards/advanced/proportion_sweep/main_k04_s16.py` |  |
| 0.17 | 4/23 | 17 | 1.3761s | 0.1004s | 1 | 8 | yes | 1.3135s | 1.4443s | `detyped_files/richards/advanced/proportion_sweep/main_k04_s17.py` |  |
| 0.17 | 4/23 | 18 | 1.3116s | 0.0919s | 1 | 8 | yes | 1.2535s | 1.3748s | `detyped_files/richards/advanced/proportion_sweep/main_k04_s18.py` |  |
| 0.17 | 4/23 | 19 | 1.9058s | 0.0724s | 1 | 8 | yes | 1.8574s | 1.9511s | `detyped_files/richards/advanced/proportion_sweep/main_k04_s19.py` |  |
| 0.17 | 4/23 | 20 | 1.4688s | 0.0779s | 1 | 8 | yes | 1.4198s | 1.5224s | `detyped_files/richards/advanced/proportion_sweep/main_k04_s20.py` |  |
| 0.22 | 5/23 | 1 | 2.3876s | 0.1003s | 1 | 8 | yes | 2.3289s | 2.4575s | `detyped_files/richards/advanced/proportion_sweep/main_k05_s01.py` |  |
| 0.22 | 5/23 | 2 | 1.8696s | 0.0438s | 1 | 8 | yes | 1.8412s | 1.8966s | `detyped_files/richards/advanced/proportion_sweep/main_k05_s02.py` |  |
| 0.22 | 5/23 | 3 | 1.2561s | 0.0563s | 1 | 8 | yes | 1.2184s | 1.2897s | `detyped_files/richards/advanced/proportion_sweep/main_k05_s03.py` |  |
| 0.22 | 5/23 | 4 | 4.3687s | 0.1162s | 1 | 8 | yes | 4.2961s | 4.4476s | `detyped_files/richards/advanced/proportion_sweep/main_k05_s04.py` |  |
| 0.22 | 5/23 | 5 | 1.2747s | 0.0282s | 1 | 8 | yes | 1.2567s | 1.2926s | `detyped_files/richards/advanced/proportion_sweep/main_k05_s05.py` |  |
| 0.22 | 5/23 | 6 | 1.6947s | 0.1072s | 1 | 8 | yes | 1.6253s | 1.7617s | `detyped_files/richards/advanced/proportion_sweep/main_k05_s06.py` |  |
| 0.22 | 5/23 | 7 | 1.7309s | 0.0719s | 1 | 8 | yes | 1.6824s | 1.7761s | `detyped_files/richards/advanced/proportion_sweep/main_k05_s07.py` |  |
| 0.22 | 5/23 | 8 | 2.1982s | 0.0568s | 1 | 8 | yes | 2.1641s | 2.2370s | `detyped_files/richards/advanced/proportion_sweep/main_k05_s08.py` |  |
| 0.22 | 5/23 | 9 | 1.9300s | 0.0960s | 1 | 8 | yes | 1.8658s | 1.9886s | `detyped_files/richards/advanced/proportion_sweep/main_k05_s09.py` |  |
| 0.22 | 5/23 | 10 | 3.8249s | 0.1224s | 1 | 8 | yes | 3.7533s | 3.9103s | `detyped_files/richards/advanced/proportion_sweep/main_k05_s10.py` |  |
| 0.22 | 5/23 | 11 | 1.9717s | 0.0945s | 1 | 8 | yes | 1.9089s | 2.0320s | `detyped_files/richards/advanced/proportion_sweep/main_k05_s11.py` |  |
| 0.22 | 5/23 | 12 | 3.9732s | 0.0977s | 1 | 8 | yes | 3.9035s | 4.0270s | `detyped_files/richards/advanced/proportion_sweep/main_k05_s12.py` |  |
| 0.22 | 5/23 | 13 | 4.2653s | 0.1584s | 1 | 8 | yes | 4.1675s | 4.3758s | `detyped_files/richards/advanced/proportion_sweep/main_k05_s13.py` |  |
| 0.22 | 5/23 | 14 | 1.3421s | 0.0718s | 1 | 8 | yes | 1.2952s | 1.3891s | `detyped_files/richards/advanced/proportion_sweep/main_k05_s14.py` |  |
| 0.22 | 5/23 | 15 | 1.3081s | 0.0812s | 1 | 8 | yes | 1.2569s | 1.3620s | `detyped_files/richards/advanced/proportion_sweep/main_k05_s15.py` |  |
| 0.22 | 5/23 | 16 | 1.8563s | 0.1871s | 1 | 8 | yes | 1.7615s | 1.9939s | `detyped_files/richards/advanced/proportion_sweep/main_k05_s16.py` |  |
| 0.22 | 5/23 | 17 | 1.9914s | 0.0617s | 1 | 8 | yes | 1.9469s | 2.0262s | `detyped_files/richards/advanced/proportion_sweep/main_k05_s17.py` |  |
| 0.22 | 5/23 | 18 | 2.3244s | 0.0621s | 1 | 8 | yes | 2.2841s | 2.3645s | `detyped_files/richards/advanced/proportion_sweep/main_k05_s18.py` |  |
| 0.22 | 5/23 | 19 | 3.9682s | 0.0803s | 1 | 8 | yes | 3.9132s | 4.0165s | `detyped_files/richards/advanced/proportion_sweep/main_k05_s19.py` |  |
| 0.22 | 5/23 | 20 | 1.7884s | 0.0625s | 1 | 8 | yes | 1.7469s | 1.8269s | `detyped_files/richards/advanced/proportion_sweep/main_k05_s20.py` |  |
| 0.26 | 6/23 | 1 | 1.6478s | 0.0990s | 1 | 8 | yes | 1.5859s | 1.7140s | `detyped_files/richards/advanced/proportion_sweep/main_k06_s01.py` |  |
| 0.26 | 6/23 | 2 | 2.2829s | 0.0553s | 1 | 8 | yes | 2.2459s | 2.3167s | `detyped_files/richards/advanced/proportion_sweep/main_k06_s02.py` |  |
| 0.26 | 6/23 | 3 | 2.5008s | 0.0761s | 1 | 8 | yes | 2.4536s | 2.5503s | `detyped_files/richards/advanced/proportion_sweep/main_k06_s03.py` |  |
| 0.26 | 6/23 | 4 | 4.6468s | 0.1358s | 1 | 8 | yes | 4.5653s | 4.7408s | `detyped_files/richards/advanced/proportion_sweep/main_k06_s04.py` |  |
| 0.26 | 6/23 | 5 | 2.5494s | 0.0854s | 1 | 8 | yes | 2.4973s | 2.6064s | `detyped_files/richards/advanced/proportion_sweep/main_k06_s05.py` |  |
| 0.26 | 6/23 | 6 | 1.5080s | 0.0784s | 1 | 8 | yes | 1.4581s | 1.5578s | `detyped_files/richards/advanced/proportion_sweep/main_k06_s06.py` |  |
| 0.26 | 6/23 | 7 | 3.9227s | 0.0943s | 1 | 8 | yes | 3.8626s | 3.9831s | `detyped_files/richards/advanced/proportion_sweep/main_k06_s07.py` |  |
| 0.26 | 6/23 | 8 | 1.4847s | 0.1019s | 1 | 8 | yes | 1.4185s | 1.5495s | `detyped_files/richards/advanced/proportion_sweep/main_k06_s08.py` |  |
| 0.26 | 6/23 | 9 | 2.6570s | 0.0866s | 1 | 8 | yes | 2.6016s | 2.7117s | `detyped_files/richards/advanced/proportion_sweep/main_k06_s09.py` |  |
| 0.26 | 6/23 | 10 | 1.9181s | 0.1029s | 1 | 8 | yes | 1.8484s | 1.9804s | `detyped_files/richards/advanced/proportion_sweep/main_k06_s10.py` |  |
| 0.26 | 6/23 | 11 | 4.5836s | 0.0990s | 1 | 8 | yes | 4.5217s | 4.6487s | `detyped_files/richards/advanced/proportion_sweep/main_k06_s11.py` |  |
| 0.26 | 6/23 | 12 | 3.2464s | 0.1346s | 1 | 8 | yes | 3.1586s | 3.3335s | `detyped_files/richards/advanced/proportion_sweep/main_k06_s12.py` |  |
| 0.26 | 6/23 | 13 | 1.9372s | 0.0529s | 1 | 8 | yes | 1.9092s | 1.9750s | `detyped_files/richards/advanced/proportion_sweep/main_k06_s13.py` |  |
| 0.26 | 6/23 | 14 | 1.8360s | 0.1785s | 1 | 8 | yes | 1.7306s | 1.9610s | `detyped_files/richards/advanced/proportion_sweep/main_k06_s14.py` |  |
| 0.26 | 6/23 | 15 | 2.1700s | 0.1249s | 1 | 8 | yes | 2.0979s | 2.2563s | `detyped_files/richards/advanced/proportion_sweep/main_k06_s15.py` |  |
| 0.26 | 6/23 | 16 | 1.6282s | 0.0658s | 1 | 8 | yes | 1.5921s | 1.6750s | `detyped_files/richards/advanced/proportion_sweep/main_k06_s16.py` |  |
| 0.26 | 6/23 | 17 | 2.0963s | 0.0851s | 1 | 8 | yes | 2.0420s | 2.1514s | `detyped_files/richards/advanced/proportion_sweep/main_k06_s17.py` |  |
| 0.26 | 6/23 | 18 | 1.8877s | 0.1027s | 1 | 8 | yes | 1.8200s | 1.9536s | `detyped_files/richards/advanced/proportion_sweep/main_k06_s18.py` |  |
| 0.26 | 6/23 | 19 | 4.0842s | 0.1196s | 1 | 8 | yes | 4.0061s | 4.1629s | `detyped_files/richards/advanced/proportion_sweep/main_k06_s19.py` |  |
| 0.26 | 6/23 | 20 | 1.3617s | 0.1161s | 1 | 8 | yes | 1.2904s | 1.4403s | `detyped_files/richards/advanced/proportion_sweep/main_k06_s20.py` |  |
| 0.30 | 7/23 | 1 | 1.9831s | 0.0891s | 1 | 8 | yes | 1.9254s | 2.0399s | `detyped_files/richards/advanced/proportion_sweep/main_k07_s01.py` |  |
| 0.30 | 7/23 | 2 | 1.4545s | 0.0733s | 1 | 8 | yes | 1.4051s | 1.4987s | `detyped_files/richards/advanced/proportion_sweep/main_k07_s02.py` |  |
| 0.30 | 7/23 | 3 | 1.5969s | 0.0506s | 1 | 8 | yes | 1.5636s | 1.6288s | `detyped_files/richards/advanced/proportion_sweep/main_k07_s03.py` |  |
| 0.30 | 7/23 | 4 | 2.4970s | 0.1286s | 1 | 8 | yes | 2.4197s | 2.5851s | `detyped_files/richards/advanced/proportion_sweep/main_k07_s04.py` |  |
| 0.30 | 7/23 | 5 | 1.6934s | 0.1581s | 1 | 8 | yes | 1.5944s | 1.7977s | `detyped_files/richards/advanced/proportion_sweep/main_k07_s05.py` |  |
| 0.30 | 7/23 | 6 | 2.2627s | 0.1399s | 1 | 8 | yes | 2.1835s | 2.3641s | `detyped_files/richards/advanced/proportion_sweep/main_k07_s06.py` |  |
| 0.30 | 7/23 | 7 | 1.6280s | 0.0866s | 1 | 8 | yes | 1.5752s | 1.6869s | `detyped_files/richards/advanced/proportion_sweep/main_k07_s07.py` |  |
| 0.30 | 7/23 | 8 | 2.3668s | 0.1175s | 1 | 8 | yes | 2.2973s | 2.4475s | `detyped_files/richards/advanced/proportion_sweep/main_k07_s08.py` |  |
| 0.30 | 7/23 | 9 | 3.8827s | 0.0551s | 1 | 8 | yes | 3.8488s | 3.9194s | `detyped_files/richards/advanced/proportion_sweep/main_k07_s09.py` |  |
| 0.30 | 7/23 | 10 | 4.0145s | 0.1175s | 1 | 8 | yes | 3.9396s | 4.0899s | `detyped_files/richards/advanced/proportion_sweep/main_k07_s10.py` |  |
| 0.30 | 7/23 | 11 | 3.9717s | 0.1294s | 1 | 8 | yes | 3.8991s | 4.0640s | `detyped_files/richards/advanced/proportion_sweep/main_k07_s11.py` |  |
| 0.30 | 7/23 | 12 | 1.4546s | 0.0459s | 1 | 8 | yes | 1.4241s | 1.4836s | `detyped_files/richards/advanced/proportion_sweep/main_k07_s12.py` |  |
| 0.30 | 7/23 | 13 | 4.1057s | 0.1398s | 1 | 8 | yes | 4.0263s | 4.2047s | `detyped_files/richards/advanced/proportion_sweep/main_k07_s13.py` |  |
| 0.30 | 7/23 | 14 | 5.0479s | 0.1172s | 1 | 8 | yes | 4.9813s | 5.1311s | `detyped_files/richards/advanced/proportion_sweep/main_k07_s14.py` |  |
| 0.30 | 7/23 | 15 | 2.5537s | 0.0778s | 1 | 8 | yes | 2.5047s | 2.6064s | `detyped_files/richards/advanced/proportion_sweep/main_k07_s15.py` |  |
| 0.30 | 7/23 | 16 | 1.6521s | 0.0333s | 1 | 8 | yes | 1.6301s | 1.6731s | `detyped_files/richards/advanced/proportion_sweep/main_k07_s16.py` |  |
| 0.30 | 7/23 | 17 | 2.0959s | 0.0568s | 1 | 8 | yes | 2.0566s | 2.1305s | `detyped_files/richards/advanced/proportion_sweep/main_k07_s17.py` |  |
| 0.30 | 7/23 | 18 | 2.2112s | 0.1182s | 1 | 8 | yes | 2.1441s | 2.2927s | `detyped_files/richards/advanced/proportion_sweep/main_k07_s18.py` |  |
| 0.30 | 7/23 | 19 | 2.6473s | 0.1285s | 1 | 8 | yes | 2.5573s | 2.7226s | `detyped_files/richards/advanced/proportion_sweep/main_k07_s19.py` |  |
| 0.30 | 7/23 | 20 | 2.2445s | 0.0907s | 1 | 8 | yes | 2.1921s | 2.3065s | `detyped_files/richards/advanced/proportion_sweep/main_k07_s20.py` |  |
| 0.35 | 8/23 | 1 | 4.7753s | 0.1544s | 1 | 8 | yes | 4.6825s | 4.8798s | `detyped_files/richards/advanced/proportion_sweep/main_k08_s01.py` |  |
| 0.35 | 8/23 | 2 | 4.4445s | 0.1618s | 1 | 8 | yes | 4.3585s | 4.5622s | `detyped_files/richards/advanced/proportion_sweep/main_k08_s02.py` |  |
| 0.35 | 8/23 | 3 | 1.9198s | 0.1157s | 1 | 8 | yes | 1.8530s | 1.9984s | `detyped_files/richards/advanced/proportion_sweep/main_k08_s03.py` |  |
| 0.35 | 8/23 | 4 | 2.5661s | 0.0915s | 1 | 8 | yes | 2.5048s | 2.6203s | `detyped_files/richards/advanced/proportion_sweep/main_k08_s04.py` |  |
| 0.35 | 8/23 | 5 | 2.1117s | 0.0746s | 1 | 8 | yes | 2.0604s | 2.1575s | `detyped_files/richards/advanced/proportion_sweep/main_k08_s05.py` |  |
| 0.35 | 8/23 | 6 | 4.0726s | 0.0640s | 1 | 8 | yes | 4.0307s | 4.1130s | `detyped_files/richards/advanced/proportion_sweep/main_k08_s06.py` |  |
| 0.35 | 8/23 | 7 | 2.2694s | 0.0868s | 1 | 8 | yes | 2.2111s | 2.3236s | `detyped_files/richards/advanced/proportion_sweep/main_k08_s07.py` |  |
| 0.35 | 8/23 | 8 | 2.3167s | 0.0601s | 1 | 8 | yes | 2.2761s | 2.3533s | `detyped_files/richards/advanced/proportion_sweep/main_k08_s08.py` |  |
| 0.35 | 8/23 | 9 | 1.7387s | 0.0939s | 1 | 8 | yes | 1.6783s | 1.7989s | `detyped_files/richards/advanced/proportion_sweep/main_k08_s09.py` |  |
| 0.35 | 8/23 | 10 | 5.1420s | 0.1912s | 1 | 8 | yes | 5.0241s | 5.2745s | `detyped_files/richards/advanced/proportion_sweep/main_k08_s10.py` |  |
| 0.35 | 8/23 | 11 | 4.8148s | 0.1365s | 1 | 8 | yes | 4.7347s | 4.9078s | `detyped_files/richards/advanced/proportion_sweep/main_k08_s11.py` |  |
| 0.35 | 8/23 | 12 | 1.7943s | 0.0692s | 1 | 8 | yes | 1.7471s | 1.8369s | `detyped_files/richards/advanced/proportion_sweep/main_k08_s12.py` |  |
| 0.35 | 8/23 | 13 | 4.2233s | 0.0519s | 1 | 8 | yes | 4.1922s | 4.2601s | `detyped_files/richards/advanced/proportion_sweep/main_k08_s13.py` |  |
| 0.35 | 8/23 | 14 | 2.9057s | 0.1054s | 1 | 8 | yes | 2.8342s | 2.9701s | `detyped_files/richards/advanced/proportion_sweep/main_k08_s14.py` |  |
| 0.35 | 8/23 | 15 | 1.5764s | 0.0952s | 1 | 8 | yes | 1.5174s | 1.6427s | `detyped_files/richards/advanced/proportion_sweep/main_k08_s15.py` |  |
| 0.35 | 8/23 | 16 | 5.0362s | 0.1384s | 1 | 8 | yes | 4.9475s | 5.1260s | `detyped_files/richards/advanced/proportion_sweep/main_k08_s16.py` |  |
| 0.35 | 8/23 | 17 | 2.0061s | 0.0872s | 1 | 8 | yes | 1.9519s | 2.0666s | `detyped_files/richards/advanced/proportion_sweep/main_k08_s17.py` |  |
| 0.35 | 8/23 | 18 | 1.9082s | 0.1119s | 1 | 8 | yes | 1.8366s | 1.9809s | `detyped_files/richards/advanced/proportion_sweep/main_k08_s18.py` |  |
| 0.35 | 8/23 | 19 | 2.0846s | 0.0856s | 1 | 8 | yes | 2.0305s | 2.1405s | `detyped_files/richards/advanced/proportion_sweep/main_k08_s19.py` |  |
| 0.35 | 8/23 | 20 | 4.4220s | 0.1960s | 1 | 8 | yes | 4.3139s | 4.5591s | `detyped_files/richards/advanced/proportion_sweep/main_k08_s20.py` |  |
| 0.39 | 9/23 | 1 | 5.0643s | 0.0960s | 1 | 8 | yes | 5.0005s | 5.1258s | `detyped_files/richards/advanced/proportion_sweep/main_k09_s01.py` |  |
| 0.39 | 9/23 | 2 | 2.6590s | 0.1500s | 1 | 8 | yes | 2.5707s | 2.7638s | `detyped_files/richards/advanced/proportion_sweep/main_k09_s02.py` |  |
| 0.39 | 9/23 | 3 | 5.0200s | 0.0724s | 1 | 8 | yes | 4.9725s | 5.0660s | `detyped_files/richards/advanced/proportion_sweep/main_k09_s03.py` |  |
| 0.39 | 9/23 | 4 | 2.0969s | 0.1712s | 1 | 8 | yes | 1.9977s | 2.2151s | `detyped_files/richards/advanced/proportion_sweep/main_k09_s04.py` |  |
| 0.39 | 9/23 | 5 | 4.8157s | 0.1131s | 1 | 8 | yes | 4.7416s | 4.8883s | `detyped_files/richards/advanced/proportion_sweep/main_k09_s05.py` |  |
| 0.39 | 9/23 | 6 | 4.0854s | 0.1196s | 1 | 8 | yes | 4.0129s | 4.1664s | `detyped_files/richards/advanced/proportion_sweep/main_k09_s06.py` |  |
| 0.39 | 9/23 | 7 | 4.4845s | 0.1839s | 1 | 8 | yes | 4.3743s | 4.6105s | `detyped_files/richards/advanced/proportion_sweep/main_k09_s07.py` |  |
| 0.39 | 9/23 | 8 | 2.7609s | 0.1427s | 1 | 8 | yes | 2.6753s | 2.8603s | `detyped_files/richards/advanced/proportion_sweep/main_k09_s08.py` |  |
| 0.39 | 9/23 | 9 | 4.3712s | 0.1435s | 1 | 8 | yes | 4.2866s | 4.4722s | `detyped_files/richards/advanced/proportion_sweep/main_k09_s09.py` |  |
| 0.39 | 9/23 | 10 | 2.3839s | 0.0973s | 1 | 8 | yes | 2.3223s | 2.4493s | `detyped_files/richards/advanced/proportion_sweep/main_k09_s10.py` |  |
| 0.39 | 9/23 | 11 | 3.0356s | 0.0805s | 1 | 8 | yes | 2.9806s | 3.0849s | `detyped_files/richards/advanced/proportion_sweep/main_k09_s11.py` |  |
| 0.39 | 9/23 | 12 | 2.1346s | 0.1124s | 1 | 8 | yes | 2.0670s | 2.2124s | `detyped_files/richards/advanced/proportion_sweep/main_k09_s12.py` |  |
| 0.39 | 9/23 | 13 | 4.6801s | 0.0971s | 1 | 8 | yes | 4.6195s | 4.7442s | `detyped_files/richards/advanced/proportion_sweep/main_k09_s13.py` |  |
| 0.39 | 9/23 | 14 | 5.2449s | 0.2254s | 1 | 8 | yes | 5.1124s | 5.4019s | `detyped_files/richards/advanced/proportion_sweep/main_k09_s14.py` |  |
| 0.39 | 9/23 | 15 | 5.3382s | 0.0672s | 1 | 8 | yes | 5.2941s | 5.3816s | `detyped_files/richards/advanced/proportion_sweep/main_k09_s15.py` |  |
| 0.39 | 9/23 | 16 | 2.6583s | 0.1182s | 1 | 8 | yes | 2.5861s | 2.7421s | `detyped_files/richards/advanced/proportion_sweep/main_k09_s16.py` |  |
| 0.39 | 9/23 | 17 | 4.6671s | 0.1107s | 1 | 8 | yes | 4.5930s | 4.7359s | `detyped_files/richards/advanced/proportion_sweep/main_k09_s17.py` |  |
| 0.39 | 9/23 | 18 | 4.1416s | 0.0758s | 1 | 8 | yes | 4.0897s | 4.1887s | `detyped_files/richards/advanced/proportion_sweep/main_k09_s18.py` |  |
| 0.39 | 9/23 | 19 | 4.4321s | 0.1688s | 1 | 8 | yes | 4.3460s | 4.5563s | `detyped_files/richards/advanced/proportion_sweep/main_k09_s19.py` |  |
| 0.39 | 9/23 | 20 | 2.1409s | 0.0923s | 1 | 8 | yes | 2.0784s | 2.1994s | `detyped_files/richards/advanced/proportion_sweep/main_k09_s20.py` |  |
| 0.43 | 10/23 | 1 | 2.8828s | 0.1466s | 1 | 8 | yes | 2.8034s | 2.9896s | `detyped_files/richards/advanced/proportion_sweep/main_k10_s01.py` |  |
| 0.43 | 10/23 | 2 | 2.4086s | 0.0306s | 1 | 8 | yes | 2.3889s | 2.4284s | `detyped_files/richards/advanced/proportion_sweep/main_k10_s02.py` |  |
| 0.43 | 10/23 | 3 | 5.1376s | 0.1219s | 1 | 8 | yes | 5.0637s | 5.2215s | `detyped_files/richards/advanced/proportion_sweep/main_k10_s03.py` |  |
| 0.43 | 10/23 | 4 | 5.2414s | 0.2299s | 1 | 8 | yes | 5.1192s | 5.4076s | `detyped_files/richards/advanced/proportion_sweep/main_k10_s04.py` |  |
| 0.43 | 10/23 | 5 | 2.5830s | 0.0929s | 1 | 8 | yes | 2.5261s | 2.6462s | `detyped_files/richards/advanced/proportion_sweep/main_k10_s05.py` |  |
| 0.43 | 10/23 | 6 | 4.6133s | 0.1841s | 1 | 8 | yes | 4.5074s | 4.7373s | `detyped_files/richards/advanced/proportion_sweep/main_k10_s06.py` |  |
| 0.43 | 10/23 | 7 | 4.3221s | 0.1451s | 1 | 8 | yes | 4.2237s | 4.4110s | `detyped_files/richards/advanced/proportion_sweep/main_k10_s07.py` |  |
| 0.43 | 10/23 | 8 | 2.6594s | 0.1239s | 1 | 8 | yes | 2.5790s | 2.7396s | `detyped_files/richards/advanced/proportion_sweep/main_k10_s08.py` |  |
| 0.43 | 10/23 | 9 | 2.4909s | 0.0609s | 1 | 8 | yes | 2.4517s | 2.5304s | `detyped_files/richards/advanced/proportion_sweep/main_k10_s09.py` |  |
| 0.43 | 10/23 | 10 | 2.6738s | 0.1325s | 1 | 8 | yes | 2.5827s | 2.7560s | `detyped_files/richards/advanced/proportion_sweep/main_k10_s10.py` |  |
| 0.43 | 10/23 | 11 | 4.8978s | 0.1504s | 1 | 8 | yes | 4.8147s | 5.0073s | `detyped_files/richards/advanced/proportion_sweep/main_k10_s11.py` |  |
| 0.43 | 10/23 | 12 | 2.2889s | 0.1038s | 1 | 8 | yes | 2.2279s | 2.3617s | `detyped_files/richards/advanced/proportion_sweep/main_k10_s12.py` |  |
| 0.43 | 10/23 | 13 | 4.9102s | 0.1364s | 1 | 8 | yes | 4.8187s | 4.9988s | `detyped_files/richards/advanced/proportion_sweep/main_k10_s13.py` |  |
| 0.43 | 10/23 | 14 | 4.9661s | 0.1584s | 1 | 8 | yes | 4.8678s | 5.0714s | `detyped_files/richards/advanced/proportion_sweep/main_k10_s14.py` |  |
| 0.43 | 10/23 | 15 | 2.2919s | 0.0686s | 1 | 8 | yes | 2.2509s | 2.3379s | `detyped_files/richards/advanced/proportion_sweep/main_k10_s15.py` |  |
| 0.43 | 10/23 | 16 | 4.7687s | 0.0457s | 1 | 8 | yes | 4.7385s | 4.7978s | `detyped_files/richards/advanced/proportion_sweep/main_k10_s16.py` |  |
| 0.43 | 10/23 | 17 | 2.5268s | 0.0347s | 1 | 8 | yes | 2.5048s | 2.5497s | `detyped_files/richards/advanced/proportion_sweep/main_k10_s17.py` |  |
| 0.43 | 10/23 | 18 | 4.2222s | 0.1007s | 1 | 8 | yes | 4.1601s | 4.2895s | `detyped_files/richards/advanced/proportion_sweep/main_k10_s18.py` |  |
| 0.43 | 10/23 | 19 | 2.5632s | 0.0401s | 1 | 8 | yes | 2.5382s | 2.5893s | `detyped_files/richards/advanced/proportion_sweep/main_k10_s19.py` |  |
| 0.43 | 10/23 | 20 | 1.7903s | 0.0824s | 1 | 8 | yes | 1.7390s | 1.8456s | `detyped_files/richards/advanced/proportion_sweep/main_k10_s20.py` |  |
| 0.48 | 11/23 | 1 | 5.3214s | 0.1648s | 1 | 8 | yes | 5.2365s | 5.4420s | `detyped_files/richards/advanced/proportion_sweep/main_k11_s01.py` |  |
| 0.48 | 11/23 | 2 | 3.1900s | 0.0763s | 1 | 8 | yes | 3.1419s | 3.2417s | `detyped_files/richards/advanced/proportion_sweep/main_k11_s02.py` |  |
| 0.48 | 11/23 | 3 | 4.4485s | 0.1368s | 1 | 8 | yes | 4.3630s | 4.5377s | `detyped_files/richards/advanced/proportion_sweep/main_k11_s03.py` |  |
| 0.48 | 11/23 | 4 | 3.4140s | 0.0811s | 1 | 8 | yes | 3.3654s | 3.4677s | `detyped_files/richards/advanced/proportion_sweep/main_k11_s04.py` |  |
| 0.48 | 11/23 | 5 | 5.0133s | 0.1233s | 1 | 8 | yes | 4.9364s | 5.0941s | `detyped_files/richards/advanced/proportion_sweep/main_k11_s05.py` |  |
| 0.48 | 11/23 | 6 | 4.9093s | 0.2435s | 1 | 8 | yes | 4.7657s | 5.0747s | `detyped_files/richards/advanced/proportion_sweep/main_k11_s06.py` |  |
| 0.48 | 11/23 | 7 | 5.2308s | 0.1231s | 1 | 8 | yes | 5.1480s | 5.3052s | `detyped_files/richards/advanced/proportion_sweep/main_k11_s07.py` |  |
| 0.48 | 11/23 | 8 | 5.5819s | 0.1868s | 1 | 8 | yes | 5.4619s | 5.7021s | `detyped_files/richards/advanced/proportion_sweep/main_k11_s08.py` |  |
| 0.48 | 11/23 | 9 | 5.2046s | 0.0952s | 1 | 8 | yes | 5.1446s | 5.2682s | `detyped_files/richards/advanced/proportion_sweep/main_k11_s09.py` |  |
| 0.48 | 11/23 | 10 | 4.1132s | 0.1463s | 1 | 8 | yes | 4.0124s | 4.2030s | `detyped_files/richards/advanced/proportion_sweep/main_k11_s10.py` |  |
| 0.48 | 11/23 | 11 | 2.2847s | 0.0783s | 1 | 8 | yes | 2.2335s | 2.3335s | `detyped_files/richards/advanced/proportion_sweep/main_k11_s11.py` |  |
| 0.48 | 11/23 | 12 | 3.0020s | 0.1118s | 1 | 8 | yes | 2.9357s | 3.0809s | `detyped_files/richards/advanced/proportion_sweep/main_k11_s12.py` |  |
| 0.48 | 11/23 | 13 | 2.9531s | 0.0906s | 1 | 8 | yes | 2.8924s | 3.0096s | `detyped_files/richards/advanced/proportion_sweep/main_k11_s13.py` |  |
| 0.48 | 11/23 | 14 | 5.2029s | 0.0944s | 1 | 8 | yes | 5.1436s | 5.2685s | `detyped_files/richards/advanced/proportion_sweep/main_k11_s14.py` |  |
| 0.48 | 11/23 | 15 | 4.9003s | 0.0800s | 1 | 8 | yes | 4.8465s | 4.9493s | `detyped_files/richards/advanced/proportion_sweep/main_k11_s15.py` |  |
| 0.48 | 11/23 | 16 | 5.0438s | 0.1653s | 1 | 8 | yes | 4.9462s | 5.1565s | `detyped_files/richards/advanced/proportion_sweep/main_k11_s16.py` |  |
| 0.48 | 11/23 | 17 | 2.7792s | 0.1144s | 1 | 8 | yes | 2.7027s | 2.8478s | `detyped_files/richards/advanced/proportion_sweep/main_k11_s17.py` |  |
| 0.48 | 11/23 | 18 | 2.0376s | 0.1320s | 1 | 8 | yes | 1.9605s | 2.1294s | `detyped_files/richards/advanced/proportion_sweep/main_k11_s18.py` |  |
| 0.48 | 11/23 | 19 | 4.1843s | 0.1473s | 1 | 8 | yes | 4.0983s | 4.2916s | `detyped_files/richards/advanced/proportion_sweep/main_k11_s19.py` |  |
| 0.48 | 11/23 | 20 | 3.2008s | 0.1341s | 1 | 8 | yes | 3.1187s | 3.2907s | `detyped_files/richards/advanced/proportion_sweep/main_k11_s20.py` |  |
| 0.52 | 12/23 | 1 | 3.3749s | 0.1282s | 1 | 8 | yes | 3.2891s | 3.4548s | `detyped_files/richards/advanced/proportion_sweep/main_k12_s01.py` |  |
| 0.52 | 12/23 | 2 | 4.2468s | 0.0680s | 1 | 8 | yes | 4.2052s | 4.2929s | `detyped_files/richards/advanced/proportion_sweep/main_k12_s02.py` |  |
| 0.52 | 12/23 | 3 | 4.9868s | 0.1472s | 1 | 8 | yes | 4.8927s | 5.0818s | `detyped_files/richards/advanced/proportion_sweep/main_k12_s03.py` |  |
| 0.52 | 12/23 | 4 | 5.0010s | 0.0940s | 1 | 8 | yes | 4.9448s | 5.0673s | `detyped_files/richards/advanced/proportion_sweep/main_k12_s04.py` |  |
| 0.52 | 12/23 | 5 | 2.8121s | 0.0830s | 1 | 8 | yes | 2.7588s | 2.8652s | `detyped_files/richards/advanced/proportion_sweep/main_k12_s05.py` |  |
| 0.52 | 12/23 | 6 | 2.4926s | 0.0653s | 1 | 8 | yes | 2.4506s | 2.5356s | `detyped_files/richards/advanced/proportion_sweep/main_k12_s06.py` |  |
| 0.52 | 12/23 | 7 | 4.3847s | 0.1084s | 1 | 8 | yes | 4.3174s | 4.4548s | `detyped_files/richards/advanced/proportion_sweep/main_k12_s07.py` |  |
| 0.52 | 12/23 | 8 | 5.1325s | 0.1001s | 1 | 8 | yes | 5.0678s | 5.1971s | `detyped_files/richards/advanced/proportion_sweep/main_k12_s08.py` |  |
| 0.52 | 12/23 | 9 | 4.8795s | 0.0897s | 1 | 8 | yes | 4.8213s | 4.9369s | `detyped_files/richards/advanced/proportion_sweep/main_k12_s09.py` |  |
| 0.52 | 12/23 | 10 | 4.7449s | 0.1311s | 1 | 8 | yes | 4.6634s | 4.8285s | `detyped_files/richards/advanced/proportion_sweep/main_k12_s10.py` |  |
| 0.52 | 12/23 | 11 | 2.0833s | 0.1232s | 1 | 8 | yes | 2.0061s | 2.1622s | `detyped_files/richards/advanced/proportion_sweep/main_k12_s11.py` |  |
| 0.52 | 12/23 | 12 | 5.7321s | 0.0712s | 1 | 8 | yes | 5.6868s | 5.7782s | `detyped_files/richards/advanced/proportion_sweep/main_k12_s12.py` |  |
| 0.52 | 12/23 | 13 | 5.1510s | 0.1648s | 1 | 8 | yes | 5.0393s | 5.2471s | `detyped_files/richards/advanced/proportion_sweep/main_k12_s13.py` |  |
| 0.52 | 12/23 | 14 | 5.4226s | 0.0905s | 1 | 8 | yes | 5.3606s | 5.4757s | `detyped_files/richards/advanced/proportion_sweep/main_k12_s14.py` |  |
| 0.52 | 12/23 | 15 | 2.2349s | 0.0436s | 1 | 8 | yes | 2.2054s | 2.2615s | `detyped_files/richards/advanced/proportion_sweep/main_k12_s15.py` |  |
| 0.52 | 12/23 | 16 | 5.0373s | 0.1521s | 1 | 8 | yes | 4.9419s | 5.1361s | `detyped_files/richards/advanced/proportion_sweep/main_k12_s16.py` |  |
| 0.52 | 12/23 | 17 | 5.7424s | 0.0964s | 1 | 8 | yes | 5.6799s | 5.8074s | `detyped_files/richards/advanced/proportion_sweep/main_k12_s17.py` |  |
| 0.52 | 12/23 | 18 | 4.5961s | 0.0639s | 1 | 8 | yes | 4.5504s | 4.6326s | `detyped_files/richards/advanced/proportion_sweep/main_k12_s18.py` |  |
| 0.52 | 12/23 | 19 | 2.3632s | 0.0743s | 1 | 8 | yes | 2.3154s | 2.4132s | `detyped_files/richards/advanced/proportion_sweep/main_k12_s19.py` |  |
| 0.52 | 12/23 | 20 | 2.4224s | 0.0651s | 1 | 8 | yes | 2.3803s | 2.4646s | `detyped_files/richards/advanced/proportion_sweep/main_k12_s20.py` |  |
| 0.57 | 13/23 | 1 | 2.4200s | 0.0524s | 1 | 8 | yes | 2.3874s | 2.4545s | `detyped_files/richards/advanced/proportion_sweep/main_k13_s01.py` |  |
| 0.57 | 13/23 | 2 | 4.7007s | 0.1017s | 1 | 8 | yes | 4.6328s | 4.7621s | `detyped_files/richards/advanced/proportion_sweep/main_k13_s02.py` |  |
| 0.57 | 13/23 | 3 | 5.9988s | 0.0967s | 1 | 8 | yes | 5.9343s | 6.0571s | `detyped_files/richards/advanced/proportion_sweep/main_k13_s03.py` |  |
| 0.57 | 13/23 | 4 | 5.3992s | 0.2321s | 1 | 8 | yes | 5.2702s | 5.5728s | `detyped_files/richards/advanced/proportion_sweep/main_k13_s04.py` |  |
| 0.57 | 13/23 | 5 | 2.7284s | 0.1369s | 1 | 8 | yes | 2.6509s | 2.8216s | `detyped_files/richards/advanced/proportion_sweep/main_k13_s05.py` |  |
| 0.57 | 13/23 | 6 | 4.7100s | 0.1694s | 1 | 8 | yes | 4.5983s | 4.8164s | `detyped_files/richards/advanced/proportion_sweep/main_k13_s06.py` |  |
| 0.57 | 13/23 | 7 | 3.1314s | 0.1155s | 1 | 8 | yes | 3.0588s | 3.2102s | `detyped_files/richards/advanced/proportion_sweep/main_k13_s07.py` |  |
| 0.57 | 13/23 | 8 | 2.9095s | 0.0626s | 1 | 8 | yes | 2.8697s | 2.9502s | `detyped_files/richards/advanced/proportion_sweep/main_k13_s08.py` |  |
| 0.57 | 13/23 | 9 | 4.7240s | 0.1353s | 1 | 8 | yes | 4.6399s | 4.8139s | `detyped_files/richards/advanced/proportion_sweep/main_k13_s09.py` |  |
| 0.57 | 13/23 | 10 | 3.4479s | 0.0468s | 1 | 8 | yes | 3.4201s | 3.4800s | `detyped_files/richards/advanced/proportion_sweep/main_k13_s10.py` |  |
| 0.57 | 13/23 | 11 | 5.2727s | 0.1042s | 1 | 8 | yes | 5.2054s | 5.3389s | `detyped_files/richards/advanced/proportion_sweep/main_k13_s11.py` |  |
| 0.57 | 13/23 | 12 | 5.4303s | 0.1606s | 1 | 8 | yes | 5.3369s | 5.5421s | `detyped_files/richards/advanced/proportion_sweep/main_k13_s12.py` |  |
| 0.57 | 13/23 | 13 | 5.2018s | 0.1369s | 1 | 8 | yes | 5.1247s | 5.2983s | `detyped_files/richards/advanced/proportion_sweep/main_k13_s13.py` |  |
| 0.57 | 13/23 | 14 | 2.7911s | 0.1284s | 1 | 8 | yes | 2.7097s | 2.8780s | `detyped_files/richards/advanced/proportion_sweep/main_k13_s14.py` |  |
| 0.57 | 13/23 | 15 | 5.3866s | 0.1028s | 1 | 8 | yes | 5.3225s | 5.4550s | `detyped_files/richards/advanced/proportion_sweep/main_k13_s15.py` |  |
| 0.57 | 13/23 | 16 | 5.6375s | 0.1389s | 1 | 8 | yes | 5.5508s | 5.7299s | `detyped_files/richards/advanced/proportion_sweep/main_k13_s16.py` |  |
| 0.57 | 13/23 | 17 | 5.0644s | 0.0986s | 1 | 8 | yes | 5.0076s | 5.1330s | `detyped_files/richards/advanced/proportion_sweep/main_k13_s17.py` |  |
| 0.57 | 13/23 | 18 | 5.0220s | 0.1105s | 1 | 8 | yes | 4.9489s | 5.0919s | `detyped_files/richards/advanced/proportion_sweep/main_k13_s18.py` |  |
| 0.57 | 13/23 | 19 | 5.2401s | 0.0938s | 1 | 8 | yes | 5.1758s | 5.2978s | `detyped_files/richards/advanced/proportion_sweep/main_k13_s19.py` |  |
| 0.57 | 13/23 | 20 | 2.3219s | 0.1278s | 1 | 8 | yes | 2.2560s | 2.4135s | `detyped_files/richards/advanced/proportion_sweep/main_k13_s20.py` |  |
| 0.61 | 14/23 | 1 | 2.8913s | 0.1062s | 1 | 8 | yes | 2.8242s | 2.9640s | `detyped_files/richards/advanced/proportion_sweep/main_k14_s01.py` |  |
| 0.61 | 14/23 | 2 | 5.0777s | 0.1628s | 1 | 8 | yes | 4.9770s | 5.1880s | `detyped_files/richards/advanced/proportion_sweep/main_k14_s02.py` |  |
| 0.61 | 14/23 | 3 | 3.1194s | 0.0862s | 1 | 8 | yes | 3.0692s | 3.1803s | `detyped_files/richards/advanced/proportion_sweep/main_k14_s03.py` |  |
| 0.61 | 14/23 | 4 | 2.8563s | 0.1539s | 1 | 8 | yes | 2.7657s | 2.9623s | `detyped_files/richards/advanced/proportion_sweep/main_k14_s04.py` |  |
| 0.61 | 14/23 | 5 | 5.7591s | 0.2306s | 1 | 8 | yes | 5.6156s | 5.9087s | `detyped_files/richards/advanced/proportion_sweep/main_k14_s05.py` |  |
| 0.61 | 14/23 | 6 | 3.2111s | 0.1055s | 1 | 8 | yes | 3.1404s | 3.2787s | `detyped_files/richards/advanced/proportion_sweep/main_k14_s06.py` |  |
| 0.61 | 14/23 | 7 | 2.2168s | 0.1110s | 1 | 8 | yes | 2.1451s | 2.2893s | `detyped_files/richards/advanced/proportion_sweep/main_k14_s07.py` |  |
| 0.61 | 14/23 | 8 | 5.7946s | 0.2492s | 1 | 8 | yes | 5.6454s | 5.9629s | `detyped_files/richards/advanced/proportion_sweep/main_k14_s08.py` |  |
| 0.61 | 14/23 | 9 | 5.5562s | 0.1675s | 1 | 8 | yes | 5.4609s | 5.6749s | `detyped_files/richards/advanced/proportion_sweep/main_k14_s09.py` |  |
| 0.61 | 14/23 | 10 | 3.3919s | 0.0619s | 1 | 8 | yes | 3.3512s | 3.4302s | `detyped_files/richards/advanced/proportion_sweep/main_k14_s10.py` |  |
| 0.61 | 14/23 | 11 | 5.2249s | 0.2358s | 1 | 8 | yes | 5.0823s | 5.3852s | `detyped_files/richards/advanced/proportion_sweep/main_k14_s11.py` |  |
| 0.61 | 14/23 | 12 | 5.9204s | 0.1388s | 1 | 8 | yes | 5.8323s | 6.0109s | `detyped_files/richards/advanced/proportion_sweep/main_k14_s12.py` |  |
| 0.61 | 14/23 | 13 | 2.8711s | 0.0575s | 1 | 8 | yes | 2.8347s | 2.9072s | `detyped_files/richards/advanced/proportion_sweep/main_k14_s13.py` |  |
| 0.61 | 14/23 | 14 | 2.5708s | 0.0745s | 1 | 8 | yes | 2.5252s | 2.6201s | `detyped_files/richards/advanced/proportion_sweep/main_k14_s14.py` |  |
| 0.61 | 14/23 | 15 | 5.0772s | 0.0543s | 1 | 8 | yes | 5.0461s | 5.1161s | `detyped_files/richards/advanced/proportion_sweep/main_k14_s15.py` |  |
| 0.61 | 14/23 | 16 | 4.7950s | 0.1500s | 1 | 8 | yes | 4.7045s | 4.8980s | `detyped_files/richards/advanced/proportion_sweep/main_k14_s16.py` |  |
| 0.61 | 14/23 | 17 | 5.4357s | 0.1674s | 1 | 8 | yes | 5.3331s | 5.5487s | `detyped_files/richards/advanced/proportion_sweep/main_k14_s17.py` |  |
| 0.61 | 14/23 | 18 | 5.3849s | 0.2009s | 1 | 8 | yes | 5.2798s | 5.5291s | `detyped_files/richards/advanced/proportion_sweep/main_k14_s18.py` |  |
| 0.61 | 14/23 | 19 | 2.5890s | 0.0577s | 1 | 8 | yes | 2.5505s | 2.6243s | `detyped_files/richards/advanced/proportion_sweep/main_k14_s19.py` |  |
| 0.61 | 14/23 | 20 | 2.6053s | 0.1157s | 1 | 8 | yes | 2.5322s | 2.6814s | `detyped_files/richards/advanced/proportion_sweep/main_k14_s20.py` |  |
| 0.65 | 15/23 | 1 | 2.7954s | 0.1580s | 1 | 8 | yes | 2.7138s | 2.9089s | `detyped_files/richards/advanced/proportion_sweep/main_k15_s01.py` |  |
| 0.65 | 15/23 | 2 | 3.1305s | 0.1185s | 1 | 8 | yes | 3.0530s | 3.2042s | `detyped_files/richards/advanced/proportion_sweep/main_k15_s02.py` |  |
| 0.65 | 15/23 | 3 | 6.1360s | 0.2207s | 1 | 8 | yes | 6.0035s | 6.2870s | `detyped_files/richards/advanced/proportion_sweep/main_k15_s03.py` |  |
| 0.65 | 15/23 | 4 | 2.8962s | 0.0679s | 1 | 8 | yes | 2.8543s | 2.9417s | `detyped_files/richards/advanced/proportion_sweep/main_k15_s04.py` |  |
| 0.65 | 15/23 | 5 | 5.6944s | 0.1491s | 1 | 8 | yes | 5.5959s | 5.7876s | `detyped_files/richards/advanced/proportion_sweep/main_k15_s05.py` |  |
| 0.65 | 15/23 | 6 | 5.7037s | 0.2161s | 1 | 8 | yes | 5.5712s | 5.8489s | `detyped_files/richards/advanced/proportion_sweep/main_k15_s06.py` |  |
| 0.65 | 15/23 | 7 | 5.5557s | 0.0791s | 1 | 8 | yes | 5.5063s | 5.6082s | `detyped_files/richards/advanced/proportion_sweep/main_k15_s07.py` |  |
| 0.65 | 15/23 | 8 | 4.9152s | 0.1430s | 1 | 8 | yes | 4.8162s | 5.0005s | `detyped_files/richards/advanced/proportion_sweep/main_k15_s08.py` |  |
| 0.65 | 15/23 | 9 | 5.4520s | 0.1541s | 1 | 8 | yes | 5.3559s | 5.5544s | `detyped_files/richards/advanced/proportion_sweep/main_k15_s09.py` |  |
| 0.65 | 15/23 | 10 | 2.5326s | 0.0879s | 1 | 8 | yes | 2.4745s | 2.5868s | `detyped_files/richards/advanced/proportion_sweep/main_k15_s10.py` |  |
| 0.65 | 15/23 | 11 | 5.0668s | 0.0886s | 1 | 8 | yes | 5.0128s | 5.1244s | `detyped_files/richards/advanced/proportion_sweep/main_k15_s11.py` |  |
| 0.65 | 15/23 | 12 | 5.7801s | 0.0697s | 1 | 8 | yes | 5.7343s | 5.8237s | `detyped_files/richards/advanced/proportion_sweep/main_k15_s12.py` |  |
| 0.65 | 15/23 | 13 | 5.6666s | 0.1162s | 1 | 8 | yes | 5.5896s | 5.7400s | `detyped_files/richards/advanced/proportion_sweep/main_k15_s13.py` |  |
| 0.65 | 15/23 | 14 | 5.1682s | 0.2218s | 1 | 8 | yes | 5.0502s | 5.3283s | `detyped_files/richards/advanced/proportion_sweep/main_k15_s14.py` |  |
| 0.65 | 15/23 | 15 | 5.7946s | 0.1935s | 1 | 8 | yes | 5.6725s | 5.9232s | `detyped_files/richards/advanced/proportion_sweep/main_k15_s15.py` |  |
| 0.65 | 15/23 | 16 | 4.8769s | 0.1799s | 1 | 8 | yes | 4.7695s | 4.9940s | `detyped_files/richards/advanced/proportion_sweep/main_k15_s16.py` |  |
| 0.65 | 15/23 | 17 | 5.2260s | 0.1531s | 1 | 8 | yes | 5.1331s | 5.3301s | `detyped_files/richards/advanced/proportion_sweep/main_k15_s17.py` |  |
| 0.65 | 15/23 | 18 | 5.0577s | 0.0686s | 1 | 8 | yes | 5.0154s | 5.1040s | `detyped_files/richards/advanced/proportion_sweep/main_k15_s18.py` |  |
| 0.65 | 15/23 | 19 | 5.5427s | 0.0961s | 1 | 8 | yes | 5.4788s | 5.6035s | `detyped_files/richards/advanced/proportion_sweep/main_k15_s19.py` |  |
| 0.65 | 15/23 | 20 | 4.2001s | 0.1038s | 1 | 8 | yes | 4.1374s | 4.2723s | `detyped_files/richards/advanced/proportion_sweep/main_k15_s20.py` |  |
| 0.70 | 16/23 | 1 | 2.3316s | 0.0410s | 1 | 8 | yes | 2.3054s | 2.3578s | `detyped_files/richards/advanced/proportion_sweep/main_k16_s01.py` |  |
| 0.70 | 16/23 | 2 | 3.3785s | 0.1166s | 1 | 8 | yes | 3.3092s | 3.4585s | `detyped_files/richards/advanced/proportion_sweep/main_k16_s02.py` |  |
| 0.70 | 16/23 | 3 | 3.4119s | 0.1315s | 1 | 8 | yes | 3.3270s | 3.4966s | `detyped_files/richards/advanced/proportion_sweep/main_k16_s03.py` |  |
| 0.70 | 16/23 | 4 | 3.4952s | 0.0568s | 1 | 8 | yes | 3.4576s | 3.5323s | `detyped_files/richards/advanced/proportion_sweep/main_k16_s04.py` |  |
| 0.70 | 16/23 | 5 | 5.1688s | 0.1646s | 1 | 8 | yes | 5.0629s | 5.2753s | `detyped_files/richards/advanced/proportion_sweep/main_k16_s05.py` |  |
| 0.70 | 16/23 | 6 | 4.5859s | 0.1265s | 1 | 8 | yes | 4.4998s | 4.6611s | `detyped_files/richards/advanced/proportion_sweep/main_k16_s06.py` |  |
| 0.70 | 16/23 | 7 | 3.1316s | 0.1277s | 1 | 8 | yes | 3.0517s | 3.2173s | `detyped_files/richards/advanced/proportion_sweep/main_k16_s07.py` |  |
| 0.70 | 16/23 | 8 | 2.2900s | 0.1234s | 1 | 8 | yes | 2.2118s | 2.3715s | `detyped_files/richards/advanced/proportion_sweep/main_k16_s08.py` |  |
| 0.70 | 16/23 | 9 | 5.4181s | 0.2042s | 1 | 8 | yes | 5.2975s | 5.5544s | `detyped_files/richards/advanced/proportion_sweep/main_k16_s09.py` |  |
| 0.70 | 16/23 | 10 | 6.0067s | 0.2347s | 1 | 8 | yes | 5.8721s | 6.1710s | `detyped_files/richards/advanced/proportion_sweep/main_k16_s10.py` |  |
| 0.70 | 16/23 | 11 | 3.3141s | 0.0724s | 1 | 8 | yes | 3.2738s | 3.3652s | `detyped_files/richards/advanced/proportion_sweep/main_k16_s11.py` |  |
| 0.70 | 16/23 | 12 | 6.0222s | 0.1201s | 1 | 8 | yes | 5.9462s | 6.1019s | `detyped_files/richards/advanced/proportion_sweep/main_k16_s12.py` |  |
| 0.70 | 16/23 | 13 | 5.6800s | 0.2280s | 1 | 8 | yes | 5.5540s | 5.8417s | `detyped_files/richards/advanced/proportion_sweep/main_k16_s13.py` |  |
| 0.70 | 16/23 | 14 | 2.8786s | 0.0647s | 1 | 8 | yes | 2.8346s | 2.9183s | `detyped_files/richards/advanced/proportion_sweep/main_k16_s14.py` |  |
| 0.70 | 16/23 | 15 | 5.7892s | 0.1444s | 1 | 8 | yes | 5.7032s | 5.8856s | `detyped_files/richards/advanced/proportion_sweep/main_k16_s15.py` |  |
| 0.70 | 16/23 | 16 | 4.6779s | 0.1689s | 1 | 8 | yes | 4.5752s | 4.7885s | `detyped_files/richards/advanced/proportion_sweep/main_k16_s16.py` |  |
| 0.70 | 16/23 | 17 | 5.6945s | 0.0836s | 1 | 8 | yes | 5.6429s | 5.7499s | `detyped_files/richards/advanced/proportion_sweep/main_k16_s17.py` |  |
| 0.70 | 16/23 | 18 | 3.0963s | 0.0412s | 1 | 8 | yes | 3.0676s | 3.1198s | `detyped_files/richards/advanced/proportion_sweep/main_k16_s18.py` |  |
| 0.70 | 16/23 | 19 | 3.2672s | 0.0719s | 1 | 8 | yes | 3.2187s | 3.3110s | `detyped_files/richards/advanced/proportion_sweep/main_k16_s19.py` |  |
| 0.70 | 16/23 | 20 | 5.2766s | 0.1672s | 1 | 8 | yes | 5.1849s | 5.3972s | `detyped_files/richards/advanced/proportion_sweep/main_k16_s20.py` |  |
| 0.74 | 17/23 | 1 | 4.7169s | 0.1105s | 1 | 8 | yes | 4.6498s | 4.7924s | `detyped_files/richards/advanced/proportion_sweep/main_k17_s01.py` |  |
| 0.74 | 17/23 | 2 | 5.8791s | 0.1703s | 1 | 8 | yes | 5.7821s | 6.0011s | `detyped_files/richards/advanced/proportion_sweep/main_k17_s02.py` |  |
| 0.74 | 17/23 | 3 | 5.8566s | 0.1978s | 1 | 8 | yes | 5.7268s | 5.9823s | `detyped_files/richards/advanced/proportion_sweep/main_k17_s03.py` |  |
| 0.74 | 17/23 | 4 | 3.1921s | 0.1169s | 1 | 8 | yes | 3.1191s | 3.2708s | `detyped_files/richards/advanced/proportion_sweep/main_k17_s04.py` |  |
| 0.74 | 17/23 | 5 | 4.7925s | 0.1353s | 1 | 8 | yes | 4.7146s | 4.8901s | `detyped_files/richards/advanced/proportion_sweep/main_k17_s05.py` |  |
| 0.74 | 17/23 | 6 | 5.7987s | 0.1409s | 1 | 8 | yes | 5.7181s | 5.9018s | `detyped_files/richards/advanced/proportion_sweep/main_k17_s06.py` |  |
| 0.74 | 17/23 | 7 | 5.3525s | 0.1679s | 1 | 8 | yes | 5.2507s | 5.4655s | `detyped_files/richards/advanced/proportion_sweep/main_k17_s07.py` |  |
| 0.74 | 17/23 | 8 | 5.7984s | 0.1718s | 1 | 8 | yes | 5.6873s | 5.9074s | `detyped_files/richards/advanced/proportion_sweep/main_k17_s08.py` |  |
| 0.74 | 17/23 | 9 | 5.9932s | 0.1513s | 1 | 8 | yes | 5.8984s | 6.0923s | `detyped_files/richards/advanced/proportion_sweep/main_k17_s09.py` |  |
| 0.74 | 17/23 | 10 | 6.0153s | 0.1493s | 1 | 8 | yes | 5.9271s | 6.1189s | `detyped_files/richards/advanced/proportion_sweep/main_k17_s10.py` |  |
| 0.74 | 17/23 | 11 | 2.8319s | 0.0754s | 1 | 8 | yes | 2.7816s | 2.8790s | `detyped_files/richards/advanced/proportion_sweep/main_k17_s11.py` |  |
| 0.74 | 17/23 | 12 | 3.3795s | 0.0966s | 1 | 8 | yes | 3.3211s | 3.4450s | `detyped_files/richards/advanced/proportion_sweep/main_k17_s12.py` |  |
| 0.74 | 17/23 | 13 | 5.6568s | 0.0929s | 1 | 8 | yes | 5.5928s | 5.7126s | `detyped_files/richards/advanced/proportion_sweep/main_k17_s13.py` |  |
| 0.74 | 17/23 | 14 | 5.6029s | 0.1158s | 1 | 8 | yes | 5.5266s | 5.6770s | `detyped_files/richards/advanced/proportion_sweep/main_k17_s14.py` |  |
| 0.74 | 17/23 | 15 | 6.0231s | 0.1449s | 1 | 8 | yes | 5.9450s | 6.1294s | `detyped_files/richards/advanced/proportion_sweep/main_k17_s15.py` |  |
| 0.74 | 17/23 | 16 | 6.1115s | 0.0926s | 1 | 8 | yes | 6.0543s | 6.1725s | `detyped_files/richards/advanced/proportion_sweep/main_k17_s16.py` |  |
| 0.74 | 17/23 | 17 | 5.5536s | 0.1672s | 1 | 8 | yes | 5.4601s | 5.6733s | `detyped_files/richards/advanced/proportion_sweep/main_k17_s17.py` |  |
| 0.74 | 17/23 | 18 | 5.3129s | 0.1314s | 1 | 8 | yes | 5.2308s | 5.4002s | `detyped_files/richards/advanced/proportion_sweep/main_k17_s18.py` |  |
| 0.74 | 17/23 | 19 | 3.2034s | 0.1355s | 1 | 8 | yes | 3.1179s | 3.2917s | `detyped_files/richards/advanced/proportion_sweep/main_k17_s19.py` |  |
| 0.74 | 17/23 | 20 | 5.4034s | 0.0727s | 1 | 8 | yes | 5.3530s | 5.4474s | `detyped_files/richards/advanced/proportion_sweep/main_k17_s20.py` |  |
| 0.78 | 18/23 | 1 | 3.5378s | 0.1256s | 1 | 8 | yes | 3.4571s | 3.6182s | `detyped_files/richards/advanced/proportion_sweep/main_k18_s01.py` |  |
| 0.78 | 18/23 | 2 | 5.1342s | 0.1678s | 1 | 8 | yes | 5.0541s | 5.2570s | `detyped_files/richards/advanced/proportion_sweep/main_k18_s02.py` |  |
| 0.78 | 18/23 | 3 | 3.4785s | 0.2619s | 1 | 8 | yes | 3.3436s | 3.6697s | `detyped_files/richards/advanced/proportion_sweep/main_k18_s03.py` |  |
| 0.78 | 18/23 | 4 | 3.4768s | 0.0983s | 1 | 8 | yes | 3.4110s | 3.5388s | `detyped_files/richards/advanced/proportion_sweep/main_k18_s04.py` |  |
| 0.78 | 18/23 | 5 | 3.8540s | 0.3941s | 1 | 8 | yes | 3.6692s | 4.1386s | `detyped_files/richards/advanced/proportion_sweep/main_k18_s05.py` |  |
| 0.78 | 18/23 | 6 | 5.5957s | 0.1060s | 1 | 8 | yes | 5.5357s | 5.6728s | `detyped_files/richards/advanced/proportion_sweep/main_k18_s06.py` |  |
| 0.78 | 18/23 | 7 | 3.4551s | 0.0470s | 1 | 8 | yes | 3.4274s | 3.4870s | `detyped_files/richards/advanced/proportion_sweep/main_k18_s07.py` |  |
| 0.78 | 18/23 | 8 | 5.4609s | 0.1963s | 1 | 8 | yes | 5.3457s | 5.6007s | `detyped_files/richards/advanced/proportion_sweep/main_k18_s08.py` |  |
| 0.78 | 18/23 | 9 | 5.4388s | 0.1597s | 1 | 8 | yes | 5.3454s | 5.5496s | `detyped_files/richards/advanced/proportion_sweep/main_k18_s09.py` |  |
| 0.78 | 18/23 | 10 | 4.9986s | 0.1487s | 1 | 8 | yes | 4.9036s | 5.0978s | `detyped_files/richards/advanced/proportion_sweep/main_k18_s10.py` |  |
| 0.78 | 18/23 | 11 | 4.4093s | 0.1443s | 1 | 8 | yes | 4.3183s | 4.5048s | `detyped_files/richards/advanced/proportion_sweep/main_k18_s11.py` |  |
| 0.78 | 18/23 | 12 | 5.4757s | 0.1717s | 1 | 8 | yes | 5.3721s | 5.5929s | `detyped_files/richards/advanced/proportion_sweep/main_k18_s12.py` |  |
| 0.78 | 18/23 | 13 | 3.7898s | 0.1238s | 1 | 8 | yes | 3.7096s | 3.8696s | `detyped_files/richards/advanced/proportion_sweep/main_k18_s13.py` |  |
| 0.78 | 18/23 | 14 | 5.4271s | 0.0803s | 1 | 8 | yes | 5.3733s | 5.4767s | `detyped_files/richards/advanced/proportion_sweep/main_k18_s14.py` |  |
| 0.78 | 18/23 | 15 | 3.1953s | 0.1383s | 1 | 8 | yes | 3.1122s | 3.2875s | `detyped_files/richards/advanced/proportion_sweep/main_k18_s15.py` |  |
| 0.78 | 18/23 | 16 | 6.1784s | 0.0884s | 1 | 8 | yes | 6.1223s | 6.2351s | `detyped_files/richards/advanced/proportion_sweep/main_k18_s16.py` |  |
| 0.78 | 18/23 | 17 | 6.2124s | 0.1041s | 1 | 8 | yes | 6.1462s | 6.2820s | `detyped_files/richards/advanced/proportion_sweep/main_k18_s17.py` |  |
| 0.78 | 18/23 | 18 | 5.6895s | 0.2000s | 1 | 8 | yes | 5.5733s | 5.8304s | `detyped_files/richards/advanced/proportion_sweep/main_k18_s18.py` |  |
| 0.78 | 18/23 | 19 | 3.5378s | 0.0831s | 1 | 8 | yes | 3.4881s | 3.5946s | `detyped_files/richards/advanced/proportion_sweep/main_k18_s19.py` |  |
| 0.78 | 18/23 | 20 | 2.9585s | 0.0335s | 1 | 8 | yes | 2.9373s | 2.9802s | `detyped_files/richards/advanced/proportion_sweep/main_k18_s20.py` |  |
| 0.83 | 19/23 | 1 | 5.8410s | 0.1983s | 1 | 8 | yes | 5.7151s | 5.9727s | `detyped_files/richards/advanced/proportion_sweep/main_k19_s01.py` |  |
| 0.83 | 19/23 | 2 | 6.1559s | 0.0631s | 1 | 8 | yes | 6.1180s | 6.1981s | `detyped_files/richards/advanced/proportion_sweep/main_k19_s02.py` |  |
| 0.83 | 19/23 | 3 | 5.3952s | 0.1114s | 1 | 8 | yes | 5.3209s | 5.4654s | `detyped_files/richards/advanced/proportion_sweep/main_k19_s03.py` |  |
| 0.83 | 19/23 | 4 | 5.6759s | 0.1736s | 1 | 8 | yes | 5.5785s | 5.8022s | `detyped_files/richards/advanced/proportion_sweep/main_k19_s04.py` |  |
| 0.83 | 19/23 | 5 | 5.3665s | 0.2338s | 1 | 8 | yes | 5.2387s | 5.5333s | `detyped_files/richards/advanced/proportion_sweep/main_k19_s05.py` |  |
| 0.83 | 19/23 | 6 | 5.6166s | 0.1543s | 1 | 8 | yes | 5.5206s | 5.7223s | `detyped_files/richards/advanced/proportion_sweep/main_k19_s06.py` |  |
| 0.83 | 19/23 | 7 | 3.5104s | 0.0923s | 1 | 8 | yes | 3.4507s | 3.5703s | `detyped_files/richards/advanced/proportion_sweep/main_k19_s07.py` |  |
| 0.83 | 19/23 | 8 | 5.7825s | 0.1118s | 1 | 8 | yes | 5.7035s | 5.8479s | `detyped_files/richards/advanced/proportion_sweep/main_k19_s08.py` |  |
| 0.83 | 19/23 | 9 | 5.1305s | 0.1214s | 1 | 8 | yes | 5.0518s | 5.2108s | `detyped_files/richards/advanced/proportion_sweep/main_k19_s09.py` |  |
| 0.83 | 19/23 | 10 | 5.0877s | 0.1236s | 1 | 8 | yes | 5.0070s | 5.1668s | `detyped_files/richards/advanced/proportion_sweep/main_k19_s10.py` |  |
| 0.83 | 19/23 | 11 | 5.2797s | 0.0595s | 1 | 8 | yes | 5.2456s | 5.3217s | `detyped_files/richards/advanced/proportion_sweep/main_k19_s11.py` |  |
| 0.83 | 19/23 | 12 | 5.8617s | 0.1366s | 1 | 8 | yes | 5.7780s | 5.9537s | `detyped_files/richards/advanced/proportion_sweep/main_k19_s12.py` |  |
| 0.83 | 19/23 | 13 | 5.0143s | 0.0597s | 1 | 8 | yes | 4.9745s | 5.0518s | `detyped_files/richards/advanced/proportion_sweep/main_k19_s13.py` |  |
| 0.83 | 19/23 | 14 | 5.4431s | 0.1358s | 1 | 8 | yes | 5.3531s | 5.5301s | `detyped_files/richards/advanced/proportion_sweep/main_k19_s14.py` |  |
| 0.83 | 19/23 | 15 | 5.7367s | 0.1307s | 1 | 8 | yes | 5.6492s | 5.8192s | `detyped_files/richards/advanced/proportion_sweep/main_k19_s15.py` |  |
| 0.83 | 19/23 | 16 | 5.4061s | 0.1073s | 1 | 8 | yes | 5.3351s | 5.4740s | `detyped_files/richards/advanced/proportion_sweep/main_k19_s16.py` |  |
| 0.83 | 19/23 | 17 | 6.1138s | 0.1196s | 1 | 8 | yes | 6.0376s | 6.1906s | `detyped_files/richards/advanced/proportion_sweep/main_k19_s17.py` |  |
| 0.83 | 19/23 | 18 | 6.0609s | 0.1395s | 1 | 8 | yes | 5.9693s | 6.1480s | `detyped_files/richards/advanced/proportion_sweep/main_k19_s18.py` |  |
| 0.83 | 19/23 | 19 | 5.4162s | 0.1000s | 1 | 8 | yes | 5.3523s | 5.4811s | `detyped_files/richards/advanced/proportion_sweep/main_k19_s19.py` |  |
| 0.83 | 19/23 | 20 | 5.3949s | 0.1102s | 1 | 8 | yes | 5.3282s | 5.4692s | `detyped_files/richards/advanced/proportion_sweep/main_k19_s20.py` |  |
| 0.87 | 20/23 | 1 | 6.3406s | 0.3415s | 1 | 8 | yes | 6.1669s | 6.5870s | `detyped_files/richards/advanced/proportion_sweep/main_k20_s01.py` |  |
| 0.87 | 20/23 | 2 | 3.8260s | 0.1443s | 1 | 8 | yes | 3.7333s | 3.9197s | `detyped_files/richards/advanced/proportion_sweep/main_k20_s02.py` |  |
| 0.87 | 20/23 | 3 | 6.2225s | 0.0678s | 1 | 8 | yes | 6.1801s | 6.2683s | `detyped_files/richards/advanced/proportion_sweep/main_k20_s03.py` |  |
| 0.87 | 20/23 | 4 | 6.1768s | 0.0951s | 1 | 8 | yes | 6.1117s | 6.2331s | `detyped_files/richards/advanced/proportion_sweep/main_k20_s04.py` |  |
| 0.87 | 20/23 | 5 | 6.0098s | 0.1016s | 1 | 8 | yes | 5.9432s | 6.0771s | `detyped_files/richards/advanced/proportion_sweep/main_k20_s05.py` |  |
| 0.87 | 20/23 | 6 | 5.4131s | 0.1072s | 1 | 8 | yes | 5.3469s | 5.4851s | `detyped_files/richards/advanced/proportion_sweep/main_k20_s06.py` |  |
| 0.87 | 20/23 | 7 | 5.7708s | 0.1453s | 1 | 8 | yes | 5.6716s | 5.8585s | `detyped_files/richards/advanced/proportion_sweep/main_k20_s07.py` |  |
| 0.87 | 20/23 | 8 | 5.7299s | 0.1791s | 1 | 8 | yes | 5.6259s | 5.8562s | `detyped_files/richards/advanced/proportion_sweep/main_k20_s08.py` |  |
| 0.87 | 20/23 | 9 | 3.4134s | 0.0579s | 1 | 8 | yes | 3.3747s | 3.4490s | `detyped_files/richards/advanced/proportion_sweep/main_k20_s09.py` |  |
| 0.87 | 20/23 | 10 | 6.1331s | 0.1104s | 1 | 8 | yes | 6.0626s | 6.2067s | `detyped_files/richards/advanced/proportion_sweep/main_k20_s10.py` |  |
| 0.87 | 20/23 | 11 | 4.9439s | 0.0660s | 1 | 8 | yes | 4.8996s | 4.9834s | `detyped_files/richards/advanced/proportion_sweep/main_k20_s11.py` |  |
| 0.87 | 20/23 | 12 | 5.8865s | 0.1210s | 1 | 8 | yes | 5.8091s | 5.9633s | `detyped_files/richards/advanced/proportion_sweep/main_k20_s12.py` |  |
| 0.87 | 20/23 | 13 | 3.4904s | 0.1455s | 1 | 8 | yes | 3.3943s | 3.5852s | `detyped_files/richards/advanced/proportion_sweep/main_k20_s13.py` |  |
| 0.87 | 20/23 | 14 | 5.9154s | 0.0842s | 1 | 8 | yes | 5.8673s | 5.9743s | `detyped_files/richards/advanced/proportion_sweep/main_k20_s14.py` |  |
| 0.87 | 20/23 | 15 | 6.2135s | 0.1637s | 1 | 8 | yes | 6.1056s | 6.3197s | `detyped_files/richards/advanced/proportion_sweep/main_k20_s15.py` |  |
| 0.87 | 20/23 | 16 | 6.0654s | 0.2331s | 1 | 8 | yes | 5.9327s | 6.2287s | `detyped_files/richards/advanced/proportion_sweep/main_k20_s16.py` |  |
| 0.87 | 20/23 | 17 | 6.1926s | 0.1300s | 1 | 8 | yes | 6.1125s | 6.2814s | `detyped_files/richards/advanced/proportion_sweep/main_k20_s17.py` |  |
| 0.87 | 20/23 | 18 | 5.3659s | 0.0797s | 1 | 8 | yes | 5.3131s | 5.4153s | `detyped_files/richards/advanced/proportion_sweep/main_k20_s18.py` |  |
| 0.87 | 20/23 | 19 | 3.4823s | 0.1697s | 1 | 8 | yes | 3.3836s | 3.6023s | `detyped_files/richards/advanced/proportion_sweep/main_k20_s19.py` |  |
| 0.87 | 20/23 | 20 | 6.1335s | 0.1074s | 1 | 8 | yes | 6.0665s | 6.2044s | `detyped_files/richards/advanced/proportion_sweep/main_k20_s20.py` |  |
| 0.91 | 21/23 | 1 | 6.2270s | 0.0984s | 1 | 8 | yes | 6.1632s | 6.2916s | `detyped_files/richards/advanced/proportion_sweep/main_k21_s01.py` |  |
| 0.91 | 21/23 | 2 | 5.8194s | 0.1087s | 1 | 8 | yes | 5.7517s | 5.8907s | `detyped_files/richards/advanced/proportion_sweep/main_k21_s02.py` |  |
| 0.91 | 21/23 | 3 | 6.2055s | 0.2355s | 1 | 8 | yes | 6.0835s | 6.3759s | `detyped_files/richards/advanced/proportion_sweep/main_k21_s03.py` |  |
| 0.91 | 21/23 | 4 | 3.7020s | 0.1415s | 1 | 8 | yes | 3.6130s | 3.7932s | `detyped_files/richards/advanced/proportion_sweep/main_k21_s04.py` |  |
| 0.91 | 21/23 | 5 | 5.8813s | 0.1285s | 1 | 8 | yes | 5.7929s | 5.9599s | `detyped_files/richards/advanced/proportion_sweep/main_k21_s05.py` |  |
| 0.91 | 21/23 | 6 | 6.1960s | 0.0828s | 1 | 8 | yes | 6.1459s | 6.2479s | `detyped_files/richards/advanced/proportion_sweep/main_k21_s06.py` |  |
| 0.91 | 21/23 | 7 | 5.7094s | 0.1357s | 1 | 8 | yes | 5.6240s | 5.8002s | `detyped_files/richards/advanced/proportion_sweep/main_k21_s07.py` |  |
| 0.91 | 21/23 | 8 | 6.2047s | 0.1394s | 1 | 8 | yes | 6.1218s | 6.3004s | `detyped_files/richards/advanced/proportion_sweep/main_k21_s08.py` |  |
| 0.91 | 21/23 | 9 | 5.8706s | 0.1888s | 1 | 8 | yes | 5.7539s | 5.9950s | `detyped_files/richards/advanced/proportion_sweep/main_k21_s09.py` |  |
| 0.91 | 21/23 | 10 | 6.1336s | 0.0924s | 1 | 8 | yes | 6.0758s | 6.1945s | `detyped_files/richards/advanced/proportion_sweep/main_k21_s10.py` |  |
| 0.91 | 21/23 | 11 | 6.2109s | 0.1139s | 1 | 8 | yes | 6.1393s | 6.2874s | `detyped_files/richards/advanced/proportion_sweep/main_k21_s11.py` |  |
| 0.91 | 21/23 | 12 | 6.1157s | 0.1179s | 1 | 8 | yes | 6.0436s | 6.1947s | `detyped_files/richards/advanced/proportion_sweep/main_k21_s12.py` |  |
| 0.91 | 21/23 | 13 | 6.1592s | 0.2315s | 1 | 8 | yes | 6.0226s | 6.3224s | `detyped_files/richards/advanced/proportion_sweep/main_k21_s13.py` |  |
| 0.91 | 21/23 | 14 | 6.2103s | 0.0693s | 1 | 8 | yes | 6.1606s | 6.2460s | `detyped_files/richards/advanced/proportion_sweep/main_k21_s14.py` |  |
| 0.91 | 21/23 | 15 | 5.9920s | 0.2054s | 1 | 8 | yes | 5.8599s | 6.1245s | `detyped_files/richards/advanced/proportion_sweep/main_k21_s15.py` |  |
| 0.91 | 21/23 | 16 | 6.1863s | 0.1120s | 1 | 8 | yes | 6.1274s | 6.2679s | `detyped_files/richards/advanced/proportion_sweep/main_k21_s16.py` |  |
| 0.91 | 21/23 | 17 | 6.0058s | 0.1660s | 1 | 8 | yes | 5.9000s | 6.1137s | `detyped_files/richards/advanced/proportion_sweep/main_k21_s17.py` |  |
| 0.91 | 21/23 | 18 | 6.2175s | 0.1172s | 1 | 8 | yes | 6.1394s | 6.2927s | `detyped_files/richards/advanced/proportion_sweep/main_k21_s18.py` |  |
| 0.91 | 21/23 | 19 | 6.1455s | 0.1159s | 1 | 8 | yes | 6.0683s | 6.2193s | `detyped_files/richards/advanced/proportion_sweep/main_k21_s19.py` |  |
| 0.91 | 21/23 | 20 | 6.3070s | 0.2117s | 1 | 8 | yes | 6.1956s | 6.4641s | `detyped_files/richards/advanced/proportion_sweep/main_k21_s20.py` |  |
| 0.96 | 22/23 | 1 | 6.1418s | 0.0570s | 1 | 8 | yes | 6.1020s | 6.1756s | `detyped_files/richards/advanced/proportion_sweep/main_k22_s01.py` |  |
| 0.96 | 22/23 | 2 | 6.1472s | 0.2160s | 1 | 8 | yes | 6.0277s | 6.3061s | `detyped_files/richards/advanced/proportion_sweep/main_k22_s02.py` |  |
| 0.96 | 22/23 | 3 | 6.1187s | 0.1089s | 1 | 8 | yes | 6.0515s | 6.1914s | `detyped_files/richards/advanced/proportion_sweep/main_k22_s03.py` |  |
| 0.96 | 22/23 | 4 | 6.1742s | 0.1301s | 1 | 8 | yes | 6.0886s | 6.2578s | `detyped_files/richards/advanced/proportion_sweep/main_k22_s04.py` |  |
| 0.96 | 22/23 | 5 | 6.2009s | 0.1580s | 1 | 8 | yes | 6.1013s | 6.3062s | `detyped_files/richards/advanced/proportion_sweep/main_k22_s05.py` |  |
| 0.96 | 22/23 | 6 | 5.8709s | 0.1104s | 1 | 8 | yes | 5.7967s | 5.9373s | `detyped_files/richards/advanced/proportion_sweep/main_k22_s06.py` |  |
| 0.96 | 22/23 | 7 | 6.1608s | 0.0863s | 1 | 8 | yes | 6.1081s | 6.2200s | `detyped_files/richards/advanced/proportion_sweep/main_k22_s07.py` |  |
| 0.96 | 22/23 | 8 | 6.1837s | 0.0908s | 1 | 8 | yes | 6.1247s | 6.2397s | `detyped_files/richards/advanced/proportion_sweep/main_k22_s08.py` |  |
| 0.96 | 22/23 | 9 | 6.1546s | 0.0720s | 1 | 8 | yes | 6.1051s | 6.1970s | `detyped_files/richards/advanced/proportion_sweep/main_k22_s09.py` |  |
| 0.96 | 22/23 | 10 | 6.2860s | 0.2296s | 1 | 8 | yes | 6.1434s | 6.4434s | `detyped_files/richards/advanced/proportion_sweep/main_k22_s10.py` |  |
| 0.96 | 22/23 | 11 | 6.2556s | 0.1191s | 1 | 8 | yes | 6.1823s | 6.3330s | `detyped_files/richards/advanced/proportion_sweep/main_k22_s11.py` |  |
| 0.96 | 22/23 | 12 | 6.3551s | 0.1862s | 1 | 8 | yes | 6.2641s | 6.4947s | `detyped_files/richards/advanced/proportion_sweep/main_k22_s12.py` |  |
| 0.96 | 22/23 | 13 | 6.2782s | 0.1081s | 1 | 8 | yes | 6.2019s | 6.3406s | `detyped_files/richards/advanced/proportion_sweep/main_k22_s13.py` |  |
| 0.96 | 22/23 | 14 | 6.2225s | 0.1986s | 1 | 8 | yes | 6.1055s | 6.3594s | `detyped_files/richards/advanced/proportion_sweep/main_k22_s14.py` |  |
| 0.96 | 22/23 | 15 | 6.1685s | 0.1160s | 1 | 8 | yes | 6.0882s | 6.2411s | `detyped_files/richards/advanced/proportion_sweep/main_k22_s15.py` |  |
| 0.96 | 22/23 | 16 | 6.2439s | 0.1536s | 1 | 8 | yes | 6.1389s | 6.3381s | `detyped_files/richards/advanced/proportion_sweep/main_k22_s16.py` |  |
| 0.96 | 22/23 | 17 | 5.9928s | 0.0778s | 1 | 8 | yes | 5.9444s | 6.0436s | `detyped_files/richards/advanced/proportion_sweep/main_k22_s17.py` |  |
| 0.96 | 22/23 | 18 | 6.2594s | 0.1445s | 1 | 8 | yes | 6.1714s | 6.3539s | `detyped_files/richards/advanced/proportion_sweep/main_k22_s18.py` |  |
| 0.96 | 22/23 | 19 | 5.5041s | 0.2067s | 1 | 8 | yes | 5.3853s | 5.6481s | `detyped_files/richards/advanced/proportion_sweep/main_k22_s19.py` |  |
| 0.96 | 22/23 | 20 | 6.2294s | 0.0858s | 1 | 8 | yes | 6.1789s | 6.2907s | `detyped_files/richards/advanced/proportion_sweep/main_k22_s20.py` |  |
| 1.00 | 23/23 | 1 | 6.2335s | 0.2005s | 1 | 8 | yes | 6.1127s | 6.3659s | `detyped_files/richards/advanced/proportion_sweep/main_k23_s01.py` |  |

## richards/shallow

- Detypable targets: `23`
- Total runs: `442`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/23 | 1 | 1.0184s | 1.0184s | 1.0184s | 1.0 | yes | ok |
| 0.04 | 1/23 | 20 | 1.1975s | 0.9795s | 2.9121s | 1.0 | yes | ok |
| 0.09 | 2/23 | 20 | 1.4420s | 0.9843s | 3.2448s | 1.0 | yes | ok |
| 0.13 | 3/23 | 20 | 1.5193s | 1.0323s | 3.0764s | 1.0 | yes | ok |
| 0.17 | 4/23 | 20 | 1.7678s | 0.9818s | 3.3357s | 1.0 | yes | ok |
| 0.22 | 5/23 | 20 | 2.0764s | 1.0828s | 3.6670s | 1.0 | yes | ok |
| 0.26 | 6/23 | 20 | 1.9137s | 1.0422s | 3.5226s | 1.0 | yes | ok |
| 0.30 | 7/23 | 20 | 1.9339s | 1.2079s | 3.7979s | 1.0 | yes | ok |
| 0.35 | 8/23 | 20 | 2.1786s | 1.4252s | 3.6891s | 1.0 | yes | ok |
| 0.39 | 9/23 | 20 | 2.2727s | 1.4702s | 3.8860s | 1.0 | yes | ok |
| 0.43 | 10/23 | 20 | 2.9469s | 1.4190s | 4.0891s | 1.0 | yes | ok |
| 0.48 | 11/23 | 20 | 2.6503s | 1.2156s | 3.9211s | 1.0 | yes | ok |
| 0.52 | 12/23 | 20 | 2.9618s | 1.4696s | 4.3374s | 1.0 | yes | ok |
| 0.57 | 13/23 | 20 | 2.9380s | 1.4280s | 4.1882s | 1.0 | yes | ok |
| 0.61 | 14/23 | 20 | 3.2220s | 1.3803s | 4.3652s | 1.0 | yes | ok |
| 0.65 | 15/23 | 20 | 3.1960s | 1.8736s | 4.4449s | 1.0 | yes | ok |
| 0.70 | 16/23 | 20 | 3.7832s | 2.3030s | 4.5439s | 1.0 | yes | ok |
| 0.74 | 17/23 | 20 | 3.5403s | 2.0170s | 4.5588s | 1.0 | yes | ok |
| 0.78 | 18/23 | 20 | 3.9937s | 2.4554s | 4.5071s | 1.0 | yes | ok |
| 0.83 | 19/23 | 20 | 4.0622s | 2.7646s | 4.5803s | 1.0 | yes | ok |
| 0.87 | 20/23 | 20 | 4.2184s | 2.7112s | 4.6828s | 1.0 | yes | ok |
| 0.91 | 21/23 | 20 | 4.3456s | 2.6771s | 4.7211s | 1.0 | yes | ok |
| 0.96 | 22/23 | 20 | 4.5232s | 4.1926s | 4.6723s | 1.0 | yes | ok |
| 1.00 | 23/23 | 1 | 4.5864s | 4.5864s | 4.5864s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/23 | 1 | 1.0184s | 0.1135s | 1 | 8 | yes | 0.9486s | 1.0913s | `detyped_files/richards/shallow/proportion_sweep/main_k00_s01.py` |  |
| 0.04 | 1/23 | 1 | 1.4571s | 0.0849s | 1 | 8 | yes | 1.4018s | 1.5103s | `detyped_files/richards/shallow/proportion_sweep/main_k01_s01.py` |  |
| 0.04 | 1/23 | 2 | 1.0071s | 0.0964s | 1 | 8 | yes | 0.9487s | 1.0739s | `detyped_files/richards/shallow/proportion_sweep/main_k01_s02.py` |  |
| 0.04 | 1/23 | 3 | 1.2289s | 0.1007s | 1 | 8 | yes | 1.1658s | 1.2956s | `detyped_files/richards/shallow/proportion_sweep/main_k01_s03.py` |  |
| 0.04 | 1/23 | 4 | 1.0630s | 0.0441s | 1 | 8 | yes | 1.0345s | 1.0914s | `detyped_files/richards/shallow/proportion_sweep/main_k01_s04.py` |  |
| 0.04 | 1/23 | 5 | 1.0454s | 0.0521s | 1 | 8 | yes | 1.0076s | 1.0753s | `detyped_files/richards/shallow/proportion_sweep/main_k01_s05.py` |  |
| 0.04 | 1/23 | 6 | 1.0232s | 0.0512s | 1 | 8 | yes | 0.9884s | 1.0536s | `detyped_files/richards/shallow/proportion_sweep/main_k01_s06.py` |  |
| 0.04 | 1/23 | 7 | 1.0109s | 0.0401s | 1 | 8 | yes | 0.9838s | 1.0355s | `detyped_files/richards/shallow/proportion_sweep/main_k01_s07.py` |  |
| 0.04 | 1/23 | 8 | 1.0014s | 0.0700s | 1 | 8 | yes | 0.9554s | 1.0464s | `detyped_files/richards/shallow/proportion_sweep/main_k01_s08.py` |  |
| 0.04 | 1/23 | 9 | 1.0158s | 0.0506s | 1 | 8 | yes | 0.9856s | 1.0503s | `detyped_files/richards/shallow/proportion_sweep/main_k01_s09.py` |  |
| 0.04 | 1/23 | 10 | 1.3539s | 0.0202s | 1 | 8 | yes | 1.3402s | 1.3661s | `detyped_files/richards/shallow/proportion_sweep/main_k01_s10.py` |  |
| 0.04 | 1/23 | 11 | 1.0421s | 0.0714s | 1 | 8 | yes | 0.9938s | 1.0853s | `detyped_files/richards/shallow/proportion_sweep/main_k01_s11.py` |  |
| 0.04 | 1/23 | 12 | 0.9795s | 0.0924s | 1 | 8 | yes | 0.9191s | 1.0394s | `detyped_files/richards/shallow/proportion_sweep/main_k01_s12.py` |  |
| 0.04 | 1/23 | 13 | 1.1216s | 0.1275s | 1 | 8 | yes | 1.0468s | 1.2118s | `detyped_files/richards/shallow/proportion_sweep/main_k01_s13.py` |  |
| 0.04 | 1/23 | 14 | 1.4010s | 0.1413s | 1 | 8 | yes | 1.3320s | 1.5044s | `detyped_files/richards/shallow/proportion_sweep/main_k01_s14.py` |  |
| 0.04 | 1/23 | 15 | 1.0378s | 0.0494s | 1 | 8 | yes | 1.0061s | 1.0695s | `detyped_files/richards/shallow/proportion_sweep/main_k01_s15.py` |  |
| 0.04 | 1/23 | 16 | 1.0977s | 0.0698s | 1 | 8 | yes | 1.0547s | 1.1455s | `detyped_files/richards/shallow/proportion_sweep/main_k01_s16.py` |  |
| 0.04 | 1/23 | 17 | 0.9997s | 0.0413s | 1 | 8 | yes | 0.9727s | 1.0258s | `detyped_files/richards/shallow/proportion_sweep/main_k01_s17.py` |  |
| 0.04 | 1/23 | 18 | 1.0572s | 0.0536s | 1 | 8 | yes | 1.0270s | 1.0952s | `detyped_files/richards/shallow/proportion_sweep/main_k01_s18.py` |  |
| 0.04 | 1/23 | 19 | 1.0950s | 0.1104s | 1 | 8 | yes | 1.0199s | 1.1615s | `detyped_files/richards/shallow/proportion_sweep/main_k01_s19.py` |  |
| 0.04 | 1/23 | 20 | 2.9121s | 0.0896s | 1 | 8 | yes | 2.8588s | 2.9746s | `detyped_files/richards/shallow/proportion_sweep/main_k01_s20.py` |  |
| 0.09 | 2/23 | 1 | 1.0550s | 0.0858s | 1 | 8 | yes | 1.0006s | 1.1121s | `detyped_files/richards/shallow/proportion_sweep/main_k02_s01.py` |  |
| 0.09 | 2/23 | 2 | 1.0467s | 0.0759s | 1 | 8 | yes | 1.0004s | 1.0989s | `detyped_files/richards/shallow/proportion_sweep/main_k02_s02.py` |  |
| 0.09 | 2/23 | 3 | 1.2054s | 0.0376s | 1 | 8 | yes | 1.1786s | 1.2274s | `detyped_files/richards/shallow/proportion_sweep/main_k02_s03.py` |  |
| 0.09 | 2/23 | 4 | 1.5381s | 0.0440s | 1 | 8 | yes | 1.5105s | 1.5670s | `detyped_files/richards/shallow/proportion_sweep/main_k02_s04.py` |  |
| 0.09 | 2/23 | 5 | 1.0804s | 0.1219s | 1 | 8 | yes | 1.0097s | 1.1657s | `detyped_files/richards/shallow/proportion_sweep/main_k02_s05.py` |  |
| 0.09 | 2/23 | 6 | 1.0499s | 0.0701s | 1 | 8 | yes | 1.0009s | 1.0916s | `detyped_files/richards/shallow/proportion_sweep/main_k02_s06.py` |  |
| 0.09 | 2/23 | 7 | 1.4044s | 0.0948s | 1 | 8 | yes | 1.3480s | 1.4707s | `detyped_files/richards/shallow/proportion_sweep/main_k02_s07.py` |  |
| 0.09 | 2/23 | 8 | 1.0051s | 0.0623s | 1 | 8 | yes | 0.9604s | 1.0408s | `detyped_files/richards/shallow/proportion_sweep/main_k02_s08.py` |  |
| 0.09 | 2/23 | 9 | 2.8903s | 0.0423s | 1 | 8 | yes | 2.8638s | 2.9174s | `detyped_files/richards/shallow/proportion_sweep/main_k02_s09.py` |  |
| 0.09 | 2/23 | 10 | 1.0815s | 0.0297s | 1 | 8 | yes | 1.0623s | 1.1001s | `detyped_files/richards/shallow/proportion_sweep/main_k02_s10.py` |  |
| 0.09 | 2/23 | 11 | 1.0439s | 0.0612s | 1 | 8 | yes | 1.0024s | 1.0819s | `detyped_files/richards/shallow/proportion_sweep/main_k02_s11.py` |  |
| 0.09 | 2/23 | 12 | 1.4222s | 0.0878s | 1 | 8 | yes | 1.3665s | 1.4774s | `detyped_files/richards/shallow/proportion_sweep/main_k02_s12.py` |  |
| 0.09 | 2/23 | 13 | 0.9843s | 0.0697s | 1 | 8 | yes | 0.9434s | 1.0340s | `detyped_files/richards/shallow/proportion_sweep/main_k02_s13.py` |  |
| 0.09 | 2/23 | 14 | 1.1414s | 0.0866s | 1 | 8 | yes | 1.0850s | 1.1939s | `detyped_files/richards/shallow/proportion_sweep/main_k02_s14.py` |  |
| 0.09 | 2/23 | 15 | 1.0963s | 0.0761s | 1 | 8 | yes | 1.0442s | 1.1420s | `detyped_files/richards/shallow/proportion_sweep/main_k02_s15.py` |  |
| 0.09 | 2/23 | 16 | 1.0919s | 0.0820s | 1 | 8 | yes | 1.0373s | 1.1419s | `detyped_files/richards/shallow/proportion_sweep/main_k02_s16.py` |  |
| 0.09 | 2/23 | 17 | 2.9443s | 0.0641s | 1 | 8 | yes | 2.9061s | 2.9886s | `detyped_files/richards/shallow/proportion_sweep/main_k02_s17.py` |  |
| 0.09 | 2/23 | 18 | 1.4533s | 0.0700s | 1 | 8 | yes | 1.4056s | 1.4973s | `detyped_files/richards/shallow/proportion_sweep/main_k02_s18.py` |  |
| 0.09 | 2/23 | 19 | 1.0617s | 0.1355s | 1 | 8 | yes | 0.9776s | 1.1549s | `detyped_files/richards/shallow/proportion_sweep/main_k02_s19.py` |  |
| 0.09 | 2/23 | 20 | 3.2448s | 0.1183s | 1 | 8 | yes | 3.1608s | 3.3112s | `detyped_files/richards/shallow/proportion_sweep/main_k02_s20.py` |  |
| 0.13 | 3/23 | 1 | 1.2577s | 0.0979s | 1 | 8 | yes | 1.1987s | 1.3252s | `detyped_files/richards/shallow/proportion_sweep/main_k03_s01.py` |  |
| 0.13 | 3/23 | 2 | 1.3660s | 0.0862s | 1 | 8 | yes | 1.3107s | 1.4218s | `detyped_files/richards/shallow/proportion_sweep/main_k03_s02.py` |  |
| 0.13 | 3/23 | 3 | 1.2326s | 0.1454s | 1 | 8 | yes | 1.1528s | 1.3382s | `detyped_files/richards/shallow/proportion_sweep/main_k03_s03.py` |  |
| 0.13 | 3/23 | 4 | 1.0323s | 0.0961s | 1 | 8 | yes | 0.9686s | 1.0942s | `detyped_files/richards/shallow/proportion_sweep/main_k03_s04.py` |  |
| 0.13 | 3/23 | 5 | 1.4164s | 0.1234s | 1 | 8 | yes | 1.3383s | 1.5025s | `detyped_files/richards/shallow/proportion_sweep/main_k03_s05.py` |  |
| 0.13 | 3/23 | 6 | 1.2746s | 0.0646s | 1 | 8 | yes | 1.2345s | 1.3168s | `detyped_files/richards/shallow/proportion_sweep/main_k03_s06.py` |  |
| 0.13 | 3/23 | 7 | 1.4629s | 0.0499s | 1 | 8 | yes | 1.4319s | 1.4969s | `detyped_files/richards/shallow/proportion_sweep/main_k03_s07.py` |  |
| 0.13 | 3/23 | 8 | 1.3198s | 0.1070s | 1 | 8 | yes | 1.2542s | 1.3914s | `detyped_files/richards/shallow/proportion_sweep/main_k03_s08.py` |  |
| 0.13 | 3/23 | 9 | 1.3533s | 0.0759s | 1 | 8 | yes | 1.3027s | 1.4012s | `detyped_files/richards/shallow/proportion_sweep/main_k03_s09.py` |  |
| 0.13 | 3/23 | 10 | 1.2264s | 0.0872s | 1 | 8 | yes | 1.1687s | 1.2828s | `detyped_files/richards/shallow/proportion_sweep/main_k03_s10.py` |  |
| 0.13 | 3/23 | 11 | 1.1435s | 0.0881s | 1 | 8 | yes | 1.0868s | 1.2001s | `detyped_files/richards/shallow/proportion_sweep/main_k03_s11.py` |  |
| 0.13 | 3/23 | 12 | 1.1035s | 0.1039s | 1 | 8 | yes | 1.0311s | 1.1671s | `detyped_files/richards/shallow/proportion_sweep/main_k03_s12.py` |  |
| 0.13 | 3/23 | 13 | 2.9926s | 0.1567s | 1 | 8 | yes | 2.8952s | 3.0954s | `detyped_files/richards/shallow/proportion_sweep/main_k03_s13.py` |  |
| 0.13 | 3/23 | 14 | 1.1733s | 0.0890s | 1 | 8 | yes | 1.1213s | 1.2355s | `detyped_files/richards/shallow/proportion_sweep/main_k03_s14.py` |  |
| 0.13 | 3/23 | 15 | 2.9835s | 0.0584s | 1 | 8 | yes | 2.9437s | 3.0185s | `detyped_files/richards/shallow/proportion_sweep/main_k03_s15.py` |  |
| 0.13 | 3/23 | 16 | 3.0764s | 0.1765s | 1 | 8 | yes | 2.9725s | 3.2037s | `detyped_files/richards/shallow/proportion_sweep/main_k03_s16.py` |  |
| 0.13 | 3/23 | 17 | 1.0351s | 0.0518s | 1 | 8 | yes | 1.0107s | 1.0727s | `detyped_files/richards/shallow/proportion_sweep/main_k03_s17.py` |  |
| 0.13 | 3/23 | 18 | 1.1980s | 0.1631s | 1 | 8 | yes | 1.1104s | 1.3127s | `detyped_files/richards/shallow/proportion_sweep/main_k03_s18.py` |  |
| 0.13 | 3/23 | 19 | 1.6190s | 0.0981s | 1 | 8 | yes | 1.5563s | 1.6840s | `detyped_files/richards/shallow/proportion_sweep/main_k03_s19.py` |  |
| 0.13 | 3/23 | 20 | 1.1196s | 0.0544s | 1 | 8 | yes | 1.0870s | 1.1570s | `detyped_files/richards/shallow/proportion_sweep/main_k03_s20.py` |  |
| 0.17 | 4/23 | 1 | 1.3231s | 0.0945s | 1 | 8 | yes | 1.2602s | 1.3812s | `detyped_files/richards/shallow/proportion_sweep/main_k04_s01.py` |  |
| 0.17 | 4/23 | 2 | 1.5598s | 0.1461s | 1 | 8 | yes | 1.4739s | 1.6631s | `detyped_files/richards/shallow/proportion_sweep/main_k04_s02.py` |  |
| 0.17 | 4/23 | 3 | 1.6806s | 0.1500s | 1 | 8 | yes | 1.6068s | 1.7873s | `detyped_files/richards/shallow/proportion_sweep/main_k04_s03.py` |  |
| 0.17 | 4/23 | 4 | 2.0233s | 0.0638s | 1 | 8 | yes | 1.9857s | 2.0677s | `detyped_files/richards/shallow/proportion_sweep/main_k04_s04.py` |  |
| 0.17 | 4/23 | 5 | 0.9818s | 0.0608s | 1 | 8 | yes | 0.9411s | 1.0190s | `detyped_files/richards/shallow/proportion_sweep/main_k04_s05.py` |  |
| 0.17 | 4/23 | 6 | 1.0726s | 0.0555s | 1 | 8 | yes | 1.0361s | 1.1080s | `detyped_files/richards/shallow/proportion_sweep/main_k04_s06.py` |  |
| 0.17 | 4/23 | 7 | 2.1463s | 0.1216s | 1 | 8 | yes | 2.0749s | 2.2324s | `detyped_files/richards/shallow/proportion_sweep/main_k04_s07.py` |  |
| 0.17 | 4/23 | 8 | 3.3357s | 0.0591s | 1 | 8 | yes | 3.2968s | 3.3728s | `detyped_files/richards/shallow/proportion_sweep/main_k04_s08.py` |  |
| 0.17 | 4/23 | 9 | 1.3626s | 0.0917s | 1 | 8 | yes | 1.2995s | 1.4177s | `detyped_files/richards/shallow/proportion_sweep/main_k04_s09.py` |  |
| 0.17 | 4/23 | 10 | 1.2260s | 0.0913s | 1 | 8 | yes | 1.1685s | 1.2837s | `detyped_files/richards/shallow/proportion_sweep/main_k04_s10.py` |  |
| 0.17 | 4/23 | 11 | 1.0563s | 0.0879s | 1 | 8 | yes | 1.0004s | 1.1138s | `detyped_files/richards/shallow/proportion_sweep/main_k04_s11.py` |  |
| 0.17 | 4/23 | 12 | 1.1386s | 0.0663s | 1 | 8 | yes | 1.0932s | 1.1781s | `detyped_files/richards/shallow/proportion_sweep/main_k04_s12.py` |  |
| 0.17 | 4/23 | 13 | 3.3225s | 0.1118s | 1 | 8 | yes | 3.2465s | 3.3913s | `detyped_files/richards/shallow/proportion_sweep/main_k04_s13.py` |  |
| 0.17 | 4/23 | 14 | 1.0120s | 0.0825s | 1 | 8 | yes | 0.9580s | 1.0633s | `detyped_files/richards/shallow/proportion_sweep/main_k04_s14.py` |  |
| 0.17 | 4/23 | 15 | 1.4134s | 0.0744s | 1 | 8 | yes | 1.3685s | 1.4634s | `detyped_files/richards/shallow/proportion_sweep/main_k04_s15.py` |  |
| 0.17 | 4/23 | 16 | 1.5903s | 0.0589s | 1 | 8 | yes | 1.5512s | 1.6281s | `detyped_files/richards/shallow/proportion_sweep/main_k04_s16.py` |  |
| 0.17 | 4/23 | 17 | 1.1786s | 0.0269s | 1 | 8 | yes | 1.1615s | 1.1967s | `detyped_files/richards/shallow/proportion_sweep/main_k04_s17.py` |  |
| 0.17 | 4/23 | 18 | 3.1403s | 0.2618s | 1 | 8 | yes | 2.9950s | 3.3283s | `detyped_files/richards/shallow/proportion_sweep/main_k04_s18.py` |  |
| 0.17 | 4/23 | 19 | 2.9191s | 0.1226s | 1 | 8 | yes | 2.8403s | 2.9971s | `detyped_files/richards/shallow/proportion_sweep/main_k04_s19.py` |  |
| 0.17 | 4/23 | 20 | 1.8735s | 0.1021s | 1 | 8 | yes | 1.8046s | 1.9359s | `detyped_files/richards/shallow/proportion_sweep/main_k04_s20.py` |  |
| 0.22 | 5/23 | 1 | 2.9677s | 0.1317s | 1 | 8 | yes | 2.8829s | 3.0547s | `detyped_files/richards/shallow/proportion_sweep/main_k05_s01.py` |  |
| 0.22 | 5/23 | 2 | 3.4318s | 0.0762s | 1 | 8 | yes | 3.3869s | 3.4848s | `detyped_files/richards/shallow/proportion_sweep/main_k05_s02.py` |  |
| 0.22 | 5/23 | 3 | 3.4234s | 0.0730s | 1 | 8 | yes | 3.3781s | 3.4728s | `detyped_files/richards/shallow/proportion_sweep/main_k05_s03.py` |  |
| 0.22 | 5/23 | 4 | 1.4470s | 0.0732s | 1 | 8 | yes | 1.4041s | 1.4983s | `detyped_files/richards/shallow/proportion_sweep/main_k05_s04.py` |  |
| 0.22 | 5/23 | 5 | 3.6670s | 0.2543s | 1 | 8 | yes | 3.5187s | 3.8444s | `detyped_files/richards/shallow/proportion_sweep/main_k05_s05.py` |  |
| 0.22 | 5/23 | 6 | 1.8917s | 0.1058s | 1 | 8 | yes | 1.8272s | 1.9660s | `detyped_files/richards/shallow/proportion_sweep/main_k05_s06.py` |  |
| 0.22 | 5/23 | 7 | 1.4859s | 0.1045s | 1 | 8 | yes | 1.4208s | 1.5520s | `detyped_files/richards/shallow/proportion_sweep/main_k05_s07.py` |  |
| 0.22 | 5/23 | 8 | 1.1386s | 0.0640s | 1 | 8 | yes | 1.0976s | 1.1790s | `detyped_files/richards/shallow/proportion_sweep/main_k05_s08.py` |  |
| 0.22 | 5/23 | 9 | 2.8621s | 0.0929s | 1 | 8 | yes | 2.7991s | 2.9177s | `detyped_files/richards/shallow/proportion_sweep/main_k05_s09.py` |  |
| 0.22 | 5/23 | 10 | 1.6635s | 0.0369s | 1 | 8 | yes | 1.6373s | 1.6848s | `detyped_files/richards/shallow/proportion_sweep/main_k05_s10.py` |  |
| 0.22 | 5/23 | 11 | 1.1671s | 0.1006s | 1 | 8 | yes | 1.1032s | 1.2328s | `detyped_files/richards/shallow/proportion_sweep/main_k05_s11.py` |  |
| 0.22 | 5/23 | 12 | 1.1945s | 0.0672s | 1 | 8 | yes | 1.1519s | 1.2374s | `detyped_files/richards/shallow/proportion_sweep/main_k05_s12.py` |  |
| 0.22 | 5/23 | 13 | 1.8382s | 0.0625s | 1 | 8 | yes | 1.7978s | 1.8790s | `detyped_files/richards/shallow/proportion_sweep/main_k05_s13.py` |  |
| 0.22 | 5/23 | 14 | 2.9523s | 0.0967s | 1 | 8 | yes | 2.8936s | 3.0186s | `detyped_files/richards/shallow/proportion_sweep/main_k05_s14.py` |  |
| 0.22 | 5/23 | 15 | 1.2063s | 0.0585s | 1 | 8 | yes | 1.1742s | 1.2488s | `detyped_files/richards/shallow/proportion_sweep/main_k05_s15.py` |  |
| 0.22 | 5/23 | 16 | 1.0828s | 0.1034s | 1 | 8 | yes | 1.0176s | 1.1500s | `detyped_files/richards/shallow/proportion_sweep/main_k05_s16.py` |  |
| 0.22 | 5/23 | 17 | 1.8391s | 0.0885s | 1 | 8 | yes | 1.7812s | 1.8954s | `detyped_files/richards/shallow/proportion_sweep/main_k05_s17.py` |  |
| 0.22 | 5/23 | 18 | 1.6537s | 0.1028s | 1 | 8 | yes | 1.5935s | 1.7223s | `detyped_files/richards/shallow/proportion_sweep/main_k05_s18.py` |  |
| 0.22 | 5/23 | 19 | 2.9706s | 0.1235s | 1 | 8 | yes | 2.8998s | 3.0572s | `detyped_files/richards/shallow/proportion_sweep/main_k05_s19.py` |  |
| 0.22 | 5/23 | 20 | 1.6445s | 0.0873s | 1 | 8 | yes | 1.5844s | 1.6972s | `detyped_files/richards/shallow/proportion_sweep/main_k05_s20.py` |  |
| 0.26 | 6/23 | 1 | 1.1546s | 0.1040s | 1 | 8 | yes | 1.0838s | 1.2172s | `detyped_files/richards/shallow/proportion_sweep/main_k06_s01.py` |  |
| 0.26 | 6/23 | 2 | 1.7109s | 0.0671s | 1 | 8 | yes | 1.6655s | 1.7535s | `detyped_files/richards/shallow/proportion_sweep/main_k06_s02.py` |  |
| 0.26 | 6/23 | 3 | 1.0422s | 0.0770s | 1 | 8 | yes | 0.9918s | 1.0909s | `detyped_files/richards/shallow/proportion_sweep/main_k06_s03.py` |  |
| 0.26 | 6/23 | 4 | 1.5411s | 0.0883s | 1 | 8 | yes | 1.4836s | 1.5949s | `detyped_files/richards/shallow/proportion_sweep/main_k06_s04.py` |  |
| 0.26 | 6/23 | 5 | 2.9958s | 0.0546s | 1 | 8 | yes | 2.9584s | 3.0282s | `detyped_files/richards/shallow/proportion_sweep/main_k06_s05.py` |  |
| 0.26 | 6/23 | 6 | 1.3111s | 0.0791s | 1 | 8 | yes | 1.2587s | 1.3674s | `detyped_files/richards/shallow/proportion_sweep/main_k06_s06.py` |  |
| 0.26 | 6/23 | 7 | 1.5694s | 0.1101s | 1 | 8 | yes | 1.5135s | 1.6502s | `detyped_files/richards/shallow/proportion_sweep/main_k06_s07.py` |  |
| 0.26 | 6/23 | 8 | 1.9101s | 0.1062s | 1 | 8 | yes | 1.8504s | 1.9860s | `detyped_files/richards/shallow/proportion_sweep/main_k06_s08.py` |  |
| 0.26 | 6/23 | 9 | 2.1500s | 0.1056s | 1 | 8 | yes | 2.0846s | 2.2203s | `detyped_files/richards/shallow/proportion_sweep/main_k06_s09.py` |  |
| 0.26 | 6/23 | 10 | 1.7581s | 0.1013s | 1 | 8 | yes | 1.6861s | 1.8174s | `detyped_files/richards/shallow/proportion_sweep/main_k06_s10.py` |  |
| 0.26 | 6/23 | 11 | 1.0497s | 0.0768s | 1 | 8 | yes | 1.0002s | 1.0995s | `detyped_files/richards/shallow/proportion_sweep/main_k06_s11.py` |  |
| 0.26 | 6/23 | 12 | 1.2901s | 0.0630s | 1 | 8 | yes | 1.2455s | 1.3233s | `detyped_files/richards/shallow/proportion_sweep/main_k06_s12.py` |  |
| 0.26 | 6/23 | 13 | 3.5226s | 0.0973s | 1 | 8 | yes | 3.4665s | 3.5913s | `detyped_files/richards/shallow/proportion_sweep/main_k06_s13.py` |  |
| 0.26 | 6/23 | 14 | 3.4306s | 0.0949s | 1 | 8 | yes | 3.3737s | 3.4934s | `detyped_files/richards/shallow/proportion_sweep/main_k06_s14.py` |  |
| 0.26 | 6/23 | 15 | 1.2872s | 0.0687s | 1 | 8 | yes | 1.2430s | 1.3323s | `detyped_files/richards/shallow/proportion_sweep/main_k06_s15.py` |  |
| 0.26 | 6/23 | 16 | 3.2193s | 0.0908s | 1 | 8 | yes | 3.1628s | 3.2793s | `detyped_files/richards/shallow/proportion_sweep/main_k06_s16.py` |  |
| 0.26 | 6/23 | 17 | 1.4112s | 0.1329s | 1 | 8 | yes | 1.3329s | 1.4999s | `detyped_files/richards/shallow/proportion_sweep/main_k06_s17.py` |  |
| 0.26 | 6/23 | 18 | 3.4230s | 0.1254s | 1 | 8 | yes | 3.3383s | 3.5010s | `detyped_files/richards/shallow/proportion_sweep/main_k06_s18.py` |  |
| 0.26 | 6/23 | 19 | 1.1458s | 0.0962s | 1 | 8 | yes | 1.0873s | 1.2084s | `detyped_files/richards/shallow/proportion_sweep/main_k06_s19.py` |  |
| 0.26 | 6/23 | 20 | 1.3520s | 0.0828s | 1 | 8 | yes | 1.2969s | 1.4036s | `detyped_files/richards/shallow/proportion_sweep/main_k06_s20.py` |  |
| 0.30 | 7/23 | 1 | 1.3076s | 0.0626s | 1 | 8 | yes | 1.2667s | 1.3472s | `detyped_files/richards/shallow/proportion_sweep/main_k07_s01.py` |  |
| 0.30 | 7/23 | 2 | 3.4080s | 0.1417s | 1 | 8 | yes | 3.3157s | 3.4970s | `detyped_files/richards/shallow/proportion_sweep/main_k07_s02.py` |  |
| 0.30 | 7/23 | 3 | 1.2530s | 0.1051s | 1 | 8 | yes | 1.1881s | 1.3210s | `detyped_files/richards/shallow/proportion_sweep/main_k07_s03.py` |  |
| 0.30 | 7/23 | 4 | 1.4423s | 0.0794s | 1 | 8 | yes | 1.3863s | 1.4883s | `detyped_files/richards/shallow/proportion_sweep/main_k07_s04.py` |  |
| 0.30 | 7/23 | 5 | 1.5664s | 0.0775s | 1 | 8 | yes | 1.5118s | 1.6134s | `detyped_files/richards/shallow/proportion_sweep/main_k07_s05.py` |  |
| 0.30 | 7/23 | 6 | 1.4687s | 0.0954s | 1 | 8 | yes | 1.4100s | 1.5326s | `detyped_files/richards/shallow/proportion_sweep/main_k07_s06.py` |  |
| 0.30 | 7/23 | 7 | 2.0083s | 0.0883s | 1 | 8 | yes | 1.9540s | 2.0678s | `detyped_files/richards/shallow/proportion_sweep/main_k07_s07.py` |  |
| 0.30 | 7/23 | 8 | 3.1482s | 0.0980s | 1 | 8 | yes | 3.0930s | 3.2194s | `detyped_files/richards/shallow/proportion_sweep/main_k07_s08.py` |  |
| 0.30 | 7/23 | 9 | 1.2079s | 0.0655s | 1 | 8 | yes | 1.1653s | 1.2497s | `detyped_files/richards/shallow/proportion_sweep/main_k07_s09.py` |  |
| 0.30 | 7/23 | 10 | 1.5660s | 0.1297s | 1 | 8 | yes | 1.4941s | 1.6583s | `detyped_files/richards/shallow/proportion_sweep/main_k07_s10.py` |  |
| 0.30 | 7/23 | 11 | 1.2264s | 0.1080s | 1 | 8 | yes | 1.1596s | 1.2981s | `detyped_files/richards/shallow/proportion_sweep/main_k07_s11.py` |  |
| 0.30 | 7/23 | 12 | 1.3312s | 0.0711s | 1 | 8 | yes | 1.2849s | 1.3755s | `detyped_files/richards/shallow/proportion_sweep/main_k07_s12.py` |  |
| 0.30 | 7/23 | 13 | 1.8360s | 0.1094s | 1 | 8 | yes | 1.7769s | 1.9145s | `detyped_files/richards/shallow/proportion_sweep/main_k07_s13.py` |  |
| 0.30 | 7/23 | 14 | 1.2535s | 0.0928s | 1 | 8 | yes | 1.1966s | 1.3177s | `detyped_files/richards/shallow/proportion_sweep/main_k07_s14.py` |  |
| 0.30 | 7/23 | 15 | 2.9956s | 0.1107s | 1 | 8 | yes | 2.9275s | 3.0698s | `detyped_files/richards/shallow/proportion_sweep/main_k07_s15.py` |  |
| 0.30 | 7/23 | 16 | 1.6032s | 0.0654s | 1 | 8 | yes | 1.5634s | 1.6493s | `detyped_files/richards/shallow/proportion_sweep/main_k07_s16.py` |  |
| 0.30 | 7/23 | 17 | 3.3828s | 0.1232s | 1 | 8 | yes | 3.3057s | 3.4657s | `detyped_files/richards/shallow/proportion_sweep/main_k07_s17.py` |  |
| 0.30 | 7/23 | 18 | 3.7979s | 0.1113s | 1 | 8 | yes | 3.7343s | 3.8772s | `detyped_files/richards/shallow/proportion_sweep/main_k07_s18.py` |  |
| 0.30 | 7/23 | 19 | 1.5755s | 0.0717s | 1 | 8 | yes | 1.5289s | 1.6216s | `detyped_files/richards/shallow/proportion_sweep/main_k07_s19.py` |  |
| 0.30 | 7/23 | 20 | 1.2993s | 0.0818s | 1 | 8 | yes | 1.2513s | 1.3566s | `detyped_files/richards/shallow/proportion_sweep/main_k07_s20.py` |  |
| 0.35 | 8/23 | 1 | 1.7636s | 0.0842s | 1 | 8 | yes | 1.7133s | 1.8211s | `detyped_files/richards/shallow/proportion_sweep/main_k08_s01.py` |  |
| 0.35 | 8/23 | 2 | 1.7136s | 0.0640s | 1 | 8 | yes | 1.6723s | 1.7544s | `detyped_files/richards/shallow/proportion_sweep/main_k08_s02.py` |  |
| 0.35 | 8/23 | 3 | 2.0065s | 0.0777s | 1 | 8 | yes | 1.9523s | 2.0527s | `detyped_files/richards/shallow/proportion_sweep/main_k08_s03.py` |  |
| 0.35 | 8/23 | 4 | 1.7429s | 0.0661s | 1 | 8 | yes | 1.7027s | 1.7882s | `detyped_files/richards/shallow/proportion_sweep/main_k08_s04.py` |  |
| 0.35 | 8/23 | 5 | 1.4459s | 0.1002s | 1 | 8 | yes | 1.3853s | 1.5140s | `detyped_files/richards/shallow/proportion_sweep/main_k08_s05.py` |  |
| 0.35 | 8/23 | 6 | 3.3141s | 0.1197s | 1 | 8 | yes | 3.2336s | 3.3868s | `detyped_files/richards/shallow/proportion_sweep/main_k08_s06.py` |  |
| 0.35 | 8/23 | 7 | 1.8904s | 0.0708s | 1 | 8 | yes | 1.8385s | 1.9307s | `detyped_files/richards/shallow/proportion_sweep/main_k08_s07.py` |  |
| 0.35 | 8/23 | 8 | 2.1413s | 0.1569s | 1 | 8 | yes | 2.0460s | 2.2454s | `detyped_files/richards/shallow/proportion_sweep/main_k08_s08.py` |  |
| 0.35 | 8/23 | 9 | 2.2847s | 0.1682s | 1 | 8 | yes | 2.1888s | 2.4053s | `detyped_files/richards/shallow/proportion_sweep/main_k08_s09.py` |  |
| 0.35 | 8/23 | 10 | 1.4619s | 0.0584s | 1 | 8 | yes | 1.4197s | 1.4895s | `detyped_files/richards/shallow/proportion_sweep/main_k08_s10.py` |  |
| 0.35 | 8/23 | 11 | 1.4252s | 0.1229s | 1 | 8 | yes | 1.3572s | 1.5150s | `detyped_files/richards/shallow/proportion_sweep/main_k08_s11.py` |  |
| 0.35 | 8/23 | 12 | 1.8793s | 0.0822s | 1 | 8 | yes | 1.8254s | 1.9320s | `detyped_files/richards/shallow/proportion_sweep/main_k08_s12.py` |  |
| 0.35 | 8/23 | 13 | 3.2158s | 0.0659s | 1 | 8 | yes | 3.1694s | 3.2533s | `detyped_files/richards/shallow/proportion_sweep/main_k08_s13.py` |  |
| 0.35 | 8/23 | 14 | 3.2613s | 0.0553s | 1 | 8 | yes | 3.2255s | 3.2974s | `detyped_files/richards/shallow/proportion_sweep/main_k08_s14.py` |  |
| 0.35 | 8/23 | 15 | 2.0135s | 0.0848s | 1 | 8 | yes | 1.9581s | 2.0679s | `detyped_files/richards/shallow/proportion_sweep/main_k08_s15.py` |  |
| 0.35 | 8/23 | 16 | 3.6891s | 0.0801s | 1 | 8 | yes | 3.6418s | 3.7434s | `detyped_files/richards/shallow/proportion_sweep/main_k08_s16.py` |  |
| 0.35 | 8/23 | 17 | 1.4963s | 0.0821s | 1 | 8 | yes | 1.4386s | 1.5452s | `detyped_files/richards/shallow/proportion_sweep/main_k08_s17.py` |  |
| 0.35 | 8/23 | 18 | 1.4959s | 0.0444s | 1 | 8 | yes | 1.4651s | 1.5225s | `detyped_files/richards/shallow/proportion_sweep/main_k08_s18.py` |  |
| 0.35 | 8/23 | 19 | 3.4025s | 0.0957s | 1 | 8 | yes | 3.3396s | 3.4642s | `detyped_files/richards/shallow/proportion_sweep/main_k08_s19.py` |  |
| 0.35 | 8/23 | 20 | 1.9290s | 0.1741s | 1 | 8 | yes | 1.8406s | 2.0562s | `detyped_files/richards/shallow/proportion_sweep/main_k08_s20.py` |  |
| 0.39 | 9/23 | 1 | 1.7696s | 0.0475s | 1 | 8 | yes | 1.7389s | 1.8005s | `detyped_files/richards/shallow/proportion_sweep/main_k09_s01.py` |  |
| 0.39 | 9/23 | 2 | 1.4702s | 0.0615s | 1 | 8 | yes | 1.4270s | 1.5061s | `detyped_files/richards/shallow/proportion_sweep/main_k09_s02.py` |  |
| 0.39 | 9/23 | 3 | 1.4972s | 0.1123s | 1 | 8 | yes | 1.4324s | 1.5756s | `detyped_files/richards/shallow/proportion_sweep/main_k09_s03.py` |  |
| 0.39 | 9/23 | 4 | 1.7868s | 0.0526s | 1 | 8 | yes | 1.7540s | 1.8207s | `detyped_files/richards/shallow/proportion_sweep/main_k09_s04.py` |  |
| 0.39 | 9/23 | 5 | 1.6532s | 0.0943s | 1 | 8 | yes | 1.5972s | 1.7194s | `detyped_files/richards/shallow/proportion_sweep/main_k09_s05.py` |  |
| 0.39 | 9/23 | 6 | 2.0207s | 0.0812s | 1 | 8 | yes | 1.9653s | 2.0690s | `detyped_files/richards/shallow/proportion_sweep/main_k09_s06.py` |  |
| 0.39 | 9/23 | 7 | 1.9760s | 0.0928s | 1 | 8 | yes | 1.9161s | 2.0349s | `detyped_files/richards/shallow/proportion_sweep/main_k09_s07.py` |  |
| 0.39 | 9/23 | 8 | 1.9302s | 0.1004s | 1 | 8 | yes | 1.8685s | 1.9979s | `detyped_files/richards/shallow/proportion_sweep/main_k09_s08.py` |  |
| 0.39 | 9/23 | 9 | 1.8928s | 0.0647s | 1 | 8 | yes | 1.8538s | 1.9368s | `detyped_files/richards/shallow/proportion_sweep/main_k09_s09.py` |  |
| 0.39 | 9/23 | 10 | 3.4751s | 0.0674s | 1 | 8 | yes | 3.4330s | 3.5199s | `detyped_files/richards/shallow/proportion_sweep/main_k09_s10.py` |  |
| 0.39 | 9/23 | 11 | 3.8860s | 0.1299s | 1 | 8 | yes | 3.8036s | 3.9715s | `detyped_files/richards/shallow/proportion_sweep/main_k09_s11.py` |  |
| 0.39 | 9/23 | 12 | 1.4987s | 0.0612s | 1 | 8 | yes | 1.4640s | 1.5419s | `detyped_files/richards/shallow/proportion_sweep/main_k09_s12.py` |  |
| 0.39 | 9/23 | 13 | 1.9024s | 0.0952s | 1 | 8 | yes | 1.8410s | 1.9660s | `detyped_files/richards/shallow/proportion_sweep/main_k09_s13.py` |  |
| 0.39 | 9/23 | 14 | 3.7974s | 0.1478s | 1 | 8 | yes | 3.7087s | 3.9023s | `detyped_files/richards/shallow/proportion_sweep/main_k09_s14.py` |  |
| 0.39 | 9/23 | 15 | 2.0668s | 0.0920s | 1 | 8 | yes | 2.0066s | 2.1271s | `detyped_files/richards/shallow/proportion_sweep/main_k09_s15.py` |  |
| 0.39 | 9/23 | 16 | 3.7720s | 0.1398s | 1 | 8 | yes | 3.6873s | 3.8692s | `detyped_files/richards/shallow/proportion_sweep/main_k09_s16.py` |  |
| 0.39 | 9/23 | 17 | 1.8645s | 0.1548s | 1 | 8 | yes | 1.7879s | 1.9756s | `detyped_files/richards/shallow/proportion_sweep/main_k09_s17.py` |  |
| 0.39 | 9/23 | 18 | 3.4922s | 0.0776s | 1 | 8 | yes | 3.4404s | 3.5394s | `detyped_files/richards/shallow/proportion_sweep/main_k09_s18.py` |  |
| 0.39 | 9/23 | 19 | 2.1212s | 0.0993s | 1 | 8 | yes | 2.0627s | 2.1910s | `detyped_files/richards/shallow/proportion_sweep/main_k09_s19.py` |  |
| 0.39 | 9/23 | 20 | 1.5816s | 0.0632s | 1 | 8 | yes | 1.5399s | 1.6202s | `detyped_files/richards/shallow/proportion_sweep/main_k09_s20.py` |  |
| 0.43 | 10/23 | 1 | 3.9874s | 0.1242s | 1 | 8 | yes | 3.9182s | 4.0789s | `detyped_files/richards/shallow/proportion_sweep/main_k10_s01.py` |  |
| 0.43 | 10/23 | 2 | 1.6425s | 0.0732s | 1 | 8 | yes | 1.5962s | 1.6893s | `detyped_files/richards/shallow/proportion_sweep/main_k10_s02.py` |  |
| 0.43 | 10/23 | 3 | 3.5757s | 0.1300s | 1 | 8 | yes | 3.5028s | 3.6704s | `detyped_files/richards/shallow/proportion_sweep/main_k10_s03.py` |  |
| 0.43 | 10/23 | 4 | 1.9054s | 0.1356s | 1 | 8 | yes | 1.8374s | 2.0041s | `detyped_files/richards/shallow/proportion_sweep/main_k10_s04.py` |  |
| 0.43 | 10/23 | 5 | 3.4488s | 0.1049s | 1 | 8 | yes | 3.3802s | 3.5152s | `detyped_files/richards/shallow/proportion_sweep/main_k10_s05.py` |  |
| 0.43 | 10/23 | 6 | 3.3157s | 0.1290s | 1 | 8 | yes | 3.2388s | 3.4028s | `detyped_files/richards/shallow/proportion_sweep/main_k10_s06.py` |  |
| 0.43 | 10/23 | 7 | 3.3586s | 0.1156s | 1 | 8 | yes | 3.2864s | 3.4363s | `detyped_files/richards/shallow/proportion_sweep/main_k10_s07.py` |  |
| 0.43 | 10/23 | 8 | 3.0970s | 0.0462s | 1 | 8 | yes | 3.0703s | 3.1295s | `detyped_files/richards/shallow/proportion_sweep/main_k10_s08.py` |  |
| 0.43 | 10/23 | 9 | 1.5936s | 0.0833s | 1 | 8 | yes | 1.5405s | 1.6476s | `detyped_files/richards/shallow/proportion_sweep/main_k10_s09.py` |  |
| 0.43 | 10/23 | 10 | 1.5916s | 0.1074s | 1 | 8 | yes | 1.5225s | 1.6617s | `detyped_files/richards/shallow/proportion_sweep/main_k10_s10.py` |  |
| 0.43 | 10/23 | 11 | 4.0891s | 0.0864s | 1 | 8 | yes | 4.0317s | 4.1445s | `detyped_files/richards/shallow/proportion_sweep/main_k10_s11.py` |  |
| 0.43 | 10/23 | 12 | 1.4190s | 0.0522s | 1 | 8 | yes | 1.3864s | 1.4539s | `detyped_files/richards/shallow/proportion_sweep/main_k10_s12.py` |  |
| 0.43 | 10/23 | 13 | 3.7306s | 0.1431s | 1 | 8 | yes | 3.6385s | 3.8229s | `detyped_files/richards/shallow/proportion_sweep/main_k10_s13.py` |  |
| 0.43 | 10/23 | 14 | 3.6293s | 0.1283s | 1 | 8 | yes | 3.5482s | 3.7134s | `detyped_files/richards/shallow/proportion_sweep/main_k10_s14.py` |  |
| 0.43 | 10/23 | 15 | 2.2442s | 0.0790s | 1 | 8 | yes | 2.1943s | 2.2974s | `detyped_files/richards/shallow/proportion_sweep/main_k10_s15.py` |  |
| 0.43 | 10/23 | 16 | 2.3040s | 0.0556s | 1 | 8 | yes | 2.2705s | 2.3419s | `detyped_files/richards/shallow/proportion_sweep/main_k10_s16.py` |  |
| 0.43 | 10/23 | 17 | 3.3822s | 0.1395s | 1 | 8 | yes | 3.2924s | 3.4727s | `detyped_files/richards/shallow/proportion_sweep/main_k10_s17.py` |  |
| 0.43 | 10/23 | 18 | 3.5642s | 0.0734s | 1 | 8 | yes | 3.5169s | 3.6115s | `detyped_files/richards/shallow/proportion_sweep/main_k10_s18.py` |  |
| 0.43 | 10/23 | 19 | 3.3577s | 0.0748s | 1 | 8 | yes | 3.3058s | 3.4004s | `detyped_files/richards/shallow/proportion_sweep/main_k10_s19.py` |  |
| 0.43 | 10/23 | 20 | 3.7017s | 0.1834s | 1 | 8 | yes | 3.5879s | 3.8275s | `detyped_files/richards/shallow/proportion_sweep/main_k10_s20.py` |  |
| 0.48 | 11/23 | 1 | 3.8588s | 0.0950s | 1 | 8 | yes | 3.7976s | 3.9202s | `detyped_files/richards/shallow/proportion_sweep/main_k11_s01.py` |  |
| 0.48 | 11/23 | 2 | 3.8095s | 0.1143s | 1 | 8 | yes | 3.7405s | 3.8859s | `detyped_files/richards/shallow/proportion_sweep/main_k11_s02.py` |  |
| 0.48 | 11/23 | 3 | 2.1807s | 0.1115s | 1 | 8 | yes | 2.1129s | 2.2559s | `detyped_files/richards/shallow/proportion_sweep/main_k11_s03.py` |  |
| 0.48 | 11/23 | 4 | 2.1662s | 0.0828s | 1 | 8 | yes | 2.1078s | 2.2154s | `detyped_files/richards/shallow/proportion_sweep/main_k11_s04.py` |  |
| 0.48 | 11/23 | 5 | 1.9363s | 0.1077s | 1 | 8 | yes | 1.8707s | 2.0123s | `detyped_files/richards/shallow/proportion_sweep/main_k11_s05.py` |  |
| 0.48 | 11/23 | 6 | 1.8054s | 0.1677s | 1 | 8 | yes | 1.7037s | 1.9189s | `detyped_files/richards/shallow/proportion_sweep/main_k11_s06.py` |  |
| 0.48 | 11/23 | 7 | 3.7376s | 0.1384s | 1 | 8 | yes | 3.6460s | 3.8261s | `detyped_files/richards/shallow/proportion_sweep/main_k11_s07.py` |  |
| 0.48 | 11/23 | 8 | 1.5336s | 0.0724s | 1 | 8 | yes | 1.4857s | 1.5788s | `detyped_files/richards/shallow/proportion_sweep/main_k11_s08.py` |  |
| 0.48 | 11/23 | 9 | 3.9211s | 0.1776s | 1 | 8 | yes | 3.8195s | 4.0488s | `detyped_files/richards/shallow/proportion_sweep/main_k11_s09.py` |  |
| 0.48 | 11/23 | 10 | 3.8415s | 0.1940s | 1 | 8 | yes | 3.7240s | 3.9758s | `detyped_files/richards/shallow/proportion_sweep/main_k11_s10.py` |  |
| 0.48 | 11/23 | 11 | 3.5531s | 0.1577s | 1 | 8 | yes | 3.4564s | 3.6593s | `detyped_files/richards/shallow/proportion_sweep/main_k11_s11.py` |  |
| 0.48 | 11/23 | 12 | 3.7671s | 0.1269s | 1 | 8 | yes | 3.6972s | 3.8595s | `detyped_files/richards/shallow/proportion_sweep/main_k11_s12.py` |  |
| 0.48 | 11/23 | 13 | 1.9710s | 0.0833s | 1 | 8 | yes | 1.9254s | 2.0325s | `detyped_files/richards/shallow/proportion_sweep/main_k11_s13.py` |  |
| 0.48 | 11/23 | 14 | 1.8770s | 0.1141s | 1 | 8 | yes | 1.8040s | 1.9525s | `detyped_files/richards/shallow/proportion_sweep/main_k11_s14.py` |  |
| 0.48 | 11/23 | 15 | 2.1444s | 0.0854s | 1 | 8 | yes | 2.0919s | 2.2034s | `detyped_files/richards/shallow/proportion_sweep/main_k11_s15.py` |  |
| 0.48 | 11/23 | 16 | 1.2156s | 0.1096s | 1 | 8 | yes | 1.1524s | 1.2926s | `detyped_files/richards/shallow/proportion_sweep/main_k11_s16.py` |  |
| 0.48 | 11/23 | 17 | 1.8458s | 0.0664s | 1 | 8 | yes | 1.8020s | 1.8864s | `detyped_files/richards/shallow/proportion_sweep/main_k11_s17.py` |  |
| 0.48 | 11/23 | 18 | 2.5501s | 0.1296s | 1 | 8 | yes | 2.4798s | 2.6430s | `detyped_files/richards/shallow/proportion_sweep/main_k11_s18.py` |  |
| 0.48 | 11/23 | 19 | 1.8245s | 0.1286s | 1 | 8 | yes | 1.7512s | 1.9151s | `detyped_files/richards/shallow/proportion_sweep/main_k11_s19.py` |  |
| 0.48 | 11/23 | 20 | 3.4659s | 0.0769s | 1 | 8 | yes | 3.4160s | 3.5144s | `detyped_files/richards/shallow/proportion_sweep/main_k11_s20.py` |  |
| 0.52 | 12/23 | 1 | 3.9190s | 0.0898s | 1 | 8 | yes | 3.8669s | 3.9809s | `detyped_files/richards/shallow/proportion_sweep/main_k12_s01.py` |  |
| 0.52 | 12/23 | 2 | 3.3822s | 0.0706s | 1 | 8 | yes | 3.3383s | 3.4302s | `detyped_files/richards/shallow/proportion_sweep/main_k12_s02.py` |  |
| 0.52 | 12/23 | 3 | 3.8179s | 0.0524s | 1 | 8 | yes | 3.7841s | 3.8504s | `detyped_files/richards/shallow/proportion_sweep/main_k12_s03.py` |  |
| 0.52 | 12/23 | 4 | 1.7853s | 0.0923s | 1 | 8 | yes | 1.7248s | 1.8440s | `detyped_files/richards/shallow/proportion_sweep/main_k12_s04.py` |  |
| 0.52 | 12/23 | 5 | 2.4976s | 0.1189s | 1 | 8 | yes | 2.4275s | 2.5780s | `detyped_files/richards/shallow/proportion_sweep/main_k12_s05.py` |  |
| 0.52 | 12/23 | 6 | 2.2957s | 0.0993s | 1 | 8 | yes | 2.2312s | 2.3586s | `detyped_files/richards/shallow/proportion_sweep/main_k12_s06.py` |  |
| 0.52 | 12/23 | 7 | 1.8463s | 0.0677s | 1 | 8 | yes | 1.8012s | 1.8891s | `detyped_files/richards/shallow/proportion_sweep/main_k12_s07.py` |  |
| 0.52 | 12/23 | 8 | 3.9635s | 0.0735s | 1 | 8 | yes | 3.9283s | 4.0170s | `detyped_files/richards/shallow/proportion_sweep/main_k12_s08.py` |  |
| 0.52 | 12/23 | 9 | 4.3374s | 0.1701s | 1 | 8 | yes | 4.2265s | 4.4457s | `detyped_files/richards/shallow/proportion_sweep/main_k12_s09.py` |  |
| 0.52 | 12/23 | 10 | 2.3706s | 0.1062s | 1 | 8 | yes | 2.3063s | 2.4411s | `detyped_files/richards/shallow/proportion_sweep/main_k12_s10.py` |  |
| 0.52 | 12/23 | 11 | 1.4696s | 0.1265s | 1 | 8 | yes | 1.4058s | 1.5632s | `detyped_files/richards/shallow/proportion_sweep/main_k12_s11.py` |  |
| 0.52 | 12/23 | 12 | 2.2807s | 0.1314s | 1 | 8 | yes | 2.1991s | 2.3680s | `detyped_files/richards/shallow/proportion_sweep/main_k12_s12.py` |  |
| 0.52 | 12/23 | 13 | 3.1718s | 0.1043s | 1 | 8 | yes | 3.1073s | 3.2424s | `detyped_files/richards/shallow/proportion_sweep/main_k12_s13.py` |  |
| 0.52 | 12/23 | 14 | 2.3563s | 0.0988s | 1 | 8 | yes | 2.2974s | 2.4204s | `detyped_files/richards/shallow/proportion_sweep/main_k12_s14.py` |  |
| 0.52 | 12/23 | 15 | 3.6484s | 0.0961s | 1 | 8 | yes | 3.5845s | 3.7078s | `detyped_files/richards/shallow/proportion_sweep/main_k12_s15.py` |  |
| 0.52 | 12/23 | 16 | 2.0014s | 0.0724s | 1 | 8 | yes | 1.9549s | 2.0473s | `detyped_files/richards/shallow/proportion_sweep/main_k12_s16.py` |  |
| 0.52 | 12/23 | 17 | 3.6760s | 0.0961s | 1 | 8 | yes | 3.6184s | 3.7421s | `detyped_files/richards/shallow/proportion_sweep/main_k12_s17.py` |  |
| 0.52 | 12/23 | 18 | 3.8202s | 0.1948s | 1 | 8 | yes | 3.7221s | 3.9640s | `detyped_files/richards/shallow/proportion_sweep/main_k12_s18.py` |  |
| 0.52 | 12/23 | 19 | 3.2298s | 0.0977s | 1 | 8 | yes | 3.1677s | 3.2945s | `detyped_files/richards/shallow/proportion_sweep/main_k12_s19.py` |  |
| 0.52 | 12/23 | 20 | 3.3664s | 0.0572s | 1 | 8 | yes | 3.3315s | 3.4041s | `detyped_files/richards/shallow/proportion_sweep/main_k12_s20.py` |  |
| 0.57 | 13/23 | 1 | 2.1626s | 0.0713s | 1 | 8 | yes | 2.1158s | 2.2080s | `detyped_files/richards/shallow/proportion_sweep/main_k13_s01.py` |  |
| 0.57 | 13/23 | 2 | 3.7446s | 0.0938s | 1 | 8 | yes | 3.6861s | 3.8058s | `detyped_files/richards/shallow/proportion_sweep/main_k13_s02.py` |  |
| 0.57 | 13/23 | 3 | 2.2893s | 0.1074s | 1 | 8 | yes | 2.2208s | 2.3598s | `detyped_files/richards/shallow/proportion_sweep/main_k13_s03.py` |  |
| 0.57 | 13/23 | 4 | 4.0151s | 0.1050s | 1 | 8 | yes | 3.9440s | 4.0803s | `detyped_files/richards/shallow/proportion_sweep/main_k13_s04.py` |  |
| 0.57 | 13/23 | 5 | 2.0771s | 0.1003s | 1 | 8 | yes | 2.0181s | 2.1469s | `detyped_files/richards/shallow/proportion_sweep/main_k13_s05.py` |  |
| 0.57 | 13/23 | 6 | 3.6623s | 0.1024s | 1 | 8 | yes | 3.6011s | 3.7314s | `detyped_files/richards/shallow/proportion_sweep/main_k13_s06.py` |  |
| 0.57 | 13/23 | 7 | 1.4280s | 0.1143s | 1 | 8 | yes | 1.3583s | 1.5047s | `detyped_files/richards/shallow/proportion_sweep/main_k13_s07.py` |  |
| 0.57 | 13/23 | 8 | 2.4194s | 0.1037s | 1 | 8 | yes | 2.3551s | 2.4896s | `detyped_files/richards/shallow/proportion_sweep/main_k13_s08.py` |  |
| 0.57 | 13/23 | 9 | 3.9622s | 0.1745s | 1 | 8 | yes | 3.8589s | 4.0866s | `detyped_files/richards/shallow/proportion_sweep/main_k13_s09.py` |  |
| 0.57 | 13/23 | 10 | 3.2114s | 0.1448s | 1 | 8 | yes | 3.1248s | 3.3101s | `detyped_files/richards/shallow/proportion_sweep/main_k13_s10.py` |  |
| 0.57 | 13/23 | 11 | 3.7055s | 0.1398s | 1 | 8 | yes | 3.6141s | 3.7953s | `detyped_files/richards/shallow/proportion_sweep/main_k13_s11.py` |  |
| 0.57 | 13/23 | 12 | 2.2337s | 0.0224s | 1 | 8 | yes | 2.2198s | 2.2481s | `detyped_files/richards/shallow/proportion_sweep/main_k13_s12.py` |  |
| 0.57 | 13/23 | 13 | 2.3946s | 0.1040s | 1 | 8 | yes | 2.3242s | 2.4589s | `detyped_files/richards/shallow/proportion_sweep/main_k13_s13.py` |  |
| 0.57 | 13/23 | 14 | 3.9826s | 0.1054s | 1 | 8 | yes | 3.9165s | 4.0550s | `detyped_files/richards/shallow/proportion_sweep/main_k13_s14.py` |  |
| 0.57 | 13/23 | 15 | 1.8043s | 0.0675s | 1 | 8 | yes | 1.7668s | 1.8525s | `detyped_files/richards/shallow/proportion_sweep/main_k13_s15.py` |  |
| 0.57 | 13/23 | 16 | 2.1901s | 0.1314s | 1 | 8 | yes | 2.1135s | 2.2827s | `detyped_files/richards/shallow/proportion_sweep/main_k13_s16.py` |  |
| 0.57 | 13/23 | 17 | 4.1882s | 0.1114s | 1 | 8 | yes | 4.1175s | 4.2610s | `detyped_files/richards/shallow/proportion_sweep/main_k13_s17.py` |  |
| 0.57 | 13/23 | 18 | 1.7863s | 0.0555s | 1 | 8 | yes | 1.7458s | 1.8152s | `detyped_files/richards/shallow/proportion_sweep/main_k13_s18.py` |  |
| 0.57 | 13/23 | 19 | 3.9769s | 0.1387s | 1 | 8 | yes | 3.8968s | 4.0744s | `detyped_files/richards/shallow/proportion_sweep/main_k13_s19.py` |  |
| 0.57 | 13/23 | 20 | 3.5257s | 0.1295s | 1 | 8 | yes | 3.4464s | 3.6119s | `detyped_files/richards/shallow/proportion_sweep/main_k13_s20.py` |  |
| 0.61 | 14/23 | 1 | 2.0529s | 0.0674s | 1 | 8 | yes | 2.0069s | 2.0931s | `detyped_files/richards/shallow/proportion_sweep/main_k14_s01.py` |  |
| 0.61 | 14/23 | 2 | 1.3803s | 0.0730s | 1 | 8 | yes | 1.3341s | 1.4264s | `detyped_files/richards/shallow/proportion_sweep/main_k14_s02.py` |  |
| 0.61 | 14/23 | 3 | 2.3971s | 0.0559s | 1 | 8 | yes | 2.3597s | 2.4309s | `detyped_files/richards/shallow/proportion_sweep/main_k14_s03.py` |  |
| 0.61 | 14/23 | 4 | 4.2534s | 0.0385s | 1 | 8 | yes | 4.2292s | 4.2788s | `detyped_files/richards/shallow/proportion_sweep/main_k14_s04.py` |  |
| 0.61 | 14/23 | 5 | 3.7478s | 0.0996s | 1 | 8 | yes | 3.6825s | 3.8103s | `detyped_files/richards/shallow/proportion_sweep/main_k14_s05.py` |  |
| 0.61 | 14/23 | 6 | 2.4731s | 0.1316s | 1 | 8 | yes | 2.3937s | 2.5648s | `detyped_files/richards/shallow/proportion_sweep/main_k14_s06.py` |  |
| 0.61 | 14/23 | 7 | 3.7730s | 0.1064s | 1 | 8 | yes | 3.7097s | 3.8440s | `detyped_files/richards/shallow/proportion_sweep/main_k14_s07.py` |  |
| 0.61 | 14/23 | 8 | 3.4882s | 0.0631s | 1 | 8 | yes | 3.4482s | 3.5285s | `detyped_files/richards/shallow/proportion_sweep/main_k14_s08.py` |  |
| 0.61 | 14/23 | 9 | 2.3979s | 0.1181s | 1 | 8 | yes | 2.3283s | 2.4784s | `detyped_files/richards/shallow/proportion_sweep/main_k14_s09.py` |  |
| 0.61 | 14/23 | 10 | 2.4860s | 0.1702s | 1 | 8 | yes | 2.3839s | 2.6017s | `detyped_files/richards/shallow/proportion_sweep/main_k14_s10.py` |  |
| 0.61 | 14/23 | 11 | 3.7729s | 0.1026s | 1 | 8 | yes | 3.7132s | 3.8448s | `detyped_files/richards/shallow/proportion_sweep/main_k14_s11.py` |  |
| 0.61 | 14/23 | 12 | 2.1661s | 0.1080s | 1 | 8 | yes | 2.0956s | 2.2340s | `detyped_files/richards/shallow/proportion_sweep/main_k14_s12.py` |  |
| 0.61 | 14/23 | 13 | 1.8519s | 0.0763s | 1 | 8 | yes | 1.8010s | 1.8994s | `detyped_files/richards/shallow/proportion_sweep/main_k14_s13.py` |  |
| 0.61 | 14/23 | 14 | 3.7673s | 0.1492s | 1 | 8 | yes | 3.6674s | 3.8620s | `detyped_files/richards/shallow/proportion_sweep/main_k14_s14.py` |  |
| 0.61 | 14/23 | 15 | 4.2633s | 0.0752s | 1 | 8 | yes | 4.2150s | 4.3125s | `detyped_files/richards/shallow/proportion_sweep/main_k14_s15.py` |  |
| 0.61 | 14/23 | 16 | 4.3652s | 0.0738s | 1 | 8 | yes | 4.3168s | 4.4130s | `detyped_files/richards/shallow/proportion_sweep/main_k14_s16.py` |  |
| 0.61 | 14/23 | 17 | 4.0618s | 0.1232s | 1 | 8 | yes | 3.9879s | 4.1471s | `detyped_files/richards/shallow/proportion_sweep/main_k14_s17.py` |  |
| 0.61 | 14/23 | 18 | 3.7796s | 0.0923s | 1 | 8 | yes | 3.7146s | 3.8316s | `detyped_files/richards/shallow/proportion_sweep/main_k14_s18.py` |  |
| 0.61 | 14/23 | 19 | 3.8336s | 0.0923s | 1 | 8 | yes | 3.7759s | 3.8957s | `detyped_files/richards/shallow/proportion_sweep/main_k14_s19.py` |  |
| 0.61 | 14/23 | 20 | 4.1298s | 0.1470s | 1 | 8 | yes | 4.0446s | 4.2348s | `detyped_files/richards/shallow/proportion_sweep/main_k14_s20.py` |  |
| 0.65 | 15/23 | 1 | 4.4449s | 0.0926s | 1 | 8 | yes | 4.3928s | 4.5108s | `detyped_files/richards/shallow/proportion_sweep/main_k15_s01.py` |  |
| 0.65 | 15/23 | 2 | 3.6465s | 0.1115s | 1 | 8 | yes | 3.5732s | 3.7144s | `detyped_files/richards/shallow/proportion_sweep/main_k15_s02.py` |  |
| 0.65 | 15/23 | 3 | 2.5399s | 0.0720s | 1 | 8 | yes | 2.4922s | 2.5862s | `detyped_files/richards/shallow/proportion_sweep/main_k15_s03.py` |  |
| 0.65 | 15/23 | 4 | 3.8550s | 0.1392s | 1 | 8 | yes | 3.7645s | 3.9440s | `detyped_files/richards/shallow/proportion_sweep/main_k15_s04.py` |  |
| 0.65 | 15/23 | 5 | 2.1551s | 0.0735s | 1 | 8 | yes | 2.1124s | 2.2061s | `detyped_files/richards/shallow/proportion_sweep/main_k15_s05.py` |  |
| 0.65 | 15/23 | 6 | 2.4497s | 0.0919s | 1 | 8 | yes | 2.3909s | 2.5095s | `detyped_files/richards/shallow/proportion_sweep/main_k15_s06.py` |  |
| 0.65 | 15/23 | 7 | 1.9313s | 0.0818s | 1 | 8 | yes | 1.8761s | 1.9812s | `detyped_files/richards/shallow/proportion_sweep/main_k15_s07.py` |  |
| 0.65 | 15/23 | 8 | 2.1285s | 0.0251s | 1 | 8 | yes | 2.1143s | 2.1459s | `detyped_files/richards/shallow/proportion_sweep/main_k15_s08.py` |  |
| 0.65 | 15/23 | 9 | 2.3203s | 0.0699s | 1 | 8 | yes | 2.2698s | 2.3581s | `detyped_files/richards/shallow/proportion_sweep/main_k15_s09.py` |  |
| 0.65 | 15/23 | 10 | 3.6142s | 0.1730s | 1 | 8 | yes | 3.5131s | 3.7380s | `detyped_files/richards/shallow/proportion_sweep/main_k15_s10.py` |  |
| 0.65 | 15/23 | 11 | 3.9133s | 0.1633s | 1 | 8 | yes | 3.8162s | 4.0267s | `detyped_files/richards/shallow/proportion_sweep/main_k15_s11.py` |  |
| 0.65 | 15/23 | 12 | 2.1304s | 0.1134s | 1 | 8 | yes | 2.0642s | 2.2114s | `detyped_files/richards/shallow/proportion_sweep/main_k15_s12.py` |  |
| 0.65 | 15/23 | 13 | 4.4113s | 0.1775s | 1 | 8 | yes | 4.3015s | 4.5299s | `detyped_files/richards/shallow/proportion_sweep/main_k15_s13.py` |  |
| 0.65 | 15/23 | 14 | 3.3177s | 0.0931s | 1 | 8 | yes | 3.2613s | 3.3811s | `detyped_files/richards/shallow/proportion_sweep/main_k15_s14.py` |  |
| 0.65 | 15/23 | 15 | 4.0022s | 0.0841s | 1 | 8 | yes | 3.9535s | 4.0603s | `detyped_files/richards/shallow/proportion_sweep/main_k15_s15.py` |  |
| 0.65 | 15/23 | 16 | 4.1854s | 0.2096s | 1 | 8 | yes | 4.0658s | 4.3317s | `detyped_files/richards/shallow/proportion_sweep/main_k15_s16.py` |  |
| 0.65 | 15/23 | 17 | 1.8736s | 0.0381s | 1 | 8 | yes | 1.8483s | 1.8985s | `detyped_files/richards/shallow/proportion_sweep/main_k15_s17.py` |  |
| 0.65 | 15/23 | 18 | 2.6409s | 0.1684s | 1 | 8 | yes | 2.5613s | 2.7640s | `detyped_files/richards/shallow/proportion_sweep/main_k15_s18.py` |  |
| 0.65 | 15/23 | 19 | 4.0737s | 0.1237s | 1 | 8 | yes | 4.0034s | 4.1623s | `detyped_files/richards/shallow/proportion_sweep/main_k15_s19.py` |  |
| 0.65 | 15/23 | 20 | 4.2864s | 0.0845s | 1 | 8 | yes | 4.2341s | 4.3426s | `detyped_files/richards/shallow/proportion_sweep/main_k15_s20.py` |  |
| 0.70 | 16/23 | 1 | 2.5764s | 0.0558s | 1 | 8 | yes | 2.5419s | 2.6139s | `detyped_files/richards/shallow/proportion_sweep/main_k16_s01.py` |  |
| 0.70 | 16/23 | 2 | 4.3912s | 0.1286s | 1 | 8 | yes | 4.3118s | 4.4777s | `detyped_files/richards/shallow/proportion_sweep/main_k16_s02.py` |  |
| 0.70 | 16/23 | 3 | 4.2302s | 0.0864s | 1 | 8 | yes | 4.1782s | 4.2896s | `detyped_files/richards/shallow/proportion_sweep/main_k16_s03.py` |  |
| 0.70 | 16/23 | 4 | 4.3010s | 0.1615s | 1 | 8 | yes | 4.2177s | 4.4210s | `detyped_files/richards/shallow/proportion_sweep/main_k16_s04.py` |  |
| 0.70 | 16/23 | 5 | 4.3160s | 0.0789s | 1 | 8 | yes | 4.2668s | 4.3688s | `detyped_files/richards/shallow/proportion_sweep/main_k16_s05.py` |  |
| 0.70 | 16/23 | 6 | 2.3030s | 0.0849s | 1 | 8 | yes | 2.2501s | 2.3601s | `detyped_files/richards/shallow/proportion_sweep/main_k16_s06.py` |  |
| 0.70 | 16/23 | 7 | 4.3687s | 0.0996s | 1 | 8 | yes | 4.3089s | 4.4358s | `detyped_files/richards/shallow/proportion_sweep/main_k16_s07.py` |  |
| 0.70 | 16/23 | 8 | 3.9171s | 0.1947s | 1 | 8 | yes | 3.8139s | 4.0568s | `detyped_files/richards/shallow/proportion_sweep/main_k16_s08.py` |  |
| 0.70 | 16/23 | 9 | 4.0423s | 0.0787s | 1 | 8 | yes | 3.9889s | 4.0907s | `detyped_files/richards/shallow/proportion_sweep/main_k16_s09.py` |  |
| 0.70 | 16/23 | 10 | 3.9984s | 0.1306s | 1 | 8 | yes | 3.9159s | 4.0866s | `detyped_files/richards/shallow/proportion_sweep/main_k16_s10.py` |  |
| 0.70 | 16/23 | 11 | 2.4485s | 0.0774s | 1 | 8 | yes | 2.3940s | 2.4937s | `detyped_files/richards/shallow/proportion_sweep/main_k16_s11.py` |  |
| 0.70 | 16/23 | 12 | 3.4055s | 0.0868s | 1 | 8 | yes | 3.3517s | 3.4628s | `detyped_files/richards/shallow/proportion_sweep/main_k16_s12.py` |  |
| 0.70 | 16/23 | 13 | 3.4613s | 0.1158s | 1 | 8 | yes | 3.3879s | 3.5382s | `detyped_files/richards/shallow/proportion_sweep/main_k16_s13.py` |  |
| 0.70 | 16/23 | 14 | 2.6452s | 0.0956s | 1 | 8 | yes | 2.5816s | 2.7048s | `detyped_files/richards/shallow/proportion_sweep/main_k16_s14.py` |  |
| 0.70 | 16/23 | 15 | 4.2572s | 0.1786s | 1 | 8 | yes | 4.1533s | 4.3850s | `detyped_files/richards/shallow/proportion_sweep/main_k16_s15.py` |  |
| 0.70 | 16/23 | 16 | 3.9413s | 0.1278s | 1 | 8 | yes | 3.8700s | 4.0300s | `detyped_files/richards/shallow/proportion_sweep/main_k16_s16.py` |  |
| 0.70 | 16/23 | 17 | 4.2590s | 0.0553s | 1 | 8 | yes | 4.2196s | 4.2909s | `detyped_files/richards/shallow/proportion_sweep/main_k16_s17.py` |  |
| 0.70 | 16/23 | 18 | 4.3920s | 0.1192s | 1 | 8 | yes | 4.3149s | 4.4687s | `detyped_files/richards/shallow/proportion_sweep/main_k16_s18.py` |  |
| 0.70 | 16/23 | 19 | 4.5439s | 0.2162s | 1 | 8 | yes | 4.4274s | 4.6929s | `detyped_files/richards/shallow/proportion_sweep/main_k16_s19.py` |  |
| 0.70 | 16/23 | 20 | 3.8667s | 0.1262s | 1 | 8 | yes | 3.7946s | 3.9552s | `detyped_files/richards/shallow/proportion_sweep/main_k16_s20.py` |  |
| 0.74 | 17/23 | 1 | 4.1750s | 0.0868s | 1 | 8 | yes | 4.1118s | 4.2230s | `detyped_files/richards/shallow/proportion_sweep/main_k17_s01.py` |  |
| 0.74 | 17/23 | 2 | 4.0325s | 0.1016s | 1 | 8 | yes | 3.9703s | 4.1009s | `detyped_files/richards/shallow/proportion_sweep/main_k17_s02.py` |  |
| 0.74 | 17/23 | 3 | 4.1652s | 0.0999s | 1 | 8 | yes | 4.1045s | 4.2328s | `detyped_files/richards/shallow/proportion_sweep/main_k17_s03.py` |  |
| 0.74 | 17/23 | 4 | 3.8533s | 0.1017s | 1 | 8 | yes | 3.7935s | 3.9262s | `detyped_files/richards/shallow/proportion_sweep/main_k17_s04.py` |  |
| 0.74 | 17/23 | 5 | 4.0994s | 0.0956s | 1 | 8 | yes | 4.0342s | 4.1581s | `detyped_files/richards/shallow/proportion_sweep/main_k17_s05.py` |  |
| 0.74 | 17/23 | 6 | 2.4071s | 0.0447s | 1 | 8 | yes | 2.3777s | 2.4369s | `detyped_files/richards/shallow/proportion_sweep/main_k17_s06.py` |  |
| 0.74 | 17/23 | 7 | 2.6011s | 0.0846s | 1 | 8 | yes | 2.5461s | 2.6562s | `detyped_files/richards/shallow/proportion_sweep/main_k17_s07.py` |  |
| 0.74 | 17/23 | 8 | 3.7097s | 0.0488s | 1 | 8 | yes | 3.6802s | 3.7426s | `detyped_files/richards/shallow/proportion_sweep/main_k17_s08.py` |  |
| 0.74 | 17/23 | 9 | 4.0280s | 0.0458s | 1 | 8 | yes | 3.9981s | 4.0563s | `detyped_files/richards/shallow/proportion_sweep/main_k17_s09.py` |  |
| 0.74 | 17/23 | 10 | 2.3619s | 0.1234s | 1 | 8 | yes | 2.2815s | 2.4425s | `detyped_files/richards/shallow/proportion_sweep/main_k17_s10.py` |  |
| 0.74 | 17/23 | 11 | 4.0523s | 0.1420s | 1 | 8 | yes | 3.9592s | 4.1413s | `detyped_files/richards/shallow/proportion_sweep/main_k17_s11.py` |  |
| 0.74 | 17/23 | 12 | 4.5588s | 0.1226s | 1 | 8 | yes | 4.4773s | 4.6336s | `detyped_files/richards/shallow/proportion_sweep/main_k17_s12.py` |  |
| 0.74 | 17/23 | 13 | 4.1281s | 0.1389s | 1 | 8 | yes | 4.0396s | 4.2188s | `detyped_files/richards/shallow/proportion_sweep/main_k17_s13.py` |  |
| 0.74 | 17/23 | 14 | 2.2498s | 0.0885s | 1 | 8 | yes | 2.1940s | 2.3093s | `detyped_files/richards/shallow/proportion_sweep/main_k17_s14.py` |  |
| 0.74 | 17/23 | 15 | 4.0038s | 0.1017s | 1 | 8 | yes | 3.9368s | 4.0679s | `detyped_files/richards/shallow/proportion_sweep/main_k17_s15.py` |  |
| 0.74 | 17/23 | 16 | 2.3137s | 0.0978s | 1 | 8 | yes | 2.2529s | 2.3801s | `detyped_files/richards/shallow/proportion_sweep/main_k17_s16.py` |  |
| 0.74 | 17/23 | 17 | 2.0170s | 0.1298s | 1 | 8 | yes | 1.9369s | 2.1042s | `detyped_files/richards/shallow/proportion_sweep/main_k17_s17.py` |  |
| 0.74 | 17/23 | 18 | 3.9285s | 0.0710s | 1 | 8 | yes | 3.8881s | 3.9784s | `detyped_files/richards/shallow/proportion_sweep/main_k17_s18.py` |  |
| 0.74 | 17/23 | 19 | 3.9665s | 0.1035s | 1 | 8 | yes | 3.9011s | 4.0371s | `detyped_files/richards/shallow/proportion_sweep/main_k17_s19.py` |  |
| 0.74 | 17/23 | 20 | 4.1532s | 0.0528s | 1 | 8 | yes | 4.1172s | 4.1837s | `detyped_files/richards/shallow/proportion_sweep/main_k17_s20.py` |  |
| 0.78 | 18/23 | 1 | 4.2091s | 0.1217s | 1 | 8 | yes | 4.1320s | 4.2898s | `detyped_files/richards/shallow/proportion_sweep/main_k18_s01.py` |  |
| 0.78 | 18/23 | 2 | 4.4957s | 0.0975s | 1 | 8 | yes | 4.4307s | 4.5550s | `detyped_files/richards/shallow/proportion_sweep/main_k18_s02.py` |  |
| 0.78 | 18/23 | 3 | 2.4554s | 0.0756s | 1 | 8 | yes | 2.4055s | 2.5041s | `detyped_files/richards/shallow/proportion_sweep/main_k18_s03.py` |  |
| 0.78 | 18/23 | 4 | 2.5463s | 0.0934s | 1 | 8 | yes | 2.4872s | 2.6092s | `detyped_files/richards/shallow/proportion_sweep/main_k18_s04.py` |  |
| 0.78 | 18/23 | 5 | 3.9415s | 0.0990s | 1 | 8 | yes | 3.8804s | 4.0079s | `detyped_files/richards/shallow/proportion_sweep/main_k18_s05.py` |  |
| 0.78 | 18/23 | 6 | 4.1761s | 0.1082s | 1 | 8 | yes | 4.1040s | 4.2448s | `detyped_files/richards/shallow/proportion_sweep/main_k18_s06.py` |  |
| 0.78 | 18/23 | 7 | 4.4795s | 0.1721s | 1 | 8 | yes | 4.3759s | 4.5951s | `detyped_files/richards/shallow/proportion_sweep/main_k18_s07.py` |  |
| 0.78 | 18/23 | 8 | 3.8355s | 0.0756s | 1 | 8 | yes | 3.7859s | 3.8832s | `detyped_files/richards/shallow/proportion_sweep/main_k18_s08.py` |  |
| 0.78 | 18/23 | 9 | 4.2285s | 0.1831s | 1 | 8 | yes | 4.1282s | 4.3587s | `detyped_files/richards/shallow/proportion_sweep/main_k18_s09.py` |  |
| 0.78 | 18/23 | 10 | 4.1336s | 0.1133s | 1 | 8 | yes | 4.0563s | 4.2008s | `detyped_files/richards/shallow/proportion_sweep/main_k18_s10.py` |  |
| 0.78 | 18/23 | 11 | 4.2281s | 0.1025s | 1 | 8 | yes | 4.1589s | 4.2902s | `detyped_files/richards/shallow/proportion_sweep/main_k18_s11.py` |  |
| 0.78 | 18/23 | 12 | 4.0747s | 0.1005s | 1 | 8 | yes | 4.0152s | 4.1411s | `detyped_files/richards/shallow/proportion_sweep/main_k18_s12.py` |  |
| 0.78 | 18/23 | 13 | 4.2196s | 0.1232s | 1 | 8 | yes | 4.1435s | 4.3029s | `detyped_files/richards/shallow/proportion_sweep/main_k18_s13.py` |  |
| 0.78 | 18/23 | 14 | 4.5071s | 0.0870s | 1 | 8 | yes | 4.4533s | 4.5631s | `detyped_files/richards/shallow/proportion_sweep/main_k18_s14.py` |  |
| 0.78 | 18/23 | 15 | 4.1605s | 0.1234s | 1 | 8 | yes | 4.0834s | 4.2400s | `detyped_files/richards/shallow/proportion_sweep/main_k18_s15.py` |  |
| 0.78 | 18/23 | 16 | 4.4533s | 0.0915s | 1 | 8 | yes | 4.3897s | 4.5074s | `detyped_files/richards/shallow/proportion_sweep/main_k18_s16.py` |  |
| 0.78 | 18/23 | 17 | 4.4592s | 0.0850s | 1 | 8 | yes | 4.4033s | 4.5135s | `detyped_files/richards/shallow/proportion_sweep/main_k18_s17.py` |  |
| 0.78 | 18/23 | 18 | 4.0657s | 0.2341s | 1 | 8 | yes | 3.9449s | 4.2343s | `detyped_files/richards/shallow/proportion_sweep/main_k18_s18.py` |  |
| 0.78 | 18/23 | 19 | 4.4886s | 0.0691s | 1 | 8 | yes | 4.4542s | 4.5394s | `detyped_files/richards/shallow/proportion_sweep/main_k18_s19.py` |  |
| 0.78 | 18/23 | 20 | 2.7164s | 0.1137s | 1 | 8 | yes | 2.6504s | 2.7932s | `detyped_files/richards/shallow/proportion_sweep/main_k18_s20.py` |  |
| 0.83 | 19/23 | 1 | 4.2015s | 0.1755s | 1 | 8 | yes | 4.0976s | 4.3198s | `detyped_files/richards/shallow/proportion_sweep/main_k19_s01.py` |  |
| 0.83 | 19/23 | 2 | 4.5460s | 0.1375s | 1 | 8 | yes | 4.4637s | 4.6398s | `detyped_files/richards/shallow/proportion_sweep/main_k19_s02.py` |  |
| 0.83 | 19/23 | 3 | 4.3634s | 0.1754s | 1 | 8 | yes | 4.2519s | 4.4814s | `detyped_files/richards/shallow/proportion_sweep/main_k19_s03.py` |  |
| 0.83 | 19/23 | 4 | 4.1679s | 0.0935s | 1 | 8 | yes | 4.1060s | 4.2253s | `detyped_files/richards/shallow/proportion_sweep/main_k19_s04.py` |  |
| 0.83 | 19/23 | 5 | 2.8107s | 0.0975s | 1 | 8 | yes | 2.7516s | 2.8763s | `detyped_files/richards/shallow/proportion_sweep/main_k19_s05.py` |  |
| 0.83 | 19/23 | 6 | 2.7646s | 0.0974s | 1 | 8 | yes | 2.7062s | 2.8312s | `detyped_files/richards/shallow/proportion_sweep/main_k19_s06.py` |  |
| 0.83 | 19/23 | 7 | 4.4429s | 0.0970s | 1 | 8 | yes | 4.3808s | 4.5053s | `detyped_files/richards/shallow/proportion_sweep/main_k19_s07.py` |  |
| 0.83 | 19/23 | 8 | 4.1802s | 0.0986s | 1 | 8 | yes | 4.1192s | 4.2457s | `detyped_files/richards/shallow/proportion_sweep/main_k19_s08.py` |  |
| 0.83 | 19/23 | 9 | 3.8608s | 0.0852s | 1 | 8 | yes | 3.8074s | 3.9185s | `detyped_files/richards/shallow/proportion_sweep/main_k19_s09.py` |  |
| 0.83 | 19/23 | 10 | 4.5778s | 0.1032s | 1 | 8 | yes | 4.5074s | 4.6415s | `detyped_files/richards/shallow/proportion_sweep/main_k19_s10.py` |  |
| 0.83 | 19/23 | 11 | 3.7713s | 0.1945s | 1 | 8 | yes | 3.6590s | 3.9105s | `detyped_files/richards/shallow/proportion_sweep/main_k19_s11.py` |  |
| 0.83 | 19/23 | 12 | 3.9595s | 0.1327s | 1 | 8 | yes | 3.8751s | 4.0486s | `detyped_files/richards/shallow/proportion_sweep/main_k19_s12.py` |  |
| 0.83 | 19/23 | 13 | 4.1841s | 0.1061s | 1 | 8 | yes | 4.1179s | 4.2530s | `detyped_files/richards/shallow/proportion_sweep/main_k19_s13.py` |  |
| 0.83 | 19/23 | 14 | 4.5803s | 0.1221s | 1 | 8 | yes | 4.5099s | 4.6645s | `detyped_files/richards/shallow/proportion_sweep/main_k19_s14.py` |  |
| 0.83 | 19/23 | 15 | 4.3436s | 0.1269s | 1 | 8 | yes | 4.2620s | 4.4258s | `detyped_files/richards/shallow/proportion_sweep/main_k19_s15.py` |  |
| 0.83 | 19/23 | 16 | 4.3030s | 0.1249s | 1 | 8 | yes | 4.2246s | 4.3858s | `detyped_files/richards/shallow/proportion_sweep/main_k19_s16.py` |  |
| 0.83 | 19/23 | 17 | 4.1632s | 0.0721s | 1 | 8 | yes | 4.1118s | 4.2038s | `detyped_files/richards/shallow/proportion_sweep/main_k19_s17.py` |  |
| 0.83 | 19/23 | 18 | 4.0602s | 0.1351s | 1 | 8 | yes | 3.9850s | 4.1594s | `detyped_files/richards/shallow/proportion_sweep/main_k19_s18.py` |  |
| 0.83 | 19/23 | 19 | 3.5905s | 0.1031s | 1 | 8 | yes | 3.5178s | 3.6503s | `detyped_files/richards/shallow/proportion_sweep/main_k19_s19.py` |  |
| 0.83 | 19/23 | 20 | 4.3727s | 0.1118s | 1 | 8 | yes | 4.3016s | 4.4466s | `detyped_files/richards/shallow/proportion_sweep/main_k19_s20.py` |  |
| 0.87 | 20/23 | 1 | 2.7112s | 0.1064s | 1 | 8 | yes | 2.6444s | 2.7810s | `detyped_files/richards/shallow/proportion_sweep/main_k20_s01.py` |  |
| 0.87 | 20/23 | 2 | 4.6339s | 0.4226s | 1 | 8 | yes | 4.4422s | 4.9427s | `detyped_files/richards/shallow/proportion_sweep/main_k20_s02.py` |  |
| 0.87 | 20/23 | 3 | 3.9309s | 0.1478s | 1 | 8 | yes | 3.8447s | 4.0357s | `detyped_files/richards/shallow/proportion_sweep/main_k20_s03.py` |  |
| 0.87 | 20/23 | 4 | 4.3180s | 0.0924s | 1 | 8 | yes | 4.2621s | 4.3804s | `detyped_files/richards/shallow/proportion_sweep/main_k20_s04.py` |  |
| 0.87 | 20/23 | 5 | 4.4880s | 0.1180s | 1 | 8 | yes | 4.4119s | 4.5631s | `detyped_files/richards/shallow/proportion_sweep/main_k20_s05.py` |  |
| 0.87 | 20/23 | 6 | 4.6139s | 0.2244s | 1 | 8 | yes | 4.4755s | 4.7645s | `detyped_files/richards/shallow/proportion_sweep/main_k20_s06.py` |  |
| 0.87 | 20/23 | 7 | 4.0976s | 0.1003s | 1 | 8 | yes | 4.0358s | 4.1670s | `detyped_files/richards/shallow/proportion_sweep/main_k20_s07.py` |  |
| 0.87 | 20/23 | 8 | 4.1784s | 0.2577s | 1 | 8 | yes | 4.0297s | 4.3637s | `detyped_files/richards/shallow/proportion_sweep/main_k20_s08.py` |  |
| 0.87 | 20/23 | 9 | 4.4475s | 0.1632s | 1 | 8 | yes | 4.3553s | 4.5632s | `detyped_files/richards/shallow/proportion_sweep/main_k20_s09.py` |  |
| 0.87 | 20/23 | 10 | 4.4926s | 0.1170s | 1 | 8 | yes | 4.4207s | 4.5700s | `detyped_files/richards/shallow/proportion_sweep/main_k20_s10.py` |  |
| 0.87 | 20/23 | 11 | 4.1123s | 0.2038s | 1 | 8 | yes | 4.0021s | 4.2594s | `detyped_files/richards/shallow/proportion_sweep/main_k20_s11.py` |  |
| 0.87 | 20/23 | 12 | 4.3814s | 0.1017s | 1 | 8 | yes | 4.3120s | 4.4435s | `detyped_files/richards/shallow/proportion_sweep/main_k20_s12.py` |  |
| 0.87 | 20/23 | 13 | 4.3559s | 0.0536s | 1 | 8 | yes | 4.3221s | 4.3904s | `detyped_files/richards/shallow/proportion_sweep/main_k20_s13.py` |  |
| 0.87 | 20/23 | 14 | 4.6828s | 0.1568s | 1 | 8 | yes | 4.5780s | 4.7837s | `detyped_files/richards/shallow/proportion_sweep/main_k20_s14.py` |  |
| 0.87 | 20/23 | 15 | 4.6079s | 0.1369s | 1 | 8 | yes | 4.5291s | 4.7011s | `detyped_files/richards/shallow/proportion_sweep/main_k20_s15.py` |  |
| 0.87 | 20/23 | 16 | 4.6372s | 0.2335s | 1 | 8 | yes | 4.5139s | 4.8080s | `detyped_files/richards/shallow/proportion_sweep/main_k20_s16.py` |  |
| 0.87 | 20/23 | 17 | 2.7379s | 0.0745s | 1 | 8 | yes | 2.6885s | 2.7844s | `detyped_files/richards/shallow/proportion_sweep/main_k20_s17.py` |  |
| 0.87 | 20/23 | 18 | 4.4645s | 0.1915s | 1 | 8 | yes | 4.3598s | 4.6019s | `detyped_files/richards/shallow/proportion_sweep/main_k20_s18.py` |  |
| 0.87 | 20/23 | 19 | 4.0410s | 0.0467s | 1 | 8 | yes | 4.0100s | 4.0709s | `detyped_files/richards/shallow/proportion_sweep/main_k20_s19.py` |  |
| 0.87 | 20/23 | 20 | 4.4359s | 0.1400s | 1 | 8 | yes | 4.3490s | 4.5310s | `detyped_files/richards/shallow/proportion_sweep/main_k20_s20.py` |  |
| 0.91 | 21/23 | 1 | 4.5586s | 0.1536s | 1 | 8 | yes | 4.4621s | 4.6582s | `detyped_files/richards/shallow/proportion_sweep/main_k21_s01.py` |  |
| 0.91 | 21/23 | 2 | 4.7211s | 0.2041s | 1 | 8 | yes | 4.6021s | 4.8661s | `detyped_files/richards/shallow/proportion_sweep/main_k21_s02.py` |  |
| 0.91 | 21/23 | 3 | 4.5908s | 0.1432s | 1 | 8 | yes | 4.5063s | 4.6902s | `detyped_files/richards/shallow/proportion_sweep/main_k21_s03.py` |  |
| 0.91 | 21/23 | 4 | 4.5909s | 0.1189s | 1 | 8 | yes | 4.5110s | 4.6623s | `detyped_files/richards/shallow/proportion_sweep/main_k21_s04.py` |  |
| 0.91 | 21/23 | 5 | 4.2233s | 0.0789s | 1 | 8 | yes | 4.1722s | 4.2732s | `detyped_files/richards/shallow/proportion_sweep/main_k21_s05.py` |  |
| 0.91 | 21/23 | 6 | 4.2188s | 0.1562s | 1 | 8 | yes | 4.1196s | 4.3218s | `detyped_files/richards/shallow/proportion_sweep/main_k21_s06.py` |  |
| 0.91 | 21/23 | 7 | 4.5588s | 0.1035s | 1 | 8 | yes | 4.4963s | 4.6282s | `detyped_files/richards/shallow/proportion_sweep/main_k21_s07.py` |  |
| 0.91 | 21/23 | 8 | 4.4476s | 0.1229s | 1 | 8 | yes | 4.3714s | 4.5341s | `detyped_files/richards/shallow/proportion_sweep/main_k21_s08.py` |  |
| 0.91 | 21/23 | 9 | 3.8842s | 0.1372s | 1 | 8 | yes | 3.8016s | 3.9796s | `detyped_files/richards/shallow/proportion_sweep/main_k21_s09.py` |  |
| 0.91 | 21/23 | 10 | 4.5115s | 0.0828s | 1 | 8 | yes | 4.4533s | 4.5602s | `detyped_files/richards/shallow/proportion_sweep/main_k21_s10.py` |  |
| 0.91 | 21/23 | 11 | 4.5356s | 0.0951s | 1 | 8 | yes | 4.4750s | 4.5990s | `detyped_files/richards/shallow/proportion_sweep/main_k21_s11.py` |  |
| 0.91 | 21/23 | 12 | 4.6521s | 0.2161s | 1 | 8 | yes | 4.5293s | 4.8056s | `detyped_files/richards/shallow/proportion_sweep/main_k21_s12.py` |  |
| 0.91 | 21/23 | 13 | 4.3136s | 0.1351s | 1 | 8 | yes | 4.2301s | 4.4014s | `detyped_files/richards/shallow/proportion_sweep/main_k21_s13.py` |  |
| 0.91 | 21/23 | 14 | 4.5077s | 0.0431s | 1 | 8 | yes | 4.4806s | 4.5365s | `detyped_files/richards/shallow/proportion_sweep/main_k21_s14.py` |  |
| 0.91 | 21/23 | 15 | 2.6771s | 0.0886s | 1 | 8 | yes | 2.6287s | 2.7406s | `detyped_files/richards/shallow/proportion_sweep/main_k21_s15.py` |  |
| 0.91 | 21/23 | 16 | 3.9699s | 0.1189s | 1 | 8 | yes | 3.9008s | 4.0574s | `detyped_files/richards/shallow/proportion_sweep/main_k21_s16.py` |  |
| 0.91 | 21/23 | 17 | 4.5161s | 0.1070s | 1 | 8 | yes | 4.4410s | 4.5818s | `detyped_files/richards/shallow/proportion_sweep/main_k21_s17.py` |  |
| 0.91 | 21/23 | 18 | 4.4816s | 0.1456s | 1 | 8 | yes | 4.4051s | 4.5888s | `detyped_files/richards/shallow/proportion_sweep/main_k21_s18.py` |  |
| 0.91 | 21/23 | 19 | 4.4786s | 0.0918s | 1 | 8 | yes | 4.4182s | 4.5368s | `detyped_files/richards/shallow/proportion_sweep/main_k21_s19.py` |  |
| 0.91 | 21/23 | 20 | 4.4744s | 0.1746s | 1 | 8 | yes | 4.3807s | 4.5970s | `detyped_files/richards/shallow/proportion_sweep/main_k21_s20.py` |  |
| 0.96 | 22/23 | 1 | 4.5698s | 0.1329s | 1 | 8 | yes | 4.4900s | 4.6634s | `detyped_files/richards/shallow/proportion_sweep/main_k22_s01.py` |  |
| 0.96 | 22/23 | 2 | 4.2421s | 0.1050s | 1 | 8 | yes | 4.1705s | 4.3078s | `detyped_files/richards/shallow/proportion_sweep/main_k22_s02.py` |  |
| 0.96 | 22/23 | 3 | 4.5088s | 0.1425s | 1 | 8 | yes | 4.4146s | 4.5992s | `detyped_files/richards/shallow/proportion_sweep/main_k22_s03.py` |  |
| 0.96 | 22/23 | 4 | 4.5512s | 0.1211s | 1 | 8 | yes | 4.4720s | 4.6267s | `detyped_files/richards/shallow/proportion_sweep/main_k22_s04.py` |  |
| 0.96 | 22/23 | 5 | 4.5580s | 0.0623s | 1 | 8 | yes | 4.5175s | 4.5977s | `detyped_files/richards/shallow/proportion_sweep/main_k22_s05.py` |  |
| 0.96 | 22/23 | 6 | 4.6113s | 0.1580s | 1 | 8 | yes | 4.5120s | 4.7142s | `detyped_files/richards/shallow/proportion_sweep/main_k22_s06.py` |  |
| 0.96 | 22/23 | 7 | 4.4794s | 0.2709s | 1 | 8 | yes | 4.3490s | 4.6808s | `detyped_files/richards/shallow/proportion_sweep/main_k22_s07.py` |  |
| 0.96 | 22/23 | 8 | 4.1926s | 0.1484s | 1 | 8 | yes | 4.1141s | 4.3000s | `detyped_files/richards/shallow/proportion_sweep/main_k22_s08.py` |  |
| 0.96 | 22/23 | 9 | 4.5097s | 0.1502s | 1 | 8 | yes | 4.4153s | 4.6110s | `detyped_files/richards/shallow/proportion_sweep/main_k22_s09.py` |  |
| 0.96 | 22/23 | 10 | 4.6504s | 0.1820s | 1 | 8 | yes | 4.5488s | 4.7818s | `detyped_files/richards/shallow/proportion_sweep/main_k22_s10.py` |  |
| 0.96 | 22/23 | 11 | 4.5435s | 0.1640s | 1 | 8 | yes | 4.4390s | 4.6513s | `detyped_files/richards/shallow/proportion_sweep/main_k22_s11.py` |  |
| 0.96 | 22/23 | 12 | 4.6320s | 0.0900s | 1 | 8 | yes | 4.5764s | 4.6905s | `detyped_files/richards/shallow/proportion_sweep/main_k22_s12.py` |  |
| 0.96 | 22/23 | 13 | 4.5862s | 0.1732s | 1 | 8 | yes | 4.4794s | 4.7014s | `detyped_files/richards/shallow/proportion_sweep/main_k22_s13.py` |  |
| 0.96 | 22/23 | 14 | 4.6181s | 0.0947s | 1 | 8 | yes | 4.5570s | 4.6787s | `detyped_files/richards/shallow/proportion_sweep/main_k22_s14.py` |  |
| 0.96 | 22/23 | 15 | 4.4578s | 0.0470s | 1 | 8 | yes | 4.4282s | 4.4894s | `detyped_files/richards/shallow/proportion_sweep/main_k22_s15.py` |  |
| 0.96 | 22/23 | 16 | 4.6723s | 0.3288s | 1 | 8 | yes | 4.4908s | 4.9108s | `detyped_files/richards/shallow/proportion_sweep/main_k22_s16.py` |  |
| 0.96 | 22/23 | 17 | 4.6293s | 0.1671s | 1 | 8 | yes | 4.5273s | 4.7403s | `detyped_files/richards/shallow/proportion_sweep/main_k22_s17.py` |  |
| 0.96 | 22/23 | 18 | 4.5124s | 0.1044s | 1 | 8 | yes | 4.4507s | 4.5843s | `detyped_files/richards/shallow/proportion_sweep/main_k22_s18.py` |  |
| 0.96 | 22/23 | 19 | 4.5907s | 0.1209s | 1 | 8 | yes | 4.5134s | 4.6691s | `detyped_files/richards/shallow/proportion_sweep/main_k22_s19.py` |  |
| 0.96 | 22/23 | 20 | 4.3477s | 0.0892s | 1 | 8 | yes | 4.2890s | 4.4029s | `detyped_files/richards/shallow/proportion_sweep/main_k22_s20.py` |  |
| 1.00 | 23/23 | 1 | 4.5864s | 0.1712s | 1 | 8 | yes | 4.4795s | 4.6964s | `detyped_files/richards/shallow/proportion_sweep/main_k23_s01.py` |  |

## richards/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.7972s | 0.7972s | 0.7972s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.7972s | 0.0721s | 1 | 8 | yes | 0.7481s | 0.8422s | `static-python-perf/Benchmark/richards/untyped/main.py` |  |
