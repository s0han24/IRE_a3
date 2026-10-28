import numpy as np

from annbench.exact import FaissExact

# 5 points in 2-D; neighbours below are worked out by hand.
BASE = np.array([[0, 0], [1, 0], [0, 2], [3, 0], [0, -4]], dtype=np.float32)


def test_faiss_exact_returns_nearest_ids_in_order():
    # q0 (0.1, 0): dists 0.1, 0.9, ~2.00, 2.9, ~4.00 -> 0, 1, 2
    # q1 (0, 3):   dists 3, ~3.16, 1, ~4.24, 7       -> 2, 0, 1
    queries = np.array([[0.1, 0], [0, 3]], dtype=np.float32)

    ids, _ = FaissExact().build(BASE).search(queries, k=3)

    np.testing.assert_array_equal(ids, [[0, 1, 2], [2, 0, 1]])


def test_faiss_exact_returns_l2_dists_ascending():
    # Plain L2, not FAISS's squared L2; matches ann-benchmarks' stored SIFT distances.
    queries = np.array([[0.1, 0], [0, 3]], dtype=np.float32)

    _, dists = FaissExact().build(BASE).search(queries, k=3)

    expected = [[0.1, 0.9, np.sqrt(4.01)], [1.0, 3.0, np.sqrt(10.0)]]
    np.testing.assert_allclose(dists, expected, rtol=1e-6)
