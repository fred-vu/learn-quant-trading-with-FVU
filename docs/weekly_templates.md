# Weekly Template Files for Quant Trading Bot

Use these templates for each week. Copy to your `docs/` folder as:
- `WEEK_00_SETUP.md`
- `WEEK_01_PYTHON_BASICS.md`
- `WEEK_02_PYTHON_BACKTEST.md`
- etc.

Then update weekly and commit to GitHub.

---

## 📋 WEEK 0: Setup & Mindset

**File:** `docs/WEEK_00_SETUP.md`

```markdown
# Week 0: Setup & GitHub Repository Foundation

**Duration:** Days 1-7 (2-3 hours total)  
**Status:** 🔄 In Progress / ✅ Complete  
**Effort:** Easy (no coding yet)

---

## 🎯 Goals This Week

- [ ] GitHub repo created & structured
- [ ] Python environment ready (test with simple script)
- [ ] C++ compiler working (test with hello world)
- [ ] Project README written
- [ ] First 3 commits done

---

## 📝 Tasks

### Task 1: GitHub Repository Setup (30 min)

**What to do:**
1. Create repo: `quant-trading-bot` on GitHub
2. Clone locally
3. Create folder structure:
   ```
   quant-trading-bot/
   ├── docs/
   ├── python/
   ├── cpp/
   ├── data/
   ├── results/
   ├── README.md
   └── .gitignore
   ```
4. First commit: `git add . && git commit -m "Initial repo structure"`

**AI Agent prompt:** (not needed this week - structural task)

**Validation:**
- [ ] Repo created on GitHub
- [ ] All folders visible locally
- [ ] .gitignore includes: `*.csv, *.o, *.so, __pycache__, .DS_Store`

**Time spent:** ____ min

---

### Task 2: Python Environment Setup (45 min)

**What to do:**
1. Create `python/` folder
2. Create `requirements.txt`:
   ```
  pandas==2.3.3
   numpy==2.3.4
   matplotlib==3.10.7
   backtrader==1.9.76.123
   yfinance==0.2.66
   ```
3. Create virtual environment:
   ```bash
   cd python
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```
4. Test with simple script:
   ```python
   # python/test_setup.py
   import pandas as pd
   import numpy as np
   print("✓ Pandas version:", pd.__version__)
   print("✓ NumPy version:", np.__version__)
   print("✓ Environment ready!")
   ```
5. Run: `python test_setup.py`
6. Commit: `git add -A && git commit -m "Python environment setup with dependencies"`

**Result:**
- [ ] Virtual environment activated
- [ ] All packages installed
- [ ] Test script runs successfully
- [ ] Commit pushed

**Time spent:** ____ min

---

### Task 3: C++ Compiler Setup (30 min)

**What to do:**

**Linux/Mac:**
```bash
# Test g++ installation
g++ --version
# If not installed:
# Mac: brew install gcc
# Linux: sudo apt install g++
```

**Windows:**
```bash
# Install MSVC or use MinGW
# Then test:
cl /?  # for MSVC
# or
g++ --version  # for MinGW
```

**Test hello world:**
```cpp
// cpp/practice/hello.cpp
#include <iostream>
int main() {
    std::cout << "✓ C++ compiler working!" << std::endl;
    return 0;
}
```

```bash
g++ -o hello cpp/practice/hello.cpp
./hello
```

**Validation:**
- [ ] Compiler installed
- [ ] Hello world compiles
- [ ] Hello world runs
- [ ] Compiler version printed

**Time spent:** ____ min

---

### Task 4: README Documentation (30 min)

**What to do:**
Create `README.md` with:

```markdown
# Quant Trading Bot: From Zero to Hero

A comprehensive learning project to build a trading bot using Python + C++, 
leveraging AI agents for rapid development.

## 🎯 Project Goal

Build a **working trading bot** in 4.5 months by:
- Developing strategies in Python
- Optimizing execution in C++
- Using AI agents to code faster
- Documenting everything for portfolio

## 🚀 Quick Start

```bash
# Python backtest
cd python
source venv/bin/activate
python scripts/run_backtest.py

# C++ bot
cd cpp
mkdir build && cd build
cmake ..
make
./trading_bot
```

## 📊 Project Status

- Week 0: ✅ Setup complete
- Week 1-2: 🔄 In progress
- Month 1: 📋 Planning
- Month 2: 📋 Planning

## 📚 Documentation

- [Roadmap](docs/ROADMAP.md) - Full 4.5 month plan
- [Learning Log](docs/LEARNING_LOG.md) - Weekly progress
- [Architecture](docs/ARCHITECTURE.md) - System design

## 🤖 Using AI Agents

This project uses AI coding agents (Claude, ChatGPT) to accelerate development.
See [AI Prompts](docs/AI_PROMPTS.md) for reusable prompts.

## 📈 Expected Results

- Working backtest engine
- 5+ trading strategies
- C++ order execution
- Performance metrics & analysis
- Full documentation & GitHub portfolio piece

## 👤 Author

[Your Name]

---

**Last Updated:** Week 0 - 2025-11-06
```

**Commit:** `git add README.md && git commit -m "Initial README and project overview"`

**Time spent:** ____ min

---

### Task 5: Create Weekly Tracking Template (20 min)

**What to do:**
Create `docs/LEARNING_LOG.md`:

```markdown
# Learning Log - Weekly Progress Tracking

This log tracks your learning journey week by week.
Update every Sunday evening.

## Week 0: Setup

- ✅ GitHub repo created
- ✅ Python environment ready
- ✅ C++ compiler working
- ✅ README written

