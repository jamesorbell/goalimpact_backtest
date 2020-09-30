from csv import DictReader, DictWriter
from datetime import datetime

with open('tweet_without_replies_or_changes.csv', 'r') as infile, open('final_tweets.csv, 'w') as outfile:
    reader = DictReader(infile)
    writer = DictWriter(outfile, fieldnames=reader.fieldnames)
    writer.writeheader()
    for row in reader:
        tweet_str = row['tweet__full_text']
        writer.writerow(row)
