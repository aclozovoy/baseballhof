import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Pull html from web
url = 'https://www.baseball-reference.com/awards/hof_2022.shtml'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

# Create empty dataframe
df = pd.DataFrame()

# Use only the body of the first table
table = soup.body.table.tbody

# Scrap stats from table
for player in table.find_all('tr'):
    for stat in player.find_all('td'):
        print(stat.get_text())
        print(stat.get('data-stat'))

