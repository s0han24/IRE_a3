| n_base | index | config | recall | QPS | p50 ms |
|---|---|---|---|---|---|
| 100000 | exact | exact (flat) | 1.000 | 487 | 2.18 |
| 100000 | hnsw | hnsw M=16, ef_search=32 | 0.958 | 12027 | 0.08 |
| 100000 | ivf_flat | ivf_flat c=1, nprobe=16 | 0.966 | 8484 | 0.12 |
