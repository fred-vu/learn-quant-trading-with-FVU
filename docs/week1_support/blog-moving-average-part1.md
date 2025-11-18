# Moving Averages, Part 1: From Simple To Advanced (SMA → HMA)

*By Fred Vu – Week 1 Learning Log*

---

## The First Line You Ever Plot

Open any charting platform, and the first overlay almost everyone adds is a moving average (MA). It is the technician’s version of a compass: simple, trustworthy, and always available. But “moving average” is not a single tool — it is an entire family, each variant tuned for a different job. This post takes you from the classic Simple Moving Average through faster, more responsive cousins such as EMA, WMA, and HMA.

---

## 1️⃣ Moving Average 101 – Why We Care

- **Purpose:** smooth price to reveal trend direction and filter noise.
- **Core idea:** instead of staring at jagged candles, we average the last `N` data points and plot the result as a line.
- **Reality check:** every MA has a trade-off between *smoothness* (less noise) and *responsiveness* (less lag). Knowing that trade-off is the only way to choose the right line.

---

## 2️⃣ The Foundational Duo: SMA & EMA

### Simple Moving Average (SMA) – “The Anchor”
- **Definition:** arithmetic mean of the last `N` closes.  
  ```math
  SMA_t = \frac{1}{N} \sum_{i=0}^{N-1} Close_{t-i}
  ```
- **Strengths:** extremely smooth; great for defining macro trend (50/100/200-day).
- **Weaknesses:** slow to react because every observation gets equal weight.
- **Use cases:** position trading, institutional dashboards, identifying bull/bear regimes.

### Exponential Moving Average (EMA) – “The Accelerator”
- **Definition:** weighted mean with exponential decay; latest candle has weight `α = 2/(N+1)`.
  ```math
  EMA_t = α·Close_t + (1-α)·EMA_{t-1}
  ```
- **Strengths:** reduces lag dramatically, perfect for swing/day trades.
- **Weaknesses:** can whipsaw in ranging markets.
- **Use cases:** EMA 9/20 for momentum confirmation; EMA 50 for medium-term bias.

💡 *Experiment recap:* plotting SMA20 vs EMA20 on AAPL shows EMA hugs price more tightly and flips direction earlier — exactly what we observed in the backtester.

---

## 3️⃣ Weighted Moving Average (WMA) – “Linear Priority”

- **Definition:** linear weights (Newest = `N`, Oldest = `1`).  
  ```math
  WMA_t = \frac{\sum_{i=1}^{N} i·Close_{t-N+i}}{\sum_{i=1}^N i}
  ```
- **Comparison:** sits between SMA and EMA. It reacts quickly but remains deterministic (no recursive formula).
- **In practice:** our BTC tests showed WMA(20/50) outperformed SMA/EMA on SOL, highlighting its balanced response.

---

## 4️⃣ Hull Moving Average (HMA) – “Formula One”

- **Concept:** Alan Hull blended multiple WMAs (with periods `N/2`, `N`, `√N`) to create a line that’s both fast and smooth.
- **Why it matters:** compared to EMA/WMA, HMA drops lag even further, making it popular for scalpers who need instant visual confirmation.
- **Caveat:** because it “turns on a dime,” it can overshoot highs/lows during violent reversals.

---

## 5️⃣ Bonus Mentions: DEMA & TEMA

- **Double EMA (DEMA)** and **Triple EMA (TEMA)** subtract lag components from EMA by layering the indicator on itself.
- They are easier to compute than HMA and are widely available in trading libraries — ideal if your platform lacks HMA.

---

## 6️⃣ Practical Playbook

1. **Trend Filter:** price above SMA50 → only long setups; below → only shorts. Add EMA20 for short-term bias.
2. **Dynamic Support/Resistance:** in strong uptrends, watch for pullbacks into EMA20 or WMA30 as springboards.
3. **Classic Crossovers:** fast EMA/WMA vs slow SMA. Golden Cross (fast crosses above slow) = bullish regime, Death Cross = bearish.

---

## 7️⃣ Checklist For Your Charts

- [ ] Plot SMA50 + EMA20 on your main ticker.
- [ ] Add WMA (or HMA if available) and compare response time.
- [ ] Note where whipsaws happen — is it because the market is ranging or because your window is too short?
- [ ] Backtest your favorite pair (e.g., 20/50, 7/30) before trading live.

---

**Next Post (Part 2):** We’ll move from “fast vs slow” into *adaptive* territory: WEMA, KAMA, and intelligent moving averages that rewrite their own rules on the fly. Stay tuned!
