import json
from selenium.webdriver.support.ui import WebDriverWait

from driver_config import configure_driver
from scrape_functions import scrape_product_data
from utils import load_urls

def load_config():
    with open('config.json') as config_file:
        config = json.load(config_file)
    return config

def main():
    config = load_config()
    file_path = config["file_path"]
    urls_file_path = config["urls_file_path"]
    webdriver_timeout = config["webdriver_timeout"]

    products_urls = load_urls(urls_file_path)
    data = []

    try:
        driver = configure_driver()
        WebDriverWait(driver, webdriver_timeout) 

        for url in products_urls:
            product_data = scrape_product_data(url, driver)
            data.append(product_data)

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
        print(f'Data has been written to {file_path}')

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
