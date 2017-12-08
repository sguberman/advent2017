# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 13:48:05 2017

@author: Seth Guberman - sguberman@gmail.com
"""


import operator
from collections import defaultdict


registers = defaultdict(int)
ops = {'>': operator.gt,
       '<': operator.lt,
       '>=': operator.ge,
       '<=': operator.le,
       '==': operator.eq,
       '!=': operator.ne,
       'inc': operator.add,
       'dec': operator.sub}


def parse(line):
    reg1, op1, amt1, _, reg2, op2, amt2 = line.strip().split()
    instruction = (reg1, op1, int(amt1))
    condition = (reg2, op2, int(amt2))
    return instruction, condition


def evaluate(condition):
    register, operator, amount = condition
    return ops[operator](registers[register], amount)


def execute(instruction):
    register, operator, amount = instruction
    registers[register] = ops[operator](registers[register], amount)


def process(filename):
    highest = 0

    with open(filename) as instructions:
        for line in instructions:
            instruction, condition = parse(line)
            if evaluate(condition):
                execute(instruction)
                current_max = max(registers.values())
                highest = current_max if current_max > highest else highest

    return current_max, highest


if __name__ == '__main__':
    print(process('input.txt'))
