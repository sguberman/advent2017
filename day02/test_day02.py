#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 20:13:58 2017

@author: Seth Guberman - sguberman@gmail.com
"""


import pytest

from day02 import rowdiff, checksum, read_spreadsheet, main, rowdiv, main2


def test_rowdiff():
    assert rowdiff([5, 1, 9, 5]) == 8
    assert rowdiff([7, 5, 3]) == 4
    assert rowdiff([2, 4, 6, 8]) == 6


def test_checksum():
    assert checksum([[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]) == 18


def test_read_spreadsheet():
    spreadsheet = [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]
    assert read_spreadsheet('test_input.txt') == spreadsheet


def test_main():
    assert main('test_input.txt') == 18
    assert main('input.txt') == 36766


def test_rowdiv():
    assert rowdiv([5, 9, 2, 8]) == 4
    assert rowdiv([9, 4, 7, 3]) == 3
    assert rowdiv([3, 8, 6, 5]) == 2


def test_main2():
    assert main2('test_input2.txt') == 9


if __name__ == '__main__':
    pytest.main()
