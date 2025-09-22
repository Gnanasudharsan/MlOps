# Lab 1 – MLOps (IE-7374)

This repository contains my submission for **Lab 1** of the MLOps course.  
The lab demonstrates environment setup, Git/GitHub usage, test automation, and CI/CD with GitHub Actions.

---

## 🔹 Project Overview
- Set up a **virtual environment** (`.venv`)  
- Initialized a **GitHub repository** and structured folders (`src/`, `test/`, `data/`, `.github/workflows/`)  
- Implemented Python code (`converter.py`) with unit tests  
- Configured **GitHub Actions** to run both `pytest` and `unittest` automatically on each push  

---

## 🔹 Modifications (vs original repo)
To ensure the submission is unique, I made functional changes:
- Renamed `calculator.py` → **`converter.py`**
- Replaced arithmetic functions with a **Unit Converter**:
  - Length (m, km, mi, ft, in)
  - Mass (kg, g, lb, oz)
  - Temperature (C, F, K)
  - Time (s, min, hr)
  - Speed (m/s, kph, mph)
  - Volume (L, mL, gal)
  - Area (sqm, sqft)
- Updated both `pytest` and `unittest` test suites to validate conversions
- CI workflows (`pytest` + `unittest`) fixed to run with proper `PYTHONPATH` setup

---

## 🔹 How to Run Locally

### 1. Create and activate virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.\.venv\Scripts\activate    # Windows

### 2. Install dependencies
pip install -r requirements.txt
### 3. Run tests
pytest -q
python -m unittest -v test/test_unittest.py
### 4. Try the converter manually
python -c 'from src.converter import convert; print(convert(60,"mph","kph"))'  # 96.56064
python -c 'from src.converter import convert; print(convert(0,"C","F"))'      # 32.0
python -c 'from src.converter import convert; print(convert(1,"mi","km"))'    # 1.609344

