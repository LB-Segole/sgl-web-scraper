# sgl-intel-scraper
# Scrapes and monitors competitor activity, funding news, or tech breakthroughs in your five divisions. 
# Feeds into a structured JSON intelligence report. Aligned to SGL's research operation.

# Looking at the requests document, i can gather how you fetch the dat you want

import requests
from bs4 import BeautifulSoup
import json
import time

url = 'https://businesstech.co.za/news/5-things/862842/google-to-pay-elon-musk-r15-billion-every-month-and-top-south-african-retailer-closing-400-stores/' # the url that will be scraped
page = requests.get(url) # requests the information from the url, sends back either 200, 403 - check website accesibility
page.text # the entire HTM of the page as a string

# now that we've fetched the site and know it's 200 and have seen the html page, we can turn to bs4
# per documents:

soup = BeautifulSoup(page.text, 'html.parser')

title = soup.find('h1')

print(title)
