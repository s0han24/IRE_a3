import numpy as np
from numpy.typing import NDArray


def recall_at_k(
    found_ids: NDArray[np.integer],
    found_dists: NDArray[np.floating],
    gt_ids: NDArray[np.integer],
    k: int,
    rtol: float = 1e-5,
) -> float:
    """Mean recall@k over queries, with ties handled on the found side.

    found_ids, found_dists: (nq, k') with k' >= k, as returned by the index, dists
        ascending. Every found id whose distance is <= the k-th found distance
        * (1 + rtol) counts as retrieved, so an index's arbitrary tie order at the
        k-th place cannot hide a true neighbour.
    gt_ids: (nq, k) int, exact top-k ids.
    """
    d_k = found_dists[:, k - 1 : k] * (1 + rtol)
    retrieved = found_dists <= d_k  # (nq, k') within the k-th place, ties included
    in_gt = (found_ids[:, :, None] == gt_ids[:, None, :]).any(axis=2)  # (nq, k')
    hits = (retrieved & in_gt).sum(axis=1)  # (nq,)
    return float(hits.mean() / k)
