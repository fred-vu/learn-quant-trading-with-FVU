"""
Stock data utilities for downloading, validating, and saving OHLCV datasets.

Example:
    from data_utils.stock_data import (
        download_stock_data,
        save_data,
        validate_ohlc_data,
    )

    df = download_stock_data("NVDA", "2020-01-01", "2025-11-01")
    if validate_ohlc_data(df) is True:
        save_data(df, "data/NVDA.csv")
        print(f"✓ Saved {len(df)} NVDA rows")
"""

from __future__ import annotations

from pathlib import Path
from typing import List, Union

import pandas as pd
import yfinance as yf
from pandas.tseries.holiday import (
    AbstractHolidayCalendar,
    GoodFriday,
    Holiday,
    USLaborDay,
    USMartinLutherKingJr,
    USMemorialDay,
    USPresidentsDay,
    USThanksgivingDay,
    nearest_workday,
)
from pandas.tseries.offsets import CustomBusinessDay

DATA_DIR = Path(__file__).resolve().parents[2] / "data"
REQUIRED_COLUMNS = ["Date", "Open", "High", "Low", "Close", "Volume"]


def is_valid_ticker(symbol: str) -> bool:
    """
    Quick validation to check whether a ticker symbol is likely valid.

    The function fetches a few days of price history; empty results indicate
    an invalid or unsupported ticker.
    """
    cleaned = symbol.upper().strip()
    if not cleaned:
        return False
    try:
        history = yf.Ticker(cleaned).history(period="5d")
    except Exception:
        return False
    return not history.empty


