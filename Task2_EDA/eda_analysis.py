import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("retail_sales_dataset.csv")

print("\n===== DATASET OVERVIEW =====")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("\nData types:")
print(df.dtypes)

# Missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# Duplicate records
print("\n===== DUPLICATES =====")
print("Duplicate rows:", df.duplicated().sum())

# Convert date
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Basic statistics
print("\n===== DESCRIPTIVE STATISTICS =====")
print(df[["Quantity", "Unit_Price", "Sales", "Profit"]].describe())

# KPIs
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
average_sales = df["Sales"].mean()
average_profit = df["Profit"].mean()

print("\n===== KEY PERFORMANCE INDICATORS =====")
print(f"Total Sales: ₹{total_sales:,.2f}")
print(f"Total Profit: ₹{total_profit:,.2f}")
print(f"Total Quantity Sold: {total_quantity:,}")
print(f"Average Sales per Order: ₹{average_sales:,.2f}")
print(f"Average Profit per Order: ₹{average_profit:,.2f}")

# Category analysis
print("\n===== CATEGORY ANALYSIS =====")
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
print(category_sales)

# Region analysis
print("\n===== REGION ANALYSIS =====")
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print(region_sales)

# Product analysis
print("\n===== PRODUCT ANALYSIS =====")
product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
print(product_sales.head())

# Monthly trend
df["Month"] = df["Order_Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum()

print("\n===== MONTHLY SALES TREND =====")
print(monthly_sales)

# Outlier detection using IQR
Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df["Sales"] < lower_limit) |
    (df["Sales"] > upper_limit)
]

print("\n===== OUTLIER DETECTION =====")
print("Lower limit:", round(lower_limit, 2))
print("Upper limit:", round(upper_limit, 2))
print("Number of sales outliers:", len(outliers))

# Top customers
print("\n===== TOP CUSTOMERS =====")
customer_sales = df.groupby("Customer_Name")["Sales"].sum().sort_values(ascending=False)
print(customer_sales.head(10))

# Save cleaned dataset
df.to_csv("retail_sales_eda_cleaned.csv", index=False)

print("\n===== EDA COMPLETED =====")
print("Cleaned dataset saved as: retail_sales_eda_cleaned.csv")