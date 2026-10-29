from annbench.metrics import latency_summary, qps
from annbench.sweeps import best_at_recall

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


INDEX_ORDER = ("exact", "hnsw", "ivf_flat", "ivf_pq")


def _config(r: dict) -> str:
    """Human-readable config of a sweep point, e.g. "hnsw M=16, ef_search=64"."""
    if r["index"] == "exact":
        return "exact (flat)"
    return f"{r['build']}, {r['search_param']}={r['search_value']}"


def _groups(pts: list[dict], *keys: str) -> list[tuple[tuple, list[dict]]]:
    """Points grouped by keys, in dataset / n_base / INDEX_ORDER order."""
    groups: dict[tuple, list[dict]] = {}
    for p in pts:
        groups.setdefault(tuple(p[k] for k in keys), []).append(p)

    def order(key: tuple) -> tuple:
        return tuple(INDEX_ORDER.index(v) if v in INDEX_ORDER else v for v in key)

    return sorted(groups.items(), key=lambda kv: order(kv[0]))


def qps_at_recall_table(
    pts: list[dict], targets: tuple[float, ...] = (0.9, 0.95)
) -> str:
    """Best single-query QPS per dataset/index at each recall target, config named."""
    head = "| dataset | index | " + " | ".join(
        f"QPS @ {t} | config @ {t}" for t in targets
    )
    lines = [head + " |", "|---|---|" + "---|---|" * len(targets)]
    for (dataset, index), group in _groups(pts, "dataset", "index"):
        cells = []
        for t in targets:
            best = best_at_recall(group, t)
            if best is None:
                top = max(p["recall"] for p in group)
                cells += ["**not reached**", f"best recall {top:.3f}"]
            else:
                cells += [f"{best['qps']:.0f}", _config(best)]
        lines.append(f"| {dataset} | {index} | " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n"


def build_cost_table(pts: list[dict], target: float = 0.95) -> str:
    """Build time, index size and bytes/vector of each index's best config at target.

    An index with no config at target is flagged and its highest-recall config shown.
    """
    lines = [
        "| dataset | index | config | recall | QPS | build s | size MB "
        "| bytes/vector |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for (dataset, index), group in _groups(pts, "dataset", "index"):
        best = best_at_recall(group, target)
        label = None
        if best is None:
            best = max(group, key=lambda p: p["recall"])
            label = f"**not reached**; highest recall: {_config(best)}"
        size = best["size_bytes"]
        lines.append(
            f"| {dataset} | {index} | {label or _config(best)} | {best['recall']:.3f} "
            f"| {best['qps']:.0f} | {best['build_seconds']:.1f} "
            f"| {size / 1e6:.1f} | {size / best['n_base']:.1f} |"
        )
    return "\n".join(lines) + "\n"


def scaling_table(pts: list[dict], target: float = 0.95) -> str:
    """Per base size and index: cheapest (highest-QPS) config reaching target recall."""
    lines = [
        "| n_base | index | config | recall | QPS | p50 ms |",
        "|---|---|---|---|---|---|",
    ]
    for (n_base, index), group in _groups(pts, "n_base", "index"):
        best = best_at_recall(group, target)
        if best is None:
            top = max(p["recall"] for p in group)
            lines.append(
                f"| {n_base} | {index} | **not reached** (best recall {top:.3f}) "
                "| | | |"
            )
            continue
        p50 = latency_summary(best["latencies_s"])["p50_ms"]
        lines.append(
            f"| {n_base} | {index} | {_config(best)} | {best['recall']:.3f} "
            f"| {best['qps']:.0f} | {p50:.2f} |"
        )
    return "\n".join(lines) + "\n"