def download_stock_data(symbol: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Download OHLCV data for a symbol between start_date and end_date.

    Args:
        symbol: Stock ticker symbol (e.g., "AAPL").
        start_date: Start date in YYYY-MM-DD format.
        end_date: End date in YYYY-MM-DD format.

    Returns:
        DataFrame containing columns Date, Open, High, Low, Close, Volume.

    Raises:
        SystemExit: if the download fails or returns empty data.
    """
    symbol = symbol.upper().strip()
    try:
        start = pd.to_datetime(start_date, format="%Y-%m-%d")
        end = pd.to_datetime(end_date, format="%Y-%m-%d")
    except ValueError as exc:
        raise SystemExit(f"[ERROR] Invalid date format: {exc}") from exc

    if start >= end:
        raise SystemExit("[ERROR] start_date must be before end_date.")

    try:
        data = yf.download(
            symbol,
            start=start.strftime("%Y-%m-%d"),
            end=end.strftime("%Y-%m-%d"),
            progress=False,
            auto_adjust=False,
        )
    except Exception as exc:
        raise SystemExit(f"[ERROR] Failed to download data: {exc}") from exc

    if data.empty:
        raise SystemExit("[ERROR] No data returned. Check symbol or date range.")

    data.reset_index(inplace=True)
    if isinstance(data.columns, pd.MultiIndex):
        flattened = [
            "_".join(col).strip("_") if isinstance(col, tuple) else str(col)
            for col in data.columns
        ]
        data.columns = flattened

    symbol_suffix = f"_{symbol}"
    rename_map = {}
    for col in data.columns:
        name = str(col)
        if name.endswith(symbol_suffix):
            name = name[: -len(symbol_suffix)]
        rename_map[col] = name
    data.rename(columns=rename_map, inplace=True)

    missing = [col for col in REQUIRED_COLUMNS if col not in data.columns]
    if missing:
        raise SystemExit(f"[ERROR] Missing required columns from download: {missing}")

    return data[REQUIRED_COLUMNS].copy()


class USTradingHolidayCalendar(AbstractHolidayCalendar):
    """U.S. stock market holiday calendar approximation."""

    rules = [
        Holiday("NewYearsDay", month=1, day=1, observance=nearest_workday),
        USMartinLutherKingJr,
        USPresidentsDay,
        GoodFriday,
        USMemorialDay,
        Holiday("Juneteenth", month=6, day=19, observance=nearest_workday, start_date="2022-01-01"),
        Holiday("IndependenceDay", month=7, day=4, observance=nearest_workday),
        USLaborDay,
        USThanksgivingDay,
        Holiday("Christmas", month=12, day=25, observance=nearest_workday),
    ]


TRADING_CALENDAR = USTradingHolidayCalendar()
TRADING_BDAY = CustomBusinessDay(calendar=TRADING_CALENDAR)


def validate_ohlc_data(df: pd.DataFrame) -> Union[bool, List[str]]:
    """
    Validate that OHLCV data satisfies structural constraints.

    Checks include:
        * No missing business days (Mon-Fri, excluding US federal holidays)
        * High >= Open, Close, Low
        * Low <= Open, Close, High
        * Non-negative volume
        * Positive price values

    Args:
        df: DataFrame structured like the output of download_stock_data.

    Returns:
        True if all checks pass, otherwise a list of error messages.
    """
    errors: List[str] = []
    warnings: List[str] = []

    if df.empty:
        errors.append("DataFrame is empty.")
        return errors

    for col in REQUIRED_COLUMNS:
        if col not in df.columns:
            errors.append(f"Missing required column: {col}")
            return errors

    df = df.copy()
    df["Date"] = pd.to_datetime(df["Date"])
    df.sort_values("Date", inplace=True)

    expected_dates = pd.date_range(
        start=df["Date"].min(), end=df["Date"].max(), freq=TRADING_BDAY
    )
    missing_dates = expected_dates.difference(df["Date"].dt.normalize().unique())
    if len(missing_dates) > 0:
        warnings.append(
            f"Missing {len(missing_dates)} trading days "
            f"(e.g., {missing_dates[0].date()}); verify market closures."
        )

    high_issue = df["High"] < df[["Open", "Close", "Low"]].max(axis=1)
    if high_issue.any():
        errors.append(
            f"High column has {int(high_issue.sum())} rows below Open/Close/Low."
        )

    low_issue = df["Low"] > df[["Open", "Close", "High"]].min(axis=1)
    if low_issue.any():
        errors.append(
            f"Low column has {int(low_issue.sum())} rows above Open/Close/High."
        )

    negative_volume = df["Volume"] < 0
    if negative_volume.any():
        errors.append(f"Volume column has {int(negative_volume.sum())} negative rows.")

    price_columns = ["Open", "High", "Low", "Close"]
    non_positive = (df[price_columns] <= 0).any(axis=1)
    if non_positive.any():
        errors.append(
            f"Price columns contain {int(non_positive.sum())} non-positive entries."
        )

    for msg in warnings:
        print(f"[WARN] {msg}")

    if errors:
        for msg in errors:
            print(f"[WARN] {msg}")
        return errors

    return True


def save_data(df: pd.DataFrame, filename: Union[str, Path]) -> None:
    """
    Persist OHLCV data to CSV under the data directory.

    Args:
        df: DataFrame to save.
        filename: Target filename (e.g., "data/AAPL.csv").
    """
    path = Path(filename)
    if not path.is_absolute():
        path = DATA_DIR / path

    path.parent.mkdir(parents=True, exist_ok=True)

    df_to_save = df.copy()
    df_to_save["Date"] = pd.to_datetime(df_to_save["Date"]).dt.strftime("%Y-%m-%d")
    df_to_save.to_csv(path, index=False)
    print(f"[OK] Saved {len(df_to_save)} rows to {path}")


def build_output_filename(symbol: str, start_date: str, end_date: str) -> Path:
    """Return Path for output in the format SYMBOL_end_start.csv."""
    symbol_clean = symbol.upper().strip()
    name = f"{symbol_clean}_{end_date}_{start_date}.csv"
    return DATA_DIR / name


def prompt_user_inputs() -> tuple[str, str, str]:
    """Interactively gather ticker, start date, and end date from the user."""
    symbol = input("Enter ticker symbol (e.g., NVDA): ").strip().upper()
    if not symbol:
        raise SystemExit("[ERROR] Ticker symbol cannot be empty.")
    if not is_valid_ticker(symbol):
        raise SystemExit(f"[ERROR] '{symbol}' is not a recognized ticker or has no data.")

    start_date = input("Enter start date (YYYY-MM-DD): ").strip()
    end_date = input("Enter end date (YYYY-MM-DD): ").strip()
    return symbol, start_date, end_date


def main() -> None:
    print("=== Stock Data Downloader ===")
    symbol, start_date, end_date = prompt_user_inputs()

    data = download_stock_data(symbol, start_date, end_date)
    validation_result = validate_ohlc_data(data)

    if validation_result is True:
        output_path = build_output_filename(symbol, start_date, end_date)
        save_data(data, output_path)
        print(f"✓ Saved {len(data)} {symbol} rows to {output_path.name}")
    else:
        print("[ERROR] Validation failed; data was not saved.")


if __name__ == "__main__":
    main()
