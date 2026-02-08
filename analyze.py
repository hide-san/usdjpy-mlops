"""
Analyze the USD/JPY dataset by generating spike and trend indicators.

This module loads `data/usdjpy.csv`, computes:
- `spike`: a boolean flag for days where the absolute percentage change
  exceeds 1%.
- `trend`: a simple trend classification comparing short-term (ma5)
  and medium-term (ma25) moving averages.

The updated dataset overwrites the original CSV file.
"""

import pandas as pd

df = pd.read_csv("data/usdjpy.csv")

# Spike flag indicating over 1% change on rate
df["spike"] = df["pct_change"].abs() > 0.01

# Trend Analysis
df["trend"] = df.apply(
    lambda row: "up" if row["ma5"] > row["ma25"] else "down",
    axis=1
)

df.to_csv("data/usdjpy.csv", index=False)
