"""
Utility script to fetch daily crypto OHLCV data (e.g., BTC-USD) and save to CSV.

Unlike equities, crypto markets trade 24/7. This helper relies on Yahoo Finance
via yfinance, so you can choose either a rolling `period` (e.g., 3y) or a fixed
start/end range.
"""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd
import yfinance as yf

DATA_DIR = Path(__file__).resolve().parent
DEFAULT_SYMBOL = "BTC-USD"
DEFAULT_PERIOD = "3y"
DEFAULT_INTERVAL = "1d"
REQUIRED_COLUMNS: List[str] = ["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Download crypto OHLCV data via yfinance.")
    parser.add_argument(
        "--symbol",
        default=DEFAULT_SYMBOL,
        help="Crypto ticker symbol, e.g., BTC-USD, ETH-USD (default: BTC-USD).",
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--period",
        default=None,
        help="Lookback period (e.g., 1y, 5y, max). Mutually exclusive with --start/--end.",
    )
    group.add_argument(
        "--start",
        help="Start date YYYY-MM-DD. Requires --end if provided.",
    )
    parser.add_argument(
        "--end",
        help="End date YYYY-MM-DD (ignored when --period is used). Defaults to today.",
    )
    parser.add_argument(
        "--interval",
        default=DEFAULT_INTERVAL,
        choices=["1h", "2h", "4h", "1d", "1wk"],
        help="Sampling interval (default: 1d).",
    )
    parser.add_argument(
        "--outfile",
        help="Optional output CSV filename (default: data/{symbol}_{interval}.csv).",
    )
    return parser


def validate_range(start: Optional[str], end: Optional[str]) -> Tuple[str, str]:
    """Validate that the provided ISO dates are in order."""
    if not start or not end:
        raise SystemExit("[ERROR] --start and --end must be provided together.")

    try:
        start_date = date.fromisoformat(start)
        end_date = date.fromisoformat(end)
    except ValueError as exc:
        raise SystemExit(f"[ERROR] Invalid date format: {exc}") from exc

    if start_date >= end_date:
        raise SystemExit("[ERROR] start must be before end.")

    return start_date.isoformat(), end_date.isoformat()


def normalize_columns(df: pd.DataFrame, symbol: str) -> pd.DataFrame:
    """Ensure the output contains the standard OHLCV columns with Date index."""
    df = df.copy()
    if "Datetime" in df.columns:
        df.rename(columns={"Datetime": "Date"}, inplace=True)

    # Flatten multi-index (happens when ticker suffix is appended).
    if isinstance(df.columns, pd.MultiIndex):
        flattened = ["_".join(filter(None, map(str, col))).strip("_") for col in df.columns]
        df.columns = flattened

    suffix = f"_{symbol}"
    rename_map: Dict[str, str] = {}
    for col in df.columns:
        name = str(col)
        if name.endswith(suffix):
            name = name[: -len(suffix)]
        rename_map[col] = name
    df.rename(columns=rename_map, inplace=True)

    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise SystemExit(f"[ERROR] Missing expected columns: {missing}")

    return df[REQUIRED_COLUMNS].copy()


def download_crypto_data(
    symbol: str,
    *,
    period: Optional[str],
    start: Optional[str],
    end: Optional[str],
    interval: str,
) -> pd.DataFrame:
    """Download crypto OHLCV data using yfinance."""
    kwargs: Dict[str, str] = {"interval": interval, "progress": False, "auto_adjust": False}
    if period:
        kwargs["period"] = period
        print(f"[INFO] Downloading {symbol} for period={period}, interval={interval}")
    else:
        range_start, range_end = validate_range(start, end)
        kwargs["start"] = range_start
        kwargs["end"] = range_end
        print(f"[INFO] Downloading {symbol} from {range_start} to {range_end} ({interval})")

    data = yf.download(symbol, **kwargs)
    if data.empty:
        raise SystemExit("[ERROR] No data returned. Check symbol or parameters.")
    data.reset_index(inplace=True)
    return normalize_columns(data, symbol)


def save_csv(df: pd.DataFrame, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    start = df["Date"].iloc[0]
    end = df["Date"].iloc[-1]
    print(f"[OK] Saved {len(df):,} rows to {output_path} ({start} → {end})")


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    period = args.period
    if not period and not args.start:
        period = DEFAULT_PERIOD

    outfile = (
        Path(args.outfile)
        if args.outfile
        else DATA_DIR / f"{args.symbol.upper().replace('-', '_')}_{args.interval}.csv"
    )

    df = download_crypto_data(
        args.symbol.upper(),
        period=period,
        start=args.start,
        end=args.end or date.today().isoformat(),
        interval=args.interval,
    )
    save_csv(df, outfile)


if __name__ == "__main__":
    main()
