# Minimal ML Ops Project: Automatically Collecting and Processing Daily USD/JPY Data
This project implements a minimal yet practical ML Ops pipeline that automatically collects, processes, and analyzes daily USD/JPY exchange rate data. It demonstrates the core components of ML Ops — data ingestion, preprocessing, analysis, automation, and reproducibility — using lightweight tools such as Python and GitHub Actions.

# Project Overview
The goal is to build a fully automated data pipeline that:
* Fetches the latest USD/JPY exchange rate from a public API
* Stores the data in a structured format
* Performs preprocessing and computes financial indicators
* Runs simple analysis such as trend detection or volatility checks
* Executes automatically every day via GitHub Actions
* Produces clean data that can be visualized later (e.g., in a Kaggle Notebook)
This project is intentionally minimal, focusing on reliability and automation rather than complex modeling.

---
# Pipeline Architecture
```
GitHub Actions (daily scheduled run)
        ↓
fetch.py      – Collect USD/JPY data from a public API
process.py    – Clean and preprocess the data
analyze.py    – Compute indicators and simple signals
        ↓
data/usdjpy.csv – Persist processed data
        ↓
Visualization (Note this can be implemnted exernally. e.g. Kaggle Notebook)
```

---
# Project Structure
```
usdjpy-mlops/
├── fetch.py          # Data ingestion
├── process.py        # Preprocessing and feature engineering
├── analyze.py        # Lightweight analysis logic
├── data/
│   └── usdjpy.csv    # Persisted dataset
├── .github/
│   └── workflows/
│       └── pipeline.yml   # GitHub Actions automation
└── README.md
```

---
# Components
## **1. Data Ingestion (`fetch.py`)**
- Retrieves the latest USD/JPY exchange rate  
- Normalizes date and rate fields  
- Appends to `data/usdjpy.csv`  
- Ensures idempotency (safe re-runs)  
- Logs success/failure  

## **2. Preprocessing (`process.py`)**
- Sorts data by date  
- Calculates:
  - 5-day moving average (MA5)  
  - 25-day moving average (MA25)  
  - Daily percentage change  
- Handles duplicates and missing values  

## **3. Analysis (`analyze.py`)**
Applies simple, interpretable financial logic:

- Spike detection (e.g., ±1% daily move)  
- Trend detection (MA5 vs MA25 crossover)  
- Volatility checks  

---
# Automation with GitHub Actions
The pipeline runs automatically every day using a scheduled workflow:
```
yaml
on:
  schedule:
    - cron: "0 9 * * *"   # Runs daily at 09:00 UTC
  workflow_dispatch:       # Allows manual execution
```

---
# External Links
- **ExchangeRate Host (API)** — https://exchangerate.host  
  Public foreign exchange rates API used for fetching USD/JPY. Check usage limits and terms before commercial use. **Last checked: 2026-01-19.**
- **Kaggle Notebook** — https://www.kaggle.com/code/hideos/minimal-ml-ops-project-daily-usd-jpy-processing  
  Interactive notebook for visualization and exploration of the collected USD/JPY data.
> **Note:** This repository does not contain any API keys. API keys (if required) are stored securely in GitHub Actions Secrets and are never committed to the repo.

