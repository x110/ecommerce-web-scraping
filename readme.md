# Ecommerce Web Scraping Project

## Overview

This project is a web scraping tool designed to extract product information from an ecommerce website. It is built to scrape data from [kickscrew.com](https://ae.kickscrew.com/collections/nike) and provides a structured output in CSV format. The tool is developed in Python using the BeautifulSoup and Requests libraries for web scraping.

## Features

- **Scraping**: Extracts product details such as name, price, description, and image URL from the specified ecommerce site.
- **Configurable**: Easily configurable to adapt to changes in the website structure or to scrape different sections of the site.
- **CSV Output**: Stores the scraped data in a CSV file for easy integration with other tools or analysis.

## Getting Started

### Prerequisites

- Python 3.x
- Install required Python packages:

```bash
pip install -r requirements.txt
```

### Usage
Clone the repository:
```bash
git clone https://github.com/yourusername/ecommerce-web-scraping.git
```

### Navigate to the project directory:
```bash
cd ecommerce-web-scraping
```
Run the scraper:
```bash
python scraper.py
```
### Check the output:
The scraped data will be saved in a file named output.csv in the project directory.
### Configuration
You can configure the scraper by modifying the config.py file. Update the URLs, selectors, and any other parameters according to the structure of the target ecommerce site.
```
python
# config.py
# URL of the ecommerce site
BASE_URL = "https://ae.kickscrew.com/collections/nike"

# Selectors for scraping
SELECTORS = {
    "product_name": ".product-title",
    "product_price": ".product-price",
    "product_description": ".product-description",
    "product_image": ".product-image",
}
```
## Contributing

If you would like to contribute to this project or report issues, please follow the guidelines in the CONTRIBUTING.md file.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
## Acknowledgments
Thanks to the developers of BeautifulSoup and Requests for providing powerful tools for web scraping in Python.

Happy Scraping! 🚀