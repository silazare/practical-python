#!/usr/bin/python3
#
# pcost.py
#
# Exercise 1.27

total_cost = 0

with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f) # remove 1st header line
    for line in f:
        row = line.split(',')
        print(row)
        cost = int(row[1]) * float(row[2].strip())
        total_cost = total_cost + cost

print('====')
print(f'Total cost: {total_cost:0.2f}')
