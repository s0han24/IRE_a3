| setting | config | clean recall | stale - clean (original) | stale - clean (own) | rebuilt - clean (original) | rebuilt - clean (own) |
|---|---|---|---|---|---|---|
| 5 | exact (flat) | 1.000 | -0.159 | +0.000 | +0.000 | +0.000 |
| 5 | hnsw M=16, ef_search=32 | 0.968 | -0.140 | -0.000 | +0.000 | +0.000 |
| 5 | hnsw M=16, ef_search=64 | 0.993 | -0.154 | -0.000 | +0.000 | +0.000 |
| 5 | hnsw M=16, ef_search=128 | 0.999 | -0.158 | -0.000 | +0.000 | +0.000 |
| 5 | hnsw M=16, ef_search=256 | 1.000 | -0.158 | +0.000 | +0.000 | +0.000 |
| 5 | hnsw M=16, ef_search=512 | 1.000 | -0.159 | -0.000 | +0.000 | +0.000 |
| 5 | ivf_flat c=1, nprobe=1 | 0.429 | -0.031 | -0.010 | +0.000 | +0.000 |
| 5 | ivf_flat c=1, nprobe=2 | 0.608 | -0.053 | -0.009 | +0.000 | +0.000 |
| 5 | ivf_flat c=1, nprobe=4 | 0.779 | -0.082 | -0.005 | +0.000 | +0.000 |
| 5 | ivf_flat c=1, nprobe=8 | 0.902 | -0.117 | -0.002 | +0.000 | +0.000 |
| 5 | ivf_flat c=1, nprobe=16 | 0.972 | -0.145 | -0.001 | +0.000 | +0.000 |
| 5 | ivf_flat c=1, nprobe=32 | 0.996 | -0.157 | -0.000 | +0.000 | +0.000 |
| 5 | ivf_flat c=1, nprobe=64 | 1.000 | -0.158 | +0.000 | +0.000 | +0.000 |
| 5 | ivf_flat c=1, nprobe=128 | 1.000 | -0.159 | +0.000 | +0.000 | +0.000 |
| 5 | ivf_pq c=1 m=64, nprobe=1 | 0.422 | -0.028 | -0.011 | -0.000 | -0.000 |
| 5 | ivf_pq c=1 m=64, nprobe=2 | 0.591 | -0.043 | -0.009 | -0.000 | -0.000 |
| 5 | ivf_pq c=1 m=64, nprobe=4 | 0.743 | -0.060 | -0.006 | -0.000 | -0.000 |
| 5 | ivf_pq c=1 m=64, nprobe=8 | 0.840 | -0.075 | -0.005 | -0.000 | -0.000 |
| 5 | ivf_pq c=1 m=64, nprobe=16 | 0.887 | -0.083 | -0.004 | -0.001 | -0.001 |
| 5 | ivf_pq c=1 m=64, nprobe=32 | 0.901 | -0.085 | -0.004 | -0.001 | -0.001 |
| 5 | ivf_pq c=1 m=64, nprobe=64 | 0.902 | -0.085 | -0.004 | -0.001 | -0.001 |
| 5 | ivf_pq c=1 m=64, nprobe=128 | 0.902 | -0.085 | -0.004 | -0.001 | -0.001 |
| 5 | ivf_pq c=1 m=64, nprobe=256 | 0.902 | -0.085 | -0.004 | -0.001 | -0.001 |

First setting at which each index has no config with recall (original) >= 0.95:

| index | clean | stale | rebuilt |
|---|---|---|---|
| exact | has 0.95 | lost at 5 | kept at all settings |
| hnsw | has 0.95 | lost at 5 | kept at all settings |
| ivf_flat | has 0.95 | lost at 5 | kept at all settings |
| ivf_pq | **never reached** | n/a | n/a |

**stale: first to lose its 0.95 config: exact, hnsw, ivf_flat (at 5)**

**rebuilt: no index that had a 0.95 config lost it**
