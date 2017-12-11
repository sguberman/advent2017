# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 12:30:18 2017

@author: Seth Guberman - sguberman@gmail.com
"""


import pytest

from day11 import move, distance, solution


testdata = [
        (('ne', 'ne', 'ne'), 3),
        (('ne', 'ne', 'sw', 'sw'), 0),
        (('ne', 'ne', 's', 's'), 2),
        (('se', 'sw', 'se', 'sw', 'sw'), 3),
]


@pytest.mark.parametrize('moves,expected', testdata)
def test_examples(moves, expected):
    location = (0, 0, 0)
    for direction in moves:
        location = move(location, direction)
    assert distance(*location) == expected


def test_solution():
    assert solution() == (834, 1569)

if __name__ == '__main__':
    pytest.main(['-v'])
