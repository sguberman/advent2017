# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 11:39:13 2017

@author: Seth Guberman - sguberman@gmail.com
"""


from day10 import knot_hash


def part1(inp):
    grid = []
    total = 0
    for row in range(128):
        hexstr = knot_hash('{}-{}'.format(inp, row))
        binstr = ''.join('{:04b}'.format(int(d, 16)) for d in hexstr)
        grid.append(binstr)
        total += sum(d == '1' for d in binstr)
    return total, grid


total, grid = part1('jzgqcdpd')
print(total)
for row in grid[:8]:
    print(row[:8])
