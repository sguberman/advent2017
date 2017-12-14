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


def part2(grid):

    # First start with a region for each used square in the grid.
    # Each region is a set with the (i, j) location of the used square
    # and its neighbors (left/right and up/down).
    regions = set()
    for i, row in enumerate(grid):
        for j, x in enumerate(row):
            if x == '1':
                region = frozenset({(i, j),
                                    (i + 1, j), (i - 1, j),
                                    (i, j + 1), (i, j - 1)})
                regions.add(region)

    # Now go through the list of regions and combine intersecting sets.
    # Keep doing that until the list doesn't get any smaller.
    prev_len = len(regions) + 1
    while len(regions) != prev_len:
        prev_len = len(regions)
        combined = set()
        region = regions.pop()
        for other in regions:
            if not region.isdisjoint(other):
                combined.add(region)
                combined.add(other)
                new_regions.add(frozenset(region | other)
        regions -= combined
        regions += new_regions



total, grid = part1('jzgqcdpd')
print(total)
for row in grid[:8]:
    print(row[:8])
