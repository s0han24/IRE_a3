from collections.abc import Callable, Iterator
from contextlib import contextmanager

import faiss
import numpy as np
from numpy.typing import NDArray


def time_batch(
    search_fn: Callable[[NDArray[np.floating]], object],
    queries: NDArray[np.floating],
    clock: Callable[[], float],
    repeats: int = 1,
) -> float:
    """Seconds for one search_fn call on all queries at once; median of `repeats` calls.

    queries: (nq, d) float32. clock: e.g. time.perf_counter, injectable for tests.
    """
    times = []
    for _ in range(repeats):
        t0 = clock()
        search_fn(queries)
        times.append(clock() - t0)
    return float(np.median(times))


def time_one_at_a_time(
    search_fn: Callable[[NDArray[np.floating]], object],
    queries: NDArray[np.floating],
    clock: Callable[[], float],
    repeats: int = 1,
) -> NDArray[np.float64]:
    """Per-query latency in seconds, searching one (1, d) query at a time.

    The whole pass over queries is run `repeats` times; each query's latency is the
    median of its `repeats` measurements.
    queries: (nq, d) float32. Returns (nq,) float64.
    """
    latencies = np.empty((repeats, queries.shape[0]))
    for r in range(repeats):
        for i in range(queries.shape[0]):
            t0 = clock()
            search_fn(queries[i : i + 1])
            latencies[r, i] = clock() - t0
    return np.median(latencies, axis=0)


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
