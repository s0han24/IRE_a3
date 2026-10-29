| dataset | index | QPS @ 0.9 | config @ 0.9 | QPS @ 0.95 | config @ 0.95 |
|---|---|---|---|---|---|
| glove-100-angular | exact | 1174 | exact (flat) | 1174 | exact (flat) |
| glove-100-angular | hnsw | 5887 | hnsw M=16, ef_search=128 | 1411 | hnsw M=16, ef_search=512 |
| glove-100-angular | ivf_flat | 4799 | ivf_flat c=1, nprobe=64 | 2407 | ivf_flat c=1, nprobe=128 |
| glove-100-angular | ivf_pq | **not reached** | best recall 0.867 | **not reached** | best recall 0.867 |
| sift-128-euclidean | exact | 998 | exact (flat) | 998 | exact (flat) |
| sift-128-euclidean | hnsw | 24551 | hnsw M=16, ef_search=32 | 24551 | hnsw M=16, ef_search=32 |
| sift-128-euclidean | ivf_flat | 12820 | ivf_flat c=1, nprobe=16 | 12820 | ivf_flat c=1, nprobe=16 |
| sift-128-euclidean | ivf_pq | **not reached** | best recall 0.894 | **not reached** | best recall 0.894 |
