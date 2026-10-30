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
| stale | 5 | exact (flat) | 1.000 | 0.841 | 2004 | - | - | - |
| stale | 5 | hnsw M=16, ef_search=32 | 0.968 | 0.828 | 34000 | 1.3 (reused) | 32.8 | 656.3 |
| stale | 5 | hnsw M=16, ef_search=64 | 0.993 | 0.839 | 19772 | 1.3 (reused) | 32.8 | 656.3 |
| stale | 5 | hnsw M=16, ef_search=128 | 0.999 | 0.841 | 10001 | 1.3 (reused) | 32.8 | 656.3 |
| stale | 5 | hnsw M=16, ef_search=256 | 1.000 | 0.841 | 5121 | 1.3 (reused) | 32.8 | 656.3 |
| stale | 5 | hnsw M=16, ef_search=512 | 1.000 | 0.841 | 2260 | 1.3 (reused) | 32.8 | 656.3 |
| stale | 5 | ivf_flat c=1, nprobe=1 | 0.419 | 0.398 | 102432 | 0.2 (reused) | 26.1 | 522.3 |
| stale | 5 | ivf_flat c=1, nprobe=2 | 0.599 | 0.555 | 73438 | 0.2 (reused) | 26.1 | 522.3 |
| stale | 5 | ivf_flat c=1, nprobe=4 | 0.774 | 0.696 | 52459 | 0.2 (reused) | 26.1 | 522.3 |
| stale | 5 | ivf_flat c=1, nprobe=8 | 0.900 | 0.785 | 33361 | 0.2 (reused) | 26.1 | 522.3 |
| stale | 5 | ivf_flat c=1, nprobe=16 | 0.971 | 0.827 | 20061 | 0.2 (reused) | 26.1 | 522.3 |
| stale | 5 | ivf_flat c=1, nprobe=32 | 0.996 | 0.839 | 10961 | 0.2 (reused) | 26.1 | 522.3 |
| stale | 5 | ivf_flat c=1, nprobe=64 | 1.000 | 0.841 | 5942 | 0.2 (reused) | 26.1 | 522.3 |
| stale | 5 | ivf_flat c=1, nprobe=128 | 1.000 | 0.841 | 3171 | 0.2 (reused) | 26.1 | 522.3 |
| stale | 5 | ivf_pq c=1 m=64, nprobe=1 | 0.411 | 0.395 | 25994 | 7.8 (reused) | 3.8 | 77.0 |
| stale | 5 | ivf_pq c=1 m=64, nprobe=2 | 0.582 | 0.548 | 22239 | 7.8 (reused) | 3.8 | 77.0 |
| stale | 5 | ivf_pq c=1 m=64, nprobe=4 | 0.736 | 0.683 | 17405 | 7.8 (reused) | 3.8 | 77.0 |
| stale | 5 | ivf_pq c=1 m=64, nprobe=8 | 0.835 | 0.765 | 12201 | 7.8 (reused) | 3.8 | 77.0 |
| stale | 5 | ivf_pq c=1 m=64, nprobe=16 | 0.883 | 0.804 | 7677 | 7.8 (reused) | 3.8 | 77.0 |
| stale | 5 | ivf_pq c=1 m=64, nprobe=32 | 0.897 | 0.815 | 4475 | 7.8 (reused) | 3.8 | 77.0 |
| stale | 5 | ivf_pq c=1 m=64, nprobe=64 | 0.899 | 0.817 | 2439 | 7.8 (reused) | 3.8 | 77.0 |
| stale | 5 | ivf_pq c=1 m=64, nprobe=128 | 0.899 | 0.817 | 1309 | 7.8 (reused) | 3.8 | 77.0 |
| stale | 5 | ivf_pq c=1 m=64, nprobe=256 | 0.899 | 0.817 | 747 | 7.8 (reused) | 3.8 | 77.0 |
| rebuilt | 5 | exact (flat) | 1.000 | 1.000 | 2015 | - | - | - |
| rebuilt | 5 | hnsw M=16, ef_search=32 | 0.968 | 0.968 | 34167 | 1.2 | 32.8 | 656.3 |
| rebuilt | 5 | hnsw M=16, ef_search=64 | 0.993 | 0.993 | 19245 | 1.2 | 32.8 | 656.3 |
| rebuilt | 5 | hnsw M=16, ef_search=128 | 0.999 | 0.999 | 9866 | 1.2 | 32.8 | 656.3 |
| rebuilt | 5 | hnsw M=16, ef_search=256 | 1.000 | 1.000 | 5153 | 1.2 | 32.8 | 656.3 |
| rebuilt | 5 | hnsw M=16, ef_search=512 | 1.000 | 1.000 | 2310 | 1.2 | 32.8 | 656.3 |
| rebuilt | 5 | ivf_flat c=1, nprobe=1 | 0.429 | 0.429 | 98461 | 0.2 | 26.1 | 522.3 |
| rebuilt | 5 | ivf_flat c=1, nprobe=2 | 0.608 | 0.608 | 73547 | 0.2 | 26.1 | 522.3 |
| rebuilt | 5 | ivf_flat c=1, nprobe=4 | 0.779 | 0.779 | 51253 | 0.2 | 26.1 | 522.3 |
| rebuilt | 5 | ivf_flat c=1, nprobe=8 | 0.902 | 0.902 | 32291 | 0.2 | 26.1 | 522.3 |
| rebuilt | 5 | ivf_flat c=1, nprobe=16 | 0.972 | 0.972 | 18791 | 0.2 | 26.1 | 522.3 |
| rebuilt | 5 | ivf_flat c=1, nprobe=32 | 0.996 | 0.996 | 10523 | 0.2 | 26.1 | 522.3 |
| rebuilt | 5 | ivf_flat c=1, nprobe=64 | 1.000 | 1.000 | 5754 | 0.2 | 26.1 | 522.3 |
| rebuilt | 5 | ivf_flat c=1, nprobe=128 | 1.000 | 1.000 | 3153 | 0.2 | 26.1 | 522.3 |
| rebuilt | 5 | ivf_pq c=1 m=64, nprobe=1 | 0.422 | 0.422 | 25855 | 7.3 | 3.8 | 77.0 |
| rebuilt | 5 | ivf_pq c=1 m=64, nprobe=2 | 0.590 | 0.590 | 22196 | 7.3 | 3.8 | 77.0 |
| rebuilt | 5 | ivf_pq c=1 m=64, nprobe=4 | 0.742 | 0.742 | 17482 | 7.3 | 3.8 | 77.0 |
| rebuilt | 5 | ivf_pq c=1 m=64, nprobe=8 | 0.840 | 0.840 | 12253 | 7.3 | 3.8 | 77.0 |
| rebuilt | 5 | ivf_pq c=1 m=64, nprobe=16 | 0.886 | 0.886 | 7678 | 7.3 | 3.8 | 77.0 |
| rebuilt | 5 | ivf_pq c=1 m=64, nprobe=32 | 0.900 | 0.900 | 4483 | 7.3 | 3.8 | 77.0 |
| rebuilt | 5 | ivf_pq c=1 m=64, nprobe=64 | 0.902 | 0.902 | 2439 | 7.3 | 3.8 | 77.0 |
| rebuilt | 5 | ivf_pq c=1 m=64, nprobe=128 | 0.902 | 0.902 | 1154 | 7.3 | 3.8 | 77.0 |
| rebuilt | 5 | ivf_pq c=1 m=64, nprobe=256 | 0.902 | 0.902 | 659 | 7.3 | 3.8 | 77.0 |
