import json

import csv

parsed = json.loads(data)

data = parsed['details']

# open a file for writing

data = open('Data.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(data)

count = 0

for data_info in data:

      if count == 0:

             header = data_info.keys()

             csvwriter.writerow(header)

             count += 1

      csvwriter.writerow(data_info.values())

data.close()
