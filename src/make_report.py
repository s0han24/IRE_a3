"""Stage 2 (report): results/<mode>/baseline.json -> tables/ and figures/.

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
from annbench.tables import baseline_table  # noqa: E402

SERIES = ("#2a78d6", "#eb6834")  # categorical slots 1-2, validated for CVD + contrast
INK, MUTED, GRID = "#0b0b0b", "#52514e", "#e4e3df"


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
    ax.set_xlabel("latency per query (ms, log scale)", color=MUTED)
    ax.set_ylabel("fraction of report queries", color=MUTED)
    ax.set_title(
        "Exact search latency, one query at a time (report queries)",
        color=INK,
        fontsize=10,
        loc="left",
    )
    ax.grid(True, color=GRID, linewidth=0.8)
    ax.tick_params(which="both", colors=MUTED, labelsize=8)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(GRID)
    ax.legend(frameon=False, fontsize=8, labelcolor=INK, loc="lower right")
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

    figures_dir = mode_dir / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)
    plot_latency_ecdf(records, figures_dir / "baseline_latency_ecdf.png")


if __name__ == "__main__":
    main()
