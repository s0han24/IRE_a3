import faiss
import numpy as np
from numpy.typing import NDArray


class FaissExact:
    """Exact Euclidean k-NN with FAISS; the reference search."""

    def build(self, base: NDArray[np.floating]) -> "FaissExact":
        """Index base: (n, d) float32. Returns self."""
        self.index = faiss.IndexFlatL2(base.shape[1])
        self.index.add(base)
        return self

    def search(
        self, queries: NDArray[np.floating], k: int
    ) -> tuple[NDArray[np.int64], NDArray[np.floating]]:
        """queries: (nq, d) float32.

        Returns ids (nq, k) int64 nearest first, and plain L2 dists (nq, k) float32.
        """
        sq, ids = self.index.search(queries, k)
        return ids, np.sqrt(sq)
