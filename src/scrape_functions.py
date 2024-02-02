from typing import Optional, Dict, Union
import re
from selenium.webdriver.remote.webdriver import WebDriver
from bs4 import BeautifulSoup

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