### Time Invested
- Total: 2.5 hours
- Coding: 0.5 hours
- Setup: 2 hours

### Commits
1. `Initial repo structure`
2. `Python environment setup`
3. `Initial README`

### Lessons Learned
- GitHub structure is important from start
- Environment setup takes time but crucial

### Next Week Focus
- Python: Create simple backtest engine
- C++: Learn pointers and basics
- Integration: Plan CSV bridge

---

```

**Commit:** `git add docs/LEARNING_LOG.md && git commit -m "Add learning log template"`

**Time spent:** ____ min

---

## ✅ Weekly Checklist

- [ ] GitHub repo created & functional
- [ ] Python environment tested
- [ ] C++ compiler tested
- [ ] README written
- [ ] Learning log started
- [ ] 3+ commits on GitHub
- [ ] .gitignore configured

---

## 📊 Metrics

| Metric | Value |
|--------|-------|
| Total time invested | ~2.5 hours |
| Python files created | 1 |
| C++ files created | 1 |
| GitHub commits | 3+ |
| Documentation pages | 2 |

---

## 💡 Notes & Insights

**What went well:**
- Fast setup process
- All tools installed without issues

**Challenges:**
- (None yet, it's setup week!)

**Next week preparation:**
- Think about what backtest engine should do
- Review pandas documentation
- Remember: Month 1 goal is 2-3 working strategies

---

## 🔗 Links & Resources

- [GitHub Repo](https://github.com/[your-username]/quant-trading-bot)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- [C++ Getting Started](https://cplusplus.com/)

---

**Status:** ✅ Complete  
**Confidence Level:** 5/5 - All tools ready  
**Recommendation:** Begin Week 1 immediately  

```

**Time spent:** ____ min

---

## ✨ End of Week Summary

**Total time this week:** ____ hours  
**Commits made:** ____  
**Blocker encountered:** [ ] Yes [ ] No - Describe: _____  
**Confidence for Week 1:** 1 ☆☆☆☆☆ 5 - Rate: ____  

**Next week:**
- Start Python backtest engine
- First trading strategy
- First working backtest

---
```

---

## 📋 WEEK 1-2: Python Backtest Engine

**File:** `docs/WEEK_01_PYTHON_BACKTEST.md`

```markdown
# Week 1-2: Python Backtest Engine Fundamentals

**Duration:** Days 8-21 (10 hours total, 5h/week)  
**Status:** 🔄 In Progress / ✅ Complete  
**Effort:** Medium (core logic coding)

---

## 🎯 Goals This Week

- [ ] Simple backtest engine written (100-150 lines)
- [ ] Load historical CSV data
- [ ] Calculate technical indicators (SMA)
- [ ] Generate trading signals
- [ ] Calculate basic metrics (total return, trades)
- [ ] Output results to CSV
- [ ] 5+ commits with working code

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
- [ ] Understand what SMA means
- [ ] Know how to use .rolling().mean()
- [ ] Can load CSV into DataFrame

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
   - [ ] File `data/AAPL.csv` exists
   - [ ] ~1250 rows (5 years of trading days)
   - [ ] Columns: Date, Open, High, Low, Close, Adj Close, Volume

**Steps:**

1. Create `CMakeLists.txt` in `cpp/` folder (use above)
2. Create header files: `data_loader.h`, `price_analyzer.h`
3. Move code to `src/` folder
4. Build:
   ```bash
   cd cpp
   mkdir build
   cd build
   cmake ..
   make
   ./trading_bot
   ```

**AI Agent Prompt:**
```
"Create professional C++ project structure:

1. Create CMakeLists.txt (CMAKE build file) that:
   - Sets C++ standard to 17
   - Includes: include/ directory
   - Sources: src/*.cpp files
   - Executable: trading_bot
   - Compiler flags: -Wall -Wextra -O2

2. Create include/data_loader.h:
   - Struct OHLC declaration
   - Function declarations: loadOHLCFromCSV(), etc.
   
3. Create include/price_analyzer.h:
   - Class PriceAnalyzer declaration
   
4. Move implementation to src/:
   - src/main.cpp
   - src/data_loader.cpp
   - src/price_analyzer.cpp
   
5. Build instructions:
   cd cpp && mkdir build && cd build
   cmake ..
   make
   ./trading_bot
   
Should compile with no warnings"
```

**Validation:**
- [ ] CMakeLists.txt created
- [ ] Project compiles: `make` succeeds
- [ ] Executable runs: `./trading_bot`
- [ ] No compiler warnings
- [ ] Commit: `git add cpp/CMakeLists.txt cpp/include/ cpp/src/ && git commit -m "Professional C++ project structure with CMake"`

**Time spent:** ____ min

---

### Task 5: Integration Test - Python vs C++ (1h)

**What to do:**

Create `scripts/compare_python_cpp_sma.py`:

Compare SMA values from Python backtest vs C++ calculator:

```python
import pandas as pd
import subprocess
import numpy as np

# Load Python backtest results
python_results = pd.read_csv('results/backtest_trades.csv')
python_sma = python_results['sma20'].values

# Run C++ program and capture output
result = subprocess.run(['./cpp/build/trading_bot'], 
                       capture_output=True, text=True)
cpp_output = result.stdout

# Parse C++ output and extract SMA values
# (Parse based on your output format)

# Compare
print("Comparing Python vs C++ SMA values...")
if np.allclose(python_sma[20:50], cpp_sma[20:50], rtol=0.001):
    print("✓ PASS: SMA values match!")
else:
    print("✗ FAIL: SMA values differ!")
    print("Max difference:", np.max(np.abs(python_sma - cpp_sma)))
```

