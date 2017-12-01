# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 08:58:50 2017

@author: Seth Guberman - sguberman@gmail.com
"""


def captcha(digits, offset=1):
    neighbors = digits[offset:] + digits[:offset]
    return sum(int(d) for d, n in zip(digits, neighbors) if d == n)


def half_captcha(digits):
    half = len(digits) // 2
    return captcha(digits, offset=half)


if __name__ == '__main__':
    with open('input.txt', 'r') as inp:
        number = inp.read().strip()
    print(captcha(number))  # part 1: 1182
    print(half_captcha(number))  # part 2: 1152
