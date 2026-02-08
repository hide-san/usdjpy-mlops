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
