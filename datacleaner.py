import numpy as np
import pandas as pd

# IMPORT DATA
df = pd.read_csv('HOF_voting.csv',sep='|')

# Duplicate player names with tags
df['player_old'] = df['player']

# Remove tags
for index, row in df.iterrows():
    name = row['player']
    #remove 'X-' from player names
    if name[0:2] == 'X-':
        clean_name = name[2:]
        df.loc[index,['player']] = clean_name
    # Remove 'HOF' from player names
    if name[-3:] == 'HOF':
        clean_name = name[0:-4]
        df.loc[index,['player']] = clean_name

# OUTPUT TO CSV
df.to_csv('HOF_voting_clean.csv',sep='|')