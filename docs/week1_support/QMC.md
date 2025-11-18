# Week 1 Quick Mastery Check (QMC)

Use these prompts to self‑test everything covered during Week 1. Answer them without looking at the code first; then verify using the repo.

---

## Quick Multiple Choice Warm-up

**Q1.** Which moving-average type weights the most recent price the heaviest *and* keeps a non-zero weight on all historical prices?  
A) SMA B) EMA C) WMA D) WEMA  

**Q2.** In our repo, which command automatically generates equity curves and metrics for SMA/EMA/WMA/WEMA at once?  
A) `python scripts/test_backtest.py`  
B) `python scripts/plot_results.py`  
C) `python scripts/compare_ma_types.py`  
D) `python data/download_data_stock.py`  

**Q3.** Where do Week 1 trade CSV exports live by default?  
A) `results/trades/` B) `results/week1/trades/` C) `docs/week1_support/` D) `data/`  

**Q4.** Which Python library do we use for downloading market data in both stock and crypto scripts?  
A) pandas B) numpy C) yfinance D) matplotlib  

**Q5.** In `SimpleBacktest`, what property stores the running list of completed trades?  
A) `self.data` B) `self.trades` C) `self._equity_curve` D) `self._results`  

**Q6.** What pandas method do we call to compute SMA given a Series?  
A) `.rolling(window).mean()` B) `.ewm(span).mean()` C) `.cumsum()` D) `.pct_change()`  

**Q7.** Which CLI argument lets you change the fast MA window via `scripts/test_backtest.py`?  
A) `--ma-type` B) `--fast-window` C) `--position-size` D) `--capital`  

**Q8.** How do we obtain cumulative PnL inside `plot_results.py`?  
A) `results["pnl"].cumsum()` B) `results["pnl"].cumprod()` C) `results["Close"].diff()` D) `results["pnl"].rolling().sum()`  

**Q9.** What does `_ensure_signals()` guard against in `SimpleBacktest`?  
A) Missing CSV columns B) Indicators not calculated C) Signals absent before `run()` D) Empty trade list  

**Q10.** Which Python module provides custom business-day calendars for validation?  
A) `pandas.tseries.offsets` B) `pandas.tseries.holiday` C) `datetime` D) `calendar`  

(Answers: 1B, C, B, 4C, B, A, B, A, C, B)

---

## Section 1 – Moving Averages
1. Explain the mathematical differences between SMA, EMA, WMA, and WEMA. In which scenarios would each be preferable?
2. Derive the WEMA(21) update formula we implemented (EMA fed into WMA). What advantage did it give on BTC vs SOL?
3. Given `fast_window=7` and `slow_window=30`, outline how signal generation changes when the fast MA is NaN for the first few rows.

## Section 2 – Backtest Engine
4. Walk through `SimpleBacktest.run()` and describe the exact sequence when a long trade is opened and closed. What happens to `cash`, `position`, and `equity_values` on each step?
5. How does the engine compute max drawdown and Sharpe ratio from the equity curve? Reproduce the formulas.
6. List the guard methods (`_ensure_*`) and explain when each raises an error.

## Section 3 – Tooling & Data
7. Compare `data/download_data_stock.py` (formerly `download_data.py`) vs `python/data_utils/stock_data.py`. When should you use each?
8. Document the CLI command to download SOL-USD daily candles from 2020‑01‑01 to 2025‑11‑01 into `data/SOL_custom.csv`.
9. Write the command to run WEMA(14/60) on SOL data, saving logs, trades, and equity curves into the Week 1 folders.

## Section 4 – Results Interpretation
10. From `results/week1/comparisons/ma_comparison_BTC_20_50.csv`, which MA performed best and why (based on metrics provided)?
11. Using `results/week1/logs/backtest_output_SOL_WEMA_20_50.txt`, summarize the risk/return characteristics. Would you deploy it live?
12. Open any `equity_curve_comparison_*.png`. Describe how you can visually detect overfitting or lagging responses among the MA types.

---

Write your answers directly in this file or in a separate notes doc. The goal is to ensure you can explain every moving part without relying on the codebase. Once finished, mark the section complete in `LEARNING_LOG.md`.
