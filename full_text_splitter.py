# importing pandas as pd
import pandas as pd

# Read the csv file and construct the
# dataframe
df = pd.read_csv('csv/split_tweets_reduced.csv')

# splitting the time and date field

tweet_details = df.tweet__created_at.tolist()

tweet_time = []
tweet_date = []

for i in tweet_details:
    split_text = i.split(' ')
    if len(split_text) != 2:
        print('This line does not have 2 arguments: ')
        print(split_text)
    else:
        tweet_time.append(split_text[0])
        tweet_date.append(split_text[1])


df['tweet_time'] =  tweet_time
df['tweet_date'] = tweet_date

# splitting the tweet text

tweet_text = df.match_info.tolist()

match_start_time = []
home_team = []
away_team = []

for i in tweet_text:
    text = str(i)
    split_time = text[0:5]
    split_tail = text[7:]
    match_start_time += [split_time]

    split_text1 = split_tail.split(" vs. ")
    home_team.append(split_text1[0])
    away_team.append(split_text1[1])

df['match_start_time'] = match_start_time
df['home_team'] = home_team
df['away_team'] = away_team

# splitting the HOME odds set

home_venue_odds = df.home_odds.tolist()

home_venue_1 = []
home_venue_X = []
home_venue_2 = []

for i in home_venue_odds:
    split_text2 = i.split(' ')
    home_venue_1.append(split_text2[1])
    home_venue_X.append(split_text2[3])
    home_venue_2.append(split_text2[5])

df['home_odds_1'] = home_venue_1
df['home_odds_X'] = home_venue_X
df['home_odds_2'] = home_venue_2

# deleting unnecessary columns

cols = [0,1,2,3,4]
df.drop(df.columns[cols],axis=1,inplace=True)

# writing to final csv

df.to_csv('csv/goalimpact_generated_odds_final.csv')
