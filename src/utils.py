import csv
from bs4 import BeautifulSoup
import re

def load_urls(urls_file_path):
    products_urls = []

    with open(urls_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
    
    # Skip the header row if it exists
        next(csv_reader, None)

    # Read each row and append the product URL to the list
        for row in csv_reader:
            products_urls.append(row[0])  # Assuming the URL is in the first (0-indexed) column

    products_urls = [url.replace(".com",'.com/en') for url in products_urls]
    return products_urls