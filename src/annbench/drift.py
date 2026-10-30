"""Simulated preprocessing drift: transforms applied to base and/or query vectors."""

import numpy as np
from numpy.typing import NDArray


def mean_shift(x: NDArray[np.floating], c: float) -> NDArray[np.float32]:
    """Add the constant c to every coordinate. No scaling, no normalisation.

    x: (n, d) float32. Returns a new (n, d) float32 array; x is not modified.
    """
    return (x + c).astype(np.float32)


def rotate_pairs(x: NDArray[np.floating], degrees: float) -> NDArray[np.float32]:
    """Rotate each coordinate pair (0, 1), (2, 3), ... by the same angle, like RoPE.

    (a, b) -> (a cos t - b sin t, a sin t + b cos t), counter-clockwise.
    x: (n, d) float32 with d even. Returns a new (n, d) float32 array.
    """
    t = np.deg2rad(degrees)
    a, b = x[:, 0::2], x[:, 1::2]
    out = np.empty(x.shape, dtype=np.float32)
    out[:, 0::2] = a * np.cos(t) - b * np.sin(t)
    out[:, 1::2] = a * np.sin(t) + b * np.cos(t)
    return out
