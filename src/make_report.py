"""Stage 2 (report): results/<mode>/*.json -> tables/ and figures/.

Reads results/ only (never data/ or FAISS). Wiring only; logic is tested in annbench.
Usage: uv run python src/make_report.py [--quick]
"""

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # headless: write files, never open a window
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.ticker import ScalarFormatter  # noqa: E402

from annbench.results_io import load_results  # noqa: E402
from annbench.sweeps import best_at_recall, points, top_build_configs  # noqa: E402
from annbench.tables import (  # noqa: E402
    baseline_table,
    build_cost_table,
    qps_at_recall_table,
    scaling_table,
)

# Categorical slots 1-4, validated (CVD + normal-vision pass; slots 3-4 are below 3:1
# contrast, so every plot also has a legend, distinct markers and a matching table).
SERIES = ("#2a78d6", "#eb6834", "#1baf7a", "#eda100")
INK, MUTED, GRID = "#0b0b0b", "#52514e", "#e4e3df"
STYLE = {  # index -> (color, marker); fixed so an index keeps its look in every plot
    "hnsw": (SERIES[0], "o"),
    "ivf_flat": (SERIES[1], "s"),
    "ivf_pq": (SERIES[2], "^"),
    "exact": (SERIES[3], "*"),
}


def style_axes(ax, title: str, xlabel: str, ylabel: str) -> None:
    """Recessive grid/spines, muted axis text, left-aligned title."""
    ax.set_title(title, color=INK, fontsize=10, loc="left")
    ax.set_xlabel(xlabel, color=MUTED)
    ax.set_ylabel(ylabel, color=MUTED)
    ax.grid(True, color=GRID, linewidth=0.8)
    ax.tick_params(which="both", colors=MUTED, labelsize=8)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(GRID)
    ax.legend(frameon=False, fontsize=8, labelcolor=INK)


def exact_points(records: list[dict]) -> list[dict]:
    """baseline_1thread records as sweep-style points (recall 1.0 by definition)."""
    pts = [{**r, "index": "exact", "report_recall": 1.0} for r in records]
    return points(pts)


def plot_recall_vs_qps(sweep: list[dict], exact: list[dict], out_path: Path) -> None:
    """Per dataset: the best build (by tune-recall curve area) of each index + exact."""
    datasets = sorted({r["dataset"] for r in sweep})
    fig, axes = plt.subplots(
        1, len(datasets), figsize=(6 * len(datasets), 4.2), dpi=150
    )
    for ax, dataset in zip(np.atleast_1d(axes), datasets, strict=True):
        for index in ("hnsw", "ivf_flat", "ivf_pq"):
            mine = [r for r in sweep if r["dataset"] == dataset and r["index"] == index]
            if not mine:
                continue
            best = top_build_configs(points(mine, "tune_recall"), 1)[0]
            curve = sorted(
                (p for p in points(mine) if p["build"] == best),
                key=lambda p: p["search_value"],
            )
            color, marker = STYLE[index]
            ax.plot(
                [p["qps"] for p in curve],
                [p["recall"] for p in curve],
                color=color,
                marker=marker,
                markersize=5,
                linewidth=2,
                label=best,
            )
        for p in exact:
            if p["dataset"] == dataset:
                color, marker = STYLE["exact"]
                ax.plot(
                    p["qps"],
                    1.0,
                    color=color,
                    marker=marker,
                    markersize=12,
                    linestyle="none",
                    label=f"exact (flat), {p['qps']:.0f} QPS",
                )
        for target in (0.9, 0.95):
            ax.axhline(target, color=MUTED, linewidth=0.8, linestyle=":")
            ax.annotate(
                f"recall {target}",
                (1, target),
                xycoords=("axes fraction", "data"),
                xytext=(-4, 2),
                textcoords="offset points",
                ha="right",
                va="bottom",
                color=MUTED,
                fontsize=7,
            )
        ax.set_xscale("log")
        style_axes(
            ax,
            f"{dataset}: recall@10 vs single-query QPS (report queries)",
            "queries per second, 1 thread (log scale)",
            "recall@10",
        )
    fig.tight_layout()
    fig.savefig(out_path)
    plt.close(fig)


