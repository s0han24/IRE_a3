| condition | setting | config | recall (own) | recall (original) | QPS | build s | size MB | bytes/vector |
|---|---|---|---|---|---|---|---|---|
| clean | - | exact (flat) | 1.000 | 1.000 | 2039 | - | - | - |
| clean | - | hnsw M=16, ef_search=32 | 0.968 | 0.968 | 34500 | 1.3 (reused) | 32.8 | 656.3 |
| clean | - | hnsw M=16, ef_search=64 | 0.993 | 0.993 | 19213 | 1.3 (reused) | 32.8 | 656.3 |
| clean | - | hnsw M=16, ef_search=128 | 0.999 | 0.999 | 10113 | 1.3 (reused) | 32.8 | 656.3 |
| clean | - | hnsw M=16, ef_search=256 | 1.000 | 1.000 | 5003 | 1.3 (reused) | 32.8 | 656.3 |
| clean | - | hnsw M=16, ef_search=512 | 1.000 | 1.000 | 2276 | 1.3 (reused) | 32.8 | 656.3 |
| clean | - | ivf_flat c=1, nprobe=1 | 0.429 | 0.429 | 99933 | 0.2 (reused) | 26.1 | 522.3 |
| clean | - | ivf_flat c=1, nprobe=2 | 0.608 | 0.608 | 74867 | 0.2 (reused) | 26.1 | 522.3 |
| clean | - | ivf_flat c=1, nprobe=4 | 0.779 | 0.779 | 52990 | 0.2 (reused) | 26.1 | 522.3 |
| clean | - | ivf_flat c=1, nprobe=8 | 0.902 | 0.902 | 33601 | 0.2 (reused) | 26.1 | 522.3 |
| clean | - | ivf_flat c=1, nprobe=16 | 0.972 | 0.972 | 19653 | 0.2 (reused) | 26.1 | 522.3 |
| clean | - | ivf_flat c=1, nprobe=32 | 0.996 | 0.996 | 11161 | 0.2 (reused) | 26.1 | 522.3 |
| clean | - | ivf_flat c=1, nprobe=64 | 1.000 | 1.000 | 5994 | 0.2 (reused) | 26.1 | 522.3 |
| clean | - | ivf_flat c=1, nprobe=128 | 1.000 | 1.000 | 3144 | 0.2 (reused) | 26.1 | 522.3 |
| clean | - | ivf_pq c=1 m=64, nprobe=1 | 0.422 | 0.422 | 26068 | 7.8 (reused) | 3.8 | 77.0 |
| clean | - | ivf_pq c=1 m=64, nprobe=2 | 0.591 | 0.591 | 22213 | 7.8 (reused) | 3.8 | 77.0 |
| clean | - | ivf_pq c=1 m=64, nprobe=4 | 0.743 | 0.743 | 17261 | 7.8 (reused) | 3.8 | 77.0 |
| clean | - | ivf_pq c=1 m=64, nprobe=8 | 0.840 | 0.840 | 12175 | 7.8 (reused) | 3.8 | 77.0 |
| clean | - | ivf_pq c=1 m=64, nprobe=16 | 0.887 | 0.887 | 7712 | 7.8 (reused) | 3.8 | 77.0 |
| clean | - | ivf_pq c=1 m=64, nprobe=32 | 0.901 | 0.901 | 4453 | 7.8 (reused) | 3.8 | 77.0 |
| clean | - | ivf_pq c=1 m=64, nprobe=64 | 0.902 | 0.902 | 2438 | 7.8 (reused) | 3.8 | 77.0 |
| clean | - | ivf_pq c=1 m=64, nprobe=128 | 0.902 | 0.902 | 1309 | 7.8 (reused) | 3.8 | 77.0 |
| clean | - | ivf_pq c=1 m=64, nprobe=256 | 0.902 | 0.902 | 747 | 7.8 (reused) | 3.8 | 77.0 |
| stale | 10 | exact (flat) | 1.000 | 0.713 | 2041 | - | - | - |
| stale | 10 | hnsw M=16, ef_search=32 | 0.961 | 0.704 | 35001 | 1.3 (reused) | 32.8 | 656.3 |
| stale | 10 | hnsw M=16, ef_search=64 | 0.992 | 0.712 | 18915 | 1.3 (reused) | 32.8 | 656.3 |
| stale | 10 | hnsw M=16, ef_search=128 | 0.999 | 0.713 | 9979 | 1.3 (reused) | 32.8 | 656.3 |
| stale | 10 | hnsw M=16, ef_search=256 | 1.000 | 0.713 | 4971 | 1.3 (reused) | 32.8 | 656.3 |
| stale | 10 | hnsw M=16, ef_search=512 | 1.000 | 0.713 | 2226 | 1.3 (reused) | 32.8 | 656.3 |
| stale | 10 | ivf_flat c=1, nprobe=1 | 0.392 | 0.348 | 101635 | 0.2 (reused) | 26.1 | 522.3 |
| stale | 10 | ivf_flat c=1, nprobe=2 | 0.567 | 0.482 | 78574 | 0.2 (reused) | 26.1 | 522.3 |
| stale | 10 | ivf_flat c=1, nprobe=4 | 0.745 | 0.598 | 54705 | 0.2 (reused) | 26.1 | 522.3 |
| stale | 10 | ivf_flat c=1, nprobe=8 | 0.881 | 0.668 | 34177 | 0.2 (reused) | 26.1 | 522.3 |
| stale | 10 | ivf_flat c=1, nprobe=16 | 0.963 | 0.700 | 20243 | 0.2 (reused) | 26.1 | 522.3 |
| stale | 10 | ivf_flat c=1, nprobe=32 | 0.994 | 0.711 | 11186 | 0.2 (reused) | 26.1 | 522.3 |
| stale | 10 | ivf_flat c=1, nprobe=64 | 1.000 | 0.713 | 5943 | 0.2 (reused) | 26.1 | 522.3 |
| stale | 10 | ivf_flat c=1, nprobe=128 | 1.000 | 0.713 | 3178 | 0.2 (reused) | 26.1 | 522.3 |
| stale | 10 | ivf_pq c=1 m=64, nprobe=1 | 0.386 | 0.345 | 26185 | 7.8 (reused) | 3.8 | 77.0 |
| stale | 10 | ivf_pq c=1 m=64, nprobe=2 | 0.551 | 0.476 | 22355 | 7.8 (reused) | 3.8 | 77.0 |
| stale | 10 | ivf_pq c=1 m=64, nprobe=4 | 0.711 | 0.590 | 17596 | 7.8 (reused) | 3.8 | 77.0 |
| stale | 10 | ivf_pq c=1 m=64, nprobe=8 | 0.821 | 0.657 | 12363 | 7.8 (reused) | 3.8 | 77.0 |
| stale | 10 | ivf_pq c=1 m=64, nprobe=16 | 0.875 | 0.688 | 7744 | 7.8 (reused) | 3.8 | 77.0 |
| stale | 10 | ivf_pq c=1 m=64, nprobe=32 | 0.893 | 0.699 | 4488 | 7.8 (reused) | 3.8 | 77.0 |
| stale | 10 | ivf_pq c=1 m=64, nprobe=64 | 0.896 | 0.700 | 2444 | 7.8 (reused) | 3.8 | 77.0 |
| stale | 10 | ivf_pq c=1 m=64, nprobe=128 | 0.896 | 0.700 | 1309 | 7.8 (reused) | 3.8 | 77.0 |
| stale | 10 | ivf_pq c=1 m=64, nprobe=256 | 0.896 | 0.700 | 747 | 7.8 (reused) | 3.8 | 77.0 |
| rebuilt | 10 | exact (flat) | 1.000 | 1.000 | 2045 | - | - | - |
| rebuilt | 10 | hnsw M=16, ef_search=32 | 0.968 | 0.968 | 33636 | 1.3 | 32.8 | 656.3 |
| rebuilt | 10 | hnsw M=16, ef_search=64 | 0.993 | 0.993 | 19258 | 1.3 | 32.8 | 656.3 |
| rebuilt | 10 | hnsw M=16, ef_search=128 | 0.999 | 0.999 | 10156 | 1.3 | 32.8 | 656.3 |
| rebuilt | 10 | hnsw M=16, ef_search=256 | 1.000 | 1.000 | 5017 | 1.3 | 32.8 | 656.3 |
| rebuilt | 10 | hnsw M=16, ef_search=512 | 1.000 | 1.000 | 2262 | 1.3 | 32.8 | 656.3 |
| rebuilt | 10 | ivf_flat c=1, nprobe=1 | 0.428 | 0.428 | 100549 | 0.2 | 26.1 | 522.3 |
| rebuilt | 10 | ivf_flat c=1, nprobe=2 | 0.607 | 0.607 | 75265 | 0.2 | 26.1 | 522.3 |
| rebuilt | 10 | ivf_flat c=1, nprobe=4 | 0.778 | 0.778 | 52550 | 0.2 | 26.1 | 522.3 |
| rebuilt | 10 | ivf_flat c=1, nprobe=8 | 0.902 | 0.902 | 34287 | 0.2 | 26.1 | 522.3 |
| rebuilt | 10 | ivf_flat c=1, nprobe=16 | 0.973 | 0.973 | 19575 | 0.2 | 26.1 | 522.3 |
| rebuilt | 10 | ivf_flat c=1, nprobe=32 | 0.996 | 0.996 | 11062 | 0.2 | 26.1 | 522.3 |
| rebuilt | 10 | ivf_flat c=1, nprobe=64 | 1.000 | 1.000 | 5937 | 0.2 | 26.1 | 522.3 |
| rebuilt | 10 | ivf_flat c=1, nprobe=128 | 1.000 | 1.000 | 3061 | 0.2 | 26.1 | 522.3 |
| rebuilt | 10 | ivf_pq c=1 m=64, nprobe=1 | 0.421 | 0.421 | 25995 | 7.7 | 3.8 | 77.0 |
| rebuilt | 10 | ivf_pq c=1 m=64, nprobe=2 | 0.590 | 0.590 | 22088 | 7.7 | 3.8 | 77.0 |
| rebuilt | 10 | ivf_pq c=1 m=64, nprobe=4 | 0.741 | 0.741 | 17389 | 7.7 | 3.8 | 77.0 |
| rebuilt | 10 | ivf_pq c=1 m=64, nprobe=8 | 0.838 | 0.838 | 12200 | 7.7 | 3.8 | 77.0 |
| rebuilt | 10 | ivf_pq c=1 m=64, nprobe=16 | 0.886 | 0.886 | 7700 | 7.7 | 3.8 | 77.0 |
| rebuilt | 10 | ivf_pq c=1 m=64, nprobe=32 | 0.899 | 0.899 | 4455 | 7.7 | 3.8 | 77.0 |
| rebuilt | 10 | ivf_pq c=1 m=64, nprobe=64 | 0.901 | 0.901 | 2431 | 7.7 | 3.8 | 77.0 |
| rebuilt | 10 | ivf_pq c=1 m=64, nprobe=128 | 0.901 | 0.901 | 1308 | 7.7 | 3.8 | 77.0 |
| rebuilt | 10 | ivf_pq c=1 m=64, nprobe=256 | 0.901 | 0.901 | 733 | 7.7 | 3.8 | 77.0 |
