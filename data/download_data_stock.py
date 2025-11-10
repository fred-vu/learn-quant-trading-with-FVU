"""
Utility script to fetch historical equity data and persist it to CSV.

Defaults to downloading 5 years of AAPL data, but you can override the
symbol/date range via CLI flags:

    python data/download_data.py --symbol MSFT --start 2018-01-01 --end 2023-01-01
"""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
from typing import Tuple

import pandas as pd
import yfinance as yf

DATA_DIR = Path(__file__).resolve().parent
DEFAULT_SYMBOL = "AAPL"
DEFAULT_START = "2020-01-01"
DEFAULT_END = "2025-01-01"
REQUIRED_COLUMNS = ["Date", "Open", "High", "Low", "Close", "Volume"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Download historical OHLCV data.")
    parser.add_argument(
        "--symbol", default=DEFAULT_SYMBOL, help="Ticker symbol (default: AAPL)"
    )
    parser.add_argument(
        "--start",
        default=DEFAULT_START,
        help="Start date YYYY-MM-DD (default: 2020-01-01)",
    )
    parser.add_argument(
        "--end", default=DEFAULT_END, help="End date YYYY-MM-DD (default: 2025-01-01)"
    )
    parser.add_argument(
        "--outfile",
        default=None,
        help="Optional output CSV filename. Defaults to data/{symbol}.csv",
    )
    return parser.parse_args()


def validate_dates(start: str, end: str) -> Tuple[str, str]:
    """Ensure dates are valid ISO strings and start <= end."""
    try:
        start_date = date.fromisoformat(start)
        end_date = date.fromisoformat(end)
    except ValueError as exc:
        raise SystemExit(f"[ERROR] Invalid date format: {exc}") from exc

    if start_date >= end_date:
        raise SystemExit("[ERROR] Start date must be before end date.")

    return start_date.isoformat(), end_date.isoformat()


def download_history(symbol: str, start: str, end: str) -> pd.DataFrame:
    """Download historical data using yfinance."""
    print(f"[INFO] Downloading {symbol} from {start} to {end} ...")
    data = yf.download(symbol, start=start, end=end, progress=False, auto_adjust=False)
    if data.empty:
        raise SystemExit("[ERROR] No data returned. Check symbol or date range.")
    data.reset_index(inplace=True)
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = [
            "_".join(filter(None, map(str, col))).strip("_")
            for col in data.columns.to_list()
        ]
    suffix = f"_{symbol}"
    rename_map = {}
    for col in data.columns:
        name = str(col)
        if name.endswith(suffix):
            name = name[: -len(suffix)]
        rename_map[col] = name
    data.rename(columns=rename_map, inplace=True)

    missing = [col for col in REQUIRED_COLUMNS if col not in data.columns]
    if missing:
        raise SystemExit(f"[ERROR] Missing expected columns: {missing}")

    return data[REQUIRED_COLUMNS].copy()


def save_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    print(f"[OK] Saved {len(df):,} rows to {path}")


def main() -> None:
    args = parse_args()
    start, end = validate_dates(args.start, args.end)
    outfile = (
        Path(args.outfile) if args.outfile else DATA_DIR / f"{args.symbol.upper()}.csv"
    )

    df = download_history(args.symbol.upper(), start, end)
    save_csv(df, outfile)

    columns_display = ", ".join(map(str, df.columns))
    first_date = df["Date"].iloc[0]
    last_date = df["Date"].iloc[-1]
    print(f"[INFO] Date range: {first_date} → {last_date} | Columns: {columns_display}")


if __name__ == "__main__":
    main()
