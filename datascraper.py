import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Create empty dataframe
df = pd.DataFrame()

# Pull html from web
year = 2022
url = 'https://www.baseball-reference.com/awards/hof_'+str(year)+'.shtml'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

# Use only the body of the first table
table = soup.body.table.tbody

# Scrap stats from table
# Each row is one player for one year of voting
for player in table.find_all('tr'):
    valuelist = [year]
    fieldlist = ['year']
    for stat in player.find_all('td'):
        value = stat.get_text()
        field = stat.get('data-stat')
        # print(value)
        # print(field)
        valuelist.append(value)
        fieldlist.append(field)
        # print(valuelist)

    print(valuelist)
    print(fieldlist)
    print(len(valuelist))
    print(len(fieldlist))
    df_row = pd.DataFrame(columns = [fieldlist])
    df_row.loc[len(df_row)] = valuelist
    print(df_row)
