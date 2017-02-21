import urllib2
import json
import csv
csvdel = ‘,’
csvquo = ‘”’
with open (‘out/tables/destination.csv’, mode=’wt’, encoding=’utf-8’) as out_file:
writer = csv.DictWriter(out_file, fieldnames=[‘col1’, ‘col2’], delimiter=csvdel, quotechar=csvquo)
writer.writeheader()
url = ‘https://www.reddit.com/r/tableau/.json’
json_obj = urllib2.urlopen(url)
data = json.load(json_obj)
for child in data[‘data’][‘children’]:
writer.writerow({‘col1’: child[‘data’][‘id’], ‘col2’: child[‘data’][‘author’]})
