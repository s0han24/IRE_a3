| dataset | index | QPS @ 0.9 | config @ 0.9 | QPS @ 0.95 | config @ 0.95 |
|---|---|---|---|---|---|
| glove-100-angular | exact | 95 | exact (flat) | 95 | exact (flat) |
| glove-100-angular | hnsw | 1133 | hnsw M=32, ef_search=256 | 629 | hnsw M=32, ef_search=512 |
| glove-100-angular | ivf_flat | 933 | ivf_flat c=1, nprobe=64 | **not reached** | best recall 0.949 |
| glove-100-angular | ivf_pq | **not reached** | best recall 0.838 | **not reached** | best recall 0.838 |
| sift-128-euclidean | exact | 102 | exact (flat) | 102 | exact (flat) |
| sift-128-euclidean | hnsw | 10728 | hnsw M=16, ef_search=32 | 7989 | hnsw M=16, ef_search=64 |
| sift-128-euclidean | ivf_flat | 6026 | ivf_flat c=4, nprobe=32 | 3540 | ivf_flat c=4, nprobe=64 |
| sift-128-euclidean | ivf_pq | **not reached** | best recall 0.887 | **not reached** | best recall 0.887 |
