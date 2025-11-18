# Moving Averages, Part 2: Intelligent & Adaptive (WEMA → KAMA)

*By Fred Vu – Week 1 Learning Log*

---

## When Moving Averages Start Thinking For Themselves

If Part 1 was about tuning knobs (fast vs slow), Part 2 explores indicators that *adapt*. Instead of picking a single window and hoping it fits every market condition, we now let the math respond dynamically:  **weighting price differently** when volatility **explodes** vs when markets drift **sideways**.

---

## 1️⃣ WEMA – Weighted Exponential Moving Average

- **How we built it:** run EMA to smooth noise, then feed the EMA output into a WMA. This compounds two weighting schemes: exponential decay + linear emphasis on the newest bars.
- **Formula sketch:**
  ```python
  ema = Close.ewm(span=N, adjust=False).mean()
  wema = weighted_moving_average(ema, N)
  ```
- **Why it matters:** compared to EMA alone, WEMA stays responsive yet reduces false flips thanks to the second smoothing pass.
- **Backtest insight:** WEMA(21/63) on BTC turned $10k into ~$111k with only 11 trades — outstanding trend capture with acceptable DD (~47%). On SOL, WEMA’s edge shrank, signaling that responsiveness must match asset volatility.

---

## 2️⃣ KAMA – Kaufman’s Adaptive Moving Average

- **Concept:** uses the Efficiency Ratio (ER) to determine whether the market is trending or noisy.
  - ER close to 1 → strong trend → KAMA speeds up (short EMA behavior).
  - ER near 0 → choppy range → KAMA slows down (long SMA behavior).
- **Implementation notes:** requires tracking price displacement vs absolute volatility over a lookback window; then adjust the smoothing constant accordingly.
- **When to use:** swing systems that alternate between trend and mean-reversion phases; KAMA can throttle itself without user intervention.

---

## 3️⃣ Other Adaptive All-Stars

- **VIDYA (Variable Index Dynamic Average):** adjusts smoothing based on volatility index (CCI or RSI-based). Helpful when you care more about volatility than direction.
- **TSF (Time Series Forecast / Adaptive EMA):** incorporates linear regression slope to anticipate future values.
- **Jurík Moving Average (JMA):** proprietary but beloved for extremely low lag in high-frequency environments.

---

## 4️⃣ Strategy Patterns With Intelligent MA

1. **Trend Quality Detector:** combine WEMA with a volatility filter (ATR or Bollinger bandwidth). Only take trades when WEMA slope exceeds a threshold *and* ATR is rising.
2. **Dual-MA Adaptive Crossover:** fast = WEMA(14), slow = KAMA(40). The fast line reacts to price shocks; the slow line adapts to regime. This reduces chop compared to EMA vs SMA.
3. **Crypto Momentum Stack:** 
   - BTC/ETH: WEMA(21/63) + EMA(9) to identify primary trend vs micro pullbacks.
   - SOL/altcoins: WMA or EMA to capture faster cycles; use KAMA as a filter to avoid sideways phases.

---

## 5️⃣ Implementation Blueprint (Python)

```python
from backtester.simple_backtest import SimpleBacktest

bt = SimpleBacktest(
    csv_file="data/BTC_USD_2020-01-01_2025-11-01.csv",
    moving_average="wema",
    fast_window=21,
    slow_window=63,
)
bt.load_data()
bt.calculate_indicators()
bt.generate_signals()
bt.run()
bt.export_trades_to_csv("results/week1/trades/backtest_trades_BTC_WEMA_21_63.csv")
```

Need fast experimentation? Run:
```
python scripts/compare_ma_types.py \
  --data ../data/BTC_USD_2020-01-01_2025-11-01.csv \
  --fast-window 21 --slow-window 63
```
This outputs metrics and multi-line equity curves into `results/week1/`.

---

## 6️⃣ Lessons From Week 1 Experiments

- **No one-size-fits-all:** BTC loved WEMA/WMA, SOL hardly cared (returns hovered around +1–2%). Always cross-check per ticker.
- **Window selection matters more than indicator type** when the asset has clear cycles (7/30 for BTC captured short bursts; 30/90 captured macro swings).
- **Adaptive ≠ perfect:** WEMA got every BTC trade right in the 30/90 test but still suffered −55% drawdown — proof that trend followers must stomach volatility.

---

## 7️⃣ Checklist Before Going Live

- [ ] Run `compare_ma_types.py` across multiple window pairs.
- [ ] Inspect equity curve overlays to see which MA lags or overshoots in the current regime.
- [ ] Add transaction costs/slippage to your backtests (Week 2 goal).
- [ ] Journal observations in `docs/week1_support/QMC.md` to lock in the theory.

---

**Takeaway:** Intelligent moving averages can adapt to market regimes, but they don’t replace judgment. They’re best used as *regime filters* paired with risk management. Master the basics (SMA/EMA) first, then layer WEMA/KAMA where they shine.
