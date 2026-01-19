import requests
import pandas as pd
import os

API_KEY = os.getenv("EXCHANGE_API_KEY")
API_URL = f"https://api.exchangerate.host/live?access_key={API_KEY}&symbols=JPY"


def fetch_usdjpy():
    r = requests.get(API_URL)
    data = r.json()
    rate = data["quotes"]["USDJPY"]
    date = data["timestamp"]

    df = pd.DataFrame([{"date": date, "usdjpy": rate}])

    os.makedirs("data", exist_ok=True)
    path = "data/usdjpy.csv"

    if os.path.exists(path):
        old = pd.read_csv(path)
        df = pd.concat([old, df]).drop_duplicates(subset=["date"])

    df.to_csv(path, index=False)


if __name__ == "__main__":
    fetch_usdjpy()
