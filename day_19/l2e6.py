# Read the hacker news csv file and find out: 
# a) Count the number of lines containing python or Python 
# b) Count the number lines containing JavaScript, javascript or Javascript 
# c) Count the number lines containing Java and not JavaScript

import csv
import re

a=0
b=0
c=0

with open('day_19/data/hacker_news.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    line_count=0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
            continue
        row = " ".join(row)
        p = re.findall(r'[Pp]ython',row)
        if p:
            a+=1
        j = re.findall(r'[Jj]ava[Ss]cript',row)
        if j:
            b+=1
        jns = re.findall(r'Java(?!Script)',row)
        if jns:
            c+=1

print(f"lines containing python or Python {a}")
print(f"lines JavaScript, javascript or Javascript {b}")
print(f"lines containing Java and not JavaScript {c}")