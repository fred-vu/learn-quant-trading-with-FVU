"""
Utility script to run the SimpleBacktest engine on a CSV file.

Example:
    cd python
    python scripts/test_backtest.py --data ../data/AAPL.csv
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict

import sys

PYTHON_DIR = Path(__file__).resolve().parents[1]
if str(PYTHON_DIR) not in sys.path:
    sys.path.insert(0, str(PYTHON_DIR))

from backtester.simple_backtest import SimpleBacktest

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DATA = REPO_ROOT / "data" / "AAPL.csv"
DEFAULT_TRADES = REPO_ROOT / "results" / "week1" / "trades" / "backtest_trades.csv"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run MA crossover backtest.")
    parser.add_argument(
        "--data",
        type=Path,
        default=DEFAULT_DATA,
        help="Path to OHLCV CSV (default: data/AAPL.csv)",
    )
    parser.add_argument(
        "--capital",
        type=float,
        default=10_000.0,
        help="Starting cash for the backtest (default: 10,000).",
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
        "--ma-type",
        choices=["sma", "ema", "wma", "wema"],
        default="sma",
        help="Moving average type for indicators (default: sma).",
    )
    parser.add_argument(
        "--trades-csv",
        type=Path,
        default=DEFAULT_TRADES,
        help="CSV path for exporting individual trades (default: results/backtest_trades.csv).",
    )
    return parser


def format_results(
    results: Dict[str, float],
    initial_capital: float,
    final_capital: float,
    ma_type: str,
    fast_window: int,
    slow_window: int,
) -> str:
    lines = ["=" * 60, "BACKTEST RESULTS", "=" * 60]
    lines.append(f"Initial Capital (USD):............... ${initial_capital:,.2f}")
    lines.append(f"Final Capital (USD):................. ${final_capital:,.2f}")
    lines.append(f"Moving Average Type:................. {ma_type.upper()}")
    lines.append(f"MA Windows (fast/slow):.............. {fast_window}/{slow_window}")
    lines.append("-" * 60)
    for key, value in results.items():
        lines.append(f"{key.replace('_', ' ').title():.<40} {value}")
    lines.append("=" * 60)
    return "\n".join(lines)


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    data_path = args.data.expanduser().resolve()
    trades_path = args.trades_csv.expanduser().resolve()
    trades_path.parent.mkdir(parents=True, exist_ok=True)

    backtest = SimpleBacktest(
        str(data_path),
        initial_capital=args.capital,
        position_size=args.position_size,
        moving_average=args.ma_type,
        fast_window=args.fast_window,
        slow_window=args.slow_window,
    )
    backtest.load_data()
    backtest.calculate_indicators()
    backtest.generate_signals()
    backtest.run()

    results = backtest.get_results()
    initial_capital = float(args.capital)
    total_pnl = sum(trade.pnl for trade in backtest.trades)
    final_capital = initial_capital + total_pnl
    print(
        format_results(
            results,
            initial_capital,
            final_capital,
            args.ma_type,
            args.fast_window,
            args.slow_window,
        )
    )

    backtest.export_trades_to_csv(str(trades_path))
    print(f"Exported {len(backtest.trades)} trades to {trades_path}")


if __name__ == "__main__":
    main()
