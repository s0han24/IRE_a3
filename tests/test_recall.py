import numpy as np
import pytest

from annbench.recall import recall_at_k


def test_recall_at_k_no_ties():
    # k=2, k'=4, no ties at the 2nd found distance, so only the first 2 found ids count.
    # query 0: found {1, 0} vs GT {0, 1} -> 1.0
    # query 1: found {3, 9} vs GT {3, 4} -> 0.5
    gt_ids = np.array([[0, 1], [3, 4]])
    found_ids = np.array([[1, 0, 7, 8], [3, 9, 4, 6]])
    found_dists = np.array([[0.1, 0.2, 0.3, 0.4]] * 2, dtype=np.float32)

    assert recall_at_k(found_ids, found_dists, gt_ids, k=2) == pytest.approx(0.75)


def test_recall_at_k_float_noise_at_kth_is_hit():
    # SIFT-scale 2nd found distance 300.0; float32 ulp there is ~3e-5.
    # id 7 at 300 * (1 + 1e-6) (~10 ulps above): float-noise tie -> joins the found set.
    # id 8 at 300 * (1 + 1e-3): real gap -> excluded. GT {7, 8} -> 1 of 2.
    gt_ids = np.array([[7, 8]])
    found_ids = np.array([[5, 6, 7, 8]])
    found_dists = np.array(
        [[299.0, 300.0, 300.0 * (1 + 1e-6), 300.0 * (1 + 1e-3)]], dtype=np.float32
    )

    assert recall_at_k(found_ids, found_dists, gt_ids, k=2) == pytest.approx(0.5)


def test_recall_at_k_found_tie_beyond_kth_is_hit():
    # k=2: found dists 0.1 0.2 0.2 0.2, so places 3 and 4 tie the 2nd.
    # GT id 12 sits at found place 3 (the index broke the tie arbitrarily):
    # still a hit.
    gt_ids = np.array([[10, 12]])
    found_ids = np.array([[10, 11, 12, 13]])
    found_dists = np.array([[0.1, 0.2, 0.2, 0.2]], dtype=np.float32)

    assert recall_at_k(found_ids, found_dists, gt_ids, k=2) == pytest.approx(1.0)
