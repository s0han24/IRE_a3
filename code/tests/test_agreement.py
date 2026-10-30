import numpy as np

from annbench.agreement import neighbours_agree


def test_neighbours_agree_when_only_tie_order_differs():
    # k=3: stored ids 7 and 9 tie at 3rd place (0.3); found picked 9 instead of 7.
    stored_ids = np.array([[5, 2, 7, 9]])
    stored_dists = np.array([[0.1, 0.2, 0.3, 0.3]], dtype=np.float32)
    found_ids = np.array([[5, 2, 9]])

    assert neighbours_agree(found_ids, stored_ids, stored_dists, k=3)


def test_neighbours_disagree_when_a_non_tied_neighbour_differs():
    # k=3: stored id 2 (0.2) is strictly better than the 3rd place; found has 8 instead.
    stored_ids = np.array([[5, 2, 7, 9]])
    stored_dists = np.array([[0.1, 0.2, 0.3, 0.3]], dtype=np.float32)
    found_ids = np.array([[5, 8, 7]])

    assert not neighbours_agree(found_ids, stored_ids, stored_dists, k=3)
