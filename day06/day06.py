#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 14:50:49 2017

@author: Seth Guberman - sguberman@gmail.com
"""


from itertools import count


def reallocate(memory):
    memory = list(memory)
    size = len(memory)
    blocks = max(memory)
    idx = memory.index(blocks)
    memory[idx] = 0
    while blocks:
        idx = (idx + 1) % size
        memory[idx] += 1
        blocks -= 1
    return tuple(memory)


def detect_loop(memory):
    seen = {memory: 0}
    for step in count(1):
        memory = reallocate(memory)
        if memory in seen:
            return step, step - seen[memory]
        seen[memory] = step


def read_input(filename):
    with open(filename) as f:
        return tuple(int(x) for x in f.read().split())


def solution():
    memory = read_input('input.txt')
    return detect_loop(memory)


if __name__ == '__main__':
    print(solution())  # 5042, 1086
