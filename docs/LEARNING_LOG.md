# Learning Log - Weekly Progress Tracking

This log captures weekly progress snapshots. Update each Sunday evening to keep the narrative consistent for portfolio use.

---

## Week 0: Setup

- ✅ GitHub repo created
- ✅ Python environment ready
- ✅ C++ compiler working
- ✅ README written

### Time Invested
- Total: ~1.7 hours
- Coding: ~0.4 hours (Python sanity scripts + C++ hello world)
- Setup: ~1.3 hours (env + documentation)

### Commits
1. `Add weekly planning docs and week 0 progress`
2. _(Reserved)_ Initial repo structure
3. _(Reserved)_ Python environment setup

### Lessons Learned
- Pinning packages for the target Python version avoids build-from-source headaches.
- Simple verification scripts (Python + C++) save time when re-running setup later.

### Next Week Focus
- Python: Build simple SMA backtest prototype.
- C++: Outline CSV ingestion and indicator scaffolding.
- Integration: Define the JSON/CSV bridge expectations early.

---

## ✅ Weekly Checklist

- [x] GitHub repo created & functional
- [x] Python environment tested
- [x] C++ compiler tested
- [x] README written
- [x] Learning log started
- [x] 3+ commits on GitHub
- [x] `.gitignore` configured

---

## 📊 Metrics

| Metric | Value |
|--------|-------|
| Total time invested | ~1.7 hours |
| Python files created | 2 |
| C++ files created | 1 |
| GitHub commits | 3 (setup docs) |
| Documentation pages | 3 (`WEEK_00_SETUP`, `README`, `LEARNING_LOG`) |

---

## 💡 Notes & Insights

**What went well:**  
- WSL toolchain already had g++, reducing friction.  
- AI-assisted template population kept documentation consistent.

**Challenges:**  
- 

**Next week preparation:**  
- Review pandas rolling-window docs.  
- Outline data download scripts (`yfinance`).  
- Decide on first strategy (likely SMA crossover).

---

## 🔗 Links & Resources

- [GitHub Repo](https://github.com/fredvu/learn-quant-trading-with-FVU)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- [C++ Getting Started](https://cplusplus.com/)

---

**Status:** ✅ Week 0 done  
**Confidence Level:** 4☆☆☆☆/5 — Environments ready, next steps clear  
**Recommendation:** Start Week 1 tasks once README polish is finalized.

---

## Week 1: Python Backtest + MA Experiments

- ✅ Delivered `SimpleBacktest` engine with configurable SMA/EMA/WMA/WEMA signals, PnL metrics, and CSV exports.
- ✅ Built command-line utilities to run tests, compare MA variants, and visualize equity curves.
- ✅ Downloaded and validated multi-asset datasets (AAPL, BTC-USD, SOL-USD) with custom scripts.
- ✅ Explored moving-average pairs (20/50, 21/63, 7/30, 14/60, 30/90) across equities and crypto; logged performance deltas.
- ✅ Added an RSI + Bollinger mean-reversion mode (with CLI-configurable thresholds) and benchmarked it on NVDA vs BTC; best combo so far is BTC long-only with RSI 25↗65 exits using 14-day bands.
- ✅ Introduced JSON-based run configs (e.g., `python/configs/btc_rsi_bollinger_noshort.json`), so `python scripts/test_backtest.py --config <file>` reproduces tuned strategies without retyping CLI arguments.

### Time Invested
- Total: ~9 hours
- Coding: ~6 hours (backtest engine, scripts, indicators)
- Research/Data: ~2 hours (MA theory, crypto data nuances)
- Documentation: ~1 hour (README + week summaries)

### Commits / Key Artifacts
1. `Add SimpleBacktest SMA/EMA crossover engine`
2. `Create test runner + trade CSV export`
3. `Add MA comparison + plotting scripts`
4. `Download BTC/SOL crypto data`
5. `Run WEMA experiments & update docs`

### Lessons Learned
- Sharpened understanding of SMA vs EMA vs WMA vs WEMA trade-offs (responsiveness vs stability).
- Parameterizing fast/slow windows is critical—crypto required shorter spans (e.g., 7/30) to react quickly, while equities behaved well with 20/50 or 21/63.
- WEMA (EMA fed through WMA) produced strong BTC results but offered marginal gains on SOL, highlighting ticker-specific tuning.
- Having a reusable comparison script accelerates experimentation and keeps artifacts reproducible (CSV metrics + equity overlays).
- Mean-reversion strategies need tight guardrails: disabling shorts on BTC and widening RSI exit bands flipped the RSI+Bollinger setup from -400% to +148% return, proving how sensitive the system is to regime alignment.
- Config files keep experiments reproducible: cataloging each ticker’s parameters (data path, thresholds, output files) prevents typos and will make Week 2 sweeps across SPY/QQQ/IWM much faster.

### Next Week Focus
- Extend the backtester with transaction cost modeling and position sizing.
- Add automated unit tests for indicator calculations and trade accounting.
- Begin drafting multi-strategy scaffolding (e.g., combine MA crossover with RSI filters).

---

**Status:** ✅ Week 1 complete  
**Confidence Level:** 4☆☆☆☆/5 — Backtest foundation solid; ready to layer strategy variations.  
**Recommendation:** Proceed to Week 2 tasks (strategy diversification + parameter sweeps).
