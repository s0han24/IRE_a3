import h5py
import numpy as np

from annbench.data import (
    download,
    l2_normalize,
    load_hdf5,
    prepare_vectors,
    split_queries,
    subset_base,
)


def test_split_queries_first_5000_tune_last_5000_report():
    queries = np.arange(10000 * 2, dtype=np.float32).reshape(10000, 2)

    tune, report = split_queries(queries)

    np.testing.assert_array_equal(tune, queries[:5000])
    np.testing.assert_array_equal(report, queries[5000:])


def test_l2_normalize_rows_have_unit_norm():
    x = np.array([[3.0, 4.0], [0.0, 2.0]], dtype=np.float32)

    np.testing.assert_allclose(l2_normalize(x), [[0.6, 0.8], [0.0, 1.0]], rtol=1e-6)


def test_l2_normalize_zero_row_stays_zero():
    x = np.array([[0.0, 0.0], [3.0, 4.0]], dtype=np.float32)

    np.testing.assert_allclose(l2_normalize(x), [[0.0, 0.0], [0.6, 0.8]], rtol=1e-6)


def test_load_hdf5_returns_ann_benchmarks_arrays_with_float32_vectors(tmp_path):
    rng = np.random.default_rng(0)
    arrays = {
        "train": rng.random((6, 3)),  # float64 on disk, must load as float32
        "test": rng.random((2, 3)),
        "neighbors": np.array([[0, 1], [2, 3]], dtype=np.int32),
        "distances": np.array([[0.1, 0.2], [0.3, 0.4]], dtype=np.float32),
    }
    path = tmp_path / "tiny.hdf5"
    with h5py.File(path, "w") as f:
        for key, value in arrays.items():
            f[key] = value

    data = load_hdf5(path)

    for key, value in arrays.items():
        np.testing.assert_allclose(data[key], value, rtol=1e-6)
    assert data["train"].dtype == np.float32
    assert data["test"].dtype == np.float32


def test_download_fetches_missing_file_via_part_then_renames(tmp_path):
    calls = []

    def fake_fetch(url, dest):  # like urlretrieve: records the call, writes dest
        calls.append((url, dest))
        dest.write_bytes(b"hdf5 bytes")

    path = download("sift-128-euclidean", tmp_path, fake_fetch)

    expected = tmp_path / "sift-128-euclidean.hdf5"
    part = tmp_path / "sift-128-euclidean.hdf5.part"
    assert calls == [("http://ann-benchmarks.com/sift-128-euclidean.hdf5", part)]
    assert path == expected
    assert expected.read_bytes() == b"hdf5 bytes"
    assert not part.exists()


def test_download_skips_fetch_when_file_exists(tmp_path):
    existing = tmp_path / "sift-128-euclidean.hdf5"
    existing.write_bytes(b"already here")
    calls = []

    path = download("sift-128-euclidean", tmp_path, lambda *a: calls.append(a))

    assert calls == []
    assert path == existing


def test_subset_base_keeps_first_n_rows():
    train = np.arange(10 * 2, dtype=np.float32).reshape(10, 2)

    np.testing.assert_array_equal(subset_base(train, 3), train[:3])


def test_prepare_vectors_normalises_angular_train_and_test_only():
    neighbors = np.array([[0, 1]])
    distances = np.array([[0.5, 0.7]], dtype=np.float32)
    data = {
        "train": np.array([[3.0, 4.0], [0.0, 2.0]], dtype=np.float32),
        "test": np.array([[0.0, 5.0]], dtype=np.float32),
        "neighbors": neighbors,
        "distances": distances,
    }

    out = prepare_vectors("glove-100-angular", data)

    np.testing.assert_allclose(out["train"], [[0.6, 0.8], [0.0, 1.0]], rtol=1e-6)
    np.testing.assert_allclose(out["test"], [[0.0, 1.0]], rtol=1e-6)
    assert out["neighbors"] is neighbors
    assert out["distances"] is distances


def test_prepare_vectors_leaves_sift_as_loaded():
    data = {
        "train": np.array([[3.0, 4.0], [0.0, 2.0]], dtype=np.float32),
        "test": np.array([[0.0, 5.0]], dtype=np.float32),
    }

    out = prepare_vectors("sift-128-euclidean", data)

    np.testing.assert_array_equal(out["train"], [[3.0, 4.0], [0.0, 2.0]])
    np.testing.assert_array_equal(out["test"], [[0.0, 5.0]])
