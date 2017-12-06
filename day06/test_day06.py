#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 14:50:30 2017

@author: Seth Guberman - sguberman@gmail.com
"""


import pytest

from day06 import reallocate, detect_loop, solution, read_input


testdata = [((0, 2, 7, 0), (2, 4, 1, 2)),
            ((2, 4, 1, 2), (3, 1, 2, 3)),
            ((3, 1, 2, 3), (0, 2, 3, 4)),
            ((0, 2, 3, 4), (1, 3, 4, 1)),
            ((1, 3, 4, 1), (2, 4, 1, 2))]


@pytest.mark.parametrize('memory,result', testdata)
def test_reallocate(memory, result):
    assert reallocate(memory) == result


def test_detect_loop():
    assert detect_loop((0, 2, 7, 0)) == (5, 4)


def test_solution():
    assert solution() == (5042, 1086)


def test_read_input():
    memory = read_input('input.txt')
    assert isinstance(memory, tuple)
    assert len(memory) == 16
    assert all(isinstance(x, int) for x in memory)


if __name__ == '__main__':
    pytest.main(['-v'])
