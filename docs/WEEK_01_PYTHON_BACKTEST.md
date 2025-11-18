
## 📋 WEEK 1-2: Python Backtest Engine

**File:** `docs/WEEK_01_PYTHON_BACKTEST.md`

```markdown
# Week 1-2: Python Backtest Engine Fundamentals

**Duration:** Days 8-21 (10 hours total, 5h/week)  
**Status:** 🔄 In Progress / ✅ Complete  
**Effort:** Medium (core logic coding)

---

## 🎯 Goals This Week

- [x] Simple backtest engine written (100-150 lines)
- [x] Load historical CSV data
- [x] Calculate technical indicators (SMA)
- [x] Generate trading signals
- [x] Calculate basic metrics (total return, trades)
- [x] Output results to CSV
- [x] 5+ commits with working code

- 📁 **Support Artifacts:** Week 1 outputs are organized under `results/week1/`:
  - Logs → `results/week1/logs/`
  - Trade exports → `results/week1/trades/`
  - Equity curves (single/multi-line) → `results/week1/equity_curves/`
  - Metric comparisons → `results/week1/comparisons/`

---

## 📚 Learning Path

### Pre-Week Learning (2h)

**What to learn:**
- Pandas DataFrame basics
- Rolling windows & moving averages
- CSV read/write
- Dictionary/list comprehension

**Resources:**
- Pandas tutorial: https://pandas.pydata.org/docs/user_guide/basics.html
- Rolling windows: https://pandas.pydata.org/docs/reference/window.html
- Total: 1-2 hours of reading

**AI Agent Learning Prompt:**
```
"Explain pandas moving averages to me:

1. What is a moving average?
2. How to calculate SMA(20)?
3. How to calculate in pandas using rolling()?
4. Show code example with 100 prices

Keep explanation simple, show working code"
```

**Notes:**
- [x] Understand what SMA means
- [x] Know how to use .rolling().mean()
- [x] Can load CSV into DataFrame

---

## 🛠️ Main Tasks

### Task 1: Download & Prepare Data (1h)

**What to do:**

1. Create `data/download_data.py`:
   ```python
   import yfinance as yf
   
   # Download AAPL data for 5 years
   data = yf.download('AAPL', start='2020-01-01', end='2025-01-01')
   
   # Save to CSV
   data.to_csv('data/AAPL.csv')
   print("✓ AAPL data saved to data/AAPL.csv")
   ```

2. Run: `python data/download_data.py`

3. Verify:
   - [x] File `data/AAPL.csv` exists
   - [x] ~1250 rows (5 years of trading days)
   - [x] Columns: Date, Open, High, Low, Close, Adj Close, Volume

**AI Agent Prompt:**
```
"Create Python script to:
1. Download AAPL stock data from Yahoo Finance (5 years)
2. Save to CSV: data/AAPL.csv
3. Print: number of rows, date range, columns

Use yfinance library. Include error handling"
```


Improved prompt (big prompt) 
"""
Create a Python module for downloading and validating stock market data.

Requirements:

1. Function: download_stock_data(symbol, start_date, end_date)
   - Use yfinance to download data
   - Parameters:
     * symbol: stock ticker (AAPL, GOOGL, etc.)
     * start_date: YYYY-MM-DD format
     * end_date: YYYY-MM-DD format
   - Return: pandas DataFrame with OHLCV (Open, High, Low, Close, Volume)
   - Error handling: invalid symbol, date range, network errors

2. Function: validate_ohlc_data(df)
   - Checks:
     * No missing dates (except weekends/holidays)
     * High >= Open, Close, Low (always)
     * Low <= Open, Close, High (always)
     * Volume >= 0
     * Positive prices
   - Return: True if valid, list of errors if invalid
   - Print warnings but don't crash

3. Function: save_data(df, filename)
   - Save DataFrame to CSV
   - Filename: data/[SYMBOL].csv
   - Include header row
   - Format dates as YYYY-MM-DD

4. Example usage:
   data = download_stock_data('AAPL', '2020-01-01', '2025-01-01')
   if validate_ohlc_data(data):
       save_data(data, 'data/AAPL.csv')
       print(f"✓ Saved {len(data)} rows")

Include docstrings and type hints for all functions.

"""



**Progress notes:** ✅ Added `data/download_data.py` CLI utility (symbol/start/end arguments, error handling) and generated `data/AAPL.csv` via `python data/download_data.py`. Output summary: 1,258 rows covering 2020-01-02 → 2024-12-31 with standard OHLCV columns. Created reusable module `python/data_utils/stock_data.py` with download/validation/save helpers, ticker validation, and interactive prompts; fetched `data/NVDA_2025-11-01_2020-01-01.csv` (1,467 rows, 2020-01-02 → latest available) per the NVDA request.

**Validation:**
- [x] CSV file created
- [x] Data looks reasonable
- [x] Commit: `git add data/AAPL.csv && git commit -m "Add AAPL historical data"`

**Time spent:** ~30 min

---

### Task 2: Create Backtest Engine Class (4h)

**What to do:**

Create `python/backtester/simple_backtest.py`:

**Specifications:**
1. Class `SimpleBacktest`
2. Constructor: takes CSV filename
3. Method `load_data()`: read CSV, basic validation
4. Method `calculate_indicators()`: compute SMA(20) and SMA(50)
5. Method `generate_signals()`: buy/sell logic
6. Method `run()`: execute backtest
7. Method `get_results()`: return metrics dict

**Signal Logic (simple):**
- BUY when: SMA(20) > SMA(50)
- SELL when: SMA(20) < SMA(50)
- HOLD otherwise

**Metrics to calculate:**
- Total trades
- Winning trades / Losing trades
- Win rate (%)
- Total return (%)
- Max drawdown (%)
- Sharpe ratio (simplified)

**AI Agent Prompt:**
```
"Create Python backtest engine:

