import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from driver_config import configure_driver
from scrape_functions import scrape_product_data
from utils import load_urls

file_path = "scraped_data.json"
urls_file_path = 'products_urls.csv'

def main():
    products_urls = load_urls(urls_file_path)
    data = []

    try:
        driver = configure_driver()
        wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed

        for url in products_urls[:6]:
            product_data = scrape_product_data(url, driver)
            data.append(product_data)

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
        print(f'Data has been written to {file_path}')

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
