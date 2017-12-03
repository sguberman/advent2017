#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 20:14:44 2017

@author: Seth Guberman - sguberman@gmail.com
"""


def rowdiff(row):
    return max(row) - min(row)


def checksum(spreadsheet):
    return sum(rowdiff(row) for row in spreadsheet)


def read_spreadsheet(filename):
    spreadsheet = []

    with open(filename, 'r') as f:
        for row in f:
            spreadsheet.append([int(x) for x in row.strip().split()])

    return spreadsheet


def main(filename):
    return checksum(read_spreadsheet(filename))
