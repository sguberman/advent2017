# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 14:21:19 2017

@author: Seth Guberman - sguberman@gmail.com
"""


import pytest

from day03 import distance, steps_to_origin, part1


def test_distance():
    assert distance(0, 0) == 0
    assert distance(2, 1) == 3
    assert distance(0, -2) == 2


def test_steps_to_origin():
    assert steps_to_origin(1) == 0
    assert steps_to_origin(12) == 3
    assert steps_to_origin(23) == 2
    assert steps_to_origin(1024) == 31


def test_part1():
    assert part1() == 419


if __name__ == '__main__':
    pytest.main()
