# importing pandas as pd
import pandas as pd

# Read the csv file and construct the
# dataframe
df = pd.read_csv('csv/Betfair Exchange_1X2_2016-2017_2020-2021.csv', engine='python')

home_teams = df.team_1.tolist()
away_teams = df.team_2.tolist()
dates = df.date.tolist()

hashes = []

for i in home_teams:
    hashes.append(i[0])

j = 0

for i in away_teams:
    combine1 = hashes[j] + i[0]
    hashes[j] = combine1
    j += 1

k = 0

for i in dates:
    split_date = i.split('/')
    time = split_date[2].split(' ')[1]
    converted_time_matrix = time.split(':')
    combine2 = hashes[k] + split_date[1].zfill(2) + split_date[0].zfill(2) + split_date[2][2:4] + converted_time_matrix[0].zfill(2) + ':' + converted_time_matrix[1]
    hashes[k] = combine2
    k += 1

df['hash'] = hashes

# deleting unnecessary columns

cols = [0,1,2,4,5,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40,41,42,44,45,46,48,49,50,51,52]
df.drop(df.columns[cols],axis=1,inplace=True)

df.dropna(subset=['Betfair Exchange_1X2 Full Time_outcome_1_closing_value', 'Betfair Exchange_1X2 Full Time_outcome_2_closing_value', 'Betfair Exchange_1X2 Full Time_outcome_3_closing_value'], inplace=True)

# writing to final csv

df.to_csv('csv/Betfair Exchange_1X2_reduced.csv')
