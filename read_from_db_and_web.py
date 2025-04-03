import pandas as pd
import sqlite3


con = sqlite3.connect('example.db')
table = pd.read_sql(
    "select * from users left join orders on orders.user_id = users.id", 
    con)

print(table)


import requests
r = requests.get('http://ufcstats.com/statistics/events/completed')
table = pd.read_html(r.text)
print(table)

import bs4
soup = bs4.BeautifulSoup(r.text)
links = soup.find_all('a', href=True)
print(links)