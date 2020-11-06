# importing pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the csv file and construct the
# dataframe
df = pd.read_csv('csv/FINAL_CSV_FIXED.csv')

df = df[pd.notnull(df['bet_value'])]
df = df[pd.notnull(df['winner_ft'])]

# Profit and total values. Starts at 0.
profit = 0

# Chosen fix stake.
stake = 100

# Bet count
bet_count = 1

# starting bank, this is for percentage staking system
bank = 5000
percent_stake = 0.02

# array for pyplot
data_points1 = []
data_points2 = []

for index, row in df.iterrows():

    bet_action = row['bet_value']
    betfair_1_odds = row['1_closing_value']
    betfair_X_odds = row['2_closing_value']
    betfair_2_odds = row['3_closing_value']

    if (bank*percent_stake) <= 1000:
        stake_for_percent = bank*percent_stake
    else:
        stake_for_percent = 1000

    output_string = row['team_1'] + ' vs ' + row['team_2'] + ', ' + row['bet_value'] + ', ' + row['winner_ft']
    print(output_string)

    if bet_action == 'Back_1':
        # Action is backing the home team.
        if row['winner_ft'] == 'H':
            profit += ((betfair_1_odds * stake) - stake)
            bank +=  ((betfair_1_odds * stake_for_percent) - stake_for_percent)
            print('Bet No: ' + str(bet_count) + ' Profit: ' + str(((betfair_1_odds * stake_for_percent) - stake_for_percent)))
        else:
            profit = profit - stake
            bank = bank - stake_for_percent
            print('Bet No: ' + str(bet_count) + ' Profit: -'+ str(stake_for_percent))
    elif bet_action == 'Back_X':
        # Action is backing the draw.
        if row['winner_ft'] == 'D':
            profit += ((betfair_X_odds * stake) - stake)
            bank +=  ((betfair_X_odds * stake_for_percent) - stake_for_percent)
            print('Bet No: ' + str(bet_count) + ' Profit: ' + str(((betfair_X_odds * stake_for_percent) - stake_for_percent)))
        else:
            profit = profit - stake
            bank = bank - stake_for_percent
            print('Bet No: ' + str(bet_count) + ' Profit: -'+ str(stake_for_percent))
    elif bet_action == 'Back_2':
        # Action is backing the away team.
        if row['winner_ft'] == 'A':
            profit += ((betfair_2_odds * stake) - stake)
            bank +=  ((betfair_2_odds * stake_for_percent) - stake_for_percent)
            print('Bet No: ' + str(bet_count) + ' Profit: ' + str(((betfair_2_odds * stake_for_percent) - stake_for_percent)))
        else:
            profit = profit - stake
            bank = bank - stake_for_percent
            print('Bet No: ' + str(bet_count) + ' Profit: -'+ str(stake_for_percent))
    elif bet_action == 'Lay_1':
        # Action is laying the home team.
        if row['winner_ft'] != 'H':
            profit += (stake/(betfair_1_odds - 1))
            bank += (stake_for_percent/(betfair_1_odds - 1))
            print('Bet No: ' + str(bet_count) + ' Profit: ' + str((stake_for_percent/(betfair_1_odds - 1))))
        else:
            profit = profit - stake
            bank = bank - stake_for_percent
            print('Bet No: ' + str(bet_count) + ' Profit: -'+ str(stake_for_percent))
    elif bet_action == 'Lay_X':
        # Action is laying the draw.
        if row['winner_ft'] != 'D':
            profit += (stake/(betfair_X_odds - 1))
            bank += (stake_for_percent/(betfair_X_odds - 1))
            print('Bet No: ' + str(bet_count) + ' Profit: ' + str((stake_for_percent/(betfair_1_odds - 1))))
        else:
            profit = profit - stake
            bank = bank - stake_for_percent
            print('Bet No: ' + str(bet_count) + ' Profit: -'+ str(stake_for_percent))
    elif bet_action == 'Lay_2':
        # Action is laying the away team.
        if row['winner_ft'] != 'A':
            profit += (stake/(betfair_2_odds - 1))
            bank += (stake_for_percent/(betfair_2_odds - 1))
            print('Bet No: ' + str(bet_count) + ' Profit: ' + str((stake_for_percent/(betfair_1_odds - 1))))
        else:
            profit = profit - stake
            bank = bank - stake_for_percent
            print('Bet No: ' + str(bet_count) + ' Profit: -'+ str(stake_for_percent))
    else:
        print('No action detected, error.')
        # Some error detected, throws to the terminal.\

    data_points1.append(profit)
    data_points2.append(bank)

    bet_count += 1

# writing to final csv
df.to_csv('csv/ONLY_BETS.csv')

print('Final fix staked profit, with £' + str(stake) + ' stakes: £' + str(round(profit,2)))
print('Final percentage staked profit: £' + str(round((bank-2000),2)))
print('----------')
print('Note: This includes all betfair fees paid, so only pure profit is applied.')
print('----------')
print('Number of bets: ' + str(bet_count))
print('----------')

plt.plot(data_points1)
plt.axis([0,5000,-1000,200000])
plt.ylabel('Cumulative profit, in £')
plt.xlabel('No. of bets')
plt.show()

plt.plot(data_points2)
plt.ylabel('Cumulative profit, in £')
plt.xlabel('No. of bets')
plt.show()
