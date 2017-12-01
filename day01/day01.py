# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 08:58:50 2017

@author: Seth Guberman - sguberman@gmail.com
"""


def captcha(digits):
    neighbors = digits[-1] + digits[:-1]
    return sum(int(d) for d, n in zip(digits, neighbors) if d == n)


def half_captcha(digits):
    half = len(digits) // 2
    neighbors = digits[half:] + digits[:half]
    return sum(int(d) for d, n in zip(digits, neighbors) if d == n)


if __name__ == '__main__':
    with open('input.txt', 'r') as inp:
        number = inp.read().strip()
    print(captcha(number))  # part 1: 1182
    print(half_captcha(number))  # part 2: 1152
