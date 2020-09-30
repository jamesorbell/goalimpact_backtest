# importing pandas as pd
import pandas as pd

# Read the csv file and construct the
# dataframe
df = pd.read_csv('tweet_without_replies_or_changes.csv')

full_texts = df.tweet__full_text.tolist()

match_info_list = []
spread_list = []
home_odds_list = []
neutral_odds_list = []

for i in full_texts:
    split_text = i.split('\\n')
    if len(split_text) != 4:
        print('This line does not have 4 arguments: ')
        print(split_text)
    else:
        match_info_list.append(split_text[0])
        spread_list.append(split_text[1])
        home_odds_list.append(split_text[2])
        neutral_odds_list.append(split_text[3])

print(match_info_list[0])
print(spread_list[0])
print(home_odds_list[0])
print(neutral_odds_list[0])

df['match_info'] =  match_info_list
df['spread'] = spread_list
df['home_odds'] = home_odds_list
df['neutral_odds'] = neutral_odds_list

df.to_csv('split_tweets.csv')
