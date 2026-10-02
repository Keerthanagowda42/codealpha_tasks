import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("retail_sales_eda_cleaned.csv")

# Convert date column
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print("\n===== DATA VISUALIZATION PROJECT =====")
print("Dataset Shape:", df.shape)

# 1. Monthly Sales Trend
monthly_sales = df.groupby(
    df["Order_Date"].dt.to_period("M")
)["Sales"].sum()

plt.figure(figsize=(10, 5))
plt.plot(monthly_sales.index.astype(str), monthly_sales.values, marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png")
plt.show()

# 2. Sales by Category
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("sales_by_category.png")
plt.show()

# 3. Sales by Region
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("sales_by_region.png")
plt.show()

# 4. Top 10 Products
product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 5))
product_sales.plot(kind="bar")
plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_10_products.png")
plt.show()

# 5. Payment Method Distribution
payment_counts = df["Payment_Method"].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(
    payment_counts.values,
    labels=payment_counts.index,
    autopct="%1.1f%%"
)
plt.title("Payment Method Distribution")
plt.tight_layout()
plt.savefig("payment_method_distribution.png")
plt.show()

# 6. Sales vs Profit
plt.figure(figsize=(8, 5))
plt.scatter(df["Sales"], df["Profit"], alpha=0.5)
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("sales_vs_profit.png")
plt.show()

# Key Insights
print("\n===== KEY INSIGHTS =====")

print(
    "1. Highest Sales Category:",
    category_sales.idxmax(),
    "with sales of ₹",
    round(category_sales.max(), 2)
)

print(
    "2. Highest Sales Region:",
    region_sales.idxmax(),
    "with sales of ₹",
    round(region_sales.max(), 2)
)

print(
    "3. Top Product:",
    product_sales.idxmax(),
    "with sales of ₹",
    round(product_sales.max(), 2)
)

print(
    "4. Most Used Payment Method:",
    payment_counts.idxmax()
)

print(
    "5. Total Sales: ₹",
    round(df["Sales"].sum(), 2)
)

print(
    "6. Total Profit: ₹",
    round(df["Profit"].sum(), 2)
)

print("\n===== VISUALIZATION COMPLETED =====")