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

## Week 2: Index ETFs, WEMA sweeps, and RSI gates

- ✅ Ported the Week 1 backtester to SPY + QQQ datasets and automated eight MA crossover variants (SMA, EMA, WEMA) per ticker with reproducible configs.
- ✅ Logged per-run trade CSVs, CLI outputs, and equity curves under `results/week2/` so every experiment (20/50 through 5/30) has matching artifacts.
- ✅ Identified WEMA21/63 (SPY) and WEMA14/60 (QQQ) as the highest-return crossovers; WEMA5/30 emerged as the best Sharpe on SPY thanks to shallow drawdowns.
- ✅ Added an RSI gating option to the MA engine plus CLI flags, then benchmarked WEMA14/60 with RSI filters (35-65, 40-70, 45-65) to reduce whipsaws.
- ✅ Built comparison configs (`python/configs/week2_*_runs.json`) so running `python scripts/compare_configs.py --config ...` regenerates summary CSVs + combined plots on demand.
- ✅ Layered beginner-friendly strategies (MACD, Donchian, ATR trailing stops) plus ATR% volatility gates and RSI exit filters across SPY/QQQ/BTC/NVDA/META/MSFT/PLTR.

### Time Invested
- Total: ~14 hours
- Coding: ~7 hours (MACD/Donchian/ATR enhancements, ATR% gates, CLI updates)
- Research/Data: ~4 hours (strategy testing across tickers)
- Documentation + write-up: ~3 hours (blog update + logs)

### Time Invested
- Total: ~11 hours *(before add-ons; see updated totals above)*
- Coding: ~5 hours (engine enhancements, RSI gating, automation scripts)
- Research/Data: ~3 hours (ETF regime analysis, RSI filter design)
- Documentation + write-up: ~3 hours (learning log + blog post)

### Commits / Key Artifacts
1. `Add compare_configs automation + SPY presets`
2. `Catalog QQQ MA sweeps + plots`
3. `Implement RSI gating for MA crossover`
4. `Add SPY/QQQ WEMA14 RSI filter configs`
5. `Document Week 2 insights (learning log + blog)`
6. `Add MACD/Donchian strategies + ATR stops/gates`
7. `Run ATR% volatility experiments on NVDA/META/MSFT/PLTR`

### Lessons Learned
- Broad-market ETFs prefer smoother windows: SPY rewarded slower WEMAs (21/63) while QQQ responded best to 14/60 due to tech momentum.
- RSI filters shine when the underlying market trends strongly (QQQ). Keeping RSI between 40-70 boosted Sharpe to 1.0 while lowering drawdown, proving the value of gating entries to “neutral” momentum ranges.
- The same RSI idea on SPY offered marginal benefit—returns stayed flat while trade count tripled—highlighting that filters must be ticker-specific.
- Automating both trade exports and equity curve plots per run makes it trivial to audit results weeks later; capturing logs alongside CSVs pays off when compiling narratives.
- MACD/Donchian without position sizing barely move the needle—highlighting the need for short-selling or broader trend filters before they’re useful.
- ATR trailing stops (SPY) and ATR% gates (META/NVDA/MSFT) provide intuitive risk controls and help target higher-volatility regimes; thresholds are ticker-specific (e.g., 2% worked for NVDA/META, 1.2% for MSFT).

### Next Week Focus
- Integrate transaction cost + slippage modeling to see how higher-turnover filters hold up.
- Build cross-ticker comparison dashboards (SPY vs QQQ) to spot parameter overlap.
- Start layering ATR/volatility throttles on top of WEMA + RSI to avoid dead regimes.

---
