import pytest

from annbench.sweeps import best_at_recall, curve_area, top_build_configs


def test_curve_area_is_trapezoid_of_log10_qps_over_recall():
    # log10 qps = 1, 2, 3 at recall 0.5, 0.75, 1.0:
    # 0.25 * (1 + 2) / 2 + 0.25 * (2 + 3) / 2 = 0.375 + 0.625 = 1.0
    assert curve_area([0.5, 0.75, 1.0], [10, 100, 1000]) == pytest.approx(1.0)


def test_curve_area_ignores_points_below_recall_half():
    # The (0.3, 1e5) point would add 0.2 * (5 + 1) / 2 = 0.6 if it were used.
    recalls = [0.3, 0.5, 0.75, 1.0]
    qps = [100_000, 10, 100, 1000]

    assert curve_area(recalls, qps) == pytest.approx(1.0)


def test_curve_area_sorts_points_by_recall():
    # Same points as the first test, shuffled: area must still be 1.0.
    assert curve_area([1.0, 0.5, 0.75], [1000, 10, 100]) == pytest.approx(1.0)


RECORDS = [
    {"config": "a", "recall": 0.80, "qps": 1000},
    {"config": "b", "recall": 0.92, "qps": 600},
    {"config": "c", "recall": 0.96, "qps": 300},
    {"config": "d", "recall": 0.99, "qps": 100},
]


def test_best_at_recall_is_fastest_record_reaching_target():
    # a is fastest overall but below 0.9; b is the fastest of b, c, d.
    assert best_at_recall(RECORDS, 0.9)["config"] == "b"


def test_best_at_recall_is_none_when_no_record_reaches_target():
    # Best recall is 0.99: nothing reaches 0.999, which the report must flag.
    assert best_at_recall(RECORDS, 0.999) is None


def test_top_build_configs_ranks_builds_by_curve_area():
    # A: 0.3 * (3 + 2) / 2 = 0.75; B: 0.3 * (2 + 1) / 2 = 0.45. Interleaved on purpose.
    records = [
        {"build": "B", "recall": 0.6, "qps": 100},
        {"build": "A", "recall": 0.6, "qps": 1000},
        {"build": "B", "recall": 0.9, "qps": 10},
        {"build": "A", "recall": 0.9, "qps": 100},
    ]

    assert top_build_configs(records, n=1) == ["A"]
