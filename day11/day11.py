# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:03:16 2017

@author: Seth Guberman - sguberman@gmail.com
"""


def read_moves(filename):
    with open(filename) as f:
        moves = f.read().strip().split(',')
    return moves


def distance(x, y, z):
    return max(abs(coord) for coord in (x, y, z))


def move(location, direction):
    deltas = {'n': (0, 1, -1),
              's': (0, -1, 1),
              'nw': (-1, 1, 0),
              'se': (1, -1, 0),
              'ne': (1, 0, -1),
              'sw': (-1, 0, 1)}
    return [ci + cd for ci, cd in zip(location, deltas[direction])]


def part1():
    moves = read_moves('input.txt')
    location = (0, 0, 0)
    for direction in moves:
        location = move(location, direction)
    return distance(*location)


if __name__ == '__main__':
    print(part1())  # 834
