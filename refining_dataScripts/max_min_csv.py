# This file is associated with ./prob-state2/solution.py

import csv

filename = './assests/maintained/district.csv'
temp = []
with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)

    for row in csv_reader:
        if (row[3] == 'A4'):
            pass
        else:
            temp.append(int(row[3]))
temp.sort()
print(temp[-5:])
print(temp[:6])
