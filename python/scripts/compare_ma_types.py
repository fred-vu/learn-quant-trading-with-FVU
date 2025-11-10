"""
Compare multiple moving-average crossover variants on a single dataset.

Example:
    cd python
    python scripts/compare_ma_types.py --data ../data/AAPL.csv
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict, List

import sys

import matplotlib.pyplot as plt
import pandas as pd

PYTHON_DIR = Path(__file__).resolve().parents[1]
if str(PYTHON_DIR) not in sys.path:
    sys.path.insert(0, str(PYTHON_DIR))

from backtester.simple_backtest import SimpleBacktest

MA_CHOICES = ["sma", "ema", "wma", "wema"]
COLOR_MAP = {
    "sma": "#1f77b4",
    "ema": "#2ca02c",
    "wma": "#ff7f0e",
    "wema": "#d62728",
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Compare MA crossover variants.")
    parser.add_argument(
        "--data",
        type=Path,
        default=Path(__file__).resolve().parents[2] / "data" / "AAPL.csv",
        help="Path to OHLCV CSV (default: data/AAPL.csv)",
    )
    parser.add_argument(
        "--ma-types",
        nargs="+",
        choices=MA_CHOICES,
        default=MA_CHOICES,
        help="Moving average types to evaluate (default: all).",
    )
    parser.add_argument(
        "--capital",
        type=float,
        default=10_000.0,
        help="Starting capital for each run (default: 10,000).",
    )
    parser.add_argument(
        "--position-size",
        type=int,
        default=1,
        help="Number of shares per trade (default: 1).",
    )
    parser.add_argument(
        "--fast-window",
        type=int,
        default=20,
        help="Lookback for the fast MA (default: 20).",
    )
    parser.add_argument(
        "--slow-window",
        type=int,
        default=50,
        help="Lookback for the slow MA (default: 50).",
    )
    parser.add_argument(
        "--summary-csv",
        type=Path,
        help="Optional CSV path for metrics summary (default: results/ma_comparison_<label>.csv).",
    )
    parser.add_argument(
        "--equity-plot",
        type=Path,
        help="Optional path for multi-line equity curve plot (default: results/equity_curve_comparison_<label>.png).",
    )
    parser.add_argument(
        "--label",
        type=str,
        help="Custom label used for output filenames (default: data filename stem).",
    )
    return parser


def run_backtest(
    data_path: Path,
    ma_type: str,
    capital: float,
    position_size: int,
    fast_window: int,
    slow_window: int,
) -> tuple[Dict[str, float], pd.Series]:
    backtest = SimpleBacktest(
        str(data_path),
        initial_capital=capital,
        position_size=position_size,
        moving_average=ma_type,
        fast_window=fast_window,
        slow_window=slow_window,
    )
    backtest.load_data()
    backtest.calculate_indicators()
    backtest.generate_signals()
    backtest.run()

    results = backtest.get_results().copy()
    total_pnl = sum(trade.pnl for trade in backtest.trades)
    results.update(
        {
            "ma_type": ma_type.upper(),
            "fast_window": fast_window,
            "slow_window": slow_window,
            "initial_capital": capital,
            "final_capital": capital + total_pnl,
        }
    )
    return results, backtest.get_equity_curve()


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    data_path = args.data.expanduser().resolve()
    if not data_path.exists():
        raise SystemExit(f"Input CSV not found: {data_path}")

    label = args.label or data_path.stem
    repo_root = Path(__file__).resolve().parents[2]
    summary_path = (
        args.summary_csv.expanduser().resolve()
        if args.summary_csv
        else (repo_root / "results" / "week1" / "comparisons" / f"ma_comparison_{label}.csv").resolve()
    )
    equity_plot_path = (
        args.equity_plot.expanduser().resolve()
        if args.equity_plot
        else (repo_root / "results" / "week1" / "equity_curves" / f"equity_curve_comparison_{label}.png").resolve()
    )
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    equity_plot_path.parent.mkdir(parents=True, exist_ok=True)

    records: List[Dict[str, float]] = []
    equity_curves: Dict[str, pd.Series] = {}

    for ma in args.ma_types:
        print(f"Running {ma.upper()} crossover...")
        metrics, curve = run_backtest(
            data_path,
            ma,
            args.capital,
            args.position_size,
            args.fast_window,
            args.slow_window,
        )
        records.append(metrics)
        equity_curves[ma.upper()] = curve

    df = pd.DataFrame(records)
    desired_columns = [
        "ma_type",
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
    df = df[desired_columns]
    df.sort_values("ma_type", inplace=True)
    df.to_csv(summary_path, index=False)
    print(f"✓ Summary saved to {summary_path}")

    plt.figure(figsize=(12, 6))
    for ma_label, series in equity_curves.items():
        series = series.sort_index()
        plt.plot(
            series.index,
            series.values,
            label=ma_label,
            linewidth=1.8,
            color=COLOR_MAP.get(ma_label.lower(), None),
        )
    plt.title(f"Equity Curve Comparison - {label} ({args.fast_window}/{args.slow_window})")
    plt.xlabel("Date")
    plt.ylabel("Equity ($)")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.legend()
    plt.tight_layout()
    plt.savefig(equity_plot_path, dpi=150)
    plt.close()
    print(f"✓ Equity curves saved to {equity_plot_path}")


if __name__ == "__main__":
    main()
