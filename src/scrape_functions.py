from typing import Optional, Dict, Union
import re
from selenium.webdriver.remote.webdriver import WebDriver
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from typing import List


def get_last_page_number(driver: webdriver.Chrome) -> int:
    """
    Get the last page number from the pagination link.

    Args:
        driver (webdriver.Chrome): The Chrome WebDriver instance.

    Returns:
        int: The last page number.
    """
    last_page_element = driver.find_element(By.CLASS_NAME, "ais-Pagination-item--lastPage")
    last_page_url = last_page_element.find_element(By.TAG_NAME, "a").get_attribute("href")
    return int(last_page_url.split("page=")[-1])


def get_product_urls(driver: webdriver.Chrome, wait, page_urls: List[str]) -> List[str]:
    """
    Get product URLs from multiple pages.

    Args:
        driver (webdriver.Chrome): The Chrome WebDriver instance.
        page_urls (List[str]): List of URLs for different pages.

    Returns:
        List[str]: List of product URLs.
    """
    product_urls = []

    for url in page_urls:
        driver.get(url)
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "ais-Hits-item")))
        search_results = driver.find_elements(By.CLASS_NAME, "ais-Hits-item")
        product_urls.extend([result.find_element(By.TAG_NAME, "a").get_attribute("href") for result in search_results])
    product_urls = [url.replace(".com",'.com/en') for url in product_urls]
    return product_urls


def find_title(soup: BeautifulSoup) -> str:
    """
    Finds and returns the text content of a specific HTML element within a BeautifulSoup object.

    Parameters:
    - soup (BeautifulSoup): The BeautifulSoup object containing the HTML document.

    Returns:
    - str: The text content of the found element.

    Raises:
    - ValueError: If the specified element is not found.
    """
    element = soup.find('h1', class_='product-area__details__title')
    if element:
        return element.get_text(strip=True)
    else:
        raise ValueError("Title not found.")


def find_body(soup: BeautifulSoup) -> str:
    """
    Finds and returns the text content of a specific HTML element within a BeautifulSoup object.

    Parameters:
    - soup (BeautifulSoup): The BeautifulSoup object containing the HTML document.

    Returns:
    - str: The text content of the found element.

    Raises:
    - ValueError: If the specified element is not found.
    """
    element = soup.find('div', class_="cc-tabs__tab__panel", id=re.compile("product-tab-panel3_"))
    if element.div:
        if "wrapper" in  element.div.get('class', []):
            return ""
    if element:
        return element.get_text(strip=True)
    else:
        raise ValueError("Body not found.")

def find_type(soup: BeautifulSoup) -> str:
    """
    Finds and returns the text content of a specific HTML element within a BeautifulSoup object.

    Parameters:
    - soup (BeautifulSoup): The BeautifulSoup object containing the HTML document.

    Returns:
    - str: The text content of the found element.

    Raises:
    - ValueError: If the specified element is not found.
    """
    element = soup.find('div', class_="vendor product-detail__gap-sm")
    if element:
        return element.get_text(strip=True)
    else:
        raise ValueError("Type not found.")


def find_product_info(soup: BeautifulSoup) -> Optional[Dict[str, Union[str, None]]]:
    """
    Extracts product information from a BeautifulSoup object representing an HTML document.

    Parameters:
    - soup (BeautifulSoup): The BeautifulSoup object containing the HTML document.

    Returns:
    - dict or None: A dictionary containing product information, or None if not found.
    """
    product_info_raw = soup.find('div', class_="pdp-product-info-container")
    if product_info_raw:
        product_info_raw = product_info_raw.get_text().strip().split('\n\n')
        product_info: Dict[str, Union[str, None]] = {key: value for key, value in (item.split('\n', 1) for item in product_info_raw)}
        return product_info
    else:
        raise ValueError('Product info not found.')


def find_gender(soup: BeautifulSoup) -> Optional[str]:
    """
    Find and return the gender information from the given BeautifulSoup object.

    Args:
        soup (BeautifulSoup): The BeautifulSoup object representing the HTML content.

    Returns:
        str or None: The extracted gender information if found, or None if not found.

    Raises:
        ValueError: If the gender information is not found.
    """
    try:
        header_div = soup.find('div', class_='pdpTabHeader')

        if header_div:
            gender_div = header_div.find('div', class_='pdpOptionValues')

            if gender_div:
                return gender_div.get_text(strip=True)

        # Raise an exception if gender is not found
        raise ValueError("Gender not found.")

    except ValueError as e:
        print(f"Error: {e}")
        return None


def scrape_product_data(url: str, driver: WebDriver) -> dict:
    """
    Scrape product data from the given URL using Selenium and BeautifulSoup.

    Args:
        url (str): The URL of the product page.
        driver (WebDriver): The Selenium WebDriver instance.

    Returns:
        dict: A dictionary containing scraped product data.
    """
    try:
        driver.get(url)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        product_data = {
            'url': url,
            'handle': url.split('/products/')[-1],
            'title': find_title(soup),
            'body': find_body(soup),
            'type': find_type(soup),
            'product_info': find_product_info(soup),
            'gender': find_gender(soup)
        }

        return product_data

    except Exception as e:
        print(f"Error scraping product data: {e}")
        return {'url': url}


def scrape_data(driver, urls):
    data = []
    for url in urls:
        try:
            product_data = scrape_product_data(url, driver)
            data.append(product_data)
        except Exception as e:
            print(f"Error scraping data from {url}: {e}")

    return data
