# importing pandas as pd
import pandas as pd

# Read the csv file and construct the
# dataframe
df = pd.read_csv('csv/Betfair Exchange_1X2_reduced.csv')

dates = df.date.tolist()

date = []
time = []

for i in dates:
    split_string = i.split(' ')
    date_string_matrix = split_string[0].split('/')
    time_string_matrix = split_string[1].split(':')
    final_date_string = date_string_matrix[1].zfill(2) + '/' + date_string_matrix[0].zfill(2) + '/' + date_string_matrix[2][2:4]
    final_time_string = time_string_matrix[0].zfill(2) + ':' + time_string_matrix[1].zfill(2)
    date.append(final_date_string)
    time.append(final_time_string)

cols = [0,1]
df.drop(df.columns[cols],axis=1,inplace=True)

df['date'] = date
df['time'] = time

# writing to final csv
df.to_csv('csv/betfair_exchange_odds_final.csv')
