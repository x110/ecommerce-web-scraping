from bs4 import BeautifulSoup
import re

def find_title(soup):
    element = soup.find('h1', class_='product-area__details__title')
    if element:
        return element.get_text(strip=True)
    else:
        print("Title not found.")
        return None

def find_body(soup):
    element = soup.find('div', class_="cc-tabs__tab__panel", id=re.compile("product-tab-panel3_"))
    if element:
        return element.get_text(strip=True)
    else:
        print("Body not found.")
        return None

def find_type(soup):
    element = soup.find('div', class_="vendor product-detail__gap-sm")
    if element:
        return element.get_text(strip=True)
    else:
        print("Type not found.")
        return None


def find_product_info(soup):
    product_info_raw = soup.find('div', class_="pdp-product-info-container")
    if product_info_raw:
        product_info_raw = product_info_raw.get_text().strip().split('\n\n')
        product_info = {}
        for item in product_info_raw:
            key, value = item.split('\n', 1)  # Split only at the first occurrence of newline
            product_info[key] = value
        return product_info
    else:
        print('Product info not found.')
        return None

def find_gender(soup):
    pdp_tab_header = soup.find('div', class_='pdpTabHeader')
    if pdp_tab_header:
        gender = pdp_tab_header.find('div', class_='pdpOptionValues')
        if gender:
            return gender.get_text(strip=True)
        else:
            print("Gender not found.")
            return None
    else:
        print("Gender not found.")
        return None

def scrape_product_data(url, driver):
    driver.get(url)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    product_data = {}
    product_data['handle'] = url.split('/products/')[-1]
    product_data['title'] = find_title(soup)
    product_data['body'] =  find_body(soup)
    product_data['type'] =  find_type(soup)
    product_data['product_info'] = find_product_info(soup)
    product_data['gender'] = find_gender(soup)

    return product_data
