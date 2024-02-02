import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from driver_config import configure_driver
from scrape_functions import scrape_data, get_product_urls, get_last_page_number


def load_config():
    with open('config.json') as config_file:
        config = json.load(config_file)
    return config


def main():
    config = load_config()
    OUTPUT_FILE_PATH = config["OUTPUT_FILE_PATH"]
    WEBDRIVER_TIMEOUT = config["WEBDRIVER_TIMEOUT"]
    BASE_URL = config['BASE_URL']

    with configure_driver() as driver:
        
        wait = WebDriverWait(driver, WEBDRIVER_TIMEOUT)

        driver.get(BASE_URL)

        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"ais-Pagination-item--lastPage")))

        last_page = get_last_page_number(driver)

        page_urls = [BASE_URL + "?page=" + str(i) for i in range(1, last_page + 1)]

        products_urls = get_product_urls(driver, wait, page_urls)

        data = scrape_data(driver, products_urls)

        with open(OUTPUT_FILE_PATH,'w') as file:
            json.dump(data, file, indent=2)
        print(f'Data has been written to {OUTPUT_FILE_PATH}')


if __name__ == "__main__":
    main()
