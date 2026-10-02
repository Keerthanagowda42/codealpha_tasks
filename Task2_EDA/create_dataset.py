import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

customers = [
    "Ananya", "Rahul", "Priya", "Arjun", "Sneha",
    "Kiran", "Divya", "Vikram", "Meera", "Rohit",
    "Aisha", "Nikhil", "Pooja", "Sanjay", "Neha"
]

products = [
    "Laptop", "Smartphone", "Headphones", "Monitor",
    "Keyboard", "Mouse", "Office Chair", "Desk",
    "Printer", "Notebook", "Pen Set", "Backpack"
]

categories = {
    "Laptop": "Electronics",
    "Smartphone": "Electronics",
    "Headphones": "Electronics",
    "Monitor": "Electronics",
    "Keyboard": "Electronics",
    "Mouse": "Electronics",
    "Office Chair": "Furniture",
    "Desk": "Furniture",
    "Printer": "Electronics",
    "Notebook": "Stationery",
    "Pen Set": "Stationery",
    "Backpack": "Accessories"
}

cities = {
    "Bengaluru": "South",
    "Chennai": "South",
    "Hyderabad": "South",
    "Mumbai": "West",
    "Pune": "West",
    "Delhi": "North",
    "Kolkata": "East",
    "Ahmedabad": "West"
}

prices = {
    "Laptop": 55000,
    "Smartphone": 30000,
    "Headphones": 2500,
    "Monitor": 15000,
    "Keyboard": 1500,
    "Mouse": 800,
    "Office Chair": 8500,
    "Desk": 7000,
    "Printer": 12000,
    "Notebook": 120,
    "Pen Set": 200,
    "Backpack": 1800
}

payments = ["UPI", "Card", "Cash", "Net Banking"]

data = []

start_date = datetime(2024, 1, 1)

for i in range(5000):

    product = random.choice(products)
    city = random.choice(list(cities.keys()))
    quantity = random.randint(1, 10)

    unit_price = prices[product]

    # Small price variation
    unit_price = round(unit_price * random.uniform(0.90, 1.10), 2)

    sales = round(quantity * unit_price, 2)

    profit = round(sales * random.uniform(0.08, 0.25), 2)

    order_date = start_date + timedelta(days=random.randint(0, 365))

    data.append({
        "Order_ID": f"ORD{1001 + i}",
        "Order_Date": order_date.strftime("%Y-%m-%d"),
        "Customer_Name": random.choice(customers),
        "Product": product,
        "Category": categories[product],
        "City": city,
        "Region": cities[city],
        "Quantity": quantity,
        "Unit_Price": unit_price,
        "Sales": sales,
        "Profit": profit,
        "Payment_Method": random.choice(payments)
    })

df = pd.DataFrame(data)

# Save dataset
df.to_csv("retail_sales_dataset.csv", index=False)

print("====================================")
print("EDA DATASET CREATED SUCCESSFULLY")
print("====================================")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("File: retail_sales_dataset.csv")
print("\nColumns:")
print(df.columns.tolist())
print("\nFirst 5 records:")
print(df.head())