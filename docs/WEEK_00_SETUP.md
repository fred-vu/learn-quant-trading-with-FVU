# Week 0: Setup & GitHub Repository Foundation

**Duration:** Days 1-7 (2-3 hours total)  
**Status:** 🔄 In Progress  
**Effort:** Easy (no coding yet)

---

## 🎯 Goals This Week

- [x] GitHub repo created & structured
- [x] Python environment ready (test with simple script)
- [x] C++ compiler working (test with hello world)
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

**Progress notes:** ✅ Created directories (`docs/`, `python/`, `cpp/`, `data/`, `results/`) and populated `.gitignore` with CSV/build/cache ignores. Initial commit still pending while scaffolding stabilises.

**Validation:**
- [x] Repo created on GitHub
- [x] All folders visible locally
- [x] `.gitignore` includes: `*.csv, *.o, *.so, __pycache__, .DS_Store`

**Time spent:** ~20 min

---

### Task 2: Python Environment Setup (45 min)

**What to do:**
1. Create `python/` folder
2. Create `requirements.txt`:
   ```
   pandas==1.5.3
   numpy==1.24.0
   matplotlib==3.7.0
   backtrader==1.9.78.123
   yfinance==0.2.18
   ```
3. Create virtual environment:
   ```bash
   cd python
   python3.10 -m venv venv
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
   # ... (see repo)
   ```
5. Run: `python test_setup.py` 
6. update .gitignore with the untrack files, folder. then commit
7. Commit: `git add -A && git commit -m "Python environment setup with dependencies"`

**Progress notes:** ✅ Switched to Python 3.10 for compatibility, created virtualenv, installed deps (adjusted `backtrader` pin to `1.9.78.123`), and ran `python test_setup.py` successfully.

**Result:**
- [x] Virtual environment activated
- [x] All packages installed
- [x] Test script runs successfully
- [ ] Commit pushed

**Time spent:** ~40 min

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

**Test hello world:**
```cpp
// cpp/practice/hello.cpp
#include <iostream>
int main() {
    std::cout << "[OK] g++ toolchain is ready!" << std::endl;
    return 0;
}
```

```bash
g++ -o hello cpp/practice/hello.cpp
./hello
```

**Progress notes:** ✅ Verified `g++ (Ubuntu 11.4.0-1ubuntu1~22.04.2)` under WSL, compiled `cpp/practice/hello.cpp`, and executed the binary.

**Validation:**
- [x] Compiler installed
- [x] Hello world compiles
- [x] Hello world runs
- [x] Compiler version printed

**Time spent:** ~15 min

---

### Task 4: README Documentation (30 min)

**What to do:** Draft project overview README (see template for full content) and commit.

**Progress notes:** ⏳ Not started.

**Time spent:** 0 min

---

### Task 5: Create Weekly Tracking Template (20 min)

**What to do:** Create `docs/LEARNING_LOG.md` from template.

**Progress notes:** ⏳ Not started.

**Time spent:** 0 min

---

## ✅ Weekly Checklist

- [x] GitHub repo created & functional
- [x] Python environment tested
- [x] C++ compiler tested
- [ ] README written
- [ ] Learning log started
- [x] `.gitignore` configured
- [ ] 3+ commits on GitHub

---

## 📊 Metrics

| Metric | Value |
|--------|-------|
| Total time invested | ~1.25 hours |
| Python files created | 2 (`requirements.txt`, `test_setup.py`) |
| C++ files created | 1 (`cpp/practice/hello.cpp`) |
| GitHub commits | 0 (working locally) |
| Documentation pages | 1 (Week 0 tracker) |

---

## 💡 Notes & Insights

**What went well:**  
- Environment setup smooth after switching interpreter versions.  
- Toolchain verification scripts (`python/test_setup.py`, `cpp/practice/hello.cpp`) ready for reuse.

**Challenges:**  
- Initial dependency pins failed on Python 3.12; resolved by using Python 3.10 and updating the Backtrader version.

**Next steps:**  
- Write initial `README.md` and `docs/LEARNING_LOG.md`.  
- Make the first commit capturing setup progress.  
- Begin prepping Week 1 backtest tasks.

---

## ✨ End of Week Summary (to complete on Sunday)

**Total time this week:** ____ hours  
**Commits made:** ____  
**Blocker encountered:** [ ] Yes [ ] No — Notes: _____  
**Confidence for Week 1:** 1 ☆☆☆☆☆ 5 — Rate: ____  

**Next week:**  
- Start Python backtest engine.  
- Build first trading strategy prototype.  
- Outline C++ data bridge requirements.

---
