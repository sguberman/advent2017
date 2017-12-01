# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 08:58:50 2017

@author: Seth Guberman - sguberman@gmail.com
"""


def captcha(number):
    raise NotImplementedError


if __name__ == '__main__':
    with open('input.txt', 'r') as inp:
        number = inp.read().strip()
    print(captcha(number))
