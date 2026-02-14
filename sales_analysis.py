# ============================================================
# Sales Data Analysis Dashboard
# Uses Pandas for data analysis and Matplotlib for charts
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import os

# ── 1. GENERATE SAMPLE DATA ──────────────────────────────────

np.random.seed(42)  # Makes results reproducible

# Product catalogue
products = [
    "Laptop", "Wireless Mouse", "USB-C Hub", "Mechanical Keyboard",
    "Monitor", "Webcam", "Headphones", "Desk Lamp", "SSD Drive",
    "Phone Stand"
]

# Unit prices per product
prices = {
    "Laptop": 999, "Wireless Mouse": 29, "USB-C Hub": 45,
    "Mechanical Keyboard": 89, "Monitor": 349, "Webcam": 79,
    "Headphones": 149, "Desk Lamp": 35, "SSD Drive": 119, "Phone Stand": 19
}

# Generate 500 random sales records across 2024
n = 500
dates = pd.date_range(start="2024-01-01", end="2024-12-31", periods=n)
chosen_products = np.random.choice(products, size=n)
quantities = np.random.randint(1, 6, size=n)  # 1–5 units per order

# Build the raw DataFrame
df_raw = pd.DataFrame({
    "date":     dates,
    "product":  chosen_products,
    "quantity": quantities,
    "unit_price": [prices[p] for p in chosen_products],
})

# Deliberately introduce ~5 % missing values to practice cleaning
missing_idx = np.random.choice(df_raw.index, size=int(n * 0.05), replace=False)
df_raw.loc[missing_idx, "quantity"] = np.nan

# Save raw data to CSV
csv_path = os.path.join(os.path.dirname(__file__), "sales.csv")
df_raw.to_csv(csv_path, index=False)
print(f"✔  sales.csv saved → {csv_path}")


# ── 2. LOAD DATA ─────────────────────────────────────────────

df = pd.read_csv(csv_path, parse_dates=["date"])
print(f"\n📂 Loaded {len(df)} rows, {df.shape[1]} columns")
print(df.head())


# ── 3. CLEAN DATA ────────────────────────────────────────────

print(f"\n🔍 Missing values before cleaning:\n{df.isnull().sum()}")

# Fill missing quantities with the median quantity for that product
df["quantity"] = df.groupby("product")["quantity"].transform(
    lambda col: col.fillna(col.median())
)

print(f"\n✔  Missing values after cleaning:\n{df.isnull().sum()}")

# Ensure correct data types
df["quantity"] = df["quantity"].astype(int)
df["unit_price"] = df["unit_price"].astype(float)

# Add a revenue column
df["revenue"] = df["quantity"] * df["unit_price"]


# ── 4. ANALYSIS ──────────────────────────────────────────────

# --- 4a. Total revenue ---
total_revenue = df["revenue"].sum()
print(f"\n💰 Total Revenue: ${total_revenue:,.2f}")

# --- 4b. Monthly revenue ---
df["month"] = df["date"].dt.to_period("M")           # e.g. "2024-01"
monthly_revenue = (
    df.groupby("month")["revenue"]
    .sum()
    .reset_index()
)
monthly_revenue["month_label"] = monthly_revenue["month"].dt.strftime("%b")
print("\n📅 Monthly Revenue:")
print(monthly_revenue[["month_label", "revenue"]].to_string(index=False))

# --- 4c. Top 5 products by total revenue ---
top_products = (
    df.groupby("product")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)
print("\n🏆 Top 5 Products by Revenue:")
print(top_products.to_string(index=False))


# ── 5. VISUALISATIONS ────────────────────────────────────────

fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle("Sales Data Analysis Dashboard — 2024", fontsize=15, fontweight="bold")

# Colour palette
BAR_COLOUR  = "#4C72B0"
TOP_COLOUR  = "#DD8452"

# --- Chart 1: Monthly Revenue Bar Chart ---
ax1 = axes[0]
ax1.bar(
    monthly_revenue["month_label"],
    monthly_revenue["revenue"],
    color=BAR_COLOUR, edgecolor="white", linewidth=0.6
)
ax1.set_title("Monthly Revenue", fontsize=13)
ax1.set_xlabel("Month")
ax1.set_ylabel("Revenue (USD)")
ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:,.0f}"))
ax1.tick_params(axis="x", rotation=45)
ax1.grid(axis="y", linestyle="--", alpha=0.5)

# Annotate each bar with its value
for bar in ax1.patches:
    ax1.annotate(
        f"${bar.get_height():,.0f}",
        xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
        xytext=(0, 4), textcoords="offset points",
        ha="center", va="bottom", fontsize=7
    )

# --- Chart 2: Top 5 Products Bar Chart ---
ax2 = axes[1]
ax2.barh(
    top_products["product"],
    top_products["revenue"],
    color=TOP_COLOUR, edgecolor="white", linewidth=0.6
)
ax2.set_title("Top 5 Products by Revenue", fontsize=13)
ax2.set_xlabel("Revenue (USD)")
ax2.invert_yaxis()                                    # Highest bar on top
ax2.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:,.0f}"))
ax2.grid(axis="x", linestyle="--", alpha=0.5)

# Annotate each bar
for bar in ax2.patches:
    ax2.annotate(
        f"${bar.get_width():,.0f}",
        xy=(bar.get_width(), bar.get_y() + bar.get_height() / 2),
        xytext=(4, 0), textcoords="offset points",
        ha="left", va="center", fontsize=9
    )

plt.tight_layout()

# Save the chart
chart_path = os.path.join(os.path.dirname(__file__), "sales_dashboard.png")
plt.savefig(chart_path, dpi=150, bbox_inches="tight")
print(f"\n📊 Dashboard chart saved → {chart_path}")
plt.show()

print("\n✅ Analysis complete!")
