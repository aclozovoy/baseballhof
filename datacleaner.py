import numpy as np
import pandas as pd

# IMPORT DATA
df = pd.read_csv('HOF_voting.csv',sep='|')

# Drop second index
df = df.drop(columns = 'Unnamed: 0')

# Initialize new columns
df['year_on_ballot_int'] =  ''
df['votes_pct_num'] =  ''
df['is_in_hof'] = False
df['years_on_ballot'] = ''


# Remove tags from player names
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

# Convert strings to numbers
for index, row in df.iterrows():
    # Votes_pct: string --> int
    year_str = row['year_on_ballot']
    year_int = int(year_str[:-2])
    df.loc[index,['year_on_ballot_int']] = year_int
    # Votes_pct: string --> float
    pct_str = row['votes_pct']
    pct_float = float(pct_str[:-1])
    df.loc[index,['votes_pct_num']] = pct_float

for index, row in df.iterrows():
    # Mark is_in_hof as true if max votes_pct >= 75%
    player_max_pct = float(df.loc[df['player'] == row['player'], ['votes_pct_num']].max())
    if player_max_pct >= 75:
        df.loc[index,['is_in_hof']] = True

    # Years on ballot
    df.loc[index,['years_on_ballot']] = int(df.loc[df['player'] == row['player'], ['year_on_ballot_int']].max())

# CREATE YEAR TABLE WITH ONE ROW PER PLAYER PER YEAR OF VOTING

# Extract single year voting values
df_year = df[['year', 'player', 'year_on_ballot', 'year_on_ballot_int', 'votes', 'votes_pct', 'votes_pct_num']].copy()

# OUTPUT TO CSV
df_year.to_csv('HOF_voting_year.csv',sep='|')


# CREATE CAREER TABLE WITH ONLY ONE ROW PER PLAYER

# Drop duplicate player rows
df_career = df.drop_duplicates('player')
df_career = df_career.reset_index()

# Drop single year values
df_career = df_career.drop(['index', 'year', 'year_on_ballot', 'year_on_ballot_int', 'votes', 'votes_pct', 'votes_pct_num'], axis=1)

# OUTPUT TO CSV
df_career.to_csv('HOF_voting_career.csv',sep='|')
