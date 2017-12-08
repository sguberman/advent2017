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


def stack_weight(program, weights, children):
    w = weights[program]
    if program not in children:
        return w
    else:
        return w + sum(stack_weight(child, weights, children)
                       for child in children[program])


def is_balanced(program, weights, children):
    if not children[program]:
        return True
    else:
        first_w = stack_weight(children[program][0], weights, children)
        all_w = (stack_weight(c, weights, children) for c in children[program])
        return all(c_w == first_w for c_w in all_w)


def find_imbalance(start, weights, children):
    todo = [start]
    while todo:
        current = todo.pop()
        print('current: ', current, 'todo: ', todo)
        if all(is_balanced(c, weights, children) for c in children[current]):
            for c in children[current]:
                print(weights[c], stack_weight(c, weights, children))
        else:
            todo.extend(children[current])


def part2():
    weights, children, parents = build_tree('input.txt')
    root = find_root(children, parents)
    find_imbalance(root, weights, children)


if __name__ == '__main__':
    print(part1())  # mkxke
    part2()
