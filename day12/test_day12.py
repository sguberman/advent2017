# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 09:25:51 2017

@author: Seth Guberman - sguberman@gmail.com
"""


import pytest

from day12 import read_input, group_containing, part1, unique_groups, part2


def test_read_input():
    expected = {0: [2],
                1: [1],
                2: [0, 3, 4],
                3: [2, 4],
                4: [2, 3, 6],
                5: [6],
                6: [4, 5]}
    assert read_input('test_input.txt') == expected


def test_group_containing():
    graph = read_input('test_input.txt')
    expected = {0, 2, 3, 4, 5, 6}
    assert group_containing(0, graph) == expected


def test_part1():
    assert part1() == 306


def test_unique_groups():
    assert len(unique_groups(read_input('test_input.txt'))) == 2


def test_part2():
    assert part2() == 200


if __name__ == '__main__':
    pytest.main(['-v'])
