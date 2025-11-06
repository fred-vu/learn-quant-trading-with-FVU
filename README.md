# Quant Trading Bot: From Zero to Hero

A comprehensive learning project to build a trading bot using Python + C++, leveraging AI agents for rapid development and documentation. The repo mirrors a 4.5‑month roadmap that goes from environment setup to a portfolio-ready bot.

## 🎯 Project Goal

Build a working trading bot by:
- Developing trading strategies, backtests, and data tooling in Python.
- Implementing high-performance order management and indicators in C++.
- Using AI coding agents to prototype quickly while documenting every step.

## 🚀 Quick Start

```bash
# Clone and enter the repo
git clone git@github.com:fredvu/learn-quant-trading-with-FVU.git
cd learn-quant-trading-with-FVU

# Python backtest environment
cd python
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python test_setup.py  # sanity check

# C++ practice build
cd ../cpp
mkdir -p build && cd build
cmake ..
make
./trading_bot   # future executable
```

## 📊 Project Status

- Week 0 (Setup): ✅ In progress, environments validated
- Week 1-2 (Python Backtest): 📋 Preparing
- Month 2 (Integration/C++ focus): 📋 Planning
- Month 3+ (Enhancements & Production): 📋 Planning

## 📚 Documentation

- `docs/ROADMAP.md` – 4.5‑month high-level roadmap
- `docs/WEEK_00_SETUP.md` – Current week’s checklist and notes
- `docs/WEEK_01_PYTHON_BACKTEST.md` – Next-week plan for the backtest engine
- `docs/MASTER_PROGRESS.md` – Timeline and metrics overview
- `docs/weekly_templates.md` – Source templates for future weeks

## 🤖 Using AI Agents

This project intentionally pairs human learning with AI copilots (ChatGPT/Codex, Claude, etc.). Prompts and responses are logged to accelerate repetitive coding tasks while ensuring understanding of every change.

## 📈 Expected Results

- A reliable Python backtest engine with multiple strategies
- C++ modules for order execution and performance-critical logic
- Seamless CSV/JSON bridge between Python ↔ C++
- Performance metrics, documentation, and presentation-ready artifacts
- GitHub history demonstrating consistent progress

## 👤 Author

Built by **Fred Vu** as part of the “learn quant trading with FVU” journey.

---

**Last Updated:** Week 0 – 2025-11-06
