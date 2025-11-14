"""
Simple backtest engine with configurable strategies.

Implements the Week 1 requirement for a lightweight engine that:
    * Loads OHLCV data from CSV.
    * Calculates indicators (MA crossovers, RSI + Bollinger signals, etc.).
    * Generates buy/sell/hold signals.
    * Simulates trades (long-only or long/short) and records trade statistics.
    * Exposes aggregate metrics (total return, drawdown, Sharpe, etc.).
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

import numpy as np
import pandas as pd

REQUIRED_COLUMNS = {"Date", "Close"}


@dataclass
class Trade:
    """Container representing a completed trade."""

    entry_date: pd.Timestamp
    entry_price: float
    exit_date: pd.Timestamp
    exit_price: float
    quantity: int

    @property
    def pnl(self) -> float:
        return (self.exit_price - self.entry_price) * self.quantity

    @property
    def pnl_percent(self) -> float:
        return (self.pnl / (self.entry_price * self.quantity)) * 100 if self.entry_price else 0.0

    @property
    def duration_days(self) -> int:
        return (self.exit_date - self.entry_date).days if self.exit_date and self.entry_date else 0


class SimpleBacktest:
    """Moving-average crossover or RSI+Bollinger mean-reversion backtest."""

    def __init__(
        self,
        csv_file: str,
        initial_capital: float = 10_000.0,
        position_size: int = 1,
        moving_average: str = "sma",
        fast_window: int = 20,
        slow_window: int = 50,
        strategy: str = "ma_crossover",
        allow_short: Optional[bool] = None,
        rsi_period: int = 14,
        bollinger_window: int = 20,
        bollinger_std: float = 2.0,
        rsi_long_entry: float = 25.0,
        rsi_long_exit: float = 55.0,
        rsi_short_entry: float = 75.0,
        rsi_short_exit: float = 45.0,
    ) -> None:
        """
        Args:
            csv_file: Path to a CSV file containing Date and Close columns.
            initial_capital: Starting cash balance.
            position_size: Number of shares per trade.
            moving_average: One of "sma", "ema", "wma", "wema" for indicator calculation.
            fast_window: Lookback window for the fast moving average.
            slow_window: Lookback window for the slow moving average.
            strategy: "ma_crossover" or "rsi_bollinger".
            allow_short: Whether shorts are allowed. Defaults to True for RSI strategy, False otherwise.
            rsi_period: Lookback window for RSI (used in RSI strategy).
            bollinger_window: Window for Bollinger band mid-line.
            bollinger_std: Standard deviation multiple for Bollinger bands.
            rsi_long_entry: RSI threshold for opening longs.
            rsi_long_exit: RSI threshold for closing longs.
            rsi_short_entry: RSI threshold for opening shorts.
            rsi_short_exit: RSI threshold for closing shorts.
        """
        self.csv_file = csv_file
        self.initial_capital = float(initial_capital)
        self.position_size = int(position_size)
        self.moving_average = moving_average.lower()
        if self.moving_average not in {"sma", "ema", "wma", "wema"}:
            raise ValueError("moving_average must be 'sma', 'ema', 'wma', or 'wema'.")
        self.fast_window = int(fast_window)
        self.slow_window = int(slow_window)
        if self.fast_window <= 0 or self.slow_window <= 0:
            raise ValueError("fast_window and slow_window must be positive integers.")
        if self.fast_window >= self.slow_window:
            raise ValueError("fast_window must be smaller than slow_window.")
        prefix = self.moving_average.upper()
        self.fast_col = f"{prefix}{self.fast_window}"
        self.slow_col = f"{prefix}{self.slow_window}"
        self.strategy = strategy.lower()
        if self.strategy not in {"ma_crossover", "rsi_bollinger"}:
            raise ValueError("strategy must be 'ma_crossover' or 'rsi_bollinger'.")
        if allow_short is None:
            self.allow_short = self.strategy == "rsi_bollinger"
        else:
            self.allow_short = bool(allow_short)
        self.rsi_period = int(rsi_period)
        self.bollinger_window = int(bollinger_window)
        if self.bollinger_window <= 0:
            raise ValueError("bollinger_window must be a positive integer.")
        self.bollinger_std = float(bollinger_std)
        if self.bollinger_std <= 0:
            raise ValueError("bollinger_std must be positive.")
        self.rsi_long_entry = float(rsi_long_entry)
        self.rsi_long_exit = float(rsi_long_exit)
        self.rsi_short_entry = float(rsi_short_entry)
        self.rsi_short_exit = float(rsi_short_exit)
        self.rsi_col = f"RSI_{self.rsi_period}"
        self.bb_mid_col = f"BB_MID_{self.bollinger_window}"
        self.bb_upper_col = f"BB_UPPER_{self.bollinger_window}"
        self.bb_lower_col = f"BB_LOWER_{self.bollinger_window}"
        self.data: pd.DataFrame = pd.DataFrame()
        self.trades: List[Trade] = []
        self._equity_curve: pd.Series = pd.Series(dtype=float)
        self._results: Dict[str, float] = {}

    # ------------------------------------------------------------------ #
    # Data preparation
    # ------------------------------------------------------------------ #
    def load_data(self) -> None:
        """Load CSV into a DataFrame, validate columns, and sort by date."""
        path = Path(self.csv_file)
        if not path.exists():
            raise FileNotFoundError(f"CSV file not found: {self.csv_file}")

        df = pd.read_csv(path)
        missing = REQUIRED_COLUMNS.difference(df.columns)
        if missing:
            raise ValueError(f"CSV missing required columns: {missing}")

        df["Date"] = pd.to_datetime(df["Date"])
        df.sort_values("Date", inplace=True)
        df.reset_index(drop=True, inplace=True)

        self.data = df

    def calculate_indicators(self) -> None:
        """Add fast/slow MA columns based on the configured windows."""
        self._ensure_data_loaded()
        close = self.data["Close"]
        if self.strategy == "ma_crossover":
            self.data[self.fast_col] = self._compute_moving_average(close, self.fast_window)
            self.data[self.slow_col] = self._compute_moving_average(close, self.slow_window)
        elif self.strategy == "rsi_bollinger":
            self.data[self.bb_mid_col] = close.rolling(
                window=self.bollinger_window, min_periods=self.bollinger_window
            ).mean()
            rolling_std = close.rolling(
                window=self.bollinger_window, min_periods=self.bollinger_window
            ).std(ddof=0)
            self.data[self.bb_upper_col] = self.data[self.bb_mid_col] + self.bollinger_std * rolling_std
            self.data[self.bb_lower_col] = self.data[self.bb_mid_col] - self.bollinger_std * rolling_std
            self.data[self.rsi_col] = self._compute_rsi(close, self.rsi_period)
        else:
            raise RuntimeError(f"Unsupported strategy: {self.strategy}")

    def generate_signals(self) -> None:
        """Create buy/sell/hold signals based on SMA crossovers."""
        self._ensure_indicators()
        if self.strategy == "ma_crossover":
            fast = self.data[self.fast_col]
            slow = self.data[self.slow_col]
            signal = np.where(fast > slow, 1, -1)
            signal = np.where(fast.isna() | slow.isna(), 0, signal)
            self.data["signal"] = signal
        else:
            self.data["signal"] = self._generate_rsi_bollinger_signals()

    # ------------------------------------------------------------------ #
    # Backtest execution
    # ------------------------------------------------------------------ #
    def run(self) -> None:
        """Simulate trades using the generated signals."""
        self._ensure_signals()
        cash = self.initial_capital
        position = 0
        entry_price: Optional[float] = None
        entry_date: Optional[pd.Timestamp] = None

        equity_values: List[float] = []
        equity_dates: List[pd.Timestamp] = []

        for _, row in self.data.iterrows():
            price = float(row["Close"])
            date = pd.Timestamp(row["Date"])
            signal = int(row["signal"])

            if signal > 0:
                # Close short positions before entering long.
                if position < 0:
                    trade = self._close_trade(price, date, entry_price, entry_date, position)
                    self.trades.append(trade)
                    cash += price * position
                    position = 0
                    entry_price = None
                    entry_date = None
                if position == 0:
                    position = self.position_size
                    entry_price = price
                    entry_date = date
                    cash -= price * position

            elif signal < 0:
                # Exit any open long.
                if position > 0:
                    trade = self._close_trade(price, date, entry_price, entry_date, position)
                    self.trades.append(trade)
                    cash += price * position
                    position = 0
                    entry_price = None
                    entry_date = None
                # Enter short if allowed and currently flat.
                if self.allow_short and position == 0:
                    position = -self.position_size
                    entry_price = price
                    entry_date = date
                    cash -= price * position  # subtracting a negative adds cash

            else:
                # Signal to be flat: close any open position.
                if position != 0:
                    trade = self._close_trade(price, date, entry_price, entry_date, position)
                    self.trades.append(trade)
                    cash += price * position
                    position = 0
                    entry_price = None
                    entry_date = None

            equity = cash + position * price
            equity_values.append(equity)
            equity_dates.append(date)

        # Close any open position at the final price.
        if position != 0 and entry_price is not None and entry_date is not None:
            last_price = float(self.data.iloc[-1]["Close"])
            last_date = pd.Timestamp(self.data.iloc[-1]["Date"])
            trade = self._close_trade(last_price, last_date, entry_price, entry_date, position)
            self.trades.append(trade)
            cash += last_price * position
            equity_values[-1] = cash  # update final equity

        self._equity_curve = pd.Series(equity_values, index=equity_dates, name="equity")
        self._results = self._calculate_metrics()

    def _close_trade(
        self,
        exit_price: float,
        exit_date: pd.Timestamp,
        entry_price: Optional[float],
        entry_date: Optional[pd.Timestamp],
        quantity: int,
    ) -> Trade:
        if entry_price is None or entry_date is None:
            raise ValueError("Attempted to close a trade that was never opened.")
        return Trade(
            entry_date=entry_date,
            entry_price=entry_price,
            exit_date=exit_date,
            exit_price=exit_price,
            quantity=quantity,
        )

    # ------------------------------------------------------------------ #
    # Metrics
    # ------------------------------------------------------------------ #
    def _calculate_metrics(self) -> Dict[str, float]:
        if self._equity_curve.empty:
            return {}

        equity = self._equity_curve
        returns = equity.pct_change().dropna()

        total_return = float(((equity.iloc[-1] / equity.iloc[0]) - 1) * 100)
        winners = sum(1 for trade in self.trades if trade.pnl > 0)
        losers = sum(1 for trade in self.trades if trade.pnl < 0)
        total_trades = len(self.trades)
        win_rate = (winners / total_trades) * 100 if total_trades else 0.0

        rolling_max = equity.cummax()
        drawdown = equity / rolling_max - 1
        max_drawdown = float(drawdown.min() * 100) if not drawdown.empty else 0.0

        sharpe_ratio = 0.0
        if len(returns) > 1 and returns.std(ddof=0) != 0:
            sharpe_ratio = (returns.mean() / returns.std(ddof=0)) * np.sqrt(252)

        return {
            "total_trades": total_trades,
            "winning_trades": winners,
            "losing_trades": losers,
            "win_rate": round(win_rate, 2),
            "total_return": round(total_return, 2),
            "max_drawdown": round(max_drawdown, 2),
            "sharpe_ratio": round(float(sharpe_ratio), 2),
        }

    def _compute_moving_average(self, series: pd.Series, window: int) -> pd.Series:
        """Compute the configured moving-average type for a given window."""
        if self.moving_average == "sma":
            return series.rolling(window=window, min_periods=window).mean()
        if self.moving_average == "ema":
            return series.ewm(span=window, adjust=False, min_periods=window).mean()
        if self.moving_average == "wma":
            return self._weighted_moving_average(series, window)
        if self.moving_average == "wema":
            ema = series.ewm(span=window, adjust=False, min_periods=window).mean()
            return self._weighted_moving_average(ema, window)
        raise ValueError(f"Unsupported moving average type: {self.moving_average}")

    @staticmethod
    def _weighted_moving_average(series: pd.Series, window: int) -> pd.Series:
        """Return linearly weighted moving average (heavier weight on recent data)."""
        weights = np.arange(1, window + 1, dtype=float)
        weight_sum = weights.sum()
        return series.rolling(window=window, min_periods=window).apply(
            lambda values: np.dot(values, weights) / weight_sum,
            raw=True,
        )

    @staticmethod
    def _compute_rsi(series: pd.Series, period: int) -> pd.Series:
        """Compute the Relative Strength Index."""
        delta = series.diff()
        gain = delta.clip(lower=0.0)
        loss = -delta.clip(upper=0.0)
        avg_gain = gain.ewm(alpha=1 / period, adjust=False, min_periods=period).mean()
        avg_loss = loss.ewm(alpha=1 / period, adjust=False, min_periods=period).mean()
        rs = avg_gain / avg_loss.replace(0, np.nan)
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def _generate_rsi_bollinger_signals(self) -> pd.Series:
        """Generate +/-1/0 signals based on RSI and Bollinger band rules."""
        signals: List[int] = []
        position = 0
        for _, row in self.data.iterrows():
            price = row["Close"]
            rsi = row[self.rsi_col]
            mid = row[self.bb_mid_col]
            lower = row[self.bb_lower_col]
            upper = row[self.bb_upper_col]
            entry_long = (
                pd.notna(rsi)
                and pd.notna(lower)
                and rsi <= self.rsi_long_entry
                and price <= lower
            )
            entry_short = (
                pd.notna(rsi)
                and pd.notna(upper)
                and rsi >= self.rsi_short_entry
                and price >= upper
            )
            exit_long = position == 1 and (
                (pd.notna(rsi) and rsi >= self.rsi_long_exit)
                or (pd.notna(mid) and price >= mid)
            )
            exit_short = position == -1 and (
                (pd.notna(rsi) and rsi <= self.rsi_short_exit)
                or (pd.notna(mid) and price <= mid)
            )

            if position == 0:
                if entry_long:
                    position = 1
                elif entry_short and self.allow_short:
                    position = -1
            elif position == 1:
                if exit_long:
                    if entry_short and self.allow_short:
                        position = -1
                    else:
                        position = 0
            elif position == -1:
                if exit_short:
                    if entry_long:
                        position = 1
                    else:
                        position = 0
            signals.append(position)
        return pd.Series(signals, index=self.data.index, dtype=int)

    def get_results(self) -> Dict[str, float]:
        """Return the metrics dictionary."""
        if not self._results:
            raise RuntimeError("Backtest has not been run yet.")
        return self._results

    def get_equity_curve(self) -> pd.Series:
        """Return a copy of the equity curve Series."""
        if self._equity_curve.empty:
            raise RuntimeError("Backtest has not been run yet.")
        return self._equity_curve.copy()

    def export_trades_to_csv(self, filename: str) -> None:
        """Export trade history to CSV."""
        if not self.trades:
            raise RuntimeError("No trades available to export.")

        rows = [
            {
                "entry_date": trade.entry_date.date(),
                "entry_price": trade.entry_price,
                "exit_date": trade.exit_date.date(),
                "exit_price": trade.exit_price,
                "quantity": trade.quantity,
                "pnl": trade.pnl,
                "pnl_percent": trade.pnl_percent,
                "trade_duration_days": trade.duration_days,
            }
            for trade in self.trades
        ]
        df = pd.DataFrame(rows)
        output_path = Path(filename)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_path, index=False)

    # ------------------------------------------------------------------ #
    # Validation helpers
    # ------------------------------------------------------------------ #
    def _ensure_data_loaded(self) -> None:
        if self.data.empty:
            raise RuntimeError("Data not loaded. Call load_data() first.")

    def _ensure_indicators(self) -> None:
        self._ensure_data_loaded()
        if self.strategy == "ma_crossover":
            if self.fast_col not in self.data or self.slow_col not in self.data:
                raise RuntimeError("Indicators not calculated. Call calculate_indicators().")
        else:
            required = {
                self.bb_mid_col,
                self.bb_upper_col,
                self.bb_lower_col,
                self.rsi_col,
            }
            if any(col not in self.data for col in required):
                raise RuntimeError("RSI/Bollinger indicators missing. Call calculate_indicators().")

    def _ensure_signals(self) -> None:
        self._ensure_indicators()
        if "signal" not in self.data:
            raise RuntimeError("Signals not generated. Call generate_signals().")


def main() -> None:
    """Quick manual test when running this module directly."""
    csv = Path(__file__).resolve().parents[2] / "data" / "AAPL.csv"
    bt = SimpleBacktest(str(csv))
    bt.load_data()
    bt.calculate_indicators()
    bt.generate_signals()
    bt.run()
    print(bt.get_results())


if __name__ == "__main__":
    main()
