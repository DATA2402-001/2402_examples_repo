from bs4 import BeautifulSoup
import requests
import pandas as pd


response = requests.get('http://ufcstats.com/statistics/events/completed?page=1')
html = response.content.decode()

soup = BeautifulSoup(html)
table = soup.find('table')

df = pd.read_html(html, extract_links='all')
print(df)