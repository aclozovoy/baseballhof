import numpy as np
import pandas as pd

# IMPORT DATA
df = pd.read_csv('HOF_voting.csv',sep='|')

# Drop second index
df = df.drop(columns = 'Unnamed: 0')

# Duplicate player names with tags
df['player_old'] = df['player']

# Remove tags
for index, row in df.iterrows():
    #remove 'X-' from player names
    name = row['player']
    if name[0:2] == 'X-':
        clean_name = name[2:]
        df.loc[index,['player']] = clean_name

for index, row in df.iterrows(): 
    # Remove 'HOF' from player names
    name = row['player']
    if name[-3:] == 'HOF':
        clean_name = name[0:-4]
        df.loc[index,['player']] = clean_name

# OUTPUT TO CSV
df.to_csv('HOF_voting_clean.csv',sep='|')