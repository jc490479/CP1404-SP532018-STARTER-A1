

import csv

list = []
csv_reader = csv.reader(open("songs.csv"))
for row in csv_reader:
    list.append(row)


for index, element in enumerate(list):
    if element[3] == "y":
       element[3] = "*"
    else:
       element[3] = ""


