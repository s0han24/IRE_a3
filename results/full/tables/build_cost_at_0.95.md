| dataset | index | config | recall | QPS | build s | size MB | bytes/vector |
|---|---|---|---|---|---|---|---|
| glove-100-angular | hnsw | hnsw M=32, ef_search=512 | 0.965 | 707 | 236.6 | 795.5 | 672.2 |
| glove-100-angular | ivf_flat | **not reached**; highest recall: ivf_flat c=1, nprobe=128 | 0.949 | 513 | 6.5 | 483.3 | 408.4 |
| glove-100-angular | ivf_pq | **not reached**; highest recall: ivf_pq c=4 m=50, nprobe=256 | 0.838 | 583 | 87.9 | 70.5 | 59.6 |
| sift-128-euclidean | hnsw | hnsw M=16, ef_search=64 | 0.971 | 8190 | 96.5 | 656.3 | 656.3 |
| sift-128-euclidean | ivf_flat | ivf_flat c=4, nprobe=64 | 0.977 | 3578 | 66.3 | 522.1 | 522.1 |
| sift-128-euclidean | ivf_pq | **not reached**; highest recall: ivf_pq c=4 m=64, nprobe=256 | 0.887 | 456 | 76.8 | 74.2 | 74.2 |
