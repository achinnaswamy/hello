import json
import csv
f =  open ('out/tables/destination2.csv')
writer = csv.writer(f)
url = 'https://www.reddit.com/r/tableau/.json'
json_obj = urllib2.urlopen(url)
data = json.load(json_obj)
for child in data['data']['children']:
    writer.writerow({child['data']['id'], child['data']['author']}) 
