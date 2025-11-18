"""
Compare arbitrary SimpleBacktest configurations and export a summary plus
combined equity curve plot. Useful for Week 2 experiments that mix different
moving-average windows or indicator types.

Example:
    cd python
    python scripts/compare_configs.py --config configs/week2_spy_runs.json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List

import matplotlib.pyplot as plt
import pandas as pd

import sys

PYTHON_DIR = Path(__file__).resolve().parents[1]
if str(PYTHON_DIR) not in sys.path:
    sys.path.insert(0, str(PYTHON_DIR))

from backtester.simple_backtest import SimpleBacktest

REPO_ROOT = Path(__file__).resolve().parents[2]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Compare arbitrary backtest configs.")
    parser.add_argument(
        "--config",
        type=Path,
        required=True,
        help="JSON file describing a list of run configurations.",
    )
    parser.add_argument(
        "--label",
        type=str,
        help="Optional label used in output filenames and plot title (default: config stem).",
    )
    parser.add_argument(
        "--summary-csv",
        type=Path,
        help="Override path for summary CSV output.",
    )
    parser.add_argument(
        "--equity-plot",
        type=Path,
        help="Override path for combined equity curve PNG.",
    )
    return parser


def load_config(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        raise SystemExit(f"Config file not found: {path}")
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Failed to parse config JSON: {exc}") from exc
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise SystemExit("Config JSON must be a list of run definitions.")
    if not data:
        raise SystemExit("Config file is empty—add at least one run definition.")
    return data


def resolve_path(value: str | Path) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = (REPO_ROOT / path).resolve()
    return path


def run_backtest(run_config: Dict[str, Any]) -> tuple[Dict[str, Any], pd.Series]:
    config = run_config.copy()
    label = config.pop("label", None)
    csv_file = config.pop("csv_file", None)
    if not csv_file:
        raise SystemExit(f"Run {label or config} missing 'csv_file'.")

    data_path = resolve_path(csv_file)
    if not data_path.exists():
        raise SystemExit(f"Data file not found: {data_path}")

    # Instantiate backtest with remaining parameters.
    backtest = SimpleBacktest(str(data_path), **config)
    backtest.load_data()
    backtest.calculate_indicators()
    backtest.generate_signals()
    backtest.run()

    results = backtest.get_results().copy()
    total_pnl = sum(trade.pnl for trade in backtest.trades)
    record = {
        "label": label or data_path.stem,
        "strategy": backtest.strategy,
        "moving_average": backtest.moving_average,
        "fast_window": backtest.fast_window,
        "slow_window": backtest.slow_window,
        "initial_capital": backtest.initial_capital,
        "final_capital": backtest.initial_capital + total_pnl,
    }
    record.update(results)
    return record, backtest.get_equity_curve()


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    runs = load_config(args.config.expanduser().resolve())
    label = args.label or args.config.stem
    summary_path = (
        args.summary_csv.expanduser().resolve()
        if args.summary_csv
        else REPO_ROOT / "results" / "week2" / "comparisons" / f"{label}_summary.csv"
    )
    equity_plot_path = (
        args.equity_plot.expanduser().resolve()
        if args.equity_plot
        else REPO_ROOT / "results" / "week2" / "comparisons" / f"{label}_equity_curve.png"
    )
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    equity_plot_path.parent.mkdir(parents=True, exist_ok=True)

    records: List[Dict[str, Any]] = []
    equity_curves: Dict[str, pd.Series] = {}

    for run in runs:
        metrics, curve = run_backtest(run)
        records.append(metrics)
        equity_curves[metrics["label"]] = curve
        print(f"✓ Completed {metrics['label']} ({metrics['moving_average'].upper()} {metrics['fast_window']}/{metrics['slow_window']})")

    df = pd.DataFrame(records)
    columns = [
        "label",
        "strategy",
        "moving_average",
        "fast_window",
        "slow_window",
        "initial_capital",
        "final_capital",
        "total_trades",
        "winning_trades",
        "losing_trades",
        "win_rate",
        "total_return",
        "max_drawdown",
        "sharpe_ratio",
    ]
    df = df[columns]
    df.sort_values("label", inplace=True)
    df.to_csv(summary_path, index=False)
    print(f"✓ Summary saved to {summary_path}")

    plt.figure(figsize=(12, 6))
    for run_label, series in equity_curves.items():
        series = series.sort_index()
        plt.plot(series.index, series.values, label=run_label, linewidth=1.8)
    plt.title(f"Equity Curve Comparison - {label}")
    plt.xlabel("Date")
    plt.ylabel("Equity ($)")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.legend()
    plt.tight_layout()
    plt.savefig(equity_plot_path, dpi=150)
    plt.close()
    print(f"✓ Combined equity curves saved to {equity_plot_path}")


if __name__ == "__main__":
    main()
