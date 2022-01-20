#!/usr/bin/python3
#
# pcost.py
#
# Exercise 1.27

import csv
import sys

def portfolio_cost(filename):
    """
    :param filename:
    :return:
    """
    total = 0
    with open(filename, 'rt') as f:
        headers = next(f)  # remove 1st header line
        for line in f:
            row = line.split(',')
            # print(row)
            try:
                cost = int(row[1]) * float(row[2].strip())
                total = total + cost
            except ValueError:
                print("WARNING: Couldn't parse a line!", row)
                pass
    return total


def portfolio_cost_csv(filename):
    """
    Parse a file using CSV module
    :param filename:
    :return:
    """
    total = 0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)  # remove 1st header line
        for row in rows:
            # print(row)
            try:
                cost = int(row[1]) * float(row[2])
                total = total + cost
            except ValueError:
                print("WARNING: Couldn't parse a line!", row)
                pass
    return total


if __name__ == '__main__':
    if len(sys.argv) == 2:
        file = sys.argv[1]
    else:
        file = 'Data/portfolio.csv'
    total_cost = portfolio_cost_csv(file)
    #total_cost = portfolio_cost(file)
    print(f'Total cost: {total_cost:0.2f}')
