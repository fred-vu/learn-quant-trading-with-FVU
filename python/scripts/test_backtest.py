"""
Utility script to run the SimpleBacktest engine on a CSV file.

Example:
    cd python
    python scripts/test_backtest.py --data ../data/AAPL.csv
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List

import sys

PYTHON_DIR = Path(__file__).resolve().parents[1]
if str(PYTHON_DIR) not in sys.path:
    sys.path.insert(0, str(PYTHON_DIR))

from backtester.simple_backtest import SimpleBacktest

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DATA = REPO_ROOT / "data" / "AAPL.csv"
DEFAULT_TRADES = REPO_ROOT / "results" / "week1" / "trades" / "backtest_trades.csv"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run backtests with MA/RSI/MACD/Donchian strategies.")
    parser.add_argument(
        "--config",
        type=Path,
        help="Optional JSON config file providing argument values.",
    )
    parser.add_argument(
        "--strategy",
        choices=["ma_crossover", "rsi_bollinger", "macd", "donchian"],
        default="ma_crossover",
        help="Strategy to run (default: ma_crossover).",
    )
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
        "--use-ma-rsi-filter",
        action="store_true",
        help="Enable RSI gating for MA crossover strategies (requires RSI between bounds).",
    )
    parser.add_argument(
        "--ma-rsi-lower",
        type=float,
        default=40.0,
        help="Lower RSI bound for MA filter (default: 40).",
    )
    parser.add_argument(
        "--ma-rsi-upper",
        type=float,
        default=70.0,
        help="Upper RSI bound for MA filter (default: 70).",
    )
    parser.add_argument(
        "--use-ma-rsi-exit",
        action="store_true",
        help="Exit long MA trades if RSI exceeds the exit threshold.",
    )
    parser.add_argument(
        "--ma-rsi-exit-threshold",
        type=float,
        default=80.0,
        help="RSI level that triggers MA exit when --use-ma-rsi-exit is set (default: 80).",
    )
    parser.add_argument(
        "--use-atr-stop",
        action="store_true",
        help="Enable ATR(14) trailing stop for MA/MACD/Donchian strategies.",
    )
    parser.add_argument(
        "--atr-period",
        type=int,
        default=14,
        help="ATR period for trailing stops (default: 14).",
    )
    parser.add_argument(
        "--atr-multiplier",
        type=float,
        default=3.0,
        help="ATR multiplier for trailing stops (default: 3.0).",
    )
    parser.add_argument(
        "--use-atr-vol-filter",
        action="store_true",
        help="Require ATR%% of price to exceed threshold before entering trades.",
    )
    parser.add_argument(
        "--atr-vol-threshold",
        type=float,
        default=0.02,
        help="ATR percentage threshold (e.g., 0.02 for 2%%) for volatility gating.",
    )
    parser.add_argument(
        "--macd-fast",
        type=int,
        default=12,
        help="MACD fast EMA window (default: 12).",
    )
    parser.add_argument(
        "--macd-slow",
        type=int,
        default=26,
        help="MACD slow EMA window (default: 26).",
    )
    parser.add_argument(
        "--macd-signal",
        type=int,
        default=9,
        help="MACD signal EMA window (default: 9).",
    )
    parser.add_argument(
        "--donchian-window",
        type=int,
        default=20,
        help="Donchian channel breakout window (default: 20).",
    )
    parser.add_argument(
        "--allow-short",
        dest="allow_short",
        action="store_true",
        help="Enable short selling (default: auto based on strategy).",
    )
    parser.add_argument(
        "--no-allow-short",
        dest="allow_short",
        action="store_false",
        help="Disable short selling explicitly.",
    )
    parser.add_argument(
        "--trades-csv",
        type=Path,
        default=DEFAULT_TRADES,
        help="CSV path for exporting individual trades (default: results/backtest_trades.csv).",
    )
    parser.add_argument(
        "--rsi-period",
        type=int,
        default=14,
        help="RSI period for rsi_bollinger strategy (default: 14).",
    )
    parser.add_argument(
        "--bollinger-window",
        type=int,
        default=20,
        help="Bollinger band window for rsi_bollinger strategy (default: 20).",
    )
    parser.add_argument(
        "--bollinger-std",
        type=float,
        default=2.0,
        help="Bollinger std multiplier for rsi_bollinger strategy (default: 2.0).",
    )
    parser.add_argument(
        "--rsi-long-entry",
        type=float,
        default=25.0,
        help="RSI threshold (<=) to open longs (default: 25).",
    )
    parser.add_argument(
        "--rsi-long-exit",
        type=float,
        default=55.0,
        help="RSI threshold (>=) to close longs (default: 55).",
    )
    parser.add_argument(
        "--rsi-short-entry",
        type=float,
        default=75.0,
        help="RSI threshold (>=) to open shorts (default: 75).",
    )
    parser.add_argument(
        "--rsi-short-exit",
        type=float,
        default=45.0,
        help="RSI threshold (<=) to close shorts (default: 45).",
    )
    parser.set_defaults(allow_short=None)
    return parser


def load_config(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise SystemExit(f"Config file not found: {path}")
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Failed to parse config JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise SystemExit("Config file must contain a JSON object with argument names.")
    return data


def apply_config_overrides(args: argparse.Namespace, parser: argparse.ArgumentParser, config: Dict[str, Any]) -> None:
    for key, value in config.items():
        if not hasattr(args, key):
            continue
        current_value = getattr(args, key)
        default_value = parser.get_default(key)
        # Skip if user already supplied a CLI override.
        if current_value != default_value:
            continue
        if isinstance(default_value, Path):
            value = Path(value)
        setattr(args, key, value)


def format_results(
    results: Dict[str, float],
    initial_capital: float,
    final_capital: float,
    strategy: str,
    detail_lines: List[str],
) -> str:
    lines = ["=" * 60, "BACKTEST RESULTS", "=" * 60]
    lines.append(f"Initial Capital (USD):............... ${initial_capital:,.2f}")
    lines.append(f"Final Capital (USD):................. ${final_capital:,.2f}")
    lines.append(f"Strategy:............................ {strategy.replace('_', ' ').title()}")
    for detail in detail_lines:
        lines.append(detail)
    lines.append("-" * 60)
    for key, value in results.items():
        lines.append(f"{key.replace('_', ' ').title():.<40} {value}")
    lines.append("=" * 60)
    return "\n".join(lines)


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if args.config:
        config_values = load_config(args.config.expanduser().resolve())
        apply_config_overrides(args, parser, config_values)

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
        strategy=args.strategy,
        allow_short=args.allow_short,
        rsi_period=args.rsi_period,
        bollinger_window=args.bollinger_window,
        bollinger_std=args.bollinger_std,
        rsi_long_entry=args.rsi_long_entry,
        rsi_long_exit=args.rsi_long_exit,
        rsi_short_entry=args.rsi_short_entry,
        rsi_short_exit=args.rsi_short_exit,
        use_rsi_filter=args.use_ma_rsi_filter,
        ma_rsi_lower=args.ma_rsi_lower,
        ma_rsi_upper=args.ma_rsi_upper,
        use_rsi_exit=args.use_ma_rsi_exit,
        rsi_exit_threshold=args.ma_rsi_exit_threshold,
        macd_fast=args.macd_fast,
        macd_slow=args.macd_slow,
        macd_signal=args.macd_signal,
        donchian_window=args.donchian_window,
        use_atr_trailing_stop=args.use_atr_stop,
        atr_period=args.atr_period,
        atr_multiplier=args.atr_multiplier,
        use_atr_volatility_filter=args.use_atr_vol_filter,
        atr_volatility_threshold=args.atr_vol_threshold,
    )
    backtest.load_data()
    backtest.calculate_indicators()
    backtest.generate_signals()
    backtest.run()

    results = backtest.get_results()
    initial_capital = float(args.capital)
    total_pnl = sum(trade.pnl for trade in backtest.trades)
    final_capital = initial_capital + total_pnl
    if args.strategy == "ma_crossover":
        detail_lines = [
            f"Moving Average Type:................. {args.ma_type.upper()}",
            f"MA Windows (fast/slow):.............. {args.fast_window}/{args.slow_window}",
        ]
        if args.use_ma_rsi_filter:
            detail_lines.append(
                f"MA RSI Filter Range:................. {args.ma_rsi_lower}-{args.ma_rsi_upper}"
            )
        if args.use_ma_rsi_exit:
            detail_lines.append(
                f"MA RSI Exit Threshold:................ {args.ma_rsi_exit_threshold}"
            )
        if args.use_atr_stop:
            detail_lines.append(
                f"ATR Trailing Stop (period/mult):..... {args.atr_period}/{args.atr_multiplier}"
            )
        if args.use_atr_vol_filter:
            detail_lines.append(
                f"ATR Volatility Filter (threshold):... {args.atr_vol_threshold:.4f}"
            )
    elif args.strategy == "macd":
        detail_lines = [
            f"MACD Windows (fast/slow/signal):...... {args.macd_fast}/{args.macd_slow}/{args.macd_signal}",
            f"Short Selling Enabled:............... {'Yes' if backtest.allow_short else 'No'}",
        ]
        if args.use_atr_stop:
            detail_lines.append(
                f"ATR Trailing Stop (period/mult):..... {args.atr_period}/{args.atr_multiplier}"
            )
    elif args.strategy == "donchian":
        detail_lines = [
            f"Donchian Window:...................... {args.donchian_window}",
            f"Short Selling Enabled:............... {'Yes' if backtest.allow_short else 'No'}",
        ]
        if args.use_atr_stop:
            detail_lines.append(
                f"ATR Trailing Stop (period/mult):..... {args.atr_period}/{args.atr_multiplier}"
            )
    else:
        detail_lines = [
            f"RSI Period:.......................... {args.rsi_period}",
            f"RSI Long Entry/Exit:................. {args.rsi_long_entry}/{args.rsi_long_exit}",
            f"RSI Short Entry/Exit:................ {args.rsi_short_entry}/{args.rsi_short_exit}",
            f"Bollinger Window/Std:................ {args.bollinger_window}/{args.bollinger_std}",
            f"Short Selling Enabled:............... {'Yes' if backtest.allow_short else 'No'}",
        ]
    print(
        format_results(
            results,
            initial_capital,
            final_capital,
            args.strategy,
            detail_lines,
        )
    )

    backtest.export_trades_to_csv(str(trades_path))
    print(f"Exported {len(backtest.trades)} trades to {trades_path}")


if __name__ == "__main__":
    main()
