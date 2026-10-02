import requests
from bs4 import BeautifulSoup
import pandas as pd

# ==========================================
# 1. WEBSITE SETUP
# ==========================================

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

data = []


# ==========================================
# 2. SCRAPE MULTIPLE PAGES WITH ERROR HANDLING
# ==========================================

for page in range(1, 6):==

    url = base_url.format(page)

    print(f"\nScraping page {page}...")

    # Error handling
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

    except requests.RequestException as e:
        print("Error while accessing page:", page)
        print("Error:", e)
        continue

    print("Status Code:", response.status_code)

    # Read webpage HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all books
    books = soup.find_all("article", class_="product_pod")

    print("Books found:", len(books))


    # ==========================================
    # 3. EXTRACT BOOK DETAILS
    # ==========================================

    for book in books:

        title = book.h3.a["title"]

        price = book.find(
            "p",
            class_="price_color"
        ).text

        availability = book.find(
            "p",
            class_="instock"
        ).text.strip()

        rating = book.find(
            "p",
            class_="star-rating"
        )["class"][1]

        data.append({
            "Title": title,
            "Price": price,
            "Availability": availability,
            "Rating": rating
        })


# ==========================================
# 4. CREATE DATAFRAME
# ==========================================

df = pd.DataFrame(data)

print("\nDataset created successfully!")
print("Dataset Shape:", df.shape)


# ==========================================
# 5. CLEAN PRICE
# ==========================================

df["Price"] = (
    df["Price"]
    .str.replace("Â£", "", regex=False)
    .str.replace("£", "", regex=False)
    .str.strip()
)

df["Price"] = pd.to_numeric(df["Price"])


# ==========================================
# 6. CONVERT RATING TO NUMBERS
# ==========================================

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating"] = df["Rating"].map(rating_map)


# ==========================================
# 7. DATA VALIDATION
# ==========================================

print("\n========== DATA VALIDATION ==========")

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nData Types:")
print(df.dtypes)

print("\nDataset Shape:")
print(df.shape)


# ==========================================
# 8. BASIC ANALYSIS
# ==========================================

print("\n========== BASIC ANALYSIS ==========")

print("Average Price:", round(df["Price"].mean(), 2))

print("Minimum Price:", df["Price"].min())

print("Maximum Price:", df["Price"].max())

print("Average Rating:", round(df["Rating"].mean(), 2))


# ==========================================
# 9. RATING DISTRIBUTION
# ==========================================

print("\nRating Distribution:")

print(
    df["Rating"]
    .value_counts()
    .sort_index()
)


# ==========================================
# 10. MOST EXPENSIVE BOOKS
# ==========================================

print("\n========== MOST EXPENSIVE BOOKS ==========")

print(
    df.nlargest(
        5,
        "Price"
    )[["Title", "Price", "Rating"]]
)


# ==========================================
# 11. CHEAPEST BOOKS
# ==========================================

print("\n========== CHEAPEST BOOKS ==========")

print(
    df.nsmallest(
        5,
        "Price"
    )[["Title", "Price", "Rating"]]
)


# ==========================================
# 12. HIGHEST RATED BOOKS
# ==========================================

print("\n========== HIGHEST RATED BOOKS ==========")

print(
    df[df["Rating"] == 5]
    [["Title", "Price", "Rating"]]
)


# ==========================================
# 13. DISPLAY FIRST 10 RECORDS
# ==========================================

print("\n========== FIRST 10 RECORDS ==========")

print(
    df.head(10).to_string(index=False)
)


# ==========================================
# 14. SAVE DATASET
# ==========================================

df.to_csv(
    "books_dataset.csv",
    index=False
)

print("\n========================================")
print("Dataset saved successfully!")
print("File: books_dataset.csv")
print("Total records:", len(df))
print("========================================")