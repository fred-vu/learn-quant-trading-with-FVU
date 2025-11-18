# Week 2 Deep Dive: WEMA Crossovers + RSI Neutral Filters

*By Fred Vu – Week 2 Learning Log*

---

## TL;DR

This week I stress-tested weighted EMA (WEMA) crossovers on US index ETFs (SPY, QQQ) and then layered an RSI “neutral zone” (e.g., 40–70) so trades only fire when momentum sits between overbought/oversold extremes. The combo delivered a **Sharpe of 1.0 on QQQ** with max drawdown under **−0.8%**, while SPY preferred the unfiltered WEMA styles. Every experiment—including logs, trades, and plots—now lives under `results/week2/` for auditability.

---

## 1. Why WEMA + RSI?

1. **WEMA advantage:** EMA responsiveness + WMA smoothing removes a lot of the chop that derails SMA crossovers.
2. **RSI neutral gating:** Instead of only entering when RSI is oversold (<30), we *only* allow trades when RSI is between 40 and 70. This keeps us out of emotional spikes and forces entries to happen in calm “trend continuation” zones.
3. **ETF focus:** Index ETFs (SPY, QQQ) have plenty of overlapping institutions and respond well to regime filters; perfect proving ground before touching single stocks again.

---

## 2. Baseline MA Sweeps

| Ticker | Best Raw MA | Return | Sharpe | Trades | Notes |
|--------|-------------|--------|--------|--------|-------|
| SPY | WEMA21/63 | +3.07% | 0.96 | 6 | Cleanest crossover, low turnover. |
| SPY | WEMA5/30 | +3.06% | **0.99** | 16 | Same return as 21/63 but half the drawdown (−0.51%). |
| QQQ | WEMA14/60 | **+3.20%** | 0.89 | 7 | Tech momentum loves slightly faster windows. |
| QQQ | EMA21/63 | +3.13% | 0.89 | 10 | More churn, similar profile to WEMA14/60. |

Paths: see `results/week2/comparisons/spy_week2_summary.csv` and `.../qqq_week2_summary.csv`.

---

## 3. Adding RSI Neutral Filters (QQQ Shines)

Config reference: `python/configs/week2_qqq_wema14_rsi_runs.json`.

| Label | RSI Band | Return | Max DD | Sharpe | Trades | Takeaway |
|-------|----------|--------|--------|--------|--------|----------|
| QQQ WEMA14/60 | None | +3.20% | −0.88% | 0.89 | 7 | Baseline trend follower. |
| QQQ WEMA14/60 RSI35-65 | 35–65 | +2.77% | −0.85% | 0.89 | 82 | Highest win rate (78%) but lower efficiency. |
| **QQQ WEMA14/60 RSI40-70** | **40–70** | **+3.24%** | **−0.74%** | **1.00** | 60 | Sweet spot: same return, better Sharpe, modest drawdown. |
| QQQ WEMA14/60 RSI45-65 | 45–65 | +2.70% | −0.71% | 0.99 | 100 | Too restrictive—return drops despite more trades. |

Why 40–70 works:
- Keeps us in trades during grindy trends but cuts off entries when RSI is extreme.
- 60 trades over five years (~1 per month) is manageable.
- Drawdown falls below 1%, so the equity curve (`results/week2/equity_curves/equity_curve_qqq_wema14_60_rsi40_70.png`) looks like a stair-step instead of a rollercoaster.

---

## 4. SPY: RSI Helps Less

Config reference: `python/configs/week2_spy_wema14_rsi_runs.json`.

| Label | RSI Band | Return | Max DD | Sharpe | Trades | Takeaway |
|-------|----------|--------|--------|--------|--------|----------|
| SPY WEMA14/60 | None | +2.81% | −1.07% | 0.89 | 9 | Baseline. |
| SPY WEMA14/60 RSI35-65 | 35–65 | +2.63% | −1.04% | 0.92 | 82 | Slight Sharpe uptick but 9× more trades. |
| SPY WEMA14/60 RSI40-70 | 40–70 | +2.63% | −0.98% | 0.91 | 59 | Marginal gains in DD; still high turnover. |
| SPY WEMA14/60 RSI45-65 | 45–65 | +2.09% | −1.07% | 0.82 | 109 | Over-filtered; performance slips. |

