#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 18:26:25 2017

@author: Seth Guberman - sguberman@gmail.com
"""


import pytest

from day07 import part1, build_tree, find_root, stack_weight


def test_part1():
    assert part1() == 'mkxke'


def test_build_tree():
    weights, children, parents = build_tree('test_input.txt')
    assert len(weights) == 13
    assert weights['pbga'] == 66
    assert weights['fwft'] == 72
    assert children['fwft'] == ['ktlj', 'cntj', 'xhth']
    assert parents['ktlj'] == 'fwft'
    assert children['pbga'] == []


def test_find_root():
    weights, children, parents = build_tree('test_input.txt')
    assert find_root(children, parents) == 'tknk'


def test_stack_weight():
    w, c, p = build_tree('test_input.txt')
    assert stack_weight('ugml', w, c) == 251
    assert stack_weight('padx', w, c) == 243
    assert stack_weight('fwft', w, c) == 243


if __name__ == '__main__':
    pytest.main(['-v'])
