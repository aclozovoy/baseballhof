import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Flag to only create DataFrame once
flag = False

# Loop over years
# no voting in 1961, 1963, 1965
start_year = 1966
end_year = 2022
for year in range(start_year,end_year+1):

    # Pull html from web
    # year = 2022
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
            valuelist.append(value)
            fieldlist.append(field)

        # Flag to only create dataframe once
        if flag == False:
            df = pd.DataFrame(columns = [fieldlist])
            flag = True
        
        # Add player row to dataframe
        df.loc[len(df)] = valuelist

print(df)
