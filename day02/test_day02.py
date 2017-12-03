#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 20:13:58 2017

@author: Seth Guberman - sguberman@gmail.com
"""


import pytest

from day02 import rowdiff, checksum, read_spreadsheet


def test_rowdiff():
    assert rowdiff([5, 1, 9, 5]) == 8
    assert rowdiff([7, 5, 3]) == 4
    assert rowdiff([2, 4, 6, 8]) == 6


def test_checksum():
    assert checksum([[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]) == 18


def test_read_spreadsheet():
    spreadsheet = [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]
    assert read_spreadsheet('test_input.txt') == spreadsheet


if __name__ == '__main__':
    pytest.main()
