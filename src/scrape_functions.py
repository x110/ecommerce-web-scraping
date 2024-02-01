from bs4 import BeautifulSoup
import re

def find_product_info(soup):
    product_info_raw = soup.find('div', class_="pdp-product-info-container").get_text().strip().split('\n\n')
    product_info = {}
    for item in product_info_raw:
        key, value = item.split('\n', 1)  # Split only at the first occurrence of newline
        product_info[key] = value
    return product_info

def find_gender(soup):
    pdp_tab_header = soup.find('div', class_='pdpTabHeader')
    gender = pdp_tab_header.find('div', class_='pdpOptionValues').text.strip()
    return gender

def scrape_product_data(url, driver):
    driver.get(url)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    product_data = {}
    product_data['handle'] = url.split('/products/')[-1]
    product_data['title'] = soup.find('h1', class_='product-area__details__title').get_text(strip=True)
    
    element = soup.find('div', class_="cc-tabs__tab__panel", id=re.compile("product-tab-panel3_"))
    if element:
        product_data['body'] = element.get_text(strip=True)
    else:
        print("Body not found.")

    product_data['type'] = soup.find('div', class_="vendor product-detail__gap-sm").get_text(strip=True)
    product_data['product_info'] = find_product_info(soup)
    product_data['gender'] = find_gender(soup)

    return product_data
