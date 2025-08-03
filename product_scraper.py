import requests
from bs4 import BeautifulSoup
import csv

# URL of the website to scrape
url = "http://books.toscrape.com/"

# Send a GET request
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all product containers
products = soup.find_all("article", class_="product_pod")

# Create/open a CSV file to write
with open("products.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Rating"])  # Header row

    # Loop through each product
    for product in products:
        title = product.h3.a["title"]
        price = product.find("p", class_="price_color").text
        rating = product.p["class"][1]  # The second class is the rating (e.g., "Three")

        writer.writerow([title, price, rating])

print("✅ Scraping complete. Data saved to products.csv")