Class SimpleBacktest:
- __init__(self, csv_file)
- load_data() → loads CSV into self.data (DataFrame)
  * Validates: has Date, Close columns
  * Sorts by date ascending
  * Error: if file not found
  
- calculate_indicators() → adds moving-average columns
  * Accept a parameter (e.g., `moving_average="sma"`, `"ema"`, `"wma"`, `"wema"`)
  * Windows are configurable via `fast_window` / `slow_window` (default 20/50)
  * For SMA: `df['Close'].rolling(window=fast_window).mean()`
  * For EMA: `df['Close'].ewm(span=fast_window, adjust=False).mean()`
  * For WMA: linearly weight the last N closes (recent price highest weight) using `rolling(...).apply()`
  * For WEMA: run EMA first, then apply the WMA weighting to emphasize the most recent EMA values
  
- generate_signals() → adds signal column
  * 1 if SMA20 > SMA50 (BUY)
  * -1 if SMA20 < SMA50 (SELL)
  * 0 otherwise (HOLD)
  * self.data['signal'] = result
  
- run() → simulate trades
  * For each row: if signal changes → trade
  * Track: entry_price, exit_price, pnl
  * Store trades in self.trades (list of dicts)
  
- get_results() → return dict:
  {
    'total_trades': int,
    'winning_trades': int,
    'losing_trades': int,
    'win_rate': float (0-100),
    'total_return': float (0-100 %),
    'max_drawdown': float (0-100 %),
    'sharpe_ratio': float
  }

Include docstrings for all methods.
Handle edge cases: no trades, single trade, NaN values"
```

**Expected output structure:**
```
results = {
    'total_trades': 45,
    'winning_trades': 28,
    'losing_trades': 17,
    'win_rate': 62.2,
    'total_return': 18.5,
    'max_drawdown': 12.3,
    'sharpe_ratio': 0.87
}
```

**Code structure:**
```python
# python/backtester/simple_backtest.py

import pandas as pd
import numpy as np

class SimpleBacktest:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.data = None
        self.trades = []
    
    def load_data(self):
        # Implementation
        pass
    
    def calculate_indicators(self):
        # Implementation
        pass
    
    def generate_signals(self):
        # Implementation
        pass
    
    def run(self):
        # Implementation
        pass
    
    def get_results(self):
        # Implementation
        pass

# Example usage
if __name__ == '__main__':
    bt = SimpleBacktest('data/AAPL.csv')
    bt.load_data()
    bt.calculate_indicators()
    bt.generate_signals()
    bt.run()
    results = bt.get_results()
    print(results)
