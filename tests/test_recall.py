import numpy as np
import pytest

from annbench.recall import recall_at_k


def test_recall_at_k_no_ties():
    # k=2, so the 2nd true distance (0.2) is the hit threshold.
    # query 0: both found within 0.2 -> 1.0; query 1: one of two -> 0.5
    gt_dists = np.array([[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]], dtype=np.float32)
    found_dists = np.array([[0.2, 0.1], [0.1, 0.9]], dtype=np.float32)

    assert recall_at_k(found_dists, gt_dists, k=2) == pytest.approx(0.75)


def test_recall_at_k_float_noise_at_kth_is_hit():
    # SIFT-scale threshold 300.0; float32 ulp there is ~3e-5.
    # 300 * (1 + 1e-6) is ~10 ulps above: float noise -> hit.
    # 300 * (1 + 1e-3) is a real gap -> miss.
    gt_dists = np.array([[299.0, 300.0]], dtype=np.float32)
    found_dists = np.array([[300.0 * (1 + 1e-6), 300.0 * (1 + 1e-3)]], dtype=np.float32)

    assert recall_at_k(found_dists, gt_dists, k=2) == pytest.approx(0.5)
