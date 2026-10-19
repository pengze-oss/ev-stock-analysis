import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# BYD stock ticker
ticker = "BYDDY"

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
# Display descriptive statistics
print("\nBYD Stock Analysis")
print("Number of records:", len(data))

print("\nClosing Price Statistics:")
print(data["Close"].describe())

print("\nDaily Return Statistics (%):")
print(data["Daily Return"].describe())

# Find highest and lowest closing prices
highest_date = data["Close"].idxmax()
lowest_date = data["Close"].idxmin()

print("\nHighest Closing Price:")
print("Date:", highest_date.date())
print("Price: $", round(data.loc[highest_date, "Close"], 2))

print("\nLowest Closing Price:")
print("Date:", lowest_date.date())
print("Price: $", round(data.loc[lowest_date, "Close"], 2))

# Find highest and lowest daily returns
highest_return_date = data["Daily Return"].idxmax()
lowest_return_date = data["Daily Return"].idxmin()

print("\nHighest Daily Return:")
print("Date:", highest_return_date.date())
print("Return:", round(data.loc[highest_return_date, "Daily Return"], 2), "%")

print("\nLowest Daily Return:")
print("Date:", lowest_return_date.date())
print("Return:", round(data.loc[lowest_return_date, "Daily Return"], 2), "%")
# Save BYD data for later analysis
data.to_csv("byd_stock_data.csv")

print("\nBYD data saved to byd_stock_data.csv")
# Save BYD data for later analysis
data.to_csv("byd_stock_data.csv")

print("\nBYD data saved to byd_stock_data.csv")
# Plot BYD closing price
plt.figure(figsize=(12, 6))

plt.plot(
    data.index,
    data["Close"],
    label="BYD (BYDDY)"
)

plt.title("BYD Daily Closing Price in 2025")
plt.xlabel("Date")
plt.ylabel("Closing Price (USD)")
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()

# Save the chart
plt.savefig("byd_closing_price.png", dpi=300)

# Display the chart
plt.show()

print("BYD closing price chart saved to byd_closing_price.png")
# Plot BYD daily returns
plt.figure(figsize=(12, 6))

plt.plot(
    data.index,
    data["Daily Return"],
    label="BYD Daily Return",
    linewidth=0.8
)

plt.axhline(y=0, linestyle="--", linewidth=1)

plt.title("BYD Daily Stock Returns in 2025")
plt.xlabel("Date")
plt.ylabel("Daily Return (%)")
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()

# Save the chart
plt.savefig("byd_daily_returns.png", dpi=300)

# Display the chart
plt.show()

print("BYD daily returns chart saved to byd_daily_returns.png")
# Plot BYD daily return distribution
plt.figure(figsize=(10, 6))

plt.hist(
    data["Daily Return"].dropna(),
    bins=30,
    edgecolor="black"
)

plt.title("Distribution of BYD Daily Returns in 2025")
plt.xlabel("Daily Return (%)")
plt.ylabel("Number of Trading Days")
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig("byd_return_distribution.png", dpi=300)
plt.show()

print("BYD return distribution chart saved to byd_return_distribution.png")
# Monthly BYD performance
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

print("\nBYD Monthly Performance:")
print(monthly_data.round(2))

monthly_data.to_csv("byd_monthly_summary.csv")
print("BYD monthly summary saved to byd_monthly_summary.csv")
# Inspect BYD's largest daily decline
