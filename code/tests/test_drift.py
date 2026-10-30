import numpy as np
import pytest

from annbench.drift import mean_shift, rotate_pairs


def test_mean_shift_adds_constant_to_every_coordinate_without_touching_input():
    x = np.array([[0.0, 1.0], [2.0, -3.0]], dtype=np.float32)

    out = mean_shift(x, 5)

    np.testing.assert_allclose(out, [[5.0, 6.0], [7.0, 2.0]])
    assert out.dtype == np.float32
    np.testing.assert_array_equal(x, [[0.0, 1.0], [2.0, -3.0]])  # input unchanged


def test_rotate_pairs_rotates_each_pair_counter_clockwise():
    # 90 degrees: pair (0, 1) = (1, 0) -> (0, 1); pair (2, 3) = (0, 1) -> (-1, 0)
    x = np.array([[1.0, 0.0, 0.0, 1.0]], dtype=np.float32)

    out = rotate_pairs(x, 90)

    np.testing.assert_allclose(out, [[0.0, 1.0, -1.0, 0.0]], atol=1e-6)
    assert out.dtype == np.float32
    np.testing.assert_array_equal(x, [[1.0, 0.0, 0.0, 1.0]])  # input unchanged


@pytest.mark.parametrize(
    "transform", [lambda x: mean_shift(x, 15), lambda x: rotate_pairs(x, 5)]
)
def test_drift_applied_to_all_vectors_preserves_pairwise_l2_distances(transform):
    # Why "rebuilt" (base and queries both transformed) should reproduce "clean".
    x = np.random.default_rng(0).random((50, 16), dtype=np.float32) * 100

    def pairwise(v):
        return np.linalg.norm(v[:, None, :] - v[None, :, :], axis=2)

    np.testing.assert_allclose(
        pairwise(transform(x)), pairwise(x), rtol=1e-5, atol=1e-3
    )
