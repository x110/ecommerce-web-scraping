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
    "url": "https://ae.kickscrew.com/en/products/nike-womens-wmns-dunk-high-aluminum-dd1869-107",
    "handle": "nike-womens-wmns-dunk-high-aluminum-dd1869-107",
    "title": "(WMNS) Nike Dunk High 'Aluminum'  DD1869-107",
    "body": "Dressed in a White and Aluminum color scheme. This Nike Dunk High features a White leather base, nylon tongues, and midsole paired with Aluminum Blue \u2013 not University Blue \u2013 leather and Swoosh overlays. The same light hue continues on the laces, liner, tongue labels, insole, and rubber outsole completes the design.\nSKU: DD1869-107\nRelease Date: 30 Sep 2021\nColor: White/Aluminum",
    "type": "Skate Shoes",
    "product_info": {
      "Model No": "DD1869-107",
      "Release Date": "2021-08-06",
      "Series": "Dunk",
      "Nickname": "Aluminum",
      "Style": "Sports, Street Style, Trendy",
      "Season": "All Season",
      "Upper material": "Polyurethane/PU Leather",
      "Closure": "Lacing",
      "Sole material": "Rubber Sole",
      "Toe type": "Round Toe",
      "Heel type": "Flat heel",
      "Color way": "White/Aluminum"
    },
    "gender": "WOMENS"
  },
  {
    "url": "https://ae.kickscrew.com/en/products/nike-sportswear-tech-fleece-cu4490-010",
    "handle": "nike-sportswear-tech-fleece-cu4490-010",
    "title": "Nike Sportswear NSW Tech Fleece Zipper Cardigan autumn 'Black'  CU4490-010",
    "body": "",
    "type": "Hoodies",
    "product_info": {
      "Model No": "CU4490-010",
      "Release Date": "2022-01-26",
      "Series": "Sportswear",
      "Nickname": "Black",
      "Season": "Autumn/Spring",
      "Version": "Regular fit",
      "Closure": "Lacing",
      "Color way": "Black"
    },
    "gender": "MENS"
  },
  {
    "url": "https://ae.kickscrew.com/en/products/nike-dunk-low-retro-championship-court-purple-dd1391-104",
    "handle": "nike-dunk-low-retro-championship-court-purple-dd1391-104",
    "title": "Nike Dunk Low 'Championship Purple'  DD1391-104",
    "body": "The Nike Dunk Low Championship Court Purple is the perfect shoe for those looking to add a unique style to their wardrobe. Crafted with premium materials, the shoe features a classic white leather upper with Championship Purple overlays and Swooshes. The iconic Nike embroidery at the heel pays homage to the original 1985 design, keeping this throwback look true to its roots. At the base, a white and purple sole adds an eye-catching finish that pairs perfectly with your everyday looks. Whether you\u2019re hitting the streets or showing off at a special occasion, these kicks are sure to turn heads and make any outfit stand out from the rest. Get your hands on a pair today!",
    "type": "Skate Shoes",
    "product_info": {
      "Model No": "DD1391-104",
      "Release Date": "2022-05-04",
      "Series": "Dunk",
      "Nickname": "Championship Purple",
      "Style": "Street Style, Trendy",
      "Season": "All Season",
      "Closure": "Lacing",
      "Sole material": "Rubber Sole",
      "Toe type": "Round Toe",
      "Heel type": "Flat heel",
      "Color way": "White/Court Purple/Total Orange"
    },
    "gender": "Mens"
  },
  ...

```


## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
## Acknowledgments
Thanks to the developers of BeautifulSoup and Selenium for providing powerful tools for web scraping in Python.

Happy Scraping! 🚀