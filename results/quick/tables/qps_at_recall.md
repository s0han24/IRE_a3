| dataset | index | QPS @ 0.9 | config @ 0.9 | QPS @ 0.95 | config @ 0.95 |
|---|---|---|---|---|---|
| glove-100-angular | exact | 572 | exact (flat) | 572 | exact (flat) |
| glove-100-angular | hnsw | 3876 | hnsw M=16, ef_search=128 | 752 | hnsw M=16, ef_search=512 |
| glove-100-angular | ivf_flat | 2884 | ivf_flat c=1, nprobe=64 | 1447 | ivf_flat c=1, nprobe=128 |
| glove-100-angular | ivf_pq | **not reached** | best recall 0.867 | **not reached** | best recall 0.867 |
| sift-128-euclidean | exact | 487 | exact (flat) | 487 | exact (flat) |
| sift-128-euclidean | hnsw | 12027 | hnsw M=16, ef_search=32 | 12027 | hnsw M=16, ef_search=32 |
| sift-128-euclidean | ivf_flat | 8484 | ivf_flat c=1, nprobe=16 | 8484 | ivf_flat c=1, nprobe=16 |
| sift-128-euclidean | ivf_pq | **not reached** | best recall 0.894 | **not reached** | best recall 0.894 |
