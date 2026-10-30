from annbench.results_io import load_results, run_meta, save_results


def test_save_then_load_results_round_trips_records_and_meta(tmp_path):
    records = [
        {
            "dataset": "sift-128-euclidean",
            "mode": "batch",
            "recall@10": 1.0,
            "qps": 812.5,
        },
        {"dataset": "sift-128-euclidean", "mode": "single", "latency_ms": [1.2, 1.4]},
    ]
    meta = {"seed": 0, "versions": {"faiss": "1.15.1"}, "machine": {"cpu": "arm64"}}
    path = tmp_path / "baseline.json"

    save_results(path, records, meta)

    assert load_results(path) == (records, meta)


def test_run_meta_records_params_versions_machine_and_time():
    params = {"k": 10, "seed": 0, "quick": True}

    meta = run_meta(params)

    assert meta["params"] == params
    assert set(meta["versions"]) == {"python", "numpy", "faiss", "h5py"}
    assert all(isinstance(v, str) for v in meta["versions"].values())
    assert {"platform", "processor", "cpu_count"} <= set(meta["machine"])
    assert isinstance(meta["timestamp"], str)


def test_run_meta_records_faiss_thread_count():
    threads = run_meta({}).get("machine", {}).get("faiss_threads")

    assert isinstance(threads, int) and threads >= 1
