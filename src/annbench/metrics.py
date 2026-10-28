import numpy as np
from numpy.typing import NDArray


def latency_summary(latencies_s: NDArray[np.floating]) -> dict[str, float]:
    """Per-query latency summary in milliseconds.

    latencies_s: (nq,) float seconds. Returns p50, p95, p99 and mean, in ms.
    """
    ms = np.asarray(latencies_s) * 1000
    p50, p95, p99 = np.percentile(ms, [50, 95, 99])
    return {
        "p50_ms": float(p50),
        "p95_ms": float(p95),
        "p99_ms": float(p99),
        "mean_ms": float(ms.mean()),
    }


def qps(n_queries: int, seconds: float) -> float:
    """Queries per second for n_queries answered in `seconds` of wall time."""
    return n_queries / seconds
