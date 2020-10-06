# importing pandas as pd
import pandas as pd
import numpy as np

# Read the csv file and construct the
# dataframe
df = pd.read_csv('csv/FINAL_CSV.csv')

df = df[pd.notnull(df['bet_value'])]

# Profit and total values. Starts at 0.
profit = 0
total_staked = 0

# Chosen fix stake.
stake = 100

# Bet count
bet_count = 0

for index, row in df.iterrows():

    bet_count += 1

    bet_action = row['bet_value']
    betfair_1_odds = row['1_closing_value']
    betfair_X_odds = row['2_closing_value']
    betfair_2_odds = row['3_closing_value']

    if bet_action == 'Back_1':
        # Action is backing the home team.
        if row['winner_ft'] == 'H':
            profit += (0.98 * ((betfair_1_odds * stake) - stake))
            total_staked += stake
        else:
            profit = profit - stake
            total_staked += stake
    elif bet_action == 'Back_X':
        # Action is backing the draw.
        if row['winner_ft'] == 'D':
            profit += (0.98 * ((betfair_X_odds * stake) - stake))
            total_staked += stake
        else:
            profit = profit - stake
            total_staked += stake
    elif bet_action == 'Back_2':
        # Action is backing the away team.
        if row['winner_ft'] == 'A':
            profit += (0.98 * ((betfair_2_odds * stake) - stake))
            total_staked += stake
        else:
            profit = profit - stake
            total_staked += stake
    elif bet_action == 'Lay_1':
        # Action is laying the home team.
        if row['winner_ft'] != 'H':
            profit += (0.98 * (stake/(betfair_1_odds - 1)))
            total_staked += stake
        else:
            profit = profit - stake
            total_staked += stake
    elif bet_action == 'Lay_X':
        # Action is laying the draw.
        if row['winner_ft'] != 'D':
            profit += (0.98 * (stake/(betfair_1_odds - 1)))
            total_staked += stake
        else:
            profit = profit - stake
            total_staked += stake
    elif bet_action == 'Lay_2':
        # Action is laying the away team.
        if row['winner_ft'] != 'A':
            profit += (0.98 * (stake/(betfair_1_odds - 1)))
            total_staked += stake
        else:
            profit = profit - stake
            total_staked += stake
    else:
        print('No action detected, error.')
        # Some error detected, throws to the terminal.

print('Final fix staked profit, with £' + str(stake) + ' stakes: £' + str(round(profit,2)))
print('Note: This includes all betfair fees paid, so only pure profit is applied.')
print('Total staked: £' + str(total_staked))
print('Number of bets: ' + str(bet_count))
