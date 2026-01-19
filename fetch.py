import requests
import pandas as pd
import json
from datetime import datetime, timedelta
import os

API_KEY = os.getenv("EXCHANGE_API_KEY")
MAX_DATE_WINDOW=365

def get_dates():
    df = pd.read_csv("data/usdjpy.csv")
    start = df['date'].max()
    date_format = "%Y-%m-%d"
    date_obj = datetime.strptime(start, date_format)
    end = date_obj + timedelta(days=MAX_DATE_WINDOW)
    return start, end.strftime(format=date_format)


start_date, end_date = get_dates()
API_URL = f"https://api.exchangerate.host/timeframe?access_key={API_KEY}&source=USD&currencies=JPY&start_date={start_date}&end_date={end_date}"


def fetch_usdjpy():
    r = requests.get(API_URL)
    data = r.json()
    rows = [{"date": d, "usdjpy": v.get("USDJPY")} for d, v in data["quotes"].items()]
    df = pd.DataFrame(rows)

    os.makedirs("data", exist_ok=True)
    path = "data/usdjpy.csv"

    if os.path.exists(path):
        old = pd.read_csv(path)
        df = pd.concat([old, df]).drop_duplicates(subset=["date"])

    df.to_csv(path, index=False)


if __name__ == "__main__":
    fetch_usdjpy()
