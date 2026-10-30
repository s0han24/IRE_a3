| setting | config | clean recall | stale - clean (original) | stale - clean (own) | rebuilt - clean (original) | rebuilt - clean (own) |
|---|---|---|---|---|---|---|
| 10 | exact (flat) | 1.000 | -0.287 | +0.000 | +0.000 | +0.000 |
| 10 | hnsw M=16, ef_search=32 | 0.968 | -0.264 | -0.007 | +0.000 | +0.000 |
| 10 | hnsw M=16, ef_search=64 | 0.993 | -0.281 | -0.001 | +0.000 | +0.000 |
| 10 | hnsw M=16, ef_search=128 | 0.999 | -0.286 | -0.000 | +0.000 | +0.000 |
| 10 | hnsw M=16, ef_search=256 | 1.000 | -0.287 | +0.000 | +0.000 | +0.000 |
| 10 | hnsw M=16, ef_search=512 | 1.000 | -0.287 | -0.000 | +0.000 | +0.000 |
| 10 | ivf_flat c=1, nprobe=1 | 0.429 | -0.081 | -0.037 | -0.001 | -0.001 |
| 10 | ivf_flat c=1, nprobe=2 | 0.608 | -0.126 | -0.041 | -0.000 | -0.000 |
| 10 | ivf_flat c=1, nprobe=4 | 0.779 | -0.181 | -0.034 | -0.001 | -0.001 |
| 10 | ivf_flat c=1, nprobe=8 | 0.902 | -0.235 | -0.022 | -0.000 | -0.000 |
| 10 | ivf_flat c=1, nprobe=16 | 0.972 | -0.273 | -0.009 | +0.000 | +0.000 |
| 10 | ivf_flat c=1, nprobe=32 | 0.996 | -0.285 | -0.002 | -0.000 | -0.000 |
| 10 | ivf_flat c=1, nprobe=64 | 1.000 | -0.287 | -0.000 | +0.000 | +0.000 |
| 10 | ivf_flat c=1, nprobe=128 | 1.000 | -0.287 | +0.000 | +0.000 | +0.000 |
| 10 | ivf_pq c=1 m=64, nprobe=1 | 0.422 | -0.078 | -0.037 | -0.001 | -0.001 |
| 10 | ivf_pq c=1 m=64, nprobe=2 | 0.591 | -0.115 | -0.039 | -0.001 | -0.001 |
| 10 | ivf_pq c=1 m=64, nprobe=4 | 0.743 | -0.152 | -0.031 | -0.002 | -0.002 |
| 10 | ivf_pq c=1 m=64, nprobe=8 | 0.840 | -0.183 | -0.019 | -0.002 | -0.002 |
| 10 | ivf_pq c=1 m=64, nprobe=16 | 0.887 | -0.199 | -0.012 | -0.001 | -0.001 |
| 10 | ivf_pq c=1 m=64, nprobe=32 | 0.901 | -0.202 | -0.008 | -0.002 | -0.002 |
| 10 | ivf_pq c=1 m=64, nprobe=64 | 0.902 | -0.202 | -0.007 | -0.002 | -0.002 |
| 10 | ivf_pq c=1 m=64, nprobe=128 | 0.902 | -0.202 | -0.007 | -0.002 | -0.002 |
| 10 | ivf_pq c=1 m=64, nprobe=256 | 0.902 | -0.202 | -0.007 | -0.002 | -0.002 |

First setting at which each index has no config with recall (original) >= 0.95:

| index | clean | stale | rebuilt |
|---|---|---|---|
| exact | has 0.95 | lost at 10 | kept at all settings |
| hnsw | has 0.95 | lost at 10 | kept at all settings |
| ivf_flat | has 0.95 | lost at 10 | kept at all settings |
| ivf_pq | **never reached** | n/a | n/a |

**stale: first to lose its 0.95 config: exact, hnsw, ivf_flat (at 10)**

**rebuilt: no index that had a 0.95 config lost it**
