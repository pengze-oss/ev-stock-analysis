import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
# Stock information
ticker = "TSLA"
company_name = "Tesla"

# Date range
start_date = "2025-01-01"
end_date = "2026-01-01"
# Download historical stock data
data = yf.download(
    ticker,
    start=start_date,
    end=end_date,
    auto_adjust=False
)

print("Downloaded columns:", data.columns.tolist())
# Convert multi-level columns into simple column names
data.columns = data.columns.get_level_values(0)

# Calculate daily returns
data["Daily Return"] = data["Adj Close"].pct_change() * 100

print("\nTesla Stock Analysis")
print("Number of records:", len(data))
print("\nColumn names:")
print(data.columns.tolist())
print("\nFirst 5 rows:")
print(data.head())
# Closing price statistics
print("\nClosing Price Statistics:")
print(data["Close"].describe())

# Daily return statistics
print("\nDaily Return Statistics (%):")
print(data["Daily Return"].describe())

# Highest closing price
highest_close_date = data["Close"].idxmax()
highest_close_price = data["Close"].max()

print("\nHighest Closing Price:")
print("Date:", highest_close_date.strftime("%Y-%m-%d"))
print("Price: $", round(highest_close_price, 2))

# Lowest closing price
lowest_close_date = data["Close"].idxmin()
lowest_close_price = data["Close"].min()

print("\nLowest Closing Price:")
print("Date:", lowest_close_date.strftime("%Y-%m-%d"))
print("Price: $", round(lowest_close_price, 2))

# Highest daily return
highest_return_date = data["Daily Return"].idxmax()
highest_return = data["Daily Return"].max()

print("\nHighest Daily Return:")
print("Date:", highest_return_date.strftime("%Y-%m-%d"))
print("Return:", round(highest_return, 2), "%")

# Lowest daily return
lowest_return_date = data["Daily Return"].idxmin()
lowest_return = data["Daily Return"].min()

print("\nLowest Daily Return:")
print("Date:", lowest_return_date.strftime("%Y-%m-%d"))
print("Return:", round(lowest_return, 2), "%")
# Plot Tesla closing prices
plt.figure(figsize=(12, 6))

plt.plot(
    data.index,
    data["Close"],
    label="Tesla (TSLA)"
)

plt.title("Tesla Daily Closing Price in 2025")
plt.xlabel("Date")
plt.ylabel("Closing Price (USD)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig("tesla_closing_price.png", dpi=300)
plt.show()

print("Tesla closing price chart saved to tesla_closing_price.png")
# Plot Tesla daily returns
plt.figure(figsize=(12, 6))

plt.plot(
    data.index,
    data["Daily Return"],
    label="Tesla Daily Return",
    linewidth=0.8
)

plt.axhline(y=0, linestyle="--", linewidth=1)

plt.title("Tesla Daily Stock Returns in 2025")
plt.xlabel("Date")
plt.ylabel("Daily Return (%)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig("tesla_daily_returns.png", dpi=300)
plt.show()

print("Tesla daily returns chart saved to tesla_daily_returns.png")
# Plot Tesla daily return distribution
plt.figure(figsize=(10, 6))

plt.hist(
    data["Daily Return"].dropna(),
    bins=30,
    edgecolor="black"
)

plt.title("Distribution of Tesla Daily Returns in 2025")
plt.xlabel("Daily Return (%)")
plt.ylabel("Number of Trading Days")
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig("tesla_return_distribution.png", dpi=300)
plt.show()

print("Tesla return distribution chart saved to tesla_return_distribution.png")
# Save Tesla stock data
data.to_csv("tesla_stock_data.csv")
print("\nTesla data saved to tesla_stock_data.csv")
# Create monthly performance summary
monthly_data = data.resample("ME").agg({
    "Close": "last",
    "Daily Return": "mean",
    "Volume": "mean"
})

monthly_data.columns = [
    "Month End Closing Price",
    "Average Daily Return (%)",
    "Average Daily Volume"
]

print("\nTesla Monthly Performance:")
print(monthly_data.round(2))

# Save monthly summary
monthly_data.to_csv("tesla_monthly_summary.csv")
print("Tesla monthly summary saved to tesla_monthly_summary.csv")