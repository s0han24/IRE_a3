import numpy as np
import pytest

from annbench.metrics import latency_summary, qps


def test_latency_summary_reports_percentiles_and_mean_in_ms():
    latencies_s = np.arange(1, 101) / 1000  # 1 ms .. 100 ms

    summary = latency_summary(latencies_s)

    # numpy's default linear interpolation: p50 = 50.5, p95 = 95.05, p99 = 99.01
    assert summary == pytest.approx(
        {"p50_ms": 50.5, "p95_ms": 95.05, "p99_ms": 99.01, "mean_ms": 50.5}
    )


def test_qps_is_queries_over_seconds():
    assert qps(5000, 2.0) == pytest.approx(2500.0)
