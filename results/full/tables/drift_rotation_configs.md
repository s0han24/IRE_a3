| condition | setting | config | recall (own) | recall (original) | QPS | build s | size MB | bytes/vector |
|---|---|---|---|---|---|---|---|---|
| clean | - | exact (flat) | 1.000 | 1.000 | 341 | - | - | - |
| clean | - | hnsw M=16, ef_search=32 | 0.933 | 0.933 | 18133 | 23.1 (reused) | 196.9 | 656.3 |
| clean | - | hnsw M=16, ef_search=64 | 0.980 | 0.980 | 10398 | 23.1 (reused) | 196.9 | 656.3 |
| clean | - | hnsw M=16, ef_search=128 | 0.996 | 0.996 | 5573 | 23.1 (reused) | 196.9 | 656.3 |
| clean | - | hnsw M=16, ef_search=256 | 1.000 | 1.000 | 2881 | 23.1 (reused) | 196.9 | 656.3 |
| clean | - | hnsw M=16, ef_search=512 | 1.000 | 1.000 | 1385 | 23.1 (reused) | 196.9 | 656.3 |
| clean | - | hnsw M=32, ef_search=32 | 0.955 | 0.955 | 14350 | 19.9 (reused) | 235.2 | 784.1 |
| clean | - | hnsw M=32, ef_search=64 | 0.989 | 0.989 | 8333 | 19.9 (reused) | 235.2 | 784.1 |
| clean | - | hnsw M=32, ef_search=128 | 0.998 | 0.998 | 4644 | 19.9 (reused) | 235.2 | 784.1 |
| clean | - | hnsw M=32, ef_search=256 | 1.000 | 1.000 | 2374 | 19.9 (reused) | 235.2 | 784.1 |
| clean | - | hnsw M=32, ef_search=512 | 1.000 | 1.000 | 1226 | 19.9 (reused) | 235.2 | 784.1 |
| clean | - | ivf_flat c=1, nprobe=1 | 0.396 | 0.396 | 55994 | 1.6 (reused) | 156.3 | 521.0 |
| clean | - | ivf_flat c=1, nprobe=2 | 0.566 | 0.566 | 40432 | 1.6 (reused) | 156.3 | 521.0 |
| clean | - | ivf_flat c=1, nprobe=4 | 0.732 | 0.732 | 25960 | 1.6 (reused) | 156.3 | 521.0 |
| clean | - | ivf_flat c=1, nprobe=8 | 0.867 | 0.867 | 15336 | 1.6 (reused) | 156.3 | 521.0 |
| clean | - | ivf_flat c=1, nprobe=16 | 0.951 | 0.951 | 8443 | 1.6 (reused) | 156.3 | 521.0 |
| clean | - | ivf_flat c=1, nprobe=32 | 0.988 | 0.988 | 4556 | 1.6 (reused) | 156.3 | 521.0 |
| clean | - | ivf_flat c=1, nprobe=64 | 0.998 | 0.998 | 2282 | 1.6 (reused) | 156.3 | 521.0 |
| clean | - | ivf_flat c=1, nprobe=128 | 1.000 | 1.000 | 1224 | 1.6 (reused) | 156.3 | 521.0 |
| clean | - | ivf_flat c=4, nprobe=1 | 0.307 | 0.307 | 34965 | 11.5 (reused) | 157.1 | 523.8 |
| clean | - | ivf_flat c=4, nprobe=2 | 0.450 | 0.450 | 32403 | 11.5 (reused) | 157.1 | 523.8 |
| clean | - | ivf_flat c=4, nprobe=4 | 0.606 | 0.606 | 28270 | 11.5 (reused) | 157.1 | 523.8 |
| clean | - | ivf_flat c=4, nprobe=8 | 0.750 | 0.750 | 22225 | 11.5 (reused) | 157.1 | 523.8 |
| clean | - | ivf_flat c=4, nprobe=16 | 0.867 | 0.867 | 15682 | 11.5 (reused) | 157.1 | 523.8 |
| clean | - | ivf_flat c=4, nprobe=32 | 0.945 | 0.945 | 10016 | 11.5 (reused) | 157.1 | 523.8 |
| clean | - | ivf_flat c=4, nprobe=64 | 0.982 | 0.982 | 5890 | 11.5 (reused) | 157.1 | 523.8 |
| clean | - | ivf_flat c=4, nprobe=128 | 0.996 | 0.996 | 3163 | 11.5 (reused) | 157.1 | 523.8 |
| clean | - | ivf_pq c=4 m=32, nprobe=1 | 0.296 | 0.296 | 21834 | 13.7 (reused) | 13.3 | 44.2 |
| clean | - | ivf_pq c=4 m=32, nprobe=2 | 0.423 | 0.423 | 20263 | 13.7 (reused) | 13.3 | 44.2 |
| clean | - | ivf_pq c=4 m=32, nprobe=4 | 0.545 | 0.545 | 18265 | 13.7 (reused) | 13.3 | 44.2 |
| clean | - | ivf_pq c=4 m=32, nprobe=8 | 0.642 | 0.642 | 15252 | 13.7 (reused) | 13.3 | 44.2 |
| clean | - | ivf_pq c=4 m=32, nprobe=16 | 0.708 | 0.708 | 11557 | 13.7 (reused) | 13.3 | 44.2 |
| clean | - | ivf_pq c=4 m=32, nprobe=32 | 0.742 | 0.742 | 7771 | 13.7 (reused) | 13.3 | 44.2 |
| clean | - | ivf_pq c=4 m=32, nprobe=64 | 0.755 | 0.755 | 4726 | 13.7 (reused) | 13.3 | 44.2 |
| clean | - | ivf_pq c=4 m=32, nprobe=128 | 0.759 | 0.759 | 2618 | 13.7 (reused) | 13.3 | 44.2 |
| clean | - | ivf_pq c=4 m=32, nprobe=256 | 0.759 | 0.759 | 1411 | 13.7 (reused) | 13.3 | 44.2 |
| clean | - | ivf_pq c=4 m=64, nprobe=1 | 0.304 | 0.304 | 17916 | 15.6 (reused) | 22.9 | 76.2 |
| clean | - | ivf_pq c=4 m=64, nprobe=2 | 0.442 | 0.442 | 16195 | 15.6 (reused) | 22.9 | 76.2 |
| clean | - | ivf_pq c=4 m=64, nprobe=4 | 0.588 | 0.588 | 13704 | 15.6 (reused) | 22.9 | 76.2 |
| clean | - | ivf_pq c=4 m=64, nprobe=8 | 0.714 | 0.714 | 10524 | 15.6 (reused) | 22.9 | 76.2 |
| clean | - | ivf_pq c=4 m=64, nprobe=16 | 0.809 | 0.809 | 7250 | 15.6 (reused) | 22.9 | 76.2 |
| clean | - | ivf_pq c=4 m=64, nprobe=32 | 0.862 | 0.862 | 4479 | 15.6 (reused) | 22.9 | 76.2 |
| clean | - | ivf_pq c=4 m=64, nprobe=64 | 0.884 | 0.884 | 2554 | 15.6 (reused) | 22.9 | 76.2 |
| clean | - | ivf_pq c=4 m=64, nprobe=128 | 0.891 | 0.891 | 1363 | 15.6 (reused) | 22.9 | 76.2 |
| clean | - | ivf_pq c=4 m=64, nprobe=256 | 0.893 | 0.893 | 718 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 2 | exact (flat) | 1.000 | 0.920 | 193 | - | - | - |
| stale | 2 | hnsw M=16, ef_search=32 | 0.932 | 0.877 | 15677 | 23.1 (reused) | 196.9 | 656.3 |
| stale | 2 | hnsw M=16, ef_search=64 | 0.979 | 0.909 | 9034 | 23.1 (reused) | 196.9 | 656.3 |
| stale | 2 | hnsw M=16, ef_search=128 | 0.995 | 0.918 | 4969 | 23.1 (reused) | 196.9 | 656.3 |
| stale | 2 | hnsw M=16, ef_search=256 | 0.999 | 0.920 | 2739 | 23.1 (reused) | 196.9 | 656.3 |
| stale | 2 | hnsw M=16, ef_search=512 | 1.000 | 0.920 | 1366 | 23.1 (reused) | 196.9 | 656.3 |
| stale | 2 | hnsw M=32, ef_search=32 | 0.956 | 0.893 | 14654 | 19.9 (reused) | 235.2 | 784.1 |
| stale | 2 | hnsw M=32, ef_search=64 | 0.989 | 0.913 | 8204 | 19.9 (reused) | 235.2 | 784.1 |
| stale | 2 | hnsw M=32, ef_search=128 | 0.998 | 0.919 | 4453 | 19.9 (reused) | 235.2 | 784.1 |
| stale | 2 | hnsw M=32, ef_search=256 | 1.000 | 0.920 | 2343 | 19.9 (reused) | 235.2 | 784.1 |
| stale | 2 | hnsw M=32, ef_search=512 | 1.000 | 0.920 | 1167 | 19.9 (reused) | 235.2 | 784.1 |
| stale | 2 | ivf_flat c=1, nprobe=1 | 0.395 | 0.386 | 51407 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 2 | ivf_flat c=1, nprobe=2 | 0.566 | 0.550 | 32002 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 2 | ivf_flat c=1, nprobe=4 | 0.731 | 0.701 | 19734 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 2 | ivf_flat c=1, nprobe=8 | 0.866 | 0.819 | 10603 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 2 | ivf_flat c=1, nprobe=16 | 0.950 | 0.887 | 5510 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 2 | ivf_flat c=1, nprobe=32 | 0.988 | 0.913 | 2714 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 2 | ivf_flat c=1, nprobe=64 | 0.998 | 0.919 | 1613 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 2 | ivf_flat c=1, nprobe=128 | 1.000 | 0.920 | 833 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 2 | ivf_flat c=4, nprobe=1 | 0.304 | 0.299 | 18745 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 2 | ivf_flat c=4, nprobe=2 | 0.448 | 0.440 | 17904 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 2 | ivf_flat c=4, nprobe=4 | 0.603 | 0.586 | 17918 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 2 | ivf_flat c=4, nprobe=8 | 0.748 | 0.719 | 15003 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 2 | ivf_flat c=4, nprobe=16 | 0.865 | 0.821 | 11153 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 2 | ivf_flat c=4, nprobe=32 | 0.944 | 0.882 | 7338 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 2 | ivf_flat c=4, nprobe=64 | 0.982 | 0.909 | 4372 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 2 | ivf_flat c=4, nprobe=128 | 0.997 | 0.918 | 2387 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 2 | ivf_pq c=4 m=32, nprobe=1 | 0.293 | 0.290 | 14981 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 2 | ivf_pq c=4 m=32, nprobe=2 | 0.421 | 0.417 | 14030 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 2 | ivf_pq c=4 m=32, nprobe=4 | 0.542 | 0.535 | 13921 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 2 | ivf_pq c=4 m=32, nprobe=8 | 0.639 | 0.631 | 11774 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 2 | ivf_pq c=4 m=32, nprobe=16 | 0.706 | 0.696 | 8308 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 2 | ivf_pq c=4 m=32, nprobe=32 | 0.740 | 0.730 | 6322 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 2 | ivf_pq c=4 m=32, nprobe=64 | 0.752 | 0.743 | 3563 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 2 | ivf_pq c=4 m=32, nprobe=128 | 0.756 | 0.746 | 2218 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 2 | ivf_pq c=4 m=32, nprobe=256 | 0.756 | 0.747 | 1167 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 2 | ivf_pq c=4 m=64, nprobe=1 | 0.301 | 0.297 | 12278 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 2 | ivf_pq c=4 m=64, nprobe=2 | 0.441 | 0.435 | 10350 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 2 | ivf_pq c=4 m=64, nprobe=4 | 0.586 | 0.576 | 10245 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 2 | ivf_pq c=4 m=64, nprobe=8 | 0.713 | 0.698 | 8285 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 2 | ivf_pq c=4 m=64, nprobe=16 | 0.807 | 0.787 | 5836 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 2 | ivf_pq c=4 m=64, nprobe=32 | 0.860 | 0.837 | 3745 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 2 | ivf_pq c=4 m=64, nprobe=64 | 0.882 | 0.858 | 2172 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 2 | ivf_pq c=4 m=64, nprobe=128 | 0.890 | 0.865 | 1166 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 2 | ivf_pq c=4 m=64, nprobe=256 | 0.891 | 0.866 | 569 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 3 | exact (flat) | 1.000 | 0.882 | 222 | - | - | - |
| stale | 3 | hnsw M=16, ef_search=32 | 0.933 | 0.845 | 16001 | 23.1 (reused) | 196.9 | 656.3 |
| stale | 3 | hnsw M=16, ef_search=64 | 0.979 | 0.872 | 9552 | 23.1 (reused) | 196.9 | 656.3 |
| stale | 3 | hnsw M=16, ef_search=128 | 0.995 | 0.880 | 5238 | 23.1 (reused) | 196.9 | 656.3 |
| stale | 3 | hnsw M=16, ef_search=256 | 0.999 | 0.882 | 2767 | 23.1 (reused) | 196.9 | 656.3 |
| stale | 3 | hnsw M=16, ef_search=512 | 1.000 | 0.882 | 1383 | 23.1 (reused) | 196.9 | 656.3 |
| stale | 3 | hnsw M=32, ef_search=32 | 0.955 | 0.859 | 14894 | 19.9 (reused) | 235.2 | 784.1 |
| stale | 3 | hnsw M=32, ef_search=64 | 0.989 | 0.877 | 8352 | 19.9 (reused) | 235.2 | 784.1 |
| stale | 3 | hnsw M=32, ef_search=128 | 0.998 | 0.881 | 4554 | 19.9 (reused) | 235.2 | 784.1 |
| stale | 3 | hnsw M=32, ef_search=256 | 1.000 | 0.882 | 2420 | 19.9 (reused) | 235.2 | 784.1 |
| stale | 3 | hnsw M=32, ef_search=512 | 1.000 | 0.882 | 1208 | 19.9 (reused) | 235.2 | 784.1 |
| stale | 3 | ivf_flat c=1, nprobe=1 | 0.395 | 0.380 | 54413 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 3 | ivf_flat c=1, nprobe=2 | 0.565 | 0.538 | 37504 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 3 | ivf_flat c=1, nprobe=4 | 0.729 | 0.683 | 22625 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 3 | ivf_flat c=1, nprobe=8 | 0.866 | 0.792 | 13104 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 3 | ivf_flat c=1, nprobe=16 | 0.950 | 0.853 | 7069 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 3 | ivf_flat c=1, nprobe=32 | 0.988 | 0.876 | 3574 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 3 | ivf_flat c=1, nprobe=64 | 0.998 | 0.881 | 1825 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 3 | ivf_flat c=1, nprobe=128 | 1.000 | 0.882 | 912 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 3 | ivf_flat c=4, nprobe=1 | 0.302 | 0.295 | 23501 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 3 | ivf_flat c=4, nprobe=2 | 0.448 | 0.433 | 21796 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 3 | ivf_flat c=4, nprobe=4 | 0.600 | 0.574 | 19285 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 3 | ivf_flat c=4, nprobe=8 | 0.745 | 0.700 | 15938 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 3 | ivf_flat c=4, nprobe=16 | 0.864 | 0.794 | 10209 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 3 | ivf_flat c=4, nprobe=32 | 0.944 | 0.850 | 7783 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 3 | ivf_flat c=4, nprobe=64 | 0.982 | 0.873 | 4713 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 3 | ivf_flat c=4, nprobe=128 | 0.997 | 0.880 | 2588 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 3 | ivf_pq c=4 m=32, nprobe=1 | 0.291 | 0.287 | 17437 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 3 | ivf_pq c=4 m=32, nprobe=2 | 0.420 | 0.411 | 16246 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 3 | ivf_pq c=4 m=32, nprobe=4 | 0.540 | 0.527 | 15015 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 3 | ivf_pq c=4 m=32, nprobe=8 | 0.638 | 0.621 | 12779 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 3 | ivf_pq c=4 m=32, nprobe=16 | 0.704 | 0.684 | 9783 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 3 | ivf_pq c=4 m=32, nprobe=32 | 0.739 | 0.718 | 6834 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 3 | ivf_pq c=4 m=32, nprobe=64 | 0.752 | 0.730 | 4222 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 3 | ivf_pq c=4 m=32, nprobe=128 | 0.755 | 0.734 | 2334 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 3 | ivf_pq c=4 m=32, nprobe=256 | 0.756 | 0.734 | 1268 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 3 | ivf_pq c=4 m=64, nprobe=1 | 0.299 | 0.293 | 13199 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 3 | ivf_pq c=4 m=64, nprobe=2 | 0.440 | 0.428 | 12362 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 3 | ivf_pq c=4 m=64, nprobe=4 | 0.583 | 0.564 | 10695 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 3 | ivf_pq c=4 m=64, nprobe=8 | 0.711 | 0.682 | 8626 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 3 | ivf_pq c=4 m=64, nprobe=16 | 0.805 | 0.768 | 6021 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 3 | ivf_pq c=4 m=64, nprobe=32 | 0.860 | 0.815 | 3810 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 3 | ivf_pq c=4 m=64, nprobe=64 | 0.882 | 0.835 | 2202 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 3 | ivf_pq c=4 m=64, nprobe=128 | 0.890 | 0.841 | 1190 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 3 | ivf_pq c=4 m=64, nprobe=256 | 0.891 | 0.843 | 624 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 5 | exact (flat) | 1.000 | 0.812 | 217 | - | - | - |
| stale | 5 | hnsw M=16, ef_search=32 | 0.930 | 0.783 | 14464 | 23.1 (reused) | 196.9 | 656.3 |
| stale | 5 | hnsw M=16, ef_search=64 | 0.979 | 0.805 | 9300 | 23.1 (reused) | 196.9 | 656.3 |
| stale | 5 | hnsw M=16, ef_search=128 | 0.995 | 0.811 | 5134 | 23.1 (reused) | 196.9 | 656.3 |
| stale | 5 | hnsw M=16, ef_search=256 | 0.999 | 0.812 | 2690 | 23.1 (reused) | 196.9 | 656.3 |
| stale | 5 | hnsw M=16, ef_search=512 | 1.000 | 0.812 | 1365 | 23.1 (reused) | 196.9 | 656.3 |
| stale | 5 | hnsw M=32, ef_search=32 | 0.954 | 0.793 | 14481 | 19.9 (reused) | 235.2 | 784.1 |
| stale | 5 | hnsw M=32, ef_search=64 | 0.988 | 0.808 | 8010 | 19.9 (reused) | 235.2 | 784.1 |
| stale | 5 | hnsw M=32, ef_search=128 | 0.998 | 0.812 | 4393 | 19.9 (reused) | 235.2 | 784.1 |
| stale | 5 | hnsw M=32, ef_search=256 | 1.000 | 0.812 | 2386 | 19.9 (reused) | 235.2 | 784.1 |
| stale | 5 | hnsw M=32, ef_search=512 | 1.000 | 0.812 | 1083 | 19.9 (reused) | 235.2 | 784.1 |
| stale | 5 | ivf_flat c=1, nprobe=1 | 0.394 | 0.366 | 36773 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 5 | ivf_flat c=1, nprobe=2 | 0.563 | 0.512 | 24894 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 5 | ivf_flat c=1, nprobe=4 | 0.728 | 0.642 | 13940 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 5 | ivf_flat c=1, nprobe=8 | 0.863 | 0.736 | 8705 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 5 | ivf_flat c=1, nprobe=16 | 0.949 | 0.788 | 4636 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 5 | ivf_flat c=1, nprobe=32 | 0.987 | 0.807 | 3400 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 5 | ivf_flat c=1, nprobe=64 | 0.998 | 0.811 | 1667 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 5 | ivf_flat c=1, nprobe=128 | 1.000 | 0.812 | 821 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 5 | ivf_flat c=4, nprobe=1 | 0.298 | 0.283 | 21528 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 5 | ivf_flat c=4, nprobe=2 | 0.444 | 0.414 | 19415 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 5 | ivf_flat c=4, nprobe=4 | 0.596 | 0.545 | 16727 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 5 | ivf_flat c=4, nprobe=8 | 0.742 | 0.657 | 14231 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 5 | ivf_flat c=4, nprobe=16 | 0.861 | 0.739 | 11133 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 5 | ivf_flat c=4, nprobe=32 | 0.943 | 0.786 | 7560 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 5 | ivf_flat c=4, nprobe=64 | 0.981 | 0.804 | 4123 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 5 | ivf_flat c=4, nprobe=128 | 0.997 | 0.811 | 2442 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 5 | ivf_pq c=4 m=32, nprobe=1 | 0.287 | 0.276 | 16262 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 5 | ivf_pq c=4 m=32, nprobe=2 | 0.417 | 0.395 | 13286 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 5 | ivf_pq c=4 m=32, nprobe=4 | 0.538 | 0.506 | 12745 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 5 | ivf_pq c=4 m=32, nprobe=8 | 0.635 | 0.592 | 8816 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 5 | ivf_pq c=4 m=32, nprobe=16 | 0.701 | 0.652 | 7856 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 5 | ivf_pq c=4 m=32, nprobe=32 | 0.737 | 0.684 | 5983 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 5 | ivf_pq c=4 m=32, nprobe=64 | 0.749 | 0.695 | 4037 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 5 | ivf_pq c=4 m=32, nprobe=128 | 0.753 | 0.698 | 2221 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 5 | ivf_pq c=4 m=32, nprobe=256 | 0.754 | 0.699 | 1218 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 5 | ivf_pq c=4 m=64, nprobe=1 | 0.295 | 0.282 | 12070 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 5 | ivf_pq c=4 m=64, nprobe=2 | 0.436 | 0.410 | 11758 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 5 | ivf_pq c=4 m=64, nprobe=4 | 0.580 | 0.538 | 10169 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 5 | ivf_pq c=4 m=64, nprobe=8 | 0.708 | 0.644 | 8021 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 5 | ivf_pq c=4 m=64, nprobe=16 | 0.803 | 0.721 | 5662 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 5 | ivf_pq c=4 m=64, nprobe=32 | 0.857 | 0.763 | 3288 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 5 | ivf_pq c=4 m=64, nprobe=64 | 0.881 | 0.780 | 1901 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 5 | ivf_pq c=4 m=64, nprobe=128 | 0.889 | 0.786 | 1106 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 5 | ivf_pq c=4 m=64, nprobe=256 | 0.890 | 0.787 | 574 | 15.6 (reused) | 22.9 | 76.2 |
| rebuilt | 2 | exact (flat) | 1.000 | 1.000 | 196 | - | - | - |
| rebuilt | 2 | hnsw M=16, ef_search=32 | 0.934 | 0.934 | 11969 | 29.2 | 196.9 | 656.3 |
| rebuilt | 2 | hnsw M=16, ef_search=64 | 0.980 | 0.980 | 9605 | 29.2 | 196.9 | 656.3 |
| rebuilt | 2 | hnsw M=16, ef_search=128 | 0.996 | 0.996 | 5193 | 29.2 | 196.9 | 656.3 |
| rebuilt | 2 | hnsw M=16, ef_search=256 | 0.999 | 0.999 | 2727 | 29.2 | 196.9 | 656.3 |
| rebuilt | 2 | hnsw M=16, ef_search=512 | 1.000 | 1.000 | 1366 | 29.2 | 196.9 | 656.3 |
| rebuilt | 2 | hnsw M=32, ef_search=32 | 0.955 | 0.955 | 13254 | 25.0 | 235.2 | 784.1 |
| rebuilt | 2 | hnsw M=32, ef_search=64 | 0.989 | 0.989 | 8053 | 25.0 | 235.2 | 784.1 |
| rebuilt | 2 | hnsw M=32, ef_search=128 | 0.998 | 0.998 | 4446 | 25.0 | 235.2 | 784.1 |
| rebuilt | 2 | hnsw M=32, ef_search=256 | 1.000 | 1.000 | 2360 | 25.0 | 235.2 | 784.1 |
| rebuilt | 2 | hnsw M=32, ef_search=512 | 1.000 | 1.000 | 1212 | 25.0 | 235.2 | 784.1 |
| rebuilt | 2 | ivf_flat c=1, nprobe=1 | 0.397 | 0.397 | 47085 | 1.6 | 156.3 | 521.0 |
| rebuilt | 2 | ivf_flat c=1, nprobe=2 | 0.566 | 0.566 | 29498 | 1.6 | 156.3 | 521.0 |
| rebuilt | 2 | ivf_flat c=1, nprobe=4 | 0.732 | 0.732 | 18040 | 1.6 | 156.3 | 521.0 |
| rebuilt | 2 | ivf_flat c=1, nprobe=8 | 0.867 | 0.867 | 10708 | 1.6 | 156.3 | 521.0 |
| rebuilt | 2 | ivf_flat c=1, nprobe=16 | 0.951 | 0.951 | 5847 | 1.6 | 156.3 | 521.0 |
| rebuilt | 2 | ivf_flat c=1, nprobe=32 | 0.988 | 0.988 | 3257 | 1.6 | 156.3 | 521.0 |
| rebuilt | 2 | ivf_flat c=1, nprobe=64 | 0.998 | 0.998 | 1744 | 1.6 | 156.3 | 521.0 |
| rebuilt | 2 | ivf_flat c=1, nprobe=128 | 1.000 | 1.000 | 851 | 1.6 | 156.3 | 521.0 |
| rebuilt | 2 | ivf_flat c=4, nprobe=1 | 0.305 | 0.305 | 27945 | 12.3 | 157.1 | 523.8 |
| rebuilt | 2 | ivf_flat c=4, nprobe=2 | 0.450 | 0.450 | 22390 | 12.3 | 157.1 | 523.8 |
| rebuilt | 2 | ivf_flat c=4, nprobe=4 | 0.606 | 0.606 | 19567 | 12.3 | 157.1 | 523.8 |
| rebuilt | 2 | ivf_flat c=4, nprobe=8 | 0.749 | 0.749 | 15685 | 12.3 | 157.1 | 523.8 |
| rebuilt | 2 | ivf_flat c=4, nprobe=16 | 0.866 | 0.866 | 11692 | 12.3 | 157.1 | 523.8 |
| rebuilt | 2 | ivf_flat c=4, nprobe=32 | 0.944 | 0.944 | 7703 | 12.3 | 157.1 | 523.8 |
| rebuilt | 2 | ivf_flat c=4, nprobe=64 | 0.982 | 0.982 | 4573 | 12.3 | 157.1 | 523.8 |
| rebuilt | 2 | ivf_flat c=4, nprobe=128 | 0.996 | 0.996 | 2556 | 12.3 | 157.1 | 523.8 |
| rebuilt | 2 | ivf_pq c=4 m=32, nprobe=1 | 0.294 | 0.294 | 17907 | 14.4 | 13.3 | 44.2 |
| rebuilt | 2 | ivf_pq c=4 m=32, nprobe=2 | 0.423 | 0.423 | 17660 | 14.4 | 13.3 | 44.2 |
| rebuilt | 2 | ivf_pq c=4 m=32, nprobe=4 | 0.546 | 0.546 | 15835 | 14.4 | 13.3 | 44.2 |
| rebuilt | 2 | ivf_pq c=4 m=32, nprobe=8 | 0.642 | 0.642 | 13375 | 14.4 | 13.3 | 44.2 |
| rebuilt | 2 | ivf_pq c=4 m=32, nprobe=16 | 0.709 | 0.709 | 10236 | 14.4 | 13.3 | 44.2 |
| rebuilt | 2 | ivf_pq c=4 m=32, nprobe=32 | 0.742 | 0.742 | 6961 | 14.4 | 13.3 | 44.2 |
| rebuilt | 2 | ivf_pq c=4 m=32, nprobe=64 | 0.754 | 0.754 | 4247 | 14.4 | 13.3 | 44.2 |
| rebuilt | 2 | ivf_pq c=4 m=32, nprobe=128 | 0.758 | 0.758 | 2348 | 14.4 | 13.3 | 44.2 |
| rebuilt | 2 | ivf_pq c=4 m=32, nprobe=256 | 0.758 | 0.758 | 1272 | 14.4 | 13.3 | 44.2 |
| rebuilt | 2 | ivf_pq c=4 m=64, nprobe=1 | 0.302 | 0.302 | 13787 | 18.2 | 22.9 | 76.2 |
| rebuilt | 2 | ivf_pq c=4 m=64, nprobe=2 | 0.443 | 0.443 | 13488 | 18.2 | 22.9 | 76.2 |
| rebuilt | 2 | ivf_pq c=4 m=64, nprobe=4 | 0.589 | 0.589 | 11464 | 18.2 | 22.9 | 76.2 |
| rebuilt | 2 | ivf_pq c=4 m=64, nprobe=8 | 0.713 | 0.713 | 8970 | 18.2 | 22.9 | 76.2 |
| rebuilt | 2 | ivf_pq c=4 m=64, nprobe=16 | 0.808 | 0.808 | 6239 | 18.2 | 22.9 | 76.2 |
| rebuilt | 2 | ivf_pq c=4 m=64, nprobe=32 | 0.861 | 0.861 | 3804 | 18.2 | 22.9 | 76.2 |
| rebuilt | 2 | ivf_pq c=4 m=64, nprobe=64 | 0.884 | 0.884 | 2222 | 18.2 | 22.9 | 76.2 |
| rebuilt | 2 | ivf_pq c=4 m=64, nprobe=128 | 0.890 | 0.890 | 1199 | 18.2 | 22.9 | 76.2 |
| rebuilt | 2 | ivf_pq c=4 m=64, nprobe=256 | 0.891 | 0.891 | 623 | 18.2 | 22.9 | 76.2 |
| rebuilt | 3 | exact (flat) | 1.000 | 1.000 | 220 | - | - | - |
| rebuilt | 3 | hnsw M=16, ef_search=32 | 0.934 | 0.934 | 11890 | 33.5 | 196.9 | 656.3 |
| rebuilt | 3 | hnsw M=16, ef_search=64 | 0.980 | 0.980 | 9139 | 33.5 | 196.9 | 656.3 |
| rebuilt | 3 | hnsw M=16, ef_search=128 | 0.996 | 0.996 | 5092 | 33.5 | 196.9 | 656.3 |
| rebuilt | 3 | hnsw M=16, ef_search=256 | 0.999 | 0.999 | 2573 | 33.5 | 196.9 | 656.3 |
| rebuilt | 3 | hnsw M=16, ef_search=512 | 1.000 | 1.000 | 1263 | 33.5 | 196.9 | 656.3 |
| rebuilt | 3 | hnsw M=32, ef_search=32 | 0.955 | 0.955 | 12173 | 30.4 | 235.2 | 784.1 |
| rebuilt | 3 | hnsw M=32, ef_search=64 | 0.989 | 0.989 | 7992 | 30.4 | 235.2 | 784.1 |
| rebuilt | 3 | hnsw M=32, ef_search=128 | 0.998 | 0.998 | 4385 | 30.4 | 235.2 | 784.1 |
| rebuilt | 3 | hnsw M=32, ef_search=256 | 1.000 | 1.000 | 2361 | 30.4 | 235.2 | 784.1 |
| rebuilt | 3 | hnsw M=32, ef_search=512 | 1.000 | 1.000 | 1207 | 30.4 | 235.2 | 784.1 |
| rebuilt | 3 | ivf_flat c=1, nprobe=1 | 0.396 | 0.396 | 47154 | 1.5 | 156.3 | 521.0 |
| rebuilt | 3 | ivf_flat c=1, nprobe=2 | 0.567 | 0.567 | 29579 | 1.5 | 156.3 | 521.0 |
| rebuilt | 3 | ivf_flat c=1, nprobe=4 | 0.732 | 0.732 | 17521 | 1.5 | 156.3 | 521.0 |
| rebuilt | 3 | ivf_flat c=1, nprobe=8 | 0.867 | 0.867 | 10752 | 1.5 | 156.3 | 521.0 |
| rebuilt | 3 | ivf_flat c=1, nprobe=16 | 0.951 | 0.951 | 5869 | 1.5 | 156.3 | 521.0 |
| rebuilt | 3 | ivf_flat c=1, nprobe=32 | 0.988 | 0.988 | 3312 | 1.5 | 156.3 | 521.0 |
| rebuilt | 3 | ivf_flat c=1, nprobe=64 | 0.998 | 0.998 | 1774 | 1.5 | 156.3 | 521.0 |
| rebuilt | 3 | ivf_flat c=1, nprobe=128 | 1.000 | 1.000 | 865 | 1.5 | 156.3 | 521.0 |
| rebuilt | 3 | ivf_flat c=4, nprobe=1 | 0.306 | 0.306 | 28211 | 12.1 | 157.1 | 523.8 |
| rebuilt | 3 | ivf_flat c=4, nprobe=2 | 0.450 | 0.450 | 23013 | 12.1 | 157.1 | 523.8 |
| rebuilt | 3 | ivf_flat c=4, nprobe=4 | 0.606 | 0.606 | 18987 | 12.1 | 157.1 | 523.8 |
| rebuilt | 3 | ivf_flat c=4, nprobe=8 | 0.749 | 0.749 | 16111 | 12.1 | 157.1 | 523.8 |
| rebuilt | 3 | ivf_flat c=4, nprobe=16 | 0.866 | 0.866 | 11945 | 12.1 | 157.1 | 523.8 |
| rebuilt | 3 | ivf_flat c=4, nprobe=32 | 0.945 | 0.945 | 7628 | 12.1 | 157.1 | 523.8 |
| rebuilt | 3 | ivf_flat c=4, nprobe=64 | 0.982 | 0.982 | 4676 | 12.1 | 157.1 | 523.8 |
| rebuilt | 3 | ivf_flat c=4, nprobe=128 | 0.996 | 0.996 | 2615 | 12.1 | 157.1 | 523.8 |
| rebuilt | 3 | ivf_pq c=4 m=32, nprobe=1 | 0.294 | 0.294 | 17286 | 14.6 | 13.3 | 44.2 |
| rebuilt | 3 | ivf_pq c=4 m=32, nprobe=2 | 0.422 | 0.422 | 17346 | 14.6 | 13.3 | 44.2 |
| rebuilt | 3 | ivf_pq c=4 m=32, nprobe=4 | 0.546 | 0.546 | 15670 | 14.6 | 13.3 | 44.2 |
| rebuilt | 3 | ivf_pq c=4 m=32, nprobe=8 | 0.642 | 0.642 | 12992 | 14.6 | 13.3 | 44.2 |
| rebuilt | 3 | ivf_pq c=4 m=32, nprobe=16 | 0.708 | 0.708 | 10040 | 14.6 | 13.3 | 44.2 |
| rebuilt | 3 | ivf_pq c=4 m=32, nprobe=32 | 0.742 | 0.742 | 6861 | 14.6 | 13.3 | 44.2 |
| rebuilt | 3 | ivf_pq c=4 m=32, nprobe=64 | 0.755 | 0.755 | 4122 | 14.6 | 13.3 | 44.2 |
| rebuilt | 3 | ivf_pq c=4 m=32, nprobe=128 | 0.758 | 0.758 | 2338 | 14.6 | 13.3 | 44.2 |
| rebuilt | 3 | ivf_pq c=4 m=32, nprobe=256 | 0.759 | 0.759 | 1265 | 14.6 | 13.3 | 44.2 |
| rebuilt | 3 | ivf_pq c=4 m=64, nprobe=1 | 0.303 | 0.303 | 14389 | 17.4 | 22.9 | 76.2 |
| rebuilt | 3 | ivf_pq c=4 m=64, nprobe=2 | 0.442 | 0.442 | 13586 | 17.4 | 22.9 | 76.2 |
| rebuilt | 3 | ivf_pq c=4 m=64, nprobe=4 | 0.588 | 0.588 | 11603 | 17.4 | 22.9 | 76.2 |
| rebuilt | 3 | ivf_pq c=4 m=64, nprobe=8 | 0.714 | 0.714 | 9051 | 17.4 | 22.9 | 76.2 |
| rebuilt | 3 | ivf_pq c=4 m=64, nprobe=16 | 0.807 | 0.807 | 6302 | 17.4 | 22.9 | 76.2 |
| rebuilt | 3 | ivf_pq c=4 m=64, nprobe=32 | 0.861 | 0.861 | 3891 | 17.4 | 22.9 | 76.2 |
| rebuilt | 3 | ivf_pq c=4 m=64, nprobe=64 | 0.883 | 0.883 | 2230 | 17.4 | 22.9 | 76.2 |
| rebuilt | 3 | ivf_pq c=4 m=64, nprobe=128 | 0.890 | 0.890 | 1191 | 17.4 | 22.9 | 76.2 |
| rebuilt | 3 | ivf_pq c=4 m=64, nprobe=256 | 0.891 | 0.891 | 619 | 17.4 | 22.9 | 76.2 |
| rebuilt | 5 | exact (flat) | 1.000 | 1.000 | 195 | - | - | - |
| rebuilt | 5 | hnsw M=16, ef_search=32 | 0.934 | 0.934 | 10799 | 35.5 | 196.9 | 656.3 |
| rebuilt | 5 | hnsw M=16, ef_search=64 | 0.980 | 0.980 | 8980 | 35.5 | 196.9 | 656.3 |
| rebuilt | 5 | hnsw M=16, ef_search=128 | 0.996 | 0.996 | 4951 | 35.5 | 196.9 | 656.3 |
| rebuilt | 5 | hnsw M=16, ef_search=256 | 0.999 | 0.999 | 2665 | 35.5 | 196.9 | 656.3 |
| rebuilt | 5 | hnsw M=16, ef_search=512 | 1.000 | 1.000 | 1292 | 35.5 | 196.9 | 656.3 |
| rebuilt | 5 | hnsw M=32, ef_search=32 | 0.955 | 0.955 | 9589 | 28.8 | 235.2 | 784.1 |
| rebuilt | 5 | hnsw M=32, ef_search=64 | 0.989 | 0.989 | 7868 | 28.8 | 235.2 | 784.1 |
| rebuilt | 5 | hnsw M=32, ef_search=128 | 0.998 | 0.998 | 4244 | 28.8 | 235.2 | 784.1 |
| rebuilt | 5 | hnsw M=32, ef_search=256 | 1.000 | 1.000 | 2215 | 28.8 | 235.2 | 784.1 |
| rebuilt | 5 | hnsw M=32, ef_search=512 | 1.000 | 1.000 | 1060 | 28.8 | 235.2 | 784.1 |
| rebuilt | 5 | ivf_flat c=1, nprobe=1 | 0.397 | 0.397 | 40329 | 1.9 | 156.3 | 521.0 |
| rebuilt | 5 | ivf_flat c=1, nprobe=2 | 0.566 | 0.566 | 26305 | 1.9 | 156.3 | 521.0 |
| rebuilt | 5 | ivf_flat c=1, nprobe=4 | 0.732 | 0.732 | 15437 | 1.9 | 156.3 | 521.0 |
| rebuilt | 5 | ivf_flat c=1, nprobe=8 | 0.867 | 0.867 | 8479 | 1.9 | 156.3 | 521.0 |
| rebuilt | 5 | ivf_flat c=1, nprobe=16 | 0.951 | 0.951 | 5099 | 1.9 | 156.3 | 521.0 |
| rebuilt | 5 | ivf_flat c=1, nprobe=32 | 0.988 | 0.988 | 2818 | 1.9 | 156.3 | 521.0 |
| rebuilt | 5 | ivf_flat c=1, nprobe=64 | 0.998 | 0.998 | 1511 | 1.9 | 156.3 | 521.0 |
| rebuilt | 5 | ivf_flat c=1, nprobe=128 | 1.000 | 1.000 | 739 | 1.9 | 156.3 | 521.0 |
| rebuilt | 5 | ivf_flat c=4, nprobe=1 | 0.306 | 0.306 | 26612 | 12.9 | 157.1 | 523.8 |
| rebuilt | 5 | ivf_flat c=4, nprobe=2 | 0.448 | 0.448 | 22066 | 12.9 | 157.1 | 523.8 |
| rebuilt | 5 | ivf_flat c=4, nprobe=4 | 0.605 | 0.605 | 18871 | 12.9 | 157.1 | 523.8 |
| rebuilt | 5 | ivf_flat c=4, nprobe=8 | 0.749 | 0.749 | 15388 | 12.9 | 157.1 | 523.8 |
| rebuilt | 5 | ivf_flat c=4, nprobe=16 | 0.866 | 0.866 | 11397 | 12.9 | 157.1 | 523.8 |
| rebuilt | 5 | ivf_flat c=4, nprobe=32 | 0.945 | 0.945 | 7455 | 12.9 | 157.1 | 523.8 |
| rebuilt | 5 | ivf_flat c=4, nprobe=64 | 0.982 | 0.982 | 4436 | 12.9 | 157.1 | 523.8 |
| rebuilt | 5 | ivf_flat c=4, nprobe=128 | 0.996 | 0.996 | 2350 | 12.9 | 157.1 | 523.8 |
| rebuilt | 5 | ivf_pq c=4 m=32, nprobe=1 | 0.295 | 0.295 | 14536 | 15.1 | 13.3 | 44.2 |
| rebuilt | 5 | ivf_pq c=4 m=32, nprobe=2 | 0.420 | 0.420 | 15261 | 15.1 | 13.3 | 44.2 |
| rebuilt | 5 | ivf_pq c=4 m=32, nprobe=4 | 0.544 | 0.544 | 14908 | 15.1 | 13.3 | 44.2 |
| rebuilt | 5 | ivf_pq c=4 m=32, nprobe=8 | 0.641 | 0.641 | 12645 | 15.1 | 13.3 | 44.2 |
| rebuilt | 5 | ivf_pq c=4 m=32, nprobe=16 | 0.707 | 0.707 | 9362 | 15.1 | 13.3 | 44.2 |
| rebuilt | 5 | ivf_pq c=4 m=32, nprobe=32 | 0.742 | 0.742 | 6143 | 15.1 | 13.3 | 44.2 |
| rebuilt | 5 | ivf_pq c=4 m=32, nprobe=64 | 0.754 | 0.754 | 3892 | 15.1 | 13.3 | 44.2 |
| rebuilt | 5 | ivf_pq c=4 m=32, nprobe=128 | 0.758 | 0.758 | 2218 | 15.1 | 13.3 | 44.2 |
| rebuilt | 5 | ivf_pq c=4 m=32, nprobe=256 | 0.758 | 0.758 | 1203 | 15.1 | 13.3 | 44.2 |
| rebuilt | 5 | ivf_pq c=4 m=64, nprobe=1 | 0.304 | 0.304 | 13969 | 18.1 | 22.9 | 76.2 |
| rebuilt | 5 | ivf_pq c=4 m=64, nprobe=2 | 0.441 | 0.441 | 13393 | 18.1 | 22.9 | 76.2 |
| rebuilt | 5 | ivf_pq c=4 m=64, nprobe=4 | 0.588 | 0.588 | 11473 | 18.1 | 22.9 | 76.2 |
| rebuilt | 5 | ivf_pq c=4 m=64, nprobe=8 | 0.716 | 0.716 | 8976 | 18.1 | 22.9 | 76.2 |
| rebuilt | 5 | ivf_pq c=4 m=64, nprobe=16 | 0.809 | 0.809 | 6064 | 18.1 | 22.9 | 76.2 |
| rebuilt | 5 | ivf_pq c=4 m=64, nprobe=32 | 0.862 | 0.862 | 3673 | 18.1 | 22.9 | 76.2 |
| rebuilt | 5 | ivf_pq c=4 m=64, nprobe=64 | 0.884 | 0.884 | 2137 | 18.1 | 22.9 | 76.2 |
| rebuilt | 5 | ivf_pq c=4 m=64, nprobe=128 | 0.891 | 0.891 | 1156 | 18.1 | 22.9 | 76.2 |
| rebuilt | 5 | ivf_pq c=4 m=64, nprobe=256 | 0.892 | 0.892 | 611 | 18.1 | 22.9 | 76.2 |
