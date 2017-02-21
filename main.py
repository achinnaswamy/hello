import json
import csv
with open ('out/tables/destination.csv', mode='wt', encoding='utf-8') as out_file:
     writer = csv.writer(out_file)
url = 'https://www.reddit.com/r/tableau/.json'
json_obj = urllib2.urlopen(url)
data = json.load(json_obj)
for child in data['data']['children']:
    writer.writerow({child['data']['id'], child['data']['author']}) 
