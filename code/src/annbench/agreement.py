import numpy as np
from numpy.typing import NDArray


def neighbours_agree(
    found_ids: NDArray[np.integer],
    stored_ids: NDArray[np.integer],
    stored_dists: NDArray[np.floating],
    k: int,
    rtol: float = 1e-5,
) -> bool:
    """True if found and stored top-k neighbours match, allowing any order within ties.

    found_ids: (nq, k) int from our exact search.
    stored_ids, stored_dists: (nq, K) with K >= k, from the data file, dists ascending.
    Ties are judged only by stored_dists, so our distance scale never matters
    (GloVe's stored distances are angular, ours are L2).
    rtol: relative slack on the k-th stored distance for float-rounding ties.
    """
    d_k = stored_dists[:, k - 1 : k]
    within_k = stored_dists <= d_k * (1 + rtol)  # (nq, K) stored ids allowed in top-k
    must_have = stored_dists < d_k * (1 - rtol)  # (nq, K) strictly better than k-th
    match = found_ids[:, :, None] == stored_ids[:, None, :]  # (nq, k, K)
    found_ok = (match & within_k[:, None, :]).any(axis=2)  # (nq, k)
    present = match.any(axis=1)  # (nq, K)
    return bool(found_ok.all() and (present | ~must_have).all())
