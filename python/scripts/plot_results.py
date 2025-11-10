"""
Plot cumulative PnL from backtest trade history.

Example:
    cd python
    python scripts/plot_results.py --input ../results/backtest_trades.csv
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = REPO_ROOT / "results" / "week1" / "trades" / "backtest_trades.csv"
DEFAULT_OUTPUT = REPO_ROOT / "results" / "week1" / "equity_curves" / "equity_curve.png"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Plot cumulative PnL from trade history.")
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT,
        help="CSV file with trade history (default: results/backtest_trades.csv).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Target path for saved figure (default: results/equity_curve.png).",
    )
    parser.add_argument(
        "--label",
        type=str,
        help="Optional label/ticker for plot title (default: derived from input filename).",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    input_path = args.input.expanduser().resolve()
    output_path = args.output.expanduser().resolve()
    if not input_path.exists():
        raise SystemExit(f"Trade CSV not found: {input_path}")

    trades = pd.read_csv(input_path, parse_dates=["entry_date", "exit_date"])
    if trades.empty:
        raise SystemExit("Trade CSV is empty—run the backtest first.")

    trades["cumulative_pnl"] = trades["pnl"].cumsum()
    label = args.label or input_path.stem.replace("backtest_trades_", "").upper()

    plt.figure(figsize=(12, 6))
    plt.plot(trades["exit_date"], trades["cumulative_pnl"], marker="o")
    plt.title(f"Backtest Equity Curve - {label}")
    plt.xlabel("Exit Date")
    plt.ylabel("Cumulative PnL ($)")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.tight_layout()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=150)
    plt.close()
    print(f"✓ Chart saved to {output_path}")


if __name__ == "__main__":
    main()
