# Ecommerce Web Scraping
## Overview

This project is a web scraping tool designed to extract product information from an ecommerce website. It is built to scrape data from [kickscrew.com](https://ae.kickscrew.com/collections/nike) and provides a structured output in JSON format. The tool is developed in Python using the BeautifulSoup, and Selenium libraries for web scraping.

## Features

- **Scraping**: Extracts product details such as name, price, and description from the specified ecommerce site.

- **JSON Output**: Stores the scraped data in a JSON file for easy integration with other tools or analysis.

## Getting Started

### Clone the repository:
```bash
git clone git@github.com:x110/ecommerce-web-scraping.git
```

### Navigate to the project directory:
```bash
cd ecommerce-web-scraping
```
### Install required Python packages
```bash
pip install -r requirements.txt
```
### Run the scraper:
```bash
python main.py
```
### Check the output:
The scraped data will be saved in a file named scraped_data.json in the project directory.

``` json
{
    "url": "https://ae.kickscrew.com/en/products/nike-dunk-low-sb-skateboard-court-purple-bq6817-500",
    "handle": "nike-dunk-low-sb-skateboard-court-purple-bq6817-500",
    "title": "Nike SB Dunk Low 'Court Purple'  BQ6817-500",
    "body": "Dressed in a Court Purple, White, and Black color scheme. This Nike SB Dunk Low comes with the Air Jordan 1\u2019s popular \u201cBlack Toe\u201d color blocking featuring a White leather base with Black overlays and Court Purple in the rear and rubber outsole.SKU: BQ6817-500Release Date: 9 Nov 2020Color: Court Purple/White/Court Purple/Black",
    "type": "Sneakers",
    "product_info": {
      "Model No": "BQ6817-500",
      "Release Date": "2024-01-27",
      "Series": "Dunk",
      "Nickname": "Court Purple",
      "Style": "Street Style",
      "Season": "All Season",
      "Upper material": "Synthetic Leather",
      "Closure": "Lacing",
      "Sole material": "Rubber Sole",
      "Toe type": "Round Toe",
      "Heel type": "Flat heel",
      "Color way": "Black/Purple/White"
    },
    "gender": "MENS"
  },
  ...

```


## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
## Acknowledgments
Thanks to the developers of BeautifulSoup and Selenium for providing powerful tools for web scraping in Python.

Happy Scraping! 🚀