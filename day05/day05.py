# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 09:09:54 2017

@author: Seth Guberman - sguberman@gmail.com
"""


def read_instructions(filename):
    with open(filename) as f:
        return [int(line.strip()) for line in f]


def execute(instructions, part2=False):
    idx = 0
    steps = 0
    state = instructions

    while True:
        try:
            jump = state[idx]
            incr = -1 if part2 and jump >= 3 else 1
            state[idx] += incr
            idx += jump
            steps += 1
        except IndexError:
            break

    return state, steps


def part1():
    state, steps = execute(read_instructions('input.txt'))
    return steps


def part2():
    state, steps = execute(read_instructions('input.txt'), True)
    return steps


if __name__ == '__main__':
    print(part1())  # 360603
    print(part2())  # 25347697
