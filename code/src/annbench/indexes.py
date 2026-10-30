"""ANN index wrappers behind one interface: build(base) -> self, set_search(...),
search(queries, k) -> (ids, dists)."""

import faiss
import numpy as np
from numpy.typing import NDArray


class _FaissWrapper:
    """Shared search over a FAISS L2 index stored in self.index."""

    index: faiss.Index

    def search(
        self, queries: NDArray[np.floating], k: int
    ) -> tuple[NDArray[np.int64], NDArray[np.floating]]:
        """queries: (nq, d) float32.

        Returns ids (nq, k) int64 nearest first, and L2 dists (nq, k) float32
        (plain, not squared; approximate for IVF-PQ).
        """
        sq, ids = self.index.search(queries, k)
        return ids, np.sqrt(sq)


class FaissHNSW(_FaissWrapper):
    """FAISS IndexHNSWFlat (L2)."""

    def __init__(self, M: int, ef_construction: int) -> None:
        self.M = M
        self.ef_construction = ef_construction

    def build(self, base: NDArray[np.floating]) -> "FaissHNSW":
        """Index base: (n, d) float32. Returns self."""
        self.index = faiss.IndexHNSWFlat(base.shape[1], self.M)
        self.index.hnsw.efConstruction = self.ef_construction
        self.index.add(base)
        return self

    def set_search(self, ef_search: int) -> None:
        """Search-time beam width; must be >= k."""
        self.index.hnsw.efSearch = ef_search


class _FaissIVF(_FaissWrapper):
    """Shared IVF build (flat coarse quantizer, train then add) and nprobe."""

    def _make_index(self, quantizer: faiss.Index, d: int) -> faiss.Index:
        raise NotImplementedError

    def build(self, base: NDArray[np.floating]) -> "_FaissIVF":
        """Train on base: (n, d) float32, then add it. Returns self."""
        self.quantizer = faiss.IndexFlatL2(base.shape[1])  # kept alive with the index
        self.index = self._make_index(self.quantizer, base.shape[1])
        self.index.train(base)
        self.index.add(base)
        return self

    def set_search(self, nprobe: int) -> None:
        """Number of inverted lists scanned per query."""
        self.index.nprobe = nprobe


class FaissIVFFlat(_FaissIVF):
    """FAISS IndexIVFFlat (L2) with a flat coarse quantizer; trained on the base."""

    def __init__(self, nlist: int) -> None:
        self.nlist = nlist

    def _make_index(self, quantizer: faiss.Index, d: int) -> faiss.Index:
        return faiss.IndexIVFFlat(quantizer, d, self.nlist)


class FaissIVFPQ(_FaissIVF):
    """FAISS IndexIVFPQ (L2): IVF lists holding product-quantised codes.

    Reported distances are approximate (computed from the codes, no re-ranking).
    """

    def __init__(self, nlist: int, m: int, nbits: int) -> None:
        self.nlist = nlist
        self.m = m
        self.nbits = nbits

    def _make_index(self, quantizer: faiss.Index, d: int) -> faiss.Index:
        return faiss.IndexIVFPQ(quantizer, d, self.nlist, self.m, self.nbits)


def index_size_bytes(wrapper: object) -> int:
    """Serialized size in bytes of a wrapper's FAISS index (its .index attribute)."""
    return len(faiss.serialize_index(wrapper.index))
