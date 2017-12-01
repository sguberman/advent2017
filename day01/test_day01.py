# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 08:59:47 2017

@author: Seth Guberman - sguberman@gmail.com
"""


import pytest

from day01 import captcha, half_captcha


def test_captcha():
    assert captcha('1122') == 3
    assert captcha('1111') == 4
    assert captcha('1234') == 0
    assert captcha('91212129') == 9


def test_half_captcha():
    assert half_captcha('1212') == 6
    assert half_captcha('1221') == 0
    assert half_captcha('123425') == 4
    assert half_captcha('123123') == 12
    assert half_captcha('12131415') == 4


if __name__ == '__main__':
    pytest.main()
