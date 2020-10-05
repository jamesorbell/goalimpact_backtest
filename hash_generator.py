# importing pandas as pd
import pandas as pd

# import timedelta for time mathematics
import datetime
from datetime import timedelta

# Read the csv file and construct the
# dataframe
df = pd.read_csv('csv/goalimpact_generated_odds_final.csv')

home_teams = df.home_team.tolist()
away_teams = df.away_team.tolist()
dates = df.tweet_date.tolist()
time = df.match_start_time.tolist()

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
    combine2 = hashes[k] + i[0:2] + i[3:5] + i[6:8]
    hashes[k] = combine2
    k += 1

l = 0

for i in time:
    newtime = datetime.datetime.strptime(i, '%H:%M') - timedelta(hours=2)
    combine3 = hashes[l] + newtime.strftime("%H:%M")
    hashes[l] = combine3
    l += 1

df['hash'] = hashes

cols = [0]
df.drop(df.columns[cols],axis=1,inplace=True)

# writing to final csv

df.to_csv('csv/goalimpact_generated_odds_final_HASHED.csv')
