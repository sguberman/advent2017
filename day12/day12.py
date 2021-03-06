# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 09:32:06 2017

@author: Seth Guberman - sguberman@gmail.com
"""


def read_input(filename):
    graph = {}
    with open(filename) as f:
        for line in f:
            lhs, rhs = line.strip().split(' <-> ')
            graph[int(lhs)] = [int(x) for x in rhs.split(', ')]
    return graph


def group_containing(node, graph):
    group = set()
    todo = {node}
    while todo:
        new = todo.pop()
        group.add(new)
        for neighbor in graph[new]:
            if neighbor not in group:
                todo.add(neighbor)
    return group


def part1():
    return len(group_containing(0, read_input('input.txt')))


def unique_groups(graph):
    groups = set()
    todo = set(graph.keys())
    while todo:
        new = todo.pop()
        new_group = group_containing(new, graph)
        groups.add(tuple(new_group))
        todo -= new_group
    return groups


def part2():
    return len(unique_groups(read_input('input.txt')))


if __name__ == '__main__':
    print(part1())  # 306
    print(part2())  # 200
