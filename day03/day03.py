# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 14:21:41 2017

@author: Seth Guberman - sguberman@gmail.com
"""


from collections import defaultdict
from itertools import count


def distance(x, y):
    """
    Return the Manhattan Distance from the (x, y) point to the origin.
    """
    return abs(x) + abs(y)


def steps_to_origin(number):

    for value, (x, y) in diagonals():
        if value == number:  # shortcut if number lands on a diagonal
            return distance(x, y)
        elif value > number:  # start at the next diagonal and work back
            startval = value
            startx = x
            starty = y
            break

    value = startval
    x = startx
    y = starty

    while x > -startx:  # search left until bottom left corner
        value -= 1
        x -= 1
        if value == number:
            return distance(x, y)
    while y < -starty:  # search up until top left corner
        value -= 1
        y += 1
        if value == number:
            return distance(x, y)
    while x < startx:  # search right until top right corner
        value -= 1
        x += 1
        if value == number:
            return distance(x, y)
    while y > starty:  # search down until bottom right corner
        value -= 1
        y -= 1
        if value == number:
            return distance(x, y)


def diagonal_locations():
    """
    Generate the (x, y) location of the bottom right corner of each spiral
    layer, relative to the access port.
    """
    return zip(count(0, 1), count(0, -1))


def diagonal_values():
    """
    Generate the value of the bottom right corner of each spiral layer. These
    are the perfect squares of the odd numbers. Ex: 1, 9, 25, 49, 81, etc.
    """
    for v in count(1, 2):
        yield v ** 2


def diagonals():
    """
    Generate the value and location of the bottom right corner of each spiral.
    """
    return zip(diagonal_values(), diagonal_locations())


def part1(number):
    return steps_to_origin(number)


def neighbors(x, y):
    dxdy = (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)
    return [(x + dx, y + dy) for dx, dy in dxdy]


def spiral_locations():
    x, y = 0, 0
    for i in count(1):
        while x < i:  # to the right
            x += 1
            yield (x, y)
        while y < i:  # up
            y += 1
            yield (x, y)
        while x > -i:  # to the left
            x -= 1
            yield (x, y)
        while y > -i:  # down
            y -= 1
            yield (x, y)
        while x < i:  # to the right
            x += 1
            yield (x, y)


def part2(number):
    spiral = defaultdict(int)
    spiral[(0, 0)] = 1
    for x, y in spiral_locations():
        value = sum(spiral[loc] for loc in neighbors(x, y))
        if value > number:
            return value
        spiral[(x, y)] = value


if __name__ == '__main__':
    print(part1(289326))  # 419
    print(part2(289326))  # 295229
