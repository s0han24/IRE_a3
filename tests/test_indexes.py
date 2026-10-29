import numpy as np
import pytest

from annbench.exact import FaissExact
from annbench.indexes import FaissHNSW, FaissIVFFlat, FaissIVFPQ, index_size_bytes
from annbench.recall import recall_at_k

RNG = np.random.default_rng(0)
BASE = RNG.random((1000, 16), dtype=np.float32)
QUERIES = RNG.random((50, 16), dtype=np.float32)
GT_IDS, _ = FaissExact().build(BASE).search(QUERIES, 10)


def hnsw():
    index = FaissHNSW(M=16, ef_construction=100).build(BASE)
    index.set_search(ef_search=64)
    return index


def ivf_flat():
    index = FaissIVFFlat(nlist=16).build(BASE)
    index.set_search(nprobe=12)
    return index


def ivf_pq():
    # nbits=4: 16 codewords per sub-quantizer, trainable on 1000 points without warnings
    index = FaissIVFPQ(nlist=16, m=8, nbits=4).build(BASE)
    index.set_search(nprobe=16)
    return index


# PQ compresses vectors, so its recall bar is looser (measured 0.712 on this data).
@pytest.mark.parametrize(
    ("make_index", "min_recall"), [(hnsw, 0.9), (ivf_flat, 0.9), (ivf_pq, 0.5)]
)
def test_index_returns_valid_neighbours_with_high_recall(make_index, min_recall):
    ids, dists = make_index().search(QUERIES, 20)

    assert ids.shape == (50, 20) and dists.shape == (50, 20)
    assert ((ids >= 0) & (ids < 1000)).all()
    assert all(len(set(row)) == 20 for row in ids)  # no duplicates per query
    assert (np.diff(dists, axis=1) >= 0).all()  # ascending
    assert recall_at_k(ids, dists, GT_IDS, k=10) >= min_recall


def test_index_size_bytes_of_flat_index_is_raw_vectors_plus_small_header():
    raw = BASE.size * 4  # 1000 x 16 float32 = 64,000 bytes

    size = index_size_bytes(FaissExact().build(BASE))

    assert raw <= size <= raw + 1_000
