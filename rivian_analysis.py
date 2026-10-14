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