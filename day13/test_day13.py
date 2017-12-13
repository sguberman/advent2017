# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 15:44:47 2017

@author: Seth Guberman - sguberman@gmail.com
"""


import pytest
from itertools import count

from day13 import Firewall


def test_trip_severity():
    f = Firewall('test_input.txt')
    assert f.trip_severity() == 24


def test_packet_caught():
    for delay in count(0):
        f = Firewall('test_input.txt')
        if not f.packet_caught(delay):
            break
    assert delay == 10


if __name__ == '__main__':
    pytest.main(['-v'])
