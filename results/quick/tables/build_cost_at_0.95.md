| dataset | index | config | recall | QPS | build s | size MB | bytes/vector |
|---|---|---|---|---|---|---|---|
| glove-100-angular | hnsw | hnsw M=16, ef_search=512 | 0.978 | 1411 | 4.6 | 54.4 | 544.3 |
| glove-100-angular | ivf_flat | ivf_flat c=1, nprobe=128 | 0.981 | 2407 | 0.4 | 40.9 | 409.3 |
| glove-100-angular | ivf_pq | **not reached**; highest recall: ivf_pq c=1 m=50, nprobe=256 | 0.867 | 692 | 2.4 | 6.0 | 60.3 |
| sift-128-euclidean | hnsw | hnsw M=16, ef_search=32 | 0.958 | 24551 | 3.4 | 65.6 | 656.3 |
| sift-128-euclidean | ivf_flat | ivf_flat c=1, nprobe=16 | 0.966 | 12820 | 0.5 | 52.2 | 521.6 |
| sift-128-euclidean | ivf_pq | **not reached**; highest recall: ivf_pq c=1 m=64, nprobe=128 | 0.894 | 1033 | 3.0 | 7.5 | 75.0 |
