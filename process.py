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
