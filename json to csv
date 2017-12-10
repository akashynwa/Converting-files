import json

import csv

parsed = json.loads(data)

data = parsed['details']

# open a file for writing

employ_data = open('Data.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(employ_data)

count = 0

for emp in data:

      if count == 0:

             header = emp.keys()

             csvwriter.writerow(header)

             count += 1

      csvwriter.writerow(emp.values())

employ_data.close()
