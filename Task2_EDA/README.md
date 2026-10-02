# CodeAlpha Web Scraping Project

## Project Overview
This project uses Python to scrape book information from the Books to Scrape website.

## Objective
- Collect book details from multiple web pages
- Clean and validate the scraped data
- Perform basic analysis
- Save the final dataset as a CSV file

## Technologies Used
- Python
- Requests
- BeautifulSoup
- Pandas

## Data Collected
- Title
- Price
- Availability
- Rating

## Dataset
- Total records: 100 books
- Pages scraped: 5

## Data Cleaning
- Removed currency symbols
- Converted prices into numeric values
- Converted ratings into numbers
- Checked missing values and duplicate records

## Analysis
The project calculates:
- Average price
- Minimum price
- Maximum price
- Average rating
- Rating distribution
- Most expensive books
- Cheapest books
- Highest-rated books

## Output
The final dataset is saved as:

`books_dataset.csv`

## Project Structure

```text
CodeAlpha_Scraping/
├── scraper.py
├── books_dataset.csv
├── requirements.txt
└── README.md