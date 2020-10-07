# importing pandas as pd
import pandas as pd
import numpy as np

# Read the csv file and construct the
# dataframe
df = pd.read_csv('csv/MERGED_WITHOUT_DUPLICATES.csv')

# Convert goalimpact implied probabilities to odds and add them as new columns.

GI_percentages_1 = df.home_odds_1.tolist()
GI_percentages_X = df.home_odds_X.tolist()
GI_percentages_2 = df.home_odds_2.tolist()

GI_odds_1 = []
GI_odds_X = []
GI_odds_2 = []

for i in GI_percentages_1:
    calculated_odds_1 = (1/(float(i)/100))
    GI_odds_1.append(round(calculated_odds_1, 2))

for j in GI_percentages_X:
    calculated_odds_2 = (1/(float(j)/100))
    GI_odds_X.append(round(calculated_odds_2, 2))

for k in GI_percentages_2:
    calculated_odds_3 = (1/(float(k)/100))
    GI_odds_2.append(round(calculated_odds_3, 2))

# Calculate value for each sets of odds by comparing them to the betfair offered odds.

betfair_odds_1 = df['1_closing_value'].tolist()
betfair_odds_X = df['2_closing_value'].tolist()
betfair_odds_2 = df['3_closing_value'].tolist()

odds_1_value = []
odds_X_value = []
odds_2_value = []

for i in betfair_odds_1:
    betfair_odds_percentage1 = (1/i)*100
    goalimpact_odds_percentage1 = (1/GI_odds_1[betfair_odds_1.index(i)])*100
    value = round(goalimpact_odds_percentage1 - betfair_odds_percentage1,2)
    odds_1_value.append(value)

for j in betfair_odds_X:
    betfair_odds_percentage2 = (1/j)*100
    goalimpact_odds_percentage2 = (1/GI_odds_X[betfair_odds_X.index(j)])*100
    value = round(goalimpact_odds_percentage2 - betfair_odds_percentage2,2)
    odds_X_value.append(value)

for k in betfair_odds_2:
    betfair_odds_percentage3 = (1/k)*100
    goalimpact_odds_percentage3 = (1/GI_odds_2[betfair_odds_2.index(k)])*100
    value = round(goalimpact_odds_percentage3 - betfair_odds_percentage3,2)
    odds_2_value.append(value)

# Calculate the value bet in each situation.

# Column key:
# Lay_1 - Lay home, Lay_X - Lay draw, Lay_2 - Lay away
# Back_1 - Back home, Back_X - Back draw, Back_2 - Back away
# NaN - No value over given threshold.

value_string = []

for i in odds_1_value:
    value_1 = i
    value_X = odds_X_value[odds_1_value.index(i)]
    value_2 = odds_2_value[odds_1_value.index(i)]

    values = [value_1,value_X,value_2]

    values_transformed = []
    for i in values:
        absolute_number = abs(i)
        values_transformed.append(absolute_number)

    biggest_value = values_transformed.index(max(values_transformed))

    if values[biggest_value] >= 0:
        # This means that the value is with backing.
        if biggest_value == 0 and values[biggest_value] >= 20:
            # Most value in backing the home team.
            value_string.append('Back_1')

        elif biggest_value == 1 and values[biggest_value] >= 20:
            # Most value in backing the draw.
            value_string.append('Back_X')

        elif biggest_value == 2 and values[biggest_value] >= 20:
            # Most value in backing the away team.
            value_string.append('Back_2')

        else:
            value_string.append('')

    else:
        # This means that value is in laying.
        if biggest_value == 0 and values[biggest_value] <= -20:
            # Most value in backing the home team.
            value_string.append('Lay_1')

        elif biggest_value == 1 and values[biggest_value] <= -20:
            # Most value in backing the draw.
            value_string.append('Lay_X')

        elif biggest_value == 2 and values[biggest_value] <= -20:
            # Most value in backing the away team.
            value_string.append('Lay_2')

        else:
            value_string.append('')

# Add newly calculated stuff into the dataframe, ready for pushing to the final dataframe.
df['GI_home_odds_1'] = GI_odds_1
df['GI_home_odds_X'] = GI_odds_X
df['GI_home_odds_2'] = GI_odds_2

df['value_1'] = odds_1_value
df['value_X'] = odds_X_value
df['value_2'] = odds_2_value

df['bet_value'] = value_string

# Deleting unnecessary columns.
cols = [0,1]
df.drop(df.columns[cols],axis=1,inplace=True)

# print count to show number of bets
no_of_bets = (df['bet_value'] != '').sum()
message = str(no_of_bets) + " total value bets discovered."
print(message)

# writing to final csv
df.to_csv('csv/FINAL_CSV.csv')
