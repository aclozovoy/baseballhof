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

# Create a new column with year_on_ballot as an integer instead of a string
df['year_on_ballot_int'] =  ''
for index, row in df.iterrows():
    year_str = row['year_on_ballot']
    year_int = int(year_str[:-2])
    df.loc[index,['year_on_ballot_int']] = year_int

# Create a new column with votes_pct as an integer instead of a string
df['votes_pct_num'] =  ''
for index, row in df.iterrows():
    pct_str = row['votes_pct']
    pct_float = float(pct_str[:-1])
    df.loc[index,['votes_pct_num']] = pct_float

# OUTPUT TO CSV
df.to_csv('HOF_voting_clean.csv',sep='|')
print(df)

# CREATE NEW TABLE WITH ONLY ONE ROW PER PLAYER

# Initialize new columns
df['is_in_hof'] = False
df['years_on_ballot'] = 0



for index, row in df.iterrows():
    # Mark is_in_hof as true if max votes_pct >= 75%
    player_max_pct = float(df.loc[df['player'] == row['player'], ['votes_pct_num']].max())
    # print(row['player'])
    # print(player_max_pct)
    if player_max_pct >= 75:
        df.loc[index,['is_in_hof']] = True

    # Years on ballot
    df.loc[index,['years_on_ballot']] = int(df.loc[df['player'] == row['player'], ['year_on_ballot_int']].max())


# Drop duplicate rows
df = df.drop_duplicates('player')
df = df.reset_index()
df = df.drop(['index', 'year', 'year_on_ballot', 'votes', 'votes_pct', 'player_old', 'year_on_ballot_int', 'votes_pct_num'], axis=1)

# OUTPUT TO CSV
df.to_csv('HOF_voting_reduced.csv',sep='|')
print(df)
print(list(df))