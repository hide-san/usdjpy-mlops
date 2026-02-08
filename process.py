"""
Annotate the USD/JPY dataset with spike and trend indicators.

This module loads `data/usdjpy.csv`, computes two derived features:

1. Spike Detection
   Flags rows where the absolute percentage change (`pct_change`)
   exceeds 1%. A boolean column `spike` is added.

2. Trend Classification
   Compares short-term (ma5) and medium-term (ma25) moving averages.
   - "up"   : ma5 > ma25
   - "down" : otherwise
   A categorical column `trend` is added.

The updated dataset overwrites the original CSV file.
"""

import pandas as pd

df = pd.read_csv("data/usdjpy.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Mean Average
df["ma5"] = df["usdjpy"].rolling(5).mean()
df["ma25"] = df["usdjpy"].rolling(25).mean()

# Percentage Change
df["pct_change"] = df["usdjpy"].pct_change()

df.to_csv("data/usdjpy.csv", index=False)
