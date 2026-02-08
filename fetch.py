"""
Fetch USD/JPY exchange rate data from the exchangerate.host API and
append it to the local dataset.

This module determines the appropriate date window based on the most
recent entry in `data/usdjpy.csv`, queries the API for historical
USD/JPY rates, normalizes the response into tabular form, and merges
the new data with the existing CSV while preventing duplicate dates.

Side Effects
------------
- Creates the `data/` directory if it does not exist.
- Reads and writes `data/usdjpy.csv`.
- Extends the dataset with newly fetched exchange rate records.
"""

from datetime import datetime, timedelta
import os
import requests
import pandas as pd

API_KEY = os.getenv("EXCHANGE_API_KEY")
MAX_DATE_WINDOW=365

def get_dates():
    """
    Determine the start and end dates for the API request window.

    This function reads the existing `data/usdjpy.csv` file and extracts the
    most recent date recorded. It then computes an end date by adding
    `MAX_DATE_WINDOW` days to that date.

    Returns
    -------
    tuple[str, str]
        A tuple containing:
        - start_date (str): The latest date found in the CSV (YYYY-MM-DD).
        - end_date (str): The computed end date (YYYY-MM-DD).
    """
    df = pd.read_csv("data/usdjpy.csv")
    start = df['date'].max()
    date_format = "%Y-%m-%d"
    date_obj = datetime.strptime(start, date_format)
    end = date_obj + timedelta(days=MAX_DATE_WINDOW)
    return start, end.strftime(format=date_format)


start_date, end_date = get_dates()
API_URL = (
    f"https://api.exchangerate.host/timeframe?"
    f"access_key={API_KEY}&"
    f"source=USD&"
    f"currencies=JPY&"
    f"start_date={start_date}&"
    f"end_date={end_date}"
)


def fetch_usdjpy():
    """
    Fetch USD/JPY exchange rate data and append it to the local CSV file.

    This function calls the exchangerate.host API using the global `API_URL`,
    parses the returned JSON, and converts the `quotes` field into a DataFrame.
    The resulting data is merged with any existing `data/usdjpy.csv` file,
    ensuring no duplicate dates are stored.

    Side Effects
    ------------
    - Creates the `data/` directory if it does not exist.
    - Writes or updates `data/usdjpy.csv`.

    Notes
    -----
    - Existing rows are preserved; new rows are appended.
    - Duplicate dates are removed based on the `date` column.
    """
    r = requests.get(API_URL, timeout=10)
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
