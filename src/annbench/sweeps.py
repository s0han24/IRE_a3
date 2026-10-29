"""Pure analysis of sweep results (recall / QPS records); no FAISS, no timing."""

import numpy as np
from numpy.typing import ArrayLike


def curve_area(recalls: ArrayLike, qps: ArrayLike) -> float:
    """Area under log10(QPS) vs recall for one build config's sweep curve.

    recalls, qps: (p,) one point per search-parameter value, any order. Only points
    with recall >= 0.5 are used; the trapezoid rule joins them in recall order.
    """
    recalls, qps = np.asarray(recalls), np.asarray(qps)
    keep = recalls >= 0.5
    recalls, qps = recalls[keep], qps[keep]
    order = np.argsort(recalls)
    return float(np.trapezoid(np.log10(qps[order]), recalls[order]))


def best_at_recall(records: list[dict], target: float) -> dict | None:
    """Highest-QPS record whose recall >= target, or None if no record reaches it.

    records: dicts with at least "recall" (report queries) and "qps" (single-query).
    """
    reaching = [r for r in records if r["recall"] >= target]
    return max(reaching, key=lambda r: r["qps"], default=None)


def top_build_configs(records: list[dict], n: int) -> list[str]:
    """The n build labels whose sweep curves have the largest curve_area, best first.

    records: dicts with "build" (str label, e.g. "hnsw M=16"), "recall" and "qps"; one
    record per (build, search parameter) point.
    """
    curves: dict[str, tuple[list[float], list[float]]] = {}
    for r in records:
        recalls, qps = curves.setdefault(r["build"], ([], []))
        recalls.append(r["recall"])
        qps.append(r["qps"])
    ranked = sorted(curves, key=lambda b: curve_area(*curves[b]), reverse=True)
    return ranked[:n]


def points(records: list[dict], recall_key: str = "report_recall") -> list[dict]:
    """Sweep records with "recall" (from recall_key) and single-query "qps" added.

    recall_key: "tune_recall" to select configs, "report_recall" for reported numbers.
    """
    out = []
    for r in records:
        lat = r["latencies_s"]
        out.append({**r, "recall": r[recall_key], "qps": len(lat) / sum(lat)})
    return out