**AI Agent Prompt:**
```
"Create Python script to validate C++ vs Python results:

1. Load Python backtest SMA values from CSV
2. Run C++ program (./cpp/build/trading_bot)
3. Parse C++ output to extract SMA values
4. Compare first 100 SMA values:
   - Should match within 0.01% tolerance
   - Print: PASS or FAIL
   - If FAIL: show max difference
   
5. Save report to results/validation_sma.txt"
```

**Validation:**
- [ ] Script runs
- [ ] Python and C++ SMA match
- [ ] Report generated
- [ ] Commit: `git add scripts/compare_python_cpp_sma.py && git commit -m "Validation: Python vs C++ SMA match"`

**Time spent:** ____ min

---

## ✅ Weekly Checklist

- [ ] 5 beginner C++ programs working
- [ ] OHLC struct created
- [ ] CSV loading in C++
- [ ] SMA calculation in C++
- [ ] Project structure with CMake
- [ ] Compiles without warnings
- [ ] Python vs C++ validation passing
- [ ] 5+ commits

---

## 📊 Metrics This Week

| Metric | Target | Actual |
|--------|--------|--------|
| C++ LOC written | 200-300 | ____ |
| Programs created | 5 | ____ |
| GitHub commits | 5+ | ____ |
| LeetCode problems | 7+ | ____ |
| Hours invested | 12 | ____ |

---

## 💡 Notes & Insights

**What went well:**
- 

**Challenges faced:**
- (Common: pointer confusion, compilation errors)
- Solution: [describe solution]

**Mistakes & lessons:**
- 

**AI agent effectiveness for C++:**
- (Rate 1-5): ____

**Most confusing concept:**
- [ ] Pointers
- [ ] References
- [ ] STL containers
- [ ] Classes
- Other: ____

---

## 🚀 Quick Win Checkpoint

✅ **This week you achieved:**
- First C++ programs running
- Professional project structure
- Cross-language validation (Python ↔ C++ match!)

**Tweet/LinkedIn post:**
```
"Week 3-4 update: Built my first C++ trading programs! 🚀

- Created OHLC data structures
- Load CSV in C++
- Calculate SMA(20)
- Validated against Python

C++ feels different but powerful!
#QuantTrading #C++ #TradingBot"
```

---

**Status:** 🔄 In Progress / ✅ Complete  
**Confidence Level:** 1 ☆☆☆☆☆ 5 - Rate: ____  
**Ready for Week 5:** [ ] Yes [ ] No  

**Next week:** Multi-strategy framework in Python + Order management in C++

```

---

## 📋 WEEK 5-6: Python Multi-Strategy + C++ Order System

**File:** `docs/WEEK_05_MULTI_STRATEGY_ORDERS.md`

```markdown
# Week 5-6: Multi-Strategy Framework & Order Management System

**Duration:** Days 36-49 (12 hours total, 6h/week)  
**Status:** 🔄 In Progress / ✅ Complete  
**Effort:** Medium (OOP design, architecture)

---

## 🎯 Goals This Week

**Python:**
- [ ] Abstract Strategy base class
- [ ] 3 concrete strategies (MA, Mean Reversion, RSI)
- [ ] Strategy comparison framework
- [ ] Parameter optimization loop
- [ ] Export signals for C++

**C++:**
- [ ] Order struct
- [ ] OrderBook class (thread-safe basics)
- [ ] Position tracking
- [ ] PnL calculation
- [ ] Read signals from Python → execute

**Integration:**
- [ ] Python exports signals.csv
- [ ] C++ reads signals, executes, exports results.csv
- [ ] Results match (validation)

---

## 🛠️ Main Tasks

### Python Task 1: Strategy Base Class (3h)

**AI Agent Prompt:**
```
"Create Python strategy framework:

1. Abstract base class Strategy:
   - __init__(self, params=None)
     * params: dict of strategy parameters
   - abstract method: calculate_indicators(prices) → dict
   - abstract method: generate_signal(indicators) → 1/-1/0
   - method: execute(prices) → signal
   - method: get_name() → string
   
2. Concrete: MACrossover(Strategy)
   - params: fast_period=20, slow_period=50
   - calculate_indicators(): compute SMA(fast), SMA(slow)
   - generate_signal(): BUY if fast > slow, SELL if <, HOLD if ==
   
3. Concrete: MeanReversion(Strategy)
   - params: window=20, std_dev=2.0
   - calculate_indicators(): mean, std of prices
   - generate_signal(): BUY if price < mean-std, SELL if >, HOLD if between
   
4. Concrete: RSI(Strategy)
   - params: period=14, oversold=30, overbought=70
   - calculate_indicators(): compute RSI
   - generate_signal(): BUY if RSI < oversold, SELL if > overbought
   
Each strategy: ~30-40 lines
Full docstrings
Include RSI calculation helper"
```

**File structure:**
```
python/strategies/
├── __init__.py
├── strategy_base.py    (abstract class)
├── ma_crossover.py
├── mean_reversion.py
└── rsi_strategy.py
```

**Validation:**
- [ ] All strategies instantiate
- [ ] Generate signals without error
- [ ] Docstrings for all methods
- [ ] Commit: `git add python/strategies/ && git commit -m "Multi-strategy framework - 3 strategies working"`

**Time spent:** ____ min

---

### Python Task 2: Strategy Comparison (2h)

