#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 20:14:44 2017

@author: Seth Guberman - sguberman@gmail.com
"""


def rowdiff(row):
    return max(row) - min(row)


def checksum(spreadsheet, func=rowdiff):
    return sum(func(row) for row in spreadsheet)


def read_spreadsheet(filename):
    spreadsheet = []

    with open(filename, 'r') as f:
        for row in f:
            spreadsheet.append([int(x) for x in row.strip().split()])

    return spreadsheet


def main(filename):
    return checksum(read_spreadsheet(filename))


def rowdiv(row):
    for i, a in enumerate(row):
        for b in row[:i] + row[i+1:]:
            if a % b == 0:
                return a // b


def main2(filename):
    return checksum(read_spreadsheet(filename), func=rowdiv)


if __name__ == '__main__':
    print(main('input.txt'))  # part 1: 36766
