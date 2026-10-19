import yfinance as yf

# Download all three stocks over the same date range
tickers = ["RIVN", "BYDDY", "TSLA"]

data = yf.download(
    tickers,
    start="2025-01-01",
    end="2026-01-01",
    auto_adjust=False,
    multi_level_index=True
)

if data.empty:
    raise ValueError("No data downloaded.")

# Select adjusted closing prices
prices = data["Adj Close"][tickers]

print("\nAdjusted closing prices:")
print(prices.head())

print("\nMissing prices:")
print(prices.isna().sum())

# Calculate daily percentage returns
returns = prices.pct_change(fill_method=None) * 100

# Keep dates with valid returns for all three stocks
common_returns = returns.dropna()

print("\nNumber of shared return observations:")
print(len(common_returns))

# Calculate the correlation matrix
correlation = common_returns.corr()

print("\nDaily Return Correlation:")
print(correlation.round(3))

import matplotlib.pyplot as plt

# Keep dates with prices for all three stocks
common_prices = prices.dropna()

# Set each stock's starting price to 100
normalized = common_prices / common_prices.iloc[0] * 100

# Compare the three stocks
normalized.plot(figsize=(10, 5))

plt.title("Normalized Stock Prices: Rivian, BYD and Tesla, 2025")
plt.xlabel("Date")
plt.ylabel("Adjusted Price Index (Starting Value = 100)")
plt.axhline(y=100, color="gray", linestyle="--")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("normalized_price_comparison.png", dpi=150)
plt.show()

print("\nEnding normalized prices:")
print(normalized.iloc[-1].round(2))

# Compare daily return distributions
common_returns.plot.box(figsize=(9, 5))

plt.title("Daily Return Distributions: Rivian, BYD and Tesla, 2025")
plt.xlabel("Stock")
plt.ylabel("Daily Return (%)")
plt.axhline(y=0, color="gray", linestyle="--")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("return_distribution_comparison.png", dpi=150)
plt.show()

# Compare daily return volatility
print("\nDaily return standard deviation (percentage points):")
print(common_returns.std().round(3))

# Show the relationship between Rivian and Tesla returns
common_returns.plot.scatter(
    x="RIVN",
    y="TSLA",
    figsize=(8, 6),
    alpha=0.6
)

plt.title("Rivian and Tesla Daily Returns, 2025")
plt.xlabel("Rivian Daily Return (%)")
plt.ylabel("Tesla Daily Return (%)")
plt.axhline(y=0, color="gray", linewidth=0.8)
plt.axvline(x=0, color="gray", linewidth=0.8)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("rivian_tesla_return_scatter.png", dpi=150)
plt.show()