```

**Progress notes:** ✅ Implemented `python/backtester/simple_backtest.py` with `SimpleBacktest` class (load → indicators → signals → run → metrics + CSV export). Includes data validation, SMA/EMA/WMA/WEMA generation (configurable windows via `fast_window` + `slow_window`), long-only trade simulation, Sharpe/return/drawdown metrics, and docstrings. Imported via `backtester.SimpleBacktest` for reuse.

**Validation:**
- [x] Code runs without errors (`PYTHONPATH=python python - <<...>` test with `data/AAPL.csv`)
- [x] Produces reasonable results (EMA test: 10 trades, ~1.32% return; WMA test: 15 trades, ~1.12% return; WEMA test: 9 trades, ~1.05% return on AAPL)
- [x] Docstrings for all methods
- [x] Handles missing data gracefully (runtime guards)
- [x] Commit: `git add python/backtester/ && git commit -m "Backtest engine v1 - MA strategy"`

**Time spent:** ~90 min

---

### Task 3: Test Backtest Engine (1h)

**What to do:**

1. Create `python/scripts/test_backtest.py`:
   ```python
   from backtester.simple_backtest import SimpleBacktest
   
   # Run backtest
   bt = SimpleBacktest('data/AAPL.csv')
   bt.load_data()
   bt.calculate_indicators()
   bt.generate_signals()
   bt.run()
   results = bt.get_results()
   
   # Print results
   print("=" * 50)
   print("BACKTEST RESULTS - AAPL")
   print("=" * 50)
   for key, value in results.items():
       print(f"{key:.<30} {value}")
   print("=" * 50)
   ```

2. Run SMA/EMA/WMA/WEMA variants with flexible windows, e.g.:
   - `python scripts/test_backtest.py --ma-type ema --fast-window 10 --slow-window 40`
   - `python scripts/test_backtest.py --ma-type wma`
   - `python scripts/test_backtest.py --ma-type wema`

3. Save output to file (per variant): `python scripts/test_backtest.py --ma-type ema > results/week1/logs/backtest_output.txt`

4. Bonus comparison helper: `python/scripts/compare_ma_types.py` runs all MA variants, exports metrics table (`results/week1/comparisons/ma_comparison_<ticker>.csv`), and plots a multi-line equity curve (`results/week1/equity_curves/equity_curve_comparison_<ticker>.png`).

**AI Agent Prompt:**
```
"Create test script for backtest:

1. Load AAPL backtest
2. Run full backtest
3. Print results in formatted table:
   - Total trades: X
   - Winning trades: X (%)
   - Win rate: X%
   - Total return: X%
   - Max drawdown: X%
   - Sharpe ratio: X

4. Also save this output to `results/week1/logs/backtest_output.txt`"
```

- **Validation:**
- [x] Script runs with SMA/EMA options
- [x] Output prints initial/final capital plus metrics
- [x] Metrics make sense
- [x] Commit: `git add python/scripts/test_backtest.py && git commit -m "Test backtest - results look good"`

**RSI + Bollinger run example:**

```bash
cd python
python scripts/test_backtest.py \
  --strategy rsi_bollinger \
  --data ../data/week1/NVDA.csv \
  --rsi-period 14 \
  --rsi-long-entry 25 --rsi-long-exit 55 \
  --rsi-short-entry 75 --rsi-short-exit 45 \
  --bollinger-window 20 --bollinger-std 2.0
```

**Config-file driven run:**

```bash
cd python
python scripts/test_backtest.py --config ../python/configs/btc_rsi_bollinger_noshort.json
```

**Time spent:** ____ min

---

### Task 4: Export Results to CSV (1h)

**What to do:**

Enhance backtest to export trade history:

```python
# In SimpleBacktest class, add:

def export_trades_to_csv(self, filename):
    """Export all trades to CSV"""
    trades_df = pd.DataFrame(self.trades)
    trades_df.to_csv(filename, index=False)
    print(f"✓ Exported {len(self.trades)} trades to {filename}")
```

Then add to test script:
```python
bt.export_trades_to_csv('results/week1/trades/backtest_trades.csv')
```

**CSV output should have columns:**
- entry_date
- entry_price
- exit_date
- exit_price
- quantity
- pnl
- pnl_percent
- trade_duration_days

**AI Agent Prompt:**
```
"Add CSV export to backtest:

1. Method export_trades_to_csv(filename):
   - Convert self.trades list → DataFrame
   - Columns: entry_date, entry_price, exit_date, exit_price, pnl, pnl_%
   - Save to CSV
   - Print: 'Exported X trades to filename'

2. Use in test script:
   bt.export_trades_to_csv('results/week1/trades/AAPL_trades.csv')

3. Verify: CSV readable in Excel/spreadsheet"
```

**Validation:**
- [x] CSV file created: `results/week1/trades/AAPL_trades.csv`
- [x] Contains all trades
- [x] Columns correct
- [x] Can open in Excel
- [x] Commit: `git add results/week1/trades && git commit -m "Export backtest trades to CSV"`

**Time spent:** ____ min

---

### Task 5: Create Visualization (1h)

**What to do:**

Create `python/scripts/plot_results.py`:

```python
import matplotlib.pyplot as plt
import pandas as pd

# Load backtest results
results = pd.read_csv('results/week1/trades/backtest_trades.csv')

# Plot: cumulative PnL over time
plt.figure(figsize=(12, 6))
plt.plot(results.index, results['cumulative_pnl'])
plt.title('Cumulative PnL - AAPL Backtest')
plt.xlabel('Trade Number')
plt.ylabel('Cumulative PnL ($)')
plt.grid(True)
plt.savefig('results/week1/equity_curves/equity_curve.png', dpi=150)
print("✓ Chart saved to results/week1/equity_curves/equity_curve.png")
```

**AI Agent Prompt:**
```
"Create visualization for backtest results:

1. Load backtest trades from CSV
2. Calculate cumulative PnL
3. Plot:
   - X-axis: trade date or trade number
   - Y-axis: cumulative PnL
   - Title: 'Backtest Equity Curve - AAPL'
   