Interpretation: SPY’s macro trend is steadier, so WEMA already filters whipsaws. RSI gating raises trade count dramatically without boosting returns—only use it if you crave higher win rates (60–78%).

---

## 5. Bonus: BTC WEMA21/63 + RSI exits

I revisited the “hero trade” from Week 1—BTC with WEMA21/63—and asked whether RSI filters could tame its 47% drawdowns without killing the 10x return.

| Label | Config | Return | Max DD | Sharpe | Trades | Notes |
|-------|--------|--------|--------|--------|--------|-------|
| BTC WEMA21/63 | No RSI | +1,009% | −46.9% | 0.98 | 11 | Classic trend follower, few but huge trades. |
| BTC WEMA21/63 RSI 25-85 | Entry filter | +1,016% | −53.4% | 0.97 | 19 | Matches baseline; wide band avoids chopping trends. |
| BTC WEMA21/63 RSI exit ≥ 85 | Exit-only | **+1,047%** | −48.4% | **0.99** | 21 | Best balance—adds a few trades and clips blow-off tops. |
| BTC WEMA21/63 RSI exit ≥ 80 | Exit-only | +917% | −47.8% | 0.93 | 51 | Too eager; gives up 13% return for more churn. |

Takeaways:
1. **Wide neutral zones** (25–85) are safe for BTC, but narrow bands (35–65) suffocate the moves that make the trend profitable.
2. **RSI exits beat RSI entries**. Let WEMA21/63 handle entries, then peel off when RSI ≥ 85 to lock in parabola peaks without missing the bulk of the run.
3. Pushing the exit down to 80 triggers >50 trades and cuts total return. Use higher thresholds (80–90) and test per regime.

Artifacts: `results/week2/logs/backtest_output_btc_wema21_63_rsi25_85.txt`, `..._rsi_exit85.txt`, `..._rsi_exit80.txt`, plus their equity curves in `results/week2/equity_curves/`.

---

## 5. Implementation Notes

1. **Engine upgrade:** `SimpleBacktest` now accepts `use_rsi_filter`, `ma_rsi_lower`, and `ma_rsi_upper`. When enabled, RSI is computed alongside the MAs and signals are zeroed whenever RSI leaves the band.
2. **CLI hooks:** run `python scripts/test_backtest.py --use-ma-rsi-filter --ma-rsi-lower 40 --ma-rsi-upper 70 ...` to gate any MA crossover.
3. **Automation:** 
   ```bash
   python scripts/compare_configs.py --config configs/week2_qqq_wema14_rsi_runs.json --label qqq_wema14_rsi_filters
   ```
   This regenerates the summary CSV (`results/week2/comparisons/qqq_wema14_rsi_filters_summary.csv`) and the multi-line equity plot.

---

## 6. Key Takeaways

- **QQQ loves the RSI neutral zone:** WEMA14/60 + RSI 40–70 beat every raw crossover on risk-adjusted return without inflating drawdowns.
- **SPY is indifferent:** stick with WEMA21/63 or WEMA5/30 unless you specifically want more trades/win rate.
- **Filters are asset-specific:** copy-pasting RSI bands across tickers is risky; always validate per asset.
- **Artifacts matter:** Having logs, trade CSVs, and PNGs per run made this write-up painless and keeps week-to-week analysis reproducible.

---

## 7. What’s Next?

1. **Add cost/slippage modeling** – RSI bands create more trades; we need to see if the edge survives $0.01/share or 2 bps.
2. **Cross-ticker dashboards** – compare SPY vs QQQ results side-by-side to catch parameter overlap.
3. **Volatility throttles** – layer ATR % filters so the system only trades when there’s enough movement to justify risk.

---

*Artifacts referenced:*
- Results CSVs: `results/week2/comparisons/spy_week2_summary.csv`, `results/week2/comparisons/qqq_week2_summary.csv`, `results/week2/comparisons/*_wema14_rsi_filters_summary.csv`
- Equity curves: `results/week2/equity_curves/`
- Logs + trades: `results/week2/logs/`, `results/week2/trades/`
