import json
import csv
import requests
with open ('out/tables/destination.csv', mode='wt', encoding='utf-8') as out_file:
     writer = csv.writer(out_file)
     r = requests.get('https://www.reddit.com/r/tableau/.json', headers = {'User-agent': 'Chrome'})
     r.text
     data = r.json()
     for child in data['data']['children']:
          writer.writerow({child['data']['id'], child['data']['author']})
