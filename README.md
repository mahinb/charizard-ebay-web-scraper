# eBay Web Scraping Project

## Overview

This is my beginner-level web scraping project designed to extract and analyze data from eBay search results. The script focuses on scraping information related to a specific product, in this instance"base set charizard," from eBay's search results page. The data is then processed, filtered, and sorted based on price.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `lxml` parser

You can install the required libraries using pip:

```sh
pip install requests beautifulsoup4 lxml
```

## How It Works

1. **Send Request**: The script sends an HTTP GET request to eBay's search results page URL with the desired query.
2. **Parse HTML**: It parses the HTML content using BeautifulSoup with the 'lxml' parser.
3. **Extract Data**: Finds and extracts relevant product information from the HTML:
   - Title
   - Price
   - Quality (if available)
   - Shipping cost
   - URL
4. **Filter and Process**: Filters results based on specific keywords (e.g., "charizard," "base set," "1999") and processes them.
5. **Sort Results**: Sorts the results by price.
6. **Print Results**: Outputs the filtered and sorted results in a readable format.

## Example Code

```python
import requests
from bs4 import BeautifulSoup
from operator import itemgetter

url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=base+set+charizard&LH_BIN=1&_sop=12'
request = requests.get(url)
print(request) # Output will be <Response[200]> if request is successful

soup = BeautifulSoup(request.text, 'lxml')
ebay_s = soup.find_all('div', class_='s-item__info clearfix')[2:] # Start from 3rd element

ebay_data = []
for item in ebay_s:
    title = item.find('div', class_='s-item__title').text.strip()
    if "charizard" in title.lower() and 'base set' in title.lower() and '1999' in title.lower():
        price = float(item.find('div', class_='s-item__detail s-item__detail--primary').text.strip().replace(',','').strip('$'))
        quality = item.find('div', class_='s-item__subtitle')
        if quality is not None:
            quality = quality.text.strip()
        else:
            quality = 'N/A'
        shipping = item.find('span', class_='s-item__shipping s-item__logisticsCost').text.strip()
        url = item.find('a', class_='s-item__link').get('href')
        data_tuple = (title, price, quality, shipping, url)
        ebay_data.append(data_tuple)

ebay_data = sorted(ebay_data, key=itemgetter(1)) # Sort by price

for item in ebay_data:
    print("Name:", item[0])
    print("Price:","$" + '{:,.2f}'.format(item[1]))
    print("Quality:", item[2])
    print("Shipping:", item[3])
    print("URL:", item[4])
    print("-" * 50)
```

## Customization

- **Search Query**: Modify the `url` variable to search for different products. Change the `base+set+charizard` part to your desired query.
- **Pagination**: Implement pagination by appending `&_pgn=` with a page number to the URL to navigate through different pages of search results.

## Notes

- This project is intended for educational purposes to demonstrate basic web scraping techniques.
- Always ensure that your web scraping activities comply with the website's `robots.txt` and terms of service.


