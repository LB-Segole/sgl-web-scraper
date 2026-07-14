# sgl-intel-scraper
# Scrapes and monitors competitor activity, funding news, or tech breakthroughs in your five divisions. 
# Feeds into a structured JSON intelligence report. Aligned to SGL's research operation.

# Looking at the requests document, i can gather how you fetch the dat you want

import requests

url = 'https://businesstech.co.za/news/'
r = requests.get(url)
r.text

print(r.text)