def plot_scaling(pts: list[dict], out_path: Path, target: float = 0.95) -> None:
    """QPS of the cheapest config reaching target recall, against base size."""
    fig, ax = plt.subplots(figsize=(7, 4.2), dpi=150)
    for index in ("exact", "hnsw", "ivf_flat"):
        xs, ys = [], []
        for n in sorted({p["n_base"] for p in pts}):
            group = [p for p in pts if p["index"] == index and p["n_base"] == n]
            best = best_at_recall(group, target)
            if best is not None:
                xs.append(n)
                ys.append(best["qps"])
        color, marker = STYLE[index]
        ax.plot(
            xs, ys, color=color, marker=marker, markersize=7, linewidth=2, label=index
        )
    ax.set_xscale("log")
    ax.set_yscale("log")
    style_axes(
        ax,
        f"SIFT: best single-query QPS reaching recall@10 >= {target}",
        "base vectors (log scale)",
        "queries per second, 1 thread (log scale)",
    )
    fig.tight_layout()
    fig.savefig(out_path)
    plt.close(fig)


def plot_latency_ecdf(records: list[dict], out_path: Path) -> None:
    """One-at-a-time exact-search latency ECDF, one line per dataset."""
    fig, ax = plt.subplots(figsize=(7, 4), dpi=150)
    for color, r in zip(SERIES, records, strict=False):
        ms = np.sort(np.asarray(r["latencies_s"]) * 1000)
        frac = np.arange(1, ms.size + 1) / ms.size
        label = f"{r['dataset']} (n_base {r['n_base']:,})"
        ax.step(ms, frac, where="post", color=color, linewidth=2, label=label)
    ax.set_xscale("log")
    ax.xaxis.set_major_formatter(ScalarFormatter())
    ax.xaxis.set_minor_formatter(ScalarFormatter())
    style_axes(
        ax,
        "Exact search latency, one query at a time (report queries)",
        "latency per query (ms, log scale)",
        "fraction of report queries",
    )
    fig.tight_layout()
    fig.savefig(out_path)
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--quick", action="store_true")
    parser.add_argument("--out", type=Path, default=Path("results"))
    args = parser.parse_args()

    mode_dir = args.out / ("quick" if args.quick else "full")
    records, _ = load_results(mode_dir / "baseline.json")

    tables_dir = mode_dir / "tables"
    tables_dir.mkdir(parents=True, exist_ok=True)
    table = baseline_table(records)
    (tables_dir / "baseline.md").write_text(table)
    print(table)
    # Optional re-timed baselines (e.g. baseline_1thread.json), each to its own table.
    for path in sorted(mode_dir.glob("baseline_*thread.json")):
        thread_table = baseline_table(load_results(path)[0])
        (tables_dir / f"{path.stem}.md").write_text(thread_table)
        print(path.stem, thread_table, sep="\n")

    figures_dir = mode_dir / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)
    plot_latency_ecdf(records, figures_dir / "baseline_latency_ecdf.png")

    # ANN sweeps (spec "Benchmarks:"): reported numbers use report-query recall.
    sweep_path, exact_path = (
        mode_dir / "sweeps.json",
        mode_dir / "baseline_1thread.json",
    )
    if sweep_path.exists() and exact_path.exists():
        sweep = load_results(sweep_path)[0]
        exact = exact_points(load_results(exact_path)[0])
        pts = points(sweep)
        for name, text in (
            ("qps_at_recall", qps_at_recall_table(pts + exact)),
            ("build_cost_at_0.95", build_cost_table(pts)),
        ):
            (tables_dir / f"{name}.md").write_text(text)
            print(name, text, sep="\n")
        plot_recall_vs_qps(sweep, exact, figures_dir / "recall_vs_qps.png")

    # Scaling experiment (spec "Experiments on standard data:").
    scaling_path = mode_dir / "scaling.json"
    if scaling_path.exists():
        pts = points(load_results(scaling_path)[0])
        text = scaling_table(pts)
        (tables_dir / "scaling.md").write_text(text)
        print("scaling", text, sep="\n")
        plot_scaling(pts, figures_dir / "scaling_qps_at_0.95.png")


if __name__ == "__main__":
    main()
