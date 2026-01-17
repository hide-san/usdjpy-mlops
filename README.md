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

# Pipeline Architecture
GitHub Actions (daily scheduled run)
        ↓
fetch.py      – Collect USD/JPY data from a public API
process.py    – Clean and preprocess the data
analyze.py    – Compute indicators and simple signals
        ↓
data/usdjpy.csv – Persist processed data
        ↓
Visualization (Note this can be implemnted exernally. e.g. Kaggle Notebook)

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
