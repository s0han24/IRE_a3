from collections.abc import Callable

import numpy as np
from numpy.typing import NDArray


def time_batch(
    search_fn: Callable[[NDArray[np.floating]], object],
    queries: NDArray[np.floating],
    clock: Callable[[], float],
) -> float:
    """Seconds for one search_fn call on all queries at once.

    queries: (nq, d) float32. clock: e.g. time.perf_counter, injectable for tests.
    """
    t0 = clock()
    search_fn(queries)
    return clock() - t0


def time_one_at_a_time(
    search_fn: Callable[[NDArray[np.floating]], object],
    queries: NDArray[np.floating],
    clock: Callable[[], float],
) -> NDArray[np.float64]:
    """Per-query latency in seconds, searching one (1, d) query at a time.

    queries: (nq, d) float32. Returns (nq,) float64.
    """
    latencies = np.empty(queries.shape[0])
    for i in range(queries.shape[0]):
        t0 = clock()
        search_fn(queries[i : i + 1])
        latencies[i] = clock() - t0
    return latencies