4. Save to `results/week1/equity_curves/equity_curve.png`
5. Print: 'Chart saved!'

Use matplotlib"
```

**Validation:**
- [x] Chart created
- [x] Shows cumulative PnL over time
- [x] File saved: `results/week1/equity_curves/equity_curve.png`
- [x] Commit: `git add results/week1/equity_curves/equity_curve.png && git commit -m "Add equity curve visualization"`

**Time spent:** ____ min

---

## ✅ Weekly Checklist

- [x] Backtest engine coded (SimpleBacktest class)
- [x] AAPL data loaded correctly
- [x] Indicators calculated (SMA20, SMA50)
- [x] Signals generated
- [x] Backtest runs without errors
- [x] Results exported to CSV
- [x] Equity curve visualization created
- [x] 5+ commits made

---

## 📊 Metrics This Week

| Metric | Target | Actual |
|--------|--------|--------|
| Python LOC written | 150-200 | ____ |
| Files created | 3-4 | ____ |
| GitHub commits | 5+ | ____ |
| Backtest engine working | ✓ | ____ |
| Hours invested | 10 | ____ |

---

## 💡 Notes & Insights

**What went well:**
- 

**Challenges faced:**
- 

**Mistakes & lessons:**
- 

**AI agent effectiveness:**
- (Rate 1-5): ____

---

## 🚀 Quick Win Checkpoint

✅ **This week you achieved:**
- Working backtest engine
- First strategy backtested
- Reproducible results in CSV
- Visual equity curve

**Tweet/LinkedIn post:**
```
"Week 1-2 of my trading bot journey: Built a complete 
backtesting engine in Python! 📊

First strategy (MA Crossover) backtested on 5 years of AAPL data.
Results: 62% win rate, 18.5% return 📈

#QuantTrading #Python #TradingBot #GitHub"
```

---

## Strategy Variations (Week 2 Prep)

| Strategy | Setup | Current Best Params | Notes |
|----------|-------|---------------------|-------|
| **MA Crossover** | Trend-following | `ma_type=sma`, `fast/slow=20/50` (AAPL), alternative WEMA 21/63 (BTC) | Baseline engine validation; produces steady, well-documented trades. |
| **RSI + Bollinger MR** | Mean-reversion | BTC long-only, `RSI 25→65`, `Bollinger window=14`, `std=2.0`, `shorts disabled` | Without shorts the strategy returned +148% over 2020-2025; re-enable shorts only with stricter thresholds (RSI ≥ 85 + band re-entry). |
| **RSI + Bollinger (Equities)** | Mean-reversion | NVDA tests with defaults underperformed | Use as comparative case study for Week 2 parameter sweeps / regime filters. |

**Suggested Week 2 experiments:**
- **US large-cap equities:** SPY or AAPL with SMA50/200 vs EMA21/63 crossovers to confirm regime differences between tech and index ETFs.
- **US growth index:** QQQ with WEMA(14/60) crossover plus RSI filter (only take trades if RSI between 40-70) to reduce whipsaws.
- **Mean reversion on mega-cap stocks:** NVDA/MSFT/PLTR using RSI(2) or RSI(5) pullbacks combined with 20-day Bollinger bands to see whether shorter windows improve signal frequency.
- **US indices mean reversion:** Dow Jones ETF (DIA) or Russell 2000 ETF (IWM) with Bollinger(20, 2.5) and RSI 30/60 thresholds; compare performance to BTC tests to highlight asset-class sensitivity.
- **Beginner-friendly add-ons:** MACD(12,26,9) crossovers on SPY (trend), Donchian 20-day breakout on QQQ (momentum), and ATR(14) trailing stops layered on top of the MA crossover to practice risk control.
- **Volatility throttles:** Use ATR filters (enter only if ATR% of price > 2%) on META or NVDA to learn how to gate trades when volatility is too low/high.
- **Session-based tests:** For US indices, run separate backtests on pandemic vs post-pandemic slices (split data at 2022-01-01) to see how strategies behave in different macro regimes.

Use this grid as the launchpad for Week 2 experimentation: extend `test_backtest.py` with CLI presets, save logs under `results/week2/`, and layer cost/risk modeling on top of these base configs.

---

## 🔗 Resources Used

- [Pandas documentation](https://pandas.pydata.org/docs/)
- [Matplotlib examples](https://matplotlib.org/examples/)
- [yfinance docs](https://github.com/ranaroussi/yfinance)

---

**Status:** 🔄 In Progress / ✅ Complete  
**Confidence Level:** 1 ☆☆☆☆☆ 5 - Rate: ____  
**Ready for Week 2-3:** [x] Yes [ ] No  

**Next week:** Multi-strategy framework + parameter optimization

```

---