**AI Agent Prompt:**
```
"Create strategy comparison framework:

1. Class StrategyComparator:
   - __init__(self, data, strategies=[])
   - add_strategy(strategy_obj)
   - run_all() → run backtest for each strategy
   - get_comparison() → dict with metrics for each
   - save_comparison_csv(filename)
   
2. Comparison metrics:
   - Total return (%)
   - Sharpe ratio
   - Win rate (%)
   - Max drawdown (%)
   - Number of trades
   
3. Output example:
   Strategy          Return  Sharpe  Win_Rate  Drawdown
   MACrossover       18.5%   0.87    62.2%     -12.3%
   MeanReversion     12.0%   0.65    55.0%     -18.5%
   RSI               15.3%   0.79    58.5%     -15.2%
   
4. Usage:
   comp = StrategyComparator(data)
   comp.add_strategy(MACrossover())
   comp.add_strategy(MeanReversion())
   comp.run_all()
   comp.save_comparison_csv('results/strategy_comparison.csv')"
```

**Validation:**
- [ ] Compares all strategies
- [ ] Output ranked by Sharpe ratio
- [ ] CSV file created
- [ ] Metrics reasonable
- [ ] Commit: `git add python/strategies/comparator.py && git commit -m "Strategy comparison framework"`

**Time spent:** ____ min

---

### C++ Task 1: Order Management System (4h)

**AI Agent Prompt:**
```
"Create C++ order management system:

1. Struct Order:
   - timestamp: string
   - symbol: string
   - action: enum {BUY, SELL}
   - price: double
   - qty: int
   - status: enum {PENDING, EXECUTED, CANCELLED}
   - Method: is_valid() → bool
   
2. Struct Position:
   - symbol: string
   - qty: int
   - entry_price: double
   - current_price: double
   - calculatePnL() → double
   - calculateROI() → double
   
3. Class OrderBook (thread-safe):
   - Private: map<int, Order> orders
   - Private: map<string, Position> positions
   - Private: std::mutex order_mutex, position_mutex
   - Public: addOrder(Order) → order_id
   - Public: executeOrder(order_id, execution_price) → bool
   - Public: getPosition(symbol) → Position
   - Public: getAllPositions() → map<string, Position>
   - Public: getTotalPnL() → double
   - Public: getTradeHistory() → vector<Order>
   
4. Error handling:
   - Order not found
   - Invalid prices
   - Thread safety (mutex)
   
5. Include: #include <mutex>, #include <map>, etc"
```

**File structure:**
```
cpp/include/
├── order.h
├── position.h
└── order_book.h

cpp/src/
├── order.cpp
├── position.cpp
├── order_book.cpp
└── main.cpp
```

