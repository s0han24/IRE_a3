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
| stale | 5 | exact (flat) | 1.000 | 0.830 | 336 | - | - | - |
| stale | 5 | hnsw M=16, ef_search=32 | 0.927 | 0.801 | 18051 | 23.1 (reused) | 196.9 | 656.3 |
| stale | 5 | hnsw M=16, ef_search=64 | 0.978 | 0.823 | 10165 | 23.1 (reused) | 196.9 | 656.3 |
| stale | 5 | hnsw M=16, ef_search=128 | 0.995 | 0.828 | 5441 | 23.1 (reused) | 196.9 | 656.3 |
| stale | 5 | hnsw M=16, ef_search=256 | 0.999 | 0.830 | 2807 | 23.1 (reused) | 196.9 | 656.3 |
| stale | 5 | hnsw M=16, ef_search=512 | 1.000 | 0.830 | 1364 | 23.1 (reused) | 196.9 | 656.3 |
| stale | 5 | hnsw M=32, ef_search=32 | 0.952 | 0.812 | 14462 | 19.9 (reused) | 235.2 | 784.1 |
| stale | 5 | hnsw M=32, ef_search=64 | 0.988 | 0.826 | 8218 | 19.9 (reused) | 235.2 | 784.1 |
| stale | 5 | hnsw M=32, ef_search=128 | 0.998 | 0.829 | 4503 | 19.9 (reused) | 235.2 | 784.1 |
| stale | 5 | hnsw M=32, ef_search=256 | 1.000 | 0.830 | 2374 | 19.9 (reused) | 235.2 | 784.1 |
| stale | 5 | hnsw M=32, ef_search=512 | 1.000 | 0.830 | 1194 | 19.9 (reused) | 235.2 | 784.1 |
| stale | 5 | ivf_flat c=1, nprobe=1 | 0.386 | 0.365 | 55671 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 5 | ivf_flat c=1, nprobe=2 | 0.553 | 0.513 | 38615 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 5 | ivf_flat c=1, nprobe=4 | 0.717 | 0.648 | 24646 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 5 | ivf_flat c=1, nprobe=8 | 0.854 | 0.749 | 14119 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 5 | ivf_flat c=1, nprobe=16 | 0.943 | 0.803 | 7547 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 5 | ivf_flat c=1, nprobe=32 | 0.985 | 0.824 | 3800 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 5 | ivf_flat c=1, nprobe=64 | 0.998 | 0.829 | 1910 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 5 | ivf_flat c=1, nprobe=128 | 1.000 | 0.830 | 980 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 5 | ivf_flat c=4, nprobe=1 | 0.290 | 0.279 | 25719 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 5 | ivf_flat c=4, nprobe=2 | 0.432 | 0.410 | 23651 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 5 | ivf_flat c=4, nprobe=4 | 0.586 | 0.546 | 21021 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 5 | ivf_flat c=4, nprobe=8 | 0.731 | 0.663 | 17268 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 5 | ivf_flat c=4, nprobe=16 | 0.853 | 0.751 | 11698 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 5 | ivf_flat c=4, nprobe=32 | 0.936 | 0.799 | 8452 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 5 | ivf_flat c=4, nprobe=64 | 0.978 | 0.820 | 5100 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 5 | ivf_flat c=4, nprobe=128 | 0.996 | 0.828 | 2846 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 5 | ivf_pq c=4 m=32, nprobe=1 | 0.280 | 0.272 | 19140 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 5 | ivf_pq c=4 m=32, nprobe=2 | 0.406 | 0.391 | 17850 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 5 | ivf_pq c=4 m=32, nprobe=4 | 0.529 | 0.505 | 16260 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 5 | ivf_pq c=4 m=32, nprobe=8 | 0.627 | 0.593 | 13712 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 5 | ivf_pq c=4 m=32, nprobe=16 | 0.696 | 0.656 | 10638 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 5 | ivf_pq c=4 m=32, nprobe=32 | 0.732 | 0.689 | 7325 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 5 | ivf_pq c=4 m=32, nprobe=64 | 0.746 | 0.702 | 4508 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 5 | ivf_pq c=4 m=32, nprobe=128 | 0.751 | 0.706 | 2514 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 5 | ivf_pq c=4 m=32, nprobe=256 | 0.752 | 0.707 | 1351 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 5 | ivf_pq c=4 m=64, nprobe=1 | 0.288 | 0.278 | 14553 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 5 | ivf_pq c=4 m=64, nprobe=2 | 0.425 | 0.406 | 13536 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 5 | ivf_pq c=4 m=64, nprobe=4 | 0.570 | 0.537 | 11817 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 5 | ivf_pq c=4 m=64, nprobe=8 | 0.699 | 0.647 | 9296 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 5 | ivf_pq c=4 m=64, nprobe=16 | 0.798 | 0.730 | 6568 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 5 | ivf_pq c=4 m=64, nprobe=32 | 0.855 | 0.774 | 4112 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 5 | ivf_pq c=4 m=64, nprobe=64 | 0.880 | 0.792 | 2357 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 5 | ivf_pq c=4 m=64, nprobe=128 | 0.889 | 0.799 | 1273 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 5 | ivf_pq c=4 m=64, nprobe=256 | 0.891 | 0.800 | 671 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 10 | exact (flat) | 1.000 | 0.671 | 251 | - | - | - |
| stale | 10 | hnsw M=16, ef_search=32 | 0.916 | 0.654 | 16108 | 23.1 (reused) | 196.9 | 656.3 |
| stale | 10 | hnsw M=16, ef_search=64 | 0.974 | 0.667 | 9467 | 23.1 (reused) | 196.9 | 656.3 |
| stale | 10 | hnsw M=16, ef_search=128 | 0.994 | 0.671 | 5121 | 23.1 (reused) | 196.9 | 656.3 |
| stale | 10 | hnsw M=16, ef_search=256 | 0.999 | 0.671 | 1995 | 23.1 (reused) | 196.9 | 656.3 |
| stale | 10 | hnsw M=16, ef_search=512 | 1.000 | 0.671 | 1251 | 23.1 (reused) | 196.9 | 656.3 |
| stale | 10 | hnsw M=32, ef_search=32 | 0.946 | 0.661 | 13646 | 19.9 (reused) | 235.2 | 784.1 |
| stale | 10 | hnsw M=32, ef_search=64 | 0.986 | 0.670 | 7582 | 19.9 (reused) | 235.2 | 784.1 |
| stale | 10 | hnsw M=32, ef_search=128 | 0.998 | 0.671 | 4209 | 19.9 (reused) | 235.2 | 784.1 |
| stale | 10 | hnsw M=32, ef_search=256 | 1.000 | 0.671 | 2278 | 19.9 (reused) | 235.2 | 784.1 |
| stale | 10 | hnsw M=32, ef_search=512 | 1.000 | 0.671 | 1155 | 19.9 (reused) | 235.2 | 784.1 |
| stale | 10 | ivf_flat c=1, nprobe=1 | 0.367 | 0.317 | 57102 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 10 | ivf_flat c=1, nprobe=2 | 0.530 | 0.436 | 38410 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 10 | ivf_flat c=1, nprobe=4 | 0.696 | 0.542 | 23058 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 10 | ivf_flat c=1, nprobe=8 | 0.836 | 0.612 | 13459 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 10 | ivf_flat c=1, nprobe=16 | 0.934 | 0.652 | 7258 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 10 | ivf_flat c=1, nprobe=32 | 0.981 | 0.666 | 3692 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 10 | ivf_flat c=1, nprobe=64 | 0.997 | 0.671 | 1929 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 10 | ivf_flat c=1, nprobe=128 | 1.000 | 0.671 | 956 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 10 | ivf_flat c=4, nprobe=1 | 0.272 | 0.243 | 24706 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 10 | ivf_flat c=4, nprobe=2 | 0.409 | 0.353 | 22098 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 10 | ivf_flat c=4, nprobe=4 | 0.558 | 0.461 | 20289 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 10 | ivf_flat c=4, nprobe=8 | 0.705 | 0.549 | 16719 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 10 | ivf_flat c=4, nprobe=16 | 0.832 | 0.614 | 12184 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 10 | ivf_flat c=4, nprobe=32 | 0.923 | 0.649 | 8338 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 10 | ivf_flat c=4, nprobe=64 | 0.973 | 0.665 | 5102 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 10 | ivf_flat c=4, nprobe=128 | 0.994 | 0.670 | 2802 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 10 | ivf_pq c=4 m=32, nprobe=1 | 0.262 | 0.237 | 17995 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 10 | ivf_pq c=4 m=32, nprobe=2 | 0.384 | 0.338 | 16824 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 10 | ivf_pq c=4 m=32, nprobe=4 | 0.502 | 0.431 | 15383 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 10 | ivf_pq c=4 m=32, nprobe=8 | 0.603 | 0.505 | 13114 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 10 | ivf_pq c=4 m=32, nprobe=16 | 0.675 | 0.555 | 10200 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 10 | ivf_pq c=4 m=32, nprobe=32 | 0.715 | 0.582 | 6958 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 10 | ivf_pq c=4 m=32, nprobe=64 | 0.732 | 0.593 | 4320 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 10 | ivf_pq c=4 m=32, nprobe=128 | 0.737 | 0.596 | 2426 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 10 | ivf_pq c=4 m=32, nprobe=256 | 0.738 | 0.597 | 1310 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 10 | ivf_pq c=4 m=64, nprobe=1 | 0.270 | 0.242 | 13985 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 10 | ivf_pq c=4 m=64, nprobe=2 | 0.403 | 0.349 | 12968 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 10 | ivf_pq c=4 m=64, nprobe=4 | 0.544 | 0.455 | 11326 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 10 | ivf_pq c=4 m=64, nprobe=8 | 0.675 | 0.540 | 9012 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 10 | ivf_pq c=4 m=64, nprobe=16 | 0.778 | 0.601 | 6381 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 10 | ivf_pq c=4 m=64, nprobe=32 | 0.844 | 0.636 | 3982 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 10 | ivf_pq c=4 m=64, nprobe=64 | 0.874 | 0.650 | 2283 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 10 | ivf_pq c=4 m=64, nprobe=128 | 0.886 | 0.655 | 1233 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 10 | ivf_pq c=4 m=64, nprobe=256 | 0.888 | 0.656 | 645 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 15 | exact (flat) | 1.000 | 0.519 | 226 | - | - | - |
| stale | 15 | hnsw M=16, ef_search=32 | 0.900 | 0.510 | 14957 | 23.1 (reused) | 196.9 | 656.3 |
| stale | 15 | hnsw M=16, ef_search=64 | 0.967 | 0.518 | 8921 | 23.1 (reused) | 196.9 | 656.3 |
| stale | 15 | hnsw M=16, ef_search=128 | 0.992 | 0.519 | 4913 | 23.1 (reused) | 196.9 | 656.3 |
| stale | 15 | hnsw M=16, ef_search=256 | 0.999 | 0.519 | 2624 | 23.1 (reused) | 196.9 | 656.3 |
| stale | 15 | hnsw M=16, ef_search=512 | 1.000 | 0.519 | 1301 | 23.1 (reused) | 196.9 | 656.3 |
| stale | 15 | hnsw M=32, ef_search=32 | 0.934 | 0.516 | 13691 | 19.9 (reused) | 235.2 | 784.1 |
| stale | 15 | hnsw M=32, ef_search=64 | 0.982 | 0.519 | 7673 | 19.9 (reused) | 235.2 | 784.1 |
| stale | 15 | hnsw M=32, ef_search=128 | 0.997 | 0.519 | 4135 | 19.9 (reused) | 235.2 | 784.1 |
| stale | 15 | hnsw M=32, ef_search=256 | 1.000 | 0.519 | 2218 | 19.9 (reused) | 235.2 | 784.1 |
| stale | 15 | hnsw M=32, ef_search=512 | 1.000 | 0.519 | 1121 | 19.9 (reused) | 235.2 | 784.1 |
| stale | 15 | ivf_flat c=1, nprobe=1 | 0.345 | 0.261 | 55719 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 15 | ivf_flat c=1, nprobe=2 | 0.505 | 0.353 | 37439 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 15 | ivf_flat c=1, nprobe=4 | 0.671 | 0.430 | 23167 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 15 | ivf_flat c=1, nprobe=8 | 0.817 | 0.481 | 13332 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 15 | ivf_flat c=1, nprobe=16 | 0.922 | 0.505 | 7139 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 15 | ivf_flat c=1, nprobe=32 | 0.977 | 0.516 | 3647 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 15 | ivf_flat c=1, nprobe=64 | 0.996 | 0.519 | 1878 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 15 | ivf_flat c=1, nprobe=128 | 1.000 | 0.519 | 934 | 1.6 (reused) | 156.3 | 521.0 |
| stale | 15 | ivf_flat c=4, nprobe=1 | 0.254 | 0.203 | 24157 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 15 | ivf_flat c=4, nprobe=2 | 0.381 | 0.288 | 22121 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 15 | ivf_flat c=4, nprobe=4 | 0.528 | 0.370 | 19839 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 15 | ivf_flat c=4, nprobe=8 | 0.673 | 0.434 | 16368 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 15 | ivf_flat c=4, nprobe=16 | 0.805 | 0.480 | 12394 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 15 | ivf_flat c=4, nprobe=32 | 0.905 | 0.506 | 8308 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 15 | ivf_flat c=4, nprobe=64 | 0.965 | 0.515 | 4941 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 15 | ivf_flat c=4, nprobe=128 | 0.991 | 0.518 | 2641 | 11.5 (reused) | 157.1 | 523.8 |
| stale | 15 | ivf_pq c=4 m=32, nprobe=1 | 0.244 | 0.198 | 17222 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 15 | ivf_pq c=4 m=32, nprobe=2 | 0.357 | 0.277 | 16220 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 15 | ivf_pq c=4 m=32, nprobe=4 | 0.473 | 0.349 | 14765 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 15 | ivf_pq c=4 m=32, nprobe=8 | 0.572 | 0.404 | 12086 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 15 | ivf_pq c=4 m=32, nprobe=16 | 0.645 | 0.440 | 9829 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 15 | ivf_pq c=4 m=32, nprobe=32 | 0.689 | 0.461 | 6939 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 15 | ivf_pq c=4 m=32, nprobe=64 | 0.708 | 0.469 | 4246 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 15 | ivf_pq c=4 m=32, nprobe=128 | 0.716 | 0.471 | 2393 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 15 | ivf_pq c=4 m=32, nprobe=256 | 0.718 | 0.472 | 1300 | 13.7 (reused) | 13.3 | 44.2 |
| stale | 15 | ivf_pq c=4 m=64, nprobe=1 | 0.252 | 0.201 | 13364 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 15 | ivf_pq c=4 m=64, nprobe=2 | 0.376 | 0.285 | 12534 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 15 | ivf_pq c=4 m=64, nprobe=4 | 0.515 | 0.365 | 10734 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 15 | ivf_pq c=4 m=64, nprobe=8 | 0.647 | 0.426 | 8763 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 15 | ivf_pq c=4 m=64, nprobe=16 | 0.756 | 0.470 | 5980 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 15 | ivf_pq c=4 m=64, nprobe=32 | 0.830 | 0.497 | 3873 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 15 | ivf_pq c=4 m=64, nprobe=64 | 0.868 | 0.506 | 2232 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 15 | ivf_pq c=4 m=64, nprobe=128 | 0.881 | 0.508 | 1210 | 15.6 (reused) | 22.9 | 76.2 |
| stale | 15 | ivf_pq c=4 m=64, nprobe=256 | 0.885 | 0.509 | 630 | 15.6 (reused) | 22.9 | 76.2 |
| rebuilt | 5 | exact (flat) | 1.000 | 1.000 | 271 | - | - | - |
| rebuilt | 5 | hnsw M=16, ef_search=32 | 0.933 | 0.933 | 17085 | 19.8 | 196.9 | 656.3 |
| rebuilt | 5 | hnsw M=16, ef_search=64 | 0.980 | 0.980 | 10174 | 19.8 | 196.9 | 656.3 |
| rebuilt | 5 | hnsw M=16, ef_search=128 | 0.996 | 0.996 | 5532 | 19.8 | 196.9 | 656.3 |
| rebuilt | 5 | hnsw M=16, ef_search=256 | 1.000 | 1.000 | 2872 | 19.8 | 196.9 | 656.3 |
| rebuilt | 5 | hnsw M=16, ef_search=512 | 1.000 | 1.000 | 1396 | 19.8 | 196.9 | 656.3 |
| rebuilt | 5 | hnsw M=32, ef_search=32 | 0.955 | 0.955 | 14111 | 21.4 | 235.2 | 784.1 |
| rebuilt | 5 | hnsw M=32, ef_search=64 | 0.989 | 0.989 | 8302 | 21.4 | 235.2 | 784.1 |
| rebuilt | 5 | hnsw M=32, ef_search=128 | 0.998 | 0.998 | 4571 | 21.4 | 235.2 | 784.1 |
| rebuilt | 5 | hnsw M=32, ef_search=256 | 1.000 | 1.000 | 2431 | 21.4 | 235.2 | 784.1 |
| rebuilt | 5 | hnsw M=32, ef_search=512 | 1.000 | 1.000 | 1222 | 21.4 | 235.2 | 784.1 |
| rebuilt | 5 | ivf_flat c=1, nprobe=1 | 0.397 | 0.397 | 54345 | 1.5 | 156.3 | 521.0 |
| rebuilt | 5 | ivf_flat c=1, nprobe=2 | 0.566 | 0.566 | 37691 | 1.5 | 156.3 | 521.0 |
| rebuilt | 5 | ivf_flat c=1, nprobe=4 | 0.732 | 0.732 | 23307 | 1.5 | 156.3 | 521.0 |
| rebuilt | 5 | ivf_flat c=1, nprobe=8 | 0.867 | 0.867 | 13380 | 1.5 | 156.3 | 521.0 |
| rebuilt | 5 | ivf_flat c=1, nprobe=16 | 0.951 | 0.951 | 7215 | 1.5 | 156.3 | 521.0 |
| rebuilt | 5 | ivf_flat c=1, nprobe=32 | 0.989 | 0.989 | 3725 | 1.5 | 156.3 | 521.0 |
| rebuilt | 5 | ivf_flat c=1, nprobe=64 | 0.998 | 0.998 | 1933 | 1.5 | 156.3 | 521.0 |
| rebuilt | 5 | ivf_flat c=1, nprobe=128 | 1.000 | 1.000 | 981 | 1.5 | 156.3 | 521.0 |
| rebuilt | 5 | ivf_flat c=4, nprobe=1 | 0.307 | 0.307 | 33919 | 11.1 | 157.1 | 523.8 |
| rebuilt | 5 | ivf_flat c=4, nprobe=2 | 0.449 | 0.449 | 28746 | 11.1 | 157.1 | 523.8 |
| rebuilt | 5 | ivf_flat c=4, nprobe=4 | 0.606 | 0.606 | 24741 | 11.1 | 157.1 | 523.8 |
| rebuilt | 5 | ivf_flat c=4, nprobe=8 | 0.749 | 0.749 | 19672 | 11.1 | 157.1 | 523.8 |
| rebuilt | 5 | ivf_flat c=4, nprobe=16 | 0.866 | 0.866 | 13976 | 11.1 | 157.1 | 523.8 |
| rebuilt | 5 | ivf_flat c=4, nprobe=32 | 0.945 | 0.945 | 9023 | 11.1 | 157.1 | 523.8 |
| rebuilt | 5 | ivf_flat c=4, nprobe=64 | 0.982 | 0.982 | 5248 | 11.1 | 157.1 | 523.8 |
| rebuilt | 5 | ivf_flat c=4, nprobe=128 | 0.996 | 0.996 | 2827 | 11.1 | 157.1 | 523.8 |
| rebuilt | 5 | ivf_pq c=4 m=32, nprobe=1 | 0.296 | 0.296 | 18528 | 14.1 | 13.3 | 44.2 |
| rebuilt | 5 | ivf_pq c=4 m=32, nprobe=2 | 0.421 | 0.421 | 18385 | 14.1 | 13.3 | 44.2 |
| rebuilt | 5 | ivf_pq c=4 m=32, nprobe=4 | 0.545 | 0.545 | 16672 | 14.1 | 13.3 | 44.2 |
| rebuilt | 5 | ivf_pq c=4 m=32, nprobe=8 | 0.642 | 0.642 | 14024 | 14.1 | 13.3 | 44.2 |
| rebuilt | 5 | ivf_pq c=4 m=32, nprobe=16 | 0.706 | 0.706 | 10519 | 14.1 | 13.3 | 44.2 |
| rebuilt | 5 | ivf_pq c=4 m=32, nprobe=32 | 0.740 | 0.740 | 7257 | 14.1 | 13.3 | 44.2 |
| rebuilt | 5 | ivf_pq c=4 m=32, nprobe=64 | 0.753 | 0.753 | 4424 | 14.1 | 13.3 | 44.2 |
| rebuilt | 5 | ivf_pq c=4 m=32, nprobe=128 | 0.757 | 0.757 | 2446 | 14.1 | 13.3 | 44.2 |
| rebuilt | 5 | ivf_pq c=4 m=32, nprobe=256 | 0.757 | 0.757 | 1315 | 14.1 | 13.3 | 44.2 |
| rebuilt | 5 | ivf_pq c=4 m=64, nprobe=1 | 0.304 | 0.304 | 16018 | 16.0 | 22.9 | 76.2 |
| rebuilt | 5 | ivf_pq c=4 m=64, nprobe=2 | 0.442 | 0.442 | 15004 | 16.0 | 22.9 | 76.2 |
| rebuilt | 5 | ivf_pq c=4 m=64, nprobe=4 | 0.589 | 0.589 | 12707 | 16.0 | 22.9 | 76.2 |
| rebuilt | 5 | ivf_pq c=4 m=64, nprobe=8 | 0.714 | 0.714 | 9804 | 16.0 | 22.9 | 76.2 |
| rebuilt | 5 | ivf_pq c=4 m=64, nprobe=16 | 0.807 | 0.807 | 6696 | 16.0 | 22.9 | 76.2 |
| rebuilt | 5 | ivf_pq c=4 m=64, nprobe=32 | 0.861 | 0.861 | 4136 | 16.0 | 22.9 | 76.2 |
| rebuilt | 5 | ivf_pq c=4 m=64, nprobe=64 | 0.883 | 0.883 | 2332 | 16.0 | 22.9 | 76.2 |
| rebuilt | 5 | ivf_pq c=4 m=64, nprobe=128 | 0.890 | 0.890 | 1258 | 16.0 | 22.9 | 76.2 |
| rebuilt | 5 | ivf_pq c=4 m=64, nprobe=256 | 0.891 | 0.891 | 647 | 16.0 | 22.9 | 76.2 |
| rebuilt | 10 | exact (flat) | 1.000 | 1.000 | 250 | - | - | - |
| rebuilt | 10 | hnsw M=16, ef_search=32 | 0.933 | 0.933 | 15713 | 21.6 | 196.9 | 656.3 |
| rebuilt | 10 | hnsw M=16, ef_search=64 | 0.980 | 0.980 | 9984 | 21.6 | 196.9 | 656.3 |
| rebuilt | 10 | hnsw M=16, ef_search=128 | 0.996 | 0.996 | 5455 | 21.6 | 196.9 | 656.3 |
| rebuilt | 10 | hnsw M=16, ef_search=256 | 1.000 | 1.000 | 2852 | 21.6 | 196.9 | 656.3 |
| rebuilt | 10 | hnsw M=16, ef_search=512 | 1.000 | 1.000 | 1389 | 21.6 | 196.9 | 656.3 |
| rebuilt | 10 | hnsw M=32, ef_search=32 | 0.955 | 0.955 | 13565 | 22.7 | 235.2 | 784.1 |
| rebuilt | 10 | hnsw M=32, ef_search=64 | 0.989 | 0.989 | 8068 | 22.7 | 235.2 | 784.1 |
| rebuilt | 10 | hnsw M=32, ef_search=128 | 0.998 | 0.998 | 4061 | 22.7 | 235.2 | 784.1 |
| rebuilt | 10 | hnsw M=32, ef_search=256 | 1.000 | 1.000 | 2186 | 22.7 | 235.2 | 784.1 |
| rebuilt | 10 | hnsw M=32, ef_search=512 | 1.000 | 1.000 | 1190 | 22.7 | 235.2 | 784.1 |
| rebuilt | 10 | ivf_flat c=1, nprobe=1 | 0.396 | 0.396 | 45078 | 1.7 | 156.3 | 521.0 |
| rebuilt | 10 | ivf_flat c=1, nprobe=2 | 0.566 | 0.566 | 29578 | 1.7 | 156.3 | 521.0 |
| rebuilt | 10 | ivf_flat c=1, nprobe=4 | 0.732 | 0.732 | 18826 | 1.7 | 156.3 | 521.0 |
| rebuilt | 10 | ivf_flat c=1, nprobe=8 | 0.867 | 0.867 | 11040 | 1.7 | 156.3 | 521.0 |
| rebuilt | 10 | ivf_flat c=1, nprobe=16 | 0.951 | 0.951 | 6184 | 1.7 | 156.3 | 521.0 |
| rebuilt | 10 | ivf_flat c=1, nprobe=32 | 0.988 | 0.988 | 3289 | 1.7 | 156.3 | 521.0 |
| rebuilt | 10 | ivf_flat c=1, nprobe=64 | 0.998 | 0.998 | 1757 | 1.7 | 156.3 | 521.0 |
| rebuilt | 10 | ivf_flat c=1, nprobe=128 | 1.000 | 1.000 | 922 | 1.7 | 156.3 | 521.0 |
| rebuilt | 10 | ivf_flat c=4, nprobe=1 | 0.306 | 0.306 | 31529 | 11.4 | 157.1 | 523.8 |
| rebuilt | 10 | ivf_flat c=4, nprobe=2 | 0.450 | 0.450 | 25427 | 11.4 | 157.1 | 523.8 |
| rebuilt | 10 | ivf_flat c=4, nprobe=4 | 0.605 | 0.605 | 22098 | 11.4 | 157.1 | 523.8 |
| rebuilt | 10 | ivf_flat c=4, nprobe=8 | 0.750 | 0.750 | 17846 | 11.4 | 157.1 | 523.8 |
| rebuilt | 10 | ivf_flat c=4, nprobe=16 | 0.867 | 0.867 | 12824 | 11.4 | 157.1 | 523.8 |
| rebuilt | 10 | ivf_flat c=4, nprobe=32 | 0.945 | 0.945 | 8395 | 11.4 | 157.1 | 523.8 |
| rebuilt | 10 | ivf_flat c=4, nprobe=64 | 0.982 | 0.982 | 4973 | 11.4 | 157.1 | 523.8 |
| rebuilt | 10 | ivf_flat c=4, nprobe=128 | 0.996 | 0.996 | 2710 | 11.4 | 157.1 | 523.8 |
| rebuilt | 10 | ivf_pq c=4 m=32, nprobe=1 | 0.295 | 0.295 | 17029 | 14.7 | 13.3 | 44.2 |
| rebuilt | 10 | ivf_pq c=4 m=32, nprobe=2 | 0.422 | 0.422 | 17207 | 14.7 | 13.3 | 44.2 |
| rebuilt | 10 | ivf_pq c=4 m=32, nprobe=4 | 0.546 | 0.546 | 15277 | 14.7 | 13.3 | 44.2 |
| rebuilt | 10 | ivf_pq c=4 m=32, nprobe=8 | 0.644 | 0.644 | 13046 | 14.7 | 13.3 | 44.2 |
| rebuilt | 10 | ivf_pq c=4 m=32, nprobe=16 | 0.708 | 0.708 | 10000 | 14.7 | 13.3 | 44.2 |
| rebuilt | 10 | ivf_pq c=4 m=32, nprobe=32 | 0.743 | 0.743 | 6382 | 14.7 | 13.3 | 44.2 |
| rebuilt | 10 | ivf_pq c=4 m=32, nprobe=64 | 0.756 | 0.756 | 4213 | 14.7 | 13.3 | 44.2 |
| rebuilt | 10 | ivf_pq c=4 m=32, nprobe=128 | 0.760 | 0.760 | 2342 | 14.7 | 13.3 | 44.2 |
| rebuilt | 10 | ivf_pq c=4 m=32, nprobe=256 | 0.761 | 0.761 | 1260 | 14.7 | 13.3 | 44.2 |
| rebuilt | 10 | ivf_pq c=4 m=64, nprobe=1 | 0.303 | 0.303 | 14830 | 17.0 | 22.9 | 76.2 |
| rebuilt | 10 | ivf_pq c=4 m=64, nprobe=2 | 0.443 | 0.443 | 13346 | 17.0 | 22.9 | 76.2 |
| rebuilt | 10 | ivf_pq c=4 m=64, nprobe=4 | 0.588 | 0.588 | 11733 | 17.0 | 22.9 | 76.2 |
| rebuilt | 10 | ivf_pq c=4 m=64, nprobe=8 | 0.715 | 0.715 | 9246 | 17.0 | 22.9 | 76.2 |
| rebuilt | 10 | ivf_pq c=4 m=64, nprobe=16 | 0.807 | 0.807 | 6395 | 17.0 | 22.9 | 76.2 |
| rebuilt | 10 | ivf_pq c=4 m=64, nprobe=32 | 0.861 | 0.861 | 3804 | 17.0 | 22.9 | 76.2 |
| rebuilt | 10 | ivf_pq c=4 m=64, nprobe=64 | 0.883 | 0.883 | 2266 | 17.0 | 22.9 | 76.2 |
| rebuilt | 10 | ivf_pq c=4 m=64, nprobe=128 | 0.890 | 0.890 | 1213 | 17.0 | 22.9 | 76.2 |
| rebuilt | 10 | ivf_pq c=4 m=64, nprobe=256 | 0.892 | 0.892 | 617 | 17.0 | 22.9 | 76.2 |
| rebuilt | 15 | exact (flat) | 1.000 | 1.000 | 241 | - | - | - |
| rebuilt | 15 | hnsw M=16, ef_search=32 | 0.933 | 0.933 | 14996 | 23.6 | 196.9 | 656.3 |
| rebuilt | 15 | hnsw M=16, ef_search=64 | 0.980 | 0.980 | 9831 | 23.6 | 196.9 | 656.3 |
| rebuilt | 15 | hnsw M=16, ef_search=128 | 0.996 | 0.996 | 5332 | 23.6 | 196.9 | 656.3 |
| rebuilt | 15 | hnsw M=16, ef_search=256 | 1.000 | 1.000 | 2786 | 23.6 | 196.9 | 656.3 |
| rebuilt | 15 | hnsw M=16, ef_search=512 | 1.000 | 1.000 | 1237 | 23.6 | 196.9 | 656.3 |
| rebuilt | 15 | hnsw M=32, ef_search=32 | 0.955 | 0.955 | 12473 | 27.1 | 235.2 | 784.1 |
| rebuilt | 15 | hnsw M=32, ef_search=64 | 0.989 | 0.989 | 8015 | 27.1 | 235.2 | 784.1 |
| rebuilt | 15 | hnsw M=32, ef_search=128 | 0.998 | 0.998 | 4381 | 27.1 | 235.2 | 784.1 |
| rebuilt | 15 | hnsw M=32, ef_search=256 | 1.000 | 1.000 | 2291 | 27.1 | 235.2 | 784.1 |
| rebuilt | 15 | hnsw M=32, ef_search=512 | 1.000 | 1.000 | 1202 | 27.1 | 235.2 | 784.1 |
| rebuilt | 15 | ivf_flat c=1, nprobe=1 | 0.396 | 0.396 | 52654 | 1.5 | 156.3 | 521.0 |
| rebuilt | 15 | ivf_flat c=1, nprobe=2 | 0.566 | 0.566 | 31563 | 1.5 | 156.3 | 521.0 |
| rebuilt | 15 | ivf_flat c=1, nprobe=4 | 0.732 | 0.732 | 19482 | 1.5 | 156.3 | 521.0 |
| rebuilt | 15 | ivf_flat c=1, nprobe=8 | 0.867 | 0.867 | 11456 | 1.5 | 156.3 | 521.0 |
| rebuilt | 15 | ivf_flat c=1, nprobe=16 | 0.951 | 0.951 | 6348 | 1.5 | 156.3 | 521.0 |
| rebuilt | 15 | ivf_flat c=1, nprobe=32 | 0.988 | 0.988 | 3348 | 1.5 | 156.3 | 521.0 |
| rebuilt | 15 | ivf_flat c=1, nprobe=64 | 0.998 | 0.998 | 1799 | 1.5 | 156.3 | 521.0 |
| rebuilt | 15 | ivf_flat c=1, nprobe=128 | 1.000 | 1.000 | 916 | 1.5 | 156.3 | 521.0 |
| rebuilt | 15 | ivf_flat c=4, nprobe=1 | 0.305 | 0.305 | 31281 | 11.5 | 157.1 | 523.8 |
| rebuilt | 15 | ivf_flat c=4, nprobe=2 | 0.450 | 0.450 | 25087 | 11.5 | 157.1 | 523.8 |
| rebuilt | 15 | ivf_flat c=4, nprobe=4 | 0.605 | 0.605 | 21870 | 11.5 | 157.1 | 523.8 |
| rebuilt | 15 | ivf_flat c=4, nprobe=8 | 0.750 | 0.750 | 17692 | 11.5 | 157.1 | 523.8 |
| rebuilt | 15 | ivf_flat c=4, nprobe=16 | 0.867 | 0.867 | 12860 | 11.5 | 157.1 | 523.8 |
| rebuilt | 15 | ivf_flat c=4, nprobe=32 | 0.945 | 0.945 | 8203 | 11.5 | 157.1 | 523.8 |
| rebuilt | 15 | ivf_flat c=4, nprobe=64 | 0.982 | 0.982 | 4962 | 11.5 | 157.1 | 523.8 |
| rebuilt | 15 | ivf_flat c=4, nprobe=128 | 0.996 | 0.996 | 2707 | 11.5 | 157.1 | 523.8 |
| rebuilt | 15 | ivf_pq c=4 m=32, nprobe=1 | 0.294 | 0.294 | 17275 | 14.6 | 13.3 | 44.2 |
| rebuilt | 15 | ivf_pq c=4 m=32, nprobe=2 | 0.422 | 0.422 | 17516 | 14.6 | 13.3 | 44.2 |
| rebuilt | 15 | ivf_pq c=4 m=32, nprobe=4 | 0.546 | 0.546 | 15835 | 14.6 | 13.3 | 44.2 |
| rebuilt | 15 | ivf_pq c=4 m=32, nprobe=8 | 0.644 | 0.644 | 13287 | 14.6 | 13.3 | 44.2 |
| rebuilt | 15 | ivf_pq c=4 m=32, nprobe=16 | 0.708 | 0.708 | 9923 | 14.6 | 13.3 | 44.2 |
| rebuilt | 15 | ivf_pq c=4 m=32, nprobe=32 | 0.742 | 0.742 | 6859 | 14.6 | 13.3 | 44.2 |
| rebuilt | 15 | ivf_pq c=4 m=32, nprobe=64 | 0.754 | 0.754 | 4230 | 14.6 | 13.3 | 44.2 |
| rebuilt | 15 | ivf_pq c=4 m=32, nprobe=128 | 0.758 | 0.758 | 2338 | 14.6 | 13.3 | 44.2 |
| rebuilt | 15 | ivf_pq c=4 m=32, nprobe=256 | 0.758 | 0.758 | 1109 | 14.6 | 13.3 | 44.2 |
| rebuilt | 15 | ivf_pq c=4 m=64, nprobe=1 | 0.302 | 0.302 | 15046 | 16.6 | 22.9 | 76.2 |
| rebuilt | 15 | ivf_pq c=4 m=64, nprobe=2 | 0.442 | 0.442 | 14087 | 16.6 | 22.9 | 76.2 |
| rebuilt | 15 | ivf_pq c=4 m=64, nprobe=4 | 0.588 | 0.588 | 11995 | 16.6 | 22.9 | 76.2 |
| rebuilt | 15 | ivf_pq c=4 m=64, nprobe=8 | 0.715 | 0.715 | 9346 | 16.6 | 22.9 | 76.2 |
| rebuilt | 15 | ivf_pq c=4 m=64, nprobe=16 | 0.809 | 0.809 | 6454 | 16.6 | 22.9 | 76.2 |
| rebuilt | 15 | ivf_pq c=4 m=64, nprobe=32 | 0.861 | 0.861 | 3970 | 16.6 | 22.9 | 76.2 |
| rebuilt | 15 | ivf_pq c=4 m=64, nprobe=64 | 0.883 | 0.883 | 2235 | 16.6 | 22.9 | 76.2 |
| rebuilt | 15 | ivf_pq c=4 m=64, nprobe=128 | 0.890 | 0.890 | 1212 | 16.6 | 22.9 | 76.2 |
| rebuilt | 15 | ivf_pq c=4 m=64, nprobe=256 | 0.892 | 0.892 | 625 | 16.6 | 22.9 | 76.2 |
