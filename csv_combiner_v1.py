import pandas as pd

# Read from two csv files

a = pd.read_csv('csv\Betfair Exchange_1X2_reduced.csv')
b = pd.read_csv('csv\goalimpact_generated_odds_final_HASHED.csv')

# replace to on=['name', 'feature', 'ipaddress'] if needed.
# In example you don't have 'ipaddress', but in your code you have it

c = pd.merge(a, b, how='inner', on=['hash'])

cols = [0]
c.drop(c.columns[cols],axis=1,inplace=True)

#Uncomment to save to file
c.to_csv('csv\combined_csv.csv')
