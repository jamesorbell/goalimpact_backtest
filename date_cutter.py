from csv import DictReader, DictWriter
from datetime import datetime

with open('tweet_without_replies_or_changes.csv', 'r') as infile, open('final_tweets.csv, 'w') as outfile:
    reader = DictReader(infile)
    writer = DictWriter(outfile, fieldnames=reader.fieldnames)
    writer.writeheader()
    for row in reader:
        if not row['tweet__created_at'].isspace():
            date_time_str = row['tweet__created_at']
            date_time_str1 = date_time_str[0:6].lower() + ' ' + date_time_str[16:20] + ' ' + date_time_str[7:15]
            date_time_obj = datetime.strptime(date_time_str1, '%b %d %Y %H:%M:%S')
            final_date_time_str = datetime.strftime(date_time_obj,'%H:%M:%S %d/%m/%y')
            row['tweet__created_at'] = final_date_time_str
            writer.writerow(row)
