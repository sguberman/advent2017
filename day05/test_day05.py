# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 09:09:38 2017

@author: Seth Guberman - sguberman@gmail.com
"""


import pytest

from day05 import execute, part1, part2


def test_execute():
    assert execute([0, 3, 0, 1, -3]) == ([2, 5, 0, 1, -2], 5)
    assert execute([0, 3, 0, 1, -3], part2=True) == ([2, 3, 2, 3, -1], 10)


def test_part1():
    assert part1() == 360603


def test_part2():
    assert part2() == 25347697


if __name__ == '__main__':
    pytest.main(['-v'])
