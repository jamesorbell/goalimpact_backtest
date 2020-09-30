# importing pandas as pd
import pandas as pd

# Read the csv file and construct the
# dataframe
df = pd.read_csv('tweet_sorted_by_date.csv')

# First filter out those rows which
# does not contain any data
df = df.dropna(how = 'all')

# Filter all rows for which the player's
# age is greater than or equal to 25
df.drop(df[df['tweet__full_text'].str[0].str.isdigit() == False].index, inplace = True)
df.drop(df[df['tweet__in_reply_to_user_id_str'].notnull()].index, inplace = True)

df.to_csv('tweet_without_replies_or_changes.csv')
