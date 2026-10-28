from annbench.metrics import latency_summary, qps

HEADER = (
    "| dataset | n_base | agrees | batch s | batch QPS | single QPS "
    "| p50 ms | p95 ms | p99 ms |"
)


def baseline_table(records: list[dict]) -> str:
    """Markdown table of exact-search baseline records, as loaded from baseline.json.

    Batch QPS, single-query QPS and latency percentiles come from annbench.metrics.
    """
    lines = [HEADER, "|---|---|---|---|---|---|---|---|---|"]
    for r in records:
        lat = latency_summary(r["latencies_s"])
        batch_qps = qps(r["n_queries"], r["batch_seconds"])
        single_qps = qps(len(r["latencies_s"]), sum(r["latencies_s"]))
        agrees = "n/a" if r["agrees_with_stored"] is None else r["agrees_with_stored"]
        lines.append(
            f"| {r['dataset']} | {r['n_base']} | {agrees} "
            f"| {r['batch_seconds']:.3f} | {batch_qps:.0f} | {single_qps:.0f} "
            f"| {lat['p50_ms']:.2f} | {lat['p95_ms']:.2f} | {lat['p99_ms']:.2f} |"
        )
    return "\n".join(lines) + "\n"
