import requests
from bs4 import BeautifulSoup
import sqlite3
import os


# Step 1: Create directory if it doesn't exist
db_dir = "scrapped_data"
os.makedirs(db_dir, exist_ok=True)

# Step 2: Define full path to the database file
db_path = os.path.join(db_dir, "books.db")

# Step 3: Fetch the HTML
url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Step 4. Extract book titles and prices
books = []
for book in soup.select("article.product_pod"):
    title = book.h3.a["title"]
    price = book.select_one("p.price_color").text.strip()
    price = float(price[1:])  # Remove the '£' symbol and convert to float
    books.append((title, price))

# Step 5. Print the scraped data
print("Books scraped: ")
for title, price in books:
    print(f"{title} - £{price:.2f}")

# Step 6: Save to SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        price REAL
    )
''')

# Insert book data
cursor.executemany("INSERT INTO books (title, price) VALUES (?, ?)", books)
conn.commit()
conn.close()
