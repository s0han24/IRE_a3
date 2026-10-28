from annbench.tables import baseline_table


def test_baseline_table_renders_header_and_one_row():
    record = {
        "dataset": "sift-128-euclidean",
        "n_base": 1000000,
        "n_queries": 5000,
        "agrees_with_stored": True,
        "batch_seconds": 2.0,
        "latencies_s": [i / 1000 for i in range(1, 101)],  # 1 ms .. 100 ms
    }

    lines = baseline_table([record]).splitlines()

    assert lines == [
        "| dataset | n_base | agrees | batch s | batch QPS | single QPS "
        "| p50 ms | p95 ms | p99 ms |",
        "|---|---|---|---|---|---|---|---|---|",
        "| sift-128-euclidean | 1000000 | True | 2.000 | 2500 | 20 "
        "| 50.50 | 95.05 | 99.01 |",
    ]


def test_baseline_table_shows_na_when_agreement_skipped():
    record = {
        "dataset": "sift-128-euclidean",
        "n_base": 100000,
        "n_queries": 5000,
        "agrees_with_stored": None,  # --quick: agreement check skipped
        "batch_seconds": 2.0,
        "latencies_s": [0.001, 0.002],
    }

    row = baseline_table([record]).splitlines()[2]
    agrees_cell = row.split("|")[3].strip()

    assert agrees_cell == "n/a"
