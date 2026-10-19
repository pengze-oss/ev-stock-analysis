import yfinance as yf

# Download Rivian's daily stock data for 2025
data = yf.download(
    "RIVN",
    start="2025-01-01",
    end="2026-01-01",
    auto_adjust=False,
    multi_level_index=False,
    keepna=True
)

# Stop if the download failed
if data.empty:
    raise ValueError("No data downloaded.")

# Display the first five rows
print(data.head())

# Inspect the whole dataset
print("\nDate range:", data.index.min(), "to", data.index.max())
print("Number of records:", len(data))
print("Column names:", data.columns.tolist())
print("\nData types:\n", data.dtypes)
print("\nMissing values:\n", data.isna().sum())

# Calculate daily percentage returns
data["Daily Return (%)"] = (
    data["Adj Close"].pct_change(fill_method=None) * 100
)

print("\nDaily returns:")
print(data[["Adj Close", "Daily Return (%)"]].head())

# Calculate descriptive statistics
stats = data[["Close", "Daily Return (%)"]].agg(
    ["count", "mean", "median", "min", "max", "std"]
)

print("\nDescriptive statistics:")
print(stats.round(3))

# Calculate monthly average closing prices
monthly = data["Close"].resample("ME").mean()

print("\nMonthly average closing price (USD):")
print(monthly.round(3))

# Find the biggest daily gain and drop
returns = data["Daily Return (%)"]

print("\nBiggest daily gain (%):", round(returns.max(), 3))
print("Date of biggest gain:", returns.idxmax().date())

print("\nBiggest daily drop (%):", round(returns.min(), 3))
print("Date of biggest drop:", returns.idxmin().date())

# Examine the period around January 3
event = data.loc["2025-01-02":"2025-01-10"]

print("\nEvent period:")
print(event[["Close", "Daily Return (%)", "Volume"]])

print("\nHighest close:", event["Close"].max())
print("Date:", event["Close"].idxmax().date())

print("\nLowest close:", event["Close"].min())
print("Date:", event["Close"].idxmin().date())

# Compare event-day volume with the annual median
typical_volume = data["Volume"].median()
event_volume = data.loc["2025-01-03", "Volume"]

print("\nMedian daily volume in 2025:", typical_volume)
print("Jan 3 volume / annual median:", round(event_volume / typical_volume, 2))

# Calculate the change over the event window
start_price = event["Adj Close"].iloc[0]
end_price = event["Adj Close"].iloc[-1]
window_change = (end_price / start_price - 1) * 100

print("Jan 2-10 price change (%):", round(window_change, 2))

import matplotlib.pyplot as plt

# Plot the closing price during the event window
plt.figure(figsize=(9, 4))
plt.plot(event.index, event["Close"], marker="o")

plt.title("Rivian Closing Price: January 2-10, 2025")
plt.xlabel("Date")
plt.ylabel("Closing Price (USD)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("rivian_event.png", dpi=150)
plt.show()

# Plot Rivian closing prices for the full year
plt.figure(figsize=(10, 5))

plt.plot(data.index, data["Close"], label="Rivian (RIVN)")

plt.title("Rivian Daily Closing Price in 2025")
plt.xlabel("Date")
plt.ylabel("Closing Price (USD)")
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("rivian_closing_price.png", dpi=150)
plt.show()

# Plot Rivian daily returns
plt.figure(figsize=(10, 5))

plt.plot(
    data.index,
    data["Daily Return (%)"],
    label="Rivian Daily Return",
    linewidth=0.8
)

plt.axhline(y=0, color="gray", linestyle="--")

plt.title("Rivian Daily Stock Returns in 2025")
plt.xlabel("Date")
plt.ylabel("Daily Return (%)")
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("rivian_daily_returns.png", dpi=150)
plt.show()

# Plot the distribution of Rivian daily returns
plt.figure(figsize=(10, 5))

plt.hist(
    data["Daily Return (%)"].dropna(),
    bins=30,
    edgecolor="black"
)

plt.title("Distribution of Rivian Daily Returns in 2025")
plt.xlabel("Daily Return (%)")
plt.ylabel("Number of Trading Days")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("rivian_return_distribution.png", dpi=150)
plt.show()