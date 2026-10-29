| n_base | index | config | recall | QPS | p50 ms |
|---|---|---|---|---|---|
| 100000 | exact | exact (flat) | 1.000 | 785 | 1.32 |
| 100000 | hnsw | hnsw M=16, ef_search=32 | 0.958 | 10988 | 0.09 |
| 100000 | ivf_flat | ivf_flat c=4, nprobe=32 | 0.958 | 10703 | 0.09 |
| 300000 | exact | exact (flat) | 1.000 | 225 | 4.33 |
| 300000 | hnsw | hnsw M=32, ef_search=32 | 0.955 | 8331 | 0.12 |
| 300000 | ivf_flat | ivf_flat c=1, nprobe=16 | 0.951 | 5207 | 0.19 |
| 1000000 | exact | exact (flat) | 1.000 | 102 | 9.70 |
| 1000000 | hnsw | hnsw M=16, ef_search=64 | 0.971 | 7989 | 0.13 |
| 1000000 | ivf_flat | ivf_flat c=4, nprobe=64 | 0.977 | 3540 | 0.28 |
