import numpy as np
from numpy.typing import NDArray


def recall_at_k(
    found_dists: NDArray[np.floating],
    gt_dists: NDArray[np.floating],
    k: int,
    rtol: float = 1e-5,
) -> float:
    """Mean recall@k over queries.

    found_dists: (nq, k) float, exact distances from each query to the ids returned
        by the search under test (recomputed, not taken from the index).
    gt_dists: (nq, K) float with K >= k, true neighbour distances sorted ascending.
    rtol: relative slack on the k-th true distance, so float-rounding ties are hits.
    """
    hits = found_dists <= gt_dists[:, k - 1 : k] * (1 + rtol)
    return float(hits.mean())
