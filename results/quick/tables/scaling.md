| n_base | index | config | recall | QPS | p50 ms |
|---|---|---|---|---|---|
| 100000 | exact | exact (flat) | 1.000 | 998 | 1.00 |
| 100000 | hnsw | hnsw M=16, ef_search=32 | 0.958 | 24551 | 0.04 |
| 100000 | ivf_flat | ivf_flat c=1, nprobe=16 | 0.966 | 12820 | 0.08 |
