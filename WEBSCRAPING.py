import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/AAPL/financials/"
headers = {"User-Agent" : "Chrome/133.0.6943.35"}
page = requests.get(url, headers=headers)
page_content=page.content
print(page_content)