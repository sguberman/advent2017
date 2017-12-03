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
