| n_base | index | config | recall | QPS | p50 ms |
|---|---|---|---|---|---|
| 100000 | exact | exact (flat) | 1.000 | 593 | 1.61 |
| 100000 | hnsw | hnsw M=32, ef_search=32 | 0.972 | 13192 | 0.07 |
| 100000 | ivf_flat | ivf_flat c=4, nprobe=32 | 0.958 | 13678 | 0.07 |
| 300000 | exact | exact (flat) | 1.000 | 242 | 4.10 |
| 300000 | hnsw | hnsw M=32, ef_search=32 | 0.955 | 12703 | 0.08 |
| 300000 | ivf_flat | ivf_flat c=1, nprobe=16 | 0.951 | 6261 | 0.16 |
| 1000000 | exact | exact (flat) | 1.000 | 70 | 14.40 |
| 1000000 | hnsw | hnsw M=16, ef_search=64 | 0.971 | 8190 | 0.13 |
| 1000000 | ivf_flat | ivf_flat c=4, nprobe=64 | 0.977 | 3578 | 0.27 |
