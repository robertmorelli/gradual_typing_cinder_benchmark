# Proportion Benchmark Report

- Generated: `2026-04-04T12:03:26-06:00`
- Benchmarks run serially: `yes`
- Iterations per detyped-count bucket: `10`
- Random seed: `0`

## call_method/advanced

- Detypable targets: `6`
- Total runs: `44`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1137s | 0.1137s | 0.1137s | 2.0 | yes | ok |
| 0.17 | 1/6 | 6 | 0.3232s | 0.1177s | 1.1661s | 1.0 | yes | ok |
| 0.33 | 2/6 | 10 | 0.5036s | 0.1269s | 1.3019s | 1.0 | yes | ok |
| 0.50 | 3/6 | 10 | 1.0009s | 0.1594s | 1.4177s | 1.0 | yes | ok |
| 0.67 | 4/6 | 10 | 0.9238s | 0.1816s | 1.3848s | 1.1 | yes | ok |
| 0.83 | 5/6 | 6 | 1.1937s | 0.3162s | 1.4077s | 1.0 | yes | ok |
| 1.00 | 6/6 | 1 | 1.4077s | 1.4077s | 1.4077s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1137s | 0.0165s | 2 | 16 | yes | 0.1064s | 0.1219s | `detyped_files/call_method/advanced/proportion_sweep/main_0x0_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 0.2685s | 0.0298s | 1 | 8 | yes | 0.2483s | 0.2860s | `detyped_files/call_method/advanced/proportion_sweep/main_0x4_k01_s01.py` |  |
| 0.17 | 1/6 | 2 | 0.1184s | 0.0100s | 1 | 8 | yes | 0.1113s | 0.1242s | `detyped_files/call_method/advanced/proportion_sweep/main_0x20_k01_s02.py` |  |
| 0.17 | 1/6 | 3 | 0.1368s | 0.0202s | 1 | 8 | yes | 0.1245s | 0.1498s | `detyped_files/call_method/advanced/proportion_sweep/main_0x8_k01_s03.py` |  |
| 0.17 | 1/6 | 4 | 1.1661s | 0.0760s | 1 | 8 | yes | 1.1157s | 1.2159s | `detyped_files/call_method/advanced/proportion_sweep/main_0x2_k01_s04.py` |  |
| 0.17 | 1/6 | 5 | 0.1316s | 0.0152s | 1 | 8 | yes | 0.1214s | 0.1411s | `detyped_files/call_method/advanced/proportion_sweep/main_0x10_k01_s05.py` |  |
| 0.17 | 1/6 | 6 | 0.1177s | 0.0119s | 1 | 8 | yes | 0.1116s | 0.1264s | `detyped_files/call_method/advanced/proportion_sweep/main_0x1_k01_s06.py` |  |
| 0.33 | 2/6 | 1 | 1.2218s | 0.0649s | 1 | 8 | yes | 1.1776s | 1.2598s | `detyped_files/call_method/advanced/proportion_sweep/main_0x12_k02_s01.py` |  |
| 0.33 | 2/6 | 2 | 0.1495s | 0.0170s | 1 | 8 | yes | 0.1376s | 0.1598s | `detyped_files/call_method/advanced/proportion_sweep/main_0x28_k02_s02.py` |  |
| 0.33 | 2/6 | 3 | 0.1269s | 0.0032s | 1 | 8 | yes | 0.1250s | 0.1291s | `detyped_files/call_method/advanced/proportion_sweep/main_0x21_k02_s03.py` |  |
| 0.33 | 2/6 | 4 | 0.1368s | 0.0070s | 1 | 8 | yes | 0.1323s | 0.1413s | `detyped_files/call_method/advanced/proportion_sweep/main_0x9_k02_s04.py` |  |
| 0.33 | 2/6 | 5 | 1.3019s | 0.0713s | 1 | 8 | yes | 1.2569s | 1.3492s | `detyped_files/call_method/advanced/proportion_sweep/main_0x6_k02_s05.py` |  |
| 0.33 | 2/6 | 6 | 0.3065s | 0.0148s | 1 | 8 | yes | 0.2979s | 0.3165s | `detyped_files/call_method/advanced/proportion_sweep/main_0xc_k02_s06.py` |  |
| 0.33 | 2/6 | 7 | 1.2046s | 0.0863s | 1 | 8 | yes | 1.1533s | 1.2649s | `detyped_files/call_method/advanced/proportion_sweep/main_0x22_k02_s07.py` |  |
| 0.33 | 2/6 | 8 | 0.2991s | 0.0104s | 1 | 8 | yes | 0.2931s | 0.3064s | `detyped_files/call_method/advanced/proportion_sweep/main_0x24_k02_s08.py` |  |
| 0.33 | 2/6 | 9 | 0.1520s | 0.0046s | 1 | 8 | yes | 0.1489s | 0.1550s | `detyped_files/call_method/advanced/proportion_sweep/main_0x18_k02_s09.py` |  |
| 0.33 | 2/6 | 10 | 0.1363s | 0.0152s | 1 | 8 | yes | 0.1271s | 0.1467s | `detyped_files/call_method/advanced/proportion_sweep/main_0x11_k02_s10.py` |  |
| 0.50 | 3/6 | 1 | 1.3669s | 0.0652s | 1 | 8 | yes | 1.3266s | 1.4115s | `detyped_files/call_method/advanced/proportion_sweep/main_0x16_k03_s01.py` |  |
| 0.50 | 3/6 | 2 | 0.1594s | 0.0204s | 1 | 8 | yes | 0.1493s | 0.1743s | `detyped_files/call_method/advanced/proportion_sweep/main_0x29_k03_s02.py` |  |
| 0.50 | 3/6 | 3 | 1.3466s | 0.0742s | 1 | 8 | yes | 1.2987s | 1.3942s | `detyped_files/call_method/advanced/proportion_sweep/main_0x26_k03_s03.py` |  |
| 0.50 | 3/6 | 4 | 1.2884s | 0.0760s | 1 | 8 | yes | 1.2393s | 1.3378s | `detyped_files/call_method/advanced/proportion_sweep/main_0xb_k03_s04.py` |  |
| 0.50 | 3/6 | 5 | 1.2930s | 0.0892s | 1 | 8 | yes | 1.2377s | 1.3544s | `detyped_files/call_method/advanced/proportion_sweep/main_0x1a_k03_s05.py` |  |
| 0.50 | 3/6 | 6 | 0.3023s | 0.0298s | 1 | 8 | yes | 0.2847s | 0.3229s | `detyped_files/call_method/advanced/proportion_sweep/main_0x25_k03_s06.py` |  |
| 0.50 | 3/6 | 7 | 0.1729s | 0.0138s | 1 | 8 | yes | 0.1630s | 0.1808s | `detyped_files/call_method/advanced/proportion_sweep/main_0x38_k03_s07.py` |  |
| 0.50 | 3/6 | 8 | 1.3077s | 0.1142s | 1 | 8 | yes | 1.2417s | 1.3866s | `detyped_files/call_method/advanced/proportion_sweep/main_0x13_k03_s08.py` |  |
| 0.50 | 3/6 | 9 | 1.3539s | 0.0601s | 1 | 8 | yes | 1.3112s | 1.3885s | `detyped_files/call_method/advanced/proportion_sweep/main_0x7_k03_s09.py` |  |
| 0.50 | 3/6 | 10 | 1.4177s | 0.1168s | 1 | 8 | yes | 1.3488s | 1.4963s | `detyped_files/call_method/advanced/proportion_sweep/main_0xe_k03_s10.py` |  |
| 0.67 | 4/6 | 1 | 0.3381s | 0.0305s | 1 | 8 | yes | 0.3160s | 0.3547s | `detyped_files/call_method/advanced/proportion_sweep/main_0x3c_k04_s01.py` |  |
| 0.67 | 4/6 | 2 | 1.3505s | 0.0506s | 1 | 8 | yes | 1.3199s | 1.3839s | `detyped_files/call_method/advanced/proportion_sweep/main_0x2e_k04_s02.py` |  |
| 0.67 | 4/6 | 3 | 0.1816s | 0.0246s | 1 | 8 | yes | 0.1658s | 0.1973s | `detyped_files/call_method/advanced/proportion_sweep/main_0x39_k04_s03.py` |  |
| 0.67 | 4/6 | 4 | 1.2787s | 0.0944s | 1 | 8 | yes | 1.2187s | 1.3408s | `detyped_files/call_method/advanced/proportion_sweep/main_0x2b_k04_s04.py` |  |
| 0.67 | 4/6 | 5 | 0.3316s | 0.0491s | 2 | 16 | yes | 0.3112s | 0.3576s | `detyped_files/call_method/advanced/proportion_sweep/main_0x1d_k04_s05.py` |  |
| 0.67 | 4/6 | 6 | 1.3682s | 0.0838s | 1 | 8 | yes | 1.3109s | 1.4210s | `detyped_files/call_method/advanced/proportion_sweep/main_0x27_k04_s06.py` |  |
| 0.67 | 4/6 | 7 | 1.3234s | 0.0841s | 1 | 8 | yes | 1.2699s | 1.3782s | `detyped_files/call_method/advanced/proportion_sweep/main_0x33_k04_s07.py` |  |
| 0.67 | 4/6 | 8 | 0.3208s | 0.0111s | 1 | 8 | yes | 0.3134s | 0.3278s | `detyped_files/call_method/advanced/proportion_sweep/main_0x2d_k04_s08.py` |  |
| 0.67 | 4/6 | 9 | 1.3600s | 0.0575s | 1 | 8 | yes | 1.3194s | 1.3930s | `detyped_files/call_method/advanced/proportion_sweep/main_0x36_k04_s09.py` |  |
| 0.67 | 4/6 | 10 | 1.3848s | 0.0952s | 1 | 8 | yes | 1.3255s | 1.4495s | `detyped_files/call_method/advanced/proportion_sweep/main_0xf_k04_s10.py` |  |
| 0.83 | 5/6 | 1 | 0.3162s | 0.0306s | 1 | 8 | yes | 0.2946s | 0.3347s | `detyped_files/call_method/advanced/proportion_sweep/main_0x3d_k05_s01.py` |  |
| 0.83 | 5/6 | 2 | 1.2617s | 0.1318s | 1 | 8 | yes | 1.1860s | 1.3533s | `detyped_files/call_method/advanced/proportion_sweep/main_0x3b_k05_s02.py` |  |
| 0.83 | 5/6 | 3 | 1.3741s | 0.1092s | 1 | 8 | yes | 1.3050s | 1.4445s | `detyped_files/call_method/advanced/proportion_sweep/main_0x1f_k05_s03.py` |  |
| 0.83 | 5/6 | 4 | 1.4077s | 0.0516s | 1 | 8 | yes | 1.3730s | 1.4396s | `detyped_files/call_method/advanced/proportion_sweep/main_0x3e_k05_s04.py` |  |
| 0.83 | 5/6 | 5 | 1.4021s | 0.0800s | 1 | 8 | yes | 1.3518s | 1.4540s | `detyped_files/call_method/advanced/proportion_sweep/main_0x2f_k05_s05.py` |  |
| 0.83 | 5/6 | 6 | 1.4001s | 0.1271s | 1 | 8 | yes | 1.3357s | 1.4917s | `detyped_files/call_method/advanced/proportion_sweep/main_0x37_k05_s06.py` |  |
| 1.00 | 6/6 | 1 | 1.4077s | 0.0596s | 1 | 8 | yes | 1.3681s | 1.4446s | `detyped_files/call_method/advanced/proportion_sweep/main_0x3f_k06_s01.py` |  |

## call_method/shallow

- Detypable targets: `6`
- Total runs: `44`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1156s | 0.1156s | 0.1156s | 1.0 | yes | ok |
| 0.17 | 1/6 | 6 | 0.3224s | 0.1119s | 1.2748s | 1.3 | yes | ok |
| 0.33 | 2/6 | 10 | 0.4651s | 0.1100s | 1.2428s | 1.2 | yes | ok |
| 0.50 | 3/6 | 10 | 0.8262s | 0.1126s | 1.3462s | 1.1 | yes | ok |
| 0.67 | 4/6 | 10 | 0.9453s | 0.1189s | 1.3436s | 1.1 | yes | ok |
| 0.83 | 5/6 | 6 | 1.1052s | 0.1920s | 1.3180s | 1.0 | yes | ok |
| 1.00 | 6/6 | 1 | 1.3070s | 1.3070s | 1.3070s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1156s | 0.0162s | 1 | 8 | yes | 0.1063s | 0.1268s | `detyped_files/call_method/shallow/proportion_sweep/main_0x0_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 0.1912s | 0.0189s | 1 | 8 | yes | 0.1778s | 0.2023s | `detyped_files/call_method/shallow/proportion_sweep/main_0x4_k01_s01.py` |  |
| 0.17 | 1/6 | 2 | 1.2748s | 0.1345s | 1 | 8 | yes | 1.1956s | 1.3686s | `detyped_files/call_method/shallow/proportion_sweep/main_0x2_k01_s02.py` |  |
| 0.17 | 1/6 | 3 | 0.1119s | 0.0057s | 1 | 8 | yes | 0.1088s | 0.1158s | `detyped_files/call_method/shallow/proportion_sweep/main_0x20_k01_s03.py` |  |
| 0.17 | 1/6 | 4 | 0.1163s | 0.0149s | 2 | 16 | yes | 0.1108s | 0.1242s | `detyped_files/call_method/shallow/proportion_sweep/main_0x8_k01_s04.py` |  |
| 0.17 | 1/6 | 5 | 0.1238s | 0.0173s | 2 | 16 | yes | 0.1164s | 0.1327s | `detyped_files/call_method/shallow/proportion_sweep/main_0x10_k01_s05.py` |  |
| 0.17 | 1/6 | 6 | 0.1161s | 0.0124s | 1 | 8 | yes | 0.1089s | 0.1248s | `detyped_files/call_method/shallow/proportion_sweep/main_0x1_k01_s06.py` |  |
| 0.33 | 2/6 | 1 | 0.1100s | 0.0120s | 1 | 8 | yes | 0.1017s | 0.1171s | `detyped_files/call_method/shallow/proportion_sweep/main_0x30_k02_s01.py` |  |
| 0.33 | 2/6 | 2 | 0.1827s | 0.0110s | 1 | 8 | yes | 0.1748s | 0.1888s | `detyped_files/call_method/shallow/proportion_sweep/main_0x24_k02_s02.py` |  |
| 0.33 | 2/6 | 3 | 0.1958s | 0.0093s | 1 | 8 | yes | 0.1900s | 0.2021s | `detyped_files/call_method/shallow/proportion_sweep/main_0x5_k02_s03.py` |  |
| 0.33 | 2/6 | 4 | 0.1218s | 0.0270s | 3 | 24 | yes | 0.1129s | 0.1338s | `detyped_files/call_method/shallow/proportion_sweep/main_0x28_k02_s04.py` |  |
| 0.33 | 2/6 | 5 | 0.1103s | 0.0050s | 1 | 8 | yes | 0.1079s | 0.1139s | `detyped_files/call_method/shallow/proportion_sweep/main_0x21_k02_s05.py` |  |
| 0.33 | 2/6 | 6 | 1.2241s | 0.0635s | 1 | 8 | yes | 1.1840s | 1.2674s | `detyped_files/call_method/shallow/proportion_sweep/main_0x3_k02_s06.py` |  |
| 0.33 | 2/6 | 7 | 1.2428s | 0.1022s | 1 | 8 | yes | 1.1775s | 1.3111s | `detyped_files/call_method/shallow/proportion_sweep/main_0x22_k02_s07.py` |  |
| 0.33 | 2/6 | 8 | 1.2284s | 0.0720s | 1 | 8 | yes | 1.1767s | 1.2696s | `detyped_files/call_method/shallow/proportion_sweep/main_0x12_k02_s08.py` |  |
| 0.33 | 2/6 | 9 | 0.1159s | 0.0110s | 1 | 8 | yes | 0.1097s | 0.1237s | `detyped_files/call_method/shallow/proportion_sweep/main_0x9_k02_s09.py` |  |
| 0.33 | 2/6 | 10 | 0.1188s | 0.0082s | 1 | 8 | yes | 0.1137s | 0.1242s | `detyped_files/call_method/shallow/proportion_sweep/main_0x11_k02_s10.py` |  |
| 0.50 | 3/6 | 1 | 1.3462s | 0.0947s | 1 | 8 | yes | 1.2811s | 1.4060s | `detyped_files/call_method/shallow/proportion_sweep/main_0x26_k03_s01.py` |  |
| 0.50 | 3/6 | 2 | 1.2217s | 0.0755s | 1 | 8 | yes | 1.1712s | 1.2688s | `detyped_files/call_method/shallow/proportion_sweep/main_0x23_k03_s02.py` |  |
| 0.50 | 3/6 | 3 | 0.1912s | 0.0147s | 1 | 8 | yes | 0.1811s | 0.2004s | `detyped_files/call_method/shallow/proportion_sweep/main_0x2c_k03_s03.py` |  |
| 0.50 | 3/6 | 4 | 0.1126s | 0.0077s | 1 | 8 | yes | 0.1072s | 0.1173s | `detyped_files/call_method/shallow/proportion_sweep/main_0x19_k03_s04.py` |  |
| 0.50 | 3/6 | 5 | 0.1245s | 0.0151s | 2 | 16 | yes | 0.1178s | 0.1323s | `detyped_files/call_method/shallow/proportion_sweep/main_0x38_k03_s05.py` |  |
| 0.50 | 3/6 | 6 | 1.2645s | 0.0373s | 1 | 8 | yes | 1.2427s | 1.2902s | `detyped_files/call_method/shallow/proportion_sweep/main_0x1a_k03_s06.py` |  |
| 0.50 | 3/6 | 7 | 1.2527s | 0.1267s | 1 | 8 | yes | 1.1725s | 1.3338s | `detyped_files/call_method/shallow/proportion_sweep/main_0x2a_k03_s07.py` |  |
| 0.50 | 3/6 | 8 | 1.3260s | 0.1056s | 1 | 8 | yes | 1.2690s | 1.4036s | `detyped_files/call_method/shallow/proportion_sweep/main_0x7_k03_s08.py` |  |
| 0.50 | 3/6 | 9 | 0.1875s | 0.0094s | 1 | 8 | yes | 0.1810s | 0.1927s | `detyped_files/call_method/shallow/proportion_sweep/main_0x1c_k03_s09.py` |  |
| 0.50 | 3/6 | 10 | 1.2350s | 0.0524s | 1 | 8 | yes | 1.2008s | 1.2689s | `detyped_files/call_method/shallow/proportion_sweep/main_0x32_k03_s10.py` |  |
| 0.67 | 4/6 | 1 | 1.2639s | 0.0725s | 1 | 8 | yes | 1.2212s | 1.3155s | `detyped_files/call_method/shallow/proportion_sweep/main_0x1b_k04_s01.py` |  |
| 0.67 | 4/6 | 2 | 0.1941s | 0.0151s | 1 | 8 | yes | 0.1857s | 0.2049s | `detyped_files/call_method/shallow/proportion_sweep/main_0x2d_k04_s02.py` |  |
| 0.67 | 4/6 | 3 | 1.2277s | 0.0398s | 1 | 8 | yes | 1.1987s | 1.2494s | `detyped_files/call_method/shallow/proportion_sweep/main_0x2b_k04_s03.py` |  |
| 0.67 | 4/6 | 4 | 1.2387s | 0.0680s | 1 | 8 | yes | 1.1948s | 1.2828s | `detyped_files/call_method/shallow/proportion_sweep/main_0x17_k04_s04.py` |  |
| 0.67 | 4/6 | 5 | 0.1948s | 0.0179s | 1 | 8 | yes | 0.1830s | 0.2062s | `detyped_files/call_method/shallow/proportion_sweep/main_0x35_k04_s05.py` |  |
| 0.67 | 4/6 | 6 | 1.2722s | 0.0867s | 1 | 8 | yes | 1.2190s | 1.3303s | `detyped_files/call_method/shallow/proportion_sweep/main_0x3a_k04_s06.py` |  |
| 0.67 | 4/6 | 7 | 1.3124s | 0.1419s | 1 | 8 | yes | 1.2236s | 1.4068s | `detyped_files/call_method/shallow/proportion_sweep/main_0x1e_k04_s07.py` |  |
| 0.67 | 4/6 | 8 | 0.1189s | 0.0136s | 2 | 16 | yes | 0.1136s | 0.1264s | `detyped_files/call_method/shallow/proportion_sweep/main_0x39_k04_s08.py` |  |
| 0.67 | 4/6 | 9 | 1.2862s | 0.0764s | 1 | 8 | yes | 1.2337s | 1.3335s | `detyped_files/call_method/shallow/proportion_sweep/main_0x27_k04_s09.py` |  |
| 0.67 | 4/6 | 10 | 1.3436s | 0.1322s | 1 | 8 | yes | 1.2603s | 1.4286s | `detyped_files/call_method/shallow/proportion_sweep/main_0xf_k04_s10.py` |  |
| 0.83 | 5/6 | 1 | 1.2619s | 0.0511s | 1 | 8 | yes | 1.2263s | 1.2924s | `detyped_files/call_method/shallow/proportion_sweep/main_0x2f_k05_s01.py` |  |
| 0.83 | 5/6 | 2 | 1.3180s | 0.1156s | 1 | 8 | yes | 1.2478s | 1.3962s | `detyped_files/call_method/shallow/proportion_sweep/main_0x37_k05_s02.py` |  |
| 0.83 | 5/6 | 3 | 1.2888s | 0.0308s | 1 | 8 | yes | 1.2681s | 1.3077s | `detyped_files/call_method/shallow/proportion_sweep/main_0x1f_k05_s03.py` |  |
| 0.83 | 5/6 | 4 | 0.1920s | 0.0232s | 1 | 8 | yes | 0.1769s | 0.2083s | `detyped_files/call_method/shallow/proportion_sweep/main_0x3d_k05_s04.py` |  |
| 0.83 | 5/6 | 5 | 1.3064s | 0.0718s | 1 | 8 | yes | 1.2610s | 1.3527s | `detyped_files/call_method/shallow/proportion_sweep/main_0x3e_k05_s05.py` |  |
| 0.83 | 5/6 | 6 | 1.2645s | 0.0899s | 1 | 8 | yes | 1.2090s | 1.3263s | `detyped_files/call_method/shallow/proportion_sweep/main_0x3b_k05_s06.py` |  |
| 1.00 | 6/6 | 1 | 1.3070s | 0.0551s | 1 | 8 | yes | 1.2740s | 1.3449s | `detyped_files/call_method/shallow/proportion_sweep/main_0x3f_k06_s01.py` |  |

## call_method/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.1209s | 0.1209s | 0.1209s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.1209s | 0.0160s | 1 | 8 | yes | 0.1113s | 0.1316s | `static-python-perf/Benchmark/call_method/untyped/main.py` |  |

## call_method_slots/advanced

- Detypable targets: `6`
- Total runs: `44`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1106s | 0.1106s | 0.1106s | 1.0 | yes | ok |
| 0.17 | 1/6 | 6 | 0.3390s | 0.1132s | 1.2349s | 1.2 | yes | ok |
| 0.33 | 2/6 | 10 | 0.6381s | 0.1290s | 1.3782s | 1.4 | yes | ok |
| 0.50 | 3/6 | 10 | 0.7886s | 0.1571s | 1.4571s | 1.0 | yes | ok |
| 0.67 | 4/6 | 10 | 1.0534s | 0.3093s | 1.4245s | 1.1 | yes | ok |
| 0.83 | 5/6 | 6 | 1.2082s | 0.3412s | 1.4294s | 1.0 | yes | ok |
| 1.00 | 6/6 | 1 | 1.4040s | 1.4040s | 1.4040s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1106s | 0.0132s | 1 | 8 | yes | 0.1025s | 0.1195s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x0_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 0.2794s | 0.0239s | 1 | 8 | yes | 0.2629s | 0.2935s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x4_k01_s01.py` |  |
| 0.17 | 1/6 | 2 | 0.1364s | 0.0137s | 1 | 8 | yes | 0.1299s | 0.1462s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x8_k01_s02.py` |  |
| 0.17 | 1/6 | 3 | 1.2349s | 0.0987s | 1 | 8 | yes | 1.1737s | 1.3007s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x2_k01_s03.py` |  |
| 0.17 | 1/6 | 4 | 0.1401s | 0.0242s | 2 | 16 | yes | 0.1305s | 0.1532s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x10_k01_s04.py` |  |
| 0.17 | 1/6 | 5 | 0.1300s | 0.0111s | 1 | 8 | yes | 0.1248s | 0.1381s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x20_k01_s05.py` |  |
| 0.17 | 1/6 | 6 | 0.1132s | 0.0114s | 1 | 8 | yes | 0.1065s | 0.1211s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x1_k01_s06.py` |  |
| 0.33 | 2/6 | 1 | 0.2897s | 0.0175s | 1 | 8 | yes | 0.2783s | 0.3013s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x5_k02_s01.py` |  |
| 0.33 | 2/6 | 2 | 1.3782s | 0.0936s | 1 | 8 | yes | 1.3161s | 1.4356s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x6_k02_s02.py` |  |
| 0.33 | 2/6 | 3 | 0.1290s | 0.0133s | 1 | 8 | yes | 0.1194s | 0.1374s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x9_k02_s03.py` |  |
| 0.33 | 2/6 | 4 | 0.1419s | 0.0285s | 3 | 24 | yes | 0.1329s | 0.1543s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x11_k02_s04.py` |  |
| 0.33 | 2/6 | 5 | 1.2125s | 0.0758s | 1 | 8 | yes | 1.1622s | 1.2595s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x3_k02_s05.py` |  |
| 0.33 | 2/6 | 6 | 0.1710s | 0.0274s | 2 | 16 | yes | 0.1589s | 0.1845s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x30_k02_s06.py` |  |
| 0.33 | 2/6 | 7 | 0.1532s | 0.0231s | 2 | 16 | yes | 0.1432s | 0.1647s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x28_k02_s07.py` |  |
| 0.33 | 2/6 | 8 | 1.2451s | 0.0433s | 1 | 8 | yes | 1.2166s | 1.2728s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x12_k02_s08.py` |  |
| 0.33 | 2/6 | 9 | 1.3601s | 0.1390s | 1 | 8 | yes | 1.2720s | 1.4476s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0xa_k02_s09.py` |  |
| 0.33 | 2/6 | 10 | 0.3008s | 0.0055s | 1 | 8 | yes | 0.2973s | 0.3045s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x14_k02_s10.py` |  |
| 0.50 | 3/6 | 1 | 1.3649s | 0.0799s | 1 | 8 | yes | 1.3144s | 1.4167s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0xe_k03_s01.py` |  |
| 0.50 | 3/6 | 2 | 1.2783s | 0.0489s | 1 | 8 | yes | 1.2471s | 1.3110s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x23_k03_s02.py` |  |
| 0.50 | 3/6 | 3 | 1.2988s | 0.0767s | 1 | 8 | yes | 1.2470s | 1.3436s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x32_k03_s03.py` |  |
| 0.50 | 3/6 | 4 | 0.1610s | 0.0183s | 1 | 8 | yes | 0.1502s | 0.1735s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x29_k03_s04.py` |  |
| 0.50 | 3/6 | 5 | 0.3351s | 0.0388s | 1 | 8 | yes | 0.3190s | 0.3632s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x1c_k03_s05.py` |  |
| 0.50 | 3/6 | 6 | 1.4571s | 0.0904s | 1 | 8 | yes | 1.4029s | 1.5166s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x26_k03_s06.py` |  |
| 0.50 | 3/6 | 7 | 0.2900s | 0.0123s | 1 | 8 | yes | 0.2812s | 0.2969s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x15_k03_s07.py` |  |
| 0.50 | 3/6 | 8 | 0.1571s | 0.0102s | 1 | 8 | yes | 0.1515s | 0.1644s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x31_k03_s08.py` |  |
| 0.50 | 3/6 | 9 | 1.2329s | 0.0854s | 1 | 8 | yes | 1.1802s | 1.2910s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0xb_k03_s09.py` |  |
| 0.50 | 3/6 | 10 | 0.3105s | 0.0299s | 1 | 8 | yes | 0.2930s | 0.3315s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x2c_k03_s10.py` |  |
| 0.67 | 4/6 | 1 | 0.3306s | 0.0515s | 2 | 16 | yes | 0.3103s | 0.3577s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x1d_k04_s01.py` |  |
| 0.67 | 4/6 | 2 | 0.3421s | 0.0067s | 1 | 8 | yes | 0.3384s | 0.3468s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x3c_k04_s02.py` |  |
| 0.67 | 4/6 | 3 | 1.2733s | 0.0507s | 1 | 8 | yes | 1.2376s | 1.3030s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x3a_k04_s03.py` |  |
| 0.67 | 4/6 | 4 | 0.3093s | 0.0235s | 1 | 8 | yes | 0.2943s | 0.3245s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x35_k04_s04.py` |  |
| 0.67 | 4/6 | 5 | 1.4000s | 0.0878s | 1 | 8 | yes | 1.3509s | 1.4617s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x36_k04_s05.py` |  |
| 0.67 | 4/6 | 6 | 1.2500s | 0.0484s | 1 | 8 | yes | 1.2172s | 1.2789s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x2b_k04_s06.py` |  |
| 0.67 | 4/6 | 7 | 1.4051s | 0.1012s | 1 | 8 | yes | 1.3422s | 1.4685s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x27_k04_s07.py` |  |
| 0.67 | 4/6 | 8 | 1.4040s | 0.1246s | 1 | 8 | yes | 1.3330s | 1.4910s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0xf_k04_s08.py` |  |
| 0.67 | 4/6 | 9 | 1.4245s | 0.1193s | 1 | 8 | yes | 1.3462s | 1.4988s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x2e_k04_s09.py` |  |
| 0.67 | 4/6 | 10 | 1.3946s | 0.1589s | 1 | 8 | yes | 1.3087s | 1.5119s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x1e_k04_s10.py` |  |
| 0.83 | 5/6 | 1 | 1.4051s | 0.0793s | 1 | 8 | yes | 1.3573s | 1.4583s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x37_k05_s01.py` |  |
| 0.83 | 5/6 | 2 | 1.2707s | 0.0655s | 1 | 8 | yes | 1.2299s | 1.3142s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x3b_k05_s02.py` |  |
| 0.83 | 5/6 | 3 | 1.3878s | 0.0332s | 1 | 8 | yes | 1.3661s | 1.4089s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x1f_k05_s03.py` |  |
| 0.83 | 5/6 | 4 | 1.4153s | 0.0804s | 1 | 8 | yes | 1.3635s | 1.4683s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x3e_k05_s04.py` |  |
| 0.83 | 5/6 | 5 | 1.4294s | 0.1081s | 1 | 8 | yes | 1.3632s | 1.5020s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x2f_k05_s05.py` |  |
| 0.83 | 5/6 | 6 | 0.3412s | 0.0411s | 1 | 8 | yes | 0.3126s | 0.3662s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x3d_k05_s06.py` |  |
| 1.00 | 6/6 | 1 | 1.4040s | 0.1040s | 1 | 8 | yes | 1.3490s | 1.4810s | `detyped_files/call_method_slots/advanced/proportion_sweep/main_0x3f_k06_s01.py` |  |

## call_method_slots/shallow

- Detypable targets: `6`
- Total runs: `44`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1134s | 0.1134s | 0.1134s | 1.0 | yes | ok |
| 0.17 | 1/6 | 6 | 0.3229s | 0.1117s | 1.2801s | 1.2 | yes | ok |
| 0.33 | 2/6 | 10 | 0.4769s | 0.1101s | 1.2570s | 1.3 | yes | ok |
| 0.50 | 3/6 | 10 | 0.4904s | 0.1094s | 1.2957s | 1.1 | yes | ok |
| 0.67 | 4/6 | 10 | 0.9620s | 0.1900s | 1.3424s | 1.1 | yes | ok |
| 0.83 | 5/6 | 6 | 1.1190s | 0.1898s | 1.3463s | 1.0 | yes | ok |
| 1.00 | 6/6 | 1 | 1.2916s | 1.2916s | 1.2916s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.1134s | 0.0084s | 1 | 8 | yes | 0.1085s | 0.1191s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x0_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 0.1244s | 0.0214s | 2 | 16 | yes | 0.1150s | 0.1353s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x1_k01_s01.py` |  |
| 0.17 | 1/6 | 2 | 0.1117s | 0.0130s | 1 | 8 | yes | 0.1027s | 0.1191s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x8_k01_s02.py` |  |
| 0.17 | 1/6 | 3 | 0.1128s | 0.0117s | 1 | 8 | yes | 0.1076s | 0.1215s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x20_k01_s03.py` |  |
| 0.17 | 1/6 | 4 | 0.1157s | 0.0089s | 1 | 8 | yes | 0.1108s | 0.1219s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x10_k01_s04.py` |  |
| 0.17 | 1/6 | 5 | 1.2801s | 0.1116s | 1 | 8 | yes | 1.2067s | 1.3509s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x2_k01_s05.py` |  |
| 0.17 | 1/6 | 6 | 0.1926s | 0.0196s | 1 | 8 | yes | 0.1844s | 0.2068s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x4_k01_s06.py` |  |
| 0.33 | 2/6 | 1 | 0.1865s | 0.0058s | 1 | 8 | yes | 0.1831s | 0.1903s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x24_k02_s01.py` |  |
| 0.33 | 2/6 | 2 | 0.1101s | 0.0156s | 1 | 8 | yes | 0.1003s | 0.1205s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x9_k02_s02.py` |  |
| 0.33 | 2/6 | 3 | 0.1222s | 0.0135s | 1 | 8 | yes | 0.1141s | 0.1315s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x30_k02_s03.py` |  |
| 0.33 | 2/6 | 4 | 0.1250s | 0.0184s | 2 | 16 | yes | 0.1170s | 0.1343s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x18_k02_s04.py` |  |
| 0.33 | 2/6 | 5 | 0.1899s | 0.0114s | 1 | 8 | yes | 0.1832s | 0.1980s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0xc_k02_s05.py` |  |
| 0.33 | 2/6 | 6 | 1.2070s | 0.0542s | 1 | 8 | yes | 1.1685s | 1.2388s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0xa_k02_s06.py` |  |
| 0.33 | 2/6 | 7 | 1.2551s | 0.0932s | 1 | 8 | yes | 1.1940s | 1.3187s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x12_k02_s07.py` |  |
| 0.33 | 2/6 | 8 | 0.1163s | 0.0178s | 3 | 24 | yes | 0.1108s | 0.1243s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x21_k02_s08.py` |  |
| 0.33 | 2/6 | 9 | 1.2570s | 0.1191s | 1 | 8 | yes | 1.1891s | 1.3451s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x3_k02_s09.py` |  |
| 0.33 | 2/6 | 10 | 0.1997s | 0.0229s | 1 | 8 | yes | 0.1854s | 0.2147s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x14_k02_s10.py` |  |
| 0.50 | 3/6 | 1 | 0.1167s | 0.0095s | 1 | 8 | yes | 0.1122s | 0.1236s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x19_k03_s01.py` |  |
| 0.50 | 3/6 | 2 | 1.2671s | 0.0990s | 1 | 8 | yes | 1.2046s | 1.3336s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x13_k03_s02.py` |  |
| 0.50 | 3/6 | 3 | 1.2957s | 0.1005s | 1 | 8 | yes | 1.2400s | 1.3660s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x1a_k03_s03.py` |  |
| 0.50 | 3/6 | 4 | 0.2015s | 0.0147s | 1 | 8 | yes | 0.1929s | 0.2117s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x34_k03_s04.py` |  |
| 0.50 | 3/6 | 5 | 1.2166s | 0.0619s | 1 | 8 | yes | 1.1781s | 1.2582s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x26_k03_s05.py` |  |
| 0.50 | 3/6 | 6 | 0.1094s | 0.0094s | 1 | 8 | yes | 0.1027s | 0.1146s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x31_k03_s06.py` |  |
| 0.50 | 3/6 | 7 | 0.1928s | 0.0123s | 1 | 8 | yes | 0.1855s | 0.2013s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0xd_k03_s07.py` |  |
| 0.50 | 3/6 | 8 | 0.2008s | 0.0305s | 2 | 16 | yes | 0.1884s | 0.2162s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x15_k03_s08.py` |  |
| 0.50 | 3/6 | 9 | 0.1123s | 0.0074s | 1 | 8 | yes | 0.1082s | 0.1174s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x29_k03_s09.py` |  |
| 0.50 | 3/6 | 10 | 0.1915s | 0.0161s | 1 | 8 | yes | 0.1812s | 0.2024s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x1c_k03_s10.py` |  |
| 0.67 | 4/6 | 1 | 1.2997s | 0.1222s | 1 | 8 | yes | 1.2258s | 1.3820s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x33_k04_s01.py` |  |
| 0.67 | 4/6 | 2 | 0.1900s | 0.0061s | 1 | 8 | yes | 0.1861s | 0.1940s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x2d_k04_s02.py` |  |
| 0.67 | 4/6 | 3 | 1.2979s | 0.0382s | 1 | 8 | yes | 1.2731s | 1.3222s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x1e_k04_s03.py` |  |
| 0.67 | 4/6 | 4 | 1.3144s | 0.0725s | 1 | 8 | yes | 1.2651s | 1.3584s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x2e_k04_s04.py` |  |
| 0.67 | 4/6 | 5 | 1.2673s | 0.0603s | 1 | 8 | yes | 1.2272s | 1.3056s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x2b_k04_s05.py` |  |
| 0.67 | 4/6 | 6 | 1.2382s | 0.0950s | 1 | 8 | yes | 1.1839s | 1.3030s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x17_k04_s06.py` |  |
| 0.67 | 4/6 | 7 | 1.2848s | 0.0829s | 1 | 8 | yes | 1.2327s | 1.3397s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x36_k04_s07.py` |  |
| 0.67 | 4/6 | 8 | 1.3424s | 0.1512s | 2 | 16 | yes | 1.2810s | 1.4221s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x27_k04_s08.py` |  |
| 0.67 | 4/6 | 9 | 0.1945s | 0.0078s | 1 | 8 | yes | 0.1899s | 0.1997s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x35_k04_s09.py` |  |
| 0.67 | 4/6 | 10 | 0.1905s | 0.0200s | 1 | 8 | yes | 0.1783s | 0.2037s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x3c_k04_s10.py` |  |
| 0.83 | 5/6 | 1 | 0.1898s | 0.0180s | 1 | 8 | yes | 0.1769s | 0.2002s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x3d_k05_s01.py` |  |
| 0.83 | 5/6 | 2 | 1.3180s | 0.0974s | 1 | 8 | yes | 1.2664s | 1.3896s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x37_k05_s02.py` |  |
| 0.83 | 5/6 | 3 | 1.2964s | 0.0492s | 1 | 8 | yes | 1.2646s | 1.3272s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x3b_k05_s03.py` |  |
| 0.83 | 5/6 | 4 | 1.2349s | 0.0496s | 1 | 8 | yes | 1.2016s | 1.2657s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x2f_k05_s04.py` |  |
| 0.83 | 5/6 | 5 | 1.3463s | 0.0839s | 1 | 8 | yes | 1.2939s | 1.4025s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x1f_k05_s05.py` |  |
| 0.83 | 5/6 | 6 | 1.3288s | 0.0737s | 1 | 8 | yes | 1.2841s | 1.3784s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x3e_k05_s06.py` |  |
| 1.00 | 6/6 | 1 | 1.2916s | 0.0840s | 1 | 8 | yes | 1.2343s | 1.3425s | `detyped_files/call_method_slots/shallow/proportion_sweep/main_0x3f_k06_s01.py` |  |

## call_method_slots/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.1250s | 0.1250s | 0.1250s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.1250s | 0.0151s | 1 | 8 | yes | 0.1153s | 0.1346s | `static-python-perf/Benchmark/call_method_slots/untyped/main.py` |  |

## call_simple/advanced

- Detypable targets: `6`
- Total runs: `44`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.0727s | 0.0727s | 0.0727s | 3.0 | yes | ok |
| 0.17 | 1/6 | 6 | 0.0981s | 0.0746s | 0.1627s | 1.2 | yes | ok |
| 0.33 | 2/6 | 10 | 0.1235s | 0.0905s | 0.1893s | 1.5 | yes | ok |
| 0.50 | 3/6 | 10 | 0.1515s | 0.0896s | 0.2094s | 1.3 | yes | ok |
| 0.67 | 4/6 | 10 | 0.1831s | 0.1164s | 0.2114s | 1.0 | yes | ok |
| 0.83 | 5/6 | 6 | 0.1971s | 0.1325s | 0.2220s | 1.3 | yes | ok |
| 1.00 | 6/6 | 1 | 0.2152s | 0.2152s | 0.2152s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.0727s | 0.0143s | 3 | 24 | yes | 0.0672s | 0.0785s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x0_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 0.1627s | 0.0184s | 1 | 8 | yes | 0.1499s | 0.1737s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x4_k01_s01.py` |  |
| 0.17 | 1/6 | 2 | 0.0756s | 0.0091s | 1 | 8 | yes | 0.0701s | 0.0819s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x1_k01_s02.py` |  |
| 0.17 | 1/6 | 3 | 0.0746s | 0.0102s | 1 | 8 | yes | 0.0686s | 0.0817s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x2_k01_s03.py` |  |
| 0.17 | 1/6 | 4 | 0.0903s | 0.0122s | 1 | 8 | yes | 0.0821s | 0.0979s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x8_k01_s04.py` |  |
| 0.17 | 1/6 | 5 | 0.0947s | 0.0130s | 2 | 16 | yes | 0.0891s | 0.1012s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x20_k01_s05.py` |  |
| 0.17 | 1/6 | 6 | 0.0907s | 0.0129s | 1 | 8 | yes | 0.0823s | 0.0992s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x10_k01_s06.py` |  |
| 0.33 | 2/6 | 1 | 0.1711s | 0.0194s | 1 | 8 | yes | 0.1601s | 0.1851s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x5_k02_s01.py` |  |
| 0.33 | 2/6 | 2 | 0.0905s | 0.0069s | 1 | 8 | yes | 0.0864s | 0.0953s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x22_k02_s02.py` |  |
| 0.33 | 2/6 | 3 | 0.1192s | 0.0131s | 1 | 8 | yes | 0.1112s | 0.1281s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x30_k02_s03.py` |  |
| 0.33 | 2/6 | 4 | 0.1777s | 0.0062s | 1 | 8 | yes | 0.1738s | 0.1817s | `detyped_files/call_simple/advanced/proportion_sweep/main_0xc_k02_s04.py` |  |
| 0.33 | 2/6 | 5 | 0.1893s | 0.0288s | 2 | 16 | yes | 0.1769s | 0.2040s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x24_k02_s05.py` |  |
| 0.33 | 2/6 | 6 | 0.0937s | 0.0181s | 3 | 24 | yes | 0.0878s | 0.1019s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x21_k02_s06.py` |  |
| 0.33 | 2/6 | 7 | 0.1090s | 0.0060s | 1 | 8 | yes | 0.1059s | 0.1134s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x28_k02_s07.py` |  |
| 0.33 | 2/6 | 8 | 0.0982s | 0.0182s | 2 | 16 | yes | 0.0905s | 0.1077s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x9_k02_s08.py` |  |
| 0.33 | 2/6 | 9 | 0.0914s | 0.0056s | 1 | 8 | yes | 0.0884s | 0.0954s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x11_k02_s09.py` |  |
| 0.33 | 2/6 | 10 | 0.0947s | 0.0110s | 2 | 16 | yes | 0.0902s | 0.1004s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x12_k02_s10.py` |  |
| 0.50 | 3/6 | 1 | 0.1351s | 0.0126s | 1 | 8 | yes | 0.1277s | 0.1441s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x38_k03_s01.py` |  |
| 0.50 | 3/6 | 2 | 0.1896s | 0.0120s | 1 | 8 | yes | 0.1821s | 0.1975s | `detyped_files/call_simple/advanced/proportion_sweep/main_0xd_k03_s02.py` |  |
| 0.50 | 3/6 | 3 | 0.2049s | 0.0108s | 1 | 8 | yes | 0.1984s | 0.2124s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x1c_k03_s03.py` |  |
| 0.50 | 3/6 | 4 | 0.1743s | 0.0250s | 1 | 8 | yes | 0.1598s | 0.1909s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x15_k03_s04.py` |  |
| 0.50 | 3/6 | 5 | 0.0896s | 0.0025s | 1 | 8 | yes | 0.0881s | 0.0912s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x13_k03_s05.py` |  |
| 0.50 | 3/6 | 6 | 0.1652s | 0.0137s | 1 | 8 | yes | 0.1572s | 0.1745s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x7_k03_s06.py` |  |
| 0.50 | 3/6 | 7 | 0.2094s | 0.0327s | 2 | 16 | yes | 0.1964s | 0.2269s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x34_k03_s07.py` |  |
| 0.50 | 3/6 | 8 | 0.1194s | 0.0207s | 3 | 24 | yes | 0.1133s | 0.1286s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x31_k03_s08.py` |  |
| 0.50 | 3/6 | 9 | 0.1131s | 0.0063s | 1 | 8 | yes | 0.1094s | 0.1175s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x1a_k03_s09.py` |  |
| 0.50 | 3/6 | 10 | 0.1141s | 0.0112s | 1 | 8 | yes | 0.1083s | 0.1223s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x2a_k03_s10.py` |  |
| 0.67 | 4/6 | 1 | 0.2057s | 0.0123s | 1 | 8 | yes | 0.1986s | 0.2147s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x2e_k04_s01.py` |  |
| 0.67 | 4/6 | 2 | 0.1865s | 0.0132s | 1 | 8 | yes | 0.1781s | 0.1950s | `detyped_files/call_simple/advanced/proportion_sweep/main_0xf_k04_s02.py` |  |
| 0.67 | 4/6 | 3 | 0.2011s | 0.0093s | 1 | 8 | yes | 0.1953s | 0.2073s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x1e_k04_s03.py` |  |
| 0.67 | 4/6 | 4 | 0.1811s | 0.0082s | 1 | 8 | yes | 0.1773s | 0.1872s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x27_k04_s04.py` |  |
| 0.67 | 4/6 | 5 | 0.1986s | 0.0152s | 1 | 8 | yes | 0.1886s | 0.2082s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x2d_k04_s05.py` |  |
| 0.67 | 4/6 | 6 | 0.1164s | 0.0146s | 1 | 8 | yes | 0.1087s | 0.1270s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x33_k04_s06.py` |  |
| 0.67 | 4/6 | 7 | 0.2069s | 0.0165s | 1 | 8 | yes | 0.1970s | 0.2178s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x1d_k04_s07.py` |  |
| 0.67 | 4/6 | 8 | 0.1883s | 0.0181s | 1 | 8 | yes | 0.1789s | 0.2018s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x17_k04_s08.py` |  |
| 0.67 | 4/6 | 9 | 0.1345s | 0.0126s | 1 | 8 | yes | 0.1265s | 0.1426s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x39_k04_s09.py` |  |
| 0.67 | 4/6 | 10 | 0.2114s | 0.0165s | 1 | 8 | yes | 0.2013s | 0.2225s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x35_k04_s10.py` |  |
| 0.83 | 5/6 | 1 | 0.2060s | 0.0153s | 1 | 8 | yes | 0.1978s | 0.2169s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x2f_k05_s01.py` |  |
| 0.83 | 5/6 | 2 | 0.2059s | 0.0243s | 2 | 16 | yes | 0.1968s | 0.2192s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x37_k05_s02.py` |  |
| 0.83 | 5/6 | 3 | 0.2220s | 0.0260s | 2 | 16 | yes | 0.2109s | 0.2354s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x3d_k05_s03.py` |  |
| 0.83 | 5/6 | 4 | 0.1957s | 0.0120s | 1 | 8 | yes | 0.1891s | 0.2046s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x1f_k05_s04.py` |  |
| 0.83 | 5/6 | 5 | 0.2207s | 0.0192s | 1 | 8 | yes | 0.2081s | 0.2332s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x3e_k05_s05.py` |  |
| 0.83 | 5/6 | 6 | 0.1325s | 0.0028s | 1 | 8 | yes | 0.1308s | 0.1344s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x3b_k05_s06.py` |  |
| 1.00 | 6/6 | 1 | 0.2152s | 0.0087s | 1 | 8 | yes | 0.2098s | 0.2209s | `detyped_files/call_simple/advanced/proportion_sweep/main_0x3f_k06_s01.py` |  |

## call_simple/shallow

- Detypable targets: `6`
- Total runs: `44`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.0708s | 0.0708s | 0.0708s | 1.0 | yes | ok |
| 0.17 | 1/6 | 6 | 0.0710s | 0.0673s | 0.0747s | 1.3 | yes | ok |
| 0.33 | 2/6 | 10 | 0.0700s | 0.0664s | 0.0758s | 1.3 | yes | ok |
| 0.50 | 3/6 | 10 | 0.0711s | 0.0687s | 0.0743s | 1.3 | yes | ok |
| 0.67 | 4/6 | 10 | 0.0735s | 0.0681s | 0.0765s | 1.3 | yes | ok |
| 0.83 | 5/6 | 6 | 0.0708s | 0.0680s | 0.0755s | 1.5 | yes | ok |
| 1.00 | 6/6 | 1 | 0.0730s | 0.0730s | 0.0730s | 2.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.0708s | 0.0090s | 1 | 8 | yes | 0.0664s | 0.0774s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x0_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 0.0747s | 0.0101s | 1 | 8 | yes | 0.0686s | 0.0814s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x10_k01_s01.py` |  |
| 0.17 | 1/6 | 2 | 0.0709s | 0.0067s | 1 | 8 | yes | 0.0669s | 0.0755s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x4_k01_s02.py` |  |
| 0.17 | 1/6 | 3 | 0.0736s | 0.0135s | 2 | 16 | yes | 0.0682s | 0.0809s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x2_k01_s03.py` |  |
| 0.17 | 1/6 | 4 | 0.0673s | 0.0069s | 1 | 8 | yes | 0.0631s | 0.0719s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x20_k01_s04.py` |  |
| 0.17 | 1/6 | 5 | 0.0675s | 0.0026s | 1 | 8 | yes | 0.0660s | 0.0694s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x1_k01_s05.py` |  |
| 0.17 | 1/6 | 6 | 0.0717s | 0.0108s | 2 | 16 | yes | 0.0675s | 0.0773s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x8_k01_s06.py` |  |
| 0.33 | 2/6 | 1 | 0.0714s | 0.0069s | 1 | 8 | yes | 0.0674s | 0.0761s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x3_k02_s01.py` |  |
| 0.33 | 2/6 | 2 | 0.0758s | 0.0117s | 2 | 16 | yes | 0.0707s | 0.0815s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x14_k02_s02.py` |  |
| 0.33 | 2/6 | 3 | 0.0741s | 0.0104s | 2 | 16 | yes | 0.0694s | 0.0792s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x22_k02_s03.py` |  |
| 0.33 | 2/6 | 4 | 0.0673s | 0.0025s | 1 | 8 | yes | 0.0660s | 0.0691s | `detyped_files/call_simple/shallow/proportion_sweep/main_0xa_k02_s04.py` |  |
| 0.33 | 2/6 | 5 | 0.0681s | 0.0017s | 1 | 8 | yes | 0.0670s | 0.0691s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x5_k02_s05.py` |  |
| 0.33 | 2/6 | 6 | 0.0664s | 0.0017s | 1 | 8 | yes | 0.0656s | 0.0677s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x28_k02_s06.py` |  |
| 0.33 | 2/6 | 7 | 0.0666s | 0.0015s | 1 | 8 | yes | 0.0657s | 0.0676s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x12_k02_s07.py` |  |
| 0.33 | 2/6 | 8 | 0.0688s | 0.0083s | 1 | 8 | yes | 0.0639s | 0.0747s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x11_k02_s08.py` |  |
| 0.33 | 2/6 | 9 | 0.0711s | 0.0116s | 2 | 16 | yes | 0.0666s | 0.0773s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x21_k02_s09.py` |  |
| 0.33 | 2/6 | 10 | 0.0699s | 0.0071s | 1 | 8 | yes | 0.0660s | 0.0749s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x18_k02_s10.py` |  |
| 0.50 | 3/6 | 1 | 0.0739s | 0.0096s | 1 | 8 | yes | 0.0685s | 0.0805s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x16_k03_s01.py` |  |
| 0.50 | 3/6 | 2 | 0.0726s | 0.0072s | 1 | 8 | yes | 0.0689s | 0.0778s | `detyped_files/call_simple/shallow/proportion_sweep/main_0xd_k03_s02.py` |  |
| 0.50 | 3/6 | 3 | 0.0705s | 0.0040s | 1 | 8 | yes | 0.0680s | 0.0731s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x31_k03_s03.py` |  |
| 0.50 | 3/6 | 4 | 0.0693s | 0.0067s | 1 | 8 | yes | 0.0658s | 0.0740s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x19_k03_s04.py` |  |
| 0.50 | 3/6 | 5 | 0.0704s | 0.0054s | 1 | 8 | yes | 0.0673s | 0.0742s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x1c_k03_s05.py` |  |
| 0.50 | 3/6 | 6 | 0.0694s | 0.0061s | 1 | 8 | yes | 0.0660s | 0.0739s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x29_k03_s06.py` |  |
| 0.50 | 3/6 | 7 | 0.0721s | 0.0101s | 2 | 16 | yes | 0.0679s | 0.0773s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x25_k03_s07.py` |  |
| 0.50 | 3/6 | 8 | 0.0743s | 0.0137s | 3 | 24 | yes | 0.0696s | 0.0800s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x38_k03_s08.py` |  |
| 0.50 | 3/6 | 9 | 0.0700s | 0.0065s | 1 | 8 | yes | 0.0661s | 0.0744s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x15_k03_s09.py` |  |
| 0.50 | 3/6 | 10 | 0.0687s | 0.0076s | 1 | 8 | yes | 0.0647s | 0.0742s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x1a_k03_s10.py` |  |
| 0.67 | 4/6 | 1 | 0.0756s | 0.0082s | 1 | 8 | yes | 0.0706s | 0.0809s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x1d_k04_s01.py` |  |
| 0.67 | 4/6 | 2 | 0.0736s | 0.0107s | 1 | 8 | yes | 0.0677s | 0.0809s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x2e_k04_s02.py` |  |
| 0.67 | 4/6 | 3 | 0.0758s | 0.0137s | 2 | 16 | yes | 0.0697s | 0.0825s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x27_k04_s03.py` |  |
| 0.67 | 4/6 | 4 | 0.0681s | 0.0049s | 1 | 8 | yes | 0.0655s | 0.0715s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x3a_k04_s04.py` |  |
| 0.67 | 4/6 | 5 | 0.0762s | 0.0139s | 3 | 24 | yes | 0.0713s | 0.0822s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x33_k04_s05.py` |  |
| 0.67 | 4/6 | 6 | 0.0741s | 0.0088s | 1 | 8 | yes | 0.0686s | 0.0800s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x2d_k04_s06.py` |  |
| 0.67 | 4/6 | 7 | 0.0708s | 0.0091s | 1 | 8 | yes | 0.0661s | 0.0772s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x35_k04_s07.py` |  |
| 0.67 | 4/6 | 8 | 0.0742s | 0.0092s | 1 | 8 | yes | 0.0687s | 0.0808s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x3c_k04_s08.py` |  |
| 0.67 | 4/6 | 9 | 0.0702s | 0.0074s | 1 | 8 | yes | 0.0659s | 0.0752s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x1b_k04_s09.py` |  |
| 0.67 | 4/6 | 10 | 0.0765s | 0.0106s | 1 | 8 | yes | 0.0700s | 0.0835s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x1e_k04_s10.py` |  |
| 0.83 | 5/6 | 1 | 0.0695s | 0.0064s | 1 | 8 | yes | 0.0662s | 0.0742s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x3d_k05_s01.py` |  |
| 0.83 | 5/6 | 2 | 0.0699s | 0.0093s | 2 | 16 | yes | 0.0664s | 0.0749s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x3e_k05_s02.py` |  |
| 0.83 | 5/6 | 3 | 0.0711s | 0.0071s | 1 | 8 | yes | 0.0669s | 0.0762s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x37_k05_s03.py` |  |
| 0.83 | 5/6 | 4 | 0.0680s | 0.0027s | 1 | 8 | yes | 0.0663s | 0.0699s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x2f_k05_s04.py` |  |
| 0.83 | 5/6 | 5 | 0.0710s | 0.0096s | 1 | 8 | yes | 0.0660s | 0.0780s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x1f_k05_s05.py` |  |
| 0.83 | 5/6 | 6 | 0.0755s | 0.0137s | 3 | 24 | yes | 0.0706s | 0.0814s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x3b_k05_s06.py` |  |
| 1.00 | 6/6 | 1 | 0.0730s | 0.0106s | 2 | 16 | yes | 0.0683s | 0.0783s | `detyped_files/call_simple/shallow/proportion_sweep/main_0x3f_k06_s01.py` |  |

## call_simple/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.0800s | 0.0800s | 0.0800s | 3.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.0800s | 0.0175s | 3 | 24 | yes | 0.0734s | 0.0871s | `static-python-perf/Benchmark/call_simple/untyped/main.py` |  |

## chaos/advanced

- Detypable targets: `5`
- Total runs: `32`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/5 | 1 | 0.3243s | 0.3243s | 0.3243s | 1.0 | yes | ok |
| 0.20 | 1/5 | 5 | 0.3445s | 0.3183s | 0.4347s | 1.0 | yes | ok |
| 0.40 | 2/5 | 10 | 0.3773s | 0.2970s | 0.4683s | 1.1 | yes | ok |
| 0.60 | 3/5 | 10 | 0.4019s | 0.3242s | 0.4626s | 1.0 | yes | ok |
| 0.80 | 4/5 | 5 | 0.4154s | 0.3358s | 0.4569s | 1.0 | yes | ok |
| 1.00 | 5/5 | 1 | 0.4246s | 0.4246s | 0.4246s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/5 | 1 | 0.3243s | 0.0113s | 1 | 8 | yes | 0.3180s | 0.3324s | `detyped_files/chaos/advanced/proportion_sweep/main_0x0_k00_s01.py` |  |
| 0.20 | 1/5 | 1 | 0.3183s | 0.0397s | 1 | 8 | yes | 0.2965s | 0.3471s | `detyped_files/chaos/advanced/proportion_sweep/main_0x8_k01_s01.py` |  |
| 0.20 | 1/5 | 2 | 0.3209s | 0.0124s | 1 | 8 | yes | 0.3130s | 0.3289s | `detyped_files/chaos/advanced/proportion_sweep/main_0x4_k01_s02.py` |  |
| 0.20 | 1/5 | 3 | 0.3265s | 0.0423s | 1 | 8 | yes | 0.2975s | 0.3543s | `detyped_files/chaos/advanced/proportion_sweep/main_0x10_k01_s03.py` |  |
| 0.20 | 1/5 | 4 | 0.3219s | 0.0220s | 1 | 8 | yes | 0.3068s | 0.3350s | `detyped_files/chaos/advanced/proportion_sweep/main_0x1_k01_s04.py` |  |
| 0.20 | 1/5 | 5 | 0.4347s | 0.0341s | 1 | 8 | yes | 0.4100s | 0.4497s | `detyped_files/chaos/advanced/proportion_sweep/main_0x2_k01_s05.py` |  |
| 0.40 | 2/5 | 1 | 0.4683s | 0.0375s | 1 | 8 | yes | 0.4429s | 0.4917s | `detyped_files/chaos/advanced/proportion_sweep/main_0x3_k02_s01.py` |  |
| 0.40 | 2/5 | 2 | 0.2970s | 0.0298s | 1 | 8 | yes | 0.2768s | 0.3155s | `detyped_files/chaos/advanced/proportion_sweep/main_0x18_k02_s02.py` |  |
| 0.40 | 2/5 | 3 | 0.4550s | 0.0564s | 1 | 8 | yes | 0.4177s | 0.4911s | `detyped_files/chaos/advanced/proportion_sweep/main_0xa_k02_s03.py` |  |
| 0.40 | 2/5 | 4 | 0.3197s | 0.0304s | 1 | 8 | yes | 0.2987s | 0.3381s | `detyped_files/chaos/advanced/proportion_sweep/main_0x14_k02_s04.py` |  |
| 0.40 | 2/5 | 5 | 0.4511s | 0.0331s | 1 | 8 | yes | 0.4328s | 0.4745s | `detyped_files/chaos/advanced/proportion_sweep/main_0x6_k02_s05.py` |  |
| 0.40 | 2/5 | 6 | 0.3293s | 0.0353s | 1 | 8 | yes | 0.3050s | 0.3498s | `detyped_files/chaos/advanced/proportion_sweep/main_0x9_k02_s06.py` |  |
| 0.40 | 2/5 | 7 | 0.4650s | 0.0281s | 1 | 8 | yes | 0.4476s | 0.4837s | `detyped_files/chaos/advanced/proportion_sweep/main_0x12_k02_s07.py` |  |
| 0.40 | 2/5 | 8 | 0.3113s | 0.0404s | 1 | 8 | yes | 0.2843s | 0.3358s | `detyped_files/chaos/advanced/proportion_sweep/main_0xc_k02_s08.py` |  |
| 0.40 | 2/5 | 9 | 0.3380s | 0.0372s | 2 | 16 | yes | 0.3209s | 0.3562s | `detyped_files/chaos/advanced/proportion_sweep/main_0x11_k02_s09.py` |  |
| 0.40 | 2/5 | 10 | 0.3379s | 0.0229s | 1 | 8 | yes | 0.3220s | 0.3514s | `detyped_files/chaos/advanced/proportion_sweep/main_0x5_k02_s10.py` |  |
| 0.60 | 3/5 | 1 | 0.4409s | 0.0332s | 1 | 8 | yes | 0.4164s | 0.4577s | `detyped_files/chaos/advanced/proportion_sweep/main_0x16_k03_s01.py` |  |
| 0.60 | 3/5 | 2 | 0.4626s | 0.0117s | 1 | 8 | yes | 0.4548s | 0.4702s | `detyped_files/chaos/advanced/proportion_sweep/main_0x7_k03_s02.py` |  |
| 0.60 | 3/5 | 3 | 0.3444s | 0.0224s | 1 | 8 | yes | 0.3297s | 0.3592s | `detyped_files/chaos/advanced/proportion_sweep/main_0xd_k03_s03.py` |  |
| 0.60 | 3/5 | 4 | 0.4298s | 0.0538s | 1 | 8 | yes | 0.3948s | 0.4622s | `detyped_files/chaos/advanced/proportion_sweep/main_0x1a_k03_s04.py` |  |
| 0.60 | 3/5 | 5 | 0.3353s | 0.0464s | 1 | 8 | yes | 0.3078s | 0.3678s | `detyped_files/chaos/advanced/proportion_sweep/main_0x1c_k03_s05.py` |  |
| 0.60 | 3/5 | 6 | 0.4610s | 0.0627s | 1 | 8 | yes | 0.4219s | 0.5014s | `detyped_files/chaos/advanced/proportion_sweep/main_0xb_k03_s06.py` |  |
| 0.60 | 3/5 | 7 | 0.4496s | 0.0210s | 1 | 8 | yes | 0.4375s | 0.4643s | `detyped_files/chaos/advanced/proportion_sweep/main_0xe_k03_s07.py` |  |
| 0.60 | 3/5 | 8 | 0.4403s | 0.0406s | 1 | 8 | yes | 0.4115s | 0.4639s | `detyped_files/chaos/advanced/proportion_sweep/main_0x13_k03_s08.py` |  |
| 0.60 | 3/5 | 9 | 0.3242s | 0.0311s | 1 | 8 | yes | 0.3048s | 0.3450s | `detyped_files/chaos/advanced/proportion_sweep/main_0x15_k03_s09.py` |  |
| 0.60 | 3/5 | 10 | 0.3308s | 0.0230s | 1 | 8 | yes | 0.3139s | 0.3414s | `detyped_files/chaos/advanced/proportion_sweep/main_0x19_k03_s10.py` |  |
| 0.80 | 4/5 | 1 | 0.3358s | 0.0050s | 1 | 8 | yes | 0.3326s | 0.3390s | `detyped_files/chaos/advanced/proportion_sweep/main_0x1d_k04_s01.py` |  |
| 0.80 | 4/5 | 2 | 0.4437s | 0.0307s | 1 | 8 | yes | 0.4237s | 0.4630s | `detyped_files/chaos/advanced/proportion_sweep/main_0x1b_k04_s02.py` |  |
| 0.80 | 4/5 | 3 | 0.4282s | 0.0355s | 1 | 8 | yes | 0.4036s | 0.4484s | `detyped_files/chaos/advanced/proportion_sweep/main_0x17_k04_s03.py` |  |
| 0.80 | 4/5 | 4 | 0.4569s | 0.0158s | 1 | 8 | yes | 0.4475s | 0.4676s | `detyped_files/chaos/advanced/proportion_sweep/main_0xf_k04_s04.py` |  |
| 0.80 | 4/5 | 5 | 0.4123s | 0.0398s | 1 | 8 | yes | 0.3862s | 0.4385s | `detyped_files/chaos/advanced/proportion_sweep/main_0x1e_k04_s05.py` |  |
| 1.00 | 5/5 | 1 | 0.4246s | 0.0528s | 1 | 8 | yes | 0.3910s | 0.4588s | `detyped_files/chaos/advanced/proportion_sweep/main_0x1f_k05_s01.py` |  |

## chaos/shallow

- Detypable targets: `5`
- Total runs: `32`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/5 | 1 | 0.3187s | 0.3187s | 0.3187s | 1.0 | yes | ok |
| 0.20 | 1/5 | 5 | 0.3574s | 0.3187s | 0.4288s | 1.0 | yes | ok |
| 0.40 | 2/5 | 10 | 0.3954s | 0.3087s | 0.4860s | 1.1 | yes | ok |
| 0.60 | 3/5 | 10 | 0.4326s | 0.3407s | 0.4979s | 1.0 | yes | ok |
| 0.80 | 4/5 | 5 | 0.4735s | 0.4090s | 0.5164s | 1.0 | yes | ok |
| 1.00 | 5/5 | 1 | 0.4939s | 0.4939s | 0.4939s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/5 | 1 | 0.3187s | 0.0332s | 1 | 8 | yes | 0.2981s | 0.3414s | `detyped_files/chaos/shallow/proportion_sweep/main_0x0_k00_s01.py` |  |
| 0.20 | 1/5 | 1 | 0.3236s | 0.0257s | 1 | 8 | yes | 0.3054s | 0.3382s | `detyped_files/chaos/shallow/proportion_sweep/main_0x1_k01_s01.py` |  |
| 0.20 | 1/5 | 2 | 0.3830s | 0.0198s | 1 | 8 | yes | 0.3707s | 0.3961s | `detyped_files/chaos/shallow/proportion_sweep/main_0x10_k01_s02.py` |  |
| 0.20 | 1/5 | 3 | 0.4288s | 0.0451s | 1 | 8 | yes | 0.3989s | 0.4568s | `detyped_files/chaos/shallow/proportion_sweep/main_0x2_k01_s03.py` |  |
| 0.20 | 1/5 | 4 | 0.3187s | 0.0301s | 1 | 8 | yes | 0.2991s | 0.3379s | `detyped_files/chaos/shallow/proportion_sweep/main_0x8_k01_s04.py` |  |
| 0.20 | 1/5 | 5 | 0.3329s | 0.0135s | 1 | 8 | yes | 0.3249s | 0.3421s | `detyped_files/chaos/shallow/proportion_sweep/main_0x4_k01_s05.py` |  |
| 0.40 | 2/5 | 1 | 0.3913s | 0.0460s | 2 | 16 | yes | 0.3720s | 0.4157s | `detyped_files/chaos/shallow/proportion_sweep/main_0x11_k02_s01.py` |  |
| 0.40 | 2/5 | 2 | 0.3732s | 0.0280s | 1 | 8 | yes | 0.3552s | 0.3911s | `detyped_files/chaos/shallow/proportion_sweep/main_0x18_k02_s02.py` |  |
| 0.40 | 2/5 | 3 | 0.3087s | 0.0341s | 1 | 8 | yes | 0.2868s | 0.3307s | `detyped_files/chaos/shallow/proportion_sweep/main_0xc_k02_s03.py` |  |
| 0.40 | 2/5 | 4 | 0.3404s | 0.0302s | 1 | 8 | yes | 0.3188s | 0.3587s | `detyped_files/chaos/shallow/proportion_sweep/main_0x5_k02_s04.py` |  |
| 0.40 | 2/5 | 5 | 0.4622s | 0.0652s | 1 | 8 | yes | 0.4182s | 0.5076s | `detyped_files/chaos/shallow/proportion_sweep/main_0x3_k02_s05.py` |  |
| 0.40 | 2/5 | 6 | 0.4315s | 0.0280s | 1 | 8 | yes | 0.4106s | 0.4480s | `detyped_files/chaos/shallow/proportion_sweep/main_0xa_k02_s06.py` |  |
| 0.40 | 2/5 | 7 | 0.3312s | 0.0376s | 1 | 8 | yes | 0.3067s | 0.3577s | `detyped_files/chaos/shallow/proportion_sweep/main_0x9_k02_s07.py` |  |
| 0.40 | 2/5 | 8 | 0.3876s | 0.0118s | 1 | 8 | yes | 0.3803s | 0.3956s | `detyped_files/chaos/shallow/proportion_sweep/main_0x14_k02_s08.py` |  |
| 0.40 | 2/5 | 9 | 0.4860s | 0.0431s | 1 | 8 | yes | 0.4577s | 0.5128s | `detyped_files/chaos/shallow/proportion_sweep/main_0x12_k02_s09.py` |  |
| 0.40 | 2/5 | 10 | 0.4415s | 0.0235s | 1 | 8 | yes | 0.4261s | 0.4560s | `detyped_files/chaos/shallow/proportion_sweep/main_0x6_k02_s10.py` |  |
| 0.60 | 3/5 | 1 | 0.4578s | 0.0434s | 1 | 8 | yes | 0.4321s | 0.4888s | `detyped_files/chaos/shallow/proportion_sweep/main_0x7_k03_s01.py` |  |
| 0.60 | 3/5 | 2 | 0.4978s | 0.0327s | 1 | 8 | yes | 0.4763s | 0.5190s | `detyped_files/chaos/shallow/proportion_sweep/main_0x1a_k03_s02.py` |  |
| 0.60 | 3/5 | 3 | 0.3829s | 0.0131s | 1 | 8 | yes | 0.3754s | 0.3924s | `detyped_files/chaos/shallow/proportion_sweep/main_0x1c_k03_s03.py` |  |
| 0.60 | 3/5 | 4 | 0.3882s | 0.0249s | 1 | 8 | yes | 0.3711s | 0.4035s | `detyped_files/chaos/shallow/proportion_sweep/main_0x19_k03_s04.py` |  |
| 0.60 | 3/5 | 5 | 0.4979s | 0.0540s | 1 | 8 | yes | 0.4607s | 0.5303s | `detyped_files/chaos/shallow/proportion_sweep/main_0x16_k03_s05.py` |  |
| 0.60 | 3/5 | 6 | 0.4437s | 0.0449s | 1 | 8 | yes | 0.4138s | 0.4721s | `detyped_files/chaos/shallow/proportion_sweep/main_0xb_k03_s06.py` |  |
| 0.60 | 3/5 | 7 | 0.4877s | 0.0292s | 1 | 8 | yes | 0.4670s | 0.5040s | `detyped_files/chaos/shallow/proportion_sweep/main_0x13_k03_s07.py` |  |
| 0.60 | 3/5 | 8 | 0.4331s | 0.0355s | 1 | 8 | yes | 0.4093s | 0.4545s | `detyped_files/chaos/shallow/proportion_sweep/main_0xe_k03_s08.py` |  |
| 0.60 | 3/5 | 9 | 0.3961s | 0.0318s | 1 | 8 | yes | 0.3747s | 0.4150s | `detyped_files/chaos/shallow/proportion_sweep/main_0x15_k03_s09.py` |  |
| 0.60 | 3/5 | 10 | 0.3407s | 0.0105s | 1 | 8 | yes | 0.3339s | 0.3473s | `detyped_files/chaos/shallow/proportion_sweep/main_0xd_k03_s10.py` |  |
| 0.80 | 4/5 | 1 | 0.4090s | 0.0424s | 1 | 8 | yes | 0.3802s | 0.4357s | `detyped_files/chaos/shallow/proportion_sweep/main_0x1d_k04_s01.py` |  |
| 0.80 | 4/5 | 2 | 0.5007s | 0.0370s | 1 | 8 | yes | 0.4747s | 0.5233s | `detyped_files/chaos/shallow/proportion_sweep/main_0x17_k04_s02.py` |  |
| 0.80 | 4/5 | 3 | 0.5164s | 0.0302s | 1 | 8 | yes | 0.4998s | 0.5383s | `detyped_files/chaos/shallow/proportion_sweep/main_0x1e_k04_s03.py` |  |
| 0.80 | 4/5 | 4 | 0.4770s | 0.0420s | 1 | 8 | yes | 0.4486s | 0.5026s | `detyped_files/chaos/shallow/proportion_sweep/main_0x1b_k04_s04.py` |  |
| 0.80 | 4/5 | 5 | 0.4643s | 0.0110s | 1 | 8 | yes | 0.4577s | 0.4719s | `detyped_files/chaos/shallow/proportion_sweep/main_0xf_k04_s05.py` |  |
| 1.00 | 5/5 | 1 | 0.4939s | 0.0615s | 1 | 8 | yes | 0.4550s | 0.5329s | `detyped_files/chaos/shallow/proportion_sweep/main_0x1f_k05_s01.py` |  |

## chaos/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.3390s | 0.3390s | 0.3390s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.3390s | 0.0140s | 1 | 8 | yes | 0.3303s | 0.3480s | `static-python-perf/Benchmark/chaos/untyped/main.py` |  |

## deltablue/advanced

- Detypable targets: `34`
- Total runs: `332`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/34 | 1 | 1.4500s | 1.4500s | 1.4500s | 1.0 | yes | ok |
| 0.03 | 1/34 | 10 | 2.0519s | 1.3649s | 6.6604s | 1.0 | yes | ok |
| 0.06 | 2/34 | 10 | 1.9354s | 1.3258s | 6.6576s | 1.0 | yes | ok |
| 0.09 | 3/34 | 10 | 1.4870s | 1.3470s | 1.8730s | 1.0 | yes | ok |
| 0.12 | 4/34 | 10 | 2.5198s | 1.3433s | 7.0802s | 1.0 | yes | ok |
| 0.15 | 5/34 | 10 | 2.6876s | 1.3462s | 7.0045s | 1.0 | yes | ok |
| 0.18 | 6/34 | 10 | 1.6161s | 1.3906s | 1.9544s | 1.0 | yes | ok |
| 0.21 | 7/34 | 10 | 1.7492s | 1.4080s | 2.2615s | 1.0 | yes | ok |
| 0.24 | 8/34 | 10 | 3.3266s | 1.3539s | 7.8454s | 1.0 | yes | ok |
| 0.26 | 9/34 | 10 | 2.8375s | 1.4974s | 6.7743s | 1.0 | yes | ok |
| 0.29 | 10/34 | 10 | 4.3157s | 1.5357s | 9.0545s | 1.0 | yes | ok |
| 0.32 | 11/34 | 10 | 3.6841s | 1.4233s | 9.5898s | 1.0 | yes | ok |
| 0.35 | 12/34 | 10 | 4.4941s | 1.6126s | 9.5279s | 1.0 | yes | ok |
| 0.38 | 13/34 | 10 | 3.7128s | 1.4311s | 8.7645s | 1.0 | yes | ok |
| 0.41 | 14/34 | 10 | 4.8834s | 1.5379s | 8.9721s | 1.0 | yes | ok |
| 0.44 | 15/34 | 10 | 5.0521s | 1.6797s | 8.6347s | 1.0 | yes | ok |
| 0.47 | 16/34 | 10 | 3.9428s | 1.5044s | 9.7108s | 1.0 | yes | ok |
| 0.50 | 17/34 | 10 | 3.4630s | 1.5724s | 8.8782s | 1.0 | yes | ok |
| 0.53 | 18/34 | 10 | 6.5327s | 1.4949s | 10.1918s | 1.0 | yes | ok |
| 0.56 | 19/34 | 10 | 3.8937s | 1.9673s | 8.6507s | 1.0 | yes | ok |
| 0.59 | 20/34 | 10 | 6.2802s | 1.7572s | 10.1249s | 1.0 | yes | ok |
| 0.62 | 21/34 | 10 | 6.1459s | 1.6185s | 9.7187s | 1.0 | yes | ok |
| 0.65 | 22/34 | 10 | 7.0445s | 2.2115s | 10.1490s | 1.0 | yes | ok |
| 0.68 | 23/34 | 10 | 7.1302s | 1.7164s | 10.1729s | 1.0 | yes | ok |
| 0.71 | 24/34 | 10 | 7.1693s | 2.1597s | 10.2517s | 1.0 | yes | ok |
| 0.74 | 25/34 | 10 | 7.1859s | 2.2520s | 10.1522s | 1.0 | yes | ok |
| 0.76 | 26/34 | 10 | 6.6378s | 2.5187s | 10.2727s | 1.0 | yes | ok |
| 0.79 | 27/34 | 10 | 6.5959s | 2.2325s | 10.1481s | 1.0 | yes | ok |
| 0.82 | 28/34 | 10 | 8.7731s | 2.1600s | 10.1772s | 1.0 | yes | ok |
| 0.85 | 29/34 | 10 | 8.3014s | 2.3126s | 10.3290s | 1.0 | yes | ok |
| 0.88 | 30/34 | 10 | 9.0504s | 2.7256s | 10.2758s | 1.0 | yes | ok |
| 0.91 | 31/34 | 10 | 9.6353s | 8.5330s | 10.2969s | 1.0 | yes | ok |
| 0.94 | 32/34 | 10 | 10.1827s | 9.8371s | 10.3211s | 1.0 | yes | ok |
| 0.97 | 33/34 | 10 | 10.2211s | 9.7970s | 10.3207s | 1.0 | yes | ok |
| 1.00 | 34/34 | 1 | 10.1930s | 10.1930s | 10.1930s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/34 | 1 | 1.4500s | 0.0762s | 1 | 8 | yes | 1.4040s | 1.5023s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x0_k00_s01.py` |  |
| 0.03 | 1/34 | 1 | 1.8884s | 0.1172s | 1 | 8 | yes | 1.8111s | 1.9656s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x80000_k01_s01.py` |  |
| 0.03 | 1/34 | 2 | 1.3649s | 0.0877s | 1 | 8 | yes | 1.3122s | 1.4249s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x100_k01_s02.py` |  |
| 0.03 | 1/34 | 3 | 1.4205s | 0.0995s | 1 | 8 | yes | 1.3605s | 1.4899s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x40000_k01_s03.py` |  |
| 0.03 | 1/34 | 4 | 1.4928s | 0.0601s | 1 | 8 | yes | 1.4528s | 1.5311s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x8_k01_s04.py` |  |
| 0.03 | 1/34 | 5 | 1.3832s | 0.0716s | 1 | 8 | yes | 1.3408s | 1.4328s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x20000000_k01_s05.py` |  |
| 0.03 | 1/34 | 6 | 1.4211s | 0.0572s | 1 | 8 | yes | 1.3886s | 1.4620s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x20000_k01_s06.py` |  |
| 0.03 | 1/34 | 7 | 1.5217s | 0.0767s | 1 | 8 | yes | 1.4763s | 1.5720s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x10000_k01_s07.py` |  |
| 0.03 | 1/34 | 8 | 1.4492s | 0.1324s | 1 | 8 | yes | 1.3743s | 1.5432s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1_k01_s08.py` |  |
| 0.03 | 1/34 | 9 | 1.9164s | 0.0896s | 1 | 8 | yes | 1.8597s | 1.9762s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x400_k01_s09.py` |  |
| 0.03 | 1/34 | 10 | 6.6604s | 0.1163s | 1 | 8 | yes | 6.5919s | 6.7422s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x100000000_k01_s10.py` |  |
| 0.06 | 2/34 | 1 | 1.5419s | 0.0871s | 1 | 8 | yes | 1.5010s | 1.6058s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x40008_k02_s01.py` |  |
| 0.06 | 2/34 | 2 | 1.5802s | 0.0903s | 1 | 8 | yes | 1.5214s | 1.6400s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x80010000_k02_s02.py` |  |
| 0.06 | 2/34 | 3 | 1.3838s | 0.0783s | 1 | 8 | yes | 1.3380s | 1.4372s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2100_k02_s03.py` |  |
| 0.06 | 2/34 | 4 | 1.3856s | 0.0732s | 1 | 8 | yes | 1.3418s | 1.4356s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x48000000_k02_s04.py` |  |
| 0.06 | 2/34 | 5 | 1.3691s | 0.1116s | 1 | 8 | yes | 1.3014s | 1.4445s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1000100_k02_s05.py` |  |
| 0.06 | 2/34 | 6 | 6.6576s | 0.1136s | 1 | 8 | yes | 6.5793s | 6.7253s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x100000080_k02_s06.py` |  |
| 0.06 | 2/34 | 7 | 1.4177s | 0.0907s | 1 | 8 | yes | 1.3656s | 1.4813s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x140_k02_s07.py` |  |
| 0.06 | 2/34 | 8 | 1.3351s | 0.0651s | 1 | 8 | yes | 1.2918s | 1.3767s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x8000010_k02_s08.py` |  |
| 0.06 | 2/34 | 9 | 1.3258s | 0.0725s | 1 | 8 | yes | 1.2760s | 1.3688s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x800010_k02_s09.py` |  |
| 0.06 | 2/34 | 10 | 1.3570s | 0.0801s | 1 | 8 | yes | 1.3044s | 1.4085s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x801000_k02_s10.py` |  |
| 0.09 | 3/34 | 1 | 1.4680s | 0.0563s | 1 | 8 | yes | 1.4333s | 1.5064s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x800088_k03_s01.py` |  |
| 0.09 | 3/34 | 2 | 1.3715s | 0.0738s | 1 | 8 | yes | 1.3231s | 1.4195s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x4008002_k03_s02.py` |  |
| 0.09 | 3/34 | 3 | 1.8730s | 0.1091s | 1 | 8 | yes | 1.8043s | 1.9464s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1000c00_k03_s03.py` |  |
| 0.09 | 3/34 | 4 | 1.4969s | 0.0932s | 1 | 8 | yes | 1.4335s | 1.5542s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x809_k03_s04.py` |  |
| 0.09 | 3/34 | 5 | 1.4127s | 0.0583s | 1 | 8 | yes | 1.3722s | 1.4482s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x40220000_k03_s05.py` |  |
| 0.09 | 3/34 | 6 | 1.4258s | 0.0972s | 1 | 8 | yes | 1.3647s | 1.4916s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x40a000_k03_s06.py` |  |
| 0.09 | 3/34 | 7 | 1.4991s | 0.0499s | 1 | 8 | yes | 1.4647s | 1.5291s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x80008200_k03_s07.py` |  |
| 0.09 | 3/34 | 8 | 1.4953s | 0.0978s | 1 | 8 | yes | 1.4296s | 1.5564s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x800000c0_k03_s08.py` |  |
| 0.09 | 3/34 | 9 | 1.4807s | 0.1143s | 1 | 8 | yes | 1.4114s | 1.5576s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x110200_k03_s09.py` |  |
| 0.09 | 3/34 | 10 | 1.3470s | 0.0707s | 1 | 8 | yes | 1.3021s | 1.3926s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x6000800_k03_s10.py` |  |
| 0.12 | 4/34 | 1 | 6.6812s | 0.1051s | 1 | 8 | yes | 6.6165s | 6.7520s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x100800840_k04_s01.py` |  |
| 0.12 | 4/34 | 2 | 1.3745s | 0.0443s | 1 | 8 | yes | 1.3479s | 1.4055s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x20000150_k04_s02.py` |  |
| 0.12 | 4/34 | 3 | 1.4055s | 0.1493s | 1 | 8 | yes | 1.3293s | 1.5159s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3900000_k04_s03.py` |  |
| 0.12 | 4/34 | 4 | 7.0802s | 0.1104s | 1 | 8 | yes | 7.0093s | 7.1506s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x100880001_k04_s04.py` |  |
| 0.12 | 4/34 | 5 | 1.3433s | 0.0338s | 1 | 8 | yes | 1.3196s | 1.3627s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2008804_k04_s05.py` |  |
| 0.12 | 4/34 | 6 | 1.4387s | 0.1010s | 1 | 8 | yes | 1.3755s | 1.5076s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x4021080_k04_s06.py` |  |
| 0.12 | 4/34 | 7 | 1.4698s | 0.0778s | 1 | 8 | yes | 1.4216s | 1.5229s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1801002_k04_s07.py` |  |
| 0.12 | 4/34 | 8 | 1.4589s | 0.0513s | 1 | 8 | yes | 1.4250s | 1.4902s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x44a00_k04_s08.py` |  |
| 0.12 | 4/34 | 9 | 1.5504s | 0.1247s | 1 | 8 | yes | 1.4763s | 1.6399s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x420a_k04_s09.py` |  |
| 0.12 | 4/34 | 10 | 1.3952s | 0.0619s | 1 | 8 | yes | 1.3521s | 1.4329s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x209000080_k04_s10.py` |  |
| 0.15 | 5/34 | 1 | 1.3524s | 0.0653s | 1 | 8 | yes | 1.3102s | 1.3934s | `detyped_files/deltablue/advanced/proportion_sweep/main_0xc100003_k05_s01.py` |  |
| 0.15 | 5/34 | 2 | 1.6272s | 0.1236s | 1 | 8 | yes | 1.5502s | 1.7085s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x90810200_k05_s02.py` |  |
| 0.15 | 5/34 | 3 | 1.9917s | 0.0789s | 1 | 8 | yes | 1.9507s | 2.0492s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x204002408_k05_s03.py` |  |
| 0.15 | 5/34 | 4 | 1.8709s | 0.0372s | 1 | 8 | yes | 1.8467s | 1.8939s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x8020424_k05_s04.py` |  |
| 0.15 | 5/34 | 5 | 7.0045s | 0.0673s | 1 | 8 | yes | 6.9624s | 7.0506s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x120880002_k05_s05.py` |  |
| 0.15 | 5/34 | 6 | 1.4182s | 0.1064s | 1 | 8 | yes | 1.3531s | 1.4908s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x9000a1_k05_s06.py` |  |
| 0.15 | 5/34 | 7 | 6.6626s | 0.1396s | 1 | 8 | yes | 6.5810s | 6.7607s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x102020300_k05_s07.py` |  |
| 0.15 | 5/34 | 8 | 1.3462s | 0.0620s | 1 | 8 | yes | 1.3057s | 1.3851s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x50800220_k05_s08.py` |  |
| 0.15 | 5/34 | 9 | 1.8825s | 0.0866s | 1 | 8 | yes | 1.8285s | 1.9435s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x81112_k05_s09.py` |  |
| 0.15 | 5/34 | 10 | 1.7196s | 0.1115s | 1 | 8 | yes | 1.6529s | 1.7958s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x8801000a_k05_s10.py` |  |
| 0.18 | 6/34 | 1 | 1.5429s | 0.0884s | 1 | 8 | yes | 1.4938s | 1.6051s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1600010c_k06_s01.py` |  |
| 0.18 | 6/34 | 2 | 1.9544s | 0.0568s | 1 | 8 | yes | 1.9167s | 1.9895s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x8044c4_k06_s02.py` |  |
| 0.18 | 6/34 | 3 | 1.6192s | 0.0923s | 1 | 8 | yes | 1.5627s | 1.6817s | `detyped_files/deltablue/advanced/proportion_sweep/main_0xa1040018_k06_s03.py` |  |
| 0.18 | 6/34 | 4 | 1.3906s | 0.0597s | 1 | 8 | yes | 1.3465s | 1.4206s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x16040180_k06_s04.py` |  |
| 0.18 | 6/34 | 5 | 1.4013s | 0.0706s | 1 | 8 | yes | 1.3522s | 1.4428s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x45408100_k06_s05.py` |  |
| 0.18 | 6/34 | 6 | 1.5143s | 0.0841s | 1 | 8 | yes | 1.4635s | 1.5730s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x4a018001_k06_s06.py` |  |
| 0.18 | 6/34 | 7 | 1.5906s | 0.0628s | 1 | 8 | yes | 1.5482s | 1.6295s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x280010b00_k06_s07.py` |  |
| 0.18 | 6/34 | 8 | 1.6380s | 0.0561s | 1 | 8 | yes | 1.6052s | 1.6767s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x841004c_k06_s08.py` |  |
| 0.18 | 6/34 | 9 | 1.5696s | 0.0774s | 1 | 8 | yes | 1.5136s | 1.6141s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x20c041008_k06_s09.py` |  |
| 0.18 | 6/34 | 10 | 1.9404s | 0.0817s | 1 | 8 | yes | 1.8921s | 1.9968s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2004d4000_k06_s10.py` |  |
| 0.21 | 7/34 | 1 | 1.6094s | 0.0488s | 1 | 8 | yes | 1.5810s | 1.6425s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x91109002_k07_s01.py` |  |
| 0.21 | 7/34 | 2 | 2.2615s | 0.1542s | 1 | 8 | yes | 2.1752s | 2.3721s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x24080644_k07_s02.py` |  |
| 0.21 | 7/34 | 3 | 1.5051s | 0.0482s | 1 | 8 | yes | 1.4753s | 1.5372s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x609128_k07_s03.py` |  |
| 0.21 | 7/34 | 4 | 1.4080s | 0.0622s | 1 | 8 | yes | 1.3688s | 1.4468s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x42208282_k07_s04.py` |  |
| 0.21 | 7/34 | 5 | 1.5245s | 0.0959s | 1 | 8 | yes | 1.4635s | 1.5849s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x440280b_k07_s05.py` |  |
| 0.21 | 7/34 | 6 | 1.5347s | 0.0661s | 1 | 8 | yes | 1.4877s | 1.5736s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x610a60_k07_s06.py` |  |
| 0.21 | 7/34 | 7 | 1.9361s | 0.0735s | 1 | 8 | yes | 1.8861s | 1.9778s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x49088028_k07_s07.py` |  |
| 0.21 | 7/34 | 8 | 1.8871s | 0.0995s | 1 | 8 | yes | 1.8232s | 1.9519s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x11840c04_k07_s08.py` |  |
| 0.21 | 7/34 | 9 | 1.9086s | 0.1030s | 1 | 8 | yes | 1.8444s | 1.9775s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x42a0211_k07_s09.py` |  |
| 0.21 | 7/34 | 10 | 1.9170s | 0.0520s | 1 | 8 | yes | 1.8903s | 1.9552s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x48e4100_k07_s10.py` |  |
| 0.24 | 8/34 | 1 | 1.6061s | 0.1462s | 1 | 8 | yes | 1.5222s | 1.7112s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x214a000a8_k08_s01.py` |  |
| 0.24 | 8/34 | 2 | 2.0927s | 0.1583s | 1 | 8 | yes | 2.0083s | 2.2056s | `detyped_files/deltablue/advanced/proportion_sweep/main_0xca100444_k08_s02.py` |  |
| 0.24 | 8/34 | 3 | 1.3539s | 0.0556s | 1 | 8 | yes | 1.3186s | 1.3896s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x214402902_k08_s03.py` |  |
| 0.24 | 8/34 | 4 | 2.1319s | 0.0486s | 1 | 8 | yes | 2.1004s | 2.1627s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2e0290004_k08_s04.py` |  |
| 0.24 | 8/34 | 5 | 1.5240s | 0.0788s | 1 | 8 | yes | 1.4716s | 1.5738s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x218224050_k08_s05.py` |  |
| 0.24 | 8/34 | 6 | 1.5251s | 0.0595s | 1 | 8 | yes | 1.4841s | 1.5615s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x24700098_k08_s06.py` |  |
| 0.24 | 8/34 | 7 | 6.9187s | 0.1159s | 1 | 8 | yes | 6.8500s | 6.9996s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x308204248_k08_s07.py` |  |
| 0.24 | 8/34 | 8 | 6.7931s | 0.0594s | 1 | 8 | yes | 6.7538s | 6.8312s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x100c11884_k08_s08.py` |  |
| 0.24 | 8/34 | 9 | 1.4753s | 0.0961s | 1 | 8 | yes | 1.4160s | 1.5376s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x5200081b_k08_s09.py` |  |
| 0.24 | 8/34 | 10 | 7.8454s | 0.1342s | 1 | 8 | yes | 7.7700s | 7.9382s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x10ba09000_k08_s10.py` |  |
| 0.26 | 9/34 | 1 | 1.5137s | 0.0962s | 1 | 8 | yes | 1.4543s | 1.5777s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x44270890_k09_s01.py` |  |
| 0.26 | 9/34 | 2 | 2.0242s | 0.0752s | 1 | 8 | yes | 1.9744s | 2.0721s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x22d90028_k09_s02.py` |  |
| 0.26 | 9/34 | 3 | 1.9699s | 0.1682s | 1 | 8 | yes | 1.8657s | 2.0836s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x140812e8_k09_s03.py` |  |
| 0.26 | 9/34 | 4 | 2.4492s | 0.0773s | 1 | 8 | yes | 2.3965s | 2.4965s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x200290c8a_k09_s04.py` |  |
| 0.26 | 9/34 | 5 | 1.9015s | 0.1409s | 1 | 8 | yes | 1.8217s | 2.0026s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x260c0069_k09_s05.py` |  |
| 0.26 | 9/34 | 6 | 1.9378s | 0.0688s | 1 | 8 | yes | 1.8920s | 1.9827s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2006e4a0_k09_s06.py` |  |
| 0.26 | 9/34 | 7 | 6.7743s | 0.1233s | 1 | 8 | yes | 6.7014s | 6.8600s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x150227010_k09_s07.py` |  |
| 0.26 | 9/34 | 8 | 1.5963s | 0.1211s | 1 | 8 | yes | 1.5208s | 1.6746s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x91805340_k09_s08.py` |  |
| 0.26 | 9/34 | 9 | 6.7103s | 0.1251s | 1 | 8 | yes | 6.6332s | 6.7951s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x118340214_k09_s09.py` |  |
| 0.26 | 9/34 | 10 | 1.4974s | 0.0640s | 1 | 8 | yes | 1.4590s | 1.5414s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1023f800_k09_s10.py` |  |
| 0.29 | 10/34 | 1 | 8.2922s | 0.0931s | 1 | 8 | yes | 8.2316s | 8.3523s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x10908d064_k10_s01.py` |  |
| 0.29 | 10/34 | 2 | 7.2890s | 0.0770s | 1 | 8 | yes | 7.2409s | 7.3415s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x328052484_k10_s02.py` |  |
| 0.29 | 10/34 | 3 | 1.9322s | 0.0560s | 1 | 8 | yes | 1.8984s | 1.9699s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x401e1268_k10_s03.py` |  |
| 0.29 | 10/34 | 4 | 1.5999s | 0.0898s | 1 | 8 | yes | 1.5440s | 1.6595s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x18419846_k10_s04.py` |  |
| 0.29 | 10/34 | 5 | 2.0259s | 0.1502s | 1 | 8 | yes | 1.9465s | 2.1364s | `detyped_files/deltablue/advanced/proportion_sweep/main_0xa4881161_k10_s05.py` |  |
| 0.29 | 10/34 | 6 | 2.0336s | 0.0454s | 1 | 8 | yes | 2.0064s | 2.0641s | `detyped_files/deltablue/advanced/proportion_sweep/main_0xd490928_k10_s06.py` |  |
| 0.29 | 10/34 | 7 | 9.0545s | 0.0889s | 1 | 8 | yes | 8.9983s | 9.1144s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1881081e1_k10_s07.py` |  |
| 0.29 | 10/34 | 8 | 1.5413s | 0.1164s | 1 | 8 | yes | 1.4668s | 1.6166s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x203372100_k10_s08.py` |  |
| 0.29 | 10/34 | 9 | 1.5357s | 0.0773s | 1 | 8 | yes | 1.4825s | 1.5818s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x23850420c_k10_s09.py` |  |
| 0.29 | 10/34 | 10 | 7.8524s | 0.1412s | 1 | 8 | yes | 7.7672s | 7.9494s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x31402c301_k10_s10.py` |  |
| 0.32 | 11/34 | 1 | 2.4108s | 0.0733s | 1 | 8 | yes | 2.3646s | 2.4597s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x47288618_k11_s01.py` |  |
| 0.32 | 11/34 | 2 | 9.5898s | 0.1740s | 1 | 8 | yes | 9.4806s | 9.7045s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1a288b082_k11_s02.py` |  |
| 0.32 | 11/34 | 3 | 2.0024s | 0.0566s | 1 | 8 | yes | 1.9659s | 2.0397s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x260b0440d_k11_s03.py` |  |
| 0.32 | 11/34 | 4 | 6.7551s | 0.4469s | 1 | 8 | yes | 6.5351s | 7.0765s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x147102a05_k11_s04.py` |  |
| 0.32 | 11/34 | 5 | 2.0136s | 0.0601s | 1 | 8 | yes | 1.9748s | 2.0520s | `detyped_files/deltablue/advanced/proportion_sweep/main_0xd416f00_k11_s05.py` |  |
| 0.32 | 11/34 | 6 | 1.4233s | 0.0728s | 1 | 8 | yes | 1.3741s | 1.4678s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x252843094_k11_s06.py` |  |
| 0.32 | 11/34 | 7 | 1.6373s | 0.0489s | 1 | 8 | yes | 1.6032s | 1.6660s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x8a11cb01_k11_s07.py` |  |
| 0.32 | 11/34 | 8 | 6.7109s | 0.0925s | 1 | 8 | yes | 6.6522s | 6.7702s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x16e460180_k11_s08.py` |  |
| 0.32 | 11/34 | 9 | 2.3755s | 0.1287s | 1 | 8 | yes | 2.2963s | 2.4614s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x18784c06_k11_s09.py` |  |
| 0.32 | 11/34 | 10 | 1.9222s | 0.0672s | 1 | 8 | yes | 1.8773s | 1.9644s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2aa91881_k11_s10.py` |  |
| 0.35 | 12/34 | 1 | 8.0446s | 0.2316s | 1 | 8 | yes | 7.9135s | 8.2121s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x391806941_k12_s01.py` |  |
| 0.35 | 12/34 | 2 | 2.0510s | 0.0599s | 1 | 8 | yes | 2.0089s | 2.0852s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x8edb8800_k12_s02.py` |  |
| 0.35 | 12/34 | 3 | 1.9579s | 0.1005s | 1 | 8 | yes | 1.8911s | 2.0204s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x9598a086_k12_s03.py` |  |
| 0.35 | 12/34 | 4 | 9.5279s | 0.0990s | 1 | 8 | yes | 9.4618s | 9.5920s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x38280b4c2_k12_s04.py` |  |
| 0.35 | 12/34 | 5 | 7.8756s | 0.1538s | 1 | 8 | yes | 7.7907s | 7.9842s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x16226c860_k12_s05.py` |  |
| 0.35 | 12/34 | 6 | 1.8911s | 0.0829s | 1 | 8 | yes | 1.8345s | 1.9408s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x429d0986_k12_s06.py` |  |
| 0.35 | 12/34 | 7 | 2.1735s | 0.0652s | 1 | 8 | yes | 2.1336s | 2.2172s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2c5a40d08_k12_s07.py` |  |
| 0.35 | 12/34 | 8 | 1.9685s | 0.1413s | 1 | 8 | yes | 1.8933s | 2.0701s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x24a5a030a_k12_s08.py` |  |
| 0.35 | 12/34 | 9 | 7.8379s | 0.1303s | 1 | 8 | yes | 7.7557s | 7.9262s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x112368885_k12_s09.py` |  |
| 0.35 | 12/34 | 10 | 1.6126s | 0.0665s | 1 | 8 | yes | 1.5683s | 1.6537s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x37250928_k12_s10.py` |  |
| 0.38 | 13/34 | 1 | 8.7645s | 0.1703s | 1 | 8 | yes | 8.6610s | 8.8800s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x134598cc0_k13_s01.py` |  |
| 0.38 | 13/34 | 2 | 2.4271s | 0.1511s | 1 | 8 | yes | 2.3463s | 2.5372s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2088c4d78_k13_s02.py` |  |
| 0.38 | 13/34 | 3 | 1.6778s | 0.1014s | 1 | 8 | yes | 1.6094s | 1.7396s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x68a700b9_k13_s03.py` |  |
| 0.38 | 13/34 | 4 | 2.3492s | 0.0922s | 1 | 8 | yes | 2.2899s | 2.4087s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x216781413_k13_s04.py` |  |
| 0.38 | 13/34 | 5 | 8.2234s | 0.1119s | 1 | 8 | yes | 8.1556s | 8.2993s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x13c028723_k13_s05.py` |  |
| 0.38 | 13/34 | 6 | 1.8873s | 0.1183s | 1 | 8 | yes | 1.8171s | 1.9695s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x210e7a23_k13_s06.py` |  |
| 0.38 | 13/34 | 7 | 1.4311s | 0.0508s | 1 | 8 | yes | 1.3954s | 1.4621s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x223423896_k13_s07.py` |  |
| 0.38 | 13/34 | 8 | 7.2005s | 0.1154s | 1 | 8 | yes | 7.1232s | 7.2717s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x121ac40ec_k13_s08.py` |  |
| 0.38 | 13/34 | 9 | 1.5566s | 0.0868s | 1 | 8 | yes | 1.5019s | 1.6157s | `detyped_files/deltablue/advanced/proportion_sweep/main_0xd229b0b_k13_s09.py` |  |
| 0.38 | 13/34 | 10 | 1.6102s | 0.0606s | 1 | 8 | yes | 1.5720s | 1.6487s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3013636c_k13_s10.py` |  |
| 0.41 | 14/34 | 1 | 8.9721s | 0.1349s | 1 | 8 | yes | 8.9047s | 9.0694s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x18b1a342c_k14_s01.py` |  |
| 0.41 | 14/34 | 2 | 6.7971s | 0.1058s | 1 | 8 | yes | 6.7286s | 6.8629s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x31a6053c4_k14_s02.py` |  |
| 0.41 | 14/34 | 3 | 8.1459s | 0.1649s | 1 | 8 | yes | 8.0475s | 8.2619s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x395654882_k14_s03.py` |  |
| 0.41 | 14/34 | 4 | 7.3180s | 0.1311s | 1 | 8 | yes | 7.2351s | 7.4033s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x31e614e40_k14_s04.py` |  |
| 0.41 | 14/34 | 5 | 1.5379s | 0.0945s | 1 | 8 | yes | 1.4782s | 1.6006s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x22456f083_k14_s05.py` |  |
| 0.41 | 14/34 | 6 | 1.6546s | 0.0874s | 1 | 8 | yes | 1.5991s | 1.7104s | `detyped_files/deltablue/advanced/proportion_sweep/main_0xe192307c_k14_s06.py` |  |
| 0.41 | 14/34 | 7 | 2.0105s | 0.0196s | 1 | 8 | yes | 1.9971s | 2.0227s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x62a47594_k14_s07.py` |  |
| 0.41 | 14/34 | 8 | 1.9393s | 0.0755s | 1 | 8 | yes | 1.8879s | 1.9859s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x72bb4830_k14_s08.py` |  |
| 0.41 | 14/34 | 9 | 1.9587s | 0.0880s | 1 | 8 | yes | 1.9094s | 2.0208s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x571496a1_k14_s09.py` |  |
| 0.41 | 14/34 | 10 | 8.5001s | 0.0711s | 1 | 8 | yes | 8.4563s | 8.5487s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x384436583_k14_s10.py` |  |
| 0.44 | 15/34 | 1 | 1.6797s | 0.0682s | 1 | 8 | yes | 1.6359s | 1.7230s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2a6a4a998_k15_s01.py` |  |
| 0.44 | 15/34 | 2 | 7.2834s | 0.1435s | 1 | 8 | yes | 7.1982s | 7.3842s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x36139423c_k15_s02.py` |  |
| 0.44 | 15/34 | 3 | 1.6805s | 0.0801s | 1 | 8 | yes | 1.6259s | 1.7283s | `detyped_files/deltablue/advanced/proportion_sweep/main_0xfb05a126_k15_s03.py` |  |
| 0.44 | 15/34 | 4 | 7.9899s | 0.0475s | 1 | 8 | yes | 7.9590s | 8.0209s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3a1123371_k15_s04.py` |  |
| 0.44 | 15/34 | 5 | 2.1655s | 0.0831s | 1 | 8 | yes | 2.1121s | 2.2201s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2e3c0952a_k15_s05.py` |  |
| 0.44 | 15/34 | 6 | 2.1817s | 0.0571s | 1 | 8 | yes | 2.1454s | 2.2195s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x80bf322e_k15_s06.py` |  |
| 0.44 | 15/34 | 7 | 8.6347s | 0.1316s | 1 | 8 | yes | 8.5613s | 8.7294s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1a4a2347c_k15_s07.py` |  |
| 0.44 | 15/34 | 8 | 2.0273s | 0.0766s | 1 | 8 | yes | 1.9807s | 2.0800s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x27e6d620_k15_s08.py` |  |
| 0.44 | 15/34 | 9 | 8.3970s | 0.1568s | 1 | 8 | yes | 8.2918s | 8.4923s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x304e28e3a_k15_s09.py` |  |
| 0.44 | 15/34 | 10 | 8.4813s | 0.1038s | 1 | 8 | yes | 8.4090s | 8.5434s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x36453c60c_k15_s10.py` |  |
| 0.47 | 16/34 | 1 | 2.0825s | 0.1089s | 1 | 8 | yes | 2.0172s | 2.1595s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x296d42ec1_k16_s01.py` |  |
| 0.47 | 16/34 | 2 | 2.1383s | 0.0566s | 1 | 8 | yes | 2.0975s | 2.1665s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x299ae9898_k16_s02.py` |  |
| 0.47 | 16/34 | 3 | 1.5044s | 0.0603s | 1 | 8 | yes | 1.4648s | 1.5425s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x24f2b22f_k16_s03.py` |  |
| 0.47 | 16/34 | 4 | 2.4772s | 0.1869s | 1 | 8 | yes | 2.3691s | 2.6070s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x26ddec11_k16_s04.py` |  |
| 0.47 | 16/34 | 5 | 2.0853s | 0.0455s | 1 | 8 | yes | 2.0530s | 2.1123s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x594f4959_k16_s05.py` |  |
| 0.47 | 16/34 | 6 | 6.6463s | 0.1246s | 1 | 8 | yes | 6.5734s | 6.7332s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x31bf60234_k16_s06.py` |  |
| 0.47 | 16/34 | 7 | 8.0273s | 0.1207s | 1 | 8 | yes | 7.9534s | 8.1094s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1c3b63813_k16_s07.py` |  |
| 0.47 | 16/34 | 8 | 2.7033s | 0.1210s | 1 | 8 | yes | 2.6355s | 2.7898s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x85dd742c_k16_s08.py` |  |
| 0.47 | 16/34 | 9 | 9.7108s | 0.1146s | 1 | 8 | yes | 9.6489s | 9.7928s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3c500d5ab_k16_s09.py` |  |
| 0.47 | 16/34 | 10 | 2.0524s | 0.0666s | 1 | 8 | yes | 2.0067s | 2.0937s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3724873b_k16_s10.py` |  |
| 0.50 | 17/34 | 1 | 1.6646s | 0.0845s | 1 | 8 | yes | 1.6137s | 1.7227s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x23a5590af_k17_s01.py` |  |
| 0.50 | 17/34 | 2 | 2.6353s | 0.1118s | 1 | 8 | yes | 2.5656s | 2.7096s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2381db4ba_k17_s02.py` |  |
| 0.50 | 17/34 | 3 | 2.0277s | 0.0679s | 1 | 8 | yes | 1.9842s | 2.0714s | `detyped_files/deltablue/advanced/proportion_sweep/main_0xde8832be_k17_s03.py` |  |
| 0.50 | 17/34 | 4 | 2.2576s | 0.1520s | 1 | 8 | yes | 2.1651s | 2.3625s | `detyped_files/deltablue/advanced/proportion_sweep/main_0xd961cc76_k17_s04.py` |  |
| 0.50 | 17/34 | 5 | 2.5047s | 0.0780s | 1 | 8 | yes | 2.4586s | 2.5582s | `detyped_files/deltablue/advanced/proportion_sweep/main_0xbabb0633_k17_s05.py` |  |
| 0.50 | 17/34 | 6 | 8.8782s | 0.1650s | 1 | 8 | yes | 8.7754s | 8.9877s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x161298fce_k17_s06.py` |  |
| 0.50 | 17/34 | 7 | 8.6090s | 0.0904s | 1 | 8 | yes | 8.5504s | 8.6690s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1d83b10bb_k17_s07.py` |  |
| 0.50 | 17/34 | 8 | 2.3218s | 0.0905s | 1 | 8 | yes | 2.2622s | 2.3796s | `detyped_files/deltablue/advanced/proportion_sweep/main_0xc83f5ac6_k17_s08.py` |  |
| 0.50 | 17/34 | 9 | 1.5724s | 0.0849s | 1 | 8 | yes | 1.5138s | 1.6231s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x20277e2c7_k17_s09.py` |  |
| 0.50 | 17/34 | 10 | 2.1586s | 0.1619s | 1 | 8 | yes | 2.0632s | 2.2674s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2af1e183c_k17_s10.py` |  |
| 0.53 | 18/34 | 1 | 2.2529s | 0.0983s | 1 | 8 | yes | 2.1908s | 2.3168s | `detyped_files/deltablue/advanced/proportion_sweep/main_0xe4547d6e_k18_s01.py` |  |
| 0.53 | 18/34 | 2 | 9.7184s | 0.1798s | 1 | 8 | yes | 9.6119s | 9.8433s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1e8c2b4fc_k18_s02.py` |  |
| 0.53 | 18/34 | 3 | 10.0996s | 0.0730s | 1 | 8 | yes | 10.0504s | 10.1444s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1a92ea65d_k18_s03.py` |  |
| 0.53 | 18/34 | 4 | 8.8992s | 0.1484s | 1 | 8 | yes | 8.8027s | 8.9932s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x17b198cae_k18_s04.py` |  |
| 0.53 | 18/34 | 5 | 10.1918s | 0.1698s | 1 | 8 | yes | 10.0887s | 10.3061s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3d60fb438_k18_s05.py` |  |
| 0.53 | 18/34 | 6 | 2.0602s | 0.1038s | 1 | 8 | yes | 1.9942s | 2.1265s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x27486f68d_k18_s06.py` |  |
| 0.53 | 18/34 | 7 | 10.0507s | 0.0616s | 1 | 8 | yes | 10.0117s | 10.0912s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1e358c6b9_k18_s07.py` |  |
| 0.53 | 18/34 | 8 | 2.0952s | 0.0890s | 1 | 8 | yes | 2.0356s | 2.1494s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2ef32bc12_k18_s08.py` |  |
| 0.53 | 18/34 | 9 | 1.4949s | 0.0837s | 1 | 8 | yes | 1.4400s | 1.5473s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x22bb3ab62_k18_s09.py` |  |
| 0.53 | 18/34 | 10 | 8.4646s | 0.1142s | 1 | 8 | yes | 8.3911s | 8.5390s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3af693330_k18_s10.py` |  |
| 0.56 | 19/34 | 1 | 2.1618s | 0.0847s | 1 | 8 | yes | 2.1126s | 2.2217s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x25a27cdda_k19_s01.py` |  |
| 0.56 | 19/34 | 2 | 1.9673s | 0.1046s | 1 | 8 | yes | 1.9126s | 2.0438s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x25b944f67_k19_s02.py` |  |
| 0.56 | 19/34 | 3 | 2.5895s | 0.1152s | 1 | 8 | yes | 2.5211s | 2.6707s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x565cf6ba_k19_s03.py` |  |
| 0.56 | 19/34 | 4 | 6.7291s | 0.0726s | 1 | 8 | yes | 6.6870s | 6.7812s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x357362b2b_k19_s04.py` |  |
| 0.56 | 19/34 | 5 | 2.1937s | 0.1086s | 1 | 8 | yes | 2.1262s | 2.2628s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2aec978d6_k19_s05.py` |  |
| 0.56 | 19/34 | 6 | 8.6507s | 0.1315s | 1 | 8 | yes | 8.5575s | 8.7292s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3c983557d_k19_s06.py` |  |
| 0.56 | 19/34 | 7 | 2.0468s | 0.1137s | 1 | 8 | yes | 1.9698s | 2.1172s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x256afa978_k19_s07.py` |  |
| 0.56 | 19/34 | 8 | 2.4978s | 0.0835s | 1 | 8 | yes | 2.4435s | 2.5521s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x21e7be683_k19_s08.py` |  |
| 0.56 | 19/34 | 9 | 2.3757s | 0.0476s | 1 | 8 | yes | 2.3454s | 2.4062s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x16ccefe6_k19_s09.py` |  |
| 0.56 | 19/34 | 10 | 7.7244s | 0.1198s | 1 | 8 | yes | 7.6502s | 7.8043s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x37daa5d09_k19_s10.py` |  |
| 0.59 | 20/34 | 1 | 2.2581s | 0.0852s | 1 | 8 | yes | 2.1997s | 2.3104s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2ea6f89bc_k20_s01.py` |  |
| 0.59 | 20/34 | 2 | 9.0195s | 0.1930s | 1 | 8 | yes | 8.8953s | 9.1440s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3999f5c56_k20_s02.py` |  |
| 0.59 | 20/34 | 3 | 1.7572s | 0.0518s | 1 | 8 | yes | 1.7225s | 1.7905s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x285353bef_k20_s03.py` |  |
| 0.59 | 20/34 | 4 | 2.2204s | 0.0935s | 1 | 8 | yes | 2.1589s | 2.2806s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x21155cffb_k20_s04.py` |  |
| 0.59 | 20/34 | 5 | 1.7940s | 0.1094s | 1 | 8 | yes | 1.7254s | 1.8669s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2f5a458fb_k20_s05.py` |  |
| 0.59 | 20/34 | 6 | 8.9982s | 0.1019s | 1 | 8 | yes | 8.9347s | 9.0663s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3917f3cc3_k20_s06.py` |  |
| 0.59 | 20/34 | 7 | 10.1249s | 0.1653s | 1 | 8 | yes | 10.0243s | 10.2375s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1cfa88fbc_k20_s07.py` |  |
| 0.59 | 20/34 | 8 | 8.1780s | 0.1167s | 1 | 8 | yes | 8.0989s | 8.2472s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3a17159f7_k20_s08.py` |  |
| 0.59 | 20/34 | 9 | 9.8583s | 0.1145s | 1 | 8 | yes | 9.7848s | 9.9320s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3f895ee58_k20_s09.py` |  |
| 0.59 | 20/34 | 10 | 8.5933s | 0.0727s | 1 | 8 | yes | 8.5464s | 8.6404s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1f453173f_k20_s10.py` |  |
| 0.62 | 21/34 | 1 | 2.2983s | 0.1193s | 1 | 8 | yes | 2.2248s | 2.3814s | `detyped_files/deltablue/advanced/proportion_sweep/main_0xb761eff8_k21_s01.py` |  |
| 0.62 | 21/34 | 2 | 8.4182s | 0.0655s | 1 | 8 | yes | 8.3758s | 8.4602s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x37a15be3e_k21_s02.py` |  |
| 0.62 | 21/34 | 3 | 1.6185s | 0.0408s | 1 | 8 | yes | 1.5924s | 1.6449s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x6ee66b7d_k21_s03.py` |  |
| 0.62 | 21/34 | 4 | 8.1214s | 0.1189s | 1 | 8 | yes | 8.0458s | 8.2011s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x396b12bdf_k21_s04.py` |  |
| 0.62 | 21/34 | 5 | 9.7187s | 0.0865s | 1 | 8 | yes | 9.6627s | 9.7761s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3fb5ff084_k21_s05.py` |  |
| 0.62 | 21/34 | 6 | 8.8849s | 0.1311s | 1 | 8 | yes | 8.8045s | 8.9729s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x11ce9f72f_k21_s06.py` |  |
| 0.62 | 21/34 | 7 | 8.9549s | 0.1032s | 1 | 8 | yes | 8.8944s | 9.0264s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x39c3c77d6_k21_s07.py` |  |
| 0.62 | 21/34 | 8 | 2.2206s | 0.0609s | 1 | 8 | yes | 2.1832s | 2.2612s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2fb04befc_k21_s08.py` |  |
| 0.62 | 21/34 | 9 | 2.6454s | 0.1933s | 1 | 8 | yes | 2.5247s | 2.7732s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x247bf75aa_k21_s09.py` |  |
| 0.62 | 21/34 | 10 | 8.5777s | 0.0930s | 1 | 8 | yes | 8.5164s | 8.6357s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x382b52f7f_k21_s10.py` |  |
| 0.65 | 22/34 | 1 | 8.8890s | 0.1184s | 1 | 8 | yes | 8.8164s | 8.9705s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3595fceda_k22_s01.py` |  |
| 0.65 | 22/34 | 2 | 7.7278s | 0.2003s | 1 | 8 | yes | 7.6218s | 7.8688s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x12ede1d7f_k22_s02.py` |  |
| 0.65 | 22/34 | 3 | 9.7338s | 0.0880s | 1 | 8 | yes | 9.6761s | 9.7898s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3ab8efa79_k22_s03.py` |  |
| 0.65 | 22/34 | 4 | 7.6691s | 0.0941s | 1 | 8 | yes | 7.6119s | 7.7335s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x375ea5e9e_k22_s04.py` |  |
| 0.65 | 22/34 | 5 | 2.2946s | 0.1525s | 1 | 8 | yes | 2.1966s | 2.3948s | `detyped_files/deltablue/advanced/proportion_sweep/main_0xae347dff_k22_s05.py` |  |
| 0.65 | 22/34 | 6 | 10.1490s | 0.1452s | 1 | 8 | yes | 10.0569s | 10.2448s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1f48cffea_k22_s06.py` |  |
| 0.65 | 22/34 | 7 | 2.2115s | 0.0776s | 1 | 8 | yes | 2.1587s | 2.2592s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2dbf33cf2_k22_s07.py` |  |
| 0.65 | 22/34 | 8 | 10.0786s | 0.1196s | 1 | 8 | yes | 9.9989s | 10.1543s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1f2ae8fbb_k22_s08.py` |  |
| 0.65 | 22/34 | 9 | 2.6786s | 0.1150s | 1 | 8 | yes | 2.6043s | 2.7522s | `detyped_files/deltablue/advanced/proportion_sweep/main_0xdbbaed1f_k22_s09.py` |  |
| 0.65 | 22/34 | 10 | 9.0125s | 0.0992s | 1 | 8 | yes | 8.9493s | 9.0763s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1f1de7c6b_k22_s10.py` |  |
| 0.68 | 23/34 | 1 | 1.7164s | 0.0660s | 1 | 8 | yes | 1.6765s | 1.7616s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x26fe5d36f_k23_s01.py` |  |
| 0.68 | 23/34 | 2 | 8.9034s | 0.2095s | 1 | 8 | yes | 8.7834s | 9.0539s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1517befde_k23_s02.py` |  |
| 0.68 | 23/34 | 3 | 10.0833s | 0.0701s | 1 | 8 | yes | 10.0382s | 10.1283s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3e08fbfed_k23_s03.py` |  |
| 0.68 | 23/34 | 4 | 7.6924s | 0.0871s | 1 | 8 | yes | 7.6342s | 7.7470s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x37d7e77e0_k23_s04.py` |  |
| 0.68 | 23/34 | 5 | 2.6535s | 0.1054s | 1 | 8 | yes | 2.5856s | 2.7193s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2af9fa7ce_k23_s05.py` |  |
| 0.68 | 23/34 | 6 | 2.0993s | 0.0605s | 1 | 8 | yes | 2.0620s | 2.1394s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2fb3c3b3f_k23_s06.py` |  |
| 0.68 | 23/34 | 7 | 9.7655s | 0.1832s | 1 | 8 | yes | 9.6532s | 9.8856s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1f5bff1e8_k23_s07.py` |  |
| 0.68 | 23/34 | 8 | 10.1729s | 0.0878s | 1 | 8 | yes | 10.1167s | 10.2293s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1edfede1a_k23_s08.py` |  |
| 0.68 | 23/34 | 9 | 9.1826s | 0.1500s | 1 | 8 | yes | 9.1040s | 9.2929s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3dae95f3b_k23_s09.py` |  |
| 0.68 | 23/34 | 10 | 9.0332s | 0.1766s | 1 | 8 | yes | 8.9207s | 9.1493s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x397fc5d7c_k23_s10.py` |  |
| 0.71 | 24/34 | 1 | 2.6668s | 0.1114s | 1 | 8 | yes | 2.5912s | 2.7366s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2f3bd7ee6_k24_s01.py` |  |
| 0.71 | 24/34 | 2 | 2.1597s | 0.0596s | 1 | 8 | yes | 2.1247s | 2.2015s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2bb9be9fd_k24_s02.py` |  |
| 0.71 | 24/34 | 3 | 8.9736s | 0.0882s | 1 | 8 | yes | 8.9162s | 9.0305s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3fefc6c73_k24_s03.py` |  |
| 0.71 | 24/34 | 4 | 2.3182s | 0.1827s | 1 | 8 | yes | 2.2115s | 2.4433s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2fbf49d7d_k24_s04.py` |  |
| 0.71 | 24/34 | 5 | 9.6920s | 0.0802s | 1 | 8 | yes | 9.6419s | 9.7459s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x19ff9d9f9_k24_s05.py` |  |
| 0.71 | 24/34 | 6 | 9.8022s | 0.1606s | 1 | 8 | yes | 9.6981s | 9.9077s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3ceadeabf_k24_s06.py` |  |
| 0.71 | 24/34 | 7 | 8.3880s | 0.1002s | 1 | 8 | yes | 8.3282s | 8.4561s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x335f9f3ed_k24_s07.py` |  |
| 0.71 | 24/34 | 8 | 10.2517s | 0.2038s | 1 | 8 | yes | 10.1246s | 10.3823s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x38f7afdce_k24_s08.py` |  |
| 0.71 | 24/34 | 9 | 9.7262s | 0.1073s | 1 | 8 | yes | 9.6610s | 9.8001s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3fc33e5f7_k24_s09.py` |  |
| 0.71 | 24/34 | 10 | 7.7143s | 0.0750s | 1 | 8 | yes | 7.6653s | 7.7621s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x35dfe7d9c_k24_s10.py` |  |
| 0.74 | 25/34 | 1 | 10.1522s | 0.1241s | 1 | 8 | yes | 10.0788s | 10.2367s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1ffbdf752_k25_s01.py` |  |
| 0.74 | 25/34 | 2 | 9.8196s | 0.1040s | 1 | 8 | yes | 9.7441s | 9.8794s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3ff27e56f_k25_s02.py` |  |
| 0.74 | 25/34 | 3 | 7.1889s | 0.1468s | 1 | 8 | yes | 7.0998s | 7.2867s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x37edb6bb7_k25_s03.py` |  |
| 0.74 | 25/34 | 4 | 2.2520s | 0.1158s | 1 | 8 | yes | 2.1755s | 2.3277s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x25fe7ff2d_k25_s04.py` |  |
| 0.74 | 25/34 | 5 | 2.7372s | 0.1322s | 1 | 8 | yes | 2.6562s | 2.8262s | `detyped_files/deltablue/advanced/proportion_sweep/main_0xfd7b7fcd_k25_s05.py` |  |
| 0.74 | 25/34 | 6 | 2.3585s | 0.0968s | 1 | 8 | yes | 2.2951s | 2.4208s | `detyped_files/deltablue/advanced/proportion_sweep/main_0xfed5ceff_k25_s06.py` |  |
| 0.74 | 25/34 | 7 | 8.8686s | 0.1055s | 1 | 8 | yes | 8.8039s | 8.9391s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1f99c77ff_k25_s07.py` |  |
| 0.74 | 25/34 | 8 | 9.7850s | 0.0678s | 1 | 8 | yes | 9.7420s | 9.8272s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1ff73fc4f_k25_s08.py` |  |
| 0.74 | 25/34 | 9 | 8.5980s | 0.0667s | 1 | 8 | yes | 8.5565s | 8.6424s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x375c7d7fb_k25_s09.py` |  |
| 0.74 | 25/34 | 10 | 10.0989s | 0.1486s | 1 | 8 | yes | 10.0029s | 10.1955s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3f6cabdfd_k25_s10.py` |  |
| 0.76 | 26/34 | 1 | 10.1710s | 0.1002s | 1 | 8 | yes | 10.1015s | 10.2287s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3cba9efff_k26_s01.py` |  |
| 0.76 | 26/34 | 2 | 2.7078s | 0.0458s | 1 | 8 | yes | 2.6796s | 2.7391s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2cff9bfbd_k26_s02.py` |  |
| 0.76 | 26/34 | 3 | 10.2727s | 0.1446s | 1 | 8 | yes | 10.1841s | 10.3708s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3c7ffd75e_k26_s03.py` |  |
| 0.76 | 26/34 | 4 | 2.6634s | 0.0461s | 1 | 8 | yes | 2.6333s | 2.6926s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2bbfef79b_k26_s04.py` |  |
| 0.76 | 26/34 | 5 | 8.8869s | 0.0513s | 1 | 8 | yes | 8.8540s | 8.9195s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x17beff773_k26_s05.py` |  |
| 0.76 | 26/34 | 6 | 2.5187s | 0.0557s | 1 | 8 | yes | 2.4816s | 2.5538s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x26f5bfef7_k26_s06.py` |  |
| 0.76 | 26/34 | 7 | 2.7214s | 0.1460s | 1 | 8 | yes | 2.6315s | 2.8175s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2f1bdf77f_k26_s07.py` |  |
| 0.76 | 26/34 | 8 | 8.9322s | 0.1206s | 1 | 8 | yes | 8.8545s | 9.0074s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3f7ef3ed5_k26_s08.py` |  |
| 0.76 | 26/34 | 9 | 8.9733s | 0.1361s | 1 | 8 | yes | 8.9099s | 9.0730s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x37bcfe7f9_k26_s09.py` |  |
| 0.76 | 26/34 | 10 | 8.5309s | 0.1609s | 1 | 8 | yes | 8.4277s | 8.6337s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3fafb3bf6_k26_s10.py` |  |
| 0.79 | 27/34 | 1 | 8.9463s | 0.1208s | 1 | 8 | yes | 8.8672s | 9.0231s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x37efaf7fa_k27_s01.py` |  |
| 0.79 | 27/34 | 2 | 9.0472s | 0.3134s | 1 | 8 | yes | 8.8916s | 9.2742s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x397ff7777_k27_s02.py` |  |
| 0.79 | 27/34 | 3 | 9.8626s | 0.1046s | 1 | 8 | yes | 9.7949s | 9.9300s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3b7f3f6bf_k27_s03.py` |  |
| 0.79 | 27/34 | 4 | 2.2961s | 0.0868s | 1 | 8 | yes | 2.2443s | 2.3544s | `detyped_files/deltablue/advanced/proportion_sweep/main_0xfef7dfe7_k27_s04.py` |  |
| 0.79 | 27/34 | 5 | 2.7609s | 0.1447s | 1 | 8 | yes | 2.6727s | 2.8579s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2ffdf7d5b_k27_s05.py` |  |
| 0.79 | 27/34 | 6 | 10.1481s | 0.0751s | 1 | 8 | yes | 10.0976s | 10.1944s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3ef3fff17_k27_s06.py` |  |
| 0.79 | 27/34 | 7 | 2.2325s | 0.0402s | 1 | 8 | yes | 2.2070s | 2.2592s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2f7ffebea_k27_s07.py` |  |
| 0.79 | 27/34 | 8 | 2.3895s | 0.1745s | 1 | 8 | yes | 2.2860s | 2.5119s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2bff5edfb_k27_s08.py` |  |
| 0.79 | 27/34 | 9 | 8.8722s | 0.1603s | 1 | 8 | yes | 8.7820s | 8.9882s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x37f7cdf7e_k27_s09.py` |  |
| 0.79 | 27/34 | 10 | 9.4031s | 0.1084s | 1 | 8 | yes | 9.3354s | 9.4769s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3fb73f3fb_k27_s10.py` |  |
| 0.82 | 28/34 | 1 | 8.9027s | 0.0861s | 1 | 8 | yes | 8.8412s | 8.9501s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x37f9ffcfe_k28_s01.py` |  |
| 0.82 | 28/34 | 2 | 9.7656s | 0.1066s | 1 | 8 | yes | 9.6988s | 9.8366s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3fbe7bff6_k28_s02.py` |  |
| 0.82 | 28/34 | 3 | 2.1600s | 0.1077s | 1 | 8 | yes | 2.0933s | 2.2323s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2ffbfb9f7_k28_s03.py` |  |
| 0.82 | 28/34 | 4 | 8.8942s | 0.1361s | 1 | 8 | yes | 8.8013s | 8.9771s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x17fbfb7df_k28_s04.py` |  |
| 0.82 | 28/34 | 5 | 10.1772s | 0.0526s | 1 | 8 | yes | 10.1420s | 10.2093s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3fd9dffdd_k28_s05.py` |  |
| 0.82 | 28/34 | 6 | 9.8862s | 0.1005s | 1 | 8 | yes | 9.8239s | 9.9518s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1bf7df3ff_k28_s06.py` |  |
| 0.82 | 28/34 | 7 | 8.9898s | 0.0957s | 1 | 8 | yes | 8.9310s | 9.0535s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x33fffeedd_k28_s07.py` |  |
| 0.82 | 28/34 | 8 | 9.7869s | 0.0573s | 1 | 8 | yes | 9.7482s | 9.8222s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3ebf7efed_k28_s08.py` |  |
| 0.82 | 28/34 | 9 | 9.0221s | 0.1135s | 1 | 8 | yes | 8.9599s | 9.1048s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1efaf7fbf_k28_s09.py` |  |
| 0.82 | 28/34 | 10 | 10.1462s | 0.1587s | 1 | 8 | yes | 10.0572s | 10.2586s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1f7fdbfed_k28_s10.py` |  |
| 0.85 | 29/34 | 1 | 2.5584s | 0.0609s | 1 | 8 | yes | 2.5244s | 2.6015s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x27fbfeffb_k29_s01.py` |  |
| 0.85 | 29/34 | 2 | 8.9467s | 0.1595s | 1 | 8 | yes | 8.8565s | 9.0582s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x37e7fff7d_k29_s02.py` |  |
| 0.85 | 29/34 | 3 | 2.3126s | 0.0858s | 1 | 8 | yes | 2.2603s | 2.3703s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2f7d7efff_k29_s03.py` |  |
| 0.85 | 29/34 | 4 | 9.7030s | 0.0883s | 1 | 8 | yes | 9.6460s | 9.7594s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3feeefbbf_k29_s04.py` |  |
| 0.85 | 29/34 | 5 | 8.6091s | 0.1057s | 1 | 8 | yes | 8.5442s | 8.6798s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3efff6bfe_k29_s05.py` |  |
| 0.85 | 29/34 | 6 | 9.8273s | 0.1196s | 1 | 8 | yes | 9.7506s | 9.9055s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3bfb7eeff_k29_s06.py` |  |
| 0.85 | 29/34 | 7 | 10.2160s | 0.1393s | 1 | 8 | yes | 10.1238s | 10.3033s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3fbdffdf6_k29_s07.py` |  |
| 0.85 | 29/34 | 8 | 10.3290s | 0.2063s | 1 | 8 | yes | 10.2055s | 10.4679s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1f7fffe9f_k29_s08.py` |  |
| 0.85 | 29/34 | 9 | 10.2234s | 0.1336s | 1 | 8 | yes | 10.1390s | 10.3109s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3eb7fbffb_k29_s09.py` |  |
| 0.85 | 29/34 | 10 | 10.2885s | 0.1506s | 1 | 8 | yes | 10.2005s | 10.3921s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3df7dbfbf_k29_s10.py` |  |
| 0.88 | 30/34 | 1 | 10.2758s | 0.1301s | 1 | 8 | yes | 10.2053s | 10.3704s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3feefbffb_k30_s01.py` |  |
| 0.88 | 30/34 | 2 | 10.2464s | 0.0516s | 1 | 8 | yes | 10.2159s | 10.2824s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3fdfffded_k30_s02.py` |  |
| 0.88 | 30/34 | 3 | 10.1537s | 0.0629s | 1 | 8 | yes | 10.1130s | 10.1944s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3fdffbff6_k30_s03.py` |  |
| 0.88 | 30/34 | 4 | 9.7197s | 0.0744s | 1 | 8 | yes | 9.6744s | 9.7695s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3efdff3ff_k30_s04.py` |  |
| 0.88 | 30/34 | 5 | 2.7256s | 0.0923s | 1 | 8 | yes | 2.6669s | 2.7861s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x2bfefffef_k30_s05.py` |  |
| 0.88 | 30/34 | 6 | 9.2971s | 0.0936s | 1 | 8 | yes | 9.2395s | 9.3591s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3ffb6fbff_k30_s06.py` |  |
| 0.88 | 30/34 | 7 | 9.9064s | 0.1166s | 1 | 8 | yes | 9.8346s | 9.9828s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3fffff0ff_k30_s07.py` |  |
| 0.88 | 30/34 | 8 | 9.0184s | 0.1071s | 1 | 8 | yes | 8.9557s | 9.0956s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3fffe6fdf_k30_s08.py` |  |
| 0.88 | 30/34 | 9 | 10.1619s | 0.0597s | 1 | 8 | yes | 10.1261s | 10.2033s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1fff8ffff_k30_s09.py` |  |
| 0.88 | 30/34 | 10 | 8.9993s | 0.1672s | 1 | 8 | yes | 8.9126s | 9.1196s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3ffde6fff_k30_s10.py` |  |
| 0.91 | 31/34 | 1 | 9.0714s | 0.0777s | 1 | 8 | yes | 9.0208s | 9.1200s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3fbff7dff_k31_s01.py` |  |
| 0.91 | 31/34 | 2 | 10.2425s | 0.1434s | 1 | 8 | yes | 10.1527s | 10.3359s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1fefff7ff_k31_s02.py` |  |
| 0.91 | 31/34 | 3 | 8.5330s | 0.1416s | 1 | 8 | yes | 8.4503s | 8.6323s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x36ffffbff_k31_s03.py` |  |
| 0.91 | 31/34 | 4 | 9.8508s | 0.1114s | 1 | 8 | yes | 9.7825s | 9.9259s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3bff3ffff_k31_s04.py` |  |
| 0.91 | 31/34 | 5 | 9.0946s | 0.1173s | 1 | 8 | yes | 9.0149s | 9.1666s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3ffbf7f7f_k31_s05.py` |  |
| 0.91 | 31/34 | 6 | 10.2724s | 0.1585s | 1 | 8 | yes | 10.1734s | 10.3762s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3ffefff7b_k31_s06.py` |  |
| 0.91 | 31/34 | 7 | 9.7674s | 0.1290s | 1 | 8 | yes | 9.6910s | 9.8544s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x1fffffbbf_k31_s07.py` |  |
| 0.91 | 31/34 | 8 | 9.0558s | 0.1021s | 1 | 8 | yes | 8.9891s | 9.1225s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3fffd7ffb_k31_s08.py` |  |
| 0.91 | 31/34 | 9 | 10.1682s | 0.0831s | 1 | 8 | yes | 10.1142s | 10.2203s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3ff7effef_k31_s09.py` |  |
| 0.91 | 31/34 | 10 | 10.2969s | 0.0558s | 1 | 8 | yes | 10.2604s | 10.3329s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3beffefff_k31_s10.py` |  |
| 0.94 | 32/34 | 1 | 10.2347s | 0.0488s | 1 | 8 | yes | 10.2040s | 10.2664s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3dfffbfff_k32_s01.py` |  |
| 0.94 | 32/34 | 2 | 9.8371s | 0.1361s | 1 | 8 | yes | 9.7473s | 9.9237s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3ffffebff_k32_s02.py` |  |
| 0.94 | 32/34 | 3 | 10.2823s | 0.1799s | 1 | 8 | yes | 10.1812s | 10.4097s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3ffffffbe_k32_s03.py` |  |
| 0.94 | 32/34 | 4 | 10.2938s | 0.1593s | 1 | 8 | yes | 10.1993s | 10.4035s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3f7fffeff_k32_s04.py` |  |
| 0.94 | 32/34 | 5 | 10.3211s | 0.1630s | 1 | 8 | yes | 10.2252s | 10.4368s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3fbffffef_k32_s05.py` |  |
| 0.94 | 32/34 | 6 | 10.2298s | 0.1641s | 1 | 8 | yes | 10.1301s | 10.3387s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3f7ffbfff_k32_s06.py` |  |
| 0.94 | 32/34 | 7 | 9.8562s | 0.0690s | 1 | 8 | yes | 9.8066s | 9.8957s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3fffffbef_k32_s07.py` |  |
| 0.94 | 32/34 | 8 | 10.2224s | 0.1209s | 1 | 8 | yes | 10.1438s | 10.2982s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3dffffffd_k32_s08.py` |  |
| 0.94 | 32/34 | 9 | 10.2318s | 0.1209s | 1 | 8 | yes | 10.1535s | 10.3087s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3deffffff_k32_s09.py` |  |
| 0.94 | 32/34 | 10 | 10.3181s | 0.1250s | 1 | 8 | yes | 10.2416s | 10.4037s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3ffffdfdf_k32_s10.py` |  |
| 0.97 | 33/34 | 1 | 10.2273s | 0.0583s | 1 | 8 | yes | 10.1907s | 10.2656s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3ffffdfff_k33_s01.py` |  |
| 0.97 | 33/34 | 2 | 10.2448s | 0.0806s | 1 | 8 | yes | 10.1903s | 10.2954s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3fffffffb_k33_s02.py` |  |
| 0.97 | 33/34 | 3 | 10.2428s | 0.0943s | 1 | 8 | yes | 10.1837s | 10.3037s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3ffefffff_k33_s03.py` |  |
| 0.97 | 33/34 | 4 | 10.2315s | 0.0809s | 1 | 8 | yes | 10.1789s | 10.2845s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3ffffefff_k33_s04.py` |  |
| 0.97 | 33/34 | 5 | 10.2851s | 0.1568s | 1 | 8 | yes | 10.2072s | 10.3993s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3bfffffff_k33_s05.py` |  |
| 0.97 | 33/34 | 6 | 10.3207s | 0.1083s | 1 | 8 | yes | 10.2512s | 10.3898s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3fffffffd_k33_s06.py` |  |
| 0.97 | 33/34 | 7 | 10.2540s | 0.1038s | 1 | 8 | yes | 10.1813s | 10.3148s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3ffffffdf_k33_s07.py` |  |
| 0.97 | 33/34 | 8 | 10.2907s | 0.1643s | 1 | 8 | yes | 10.1833s | 10.3963s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3ffbfffff_k33_s08.py` |  |
| 0.97 | 33/34 | 9 | 10.3173s | 0.1840s | 1 | 8 | yes | 10.1981s | 10.4349s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3feffffff_k33_s09.py` |  |
| 0.97 | 33/34 | 10 | 9.7970s | 0.1003s | 1 | 8 | yes | 9.7310s | 9.8610s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3fffffbff_k33_s10.py` |  |
| 1.00 | 34/34 | 1 | 10.1930s | 0.1047s | 1 | 8 | yes | 10.1274s | 10.2624s | `detyped_files/deltablue/advanced/proportion_sweep/main_0x3ffffffff_k34_s01.py` |  |

## deltablue/shallow

- Detypable targets: `35`
- Total runs: `342`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/35 | 1 | 1.1112s | 1.1112s | 1.1112s | 1.0 | yes | ok |
| 0.03 | 1/35 | 10 | 1.2097s | 1.0469s | 1.6017s | 1.0 | yes | ok |
| 0.06 | 2/35 | 10 | 1.2824s | 1.0834s | 1.7213s | 1.0 | yes | ok |
| 0.09 | 3/35 | 10 | 1.2724s | 1.1102s | 1.5586s | 1.0 | yes | ok |
| 0.11 | 4/35 | 10 | 1.1689s | 1.0622s | 1.4248s | 1.0 | yes | ok |
| 0.14 | 5/35 | 10 | 1.4246s | 1.1149s | 1.7876s | 1.0 | yes | ok |
| 0.17 | 6/35 | 10 | 1.3708s | 1.1350s | 1.8239s | 1.0 | yes | ok |
| 0.20 | 7/35 | 10 | 1.4144s | 1.1126s | 1.9249s | 1.0 | yes | ok |
| 0.23 | 8/35 | 10 | 1.4407s | 1.1585s | 1.8650s | 1.0 | yes | ok |
| 0.26 | 9/35 | 10 | 1.7682s | 1.2136s | 2.2002s | 1.0 | yes | ok |
| 0.29 | 10/35 | 10 | 1.6026s | 1.1734s | 2.0927s | 1.0 | yes | ok |
| 0.31 | 11/35 | 10 | 1.5008s | 1.2498s | 1.8916s | 1.0 | yes | ok |
| 0.34 | 12/35 | 10 | 1.5361s | 1.1211s | 2.0552s | 1.0 | yes | ok |
| 0.37 | 13/35 | 10 | 1.7140s | 1.3485s | 2.1959s | 1.0 | yes | ok |
| 0.40 | 14/35 | 10 | 1.7780s | 1.3149s | 2.2468s | 1.0 | yes | ok |
| 0.43 | 15/35 | 10 | 1.7756s | 1.2706s | 2.3040s | 1.0 | yes | ok |
| 0.46 | 16/35 | 10 | 1.7848s | 1.3054s | 2.1983s | 1.0 | yes | ok |
| 0.49 | 17/35 | 10 | 1.8077s | 1.3261s | 2.3774s | 1.0 | yes | ok |
| 0.51 | 18/35 | 10 | 2.1447s | 1.4825s | 2.5332s | 1.0 | yes | ok |
| 0.54 | 19/35 | 10 | 1.9345s | 1.4411s | 2.3869s | 1.0 | yes | ok |
| 0.57 | 20/35 | 10 | 1.9776s | 1.4933s | 2.4994s | 1.0 | yes | ok |
| 0.60 | 21/35 | 10 | 2.1271s | 1.6302s | 2.5208s | 1.0 | yes | ok |
| 0.63 | 22/35 | 10 | 2.0296s | 1.5858s | 2.4213s | 1.0 | yes | ok |
| 0.66 | 23/35 | 10 | 2.1768s | 1.6710s | 2.4253s | 1.0 | yes | ok |
| 0.69 | 24/35 | 10 | 2.1911s | 1.9672s | 2.5116s | 1.0 | yes | ok |
| 0.71 | 25/35 | 10 | 2.3875s | 2.1910s | 2.5750s | 1.0 | yes | ok |
| 0.74 | 26/35 | 10 | 2.2540s | 1.6866s | 2.5332s | 1.0 | yes | ok |
| 0.77 | 27/35 | 10 | 2.2595s | 1.7038s | 2.6182s | 1.0 | yes | ok |
| 0.80 | 28/35 | 10 | 2.2548s | 1.5727s | 2.5152s | 1.0 | yes | ok |
| 0.83 | 29/35 | 10 | 2.3629s | 1.7506s | 2.6117s | 1.0 | yes | ok |
| 0.86 | 30/35 | 10 | 2.4242s | 2.0591s | 2.6126s | 1.0 | yes | ok |
| 0.89 | 31/35 | 10 | 2.5535s | 2.2041s | 2.7084s | 1.0 | yes | ok |
| 0.91 | 32/35 | 10 | 2.5120s | 2.2600s | 2.6024s | 1.0 | yes | ok |
| 0.94 | 33/35 | 10 | 2.5025s | 2.0654s | 2.6532s | 1.0 | yes | ok |
| 0.97 | 34/35 | 10 | 2.5905s | 2.4848s | 2.6740s | 1.0 | yes | ok |
| 1.00 | 35/35 | 1 | 2.6380s | 2.6380s | 2.6380s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/35 | 1 | 1.1112s | 0.0907s | 1 | 8 | yes | 1.0512s | 1.1681s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x0_k00_s01.py` |  |
| 0.03 | 1/35 | 1 | 1.0469s | 0.0769s | 1 | 8 | yes | 0.9974s | 1.0960s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x4000_k01_s01.py` |  |
| 0.03 | 1/35 | 2 | 1.1635s | 0.1318s | 1 | 8 | yes | 1.0796s | 1.2472s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x800000_k01_s02.py` |  |
| 0.03 | 1/35 | 3 | 1.1338s | 0.0893s | 1 | 8 | yes | 1.0730s | 1.1886s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x8000_k01_s03.py` |  |
| 0.03 | 1/35 | 4 | 1.1178s | 0.0749s | 1 | 8 | yes | 1.0806s | 1.1722s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x4_k01_s04.py` |  |
| 0.03 | 1/35 | 5 | 1.0704s | 0.0649s | 1 | 8 | yes | 1.0310s | 1.1141s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x10000000_k01_s05.py` |  |
| 0.03 | 1/35 | 6 | 1.0659s | 0.0437s | 1 | 8 | yes | 1.0337s | 1.0873s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x400000000_k01_s06.py` |  |
| 0.03 | 1/35 | 7 | 1.1440s | 0.0686s | 1 | 8 | yes | 1.1003s | 1.1882s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x200000_k01_s07.py` |  |
| 0.03 | 1/35 | 8 | 1.5846s | 0.0802s | 1 | 8 | yes | 1.5378s | 1.6413s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x100000_k01_s08.py` |  |
| 0.03 | 1/35 | 9 | 1.6017s | 0.0943s | 1 | 8 | yes | 1.5423s | 1.6652s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x800_k01_s09.py` |  |
| 0.03 | 1/35 | 10 | 1.1686s | 0.0499s | 1 | 8 | yes | 1.1381s | 1.2024s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x1_k01_s10.py` |  |
| 0.06 | 2/35 | 1 | 1.7213s | 0.1351s | 1 | 8 | yes | 1.6464s | 1.8204s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x800800_k02_s01.py` |  |
| 0.06 | 2/35 | 2 | 1.5085s | 0.0738s | 1 | 8 | yes | 1.4609s | 1.5585s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x102000_k02_s02.py` |  |
| 0.06 | 2/35 | 3 | 1.1331s | 0.0660s | 1 | 8 | yes | 1.0897s | 1.1745s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x408000_k02_s03.py` |  |
| 0.06 | 2/35 | 4 | 1.1140s | 0.1167s | 1 | 8 | yes | 1.0417s | 1.1909s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x80000004_k02_s04.py` |  |
| 0.06 | 2/35 | 5 | 1.1034s | 0.0995s | 1 | 8 | yes | 1.0415s | 1.1702s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x40400_k02_s05.py` |  |
| 0.06 | 2/35 | 6 | 1.0834s | 0.0540s | 1 | 8 | yes | 1.0467s | 1.1149s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x10400_k02_s06.py` |  |
| 0.06 | 2/35 | 7 | 1.1274s | 0.1052s | 1 | 8 | yes | 1.0610s | 1.1962s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x20020000_k02_s07.py` |  |
| 0.06 | 2/35 | 8 | 1.1412s | 0.1268s | 1 | 8 | yes | 1.0641s | 1.2259s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x480000000_k02_s08.py` |  |
| 0.06 | 2/35 | 9 | 1.5773s | 0.0868s | 1 | 8 | yes | 1.5229s | 1.6317s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x4100000_k02_s09.py` |  |
| 0.06 | 2/35 | 10 | 1.3141s | 0.0725s | 1 | 8 | yes | 1.2710s | 1.3635s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x400000001_k02_s10.py` |  |
| 0.09 | 3/35 | 1 | 1.1809s | 0.0700s | 1 | 8 | yes | 1.1378s | 1.2271s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x4810000_k03_s01.py` |  |
| 0.09 | 3/35 | 2 | 1.2879s | 0.1049s | 1 | 8 | yes | 1.2289s | 1.3637s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x101000008_k03_s02.py` |  |
| 0.09 | 3/35 | 3 | 1.1883s | 0.0968s | 1 | 8 | yes | 1.1275s | 1.2515s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x88008_k03_s03.py` |  |
| 0.09 | 3/35 | 4 | 1.1754s | 0.0894s | 1 | 8 | yes | 1.1213s | 1.2360s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x8201000_k03_s04.py` |  |
| 0.09 | 3/35 | 5 | 1.5227s | 0.1003s | 1 | 8 | yes | 1.4588s | 1.5913s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x2120000_k03_s05.py` |  |
| 0.09 | 3/35 | 6 | 1.4271s | 0.1126s | 1 | 8 | yes | 1.3610s | 1.5047s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x8012_k03_s06.py` |  |
| 0.09 | 3/35 | 7 | 1.1102s | 0.0565s | 1 | 8 | yes | 1.0730s | 1.1454s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x410040_k03_s07.py` |  |
| 0.09 | 3/35 | 8 | 1.1216s | 0.0922s | 1 | 8 | yes | 1.0663s | 1.1858s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x4202000_k03_s08.py` |  |
| 0.09 | 3/35 | 9 | 1.1513s | 0.0525s | 1 | 8 | yes | 1.1156s | 1.1832s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x1000030_k03_s09.py` |  |
| 0.09 | 3/35 | 10 | 1.5586s | 0.0665s | 1 | 8 | yes | 1.5200s | 1.6045s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x100084_k03_s10.py` |  |
| 0.11 | 4/35 | 1 | 1.0622s | 0.0712s | 1 | 8 | yes | 1.0153s | 1.1065s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x221400_k04_s01.py` |  |
| 0.11 | 4/35 | 2 | 1.1040s | 0.0705s | 1 | 8 | yes | 1.0538s | 1.1429s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x40080a0_k04_s02.py` |  |
| 0.11 | 4/35 | 3 | 1.0677s | 0.0781s | 1 | 8 | yes | 1.0179s | 1.1190s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x200540_k04_s03.py` |  |
| 0.11 | 4/35 | 4 | 1.4248s | 0.1203s | 1 | 8 | yes | 1.3521s | 1.5073s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x80040012_k04_s04.py` |  |
| 0.11 | 4/35 | 5 | 1.2861s | 0.0823s | 1 | 8 | yes | 1.2345s | 1.3395s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x280800100_k04_s05.py` |  |
| 0.11 | 4/35 | 6 | 1.1614s | 0.0735s | 1 | 8 | yes | 1.1141s | 1.2078s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x440840000_k04_s06.py` |  |
| 0.11 | 4/35 | 7 | 1.3623s | 0.0956s | 1 | 8 | yes | 1.3081s | 1.4299s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x300022000_k04_s07.py` |  |
| 0.11 | 4/35 | 8 | 1.0845s | 0.1047s | 1 | 8 | yes | 1.0226s | 1.1581s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x10008600_k04_s08.py` |  |
| 0.11 | 4/35 | 9 | 1.0663s | 0.0478s | 1 | 8 | yes | 1.0351s | 1.0961s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x282100_k04_s09.py` |  |
| 0.11 | 4/35 | 10 | 1.0699s | 0.0541s | 1 | 8 | yes | 1.0335s | 1.1019s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x1004440_k04_s10.py` |  |
| 0.14 | 5/35 | 1 | 1.2265s | 0.0588s | 1 | 8 | yes | 1.1869s | 1.2629s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x12010041_k05_s01.py` |  |
| 0.14 | 5/35 | 2 | 1.2928s | 0.0439s | 1 | 8 | yes | 1.2660s | 1.3227s | `detyped_files/deltablue/shallow/proportion_sweep/main_0xc008041_k05_s02.py` |  |
| 0.14 | 5/35 | 3 | 1.1149s | 0.0479s | 1 | 8 | yes | 1.0832s | 1.1450s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x40082104_k05_s03.py` |  |
| 0.14 | 5/35 | 4 | 1.7469s | 0.1026s | 1 | 8 | yes | 1.6800s | 1.8144s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x40a000808_k05_s04.py` |  |
| 0.14 | 5/35 | 5 | 1.1592s | 0.1208s | 1 | 8 | yes | 1.0810s | 1.2355s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x50e0000_k05_s05.py` |  |
| 0.14 | 5/35 | 6 | 1.5351s | 0.0822s | 1 | 8 | yes | 1.4798s | 1.5852s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x183004_k05_s06.py` |  |
| 0.14 | 5/35 | 7 | 1.3891s | 0.0768s | 1 | 8 | yes | 1.3379s | 1.4365s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x10040000d_k05_s07.py` |  |
| 0.14 | 5/35 | 8 | 1.7876s | 0.0488s | 1 | 8 | yes | 1.7525s | 1.8152s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x800a18_k05_s08.py` |  |
| 0.14 | 5/35 | 9 | 1.2682s | 0.0658s | 1 | 8 | yes | 1.2272s | 1.3113s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x208441_k05_s09.py` |  |
| 0.14 | 5/35 | 10 | 1.7255s | 0.1134s | 1 | 8 | yes | 1.6551s | 1.8006s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x8100122_k05_s10.py` |  |
| 0.17 | 6/35 | 1 | 1.1560s | 0.0756s | 1 | 8 | yes | 1.1075s | 1.2045s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x70024400_k06_s01.py` |  |
| 0.17 | 6/35 | 2 | 1.8239s | 0.0533s | 1 | 8 | yes | 1.7867s | 1.8570s | `detyped_files/deltablue/shallow/proportion_sweep/main_0xa0900009_k06_s02.py` |  |
| 0.17 | 6/35 | 3 | 1.4766s | 0.0562s | 1 | 8 | yes | 1.4371s | 1.5095s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x22c000012_k06_s03.py` |  |
| 0.17 | 6/35 | 4 | 1.2119s | 0.0923s | 1 | 8 | yes | 1.1499s | 1.2707s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x100483400_k06_s04.py` |  |
| 0.17 | 6/35 | 5 | 1.3777s | 0.1128s | 1 | 8 | yes | 1.3107s | 1.4558s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x10200e002_k06_s05.py` |  |
| 0.17 | 6/35 | 6 | 1.2542s | 0.0865s | 1 | 8 | yes | 1.2094s | 1.3177s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x40814208_k06_s06.py` |  |
| 0.17 | 6/35 | 7 | 1.3020s | 0.0793s | 1 | 8 | yes | 1.2520s | 1.3535s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x258020080_k06_s07.py` |  |
| 0.17 | 6/35 | 8 | 1.7723s | 0.1350s | 1 | 8 | yes | 1.6848s | 1.8573s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x2a00a0800_k06_s08.py` |  |
| 0.17 | 6/35 | 9 | 1.1350s | 0.0726s | 1 | 8 | yes | 1.0950s | 1.1879s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x1018580_k06_s09.py` |  |
| 0.17 | 6/35 | 10 | 1.1980s | 0.0871s | 1 | 8 | yes | 1.1397s | 1.2523s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x810a1010_k06_s10.py` |  |
| 0.20 | 7/35 | 1 | 1.3146s | 0.0418s | 1 | 8 | yes | 1.2864s | 1.3398s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x3a1004100_k07_s01.py` |  |
| 0.20 | 7/35 | 2 | 1.1126s | 0.0754s | 1 | 8 | yes | 1.0625s | 1.1601s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x84048244_k07_s02.py` |  |
| 0.20 | 7/35 | 3 | 1.6667s | 0.0423s | 1 | 8 | yes | 1.6402s | 1.6945s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x50304102_k07_s03.py` |  |
| 0.20 | 7/35 | 4 | 1.6735s | 0.0439s | 1 | 8 | yes | 1.6441s | 1.7007s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x26000c60_k07_s04.py` |  |
| 0.20 | 7/35 | 5 | 1.2792s | 0.0763s | 1 | 8 | yes | 1.2285s | 1.3253s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x216442_k07_s05.py` |  |
| 0.20 | 7/35 | 6 | 1.3405s | 0.0881s | 1 | 8 | yes | 1.2868s | 1.4019s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x341402080_k07_s06.py` |  |
| 0.20 | 7/35 | 7 | 1.9249s | 0.1167s | 1 | 8 | yes | 1.8605s | 2.0086s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x206110011_k07_s07.py` |  |
| 0.20 | 7/35 | 8 | 1.2810s | 0.0618s | 1 | 8 | yes | 1.2399s | 1.3199s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x1020084c1_k07_s08.py` |  |
| 0.20 | 7/35 | 9 | 1.2501s | 0.0993s | 1 | 8 | yes | 1.1843s | 1.3126s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x2080a4120_k07_s09.py` |  |
| 0.20 | 7/35 | 10 | 1.3009s | 0.0768s | 1 | 8 | yes | 1.2519s | 1.3530s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x20a024210_k07_s10.py` |  |
| 0.23 | 8/35 | 1 | 1.7436s | 0.0387s | 1 | 8 | yes | 1.7258s | 1.7717s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x20a802904_k08_s01.py` |  |
| 0.23 | 8/35 | 2 | 1.3371s | 0.0778s | 1 | 8 | yes | 1.2866s | 1.3862s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x718084010_k08_s02.py` |  |
| 0.23 | 8/35 | 3 | 1.1919s | 0.0666s | 1 | 8 | yes | 1.1482s | 1.2344s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x36c0028_k08_s03.py` |  |
| 0.23 | 8/35 | 4 | 1.8650s | 0.0863s | 1 | 8 | yes | 1.8098s | 1.9191s | `detyped_files/deltablue/shallow/proportion_sweep/main_0xa0404a09_k08_s04.py` |  |
| 0.23 | 8/35 | 5 | 1.2790s | 0.0706s | 1 | 8 | yes | 1.2368s | 1.3279s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x2c2005024_k08_s05.py` |  |
| 0.23 | 8/35 | 6 | 1.7354s | 0.0905s | 1 | 8 | yes | 1.6760s | 1.7926s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x133800810_k08_s06.py` |  |
| 0.23 | 8/35 | 7 | 1.1585s | 0.0845s | 1 | 8 | yes | 1.1051s | 1.2151s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x1a06800a0_k08_s07.py` |  |
| 0.23 | 8/35 | 8 | 1.4052s | 0.0387s | 1 | 8 | yes | 1.3805s | 1.4299s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x48080142a_k08_s08.py` |  |
| 0.23 | 8/35 | 9 | 1.4520s | 0.0313s | 1 | 8 | yes | 1.4336s | 1.4739s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x203210051_k08_s09.py` |  |
| 0.23 | 8/35 | 10 | 1.2394s | 0.0511s | 1 | 8 | yes | 1.2073s | 1.2730s | `detyped_files/deltablue/shallow/proportion_sweep/main_0xa524000c_k08_s10.py` |  |
| 0.26 | 9/35 | 1 | 1.2136s | 0.0845s | 1 | 8 | yes | 1.1640s | 1.2722s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x401299208_k09_s01.py` |  |
| 0.26 | 9/35 | 2 | 2.0122s | 0.0462s | 1 | 8 | yes | 1.9824s | 2.0420s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x2c000a80e_k09_s02.py` |  |
| 0.26 | 9/35 | 3 | 1.7961s | 0.1216s | 1 | 8 | yes | 1.7223s | 1.8804s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x1834500a_k09_s03.py` |  |
| 0.26 | 9/35 | 4 | 2.2002s | 0.0628s | 1 | 8 | yes | 2.1560s | 2.2370s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x190b86_k09_s04.py` |  |
| 0.26 | 9/35 | 5 | 1.8285s | 0.0782s | 1 | 8 | yes | 1.7757s | 1.8760s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x430a01902_k09_s05.py` |  |
| 0.26 | 9/35 | 6 | 1.3349s | 0.0745s | 1 | 8 | yes | 1.2868s | 1.3855s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x1112280c2_k09_s06.py` |  |
| 0.26 | 9/35 | 7 | 1.4308s | 0.0553s | 1 | 8 | yes | 1.3939s | 1.4661s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x265014011_k09_s07.py` |  |
| 0.26 | 9/35 | 8 | 2.0058s | 0.0828s | 1 | 8 | yes | 1.9506s | 2.0577s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x2c8400807_k09_s08.py` |  |
| 0.26 | 9/35 | 9 | 1.9966s | 0.1189s | 1 | 8 | yes | 1.9180s | 2.0722s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x210048869_k09_s09.py` |  |
| 0.26 | 9/35 | 10 | 1.8631s | 0.1225s | 1 | 8 | yes | 1.7866s | 1.9444s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x407110083_k09_s10.py` |  |
| 0.29 | 10/35 | 1 | 1.1734s | 0.0421s | 1 | 8 | yes | 1.1440s | 1.1977s | `detyped_files/deltablue/shallow/proportion_sweep/main_0xe08a4214_k10_s01.py` |  |
| 0.29 | 10/35 | 2 | 1.5906s | 0.0387s | 1 | 8 | yes | 1.5665s | 1.6167s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x596188040_k10_s02.py` |  |
| 0.29 | 10/35 | 3 | 1.8621s | 0.0954s | 1 | 8 | yes | 1.8037s | 1.9289s | `detyped_files/deltablue/shallow/proportion_sweep/main_0xa3280a3_k10_s03.py` |  |
| 0.29 | 10/35 | 4 | 1.8406s | 0.0792s | 1 | 8 | yes | 1.7874s | 1.8922s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x90c04b82_k10_s04.py` |  |
| 0.29 | 10/35 | 5 | 1.2898s | 0.0455s | 1 | 8 | yes | 1.2585s | 1.3165s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x650a81024_k10_s05.py` |  |
| 0.29 | 10/35 | 6 | 1.8919s | 0.0744s | 1 | 8 | yes | 1.8497s | 1.9438s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x212282885_k10_s06.py` |  |
| 0.29 | 10/35 | 7 | 1.4257s | 0.0654s | 1 | 8 | yes | 1.3802s | 1.4631s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x540034423_k10_s07.py` |  |
| 0.29 | 10/35 | 8 | 2.0927s | 0.0501s | 1 | 8 | yes | 2.0686s | 2.1297s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x110b44b00_k10_s08.py` |  |
| 0.29 | 10/35 | 9 | 1.5968s | 0.0677s | 1 | 8 | yes | 1.5548s | 1.6419s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x8051b610_k10_s09.py` |  |
| 0.29 | 10/35 | 10 | 1.2623s | 0.0351s | 1 | 8 | yes | 1.2422s | 1.2871s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x28876408_k10_s10.py` |  |
| 0.31 | 11/35 | 1 | 1.2830s | 0.0760s | 1 | 8 | yes | 1.2323s | 1.3300s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x106254681_k11_s01.py` |  |
| 0.31 | 11/35 | 2 | 1.4796s | 0.0865s | 1 | 8 | yes | 1.4269s | 1.5381s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x41224068b_k11_s02.py` |  |
| 0.31 | 11/35 | 3 | 1.6742s | 0.0784s | 1 | 8 | yes | 1.6251s | 1.7260s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x10c08dd4_k11_s03.py` |  |
| 0.31 | 11/35 | 4 | 1.2498s | 0.0861s | 1 | 8 | yes | 1.2041s | 1.3128s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x68024d604_k11_s04.py` |  |
| 0.31 | 11/35 | 5 | 1.4155s | 0.0525s | 1 | 8 | yes | 1.3805s | 1.4489s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x9807343_k11_s05.py` |  |
| 0.31 | 11/35 | 6 | 1.8916s | 0.0357s | 1 | 8 | yes | 1.8685s | 1.9148s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x27006b12_k11_s06.py` |  |
| 0.31 | 11/35 | 7 | 1.5950s | 0.0598s | 1 | 8 | yes | 1.5549s | 1.6321s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x8e11c310_k11_s07.py` |  |
| 0.31 | 11/35 | 8 | 1.4299s | 0.0389s | 1 | 8 | yes | 1.4031s | 1.4532s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x60d836001_k11_s08.py` |  |
| 0.31 | 11/35 | 9 | 1.2777s | 0.0543s | 1 | 8 | yes | 1.2393s | 1.3092s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x1d90a0045_k11_s09.py` |  |
| 0.31 | 11/35 | 10 | 1.7116s | 0.0753s | 1 | 8 | yes | 1.6611s | 1.7579s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x20a78a28_k11_s10.py` |  |
| 0.34 | 12/35 | 1 | 1.1211s | 0.0668s | 1 | 8 | yes | 1.0809s | 1.1669s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x12e071284_k12_s01.py` |  |
| 0.34 | 12/35 | 2 | 1.3454s | 0.0800s | 1 | 8 | yes | 1.2967s | 1.4007s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x258805b5_k12_s02.py` |  |
| 0.34 | 12/35 | 3 | 2.0552s | 0.0863s | 1 | 8 | yes | 1.9960s | 2.1082s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x91752c20_k12_s03.py` |  |
| 0.34 | 12/35 | 4 | 1.4726s | 0.0987s | 1 | 8 | yes | 1.4063s | 1.5348s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x655890421_k12_s04.py` |  |
| 0.34 | 12/35 | 5 | 1.8165s | 0.1126s | 1 | 8 | yes | 1.7474s | 1.8929s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x42101f942_k12_s05.py` |  |
| 0.34 | 12/35 | 6 | 1.7378s | 0.0649s | 1 | 8 | yes | 1.6944s | 1.7776s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x2813170c8_k12_s06.py` |  |
| 0.34 | 12/35 | 7 | 1.2203s | 0.0610s | 1 | 8 | yes | 1.1851s | 1.2639s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x16c293030_k12_s07.py` |  |
| 0.34 | 12/35 | 8 | 1.6283s | 0.0664s | 1 | 8 | yes | 1.5878s | 1.6747s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x231b11c8_k12_s08.py` |  |
| 0.34 | 12/35 | 9 | 1.6640s | 0.0963s | 1 | 8 | yes | 1.6076s | 1.7324s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x138309074_k12_s09.py` |  |
| 0.34 | 12/35 | 10 | 1.3000s | 0.0674s | 1 | 8 | yes | 1.2541s | 1.3428s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x203a22760_k12_s10.py` |  |
| 0.37 | 13/35 | 1 | 1.8444s | 0.1237s | 1 | 8 | yes | 1.7724s | 1.9293s | `detyped_files/deltablue/shallow/proportion_sweep/main_0xa1d830c9_k13_s01.py` |  |
| 0.37 | 13/35 | 2 | 1.5706s | 0.0892s | 1 | 8 | yes | 1.5096s | 1.6258s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x13e412213_k13_s02.py` |  |
| 0.37 | 13/35 | 3 | 1.8026s | 0.0998s | 1 | 8 | yes | 1.7403s | 1.8677s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x282c30b54_k13_s03.py` |  |
| 0.37 | 13/35 | 4 | 1.5697s | 0.0971s | 1 | 8 | yes | 1.5077s | 1.6343s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x4a9390360_k13_s04.py` |  |
| 0.37 | 13/35 | 5 | 2.1959s | 0.1122s | 1 | 8 | yes | 2.1263s | 2.2700s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x1d2108b91_k13_s05.py` |  |
| 0.37 | 13/35 | 6 | 1.9695s | 0.1122s | 1 | 8 | yes | 1.9163s | 2.0495s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x22d0afa_k13_s06.py` |  |
| 0.37 | 13/35 | 7 | 1.3485s | 0.0616s | 1 | 8 | yes | 1.3114s | 1.3904s | `detyped_files/deltablue/shallow/proportion_sweep/main_0xe6890638_k13_s07.py` |  |
| 0.37 | 13/35 | 8 | 1.4994s | 0.0699s | 1 | 8 | yes | 1.4596s | 1.5496s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x71d05d001_k13_s08.py` |  |
| 0.37 | 13/35 | 9 | 1.4623s | 0.0635s | 1 | 8 | yes | 1.4209s | 1.5045s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x23d00b08d_k13_s09.py` |  |
| 0.37 | 13/35 | 10 | 1.8773s | 0.1223s | 1 | 8 | yes | 1.8052s | 1.9622s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x792cc2808_k13_s10.py` |  |
| 0.40 | 14/35 | 1 | 2.2468s | 0.1007s | 1 | 8 | yes | 2.1888s | 2.3172s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x2117c8d82_k14_s01.py` |  |
| 0.40 | 14/35 | 2 | 1.3149s | 0.1206s | 1 | 8 | yes | 1.2429s | 1.3961s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x632185dc_k14_s02.py` |  |
| 0.40 | 14/35 | 3 | 2.2032s | 0.1334s | 1 | 8 | yes | 2.1183s | 2.2866s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x1187519c8_k14_s03.py` |  |
| 0.40 | 14/35 | 4 | 2.0339s | 0.0791s | 1 | 8 | yes | 1.9839s | 2.0851s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x503095c3a_k14_s04.py` |  |
| 0.40 | 14/35 | 5 | 1.9474s | 0.1030s | 1 | 8 | yes | 1.8869s | 2.0197s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x1ee003907_k14_s05.py` |  |
| 0.40 | 14/35 | 6 | 1.9332s | 0.0825s | 1 | 8 | yes | 1.8823s | 1.9896s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x74c44a886_k14_s06.py` |  |
| 0.40 | 14/35 | 7 | 1.3813s | 0.0486s | 1 | 8 | yes | 1.3475s | 1.4097s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x13c0d1692_k14_s07.py` |  |
| 0.40 | 14/35 | 8 | 1.4363s | 0.0829s | 1 | 8 | yes | 1.3815s | 1.4876s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x2cb8ca026_k14_s08.py` |  |
| 0.40 | 14/35 | 9 | 1.4783s | 0.1523s | 1 | 8 | yes | 1.3947s | 1.5888s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x6406707a1_k14_s09.py` |  |
| 0.40 | 14/35 | 10 | 1.8045s | 0.0597s | 1 | 8 | yes | 1.7635s | 1.8396s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x3bccc1900_k14_s10.py` |  |
| 0.43 | 15/35 | 1 | 1.3022s | 0.0784s | 1 | 8 | yes | 1.2572s | 1.3580s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x6ee8930c_k15_s01.py` |  |
| 0.43 | 15/35 | 2 | 2.0054s | 0.1412s | 1 | 8 | yes | 1.9217s | 2.1017s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x273686c0a_k15_s02.py` |  |
| 0.43 | 15/35 | 3 | 1.7957s | 0.0949s | 1 | 8 | yes | 1.7370s | 1.8576s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x370db7100_k15_s03.py` |  |
| 0.43 | 15/35 | 4 | 1.7911s | 0.0840s | 1 | 8 | yes | 1.7361s | 1.8440s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x644dcb190_k15_s04.py` |  |
| 0.43 | 15/35 | 5 | 2.1569s | 0.1188s | 1 | 8 | yes | 2.0895s | 2.2405s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x6945e040f_k15_s05.py` |  |
| 0.43 | 15/35 | 6 | 2.0262s | 0.0873s | 1 | 8 | yes | 1.9701s | 2.0826s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x2c190f0da_k15_s06.py` |  |
| 0.43 | 15/35 | 7 | 1.3307s | 0.0922s | 1 | 8 | yes | 1.2686s | 1.3876s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x4bd6a0451_k15_s07.py` |  |
| 0.43 | 15/35 | 8 | 2.3040s | 0.0955s | 1 | 8 | yes | 2.2436s | 2.3670s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x518580b5d_k15_s08.py` |  |
| 0.43 | 15/35 | 9 | 1.7728s | 0.0286s | 1 | 8 | yes | 1.7559s | 1.7925s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7a148849b_k15_s09.py` |  |
| 0.43 | 15/35 | 10 | 1.2706s | 0.0880s | 1 | 8 | yes | 1.2155s | 1.3290s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x2552de680_k15_s10.py` |  |
| 0.46 | 16/35 | 1 | 1.5605s | 0.0598s | 1 | 8 | yes | 1.5265s | 1.6022s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x614c96569_k16_s01.py` |  |
| 0.46 | 16/35 | 2 | 2.1983s | 0.0525s | 1 | 8 | yes | 2.1632s | 2.2298s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x749cbb42_k16_s02.py` |  |
| 0.46 | 16/35 | 3 | 2.1415s | 0.0820s | 1 | 8 | yes | 2.0882s | 2.1952s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x75c98410f_k16_s03.py` |  |
| 0.46 | 16/35 | 4 | 2.1721s | 0.0708s | 1 | 8 | yes | 2.1262s | 2.2164s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x385d56a24_k16_s04.py` |  |
| 0.46 | 16/35 | 5 | 1.9136s | 0.0479s | 1 | 8 | yes | 1.8798s | 1.9425s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x216cc7d22_k16_s05.py` |  |
| 0.46 | 16/35 | 6 | 1.3054s | 0.0823s | 1 | 8 | yes | 1.2513s | 1.3570s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x46f42869c_k16_s06.py` |  |
| 0.46 | 16/35 | 7 | 1.4138s | 0.0776s | 1 | 8 | yes | 1.3622s | 1.4633s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x21985b785_k16_s07.py` |  |
| 0.46 | 16/35 | 8 | 1.9884s | 0.0694s | 1 | 8 | yes | 1.9447s | 2.0342s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x21dce988a_k16_s08.py` |  |
| 0.46 | 16/35 | 9 | 1.7406s | 0.0930s | 1 | 8 | yes | 1.6818s | 1.8024s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x18f527582_k16_s09.py` |  |
| 0.46 | 16/35 | 10 | 1.4136s | 0.0848s | 1 | 8 | yes | 1.3585s | 1.4673s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x4f786050e_k16_s10.py` |  |
| 0.49 | 17/35 | 1 | 1.4910s | 0.0935s | 1 | 8 | yes | 1.4298s | 1.5509s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x61d8ba551_k17_s01.py` |  |
| 0.49 | 17/35 | 2 | 1.8792s | 0.0965s | 1 | 8 | yes | 1.8165s | 1.9406s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x55a78252e_k17_s02.py` |  |
| 0.49 | 17/35 | 3 | 1.4342s | 0.0474s | 1 | 8 | yes | 1.4056s | 1.4666s | `detyped_files/deltablue/shallow/proportion_sweep/main_0xf0a2b71d_k17_s03.py` |  |
| 0.49 | 17/35 | 4 | 1.3261s | 0.0684s | 1 | 8 | yes | 1.2816s | 1.3690s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x13c0f9556_k17_s04.py` |  |
| 0.49 | 17/35 | 5 | 2.3774s | 0.0507s | 1 | 8 | yes | 2.3440s | 2.4096s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x41096db4f_k17_s05.py` |  |
| 0.49 | 17/35 | 6 | 2.2654s | 0.0658s | 1 | 8 | yes | 2.2227s | 2.3069s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x134bc9e62_k17_s06.py` |  |
| 0.49 | 17/35 | 7 | 2.0725s | 0.0754s | 1 | 8 | yes | 2.0253s | 2.1252s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x704afe82a_k17_s07.py` |  |
| 0.49 | 17/35 | 8 | 1.9773s | 0.0802s | 1 | 8 | yes | 1.9255s | 2.0274s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x1cdc48cce_k17_s08.py` |  |
| 0.49 | 17/35 | 9 | 1.3875s | 0.1183s | 1 | 8 | yes | 1.3156s | 1.4691s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x277c713c0_k17_s09.py` |  |
| 0.49 | 17/35 | 10 | 1.8668s | 0.1366s | 1 | 8 | yes | 1.7812s | 1.9561s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x3d765299_k17_s10.py` |  |
| 0.51 | 18/35 | 1 | 2.1423s | 0.1190s | 1 | 8 | yes | 2.0665s | 2.2208s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x3358eaa3a_k18_s01.py` |  |
| 0.51 | 18/35 | 2 | 2.2063s | 0.0685s | 1 | 8 | yes | 2.1581s | 2.2477s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x2e5915f2c_k18_s02.py` |  |
| 0.51 | 18/35 | 3 | 2.3857s | 0.0871s | 1 | 8 | yes | 2.3266s | 2.4389s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x8755cb37_k18_s03.py` |  |
| 0.51 | 18/35 | 4 | 2.2292s | 0.0650s | 1 | 8 | yes | 2.1881s | 2.2716s | `detyped_files/deltablue/shallow/proportion_sweep/main_0xf49c5cb5_k18_s04.py` |  |
| 0.51 | 18/35 | 5 | 2.2370s | 0.0853s | 1 | 8 | yes | 2.1856s | 2.2946s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x6a6bec846_k18_s05.py` |  |
| 0.51 | 18/35 | 6 | 2.2033s | 0.0819s | 1 | 8 | yes | 2.1530s | 2.2588s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x3012f0fdb_k18_s06.py` |  |
| 0.51 | 18/35 | 7 | 1.4825s | 0.1043s | 1 | 8 | yes | 1.4171s | 1.5526s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x17d435339_k18_s07.py` |  |
| 0.51 | 18/35 | 8 | 2.0741s | 0.0828s | 1 | 8 | yes | 2.0229s | 2.1293s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x6e2c8bc47_k18_s08.py` |  |
| 0.51 | 18/35 | 9 | 1.9535s | 0.0622s | 1 | 8 | yes | 1.9096s | 1.9892s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x29e18dfe_k18_s09.py` |  |
| 0.51 | 18/35 | 10 | 2.5332s | 0.1689s | 1 | 8 | yes | 2.4268s | 2.6427s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x51a5459cf_k18_s10.py` |  |
| 0.54 | 19/35 | 1 | 1.6119s | 0.0914s | 1 | 8 | yes | 1.5530s | 1.6703s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7cd8585c7_k19_s01.py` |  |
| 0.54 | 19/35 | 2 | 2.2507s | 0.0389s | 1 | 8 | yes | 2.2244s | 2.2745s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x4cb73da32_k19_s02.py` |  |
| 0.54 | 19/35 | 3 | 2.1228s | 0.1060s | 1 | 8 | yes | 2.0546s | 2.1888s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x5a1eea86b_k19_s03.py` |  |
| 0.54 | 19/35 | 4 | 2.3869s | 0.1403s | 1 | 8 | yes | 2.3058s | 2.4815s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x1a398daf9_k19_s04.py` |  |
| 0.54 | 19/35 | 5 | 1.4411s | 0.1410s | 1 | 8 | yes | 1.3644s | 1.5434s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x5bee483a9_k19_s05.py` |  |
| 0.54 | 19/35 | 6 | 1.7688s | 0.0755s | 1 | 8 | yes | 1.7216s | 1.8188s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x237e3e9e0_k19_s06.py` |  |
| 0.54 | 19/35 | 7 | 1.9218s | 0.0707s | 1 | 8 | yes | 1.8754s | 1.9675s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x1192fbf83_k19_s07.py` |  |
| 0.54 | 19/35 | 8 | 1.7613s | 0.0779s | 1 | 8 | yes | 1.7104s | 1.8111s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x26f576730_k19_s08.py` |  |
| 0.54 | 19/35 | 9 | 2.3609s | 0.0552s | 1 | 8 | yes | 2.3313s | 2.4009s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x50a7c9cbd_k19_s09.py` |  |
| 0.54 | 19/35 | 10 | 1.7185s | 0.0645s | 1 | 8 | yes | 1.6787s | 1.7614s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x1f69535b8_k19_s10.py` |  |
| 0.57 | 20/35 | 1 | 2.0015s | 0.0811s | 1 | 8 | yes | 1.9498s | 2.0545s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x595a17b3e_k20_s01.py` |  |
| 0.57 | 20/35 | 2 | 1.4933s | 0.0598s | 1 | 8 | yes | 1.4505s | 1.5253s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x5faa73623_k20_s02.py` |  |
| 0.57 | 20/35 | 3 | 2.2897s | 0.1018s | 1 | 8 | yes | 2.2241s | 2.3569s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x776b6de08_k20_s03.py` |  |
| 0.57 | 20/35 | 4 | 1.9610s | 0.0826s | 1 | 8 | yes | 1.9117s | 2.0177s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x1a92e4fde_k20_s04.py` |  |
| 0.57 | 20/35 | 5 | 1.9625s | 0.1462s | 1 | 8 | yes | 1.8762s | 2.0684s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7a2b3f42d_k20_s05.py` |  |
| 0.57 | 20/35 | 6 | 1.6104s | 0.1402s | 1 | 8 | yes | 1.5279s | 1.7075s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x3894bf36d_k20_s06.py` |  |
| 0.57 | 20/35 | 7 | 2.4994s | 0.0718s | 1 | 8 | yes | 2.4543s | 2.5464s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x36db3b94a_k20_s07.py` |  |
| 0.57 | 20/35 | 8 | 2.1135s | 0.0903s | 1 | 8 | yes | 2.0615s | 2.1752s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7ea38e0eb_k20_s08.py` |  |
| 0.57 | 20/35 | 9 | 2.0508s | 0.1199s | 1 | 8 | yes | 1.9758s | 2.1327s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7f222cbb9_k20_s09.py` |  |
| 0.57 | 20/35 | 10 | 1.7938s | 0.1073s | 1 | 8 | yes | 1.7339s | 1.8720s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x5355c57b5_k20_s10.py` |  |
| 0.60 | 21/35 | 1 | 1.8540s | 0.0791s | 1 | 8 | yes | 1.7996s | 1.9020s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x1aee6bfa1_k21_s01.py` |  |
| 0.60 | 21/35 | 2 | 2.4462s | 0.1552s | 1 | 8 | yes | 2.3577s | 2.5527s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x41e9d6f97_k21_s02.py` |  |
| 0.60 | 21/35 | 3 | 2.0783s | 0.0566s | 1 | 8 | yes | 2.0379s | 2.1112s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x65c8bfd93_k21_s03.py` |  |
| 0.60 | 21/35 | 4 | 2.3707s | 0.0735s | 1 | 8 | yes | 2.3219s | 2.4151s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x156396fd7_k21_s04.py` |  |
| 0.60 | 21/35 | 5 | 2.3566s | 0.0730s | 1 | 8 | yes | 2.3082s | 2.4017s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x74cb57d35_k21_s05.py` |  |
| 0.60 | 21/35 | 6 | 2.5208s | 0.0843s | 1 | 8 | yes | 2.4631s | 2.5715s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x627f69cab_k21_s06.py` |  |
| 0.60 | 21/35 | 7 | 1.6302s | 0.0649s | 1 | 8 | yes | 1.5844s | 1.6660s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x4facb171f_k21_s07.py` |  |
| 0.60 | 21/35 | 8 | 1.9763s | 0.0710s | 1 | 8 | yes | 1.9293s | 2.0202s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x2dd9fe2aa_k21_s08.py` |  |
| 0.60 | 21/35 | 9 | 2.0448s | 0.0987s | 1 | 8 | yes | 1.9789s | 2.1075s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7d174e3e3_k21_s09.py` |  |
| 0.60 | 21/35 | 10 | 1.9937s | 0.0687s | 1 | 8 | yes | 1.9493s | 2.0373s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7539a63f9_k21_s10.py` |  |
| 0.63 | 22/35 | 1 | 2.1689s | 0.0826s | 1 | 8 | yes | 2.1171s | 2.2242s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x62ddaf4bb_k22_s01.py` |  |
| 0.63 | 22/35 | 2 | 2.4213s | 0.1087s | 1 | 8 | yes | 2.3509s | 2.4901s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x6689e3efd_k22_s02.py` |  |
| 0.63 | 22/35 | 3 | 2.3704s | 0.0861s | 1 | 8 | yes | 2.3138s | 2.4241s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x53e79ced9_k22_s03.py` |  |
| 0.63 | 22/35 | 4 | 2.2155s | 0.0810s | 1 | 8 | yes | 2.1616s | 2.2661s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x737d9333b_k22_s04.py` |  |
| 0.63 | 22/35 | 5 | 1.9874s | 0.0733s | 1 | 8 | yes | 1.9386s | 2.0318s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x1bcf5c2f7_k22_s05.py` |  |
| 0.63 | 22/35 | 6 | 1.6370s | 0.1009s | 1 | 8 | yes | 1.5776s | 1.7063s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x673e795c7_k22_s06.py` |  |
| 0.63 | 22/35 | 7 | 1.5858s | 0.0787s | 1 | 8 | yes | 1.5363s | 1.6383s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x73ce3e367_k22_s07.py` |  |
| 0.63 | 22/35 | 8 | 1.8052s | 0.1205s | 1 | 8 | yes | 1.7318s | 1.8884s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x4b7df22ed_k22_s08.py` |  |
| 0.63 | 22/35 | 9 | 2.2304s | 0.0599s | 1 | 8 | yes | 2.1957s | 2.2726s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x697ed98bb_k22_s09.py` |  |
| 0.63 | 22/35 | 10 | 1.8741s | 0.1030s | 1 | 8 | yes | 1.8100s | 1.9449s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x2cfbbe55c_k22_s10.py` |  |
| 0.66 | 23/35 | 1 | 2.2228s | 0.1065s | 1 | 8 | yes | 2.1616s | 2.2967s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x3a9afc9df_k23_s01.py` |  |
| 0.66 | 23/35 | 2 | 2.1705s | 0.0961s | 1 | 8 | yes | 2.1163s | 2.2377s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x67b4f1e3f_k23_s02.py` |  |
| 0.66 | 23/35 | 3 | 1.6710s | 0.0849s | 1 | 8 | yes | 1.6176s | 1.7241s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x73badf693_k23_s03.py` |  |
| 0.66 | 23/35 | 4 | 2.4253s | 0.0942s | 1 | 8 | yes | 2.3663s | 2.4869s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x1d4d71ff7_k23_s04.py` |  |
| 0.66 | 23/35 | 5 | 1.8968s | 0.0947s | 1 | 8 | yes | 1.8343s | 1.9552s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x73bacdcfc_k23_s05.py` |  |
| 0.66 | 23/35 | 6 | 2.3775s | 0.0398s | 1 | 8 | yes | 2.3523s | 2.4037s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x5b651edfe_k23_s06.py` |  |
| 0.66 | 23/35 | 7 | 2.1045s | 0.0819s | 1 | 8 | yes | 2.0545s | 2.1612s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x3f7f6d519_k23_s07.py` |  |
| 0.66 | 23/35 | 8 | 2.1056s | 0.0803s | 1 | 8 | yes | 2.0549s | 2.1592s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x74a6dbe77_k23_s08.py` |  |
| 0.66 | 23/35 | 9 | 2.3976s | 0.0831s | 1 | 8 | yes | 2.3454s | 2.4506s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7da7b8ea7_k23_s09.py` |  |
| 0.66 | 23/35 | 10 | 2.3968s | 0.1085s | 1 | 8 | yes | 2.3242s | 2.4660s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x571facf5d_k23_s10.py` |  |
| 0.69 | 24/35 | 1 | 2.5116s | 0.0469s | 1 | 8 | yes | 2.4802s | 2.5415s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x6757a7f8f_k24_s01.py` |  |
| 0.69 | 24/35 | 2 | 1.9672s | 0.0856s | 1 | 8 | yes | 1.9155s | 2.0263s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x5bbcbf8f6_k24_s02.py` |  |
| 0.69 | 24/35 | 3 | 2.4427s | 0.0740s | 1 | 8 | yes | 2.3923s | 2.4885s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x3fbb5fb2a_k24_s03.py` |  |
| 0.69 | 24/35 | 4 | 2.5039s | 0.0592s | 1 | 8 | yes | 2.4658s | 2.5428s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x3ee93cfaf_k24_s04.py` |  |
| 0.69 | 24/35 | 5 | 2.0332s | 0.0683s | 1 | 8 | yes | 1.9911s | 2.0783s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x4fe8e5f5f_k24_s05.py` |  |
| 0.69 | 24/35 | 6 | 2.0202s | 0.0520s | 1 | 8 | yes | 1.9896s | 2.0565s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x5cb2e3ff7_k24_s06.py` |  |
| 0.69 | 24/35 | 7 | 1.9869s | 0.0624s | 1 | 8 | yes | 1.9466s | 2.0267s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x2ebbdf2dd_k24_s07.py` |  |
| 0.69 | 24/35 | 8 | 1.9866s | 0.0444s | 1 | 8 | yes | 1.9593s | 2.0162s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x17e75f78f_k24_s08.py` |  |
| 0.69 | 24/35 | 9 | 2.0024s | 0.1262s | 1 | 8 | yes | 1.9282s | 2.0886s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x59f3b31ff_k24_s09.py` |  |
| 0.69 | 24/35 | 10 | 2.4567s | 0.0836s | 1 | 8 | yes | 2.4069s | 2.5140s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7ac597dfe_k24_s10.py` |  |
| 0.71 | 25/35 | 1 | 2.3014s | 0.1296s | 1 | 8 | yes | 2.2226s | 2.3888s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x5ffd97dd2_k25_s01.py` |  |
| 0.71 | 25/35 | 2 | 2.1910s | 0.0577s | 1 | 8 | yes | 2.1542s | 2.2290s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7b7a9ef5b_k25_s02.py` |  |
| 0.71 | 25/35 | 3 | 2.3909s | 0.0604s | 1 | 8 | yes | 2.3491s | 2.4266s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x67f7cfd1e_k25_s03.py` |  |
| 0.71 | 25/35 | 4 | 2.4754s | 0.0903s | 1 | 8 | yes | 2.4097s | 2.5249s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x5c5fd5fcf_k25_s04.py` |  |
| 0.71 | 25/35 | 5 | 2.5081s | 0.1431s | 1 | 8 | yes | 2.4170s | 2.6036s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7777f19b7_k25_s05.py` |  |
| 0.71 | 25/35 | 6 | 2.4834s | 0.0576s | 1 | 8 | yes | 2.4413s | 2.5152s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x67d5e5eef_k25_s06.py` |  |
| 0.71 | 25/35 | 7 | 2.5750s | 0.1604s | 1 | 8 | yes | 2.4808s | 2.6888s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x47ef1e9ff_k25_s07.py` |  |
| 0.71 | 25/35 | 8 | 2.2408s | 0.0556s | 1 | 8 | yes | 2.2079s | 2.2800s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x737a6aeff_k25_s08.py` |  |
| 0.71 | 25/35 | 9 | 2.2149s | 0.0965s | 1 | 8 | yes | 2.1565s | 2.2797s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x6da3ffdd5_k25_s09.py` |  |
| 0.71 | 25/35 | 10 | 2.4935s | 0.0586s | 1 | 8 | yes | 2.4605s | 2.5352s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7d6f9eed9_k25_s10.py` |  |
| 0.74 | 26/35 | 1 | 2.5307s | 0.1364s | 1 | 8 | yes | 2.4434s | 2.6173s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x6fff26dfa_k26_s01.py` |  |
| 0.74 | 26/35 | 2 | 2.2785s | 0.1205s | 1 | 8 | yes | 2.1998s | 2.3569s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x5e9be7ff5_k26_s02.py` |  |
| 0.74 | 26/35 | 3 | 2.1499s | 0.0483s | 1 | 8 | yes | 2.1176s | 2.1794s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x3fafbf38f_k26_s03.py` |  |
| 0.74 | 26/35 | 4 | 1.6866s | 0.0686s | 1 | 8 | yes | 1.6430s | 1.7326s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x75f2df3bf_k26_s04.py` |  |
| 0.74 | 26/35 | 5 | 2.1423s | 0.0887s | 1 | 8 | yes | 2.0861s | 2.1995s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x76bebbf8f_k26_s05.py` |  |
| 0.74 | 26/35 | 6 | 2.3726s | 0.0362s | 1 | 8 | yes | 2.3483s | 2.3945s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7feff6d51_k26_s06.py` |  |
| 0.74 | 26/35 | 7 | 2.2632s | 0.1307s | 1 | 8 | yes | 2.1825s | 2.3556s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x37eefaddb_k26_s07.py` |  |
| 0.74 | 26/35 | 8 | 2.0746s | 0.0467s | 1 | 8 | yes | 2.0448s | 2.1059s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7ffe5fa59_k26_s08.py` |  |
| 0.74 | 26/35 | 9 | 2.5079s | 0.1419s | 1 | 8 | yes | 2.4220s | 2.6049s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7753ffe37_k26_s09.py` |  |
| 0.74 | 26/35 | 10 | 2.5332s | 0.1142s | 1 | 8 | yes | 2.4588s | 2.6042s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x3ddf3ddb7_k26_s10.py` |  |
| 0.77 | 27/35 | 1 | 1.7038s | 0.0964s | 1 | 8 | yes | 1.6411s | 1.7638s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x6fbafb3df_k27_s01.py` |  |
| 0.77 | 27/35 | 2 | 2.3680s | 0.0582s | 1 | 8 | yes | 2.3263s | 2.3989s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7bef73df5_k27_s02.py` |  |
| 0.77 | 27/35 | 3 | 2.5494s | 0.0921s | 1 | 8 | yes | 2.4921s | 2.6110s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7bfd5abef_k27_s03.py` |  |
| 0.77 | 27/35 | 4 | 2.6182s | 0.0883s | 1 | 8 | yes | 2.5588s | 2.6706s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x79dffdf1b_k27_s04.py` |  |
| 0.77 | 27/35 | 5 | 2.1980s | 0.0388s | 1 | 8 | yes | 2.1733s | 2.2232s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7b8fff5af_k27_s05.py` |  |
| 0.77 | 27/35 | 6 | 2.4173s | 0.0964s | 1 | 8 | yes | 2.3578s | 2.4838s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x6fbbd7cfd_k27_s06.py` |  |
| 0.77 | 27/35 | 7 | 2.0844s | 0.1289s | 1 | 8 | yes | 2.0063s | 2.1716s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x6ebe6fbfe_k27_s07.py` |  |
| 0.77 | 27/35 | 8 | 2.0904s | 0.0738s | 1 | 8 | yes | 2.0455s | 2.1422s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7ed6ff8fe_k27_s08.py` |  |
| 0.77 | 27/35 | 9 | 1.9731s | 0.1041s | 1 | 8 | yes | 1.9049s | 2.0401s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x65f7bf3fd_k27_s09.py` |  |
| 0.77 | 27/35 | 10 | 2.5921s | 0.0908s | 1 | 8 | yes | 2.5325s | 2.6492s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x2f6fb6ffb_k27_s10.py` |  |
| 0.80 | 28/35 | 1 | 2.4103s | 0.0752s | 1 | 8 | yes | 2.3623s | 2.4600s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x79bfdff6d_k28_s01.py` |  |
| 0.80 | 28/35 | 2 | 2.5152s | 0.1562s | 1 | 8 | yes | 2.4239s | 2.6255s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7ceff9ff9_k28_s02.py` |  |
| 0.80 | 28/35 | 3 | 2.5131s | 0.0666s | 1 | 8 | yes | 2.4681s | 2.5546s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x65dfaffef_k28_s03.py` |  |
| 0.80 | 28/35 | 4 | 2.3999s | 0.0808s | 1 | 8 | yes | 2.3440s | 2.4494s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7fb7dbf3d_k28_s04.py` |  |
| 0.80 | 28/35 | 5 | 2.2212s | 0.1099s | 1 | 8 | yes | 2.1648s | 2.3015s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7ff68fd7f_k28_s05.py` |  |
| 0.80 | 28/35 | 6 | 1.8910s | 0.0699s | 1 | 8 | yes | 1.8466s | 1.9381s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x6fffff695_k28_s06.py` |  |
| 0.80 | 28/35 | 7 | 1.5727s | 0.0976s | 1 | 8 | yes | 1.5159s | 1.6394s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7f6cff7f6_k28_s07.py` |  |
| 0.80 | 28/35 | 8 | 2.2583s | 0.1116s | 1 | 8 | yes | 2.1906s | 2.3355s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x3fdfb37bf_k28_s08.py` |  |
| 0.80 | 28/35 | 9 | 2.5094s | 0.0440s | 1 | 8 | yes | 2.4808s | 2.5376s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x59e7fbbff_k28_s09.py` |  |
| 0.80 | 28/35 | 10 | 2.2571s | 0.0679s | 1 | 8 | yes | 2.2144s | 2.3017s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x6ff7bff78_k28_s10.py` |  |
| 0.83 | 29/35 | 1 | 2.4217s | 0.0653s | 1 | 8 | yes | 2.3758s | 2.4583s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7ff1f7f7e_k29_s01.py` |  |
| 0.83 | 29/35 | 2 | 2.5675s | 0.1079s | 1 | 8 | yes | 2.5034s | 2.6425s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7f9ffaeef_k29_s02.py` |  |
| 0.83 | 29/35 | 3 | 2.4275s | 0.1167s | 1 | 8 | yes | 2.3515s | 2.5032s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7ffdf6eee_k29_s03.py` |  |
| 0.83 | 29/35 | 4 | 1.7506s | 0.0406s | 1 | 8 | yes | 1.7208s | 1.7731s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x6fecbf7ff_k29_s04.py` |  |
| 0.83 | 29/35 | 5 | 2.1558s | 0.1012s | 1 | 8 | yes | 2.0940s | 2.2242s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x5fffcffec_k29_s05.py` |  |
| 0.83 | 29/35 | 6 | 2.4579s | 0.0760s | 1 | 8 | yes | 2.4095s | 2.5063s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x5dfbddf7f_k29_s06.py` |  |
| 0.83 | 29/35 | 7 | 2.5797s | 0.0660s | 1 | 8 | yes | 2.5333s | 2.6180s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x35ebf7fff_k29_s07.py` |  |
| 0.83 | 29/35 | 8 | 2.6117s | 0.0346s | 1 | 8 | yes | 2.5899s | 2.6344s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7febebbbf_k29_s08.py` |  |
| 0.83 | 29/35 | 9 | 2.4943s | 0.1046s | 1 | 8 | yes | 2.4266s | 2.5592s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x53f3fefff_k29_s09.py` |  |
| 0.83 | 29/35 | 10 | 2.1628s | 0.0590s | 1 | 8 | yes | 2.1250s | 2.1999s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7ff6ff9cf_k29_s10.py` |  |
| 0.86 | 30/35 | 1 | 2.2662s | 0.0833s | 1 | 8 | yes | 2.2164s | 2.3231s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7fa6ffbff_k30_s01.py` |  |
| 0.86 | 30/35 | 2 | 2.0591s | 0.0620s | 1 | 8 | yes | 2.0234s | 2.1023s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x6efbff7fe_k30_s02.py` |  |
| 0.86 | 30/35 | 3 | 2.5129s | 0.1245s | 1 | 8 | yes | 2.4387s | 2.5999s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x57dfeffdf_k30_s03.py` |  |
| 0.86 | 30/35 | 4 | 2.4789s | 0.1389s | 1 | 8 | yes | 2.3890s | 2.5665s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x6ff7feffa_k30_s04.py` |  |
| 0.86 | 30/35 | 5 | 2.5911s | 0.1050s | 1 | 8 | yes | 2.5182s | 2.6526s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7ff33feff_k30_s05.py` |  |
| 0.86 | 30/35 | 6 | 2.2184s | 0.1346s | 1 | 8 | yes | 2.1346s | 2.3075s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7ff8effef_k30_s06.py` |  |
| 0.86 | 30/35 | 7 | 2.4201s | 0.0925s | 1 | 8 | yes | 2.3576s | 2.4785s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7ffdfff2e_k30_s07.py` |  |
| 0.86 | 30/35 | 8 | 2.4758s | 0.0795s | 1 | 8 | yes | 2.4317s | 2.5340s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x3ff7f3ffe_k30_s08.py` |  |
| 0.86 | 30/35 | 9 | 2.6126s | 0.0816s | 1 | 8 | yes | 2.5719s | 2.6711s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x6df77dfff_k30_s09.py` |  |
| 0.86 | 30/35 | 10 | 2.6074s | 0.1239s | 1 | 8 | yes | 2.5296s | 2.6905s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x67ebffffb_k30_s10.py` |  |
| 0.89 | 31/35 | 1 | 2.6209s | 0.0603s | 1 | 8 | yes | 2.5828s | 2.6616s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7f6ff3fff_k31_s01.py` |  |
| 0.89 | 31/35 | 2 | 2.2041s | 0.0562s | 1 | 8 | yes | 2.1662s | 2.2386s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x77bfbf7ff_k31_s02.py` |  |
| 0.89 | 31/35 | 3 | 2.6366s | 0.1128s | 1 | 8 | yes | 2.5678s | 2.7115s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7febf3fff_k31_s03.py` |  |
| 0.89 | 31/35 | 4 | 2.6689s | 0.1008s | 1 | 8 | yes | 2.6030s | 2.7335s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7fff3f9ff_k31_s04.py` |  |
| 0.89 | 31/35 | 5 | 2.6256s | 0.1243s | 1 | 8 | yes | 2.5692s | 2.7161s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x777ffffbb_k31_s05.py` |  |
| 0.89 | 31/35 | 6 | 2.6323s | 0.1118s | 1 | 8 | yes | 2.5642s | 2.7077s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x37ffdfffb_k31_s06.py` |  |
| 0.89 | 31/35 | 7 | 2.4617s | 0.1012s | 1 | 8 | yes | 2.3948s | 2.5254s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x77ffdeffe_k31_s07.py` |  |
| 0.89 | 31/35 | 8 | 2.4983s | 0.1102s | 1 | 8 | yes | 2.4273s | 2.5687s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7edffff7e_k31_s08.py` |  |
| 0.89 | 31/35 | 9 | 2.4782s | 0.0615s | 1 | 8 | yes | 2.4428s | 2.5233s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7fbffdefd_k31_s09.py` |  |
| 0.89 | 31/35 | 10 | 2.7084s | 0.1312s | 1 | 8 | yes | 2.6201s | 2.7892s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7efdffbfb_k31_s10.py` |  |
| 0.91 | 32/35 | 1 | 2.4071s | 0.0841s | 1 | 8 | yes | 2.3537s | 2.4622s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7ffffefee_k32_s01.py` |  |
| 0.91 | 32/35 | 2 | 2.6024s | 0.0949s | 1 | 8 | yes | 2.5411s | 2.6640s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7fdfdffdf_k32_s02.py` |  |
| 0.91 | 32/35 | 3 | 2.5882s | 0.0706s | 1 | 8 | yes | 2.5443s | 2.6349s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7ffbfbffb_k32_s03.py` |  |
| 0.91 | 32/35 | 4 | 2.5987s | 0.0797s | 1 | 8 | yes | 2.5442s | 2.6459s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x77ffefdff_k32_s04.py` |  |
| 0.91 | 32/35 | 5 | 2.5702s | 0.0747s | 1 | 8 | yes | 2.5205s | 2.6163s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x6fedfffff_k32_s05.py` |  |
| 0.91 | 32/35 | 6 | 2.5270s | 0.1010s | 1 | 8 | yes | 2.4612s | 2.5926s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7fdf7fff7_k32_s06.py` |  |
| 0.91 | 32/35 | 7 | 2.4640s | 0.0951s | 1 | 8 | yes | 2.4098s | 2.5288s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7ffffffcd_k32_s07.py` |  |
| 0.91 | 32/35 | 8 | 2.2600s | 0.0779s | 1 | 8 | yes | 2.2050s | 2.3053s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7fecfffff_k32_s08.py` |  |
| 0.91 | 32/35 | 9 | 2.5086s | 0.0625s | 1 | 8 | yes | 2.4660s | 2.5474s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x5f9ffffff_k32_s09.py` |  |
| 0.91 | 32/35 | 10 | 2.5939s | 0.0632s | 1 | 8 | yes | 2.5514s | 2.6334s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x77cffffff_k32_s10.py` |  |
| 0.94 | 33/35 | 1 | 2.6392s | 0.0481s | 1 | 8 | yes | 2.6057s | 2.6686s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7fff77fff_k33_s01.py` |  |
| 0.94 | 33/35 | 2 | 2.5707s | 0.1201s | 1 | 8 | yes | 2.4992s | 2.6534s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x5ffffbfff_k33_s02.py` |  |
| 0.94 | 33/35 | 3 | 2.5489s | 0.0529s | 1 | 8 | yes | 2.5137s | 2.5815s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x6fffffbff_k33_s03.py` |  |
| 0.94 | 33/35 | 4 | 2.4731s | 0.0527s | 1 | 8 | yes | 2.4375s | 2.5057s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7ffffffe7_k33_s04.py` |  |
| 0.94 | 33/35 | 5 | 2.6316s | 0.0945s | 1 | 8 | yes | 2.5713s | 2.6938s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7ffffff5f_k33_s05.py` |  |
| 0.94 | 33/35 | 6 | 2.1601s | 0.0964s | 1 | 8 | yes | 2.1021s | 2.2253s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7ff6fffff_k33_s06.py` |  |
| 0.94 | 33/35 | 7 | 2.0654s | 0.0774s | 1 | 8 | yes | 2.0138s | 2.1141s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7ffeffffe_k33_s07.py` |  |
| 0.94 | 33/35 | 8 | 2.6397s | 0.0866s | 1 | 8 | yes | 2.5880s | 2.6997s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7feffdfff_k33_s08.py` |  |
| 0.94 | 33/35 | 9 | 2.6532s | 0.0994s | 1 | 8 | yes | 2.5873s | 2.7147s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7beffffff_k33_s09.py` |  |
| 0.94 | 33/35 | 10 | 2.6436s | 0.1254s | 1 | 8 | yes | 2.5661s | 2.7288s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7ffddffff_k33_s10.py` |  |
| 0.97 | 34/35 | 1 | 2.6093s | 0.0464s | 1 | 8 | yes | 2.5849s | 2.6439s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7fbffffff_k34_s01.py` |  |
| 0.97 | 34/35 | 2 | 2.5451s | 0.0688s | 1 | 8 | yes | 2.5003s | 2.5896s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x6ffffffff_k34_s02.py` |  |
| 0.97 | 34/35 | 3 | 2.5937s | 0.0737s | 1 | 8 | yes | 2.5469s | 2.6424s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7ffff7fff_k34_s03.py` |  |
| 0.97 | 34/35 | 4 | 2.6740s | 0.1250s | 1 | 8 | yes | 2.6095s | 2.7657s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7fffeffff_k34_s04.py` |  |
| 0.97 | 34/35 | 5 | 2.6018s | 0.0805s | 1 | 8 | yes | 2.5527s | 2.6555s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x3ffffffff_k34_s05.py` |  |
| 0.97 | 34/35 | 6 | 2.6341s | 0.1141s | 1 | 8 | yes | 2.5692s | 2.7147s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7ffffefff_k34_s06.py` |  |
| 0.97 | 34/35 | 7 | 2.4848s | 0.1331s | 1 | 8 | yes | 2.4039s | 2.5758s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x5ffffffff_k34_s07.py` |  |
| 0.97 | 34/35 | 8 | 2.4974s | 0.0737s | 1 | 8 | yes | 2.4498s | 2.5460s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7fffffffe_k34_s08.py` |  |
| 0.97 | 34/35 | 9 | 2.6457s | 0.0972s | 1 | 8 | yes | 2.5853s | 2.7109s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7fffbffff_k34_s09.py` |  |
| 0.97 | 34/35 | 10 | 2.6194s | 0.0997s | 1 | 8 | yes | 2.5594s | 2.6864s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7fffffdff_k34_s10.py` |  |
| 1.00 | 35/35 | 1 | 2.6380s | 0.1324s | 1 | 8 | yes | 2.5596s | 2.7293s | `detyped_files/deltablue/shallow/proportion_sweep/main_0x7ffffffff_k35_s01.py` |  |

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
| 0.00 | 0/1 | 1 | 2.0495s | 2.0495s | 2.0495s | 1.0 | yes | ok |
| 1.00 | 1/1 | 1 | 2.2716s | 2.2716s | 2.2716s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/1 | 1 | 2.0495s | 0.0939s | 1 | 8 | yes | 1.9886s | 2.1100s | `detyped_files/fannkuch/advanced/proportion_sweep/main_0x0_k00_s01.py` |  |
| 1.00 | 1/1 | 1 | 2.2716s | 0.1071s | 1 | 8 | yes | 2.2083s | 2.3450s | `detyped_files/fannkuch/advanced/proportion_sweep/main_0x1_k01_s01.py` |  |

## fannkuch/shallow

- Detypable targets: `1`
- Total runs: `2`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/1 | 1 | 0.7936s | 0.7936s | 0.7936s | 1.0 | yes | ok |
| 1.00 | 1/1 | 1 | 0.8714s | 0.8714s | 0.8714s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/1 | 1 | 0.7936s | 0.0447s | 1 | 8 | yes | 0.7629s | 0.8211s | `detyped_files/fannkuch/shallow/proportion_sweep/main_0x0_k00_s01.py` |  |
| 1.00 | 1/1 | 1 | 0.8714s | 0.0953s | 1 | 8 | yes | 0.8137s | 0.9350s | `detyped_files/fannkuch/shallow/proportion_sweep/main_0x1_k01_s01.py` |  |

## fannkuch/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.8558s | 0.8558s | 0.8558s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.8558s | 0.0715s | 1 | 8 | yes | 0.8052s | 0.8957s | `static-python-perf/Benchmark/fannkuch/untyped/main.py` |  |

## float/advanced

- Detypable targets: `5`
- Total runs: `32`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/5 | 1 | 0.4919s | 0.4919s | 0.4919s | 1.0 | yes | ok |
| 0.20 | 1/5 | 5 | 0.5666s | 0.4493s | 0.8091s | 1.0 | yes | ok |
| 0.40 | 2/5 | 10 | 0.6290s | 0.4751s | 0.7959s | 1.0 | yes | ok |
| 0.60 | 3/5 | 10 | 0.7291s | 0.4928s | 0.9047s | 1.0 | yes | ok |
| 0.80 | 4/5 | 5 | 0.7996s | 0.5774s | 0.8741s | 1.0 | yes | ok |
| 1.00 | 5/5 | 1 | 0.9176s | 0.9176s | 0.9176s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/5 | 1 | 0.4919s | 0.0215s | 1 | 8 | yes | 0.4791s | 0.5067s | `detyped_files/float/advanced/proportion_sweep/main_0x0_k00_s01.py` |  |
| 0.20 | 1/5 | 1 | 0.5141s | 0.0148s | 1 | 8 | yes | 0.5046s | 0.5239s | `detyped_files/float/advanced/proportion_sweep/main_0x4_k01_s01.py` |  |
| 0.20 | 1/5 | 2 | 0.8091s | 0.0507s | 1 | 8 | yes | 0.7772s | 0.8426s | `detyped_files/float/advanced/proportion_sweep/main_0x8_k01_s02.py` |  |
| 0.20 | 1/5 | 3 | 0.4493s | 0.0420s | 1 | 8 | yes | 0.4218s | 0.4756s | `detyped_files/float/advanced/proportion_sweep/main_0x10_k01_s03.py` |  |
| 0.20 | 1/5 | 4 | 0.5949s | 0.0433s | 1 | 8 | yes | 0.5662s | 0.6222s | `detyped_files/float/advanced/proportion_sweep/main_0x1_k01_s04.py` |  |
| 0.20 | 1/5 | 5 | 0.4657s | 0.0540s | 1 | 8 | yes | 0.4291s | 0.4987s | `detyped_files/float/advanced/proportion_sweep/main_0x2_k01_s05.py` |  |
| 0.40 | 2/5 | 1 | 0.4751s | 0.0367s | 1 | 8 | yes | 0.4533s | 0.5017s | `detyped_files/float/advanced/proportion_sweep/main_0x12_k02_s01.py` |  |
| 0.40 | 2/5 | 2 | 0.5953s | 0.0480s | 1 | 8 | yes | 0.5601s | 0.6175s | `detyped_files/float/advanced/proportion_sweep/main_0x5_k02_s02.py` |  |
| 0.40 | 2/5 | 3 | 0.7498s | 0.0631s | 1 | 8 | yes | 0.7073s | 0.7880s | `detyped_files/float/advanced/proportion_sweep/main_0xa_k02_s03.py` |  |
| 0.40 | 2/5 | 4 | 0.7255s | 0.0744s | 1 | 8 | yes | 0.6774s | 0.7737s | `detyped_files/float/advanced/proportion_sweep/main_0x18_k02_s04.py` |  |
| 0.40 | 2/5 | 5 | 0.7959s | 0.0651s | 1 | 8 | yes | 0.7529s | 0.8378s | `detyped_files/float/advanced/proportion_sweep/main_0x9_k02_s05.py` |  |
| 0.40 | 2/5 | 6 | 0.5786s | 0.0361s | 1 | 8 | yes | 0.5552s | 0.6021s | `detyped_files/float/advanced/proportion_sweep/main_0x11_k02_s06.py` |  |
| 0.40 | 2/5 | 7 | 0.7787s | 0.0820s | 1 | 8 | yes | 0.7252s | 0.8296s | `detyped_files/float/advanced/proportion_sweep/main_0xc_k02_s07.py` |  |
| 0.40 | 2/5 | 8 | 0.5093s | 0.0301s | 1 | 8 | yes | 0.4945s | 0.5312s | `detyped_files/float/advanced/proportion_sweep/main_0x6_k02_s08.py` |  |
| 0.40 | 2/5 | 9 | 0.5897s | 0.0218s | 1 | 8 | yes | 0.5770s | 0.6050s | `detyped_files/float/advanced/proportion_sweep/main_0x3_k02_s09.py` |  |
| 0.40 | 2/5 | 10 | 0.4920s | 0.0340s | 1 | 8 | yes | 0.4673s | 0.5112s | `detyped_files/float/advanced/proportion_sweep/main_0x14_k02_s10.py` |  |
| 0.60 | 3/5 | 1 | 0.8568s | 0.0532s | 1 | 8 | yes | 0.8184s | 0.8855s | `detyped_files/float/advanced/proportion_sweep/main_0x19_k03_s01.py` |  |
| 0.60 | 3/5 | 2 | 0.6196s | 0.0336s | 1 | 8 | yes | 0.5983s | 0.6418s | `detyped_files/float/advanced/proportion_sweep/main_0x7_k03_s02.py` |  |
| 0.60 | 3/5 | 3 | 0.8174s | 0.0617s | 1 | 8 | yes | 0.7756s | 0.8549s | `detyped_files/float/advanced/proportion_sweep/main_0x1c_k03_s03.py` |  |
| 0.60 | 3/5 | 4 | 0.7864s | 0.0535s | 1 | 8 | yes | 0.7516s | 0.8217s | `detyped_files/float/advanced/proportion_sweep/main_0xe_k03_s04.py` |  |
| 0.60 | 3/5 | 5 | 0.4928s | 0.0286s | 1 | 8 | yes | 0.4717s | 0.5081s | `detyped_files/float/advanced/proportion_sweep/main_0x16_k03_s05.py` |  |
| 0.60 | 3/5 | 6 | 0.6033s | 0.0477s | 1 | 8 | yes | 0.5716s | 0.6334s | `detyped_files/float/advanced/proportion_sweep/main_0x15_k03_s06.py` |  |
| 0.60 | 3/5 | 7 | 0.9047s | 0.0776s | 1 | 8 | yes | 0.8550s | 0.9541s | `detyped_files/float/advanced/proportion_sweep/main_0xb_k03_s07.py` |  |
| 0.60 | 3/5 | 8 | 0.7830s | 0.0755s | 1 | 8 | yes | 0.7354s | 0.8314s | `detyped_files/float/advanced/proportion_sweep/main_0x1a_k03_s08.py` |  |
| 0.60 | 3/5 | 9 | 0.8887s | 0.0745s | 1 | 8 | yes | 0.8456s | 0.9428s | `detyped_files/float/advanced/proportion_sweep/main_0xd_k03_s09.py` |  |
| 0.60 | 3/5 | 10 | 0.5387s | 0.0384s | 1 | 8 | yes | 0.5143s | 0.5633s | `detyped_files/float/advanced/proportion_sweep/main_0x13_k03_s10.py` |  |
| 0.80 | 4/5 | 1 | 0.5774s | 0.0536s | 1 | 8 | yes | 0.5414s | 0.6113s | `detyped_files/float/advanced/proportion_sweep/main_0x17_k04_s01.py` |  |
| 0.80 | 4/5 | 2 | 0.8659s | 0.0327s | 1 | 8 | yes | 0.8451s | 0.8872s | `detyped_files/float/advanced/proportion_sweep/main_0x1b_k04_s02.py` |  |
| 0.80 | 4/5 | 3 | 0.8104s | 0.0873s | 1 | 8 | yes | 0.7535s | 0.8669s | `detyped_files/float/advanced/proportion_sweep/main_0x1e_k04_s03.py` |  |
| 0.80 | 4/5 | 4 | 0.8700s | 0.0483s | 1 | 8 | yes | 0.8402s | 0.9028s | `detyped_files/float/advanced/proportion_sweep/main_0x1d_k04_s04.py` |  |
| 0.80 | 4/5 | 5 | 0.8741s | 0.0671s | 1 | 8 | yes | 0.8316s | 0.9177s | `detyped_files/float/advanced/proportion_sweep/main_0xf_k04_s05.py` |  |
| 1.00 | 5/5 | 1 | 0.9176s | 0.0875s | 1 | 8 | yes | 0.8608s | 0.9734s | `detyped_files/float/advanced/proportion_sweep/main_0x1f_k05_s01.py` |  |

## float/shallow

- Detypable targets: `3`
- Total runs: `8`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/3 | 1 | 0.4700s | 0.4700s | 0.4700s | 1.0 | yes | ok |
| 0.33 | 1/3 | 3 | 0.5099s | 0.4742s | 0.5664s | 1.0 | yes | ok |
| 0.67 | 2/3 | 3 | 0.5328s | 0.4530s | 0.5887s | 1.0 | yes | ok |
| 1.00 | 3/3 | 1 | 0.5641s | 0.5641s | 0.5641s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/3 | 1 | 0.4700s | 0.0416s | 1 | 8 | yes | 0.4444s | 0.4986s | `detyped_files/float/shallow/proportion_sweep/main_0x0_k00_s01.py` |  |
| 0.33 | 1/3 | 1 | 0.4742s | 0.0440s | 1 | 8 | yes | 0.4449s | 0.5015s | `detyped_files/float/shallow/proportion_sweep/main_0x2_k01_s01.py` |  |
| 0.33 | 1/3 | 2 | 0.4890s | 0.0264s | 1 | 8 | yes | 0.4745s | 0.5077s | `detyped_files/float/shallow/proportion_sweep/main_0x4_k01_s02.py` |  |
| 0.33 | 1/3 | 3 | 0.5664s | 0.0404s | 1 | 8 | yes | 0.5370s | 0.5901s | `detyped_files/float/shallow/proportion_sweep/main_0x1_k01_s03.py` |  |
| 0.67 | 2/3 | 1 | 0.5567s | 0.0232s | 1 | 8 | yes | 0.5399s | 0.5694s | `detyped_files/float/shallow/proportion_sweep/main_0x3_k02_s01.py` |  |
| 0.67 | 2/3 | 2 | 0.4530s | 0.0417s | 1 | 8 | yes | 0.4250s | 0.4783s | `detyped_files/float/shallow/proportion_sweep/main_0x6_k02_s02.py` |  |
| 0.67 | 2/3 | 3 | 0.5887s | 0.0190s | 1 | 8 | yes | 0.5771s | 0.6014s | `detyped_files/float/shallow/proportion_sweep/main_0x5_k02_s03.py` |  |
| 1.00 | 3/3 | 1 | 0.5641s | 0.0249s | 1 | 8 | yes | 0.5458s | 0.5764s | `detyped_files/float/shallow/proportion_sweep/main_0x7_k03_s01.py` |  |

## float/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.4805s | 0.4805s | 0.4805s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.4805s | 0.0312s | 1 | 8 | yes | 0.4575s | 0.4957s | `static-python-perf/Benchmark/float/untyped/main.py` |  |

## nbody/advanced

- Detypable targets: `6`
- Total runs: `44`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 1.4809s | 1.4809s | 1.4809s | 1.0 | yes | ok |
| 0.17 | 1/6 | 6 | 1.9645s | 1.4977s | 4.1235s | 1.0 | yes | ok |
| 0.33 | 2/6 | 10 | 2.2748s | 1.4589s | 4.1338s | 1.0 | yes | ok |
| 0.50 | 3/6 | 10 | 2.5335s | 1.4705s | 4.1007s | 1.0 | yes | ok |
| 0.67 | 4/6 | 10 | 3.2994s | 1.4643s | 4.1374s | 1.0 | yes | ok |
| 0.83 | 5/6 | 6 | 3.6016s | 1.4697s | 4.0998s | 1.0 | yes | ok |
| 1.00 | 6/6 | 1 | 4.1076s | 4.1076s | 4.1076s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 1.4809s | 0.1112s | 1 | 8 | yes | 1.4111s | 1.5558s | `detyped_files/nbody/advanced/proportion_sweep/main_0x0_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 4.1235s | 0.1480s | 1 | 8 | yes | 4.0408s | 4.2323s | `detyped_files/nbody/advanced/proportion_sweep/main_0x20_k01_s01.py` |  |
| 0.17 | 1/6 | 2 | 1.5446s | 0.1289s | 1 | 8 | yes | 1.4670s | 1.6299s | `detyped_files/nbody/advanced/proportion_sweep/main_0x8_k01_s02.py` |  |
| 0.17 | 1/6 | 3 | 1.4977s | 0.0354s | 1 | 8 | yes | 1.4739s | 1.5191s | `detyped_files/nbody/advanced/proportion_sweep/main_0x2_k01_s03.py` |  |
| 0.17 | 1/6 | 4 | 1.5424s | 0.1119s | 1 | 8 | yes | 1.4800s | 1.6208s | `detyped_files/nbody/advanced/proportion_sweep/main_0x10_k01_s04.py` |  |
| 0.17 | 1/6 | 5 | 1.5092s | 0.1088s | 1 | 8 | yes | 1.4374s | 1.5773s | `detyped_files/nbody/advanced/proportion_sweep/main_0x1_k01_s05.py` |  |
| 0.17 | 1/6 | 6 | 1.5697s | 0.1470s | 1 | 8 | yes | 1.4763s | 1.6712s | `detyped_files/nbody/advanced/proportion_sweep/main_0x4_k01_s06.py` |  |
| 0.33 | 2/6 | 1 | 1.5471s | 0.1438s | 1 | 8 | yes | 1.4654s | 1.6483s | `detyped_files/nbody/advanced/proportion_sweep/main_0x5_k02_s01.py` |  |
| 0.33 | 2/6 | 2 | 1.5107s | 0.0499s | 1 | 8 | yes | 1.4757s | 1.5403s | `detyped_files/nbody/advanced/proportion_sweep/main_0x14_k02_s02.py` |  |
| 0.33 | 2/6 | 3 | 4.1338s | 0.1296s | 1 | 8 | yes | 4.0512s | 4.2186s | `detyped_files/nbody/advanced/proportion_sweep/main_0x22_k02_s03.py` |  |
| 0.33 | 2/6 | 4 | 1.4717s | 0.0674s | 1 | 8 | yes | 1.4285s | 1.5148s | `detyped_files/nbody/advanced/proportion_sweep/main_0x18_k02_s04.py` |  |
| 0.33 | 2/6 | 5 | 1.5151s | 0.1809s | 1 | 8 | yes | 1.4254s | 1.6471s | `detyped_files/nbody/advanced/proportion_sweep/main_0xc_k02_s05.py` |  |
| 0.33 | 2/6 | 6 | 4.0192s | 0.0711s | 1 | 8 | yes | 3.9707s | 4.0625s | `detyped_files/nbody/advanced/proportion_sweep/main_0x30_k02_s06.py` |  |
| 0.33 | 2/6 | 7 | 1.5210s | 0.1087s | 1 | 8 | yes | 1.4520s | 1.5937s | `detyped_files/nbody/advanced/proportion_sweep/main_0x12_k02_s07.py` |  |
| 0.33 | 2/6 | 8 | 1.4817s | 0.0423s | 1 | 8 | yes | 1.4532s | 1.5080s | `detyped_files/nbody/advanced/proportion_sweep/main_0x3_k02_s08.py` |  |
| 0.33 | 2/6 | 9 | 1.4589s | 0.0993s | 1 | 8 | yes | 1.3977s | 1.5250s | `detyped_files/nbody/advanced/proportion_sweep/main_0x6_k02_s09.py` |  |
| 0.33 | 2/6 | 10 | 4.0886s | 0.0894s | 1 | 8 | yes | 4.0386s | 4.1524s | `detyped_files/nbody/advanced/proportion_sweep/main_0x24_k02_s10.py` |  |
| 0.50 | 3/6 | 1 | 4.1007s | 0.0920s | 1 | 8 | yes | 4.0425s | 4.1620s | `detyped_files/nbody/advanced/proportion_sweep/main_0x34_k03_s01.py` |  |
| 0.50 | 3/6 | 2 | 4.0513s | 0.1070s | 1 | 8 | yes | 3.9771s | 4.1119s | `detyped_files/nbody/advanced/proportion_sweep/main_0x31_k03_s02.py` |  |
| 0.50 | 3/6 | 3 | 1.4705s | 0.0802s | 1 | 8 | yes | 1.4183s | 1.5217s | `detyped_files/nbody/advanced/proportion_sweep/main_0x7_k03_s03.py` |  |
| 0.50 | 3/6 | 4 | 1.4908s | 0.0927s | 1 | 8 | yes | 1.4335s | 1.5516s | `detyped_files/nbody/advanced/proportion_sweep/main_0xe_k03_s04.py` |  |
| 0.50 | 3/6 | 5 | 4.0827s | 0.0929s | 1 | 8 | yes | 4.0256s | 4.1461s | `detyped_files/nbody/advanced/proportion_sweep/main_0x38_k03_s05.py` |  |
| 0.50 | 3/6 | 6 | 1.5040s | 0.0746s | 1 | 8 | yes | 1.4512s | 1.5479s | `detyped_files/nbody/advanced/proportion_sweep/main_0xb_k03_s06.py` |  |
| 0.50 | 3/6 | 7 | 1.5035s | 0.0531s | 1 | 8 | yes | 1.4672s | 1.5358s | `detyped_files/nbody/advanced/proportion_sweep/main_0x16_k03_s07.py` |  |
| 0.50 | 3/6 | 8 | 1.5140s | 0.0709s | 1 | 8 | yes | 1.4633s | 1.5544s | `detyped_files/nbody/advanced/proportion_sweep/main_0xd_k03_s08.py` |  |
| 0.50 | 3/6 | 9 | 1.5334s | 0.0991s | 1 | 8 | yes | 1.4821s | 1.6035s | `detyped_files/nbody/advanced/proportion_sweep/main_0x15_k03_s09.py` |  |
| 0.50 | 3/6 | 10 | 4.0840s | 0.1588s | 1 | 8 | yes | 3.9933s | 4.1995s | `detyped_files/nbody/advanced/proportion_sweep/main_0x25_k03_s10.py` |  |
| 0.67 | 4/6 | 1 | 1.4643s | 0.0656s | 1 | 8 | yes | 1.4212s | 1.5055s | `detyped_files/nbody/advanced/proportion_sweep/main_0x1d_k04_s01.py` |  |
| 0.67 | 4/6 | 2 | 1.4979s | 0.0730s | 1 | 8 | yes | 1.4522s | 1.5461s | `detyped_files/nbody/advanced/proportion_sweep/main_0x1e_k04_s02.py` |  |
| 0.67 | 4/6 | 3 | 3.9918s | 0.0889s | 1 | 8 | yes | 3.9353s | 4.0497s | `detyped_files/nbody/advanced/proportion_sweep/main_0x35_k04_s03.py` |  |
| 0.67 | 4/6 | 4 | 4.0120s | 0.0875s | 1 | 8 | yes | 3.9507s | 4.0632s | `detyped_files/nbody/advanced/proportion_sweep/main_0x2e_k04_s04.py` |  |
| 0.67 | 4/6 | 5 | 4.0404s | 0.1419s | 1 | 8 | yes | 3.9540s | 4.1375s | `detyped_files/nbody/advanced/proportion_sweep/main_0x3a_k04_s05.py` |  |
| 0.67 | 4/6 | 6 | 4.1282s | 0.1064s | 1 | 8 | yes | 4.0620s | 4.1998s | `detyped_files/nbody/advanced/proportion_sweep/main_0x2d_k04_s06.py` |  |
| 0.67 | 4/6 | 7 | 4.1374s | 0.2145s | 1 | 8 | yes | 4.0101s | 4.2851s | `detyped_files/nbody/advanced/proportion_sweep/main_0x3c_k04_s07.py` |  |
| 0.67 | 4/6 | 8 | 4.0747s | 0.1252s | 1 | 8 | yes | 3.9949s | 4.1554s | `detyped_files/nbody/advanced/proportion_sweep/main_0x36_k04_s08.py` |  |
| 0.67 | 4/6 | 9 | 4.1251s | 0.0630s | 1 | 8 | yes | 4.0834s | 4.1650s | `detyped_files/nbody/advanced/proportion_sweep/main_0x27_k04_s09.py` |  |
| 0.67 | 4/6 | 10 | 1.5227s | 0.1003s | 1 | 8 | yes | 1.4593s | 1.5887s | `detyped_files/nbody/advanced/proportion_sweep/main_0x1b_k04_s10.py` |  |
| 0.83 | 5/6 | 1 | 1.4697s | 0.0718s | 1 | 8 | yes | 1.4208s | 1.5159s | `detyped_files/nbody/advanced/proportion_sweep/main_0x1f_k05_s01.py` |  |
| 0.83 | 5/6 | 2 | 3.9712s | 0.0994s | 1 | 8 | yes | 3.9136s | 4.0395s | `detyped_files/nbody/advanced/proportion_sweep/main_0x2f_k05_s02.py` |  |
| 0.83 | 5/6 | 3 | 3.9601s | 0.1248s | 1 | 8 | yes | 3.8836s | 4.0435s | `detyped_files/nbody/advanced/proportion_sweep/main_0x37_k05_s03.py` |  |
| 0.83 | 5/6 | 4 | 4.0109s | 0.0915s | 1 | 8 | yes | 3.9513s | 4.0692s | `detyped_files/nbody/advanced/proportion_sweep/main_0x3e_k05_s04.py` |  |
| 0.83 | 5/6 | 5 | 4.0998s | 0.1168s | 1 | 8 | yes | 4.0286s | 4.1786s | `detyped_files/nbody/advanced/proportion_sweep/main_0x3d_k05_s05.py` |  |
| 0.83 | 5/6 | 6 | 4.0980s | 0.1414s | 1 | 8 | yes | 4.0117s | 4.1924s | `detyped_files/nbody/advanced/proportion_sweep/main_0x3b_k05_s06.py` |  |
| 1.00 | 6/6 | 1 | 4.1076s | 0.1560s | 1 | 8 | yes | 4.0177s | 4.2186s | `detyped_files/nbody/advanced/proportion_sweep/main_0x3f_k06_s01.py` |  |

## nbody/shallow

- Detypable targets: `6`
- Total runs: `44`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.9882s | 0.9882s | 0.9882s | 1.0 | yes | ok |
| 0.17 | 1/6 | 6 | 1.0042s | 0.9837s | 1.0236s | 1.0 | yes | 1 failed |
| 0.33 | 2/6 | 10 | 0.9991s | 0.9669s | 1.0369s | 1.0 | yes | 3 failed |
| 0.50 | 3/6 | 10 | 0.9886s | 0.9629s | 1.0091s | 1.0 | yes | 7 failed |
| 0.67 | 4/6 | 10 | 1.0046s | 0.9903s | 1.0302s | 1.0 | yes | 6 failed |
| 0.83 | 5/6 | 6 | 1.0034s | 1.0034s | 1.0034s | 1.0 | yes | 5 failed |
| 1.00 | 6/6 | 1 | - | - | - | - | - | 1 failed |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/6 | 1 | 0.9882s | 0.1002s | 1 | 8 | yes | 0.9223s | 1.0512s | `detyped_files/nbody/shallow/proportion_sweep/main_0x0_k00_s01.py` |  |
| 0.17 | 1/6 | 1 | 1.0215s | 0.0769s | 1 | 8 | yes | 0.9703s | 1.0696s | `detyped_files/nbody/shallow/proportion_sweep/main_0x20_k01_s01.py` |  |
| 0.17 | 1/6 | 2 | 1.0236s | 0.0279s | 1 | 8 | yes | 1.0047s | 1.0406s | `detyped_files/nbody/shallow/proportion_sweep/main_0x2_k01_s02.py` |  |
| 0.17 | 1/6 | 3 | 0.9856s | 0.0724s | 1 | 8 | yes | 0.9358s | 1.0311s | `detyped_files/nbody/shallow/proportion_sweep/main_0x10_k01_s03.py` |  |
| 0.17 | 1/6 | 4 | 1.0066s | 0.0446s | 1 | 8 | yes | 0.9764s | 1.0340s | `detyped_files/nbody/shallow/proportion_sweep/main_0x8_k01_s04.py` |  |
| 0.17 | 1/6 | 5 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0x4_k01_s05.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_0x4_k01_s05.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_0x4_k01_s05.py", line 72
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.17 | 1/6 | 6 | 0.9837s | 0.1211s | 1 | 8 | yes | 0.9068s | 1.0635s | `detyped_files/nbody/shallow/proportion_sweep/main_0x1_k01_s06.py` |  |
| 0.33 | 2/6 | 1 | 0.9908s | 0.0400s | 1 | 8 | yes | 0.9627s | 1.0142s | `detyped_files/nbody/shallow/proportion_sweep/main_0x11_k02_s01.py` |  |
| 0.33 | 2/6 | 2 | 1.0260s | 0.0418s | 1 | 8 | yes | 0.9985s | 1.0519s | `detyped_files/nbody/shallow/proportion_sweep/main_0x28_k02_s02.py` |  |
| 0.33 | 2/6 | 3 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0xc_k02_s03.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_0xc_k02_s03.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_0xc_k02_s03.py", line 73
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.33 | 2/6 | 4 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0x14_k02_s04.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_0x14_k02_s04.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_0x14_k02_s04.py", line 72
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.33 | 2/6 | 5 | 0.9798s | 0.0639s | 1 | 8 | yes | 0.9364s | 1.0178s | `detyped_files/nbody/shallow/proportion_sweep/main_0x30_k02_s05.py` |  |
| 0.33 | 2/6 | 6 | 1.0036s | 0.0381s | 1 | 8 | yes | 0.9775s | 1.0262s | `detyped_files/nbody/shallow/proportion_sweep/main_0x21_k02_s06.py` |  |
| 0.33 | 2/6 | 7 | 0.9669s | 0.0738s | 1 | 8 | yes | 0.9197s | 1.0143s | `detyped_files/nbody/shallow/proportion_sweep/main_0x3_k02_s07.py` |  |
| 0.33 | 2/6 | 8 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0x24_k02_s08.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_0x24_k02_s08.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_0x24_k02_s08.py", line 74
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.33 | 2/6 | 9 | 0.9895s | 0.0663s | 1 | 8 | yes | 0.9441s | 1.0276s | `detyped_files/nbody/shallow/proportion_sweep/main_0x18_k02_s09.py` |  |
| 0.33 | 2/6 | 10 | 1.0369s | 0.0656s | 1 | 8 | yes | 0.9991s | 1.0828s | `detyped_files/nbody/shallow/proportion_sweep/main_0xa_k02_s10.py` |  |
| 0.50 | 3/6 | 1 | 1.0091s | 0.0681s | 1 | 8 | yes | 0.9637s | 1.0524s | `detyped_files/nbody/shallow/proportion_sweep/main_0x2a_k03_s01.py` |  |
| 0.50 | 3/6 | 2 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0x16_k03_s02.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_0x16_k03_s02.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_0x16_k03_s02.py", line 74
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.50 | 3/6 | 3 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0x7_k03_s03.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_0x7_k03_s03.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_0x7_k03_s03.py", line 74
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.50 | 3/6 | 4 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0x25_k03_s04.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_0x25_k03_s04.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_0x25_k03_s04.py", line 74
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.50 | 3/6 | 5 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0x26_k03_s05.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_0x26_k03_s05.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_0x26_k03_s05.py", line 76
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.50 | 3/6 | 6 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0x1c_k03_s06.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_0x1c_k03_s06.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_0x1c_k03_s06.py", line 73
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.50 | 3/6 | 7 | 0.9939s | 0.1155s | 1 | 8 | yes | 0.9269s | 1.0736s | `detyped_files/nbody/shallow/proportion_sweep/main_0x19_k03_s07.py` |  |
| 0.50 | 3/6 | 8 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0x34_k03_s08.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_0x34_k03_s08.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_0x34_k03_s08.py", line 74
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.50 | 3/6 | 9 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0xd_k03_s09.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_0xd_k03_s09.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_0xd_k03_s09.py", line 73
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.50 | 3/6 | 10 | 0.9629s | 0.0462s | 1 | 8 | yes | 0.9318s | 0.9914s | `detyped_files/nbody/shallow/proportion_sweep/main_0x31_k03_s10.py` |  |
| 0.67 | 4/6 | 1 | 0.9936s | 0.0700s | 1 | 8 | yes | 0.9487s | 1.0371s | `detyped_files/nbody/shallow/proportion_sweep/main_0x39_k04_s01.py` |  |
| 0.67 | 4/6 | 2 | 1.0302s | 0.0967s | 1 | 8 | yes | 0.9702s | 1.0954s | `detyped_files/nbody/shallow/proportion_sweep/main_0x3a_k04_s02.py` |  |
| 0.67 | 4/6 | 3 | 0.9903s | 0.0707s | 1 | 8 | yes | 0.9413s | 1.0341s | `detyped_files/nbody/shallow/proportion_sweep/main_0x1b_k04_s03.py` |  |
| 0.67 | 4/6 | 4 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0x2e_k04_s04.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_0x2e_k04_s04.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_0x2e_k04_s04.py", line 77
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.67 | 4/6 | 5 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0x2d_k04_s05.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_0x2d_k04_s05.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_0x2d_k04_s05.py", line 75
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.67 | 4/6 | 6 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0x17_k04_s06.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_0x17_k04_s06.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_0x17_k04_s06.py", line 74
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.67 | 4/6 | 7 | 1.0044s | 0.1037s | 1 | 8 | yes | 0.9405s | 1.0746s | `detyped_files/nbody/shallow/proportion_sweep/main_0x2b_k04_s07.py` |  |
| 0.67 | 4/6 | 8 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0x1e_k04_s08.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_0x1e_k04_s08.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_0x1e_k04_s08.py", line 75
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.67 | 4/6 | 9 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0x1d_k04_s09.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_0x1d_k04_s09.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_0x1d_k04_s09.py", line 73
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.67 | 4/6 | 10 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0x35_k04_s10.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_0x35_k04_s10.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_0x35_k04_s10.py", line 74
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.83 | 5/6 | 1 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0x2f_k05_s01.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_0x2f_k05_s01.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_0x2f_k05_s01.py", line 77
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.83 | 5/6 | 2 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0x3d_k05_s02.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_0x3d_k05_s02.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_0x3d_k05_s02.py", line 75
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.83 | 5/6 | 3 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0x3e_k05_s03.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_0x3e_k05_s03.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_0x3e_k05_s03.py", line 77
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.83 | 5/6 | 4 | 1.0034s | 0.0437s | 1 | 8 | yes | 0.9740s | 1.0295s | `detyped_files/nbody/shallow/proportion_sweep/main_0x3b_k05_s04.py` |  |
| 0.83 | 5/6 | 5 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0x37_k05_s05.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_0x37_k05_s05.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_0x37_k05_s05.py", line 76
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 0.83 | 5/6 | 6 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0x1f_k05_s06.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_0x1f_k05_s06.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_0x1f_k05_s06.py", line 75
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |
| 1.00 | 6/6 | 1 | - | - | - | - | - | - | - | `detyped_files/nbody/shallow/proportion_sweep/main_0x3f_k06_s01.py` | benchmark script failed (1): detyped_files/nbody/shallow/proportion_sweep/main_0x3f_k06_s01.py
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
  File "detyped_files/nbody/shallow/proportion_sweep/main_0x3f_k06_s01.py", line 77
    ref: Body = cast(Body, _ref)
               ^
cinderx.compiler.errors.TypedSyntaxError: cast to unknown type |

## nbody/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 1.0937s | 1.0937s | 1.0937s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 1.0937s | 0.1137s | 1 | 8 | yes | 1.0248s | 1.1717s | `static-python-perf/Benchmark/nbody/untyped/main.py` |  |

## nqueens/advanced

- Detypable targets: `5`
- Total runs: `32`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/5 | 1 | 0.2297s | 0.2297s | 0.2297s | 1.0 | yes | ok |
| 0.20 | 1/5 | 5 | 0.2267s | 0.2063s | 0.2539s | 1.0 | yes | ok |
| 0.40 | 2/5 | 10 | 0.2315s | 0.2154s | 0.2445s | 1.2 | yes | ok |
| 0.60 | 3/5 | 10 | 0.2404s | 0.2203s | 0.2552s | 1.0 | yes | ok |
| 0.80 | 4/5 | 5 | 0.2517s | 0.2337s | 0.2633s | 1.2 | yes | ok |
| 1.00 | 5/5 | 1 | 0.2576s | 0.2576s | 0.2576s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/5 | 1 | 0.2297s | 0.0217s | 1 | 8 | yes | 0.2164s | 0.2446s | `detyped_files/nqueens/advanced/proportion_sweep/main_0x0_k00_s01.py` |  |
| 0.20 | 1/5 | 1 | 0.2153s | 0.0123s | 1 | 8 | yes | 0.2075s | 0.2233s | `detyped_files/nqueens/advanced/proportion_sweep/main_0x2_k01_s01.py` |  |
| 0.20 | 1/5 | 2 | 0.2327s | 0.0226s | 1 | 8 | yes | 0.2196s | 0.2486s | `detyped_files/nqueens/advanced/proportion_sweep/main_0x1_k01_s02.py` |  |
| 0.20 | 1/5 | 3 | 0.2254s | 0.0237s | 1 | 8 | yes | 0.2110s | 0.2416s | `detyped_files/nqueens/advanced/proportion_sweep/main_0x10_k01_s03.py` |  |
| 0.20 | 1/5 | 4 | 0.2063s | 0.0186s | 1 | 8 | yes | 0.1934s | 0.2171s | `detyped_files/nqueens/advanced/proportion_sweep/main_0x8_k01_s04.py` |  |
| 0.20 | 1/5 | 5 | 0.2539s | 0.0230s | 1 | 8 | yes | 0.2419s | 0.2706s | `detyped_files/nqueens/advanced/proportion_sweep/main_0x4_k01_s05.py` |  |
| 0.40 | 2/5 | 1 | 0.2405s | 0.0189s | 1 | 8 | yes | 0.2272s | 0.2519s | `detyped_files/nqueens/advanced/proportion_sweep/main_0x14_k02_s01.py` |  |
| 0.40 | 2/5 | 2 | 0.2298s | 0.0338s | 2 | 16 | yes | 0.2156s | 0.2474s | `detyped_files/nqueens/advanced/proportion_sweep/main_0x18_k02_s02.py` |  |
| 0.40 | 2/5 | 3 | 0.2303s | 0.0216s | 1 | 8 | yes | 0.2148s | 0.2429s | `detyped_files/nqueens/advanced/proportion_sweep/main_0x5_k02_s03.py` |  |
| 0.40 | 2/5 | 4 | 0.2299s | 0.0382s | 2 | 16 | yes | 0.2137s | 0.2494s | `detyped_files/nqueens/advanced/proportion_sweep/main_0x12_k02_s04.py` |  |
| 0.40 | 2/5 | 5 | 0.2289s | 0.0281s | 1 | 8 | yes | 0.2134s | 0.2493s | `detyped_files/nqueens/advanced/proportion_sweep/main_0x11_k02_s05.py` |  |
| 0.40 | 2/5 | 6 | 0.2211s | 0.0080s | 1 | 8 | yes | 0.2169s | 0.2269s | `detyped_files/nqueens/advanced/proportion_sweep/main_0x3_k02_s06.py` |  |
| 0.40 | 2/5 | 7 | 0.2154s | 0.0202s | 1 | 8 | yes | 0.2006s | 0.2242s | `detyped_files/nqueens/advanced/proportion_sweep/main_0xa_k02_s07.py` |  |
| 0.40 | 2/5 | 8 | 0.2445s | 0.0129s | 1 | 8 | yes | 0.2370s | 0.2540s | `detyped_files/nqueens/advanced/proportion_sweep/main_0x6_k02_s08.py` |  |
| 0.40 | 2/5 | 9 | 0.2333s | 0.0288s | 1 | 8 | yes | 0.2184s | 0.2545s | `detyped_files/nqueens/advanced/proportion_sweep/main_0x9_k02_s09.py` |  |
| 0.40 | 2/5 | 10 | 0.2411s | 0.0155s | 1 | 8 | yes | 0.2307s | 0.2502s | `detyped_files/nqueens/advanced/proportion_sweep/main_0xc_k02_s10.py` |  |
| 0.60 | 3/5 | 1 | 0.2418s | 0.0182s | 1 | 8 | yes | 0.2290s | 0.2531s | `detyped_files/nqueens/advanced/proportion_sweep/main_0x7_k03_s01.py` |  |
| 0.60 | 3/5 | 2 | 0.2316s | 0.0144s | 1 | 8 | yes | 0.2244s | 0.2422s | `detyped_files/nqueens/advanced/proportion_sweep/main_0x19_k03_s02.py` |  |
| 0.60 | 3/5 | 3 | 0.2531s | 0.0110s | 1 | 8 | yes | 0.2458s | 0.2600s | `detyped_files/nqueens/advanced/proportion_sweep/main_0xd_k03_s03.py` |  |
| 0.60 | 3/5 | 4 | 0.2239s | 0.0181s | 1 | 8 | yes | 0.2138s | 0.2370s | `detyped_files/nqueens/advanced/proportion_sweep/main_0x1a_k03_s04.py` |  |
| 0.60 | 3/5 | 5 | 0.2203s | 0.0069s | 1 | 8 | yes | 0.2159s | 0.2246s | `detyped_files/nqueens/advanced/proportion_sweep/main_0xb_k03_s05.py` |  |
| 0.60 | 3/5 | 6 | 0.2537s | 0.0207s | 1 | 8 | yes | 0.2438s | 0.2689s | `detyped_files/nqueens/advanced/proportion_sweep/main_0x15_k03_s06.py` |  |
| 0.60 | 3/5 | 7 | 0.2488s | 0.0280s | 1 | 8 | yes | 0.2328s | 0.2681s | `detyped_files/nqueens/advanced/proportion_sweep/main_0x16_k03_s07.py` |  |
| 0.60 | 3/5 | 8 | 0.2552s | 0.0123s | 1 | 8 | yes | 0.2480s | 0.2637s | `detyped_files/nqueens/advanced/proportion_sweep/main_0xe_k03_s08.py` |  |
| 0.60 | 3/5 | 9 | 0.2498s | 0.0102s | 1 | 8 | yes | 0.2436s | 0.2567s | `detyped_files/nqueens/advanced/proportion_sweep/main_0x1c_k03_s09.py` |  |
| 0.60 | 3/5 | 10 | 0.2261s | 0.0216s | 1 | 8 | yes | 0.2155s | 0.2419s | `detyped_files/nqueens/advanced/proportion_sweep/main_0x13_k03_s10.py` |  |
| 0.80 | 4/5 | 1 | 0.2546s | 0.0097s | 1 | 8 | yes | 0.2485s | 0.2608s | `detyped_files/nqueens/advanced/proportion_sweep/main_0xf_k04_s01.py` |  |
| 0.80 | 4/5 | 2 | 0.2518s | 0.0218s | 1 | 8 | yes | 0.2379s | 0.2659s | `detyped_files/nqueens/advanced/proportion_sweep/main_0x1d_k04_s02.py` |  |
| 0.80 | 4/5 | 3 | 0.2337s | 0.0223s | 1 | 8 | yes | 0.2213s | 0.2497s | `detyped_files/nqueens/advanced/proportion_sweep/main_0x1b_k04_s03.py` |  |
| 0.80 | 4/5 | 4 | 0.2549s | 0.0160s | 1 | 8 | yes | 0.2445s | 0.2651s | `detyped_files/nqueens/advanced/proportion_sweep/main_0x1e_k04_s04.py` |  |
| 0.80 | 4/5 | 5 | 0.2633s | 0.0316s | 2 | 16 | yes | 0.2505s | 0.2800s | `detyped_files/nqueens/advanced/proportion_sweep/main_0x17_k04_s05.py` |  |
| 1.00 | 5/5 | 1 | 0.2576s | 0.0155s | 1 | 8 | yes | 0.2493s | 0.2689s | `detyped_files/nqueens/advanced/proportion_sweep/main_0x1f_k05_s01.py` |  |

## nqueens/shallow

- Detypable targets: `3`
- Total runs: `8`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/3 | 1 | 0.2366s | 0.2366s | 0.2366s | 1.0 | yes | ok |
| 0.33 | 1/3 | 3 | 0.2368s | 0.2326s | 0.2397s | 1.0 | yes | ok |
| 0.67 | 2/3 | 3 | 0.2401s | 0.2340s | 0.2463s | 1.0 | yes | ok |
| 1.00 | 3/3 | 1 | 0.2299s | 0.2299s | 0.2299s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/3 | 1 | 0.2366s | 0.0104s | 1 | 8 | yes | 0.2306s | 0.2439s | `detyped_files/nqueens/shallow/proportion_sweep/main_0x0_k00_s01.py` |  |
| 0.33 | 1/3 | 1 | 0.2397s | 0.0274s | 1 | 8 | yes | 0.2228s | 0.2583s | `detyped_files/nqueens/shallow/proportion_sweep/main_0x1_k01_s01.py` |  |
| 0.33 | 1/3 | 2 | 0.2381s | 0.0333s | 1 | 8 | yes | 0.2177s | 0.2612s | `detyped_files/nqueens/shallow/proportion_sweep/main_0x4_k01_s02.py` |  |
| 0.33 | 1/3 | 3 | 0.2326s | 0.0107s | 1 | 8 | yes | 0.2270s | 0.2403s | `detyped_files/nqueens/shallow/proportion_sweep/main_0x2_k01_s03.py` |  |
| 0.67 | 2/3 | 1 | 0.2340s | 0.0063s | 1 | 8 | yes | 0.2303s | 0.2383s | `detyped_files/nqueens/shallow/proportion_sweep/main_0x3_k02_s01.py` |  |
| 0.67 | 2/3 | 2 | 0.2463s | 0.0179s | 1 | 8 | yes | 0.2354s | 0.2583s | `detyped_files/nqueens/shallow/proportion_sweep/main_0x6_k02_s02.py` |  |
| 0.67 | 2/3 | 3 | 0.2402s | 0.0260s | 1 | 8 | yes | 0.2246s | 0.2578s | `detyped_files/nqueens/shallow/proportion_sweep/main_0x5_k02_s03.py` |  |
| 1.00 | 3/3 | 1 | 0.2299s | 0.0200s | 1 | 8 | yes | 0.2172s | 0.2433s | `detyped_files/nqueens/shallow/proportion_sweep/main_0x7_k03_s01.py` |  |

## nqueens/untyped

- Detypable targets: `0`
- Total runs: `1`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.2522s | 0.2522s | 0.2522s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/0 | 1 | 0.2522s | 0.0301s | 1 | 8 | yes | 0.2373s | 0.2740s | `static-python-perf/Benchmark/nqueens/untyped/main.py` |  |

## pystone/advanced

- Detypable targets: `15`
- Total runs: `142`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/15 | 1 | 0.6937s | 0.6937s | 0.6937s | 1.0 | yes | ok |
| 0.07 | 1/15 | 10 | 0.7816s | 0.6655s | 1.4908s | 1.0 | yes | ok |
| 0.13 | 2/15 | 10 | 0.9593s | 0.6389s | 1.5508s | 1.0 | yes | ok |
| 0.20 | 3/15 | 10 | 0.9963s | 0.6654s | 1.7694s | 1.0 | yes | ok |
| 0.27 | 4/15 | 10 | 0.9678s | 0.6697s | 1.5546s | 1.0 | yes | ok |
| 0.33 | 5/15 | 10 | 1.1353s | 0.6498s | 1.5645s | 1.0 | yes | ok |
| 0.40 | 6/15 | 10 | 1.1772s | 0.6535s | 1.7723s | 1.0 | yes | ok |
| 0.47 | 7/15 | 10 | 1.3652s | 0.6583s | 1.9519s | 1.0 | yes | ok |
| 0.53 | 8/15 | 10 | 1.1908s | 0.6559s | 1.7395s | 1.0 | yes | ok |
| 0.60 | 9/15 | 10 | 1.3339s | 0.8296s | 1.8160s | 1.0 | yes | ok |
| 0.67 | 10/15 | 10 | 1.3336s | 0.8160s | 1.9764s | 1.0 | yes | ok |
| 0.73 | 11/15 | 10 | 1.5284s | 1.0991s | 2.0157s | 1.0 | yes | ok |
| 0.80 | 12/15 | 10 | 1.8926s | 1.6073s | 1.9768s | 1.0 | yes | ok |
| 0.87 | 13/15 | 10 | 1.7168s | 1.0959s | 1.9463s | 1.0 | yes | ok |
| 0.93 | 14/15 | 10 | 1.8316s | 1.1029s | 1.9499s | 1.0 | yes | ok |
| 1.00 | 15/15 | 1 | 1.8914s | 1.8914s | 1.8914s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/15 | 1 | 0.6937s | 0.0474s | 1 | 8 | yes | 0.6590s | 0.7189s | `detyped_files/pystone/advanced/proportion_sweep/main_0x0_k00_s01.py` |  |
| 0.07 | 1/15 | 1 | 0.7010s | 0.0413s | 1 | 8 | yes | 0.6750s | 0.7285s | `detyped_files/pystone/advanced/proportion_sweep/main_0x2_k01_s01.py` |  |
| 0.07 | 1/15 | 2 | 0.8251s | 0.0674s | 1 | 8 | yes | 0.7800s | 0.8658s | `detyped_files/pystone/advanced/proportion_sweep/main_0x400_k01_s02.py` |  |
| 0.07 | 1/15 | 3 | 0.6689s | 0.0638s | 1 | 8 | yes | 0.6252s | 0.7089s | `detyped_files/pystone/advanced/proportion_sweep/main_0x40_k01_s03.py` |  |
| 0.07 | 1/15 | 4 | 0.6755s | 0.0562s | 1 | 8 | yes | 0.6377s | 0.7108s | `detyped_files/pystone/advanced/proportion_sweep/main_0x20_k01_s04.py` |  |
| 0.07 | 1/15 | 5 | 0.6820s | 0.0442s | 1 | 8 | yes | 0.6531s | 0.7102s | `detyped_files/pystone/advanced/proportion_sweep/main_0x800_k01_s05.py` |  |
| 0.07 | 1/15 | 6 | 0.7196s | 0.0679s | 1 | 8 | yes | 0.6732s | 0.7618s | `detyped_files/pystone/advanced/proportion_sweep/main_0x80_k01_s06.py` |  |
| 0.07 | 1/15 | 7 | 0.6889s | 0.0609s | 1 | 8 | yes | 0.6477s | 0.7252s | `detyped_files/pystone/advanced/proportion_sweep/main_0x200_k01_s07.py` |  |
| 0.07 | 1/15 | 8 | 1.4908s | 0.0838s | 1 | 8 | yes | 1.4367s | 1.5443s | `detyped_files/pystone/advanced/proportion_sweep/main_0x8_k01_s08.py` |  |
| 0.07 | 1/15 | 9 | 0.6655s | 0.0625s | 1 | 8 | yes | 0.6241s | 0.7066s | `detyped_files/pystone/advanced/proportion_sweep/main_0x4_k01_s09.py` |  |
| 0.07 | 1/15 | 10 | 0.6985s | 0.0295s | 1 | 8 | yes | 0.6804s | 0.7185s | `detyped_files/pystone/advanced/proportion_sweep/main_0x1_k01_s10.py` |  |
| 0.13 | 2/15 | 1 | 0.6812s | 0.0869s | 1 | 8 | yes | 0.6207s | 0.7324s | `detyped_files/pystone/advanced/proportion_sweep/main_0x90_k02_s01.py` |  |
| 0.13 | 2/15 | 2 | 0.9974s | 0.0985s | 1 | 8 | yes | 0.9409s | 1.0658s | `detyped_files/pystone/advanced/proportion_sweep/main_0x1100_k02_s02.py` |  |
| 0.13 | 2/15 | 3 | 0.7021s | 0.0368s | 1 | 8 | yes | 0.6758s | 0.7227s | `detyped_files/pystone/advanced/proportion_sweep/main_0x42_k02_s03.py` |  |
| 0.13 | 2/15 | 4 | 0.6851s | 0.0415s | 1 | 8 | yes | 0.6575s | 0.7108s | `detyped_files/pystone/advanced/proportion_sweep/main_0x2040_k02_s04.py` |  |
| 0.13 | 2/15 | 5 | 1.5508s | 0.0929s | 1 | 8 | yes | 1.4959s | 1.6133s | `detyped_files/pystone/advanced/proportion_sweep/main_0x18_k02_s05.py` |  |
| 0.13 | 2/15 | 6 | 1.4944s | 0.1308s | 1 | 8 | yes | 1.4131s | 1.5855s | `detyped_files/pystone/advanced/proportion_sweep/main_0x48_k02_s06.py` |  |
| 0.13 | 2/15 | 7 | 1.0380s | 0.1294s | 1 | 8 | yes | 0.9538s | 1.1186s | `detyped_files/pystone/advanced/proportion_sweep/main_0x180_k02_s07.py` |  |
| 0.13 | 2/15 | 8 | 0.6389s | 0.0658s | 1 | 8 | yes | 0.5971s | 0.6808s | `detyped_files/pystone/advanced/proportion_sweep/main_0x2020_k02_s08.py` |  |
| 0.13 | 2/15 | 9 | 0.8286s | 0.0814s | 1 | 8 | yes | 0.7744s | 0.8780s | `detyped_files/pystone/advanced/proportion_sweep/main_0xc00_k02_s09.py` |  |
| 0.13 | 2/15 | 10 | 0.9767s | 0.0821s | 1 | 8 | yes | 0.9256s | 1.0335s | `detyped_files/pystone/advanced/proportion_sweep/main_0x120_k02_s10.py` |  |
| 0.20 | 3/15 | 1 | 1.0271s | 0.0585s | 1 | 8 | yes | 0.9916s | 1.0663s | `detyped_files/pystone/advanced/proportion_sweep/main_0x2900_k03_s01.py` |  |
| 0.20 | 3/15 | 2 | 0.6679s | 0.0563s | 1 | 8 | yes | 0.6288s | 0.7001s | `detyped_files/pystone/advanced/proportion_sweep/main_0x830_k03_s02.py` |  |
| 0.20 | 3/15 | 3 | 0.7034s | 0.0255s | 1 | 8 | yes | 0.6872s | 0.7203s | `detyped_files/pystone/advanced/proportion_sweep/main_0xe0_k03_s03.py` |  |
| 0.20 | 3/15 | 4 | 0.6654s | 0.0436s | 1 | 8 | yes | 0.6367s | 0.6925s | `detyped_files/pystone/advanced/proportion_sweep/main_0x806_k03_s04.py` |  |
| 0.20 | 3/15 | 5 | 0.8254s | 0.0595s | 1 | 8 | yes | 0.7823s | 0.8601s | `detyped_files/pystone/advanced/proportion_sweep/main_0x4420_k03_s05.py` |  |
| 0.20 | 3/15 | 6 | 1.4985s | 0.0633s | 1 | 8 | yes | 1.4605s | 1.5423s | `detyped_files/pystone/advanced/proportion_sweep/main_0xd_k03_s06.py` |  |
| 0.20 | 3/15 | 7 | 1.1642s | 0.1031s | 1 | 8 | yes | 1.1023s | 1.2325s | `detyped_files/pystone/advanced/proportion_sweep/main_0x502_k03_s07.py` |  |
| 0.20 | 3/15 | 8 | 0.8235s | 0.0455s | 1 | 8 | yes | 0.7930s | 0.8503s | `detyped_files/pystone/advanced/proportion_sweep/main_0x602_k03_s08.py` |  |
| 0.20 | 3/15 | 9 | 0.8178s | 0.0544s | 1 | 8 | yes | 0.7780s | 0.8429s | `detyped_files/pystone/advanced/proportion_sweep/main_0x4c00_k03_s09.py` |  |
| 0.20 | 3/15 | 10 | 1.7694s | 0.0873s | 1 | 8 | yes | 1.7149s | 1.8262s | `detyped_files/pystone/advanced/proportion_sweep/main_0x908_k03_s10.py` |  |
| 0.27 | 4/15 | 1 | 0.6930s | 0.0583s | 1 | 8 | yes | 0.6529s | 0.7285s | `detyped_files/pystone/advanced/proportion_sweep/main_0x6204_k04_s01.py` |  |
| 0.27 | 4/15 | 2 | 0.6697s | 0.0641s | 1 | 8 | yes | 0.6271s | 0.7104s | `detyped_files/pystone/advanced/proportion_sweep/main_0x5280_k04_s02.py` |  |
| 0.27 | 4/15 | 3 | 1.4508s | 0.0591s | 1 | 8 | yes | 1.4113s | 1.4871s | `detyped_files/pystone/advanced/proportion_sweep/main_0x59_k04_s03.py` |  |
| 0.27 | 4/15 | 4 | 1.5546s | 0.0811s | 1 | 8 | yes | 1.5032s | 1.6069s | `detyped_files/pystone/advanced/proportion_sweep/main_0x600c_k04_s04.py` |  |
| 0.27 | 4/15 | 5 | 1.1586s | 0.0715s | 1 | 8 | yes | 1.1161s | 1.2067s | `detyped_files/pystone/advanced/proportion_sweep/main_0x584_k04_s05.py` |  |
| 0.27 | 4/15 | 6 | 0.9470s | 0.0455s | 1 | 8 | yes | 0.9199s | 0.9781s | `detyped_files/pystone/advanced/proportion_sweep/main_0x1c4_k04_s06.py` |  |
| 0.27 | 4/15 | 7 | 0.6961s | 0.0446s | 1 | 8 | yes | 0.6648s | 0.7218s | `detyped_files/pystone/advanced/proportion_sweep/main_0x7010_k04_s07.py` |  |
| 0.27 | 4/15 | 8 | 0.9767s | 0.0784s | 1 | 8 | yes | 0.9217s | 1.0222s | `detyped_files/pystone/advanced/proportion_sweep/main_0x321_k04_s08.py` |  |
| 0.27 | 4/15 | 9 | 0.8286s | 0.0520s | 1 | 8 | yes | 0.7947s | 0.8626s | `detyped_files/pystone/advanced/proportion_sweep/main_0xc44_k04_s09.py` |  |
| 0.27 | 4/15 | 10 | 0.7032s | 0.0633s | 1 | 8 | yes | 0.6616s | 0.7437s | `detyped_files/pystone/advanced/proportion_sweep/main_0x246_k04_s10.py` |  |
| 0.33 | 5/15 | 1 | 0.6791s | 0.0790s | 1 | 8 | yes | 0.6263s | 0.7285s | `detyped_files/pystone/advanced/proportion_sweep/main_0x2e1_k05_s01.py` |  |
| 0.33 | 5/15 | 2 | 1.5012s | 0.0396s | 1 | 8 | yes | 1.4755s | 1.5270s | `detyped_files/pystone/advanced/proportion_sweep/main_0x5089_k05_s02.py` |  |
| 0.33 | 5/15 | 3 | 0.8071s | 0.0802s | 1 | 8 | yes | 0.7579s | 0.8609s | `detyped_files/pystone/advanced/proportion_sweep/main_0xe05_k05_s03.py` |  |
| 0.33 | 5/15 | 4 | 1.5281s | 0.0836s | 1 | 8 | yes | 1.4784s | 1.5856s | `detyped_files/pystone/advanced/proportion_sweep/main_0x2a9_k05_s04.py` |  |
| 0.33 | 5/15 | 5 | 1.4819s | 0.0688s | 1 | 8 | yes | 1.4318s | 1.5165s | `detyped_files/pystone/advanced/proportion_sweep/main_0x422a_k05_s05.py` |  |
| 0.33 | 5/15 | 6 | 0.8119s | 0.1093s | 1 | 8 | yes | 0.7432s | 0.8858s | `detyped_files/pystone/advanced/proportion_sweep/main_0x6b0_k05_s06.py` |  |
| 0.33 | 5/15 | 7 | 1.5057s | 0.1502s | 1 | 8 | yes | 1.4104s | 1.6042s | `detyped_files/pystone/advanced/proportion_sweep/main_0x204d_k05_s07.py` |  |
| 0.33 | 5/15 | 8 | 0.8240s | 0.0413s | 1 | 8 | yes | 0.7946s | 0.8502s | `detyped_files/pystone/advanced/proportion_sweep/main_0x1464_k05_s08.py` |  |
| 0.33 | 5/15 | 9 | 1.5645s | 0.0525s | 1 | 8 | yes | 1.5294s | 1.5966s | `detyped_files/pystone/advanced/proportion_sweep/main_0x2489_k05_s09.py` |  |
| 0.33 | 5/15 | 10 | 0.6498s | 0.0630s | 1 | 8 | yes | 0.6092s | 0.6906s | `detyped_files/pystone/advanced/proportion_sweep/main_0x1a11_k05_s10.py` |  |
| 0.40 | 6/15 | 1 | 1.1395s | 0.1315s | 1 | 8 | yes | 1.0613s | 1.2312s | `detyped_files/pystone/advanced/proportion_sweep/main_0xd43_k06_s01.py` |  |
| 0.40 | 6/15 | 2 | 1.6662s | 0.1768s | 1 | 8 | yes | 1.5787s | 1.7982s | `detyped_files/pystone/advanced/proportion_sweep/main_0x24cc_k06_s02.py` |  |
| 0.40 | 6/15 | 3 | 1.4682s | 0.0701s | 1 | 8 | yes | 1.4226s | 1.5128s | `detyped_files/pystone/advanced/proportion_sweep/main_0x5258_k06_s03.py` |  |
| 0.40 | 6/15 | 4 | 0.6795s | 0.0467s | 1 | 8 | yes | 0.6453s | 0.7036s | `detyped_files/pystone/advanced/proportion_sweep/main_0x18d2_k06_s04.py` |  |
| 0.40 | 6/15 | 5 | 1.7723s | 0.0532s | 1 | 8 | yes | 1.7382s | 1.8068s | `detyped_files/pystone/advanced/proportion_sweep/main_0x5918_k06_s05.py` |  |
| 0.40 | 6/15 | 6 | 1.0887s | 0.0638s | 1 | 8 | yes | 1.0491s | 1.1310s | `detyped_files/pystone/advanced/proportion_sweep/main_0x6541_k06_s06.py` |  |
| 0.40 | 6/15 | 7 | 0.6535s | 0.0803s | 1 | 8 | yes | 0.6007s | 0.7040s | `detyped_files/pystone/advanced/proportion_sweep/main_0x5807_k06_s07.py` |  |
| 0.40 | 6/15 | 8 | 0.8101s | 0.0657s | 1 | 8 | yes | 0.7689s | 0.8527s | `detyped_files/pystone/advanced/proportion_sweep/main_0x4cd0_k06_s08.py` |  |
| 0.40 | 6/15 | 9 | 0.9866s | 0.0409s | 1 | 8 | yes | 0.9629s | 1.0152s | `detyped_files/pystone/advanced/proportion_sweep/main_0x6154_k06_s09.py` |  |
| 0.40 | 6/15 | 10 | 1.5074s | 0.1737s | 1 | 8 | yes | 1.4160s | 1.6321s | `detyped_files/pystone/advanced/proportion_sweep/main_0x1a2a_k06_s10.py` |  |
| 0.47 | 7/15 | 1 | 0.6583s | 0.0571s | 1 | 8 | yes | 0.6200s | 0.6931s | `detyped_files/pystone/advanced/proportion_sweep/main_0x2ab4_k07_s01.py` |  |
| 0.47 | 7/15 | 2 | 1.8313s | 0.0973s | 1 | 8 | yes | 1.7724s | 1.8977s | `detyped_files/pystone/advanced/proportion_sweep/main_0x5b18_k07_s02.py` |  |
| 0.47 | 7/15 | 3 | 1.5831s | 0.0460s | 1 | 8 | yes | 1.5517s | 1.6109s | `detyped_files/pystone/advanced/proportion_sweep/main_0xcda_k07_s03.py` |  |
| 0.47 | 7/15 | 4 | 1.9519s | 0.0382s | 1 | 8 | yes | 1.9269s | 1.9765s | `detyped_files/pystone/advanced/proportion_sweep/main_0x45c9_k07_s04.py` |  |
| 0.47 | 7/15 | 5 | 1.0913s | 0.0498s | 1 | 8 | yes | 1.0574s | 1.1214s | `detyped_files/pystone/advanced/proportion_sweep/main_0x2d25_k07_s05.py` |  |
| 0.47 | 7/15 | 6 | 1.5927s | 0.0571s | 1 | 8 | yes | 1.5572s | 1.6306s | `detyped_files/pystone/advanced/proportion_sweep/main_0x641e_k07_s06.py` |  |
| 0.47 | 7/15 | 7 | 1.6246s | 0.0593s | 1 | 8 | yes | 1.5878s | 1.6637s | `detyped_files/pystone/advanced/proportion_sweep/main_0x541b_k07_s07.py` |  |
| 0.47 | 7/15 | 8 | 1.4987s | 0.0785s | 1 | 8 | yes | 1.4502s | 1.5512s | `detyped_files/pystone/advanced/proportion_sweep/main_0x58e8_k07_s08.py` |  |
| 0.47 | 7/15 | 9 | 0.8363s | 0.0517s | 1 | 8 | yes | 0.8020s | 0.8698s | `detyped_files/pystone/advanced/proportion_sweep/main_0xec5_k07_s09.py` |  |
| 0.47 | 7/15 | 10 | 0.9839s | 0.0255s | 1 | 8 | yes | 0.9682s | 1.0017s | `detyped_files/pystone/advanced/proportion_sweep/main_0x2ba1_k07_s10.py` |  |
| 0.53 | 8/15 | 1 | 0.8823s | 0.0769s | 1 | 8 | yes | 0.8346s | 0.9346s | `detyped_files/pystone/advanced/proportion_sweep/main_0x6ca6_k08_s01.py` |  |
| 0.53 | 8/15 | 2 | 1.0998s | 0.0764s | 1 | 8 | yes | 1.0464s | 1.1459s | `detyped_files/pystone/advanced/proportion_sweep/main_0x2755_k08_s02.py` |  |
| 0.53 | 8/15 | 3 | 0.6559s | 0.0504s | 1 | 8 | yes | 0.6212s | 0.6858s | `detyped_files/pystone/advanced/proportion_sweep/main_0x6873_k08_s03.py` |  |
| 0.53 | 8/15 | 4 | 1.1563s | 0.1091s | 1 | 8 | yes | 1.0876s | 1.2281s | `detyped_files/pystone/advanced/proportion_sweep/main_0x4db1_k08_s04.py` |  |
| 0.53 | 8/15 | 5 | 0.6761s | 0.0458s | 1 | 8 | yes | 0.6453s | 0.7057s | `detyped_files/pystone/advanced/proportion_sweep/main_0x7a07_k08_s05.py` |  |
| 0.53 | 8/15 | 6 | 1.6296s | 0.1080s | 1 | 8 | yes | 1.5660s | 1.7043s | `detyped_files/pystone/advanced/proportion_sweep/main_0x6ec8_k08_s06.py` |  |
| 0.53 | 8/15 | 7 | 1.6003s | 0.0710s | 1 | 8 | yes | 1.5553s | 1.6479s | `detyped_files/pystone/advanced/proportion_sweep/main_0x6dd_k08_s07.py` |  |
| 0.53 | 8/15 | 8 | 0.9741s | 0.0338s | 1 | 8 | yes | 0.9560s | 0.9979s | `detyped_files/pystone/advanced/proportion_sweep/main_0x4ba3_k08_s08.py` |  |
| 0.53 | 8/15 | 9 | 1.4944s | 0.0555s | 1 | 8 | yes | 1.4541s | 1.5261s | `detyped_files/pystone/advanced/proportion_sweep/main_0x3ac9_k08_s09.py` |  |
| 0.53 | 8/15 | 10 | 1.7395s | 0.0685s | 1 | 8 | yes | 1.6939s | 1.7818s | `detyped_files/pystone/advanced/proportion_sweep/main_0x236d_k08_s10.py` |  |
| 0.60 | 9/15 | 1 | 1.6297s | 0.0770s | 1 | 8 | yes | 1.5780s | 1.6778s | `detyped_files/pystone/advanced/proportion_sweep/main_0x1ed9_k09_s01.py` |  |
| 0.60 | 9/15 | 2 | 0.8628s | 0.0353s | 1 | 8 | yes | 0.8405s | 0.8863s | `detyped_files/pystone/advanced/proportion_sweep/main_0x7687_k09_s02.py` |  |
| 0.60 | 9/15 | 3 | 1.8131s | 0.0800s | 1 | 8 | yes | 1.7617s | 1.8644s | `detyped_files/pystone/advanced/proportion_sweep/main_0x63dc_k09_s03.py` |  |
| 0.60 | 9/15 | 4 | 1.5965s | 0.1165s | 1 | 8 | yes | 1.5272s | 1.6754s | `detyped_files/pystone/advanced/proportion_sweep/main_0x6ccb_k09_s04.py` |  |
| 0.60 | 9/15 | 5 | 1.8160s | 0.0958s | 1 | 8 | yes | 1.7543s | 1.8778s | `detyped_files/pystone/advanced/proportion_sweep/main_0x5b4d_k09_s05.py` |  |
| 0.60 | 9/15 | 6 | 0.8296s | 0.0212s | 1 | 8 | yes | 0.8152s | 0.8425s | `detyped_files/pystone/advanced/proportion_sweep/main_0x76a3_k09_s06.py` |  |
| 0.60 | 9/15 | 7 | 1.1316s | 0.0729s | 1 | 8 | yes | 1.0914s | 1.1838s | `detyped_files/pystone/advanced/proportion_sweep/main_0x1f66_k09_s07.py` |  |
| 0.60 | 9/15 | 8 | 1.0495s | 0.0684s | 1 | 8 | yes | 1.0057s | 1.0933s | `detyped_files/pystone/advanced/proportion_sweep/main_0x77c2_k09_s08.py` |  |
| 0.60 | 9/15 | 9 | 0.9491s | 0.0910s | 1 | 8 | yes | 0.8945s | 1.0104s | `detyped_files/pystone/advanced/proportion_sweep/main_0x23f6_k09_s09.py` |  |
| 0.60 | 9/15 | 10 | 1.6612s | 0.0934s | 1 | 8 | yes | 1.6000s | 1.7192s | `detyped_files/pystone/advanced/proportion_sweep/main_0x56dc_k09_s10.py` |  |
| 0.67 | 10/15 | 1 | 1.7962s | 0.0797s | 1 | 8 | yes | 1.7434s | 1.8478s | `detyped_files/pystone/advanced/proportion_sweep/main_0x336f_k10_s01.py` |  |
| 0.67 | 10/15 | 2 | 1.9764s | 0.0948s | 1 | 8 | yes | 1.9211s | 2.0407s | `detyped_files/pystone/advanced/proportion_sweep/main_0x1f1f_k10_s02.py` |  |
| 0.67 | 10/15 | 3 | 0.8160s | 0.0672s | 1 | 8 | yes | 0.7711s | 0.8578s | `detyped_files/pystone/advanced/proportion_sweep/main_0x6cb7_k10_s03.py` |  |
| 0.67 | 10/15 | 4 | 1.1067s | 0.0678s | 1 | 8 | yes | 1.0690s | 1.1549s | `detyped_files/pystone/advanced/proportion_sweep/main_0x5776_k10_s04.py` |  |
| 0.67 | 10/15 | 5 | 0.8264s | 0.0739s | 1 | 8 | yes | 0.7837s | 0.8789s | `detyped_files/pystone/advanced/proportion_sweep/main_0x3677_k10_s05.py` |  |
| 0.67 | 10/15 | 6 | 1.0936s | 0.0526s | 1 | 8 | yes | 1.0584s | 1.1276s | `detyped_files/pystone/advanced/proportion_sweep/main_0x75e3_k10_s06.py` |  |
| 0.67 | 10/15 | 7 | 1.1147s | 0.1032s | 1 | 8 | yes | 1.0516s | 1.1857s | `detyped_files/pystone/advanced/proportion_sweep/main_0x3f96_k10_s07.py` |  |
| 0.67 | 10/15 | 8 | 1.7948s | 0.0723s | 1 | 8 | yes | 1.7464s | 1.8393s | `detyped_files/pystone/advanced/proportion_sweep/main_0x19ef_k10_s08.py` |  |
| 0.67 | 10/15 | 9 | 1.8309s | 0.1289s | 1 | 8 | yes | 1.7444s | 1.9105s | `detyped_files/pystone/advanced/proportion_sweep/main_0x6bf8_k10_s09.py` |  |
| 0.67 | 10/15 | 10 | 0.9804s | 0.0770s | 1 | 8 | yes | 0.9356s | 1.0345s | `detyped_files/pystone/advanced/proportion_sweep/main_0x7be2_k10_s10.py` |  |
| 0.73 | 11/15 | 1 | 1.1095s | 0.0683s | 1 | 8 | yes | 1.0717s | 1.1587s | `detyped_files/pystone/advanced/proportion_sweep/main_0x2fd7_k11_s01.py` |  |
| 0.73 | 11/15 | 2 | 2.0157s | 0.0654s | 1 | 8 | yes | 1.9813s | 2.0642s | `detyped_files/pystone/advanced/proportion_sweep/main_0x27fe_k11_s02.py` |  |
| 0.73 | 11/15 | 3 | 1.6688s | 0.1044s | 1 | 8 | yes | 1.6063s | 1.7410s | `detyped_files/pystone/advanced/proportion_sweep/main_0x6e5f_k11_s03.py` |  |
| 0.73 | 11/15 | 4 | 1.0991s | 0.0619s | 1 | 8 | yes | 1.0573s | 1.1363s | `detyped_files/pystone/advanced/proportion_sweep/main_0x6fd5_k11_s04.py` |  |
| 0.73 | 11/15 | 5 | 1.1213s | 0.0584s | 1 | 8 | yes | 1.0859s | 1.1613s | `detyped_files/pystone/advanced/proportion_sweep/main_0x6dd7_k11_s05.py` |  |
| 0.73 | 11/15 | 6 | 1.8487s | 0.0686s | 1 | 8 | yes | 1.8114s | 1.8987s | `detyped_files/pystone/advanced/proportion_sweep/main_0x3bcf_k11_s06.py` |  |
| 0.73 | 11/15 | 7 | 1.8059s | 0.0742s | 1 | 8 | yes | 1.7561s | 1.8507s | `detyped_files/pystone/advanced/proportion_sweep/main_0x3b7e_k11_s07.py` |  |
| 0.73 | 11/15 | 8 | 1.5374s | 0.1160s | 1 | 8 | yes | 1.4741s | 1.6216s | `detyped_files/pystone/advanced/proportion_sweep/main_0x7aeb_k11_s08.py` |  |
| 0.73 | 11/15 | 9 | 1.1465s | 0.0960s | 1 | 8 | yes | 1.0930s | 1.2149s | `detyped_files/pystone/advanced/proportion_sweep/main_0x6df3_k11_s09.py` |  |
| 0.73 | 11/15 | 10 | 1.9313s | 0.0540s | 1 | 8 | yes | 1.8965s | 1.9670s | `detyped_files/pystone/advanced/proportion_sweep/main_0x4f7d_k11_s10.py` |  |
| 0.80 | 12/15 | 1 | 1.9539s | 0.1226s | 1 | 8 | yes | 1.8733s | 2.0324s | `detyped_files/pystone/advanced/proportion_sweep/main_0x3fdb_k12_s01.py` |  |
| 0.80 | 12/15 | 2 | 1.9243s | 0.0647s | 1 | 8 | yes | 1.8810s | 1.9634s | `detyped_files/pystone/advanced/proportion_sweep/main_0x7fce_k12_s02.py` |  |
| 0.80 | 12/15 | 3 | 1.9768s | 0.0585s | 1 | 8 | yes | 1.9386s | 2.0145s | `detyped_files/pystone/advanced/proportion_sweep/main_0x35ff_k12_s03.py` |  |
| 0.80 | 12/15 | 4 | 1.9351s | 0.0506s | 1 | 8 | yes | 1.9004s | 1.9653s | `detyped_files/pystone/advanced/proportion_sweep/main_0xfff_k12_s04.py` |  |
| 0.80 | 12/15 | 5 | 1.9239s | 0.0379s | 1 | 8 | yes | 1.8986s | 1.9473s | `detyped_files/pystone/advanced/proportion_sweep/main_0x75fb_k12_s05.py` |  |
| 0.80 | 12/15 | 6 | 1.7738s | 0.0471s | 1 | 8 | yes | 1.7455s | 1.8053s | `detyped_files/pystone/advanced/proportion_sweep/main_0x3bfe_k12_s06.py` |  |
| 0.80 | 12/15 | 7 | 1.6073s | 0.0833s | 1 | 8 | yes | 1.5528s | 1.6610s | `detyped_files/pystone/advanced/proportion_sweep/main_0x7ebe_k12_s07.py` |  |
| 0.80 | 12/15 | 8 | 1.9699s | 0.0594s | 1 | 8 | yes | 1.9305s | 2.0077s | `detyped_files/pystone/advanced/proportion_sweep/main_0x77ed_k12_s08.py` |  |
| 0.80 | 12/15 | 9 | 1.9411s | 0.1037s | 1 | 8 | yes | 1.8777s | 2.0107s | `detyped_files/pystone/advanced/proportion_sweep/main_0x3f3f_k12_s09.py` |  |
| 0.80 | 12/15 | 10 | 1.9204s | 0.1065s | 1 | 8 | yes | 1.8600s | 1.9981s | `detyped_files/pystone/advanced/proportion_sweep/main_0x77fc_k12_s10.py` |  |
| 0.87 | 13/15 | 1 | 1.9463s | 0.0959s | 1 | 8 | yes | 1.8907s | 2.0148s | `detyped_files/pystone/advanced/proportion_sweep/main_0x5fef_k13_s01.py` |  |
| 0.87 | 13/15 | 2 | 1.9389s | 0.0712s | 1 | 8 | yes | 1.8963s | 1.9888s | `detyped_files/pystone/advanced/proportion_sweep/main_0x3ffb_k13_s02.py` |  |
| 0.87 | 13/15 | 3 | 1.5743s | 0.1272s | 1 | 8 | yes | 1.4999s | 1.6624s | `detyped_files/pystone/advanced/proportion_sweep/main_0x7edf_k13_s03.py` |  |
| 0.87 | 13/15 | 4 | 1.7643s | 0.0635s | 1 | 8 | yes | 1.7223s | 1.8035s | `detyped_files/pystone/advanced/proportion_sweep/main_0x7b7f_k13_s04.py` |  |
| 0.87 | 13/15 | 5 | 1.6055s | 0.0763s | 1 | 8 | yes | 1.5544s | 1.6529s | `detyped_files/pystone/advanced/proportion_sweep/main_0x7efb_k13_s05.py` |  |
| 0.87 | 13/15 | 6 | 1.8974s | 0.0658s | 1 | 8 | yes | 1.8546s | 1.9387s | `detyped_files/pystone/advanced/proportion_sweep/main_0x7fcf_k13_s06.py` |  |
| 0.87 | 13/15 | 7 | 1.6282s | 0.0975s | 1 | 8 | yes | 1.5693s | 1.6951s | `detyped_files/pystone/advanced/proportion_sweep/main_0x7e7f_k13_s07.py` |  |
| 0.87 | 13/15 | 8 | 1.0959s | 0.0914s | 1 | 8 | yes | 1.0376s | 1.1533s | `detyped_files/pystone/advanced/proportion_sweep/main_0x7f77_k13_s08.py` |  |
| 0.87 | 13/15 | 9 | 1.7882s | 0.0896s | 1 | 8 | yes | 1.7300s | 1.8463s | `detyped_files/pystone/advanced/proportion_sweep/main_0x7bbf_k13_s09.py` |  |
| 0.87 | 13/15 | 10 | 1.9286s | 0.0606s | 1 | 8 | yes | 1.8910s | 1.9692s | `detyped_files/pystone/advanced/proportion_sweep/main_0x6fbf_k13_s10.py` |  |
| 0.93 | 14/15 | 1 | 1.9495s | 0.0546s | 1 | 8 | yes | 1.9142s | 1.9841s | `detyped_files/pystone/advanced/proportion_sweep/main_0x7ffe_k14_s01.py` |  |
| 0.93 | 14/15 | 2 | 1.8934s | 0.0585s | 1 | 8 | yes | 1.8531s | 1.9303s | `detyped_files/pystone/advanced/proportion_sweep/main_0x77ff_k14_s02.py` |  |
| 0.93 | 14/15 | 3 | 1.9175s | 0.0755s | 1 | 8 | yes | 1.8709s | 1.9694s | `detyped_files/pystone/advanced/proportion_sweep/main_0x7ffb_k14_s03.py` |  |
| 0.93 | 14/15 | 4 | 1.1029s | 0.1351s | 1 | 8 | yes | 1.0248s | 1.1986s | `detyped_files/pystone/advanced/proportion_sweep/main_0x7ff7_k14_s04.py` |  |
| 0.93 | 14/15 | 5 | 1.9499s | 0.0516s | 1 | 8 | yes | 1.9183s | 1.9853s | `detyped_files/pystone/advanced/proportion_sweep/main_0x7fef_k14_s05.py` |  |
| 0.93 | 14/15 | 6 | 1.9283s | 0.1040s | 1 | 8 | yes | 1.8622s | 1.9965s | `detyped_files/pystone/advanced/proportion_sweep/main_0x7dff_k14_s06.py` |  |
| 0.93 | 14/15 | 7 | 1.9426s | 0.0675s | 1 | 8 | yes | 1.8985s | 1.9838s | `detyped_files/pystone/advanced/proportion_sweep/main_0x3fff_k14_s07.py` |  |
| 0.93 | 14/15 | 8 | 1.8005s | 0.0497s | 1 | 8 | yes | 1.7713s | 1.8352s | `detyped_files/pystone/advanced/proportion_sweep/main_0x7bff_k14_s08.py` |  |
| 0.93 | 14/15 | 9 | 1.9100s | 0.0293s | 1 | 8 | yes | 1.8903s | 1.9286s | `detyped_files/pystone/advanced/proportion_sweep/main_0x7ffd_k14_s09.py` |  |
| 0.93 | 14/15 | 10 | 1.9216s | 0.0792s | 1 | 8 | yes | 1.8672s | 1.9672s | `detyped_files/pystone/advanced/proportion_sweep/main_0x6fff_k14_s10.py` |  |
| 1.00 | 15/15 | 1 | 1.8914s | 0.0477s | 1 | 8 | yes | 1.8592s | 1.9204s | `detyped_files/pystone/advanced/proportion_sweep/main_0x7fff_k15_s01.py` |  |

## pystone/shallow

- Detypable targets: `15`
- Total runs: `142`

### Summary

| proportion | detyped | samples | mean time | min | max | avg batches | all converged | status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.00 | 0/15 | 1 | 0.6738s | 0.6738s | 0.6738s | 1.0 | yes | ok |
| 0.07 | 1/15 | 10 | 0.6823s | 0.6366s | 0.8448s | 1.0 | yes | ok |
| 0.13 | 2/15 | 10 | 0.7563s | 0.6570s | 1.0634s | 1.0 | yes | ok |
| 0.20 | 3/15 | 10 | 0.7874s | 0.6230s | 1.0925s | 1.0 | yes | ok |
| 0.27 | 4/15 | 10 | 0.8879s | 0.6741s | 1.1234s | 1.0 | yes | ok |
| 0.33 | 5/15 | 10 | 0.8838s | 0.6443s | 1.2655s | 1.0 | yes | ok |
| 0.40 | 6/15 | 10 | 1.0223s | 0.6589s | 1.3845s | 1.0 | yes | ok |
| 0.47 | 7/15 | 10 | 0.9018s | 0.6657s | 1.3406s | 1.0 | yes | ok |
| 0.53 | 8/15 | 10 | 1.0383s | 0.8234s | 1.3120s | 1.0 | yes | ok |
| 0.60 | 9/15 | 10 | 1.1298s | 0.6642s | 1.4998s | 1.0 | yes | ok |
| 0.67 | 10/15 | 10 | 1.2741s | 0.8070s | 1.5049s | 1.0 | yes | ok |
| 0.73 | 11/15 | 10 | 1.1755s | 0.6959s | 1.4967s | 1.0 | yes | ok |
| 0.80 | 12/15 | 10 | 1.2780s | 1.0549s | 1.5103s | 1.0 | yes | ok |
| 0.87 | 13/15 | 10 | 1.4613s | 1.0696s | 1.5604s | 1.0 | yes | ok |
| 0.93 | 14/15 | 10 | 1.4226s | 1.0698s | 1.5504s | 1.0 | yes | ok |
| 1.00 | 15/15 | 1 | 1.5468s | 1.5468s | 1.5468s | 1.0 | yes | ok |

### Detailed Runs

| proportion | detyped | sample | mean time | stdev | batches | total samples | converged | ci lower | ci upper | artifact | notes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| 0.00 | 0/15 | 1 | 0.6738s | 0.0539s | 1 | 8 | yes | 0.6365s | 0.7069s | `detyped_files/pystone/shallow/proportion_sweep/main_0x0_k00_s01.py` |  |
| 0.07 | 1/15 | 1 | 0.8448s | 0.0348s | 1 | 8 | yes | 0.8227s | 0.8667s | `detyped_files/pystone/shallow/proportion_sweep/main_0x400_k01_s01.py` |  |
| 0.07 | 1/15 | 2 | 0.7121s | 0.0325s | 1 | 8 | yes | 0.6890s | 0.7306s | `detyped_files/pystone/shallow/proportion_sweep/main_0x20_k01_s02.py` |  |
| 0.07 | 1/15 | 3 | 0.6366s | 0.0703s | 1 | 8 | yes | 0.5937s | 0.6830s | `detyped_files/pystone/shallow/proportion_sweep/main_0x4_k01_s03.py` |  |
| 0.07 | 1/15 | 4 | 0.6570s | 0.0698s | 1 | 8 | yes | 0.6111s | 0.7008s | `detyped_files/pystone/shallow/proportion_sweep/main_0x1000_k01_s04.py` |  |
| 0.07 | 1/15 | 5 | 0.6771s | 0.0190s | 1 | 8 | yes | 0.6648s | 0.6894s | `detyped_files/pystone/shallow/proportion_sweep/main_0x1_k01_s05.py` |  |
| 0.07 | 1/15 | 6 | 0.6468s | 0.0680s | 1 | 8 | yes | 0.5999s | 0.6877s | `detyped_files/pystone/shallow/proportion_sweep/main_0x800_k01_s06.py` |  |
| 0.07 | 1/15 | 7 | 0.6798s | 0.0390s | 1 | 8 | yes | 0.6592s | 0.7086s | `detyped_files/pystone/shallow/proportion_sweep/main_0x200_k01_s07.py` |  |
| 0.07 | 1/15 | 8 | 0.6457s | 0.0727s | 1 | 8 | yes | 0.5979s | 0.6923s | `detyped_files/pystone/shallow/proportion_sweep/main_0x80_k01_s08.py` |  |
| 0.07 | 1/15 | 9 | 0.6849s | 0.0303s | 1 | 8 | yes | 0.6665s | 0.7051s | `detyped_files/pystone/shallow/proportion_sweep/main_0x40_k01_s09.py` |  |
| 0.07 | 1/15 | 10 | 0.6380s | 0.0589s | 1 | 8 | yes | 0.5988s | 0.6765s | `detyped_files/pystone/shallow/proportion_sweep/main_0x10_k01_s10.py` |  |
| 0.13 | 2/15 | 1 | 0.8222s | 0.0384s | 1 | 8 | yes | 0.7968s | 0.8461s | `detyped_files/pystone/shallow/proportion_sweep/main_0xc00_k02_s01.py` |  |
| 0.13 | 2/15 | 2 | 0.6570s | 0.0628s | 1 | 8 | yes | 0.6144s | 0.6944s | `detyped_files/pystone/shallow/proportion_sweep/main_0x240_k02_s02.py` |  |
| 0.13 | 2/15 | 3 | 0.6572s | 0.0346s | 1 | 8 | yes | 0.6343s | 0.6788s | `detyped_files/pystone/shallow/proportion_sweep/main_0x4004_k02_s03.py` |  |
| 0.13 | 2/15 | 4 | 0.6576s | 0.0555s | 1 | 8 | yes | 0.6177s | 0.6850s | `detyped_files/pystone/shallow/proportion_sweep/main_0x12_k02_s04.py` |  |
| 0.13 | 2/15 | 5 | 0.6857s | 0.0269s | 1 | 8 | yes | 0.6669s | 0.7017s | `detyped_files/pystone/shallow/proportion_sweep/main_0x880_k02_s05.py` |  |
| 0.13 | 2/15 | 6 | 0.6619s | 0.0488s | 1 | 8 | yes | 0.6263s | 0.6849s | `detyped_files/pystone/shallow/proportion_sweep/main_0x1020_k02_s06.py` |  |
| 0.13 | 2/15 | 7 | 0.9787s | 0.0683s | 1 | 8 | yes | 0.9358s | 1.0250s | `detyped_files/pystone/shallow/proportion_sweep/main_0x2100_k02_s07.py` |  |
| 0.13 | 2/15 | 8 | 1.0634s | 0.0614s | 1 | 8 | yes | 1.0248s | 1.1046s | `detyped_files/pystone/shallow/proportion_sweep/main_0x48_k02_s08.py` |  |
| 0.13 | 2/15 | 9 | 0.7104s | 0.0447s | 1 | 8 | yes | 0.6813s | 0.7389s | `detyped_files/pystone/shallow/proportion_sweep/main_0x4020_k02_s09.py` |  |
| 0.13 | 2/15 | 10 | 0.6687s | 0.0584s | 1 | 8 | yes | 0.6305s | 0.7035s | `detyped_files/pystone/shallow/proportion_sweep/main_0x6_k02_s10.py` |  |
| 0.20 | 3/15 | 1 | 0.7940s | 0.0669s | 1 | 8 | yes | 0.7501s | 0.8358s | `detyped_files/pystone/shallow/proportion_sweep/main_0x2401_k03_s01.py` |  |
| 0.20 | 3/15 | 2 | 0.6555s | 0.0447s | 1 | 8 | yes | 0.6276s | 0.6837s | `detyped_files/pystone/shallow/proportion_sweep/main_0x241_k03_s02.py` |  |
| 0.20 | 3/15 | 3 | 0.6946s | 0.0392s | 1 | 8 | yes | 0.6670s | 0.7175s | `detyped_files/pystone/shallow/proportion_sweep/main_0x2240_k03_s03.py` |  |
| 0.20 | 3/15 | 4 | 0.9636s | 0.0853s | 1 | 8 | yes | 0.9048s | 1.0138s | `detyped_files/pystone/shallow/proportion_sweep/main_0x2120_k03_s04.py` |  |
| 0.20 | 3/15 | 5 | 0.6797s | 0.0633s | 1 | 8 | yes | 0.6341s | 0.7152s | `detyped_files/pystone/shallow/proportion_sweep/main_0x10c0_k03_s05.py` |  |
| 0.20 | 3/15 | 6 | 0.7867s | 0.0465s | 1 | 8 | yes | 0.7543s | 0.8140s | `detyped_files/pystone/shallow/proportion_sweep/main_0xc10_k03_s06.py` |  |
| 0.20 | 3/15 | 7 | 1.0925s | 0.0779s | 1 | 8 | yes | 1.0433s | 1.1432s | `detyped_files/pystone/shallow/proportion_sweep/main_0x228_k03_s07.py` |  |
| 0.20 | 3/15 | 8 | 0.6602s | 0.0298s | 1 | 8 | yes | 0.6389s | 0.6763s | `detyped_files/pystone/shallow/proportion_sweep/main_0x2021_k03_s08.py` |  |
| 0.20 | 3/15 | 9 | 0.9243s | 0.0640s | 1 | 8 | yes | 0.8839s | 0.9665s | `detyped_files/pystone/shallow/proportion_sweep/main_0x4104_k03_s09.py` |  |
| 0.20 | 3/15 | 10 | 0.6230s | 0.0680s | 1 | 8 | yes | 0.5797s | 0.6667s | `detyped_files/pystone/shallow/proportion_sweep/main_0x2082_k03_s10.py` |  |
| 0.27 | 4/15 | 1 | 1.0339s | 0.0549s | 1 | 8 | yes | 0.9983s | 1.0692s | `detyped_files/pystone/shallow/proportion_sweep/main_0xa9_k04_s01.py` |  |
| 0.27 | 4/15 | 2 | 0.7003s | 0.0445s | 1 | 8 | yes | 0.6674s | 0.7227s | `detyped_files/pystone/shallow/proportion_sweep/main_0x1016_k04_s02.py` |  |
| 0.27 | 4/15 | 3 | 1.1008s | 0.0728s | 1 | 8 | yes | 1.0523s | 1.1467s | `detyped_files/pystone/shallow/proportion_sweep/main_0x2520_k04_s03.py` |  |
| 0.27 | 4/15 | 4 | 0.8050s | 0.0686s | 1 | 8 | yes | 0.7608s | 0.8473s | `detyped_files/pystone/shallow/proportion_sweep/main_0x5600_k04_s04.py` |  |
| 0.27 | 4/15 | 5 | 1.0683s | 0.0850s | 1 | 8 | yes | 1.0154s | 1.1257s | `detyped_files/pystone/shallow/proportion_sweep/main_0x24c_k04_s05.py` |  |
| 0.27 | 4/15 | 6 | 0.8516s | 0.0526s | 1 | 8 | yes | 0.8170s | 0.8847s | `detyped_files/pystone/shallow/proportion_sweep/main_0xca0_k04_s06.py` |  |
| 0.27 | 4/15 | 7 | 0.6741s | 0.0473s | 1 | 8 | yes | 0.6418s | 0.7036s | `detyped_files/pystone/shallow/proportion_sweep/main_0x8a1_k04_s07.py` |  |
| 0.27 | 4/15 | 8 | 0.8382s | 0.0317s | 1 | 8 | yes | 0.8188s | 0.8593s | `detyped_files/pystone/shallow/proportion_sweep/main_0x2482_k04_s08.py` |  |
| 0.27 | 4/15 | 9 | 1.1234s | 0.0863s | 1 | 8 | yes | 1.0678s | 1.1796s | `detyped_files/pystone/shallow/proportion_sweep/main_0x88c_k04_s09.py` |  |
| 0.27 | 4/15 | 10 | 0.6831s | 0.0480s | 1 | 8 | yes | 0.6490s | 0.7093s | `detyped_files/pystone/shallow/proportion_sweep/main_0x2a04_k04_s10.py` |  |
| 0.33 | 5/15 | 1 | 0.6880s | 0.0496s | 1 | 8 | yes | 0.6528s | 0.7156s | `detyped_files/pystone/shallow/proportion_sweep/main_0x12a2_k05_s01.py` |  |
| 0.33 | 5/15 | 2 | 0.6944s | 0.0322s | 1 | 8 | yes | 0.6742s | 0.7160s | `detyped_files/pystone/shallow/proportion_sweep/main_0xa70_k05_s02.py` |  |
| 0.33 | 5/15 | 3 | 0.7089s | 0.0415s | 1 | 8 | yes | 0.6829s | 0.7356s | `detyped_files/pystone/shallow/proportion_sweep/main_0x1a90_k05_s03.py` |  |
| 0.33 | 5/15 | 4 | 0.9477s | 0.0201s | 1 | 8 | yes | 0.9349s | 0.9610s | `detyped_files/pystone/shallow/proportion_sweep/main_0x3980_k05_s04.py` |  |
| 0.33 | 5/15 | 5 | 1.2655s | 0.0844s | 1 | 8 | yes | 1.2140s | 1.3240s | `detyped_files/pystone/shallow/proportion_sweep/main_0x448c_k05_s05.py` |  |
| 0.33 | 5/15 | 6 | 0.6903s | 0.0368s | 1 | 8 | yes | 0.6659s | 0.7134s | `detyped_files/pystone/shallow/proportion_sweep/main_0x1a21_k05_s06.py` |  |
| 0.33 | 5/15 | 7 | 0.6443s | 0.0527s | 1 | 8 | yes | 0.6088s | 0.6766s | `detyped_files/pystone/shallow/proportion_sweep/main_0x893_k05_s07.py` |  |
| 0.33 | 5/15 | 8 | 1.1134s | 0.0850s | 1 | 8 | yes | 1.0632s | 1.1736s | `detyped_files/pystone/shallow/proportion_sweep/main_0xdc0_k05_s08.py` |  |
| 0.33 | 5/15 | 9 | 1.1444s | 0.0487s | 1 | 8 | yes | 1.1129s | 1.1747s | `detyped_files/pystone/shallow/proportion_sweep/main_0x2d01_k05_s09.py` |  |
| 0.33 | 5/15 | 10 | 0.9416s | 0.0464s | 1 | 8 | yes | 0.9137s | 0.9737s | `detyped_files/pystone/shallow/proportion_sweep/main_0x3304_k05_s10.py` |  |
| 0.40 | 6/15 | 1 | 1.0630s | 0.0431s | 1 | 8 | yes | 1.0317s | 1.0861s | `detyped_files/pystone/shallow/proportion_sweep/main_0x700e_k06_s01.py` |  |
| 0.40 | 6/15 | 2 | 1.0664s | 0.0775s | 1 | 8 | yes | 1.0159s | 1.1160s | `detyped_files/pystone/shallow/proportion_sweep/main_0xd07_k06_s02.py` |  |
| 0.40 | 6/15 | 3 | 0.6589s | 0.0567s | 1 | 8 | yes | 0.6194s | 0.6935s | `detyped_files/pystone/shallow/proportion_sweep/main_0x20d5_k06_s03.py` |  |
| 0.40 | 6/15 | 4 | 0.8563s | 0.0725s | 1 | 8 | yes | 0.8080s | 0.9032s | `detyped_files/pystone/shallow/proportion_sweep/main_0x3e20_k06_s04.py` |  |
| 0.40 | 6/15 | 5 | 0.9525s | 0.0316s | 1 | 8 | yes | 0.9315s | 0.9726s | `detyped_files/pystone/shallow/proportion_sweep/main_0x4b11_k06_s05.py` |  |
| 0.40 | 6/15 | 6 | 1.0688s | 0.0708s | 1 | 8 | yes | 1.0261s | 1.1167s | `detyped_files/pystone/shallow/proportion_sweep/main_0x1585_k06_s06.py` |  |
| 0.40 | 6/15 | 7 | 1.2552s | 0.0814s | 1 | 8 | yes | 1.2134s | 1.3145s | `detyped_files/pystone/shallow/proportion_sweep/main_0x243a_k06_s07.py` |  |
| 0.40 | 6/15 | 8 | 1.3845s | 0.0582s | 1 | 8 | yes | 1.3507s | 1.4263s | `detyped_files/pystone/shallow/proportion_sweep/main_0x510b_k06_s08.py` |  |
| 0.40 | 6/15 | 9 | 1.0907s | 0.1115s | 1 | 8 | yes | 1.0171s | 1.1614s | `detyped_files/pystone/shallow/proportion_sweep/main_0x2724_k06_s09.py` |  |
| 0.40 | 6/15 | 10 | 0.8271s | 0.0403s | 1 | 8 | yes | 0.8022s | 0.8549s | `detyped_files/pystone/shallow/proportion_sweep/main_0x5445_k06_s10.py` |  |
| 0.47 | 7/15 | 1 | 0.8038s | 0.0590s | 1 | 8 | yes | 0.7691s | 0.8453s | `detyped_files/pystone/shallow/proportion_sweep/main_0x4647_k07_s01.py` |  |
| 0.47 | 7/15 | 2 | 0.8420s | 0.0933s | 1 | 8 | yes | 0.7802s | 0.9000s | `detyped_files/pystone/shallow/proportion_sweep/main_0x64e2_k07_s02.py` |  |
| 0.47 | 7/15 | 3 | 0.8381s | 0.0867s | 1 | 8 | yes | 0.7778s | 0.8915s | `detyped_files/pystone/shallow/proportion_sweep/main_0x44e5_k07_s03.py` |  |
| 0.47 | 7/15 | 4 | 1.0859s | 0.0562s | 1 | 8 | yes | 1.0490s | 1.1209s | `detyped_files/pystone/shallow/proportion_sweep/main_0x5899_k07_s04.py` |  |
| 0.47 | 7/15 | 5 | 0.7157s | 0.0630s | 1 | 8 | yes | 0.6819s | 0.7611s | `detyped_files/pystone/shallow/proportion_sweep/main_0x3295_k07_s05.py` |  |
| 0.47 | 7/15 | 6 | 0.9425s | 0.0981s | 1 | 8 | yes | 0.8783s | 1.0050s | `detyped_files/pystone/shallow/proportion_sweep/main_0x7116_k07_s06.py` |  |
| 0.47 | 7/15 | 7 | 1.3406s | 0.0417s | 1 | 8 | yes | 1.3099s | 1.3653s | `detyped_files/pystone/shallow/proportion_sweep/main_0x1b19_k07_s07.py` |  |
| 0.47 | 7/15 | 8 | 0.6657s | 0.0408s | 1 | 8 | yes | 0.6376s | 0.6908s | `detyped_files/pystone/shallow/proportion_sweep/main_0x7035_k07_s08.py` |  |
| 0.47 | 7/15 | 9 | 0.8227s | 0.0674s | 1 | 8 | yes | 0.7766s | 0.8634s | `detyped_files/pystone/shallow/proportion_sweep/main_0x1c66_k07_s09.py` |  |
| 0.47 | 7/15 | 10 | 0.9605s | 0.0716s | 1 | 8 | yes | 0.9094s | 1.0020s | `detyped_files/pystone/shallow/proportion_sweep/main_0x6361_k07_s10.py` |  |
| 0.53 | 8/15 | 1 | 0.8234s | 0.0657s | 1 | 8 | yes | 0.7773s | 0.8654s | `detyped_files/pystone/shallow/proportion_sweep/main_0x6e45_k08_s01.py` |  |
| 0.53 | 8/15 | 2 | 1.0733s | 0.0682s | 1 | 8 | yes | 1.0301s | 1.1179s | `detyped_files/pystone/shallow/proportion_sweep/main_0x2a6b_k08_s02.py` |  |
| 0.53 | 8/15 | 3 | 1.1806s | 0.1371s | 1 | 8 | yes | 1.1013s | 1.2748s | `detyped_files/pystone/shallow/proportion_sweep/main_0x46cb_k08_s03.py` |  |
| 0.53 | 8/15 | 4 | 0.9609s | 0.0849s | 1 | 8 | yes | 0.9094s | 1.0201s | `detyped_files/pystone/shallow/proportion_sweep/main_0x4b65_k08_s04.py` |  |
| 0.53 | 8/15 | 5 | 0.8545s | 0.0578s | 1 | 8 | yes | 0.8159s | 0.8913s | `detyped_files/pystone/shallow/proportion_sweep/main_0x74a6_k08_s05.py` |  |
| 0.53 | 8/15 | 6 | 1.3120s | 0.0910s | 1 | 8 | yes | 1.2534s | 1.3703s | `detyped_files/pystone/shallow/proportion_sweep/main_0x69aa_k08_s06.py` |  |
| 0.53 | 8/15 | 7 | 0.9503s | 0.0755s | 1 | 8 | yes | 0.9020s | 0.9984s | `detyped_files/pystone/shallow/proportion_sweep/main_0x3396_k08_s07.py` |  |
| 0.53 | 8/15 | 8 | 1.2140s | 0.0564s | 1 | 8 | yes | 1.1732s | 1.2451s | `detyped_files/pystone/shallow/proportion_sweep/main_0x644f_k08_s08.py` |  |
| 0.53 | 8/15 | 9 | 1.0631s | 0.0371s | 1 | 8 | yes | 1.0389s | 1.0864s | `detyped_files/pystone/shallow/proportion_sweep/main_0x7299_k08_s09.py` |  |
| 0.53 | 8/15 | 10 | 0.9505s | 0.0486s | 1 | 8 | yes | 0.9166s | 0.9785s | `detyped_files/pystone/shallow/proportion_sweep/main_0x79c1_k08_s10.py` |  |
| 0.60 | 9/15 | 1 | 0.6642s | 0.0831s | 1 | 8 | yes | 0.6091s | 0.7166s | `detyped_files/pystone/shallow/proportion_sweep/main_0x1af5_k09_s01.py` |  |
| 0.60 | 9/15 | 2 | 1.0681s | 0.1028s | 1 | 8 | yes | 1.0056s | 1.1440s | `detyped_files/pystone/shallow/proportion_sweep/main_0x68ed_k09_s02.py` |  |
| 0.60 | 9/15 | 3 | 1.4998s | 0.0850s | 1 | 8 | yes | 1.4461s | 1.5558s | `detyped_files/pystone/shallow/proportion_sweep/main_0x571e_k09_s03.py` |  |
| 0.60 | 9/15 | 4 | 0.7883s | 0.0622s | 1 | 8 | yes | 0.7463s | 0.8258s | `detyped_files/pystone/shallow/proportion_sweep/main_0x4e97_k09_s04.py` |  |
| 0.60 | 9/15 | 5 | 1.2493s | 0.0983s | 1 | 8 | yes | 1.1886s | 1.3157s | `detyped_files/pystone/shallow/proportion_sweep/main_0x7e0e_k09_s05.py` |  |
| 0.60 | 9/15 | 6 | 1.1892s | 0.0613s | 1 | 8 | yes | 1.1491s | 1.2281s | `detyped_files/pystone/shallow/proportion_sweep/main_0x7e58_k09_s06.py` |  |
| 0.60 | 9/15 | 7 | 1.2005s | 0.0963s | 1 | 8 | yes | 1.1385s | 1.2597s | `detyped_files/pystone/shallow/proportion_sweep/main_0x366e_k09_s07.py` |  |
| 0.60 | 9/15 | 8 | 1.4485s | 0.1297s | 1 | 8 | yes | 1.3703s | 1.5345s | `detyped_files/pystone/shallow/proportion_sweep/main_0x5799_k09_s08.py` |  |
| 0.60 | 9/15 | 9 | 1.3781s | 0.0796s | 1 | 8 | yes | 1.3341s | 1.4343s | `detyped_files/pystone/shallow/proportion_sweep/main_0x394f_k09_s09.py` |  |
| 0.60 | 9/15 | 10 | 0.8127s | 0.0439s | 1 | 8 | yes | 0.7833s | 0.8406s | `detyped_files/pystone/shallow/proportion_sweep/main_0x74e6_k09_s10.py` |  |
| 0.67 | 10/15 | 1 | 1.4872s | 0.0966s | 1 | 8 | yes | 1.4237s | 1.5514s | `detyped_files/pystone/shallow/proportion_sweep/main_0x5fa9_k10_s01.py` |  |
| 0.67 | 10/15 | 2 | 1.1619s | 0.0741s | 1 | 8 | yes | 1.1142s | 1.2100s | `detyped_files/pystone/shallow/proportion_sweep/main_0x4eed_k10_s02.py` |  |
| 0.67 | 10/15 | 3 | 1.3525s | 0.0775s | 1 | 8 | yes | 1.2998s | 1.3997s | `detyped_files/pystone/shallow/proportion_sweep/main_0x69fc_k10_s03.py` |  |
| 0.67 | 10/15 | 4 | 1.1195s | 0.0547s | 1 | 8 | yes | 1.0848s | 1.1556s | `detyped_files/pystone/shallow/proportion_sweep/main_0x5acf_k10_s04.py` |  |
| 0.67 | 10/15 | 5 | 1.4934s | 0.0959s | 1 | 8 | yes | 1.4299s | 1.5538s | `detyped_files/pystone/shallow/proportion_sweep/main_0x5fca_k10_s05.py` |  |
| 0.67 | 10/15 | 6 | 1.5049s | 0.1203s | 1 | 8 | yes | 1.4296s | 1.5828s | `detyped_files/pystone/shallow/proportion_sweep/main_0x479f_k10_s06.py` |  |
| 0.67 | 10/15 | 7 | 1.0486s | 0.0572s | 1 | 8 | yes | 1.0101s | 1.0839s | `detyped_files/pystone/shallow/proportion_sweep/main_0x7a9d_k10_s07.py` |  |
| 0.67 | 10/15 | 8 | 1.4792s | 0.0944s | 1 | 8 | yes | 1.4307s | 1.5489s | `detyped_files/pystone/shallow/proportion_sweep/main_0x65eb_k10_s08.py` |  |
| 0.67 | 10/15 | 9 | 0.8070s | 0.0612s | 1 | 8 | yes | 0.7666s | 0.8432s | `detyped_files/pystone/shallow/proportion_sweep/main_0x7cb3_k10_s09.py` |  |
| 0.67 | 10/15 | 10 | 1.2865s | 0.0775s | 1 | 8 | yes | 1.2379s | 1.3375s | `detyped_files/pystone/shallow/proportion_sweep/main_0x2cfd_k10_s10.py` |  |
| 0.73 | 11/15 | 1 | 1.0674s | 0.0635s | 1 | 8 | yes | 1.0245s | 1.1070s | `detyped_files/pystone/shallow/proportion_sweep/main_0x5df6_k11_s01.py` |  |
| 0.73 | 11/15 | 2 | 1.1099s | 0.1085s | 1 | 8 | yes | 1.0390s | 1.1785s | `detyped_files/pystone/shallow/proportion_sweep/main_0x4f77_k11_s02.py` |  |
| 0.73 | 11/15 | 3 | 0.6959s | 0.0603s | 1 | 8 | yes | 0.6529s | 0.7300s | `detyped_files/pystone/shallow/proportion_sweep/main_0x3af7_k11_s03.py` |  |
| 0.73 | 11/15 | 4 | 1.3406s | 0.0720s | 1 | 8 | yes | 1.3020s | 1.3927s | `detyped_files/pystone/shallow/proportion_sweep/main_0x7bd9_k11_s04.py` |  |
| 0.73 | 11/15 | 5 | 1.4967s | 0.0840s | 1 | 8 | yes | 1.4430s | 1.5511s | `detyped_files/pystone/shallow/proportion_sweep/main_0x3f5d_k11_s05.py` |  |
| 0.73 | 11/15 | 6 | 1.4956s | 0.0680s | 1 | 8 | yes | 1.4474s | 1.5340s | `detyped_files/pystone/shallow/proportion_sweep/main_0x772f_k11_s06.py` |  |
| 0.73 | 11/15 | 7 | 1.3272s | 0.1026s | 1 | 8 | yes | 1.2650s | 1.3955s | `detyped_files/pystone/shallow/proportion_sweep/main_0x7be9_k11_s07.py` |  |
| 0.73 | 11/15 | 8 | 1.3255s | 0.0660s | 1 | 8 | yes | 1.2820s | 1.3660s | `detyped_files/pystone/shallow/proportion_sweep/main_0x63df_k11_s08.py` |  |
| 0.73 | 11/15 | 9 | 0.8114s | 0.0858s | 1 | 8 | yes | 0.7575s | 0.8678s | `detyped_files/pystone/shallow/proportion_sweep/main_0x6ee7_k11_s09.py` |  |
| 0.73 | 11/15 | 10 | 1.0846s | 0.0809s | 1 | 8 | yes | 1.0300s | 1.1328s | `detyped_files/pystone/shallow/proportion_sweep/main_0x5de7_k11_s10.py` |  |
| 0.80 | 12/15 | 1 | 1.0643s | 0.1078s | 1 | 8 | yes | 1.0071s | 1.1432s | `detyped_files/pystone/shallow/proportion_sweep/main_0x7fb6_k12_s01.py` |  |
| 0.80 | 12/15 | 2 | 1.1975s | 0.0500s | 1 | 8 | yes | 1.1634s | 1.2280s | `detyped_files/pystone/shallow/proportion_sweep/main_0x6efd_k12_s02.py` |  |
| 0.80 | 12/15 | 3 | 1.0991s | 0.0355s | 1 | 8 | yes | 1.0782s | 1.1238s | `detyped_files/pystone/shallow/proportion_sweep/main_0x7dd7_k12_s03.py` |  |
| 0.80 | 12/15 | 4 | 1.4541s | 0.1020s | 1 | 8 | yes | 1.3932s | 1.5227s | `detyped_files/pystone/shallow/proportion_sweep/main_0x6f9f_k12_s04.py` |  |
| 0.80 | 12/15 | 5 | 1.0549s | 0.0614s | 1 | 8 | yes | 1.0138s | 1.0925s | `detyped_files/pystone/shallow/proportion_sweep/main_0x7afb_k12_s05.py` |  |
| 0.80 | 12/15 | 6 | 1.1857s | 0.0406s | 1 | 8 | yes | 1.1583s | 1.2104s | `detyped_files/pystone/shallow/proportion_sweep/main_0x4eff_k12_s06.py` |  |
| 0.80 | 12/15 | 7 | 1.2167s | 0.0692s | 1 | 8 | yes | 1.1660s | 1.2540s | `detyped_files/pystone/shallow/proportion_sweep/main_0x7c7f_k12_s07.py` |  |
| 0.80 | 12/15 | 8 | 1.5103s | 0.0689s | 1 | 8 | yes | 1.4670s | 1.5553s | `detyped_files/pystone/shallow/proportion_sweep/main_0x5f9f_k12_s08.py` |  |
| 0.80 | 12/15 | 9 | 1.4932s | 0.1074s | 1 | 8 | yes | 1.4278s | 1.5670s | `detyped_files/pystone/shallow/proportion_sweep/main_0x6fed_k12_s09.py` |  |
| 0.80 | 12/15 | 10 | 1.5038s | 0.0775s | 1 | 8 | yes | 1.4521s | 1.5526s | `detyped_files/pystone/shallow/proportion_sweep/main_0x5fed_k12_s10.py` |  |
| 0.87 | 13/15 | 1 | 1.4712s | 0.0745s | 1 | 8 | yes | 1.4253s | 1.5200s | `detyped_files/pystone/shallow/proportion_sweep/main_0x5ffb_k13_s01.py` |  |
| 0.87 | 13/15 | 2 | 1.4556s | 0.0766s | 1 | 8 | yes | 1.4089s | 1.5067s | `detyped_files/pystone/shallow/proportion_sweep/main_0x5fef_k13_s02.py` |  |
| 0.87 | 13/15 | 3 | 1.0696s | 0.0466s | 1 | 8 | yes | 1.0408s | 1.1009s | `detyped_files/pystone/shallow/proportion_sweep/main_0x7fd7_k13_s03.py` |  |
| 0.87 | 13/15 | 4 | 1.4870s | 0.0900s | 1 | 8 | yes | 1.4274s | 1.5426s | `detyped_files/pystone/shallow/proportion_sweep/main_0x7f7d_k13_s04.py` |  |
| 0.87 | 13/15 | 5 | 1.5133s | 0.1011s | 1 | 8 | yes | 1.4486s | 1.5781s | `detyped_files/pystone/shallow/proportion_sweep/main_0x3ffe_k13_s05.py` |  |
| 0.87 | 13/15 | 6 | 1.5570s | 0.1069s | 1 | 8 | yes | 1.4976s | 1.6345s | `detyped_files/pystone/shallow/proportion_sweep/main_0x7ffc_k13_s06.py` |  |
| 0.87 | 13/15 | 7 | 1.5262s | 0.0943s | 1 | 8 | yes | 1.4650s | 1.5849s | `detyped_files/pystone/shallow/proportion_sweep/main_0x7dfb_k13_s07.py` |  |
| 0.87 | 13/15 | 8 | 1.4827s | 0.0743s | 1 | 8 | yes | 1.4368s | 1.5331s | `detyped_files/pystone/shallow/proportion_sweep/main_0x6dff_k13_s08.py` |  |
| 0.87 | 13/15 | 9 | 1.5604s | 0.1326s | 1 | 8 | yes | 1.4751s | 1.6441s | `detyped_files/pystone/shallow/proportion_sweep/main_0x5fdf_k13_s09.py` |  |
| 0.87 | 13/15 | 10 | 1.4897s | 0.0424s | 1 | 8 | yes | 1.4627s | 1.5166s | `detyped_files/pystone/shallow/proportion_sweep/main_0x77fe_k13_s10.py` |  |
| 0.93 | 14/15 | 1 | 1.4784s | 0.0960s | 1 | 8 | yes | 1.4189s | 1.5442s | `detyped_files/pystone/shallow/proportion_sweep/main_0x7ffd_k14_s01.py` |  |
| 0.93 | 14/15 | 2 | 1.0698s | 0.0872s | 1 | 8 | yes | 1.0136s | 1.1247s | `detyped_files/pystone/shallow/proportion_sweep/main_0x7ff7_k14_s02.py` |  |
| 0.93 | 14/15 | 3 | 1.4271s | 0.0788s | 1 | 8 | yes | 1.3756s | 1.4758s | `detyped_files/pystone/shallow/proportion_sweep/main_0x5fff_k14_s03.py` |  |
| 0.93 | 14/15 | 4 | 1.5504s | 0.0894s | 1 | 8 | yes | 1.4971s | 1.6129s | `detyped_files/pystone/shallow/proportion_sweep/main_0x7fef_k14_s04.py` |  |
| 0.93 | 14/15 | 5 | 1.4809s | 0.0539s | 1 | 8 | yes | 1.4435s | 1.5121s | `detyped_files/pystone/shallow/proportion_sweep/main_0x7fbf_k14_s05.py` |  |
| 0.93 | 14/15 | 6 | 1.5143s | 0.1090s | 1 | 8 | yes | 1.4452s | 1.5860s | `detyped_files/pystone/shallow/proportion_sweep/main_0x3fff_k14_s06.py` |  |
| 0.93 | 14/15 | 7 | 1.4633s | 0.0696s | 1 | 8 | yes | 1.4181s | 1.5097s | `detyped_files/pystone/shallow/proportion_sweep/main_0x7ffb_k14_s07.py` |  |
| 0.93 | 14/15 | 8 | 1.5251s | 0.1261s | 1 | 8 | yes | 1.4573s | 1.6189s | `detyped_files/pystone/shallow/proportion_sweep/main_0x77ff_k14_s08.py` |  |
| 0.93 | 14/15 | 9 | 1.5004s | 0.1178s | 1 | 8 | yes | 1.4288s | 1.5828s | `detyped_files/pystone/shallow/proportion_sweep/main_0x6fff_k14_s09.py` |  |
| 0.93 | 14/15 | 10 | 1.2164s | 0.0764s | 1 | 8 | yes | 1.1738s | 1.2736s | `detyped_files/pystone/shallow/proportion_sweep/main_0x7eff_k14_s10.py` |  |
| 1.00 | 15/15 | 1 | 1.5468s | 0.1307s | 1 | 8 | yes | 1.4774s | 1.6409s | `detyped_files/pystone/shallow/proportion_sweep/main_0x7fff_k15_s01.py` |  |

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
