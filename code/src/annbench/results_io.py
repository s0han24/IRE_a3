import json
import os
import platform
from datetime import UTC, datetime
from pathlib import Path

import faiss
import h5py
import numpy as np


def save_results(path: Path, records: list[dict], meta: dict) -> None:
    """Write records plus run metadata (params, seed, versions, machine) as JSON."""
    path.write_text(json.dumps({"meta": meta, "records": records}, indent=2))


def load_results(path: Path) -> tuple[list[dict], dict]:
    """Read a file written by save_results. Returns (records, meta)."""
    data = json.loads(path.read_text())
    return data["records"], data["meta"]


def run_meta(params: dict) -> dict:
    """Metadata saved next to every result: params, library versions, machine, time."""
    return {
        "params": params,
        "versions": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "faiss": faiss.__version__,
            "h5py": h5py.__version__,
        },
        "machine": {
            "platform": platform.platform(),
            "processor": platform.processor(),
            "cpu_count": os.cpu_count(),
            "faiss_threads": faiss.omp_get_max_threads(),
        },
        "timestamp": datetime.now(UTC).isoformat(),
    }
