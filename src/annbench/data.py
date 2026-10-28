from collections.abc import Callable
from pathlib import Path

import h5py
import numpy as np
from numpy.typing import NDArray


def split_queries(
    queries: NDArray[np.floating],
) -> tuple[NDArray[np.floating], NDArray[np.floating]]:
    """Split queries into (tune, report) halves.

    queries: (10000, d) float. Returns tune = first 5000 rows, report = last 5000 rows.
    """
    return queries[:5000], queries[5000:]


def l2_normalize(x: NDArray[np.floating]) -> NDArray[np.floating]:
    """Scale each row to unit L2 norm.

    x: (n, d) float32. Returns (n, d) float32. All-zero rows stay zero.
    """
    norms = np.linalg.norm(x, axis=1, keepdims=True)
    norms[norms == 0] = 1
    return x / norms


def load_hdf5(path: Path) -> dict[str, NDArray]:
    """Load an ann-benchmarks HDF5 file.

    Returns train (n, d) float32, test (nq, d) float32, neighbors (nq, K) int,
    distances (nq, K) float, keyed by their names in the file.
    """
    with h5py.File(path, "r") as f:
        data = {key: f[key][:] for key in ("train", "test", "neighbors", "distances")}
    for key in ("train", "test"):
        data[key] = np.ascontiguousarray(data[key], dtype=np.float32)
    return data


def download(name: str, data_dir: Path, fetch: Callable[[str, Path], object]) -> Path:
    """Fetch ann-benchmarks dataset `name` (e.g. "sift-128-euclidean") into data_dir.

    fetch(url, dest): e.g. urllib.request.urlretrieve, injectable for tests.
    Returns the local path data_dir / f"{name}.hdf5".
    """
    dest = data_dir / f"{name}.hdf5"
    if not dest.exists():
        part = dest.with_name(dest.name + ".part")
        fetch(f"http://ann-benchmarks.com/{name}.hdf5", part)
        part.replace(dest)
    return dest


def subset_base(train: NDArray[np.floating], n: int) -> NDArray[np.floating]:
    """First n base vectors, for --quick runs.

    train: (N, d) float32. Returns (n, d) float32.
    """
    return train[:n]


def prepare_vectors(name: str, data: dict[str, NDArray]) -> dict[str, NDArray]:
    """Apply per-dataset preprocessing to load_hdf5 output.

    Angular datasets (name ends in "-angular", i.e. GloVe) get train and test
    L2-normalised so Euclidean search ranks like cosine. Others are returned as loaded.
    neighbors and distances are never changed.
    """
    if not name.endswith("-angular"):
        return data
    return {
        **data,
        "train": l2_normalize(data["train"]),
        "test": l2_normalize(data["test"]),
    }
