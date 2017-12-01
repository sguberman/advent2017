# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 08:58:50 2017

@author: Seth Guberman - sguberman@gmail.com
"""


def captcha(digits):
    neighbors = digits[-1] + digits[:-1]
    return sum(int(d) for d, n in zip(digits, neighbors) if d == n)


if __name__ == '__main__':
    with open('input.txt', 'r') as inp:
        number = inp.read().strip()
    print(captcha(number))
