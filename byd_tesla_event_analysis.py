"""Supplementary analysis for BYD (BYDDY) and Tesla (TSLA).

Reads the CSV files exported by byd_analysis.py and tesla_analysis.py.
Reports data checks, six statistics, monthly means and event-window evidence.
The business explanations and their sources are in README.md.
"""

import pandas as pd

# BYD: read the data exported by byd_analysis.py
data = pd.read_csv("byd_stock_data.csv", index_col="Date", parse_dates=True)
fields = data[["Adj Close", "Close", "High", "Low", "Open", "Volume"]]

print("BYD (BYDDY) - Data Inspection")
print("Date range:", data.index.min().date(), "to", data.index.max().date())
print("Number of records:", len(data))
print("Downloaded fields:", fields.columns.tolist())
print("\nData types:")
print(fields.dtypes)
print("\nMissing values in downloaded fields:")
print(fields.isna().sum())

# Recalculate returns without filling missing prices
data["Daily Return"] = data["Adj Close"].pct_change(fill_method=None) * 100
stats = data[["Close", "Daily Return"]].agg(
    ["count", "mean", "median", "min", "max", "std"]
)
print("\nDescriptive statistics (prices in USD, returns in %):")
print(stats.round(3))
print("\nMonthly average closing price (USD):")
print(data["Close"].resample("ME").mean().round(3))

# Inspect BYD's largest daily decline and the surrounding period
event = data.loc["2025-05-23":"2025-05-30"]
print("\nBYD event window: May 23-30, 2025")
print(event[["Close", "Daily Return", "Volume"]].round(3))
print("Highest close:", round(event["Close"].max(), 2))
print("Date:", event["Close"].idxmax().date())
print("Lowest close:", round(event["Close"].min(), 2))
print("Date:", event["Close"].idxmin().date())
print("Biggest daily drop in 2025 (%):", round(data["Daily Return"].min(), 2))
print("Date:", data["Daily Return"].idxmin().date())
print("May 27 daily return (%):", round(data.loc["2025-05-27", "Daily Return"], 2))
typical_volume = data["Volume"].median()
event_volume = data.loc["2025-05-27", "Volume"]
print("Annual median daily volume:", typical_volume)
print("Event-day volume:", event_volume)
print("Event-day volume / annual median:", round(event_volume / typical_volume, 2))
start_price = event["Adj Close"].iloc[0]
end_price = event["Adj Close"].iloc[-1]
print("Event-window price change (%):", round((end_price / start_price - 1) * 100, 2))

print("\n" + "=" * 60 + "\n")

# Tesla: read the data exported by tesla_analysis.py
data = pd.read_csv("tesla_stock_data.csv", index_col="Date", parse_dates=True)
fields = data[["Adj Close", "Close", "High", "Low", "Open", "Volume"]]

print("Tesla (TSLA) - Data Inspection")
print("Date range:", data.index.min().date(), "to", data.index.max().date())
print("Number of records:", len(data))
print("Downloaded fields:", fields.columns.tolist())
print("\nData types:")
print(fields.dtypes)
print("\nMissing values in downloaded fields:")
print(fields.isna().sum())

data["Daily Return"] = data["Adj Close"].pct_change(fill_method=None) * 100
stats = data[["Close", "Daily Return"]].agg(
    ["count", "mean", "median", "min", "max", "std"]
)
print("\nDescriptive statistics (prices in USD, returns in %):")
print(stats.round(3))
print("\nMonthly average closing price (USD):")
print(data["Close"].resample("ME").mean().round(3))

# Inspect Tesla's largest daily gain and the surrounding period
event = data.loc["2025-04-07":"2025-04-11"]
print("\nTesla event window: April 7-11, 2025")
print(event[["Close", "Daily Return", "Volume"]].round(3))
print("Highest close:", round(event["Close"].max(), 2))
print("Date:", event["Close"].idxmax().date())
print("Lowest close:", round(event["Close"].min(), 2))
print("Date:", event["Close"].idxmin().date())
print("Biggest daily gain in 2025 (%):", round(data["Daily Return"].max(), 2))
print("Date:", data["Daily Return"].idxmax().date())
print("April 9 daily return (%):", round(data.loc["2025-04-09", "Daily Return"], 2))
typical_volume = data["Volume"].median()
event_volume = data.loc["2025-04-09", "Volume"]
print("Annual median daily volume:", typical_volume)
print("Event-day volume:", event_volume)
print("Event-day volume / annual median:", round(event_volume / typical_volume, 2))
start_price = event["Adj Close"].iloc[0]
end_price = event["Adj Close"].iloc[-1]
print("Event-window price change (%):", round((end_price / start_price - 1) * 100, 2))
