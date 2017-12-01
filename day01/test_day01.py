# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 08:59:47 2017

@author: Seth Guberman - sguberman@gmail.com
"""


import pytest

from day01 import captcha


def test_captcha():
    assert captcha('1122') == 3
    assert captcha('1111') == 4
    assert captcha('1234') == 0
    assert captcha('91212129') == 9


if __name__ == '__main__':
    pytest.main()
