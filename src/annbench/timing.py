from collections.abc import Callable, Iterator
from contextlib import contextmanager

import faiss
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


@contextmanager
def faiss_threads(n: int) -> Iterator[None]:
    """Run the block with FAISS (OpenMP) at n threads; restore the old count after."""
    before = faiss.omp_get_max_threads()
    faiss.omp_set_num_threads(n)
    try:
        yield
    finally:
        faiss.omp_set_num_threads(before)


def time_build[T](
    build_fn: Callable[[], T], clock: Callable[[], float]
) -> tuple[T, float]:
    """Call build_fn once (e.g. train + add an index). Returns (its result, seconds)."""
    t0 = clock()
    result = build_fn()
    return result, clock() - t0
