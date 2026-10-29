import faiss
import numpy as np
import pytest

from annbench.timing import (
    faiss_threads,
    time_batch,
    time_build,
    time_one_at_a_time,
)


def test_time_batch_calls_search_once_on_all_queries_and_returns_clock_delta():
    queries = np.zeros((4, 2), dtype=np.float32)
    calls = []
    clock = iter([10.0, 12.5]).__next__

    elapsed = time_batch(calls.append, queries, clock)

    assert len(calls) == 1
    assert calls[0] is queries
    assert elapsed == pytest.approx(2.5)


def test_time_one_at_a_time_calls_search_per_query_and_returns_latencies():
    queries = np.arange(6, dtype=np.float32).reshape(3, 2)
    calls = []
    clock = iter([0.0, 1.0, 1.0, 3.0, 3.0, 6.0]).__next__

    latencies = time_one_at_a_time(calls.append, queries, clock)

    assert len(calls) == 3
    for i, call in enumerate(calls):
        np.testing.assert_array_equal(call, queries[i : i + 1])  # (1, d) slice
    np.testing.assert_allclose(latencies, [1.0, 2.0, 3.0])


def test_faiss_threads_sets_count_and_restores_it_even_on_error():
    before = faiss.omp_get_max_threads()

    with faiss_threads(1):
        assert faiss.omp_get_max_threads() == 1
    assert faiss.omp_get_max_threads() == before

    with pytest.raises(RuntimeError), faiss_threads(1):
        raise RuntimeError("search failed")
    assert faiss.omp_get_max_threads() == before


def test_time_build_calls_build_once_and_returns_result_and_clock_delta():
    built = object()
    calls = []

    def build():
        calls.append(1)
        return built

    result, seconds = time_build(build, iter([5.0, 7.5]).__next__)

    assert calls == [1]
    assert result is built
    assert seconds == pytest.approx(2.5)
