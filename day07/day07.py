# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 15:58:32 2017

@author: Seth Guberman - sguberman@gmail.com
"""

from collections import defaultdict


weights = {}
children = defaultdict(list)
parents = {}

with open('input.txt') as f:
    for line in f:
        lhs, *rhs = line.strip().split(' -> ')
        program, weight = lhs.split()
        weight = int(weight[1:-1])
        weights[program] = weight
        if rhs:
            for child in rhs[0].split(', '):
                children[program].append(child)
                parents[child] = program

for program in parents.values():
    if all(program not in v for v in children.values()):
        print(program)
