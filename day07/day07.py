# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 15:58:32 2017

@author: Seth Guberman - sguberman@gmail.com
"""

from collections import defaultdict


def build_tree(filename):
    weights = {}
    children = defaultdict(list)
    parents = {}

    with open(filename) as f:
        for line in f:
            lhs, *rhs = line.strip().split(' -> ')
            program, weight = lhs.split()
            weight = int(weight[1:-1])
            weights[program] = weight
            if rhs:
                for child in rhs[0].split(', '):
                    children[program].append(child)
                    parents[child] = program

    return weights, children, parents


def find_root(children, parents):
    for program in parents.values():
        if all(program not in v for v in children.values()):
            return program


def part1():
    weights, children, parents = build_tree('input.txt')
    return find_root(children, parents)


if __name__ == '__main__':
    print(part1())  # mkxke
