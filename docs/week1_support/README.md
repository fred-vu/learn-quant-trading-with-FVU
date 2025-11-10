# Week 1 Support Artifacts

Centralized index for every document generated during Week 1 (Python backtest + MA experiments). Raw outputs live under `results/week1/` grouped by type so future weeks can keep their own subfolders.

## Directory Map

| Folder | Description | Example Files |
|--------|-------------|---------------|
| `results/week1/logs/` | Console captures from `scripts/test_backtest.py` (SMA/EMA/WMA/WEMA runs, ticker sweeps, crypto experiments). | `backtest_output_BTC_WEMA_21_63.txt`, `backtest_output_SOL_WEMA_20_50.txt` |
| `results/week1/trades/` | Trade-by-trade CSV exports for every run. Each filename encodes ticker + MA type + window. | `backtest_trades_NVDA_WMA.csv`, `backtest_trades_BTC_WEMA_20_50.csv` |
| `results/week1/equity_curves/` | All visualization assets (single-run equity curves + multi-variant overlays). | `equity_curve_BTC_WEMA_21_63.png`, `equity_curve_comparison_SOL_30_90.png` |
| `results/week1/comparisons/` | Summary metrics per ticker/window generated via `compare_ma_types.py`. | `ma_comparison_AAPL.csv`, `ma_comparison_BTC_30_90.csv` |

## Usage Tips

- Use `python/scripts/test_backtest.py` with `--trades-csv` inside `results/week1/trades/` to keep naming consistent.
- Use `python/scripts/compare_ma_types.py` without specifying `--summary-csv`/`--equity-plot` to auto-save into the Week 1 folders.
- When documenting findings, reference paths directly (e.g., ``results/week1/logs/backtest_output_BTC_WEMA_21_63.txt``) for reproducibility.
- For quick ad-hoc stock downloads, `data/download_data.py` is fine; for reusable workflows with validation, prefer `python/data_utils/stock_data.py` (ticker checks, holiday-aware gaps, structural validation, and reusable functions).

This support folder will remain read-only; future weeks should create `results/weekN/` equivalents plus a matching doc (e.g., `docs/week2_support`).