**Validation:**
- [ ] Compiles without warnings
- [ ] OrderBook methods work
- [ ] Thread-safe (doesn't crash)
- [ ] PnL calculations correct
- [ ] Commit: `git add cpp/include/order* cpp/include/position* cpp/include/order_book* cpp/src/order* cpp/src/position* cpp/src/order_book* && git commit -m "Order management system - thread-safe"`

**Time spent:** ____ min

---

### C++ Task 2: Signal Executor (2h)

**AI Agent Prompt:**
```
"Create C++ signal executor:

1. Class SignalReader:
   - loadSignals(csv_file) → vector<Order>
   - Parse: timestamp, symbol, action, price, qty
   - Validate all fields present
   
2. Class SignalExecutor:
   - member: OrderBook
   - member: map<string, double> last_price
   - execute(orders) → vector<Order> with execution prices
   - For each order:
     * Add to OrderBook
     * Set execution_price = signal price
     * Calculate PnL for closed trades
   - exportResults(filename) → write executed orders to CSV
   
3. main():
   - Load signals.csv (from Python)
   - Execute all signals
   - Export results.csv
   - Print: total PnL, num trades, etc.
   
4. CSV format:
   Input (signals.csv): timestamp, symbol, action, price, qty
   Output (results.csv): timestamp, symbol, action, price, qty, execution_price, pnl"
```

**Validation:**
- [ ] Reads signals.csv from Python
- [ ] Executes trades correctly
- [ ] Exports results.csv
- [ ] PnL calculations correct
- [ ] Commit: `git add cpp/src/signal_executor* && git commit -m "Signal executor - reads Python signals, executes"`

**Time spent:** ____ min

---

### Integration Task: Full Pipeline (2h)

**What to do:**

1. **Python exports signals:**
   ```python
   # In strategy, add method:
   def export_signals(self, filename):
       """Export trading signals to CSV for C++"""
       signals_df = pd.DataFrame(self.signals)
       signals_df.to_csv(filename, index=False)
   ```

2. **Run Python → Export signals:**
   ```bash
   python python/scripts/run_backtest.py
   # Outputs: results/signals.csv
   ```

3. **Run C++ → Read signals → Execute:**
   ```bash
   ./cpp/build/trading_bot
   # Input: results/signals.csv
   # Output: results/execution_results.csv
   ```

4. **Validate:**
   ```python
   # Run validation.py
   python scripts/validate_pipeline.py
   # Compares: Python PnL vs C++ PnL (should match)
   ```

**AI Agent Prompt:**
```
"Create validation script:

1. Load: Python backtest results CSV
2. Load: C++ execution results CSV
3. Compare:
   - Number of trades (should match exactly)
   - Total PnL (should match within 0.01%)
   - Average trade PnL
   - Win rate
4. Output:
   - Print: PASS or FAIL
   - If FAIL: show differences
   - Save report to validation_report.txt"
```

**Expected output:**
```
=== Pipeline Validation Report ===
Total trades:
  Python: 45
  C++:    45
  Match: ✓ PASS

Total PnL:
  Python: $2345.67
  C++:    $2346.01
  Diff:   0.01%
  Match: ✓ PASS

Overall: ✓✓✓ FULLY VALIDATED ✓✓✓
```

**Validation:**
- [ ] Pipeline end-to-end working
- [ ] Python → signals.csv
- [ ] C++ reads signals
- [ ] Results match
- [ ] Validation report positive
- [ ] Commit: `git add scripts/validate_pipeline.py results/validation_report.txt && git commit -m "End-to-end pipeline validated - Python and C++ match!"`

**Time spent:** ____ min

---

## ✅ Weekly Checklist

- [ ] Strategy base class created
- [ ] 3 concrete strategies working
- [ ] Strategy comparison framework
- [ ] Order and Position structs
- [ ] OrderBook class thread-safe
- [ ] Signal reader/executor
- [ ] End-to-end pipeline working
- [ ] Validation passing (Python ↔ C++ match)
- [ ] 8+ commits

---

## 📊 Metrics This Week

| Metric | Target | Actual |
|--------|--------|--------|
| Python LOC | 250-350 | ____ |
| C++ LOC | 300-400 | ____ |
| Strategies | 3 | ____ |
| GitHub commits | 8+ | ____ |
| Pipeline tests | ✓ Pass | ____ |
| Hours invested | 12 | ____ |

---

## 💡 Notes & Insights

**What went well:**
- 

**Challenges faced:**
- 

**Mistakes & lessons:**
- 

**Most useful AI prompt:**
- 

---

## 🚀 Quick Win Checkpoint

✅ **This week you achieved:**
- Professional multi-strategy framework
- Thread-safe order management
- **Full end-to-end pipeline working!**
- Python and C++ seamlessly integrated

**Tweet/LinkedIn post:**
```
"Week 5-6: MAJOR milestone achieved! 🎉

Built complete trading pipeline:
1. Python: 3 strategies, signal generation
2. C++: Order execution, position tracking
3. Validation: Python and C++ results MATCH perfectly ✓

This is a real trading system! 📊
#QuantTrading #Python #C++ #TradingBot"
```

---

**Status:** 🔄 In Progress / ✅ Complete  
**Confidence Level:** 1 ☆☆☆☆☆ 5 - Rate: ____  

**Next week:** Real market data integration + advanced strategies

```

---

## 📋 WEEK 7-11: Enhancement Phase Template

**File:** `docs/WEEK_07_ENHANCEMENT_PHASE.md`

```markdown
# Week 7-11: Enhancement Phase - Real Data & Advanced Features

**Duration:** Days 50-77 (30 hours total, 6h/week)  
**Status:** 🔄 In Progress / ✅ Complete  

This is a high-level template. Weeks 7-11 focus on:
- Real market data integration
- Advanced strategies (RSI, Bollinger Bands, etc.)
- Risk management
- Performance optimization
- Parameter tuning

---

## 📋 Weekly Breakdown

### Week 7: Real Market Data Integration
- [ ] Fetch data from Alpha Vantage API
- [ ] Cache locally (avoid rate limits)
- [ ] Data validation & cleaning
- [ ] Backtest on 3 stocks (AAPL, GOOGL, MSFT)

**Commits:** 3-4

### Week 8: Advanced Strategies
- [ ] RSI strategy (14-period, overbought/oversold)
- [ ] Bollinger Bands strategy
- [ ] Strategy ensemble (combine multiple)
- [ ] Backtest all on real data

**Commits:** 3-4

### Week 9: Risk Management
- [ ] Max position size checks
- [ ] Daily loss limits
- [ ] Stop loss / take profit
- [ ] Risk calculator module

**Commits:** 2-3

### Week 10: Parameter Optimization
- [ ] Grid search optimization
- [ ] Walk-forward analysis
- [ ] Best parameters per strategy
- [ ] Sensitivity analysis

**Commits:** 3-4

### Week 11: Performance Reports & Polish
- [ ] Generate comprehensive reports
- [ ] Optimize C++ code
- [ ] Full documentation
- [ ] Code cleanup

**Commits:** 3-4

---

## 📊 Cumulative Metrics (End of Week 11)

| Metric | Target |
|--------|--------|
| Python LOC | 3000+ |
| C++ LOC | 2500+ |
| Strategies | 6+ |
| GitHub commits | 100+ |
| Test coverage | 60%+ |

---

**Template:** Use same structure as Week 1-6 templates
- Set specific AI prompts for each task
- Break into 1-2 hour chunks
- Weekly checkpoints
- Progress metrics

```

---

## 📋 WEEK 12-14: Polish & Production Phase

**File:** `docs/WEEK_12_PRODUCTION_PHASE.md`

```markdown
# Week 12-14: Production Phase - Polish, Test, Deploy

**Duration:** Days 78-98 (18 hours total, 6h/week)  
**Status:** 🔄 In Progress / ✅ Complete  

---

## 🎯 Final Push Goals

- [ ] Comprehensive testing (unit tests)
- [ ] Full documentation (README, guides, API docs)
- [ ] Performance benchmarks
- [ ] Code cleanup & refactoring
- [ ] Version 1.0 release on GitHub
- [ ] Portfolio-ready presentation

---

## 📋 Weekly Breakdown

### Week 12: Testing & Benchmarks
- [ ] Unit tests for all modules (Python)
- [ ] Unit tests for C++ (Google Test)
- [ ] Integration tests
- [ ] Performance benchmarks (Python vs C++)
- [ ] Stress tests (1000+ trades)

**Commits:** 4-5

### Week 13: Documentation & Polish
- [ ] Update README with examples
- [ ] Create API documentation
- [ ] Strategy guide with parameters
- [ ] Performance analysis report
- [ ] Architecture diagrams
- [ ] Add inline code comments

**Commits:** 4-5

### Week 14: Release & Portfolio
- [ ] Code cleanup
- [ ] Final validation
- [ ] Create GitHub Release v1.0
- [ ] Write blog post about project
- [ ] Add to portfolio website
- [ ] Prepare for interviews

**Commits:** 3-4

---

## 📊 Final Metrics (End of Week 14)

| Metric | Target |
|--------|--------|
| Total Python LOC | 3500-4000 |
| Total C++ LOC | 2500-3000 |
| Test coverage | 80%+ |
| GitHub stars | ? (public project) |
| Total commits | 150+ |
| Documentation | Comprehensive |
| Status | 🚀 Production Ready v1.0 |

---

## 📝 Documentation Checklist

- [ ] README.md (setup, quick start, results)
- [ ] ARCHITECTURE.md (system design)
- [ ] STRATEGY_GUIDE.md (how each strategy works)
- [ ] PERFORMANCE_ANALYSIS.md (results & metrics)
- [ ] SETUP.md (step-by-step installation)
- [ ] API_DOCS.md (how to use classes/functions)
- [ ] LEARNING_LOG.md (complete weekly logs)
- [ ] AI_PROMPTS.md (reusable prompts for others)

---

## 🎬 Portfolio Presentation

Create `PORTFOLIO.md`:

```markdown
# Quant Trading Bot - Portfolio Showcase

## What I Built
A production-grade trading bot in Python + C++ that backtests trading strategies 
and executes them efficiently.

## Technical Highlights
- **Language:** Python (strategy/backtesting) + C++ (execution engine)
- **Data:** 5+ years of historical stock data
- **Strategies:** 6+ algorithmic trading strategies
- **Performance:** 15-20% annual return with 0.8+ Sharpe ratio
- **Testing:** 80%+ code coverage

## Key Achievements
✓ 150+ commits on GitHub
✓ End-to-end pipeline (Python → CSV → C++)
✓ Multi-threaded, thread-safe order management
✓ Comprehensive documentation & learning logs

## What I Learned
- Quantitative trading principles
- Backtesting frameworks
- Python data science stack (pandas, numpy, matplotlib)
- C++ performance engineering
- System design & architecture
- AI-assisted rapid development

## Results
[Insert performance charts, metrics, equity curve]

[Insert GitHub links]
```

---

**This is the FINAL PUSH. After Week 14, you'll have:**
- ✅ Working trading bot
- ✅ Portfolio-ready GitHub project
- ✅ Impressive LinkedIn portfolio
- ✅ Knowledge for quant interviews
- ✅ Open-source contribution ready

```

---

# 🎯 How to Use These Templates

## Weekly Workflow:

1. **Sunday evening:** Copy template for next week to `docs/`
2. **Monday:** Read "Goals" section, understand weekly focus
3. **Daily:** Work on tasks, update progress
4. **Friday:** Fill in metrics and notes
5. **Sunday:** Commit everything, write summary

## Example:

```bash
# Week 1 start
cp docs/WEEK_01_PYTHON_BACKTEST_TEMPLATE.md docs/WEEK_01_PYTHON_BACKTEST.md

# Throughout week
# - Update task completion
# - Add time spent
# - Note insights

# Sunday
git add docs/WEEK_01_*.md
git commit -m "Week 1 complete - backtest engine working, 5 commits"
```

## Commit Pattern:

```bash
# Throughout week
git commit -m "Task 1: Create backtest engine - basic structure"
git commit -m "Task 1: Backtest engine - SMA calculations working"
git commit -m "Task 1: Complete - backtest produces valid results"

# End of week
git commit -m "Week 1 COMPLETE - Backtest engine production ready ✓"
```

---

# 📊 Master Progress Tracking

Keep this in `docs/MASTER_PROGRESS.md`:

```markdown
# Master Progress Tracking

## Timeline

| Week | Phase | Python | C++ | Integration | Status |
|------|-------|--------|-----|-------------|--------|
| 0 | Setup | ✓ | ✓ | N/A | ✅ |
| 1-2 | Backtest | ✓ | - | - | 🔄 |
| 3-4 | Foundations | - | ✓ | - | 🔄 |
| 5-6 | Multi-strat | ✓ | ✓ | ✓ | 🔄 |
| 7-11 | Enhancement | ✓ | ✓ | ✓ | 📋 |
| 12-14 | Production | ✓ | ✓ | ✓ | 📋 |

## Cumulative Metrics

- Week 0: 3 commits, 0 LOC
- Week 2: 8 commits, 300 LOC Python
- Week 4: 16 commits, 300 LOC Python + 250 LOC C++
- Week 6: 30 commits, 800 LOC Python + 600 LOC C++
- Week 11: 80 commits, 3500 LOC Python + 2500 LOC C++
- Week 14: 150+ commits, 4000 LOC Python + 3000 LOC C++

## GitHub Milestones Achieved

- ✅ Milestone 1: Foundations (Week 1)
- ✅ Milestone 2: Pipeline Bridge (Week 7)
- 🔄 Milestone 3: Enhancement Complete (Week 11)
- 📋 Milestone 4: Production Ready (Week 14)

## Next Phase (Optional)

- Real API integration (paper trading)
- Machine learning strategies
- Advanced optimization
- Cloud deployment

---
```

---

# 📌 Final Notes

These templates are **living documents**. As you:
- Discover better prompts → update `AI_PROMPTS.md`
- Hit blockers → document solution in template
- Find shortcuts → share with future self

**Make it yours.** Customize templates to your style.

**Commit templates** to GitHub so anyone can follow your journey.

Good luck! 🚀

---

**Last Updated:** 2025-11-06  
**Template Version:** 1.0  
**Ready to start:** Week 0 ✓
"Create Python script to:
1. Download AAPL stock data from Yahoo Finance (5 years)
2. Save to CSV: data/AAPL.csv
3. Print: number of rows, date range, columns

Use yfinance library. Include error handling"
```

**Validation:**
- [ ] CSV file created
- [ ] Data looks reasonable
- [ ] Commit: `git add data/AAPL.csv && git commit -m "Add AAPL historical data"`

**Time spent:** ____ min

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
  
- calculate_indicators() → adds SMA columns
  * self.data['SMA20'] = rolling average 20 days
  * self.data['SMA50'] = rolling average 50 days
  
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

**Validation:**
- [ ] Code runs without errors
- [ ] Produces reasonable results
- [ ] Docstrings for all methods
- [ ] Handles missing data gracefully
- [ ] Commit: `git add python/backtester/ && git commit -m "Backtest engine v1 - MA strategy"`

**Time spent:** ____ min

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

2. Run: `python scripts/test_backtest.py`

3. Save output to file: `python scripts/test_backtest.py > results/backtest_output.txt`

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

4. Also save this output to results/backtest_output.txt"
```

**Validation:**
- [ ] Script runs
- [ ] Output looks reasonable
- [ ] Metrics make sense
- [ ] Commit: `git add python/scripts/test_backtest.py && git commit -m "Test backtest - results look good"`

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
bt.export_trades_to_csv('results/backtest_trades.csv')
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
   bt.export_trades_to_csv('results/AAPL_trades.csv')

3. Verify: CSV readable in Excel/spreadsheet"
```

**Validation:**
- [ ] CSV file created: `results/AAPL_trades.csv`
- [ ] Contains all trades
- [ ] Columns correct
- [ ] Can open in Excel
- [ ] Commit: `git add results/ && git commit -m "Export backtest trades to CSV"`

**Time spent:** ____ min

---

### Task 5: Create Visualization (1h)

**What to do:**

Create `python/scripts/plot_results.py`:

```python
import matplotlib.pyplot as plt
import pandas as pd

# Load backtest results
results = pd.read_csv('results/backtest_trades.csv')

# Plot: cumulative PnL over time
plt.figure(figsize=(12, 6))
plt.plot(results.index, results['cumulative_pnl'])
plt.title('Cumulative PnL - AAPL Backtest')
plt.xlabel('Trade Number')
plt.ylabel('Cumulative PnL ($)')
plt.grid(True)
plt.savefig('results/equity_curve.png', dpi=150)
print("✓ Chart saved to results/equity_curve.png")
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
   
4. Save to results/equity_curve.png
5. Print: 'Chart saved!'

Use matplotlib"
```

**Validation:**
- [ ] Chart created
- [ ] Shows cumulative PnL over time
- [ ] File saved: `results/equity_curve.png`
- [ ] Commit: `git add results/equity_curve.png && git commit -m "Add equity curve visualization"`

**Time spent:** ____ min

---

## ✅ Weekly Checklist

- [ ] Backtest engine coded (SimpleBacktest class)
- [ ] AAPL data loaded correctly
- [ ] Indicators calculated (SMA20, SMA50)
- [ ] Signals generated
- [ ] Backtest runs without errors
- [ ] Results exported to CSV
- [ ] Equity curve visualization created
- [ ] 5+ commits made

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

## 🔗 Resources Used

- [Pandas documentation](https://pandas.pydata.org/docs/)
- [Matplotlib examples](https://matplotlib.org/examples/)
- [yfinance docs](https://github.com/ranaroussi/yfinance)

---

**Status:** 🔄 In Progress / ✅ Complete  
**Confidence Level:** 1 ☆☆☆☆☆ 5 - Rate: ____  
**Ready for Week 2-3:** [ ] Yes [ ] No  

**Next week:** Multi-strategy framework + parameter optimization

```

---

## 📋 WEEK 3-4: C++ Foundations & Simple Program

**File:** `docs/WEEK_03_CPP_FOUNDATIONS.md`

```markdown
# Week 3-4: C++ Fundamentals & First Working Program

**Duration:** Days 22-35 (12 hours total, 6h/week)  
**Status:** 🔄 In Progress / ✅ Complete  
**Effort:** Medium-Hard (learning language syntax)

---

## 🎯 Goals This Week

- [ ] Understand pointers and references (critical!)
- [ ] Learn STL containers: vector, map
- [ ] Write and compile first C++ program
- [ ] Read CSV file into data structure
- [ ] Calculate simple indicator (SMA)
- [ ] Output to console
- [ ] 5+ commits

---

## 📚 Learning Path

### Pre-Week Learning (3h)

**What to learn:**
- C++ syntax basics (variables, types, control flow)
- Functions and scope
- Pointers & references (very important!)
- Classes and objects
- STL containers

**Resources:**
- freeCodeCamp C++ video: https://www.youtube.com/watch?v=vLnPJ8SOHQE (4h)
  Watch at 1.5x speed, focus on: variables, pointers, classes
  
- C++ Primer chapters 1-7 (read, don't memorize)

**LeetCode Practice (2h):**
- 5-7 easy problems: string manipulation, arrays
- Goal: get comfortable with syntax

**AI Agent Learning:**
```
"I'm new to C++. Explain these concepts like I'm 5:

1. Pointers: What are they? Why use them?
2. References: How different from pointers?
3. Vector: Why use instead of arrays?
4. Map: When to use?

Show code examples for each, keep simple"
```

**Checklist:**
- [ ] Understand pointers conceptually
- [ ] Know difference between pointer and reference
- [ ] Know what vector and map do
- [ ] Completed 5+ LeetCode problems

---

## 🛠️ Main Tasks

### Task 1: C++ Basics Practice (3h)

**What to do:**

Create `cpp/practice/` folder with exercises:

1. **hello.cpp** - Print statement
2. **data_types.cpp** - Variables, types, casting
3. **functions.cpp** - Function definition and calls
4. **pointers.cpp** - Pointer declaration, dereferencing
5. **vectors.cpp** - Vector creation, push_back, iteration

**AI Agent Prompt:**
```
"Create 5 beginner C++ programs:

1. hello.cpp: Print 'Hello, Quant!' to console

2. data_types.cpp: 
   - Create: int, double, string variables
   - Print each with its value
   
3. functions.cpp:
   - Function: calculateSum(int a, int b) → int
   - Main: call function, print result
   
4. pointers.cpp:
   - Create int variable
   - Create pointer to it
   - Print variable value via pointer
   - Change value via pointer
   
5. vectors.cpp:
   - Create vector of doubles
   - Add 5 numbers with push_back()
   - Print each number in loop
   - Calculate sum using loop

Each file: 10-20 lines
Include comments
Make sure each compiles: g++ -o program program.cpp"
```

**Compilation & Testing:**
```bash
cd cpp/practice
g++ -o hello hello.cpp && ./hello
g++ -o data_types data_types.cpp && ./data_types
# etc for each
```

**Validation:**
- [ ] All 5 programs compile
- [ ] Each runs without errors
- [ ] Output reasonable
- [ ] Commit: `git add cpp/practice/ && git commit -m "C++ basics exercises - 5 programs working"`

**Time spent:** ____ min

---

### Task 2: Structs & Simple Data Structures (2h)

**What to do:**

Create `cpp/practice/ohlc_struct.cpp`:

**Specifications:**
1. Struct OHLC with fields: date, open, high, low, close
2. Function to calculate daily return
3. Function to read OHLC from CSV
4. Store in vector of OHLC
5. Print first 5 bars

**AI Agent Prompt:**
```
"Create C++ program with OHLC struct:

1. Struct OHLC:
   - date: string (YYYY-MM-DD)
   - open, high, low, close: double
   - Method: getDailyReturn() → double
     * (close - open) / open * 100
   
2. Function: loadOHLCFromCSV(filename) → vector<OHLC>
   - Read CSV file
   - Each row → OHLC struct
   - Return vector of all OHLC
   - Error handling: file not found
   
3. main():
   - Load AAPL.csv
   - Print first 5 bars: date, close, daily_return
   - Print last 5 bars
   
Include:
- #include statements
- Error handling
- Comments
- Compile with: g++ -o ohlc ohlc_struct.cpp"
```

**Expected output:**
```
Date        Close   Daily Return (%)
2020-01-02  75.09   -0.50
2020-01-03  74.37   -0.95
...
```

**Validation:**
- [ ] Compiles without errors
- [ ] Loads CSV correctly
- [ ] Calculates returns
- [ ] Output matches expectations
- [ ] Commit: `git add cpp/practice/ohlc_struct.cpp && git commit -m "OHLC struct and CSV loading"`

**Time spent:** ____ min

---

### Task 3: SMA Calculation in C++ (2h)

**What to do:**

Create `cpp/practice/sma_calculator.cpp`:

**Specifications:**
1. Function: calculateSMA(vector<double>& prices, int window) → vector<double>
2. Load AAPL data
3. Extract closing prices
4. Calculate SMA(20)
5. Print: date, close, SMA20

**AI Agent Prompt:**
```
"Create C++ program to calculate SMA:

1. Function: calculateSMA(vector<double>& prices, int window)
   - Input: price series, window size
   - Output: vector of SMA values
   - Algorithm: simple average of last 'window' prices
   - Handle: first 'window-1' values are NaN
   
2. Class: PriceAnalyzer
   - Member: vector<OHLC> data
   - Member: vector<double> sma20
   - Method: loadData(filename)
   - Method: calculateSMA()
   - Method: printResults()
   
3. main():
   - Create PriceAnalyzer
   - Load AAPL.csv
   - Calculate SMA(20)
   - Print first 50 bars: date, close, sma20
   
Include: OHLC struct from previous exercise"
```

**Expected output:**
```
Date        Close    SMA20
2020-01-02  75.09    NaN
...
2020-02-21  74.24    76.52
2020-02-24  73.45    76.48
```

**Validation:**
- [ ] SMA calculated correctly
- [ ] Matches Python backtest SMA values
- [ ] Output reasonable
- [ ] Compiles without warnings
- [ ] Commit: `git add cpp/practice/sma_calculator.cpp && git commit -m "SMA calculation in C++"`

**Time spent:** ____ min

---

### Task 4: Project Structure & CMake (2h)

**What to do:**

Create professional C++ project structure:

```
cpp/
├── CMakeLists.txt         (Build config)
├── include/               (Headers)
│   ├── data_loader.h
│   └── price_analyzer.h
├── src/                   (Implementation)
│   ├── data_loader.cpp
│   ├── price_analyzer.cpp
│   └── main.cpp
├── practice/              (Learning exercises)
└── build/                 (Generated by CMake)
```

**CMakeLists.txt:**
```cmake
cmake_minimum_required(VERSION 3.10)
project(QuantBot)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -O2")

# Include directories
include_directories(include)

# Source files
set(SOURCES
    src/main.cpp
    src/data_loader.cpp
    src/price_analyzer.cpp
)

# Create executable
add_executable(trading_bot ${SOURCES})

# Optional: for later use
# find_package(Boost REQUIRED)
# target_link_libraries(trading_bot Boost::system)
```

**AI Agent Prompt:**
```