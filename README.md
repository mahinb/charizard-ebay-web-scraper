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

## Customization

- **Search Query**: Modify the `url` variable to search for different products. Change the `base+set+charizard` part to your desired query.
- **Pagination**: Implement pagination by appending `&_pgn=` with a page number to the URL to navigate through different pages of search results.

## Notes

- This project is intended for educational purposes to demonstrate basic web scraping techniques.
- Always ensure that your web scraping activities comply with the website's `robots.txt` and terms of service.


