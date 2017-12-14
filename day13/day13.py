# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 14:32:34 2017

@author: Seth Guberman - sguberman@gmail.com
"""

from collections import defaultdict
from itertools import count


class EmptyLayer:

    def update(self):
        pass

    def severity(self):
        return 0

    def scanner_location(self):
        return -1


class Layer:

    def __init__(self, depth, range):
        self.depth = depth
        self.range = range
        self.scanner_at = 0
        self.scanner_dir = 1

    def update(self):
        if self.scanner_at == 0:
            self.scanner_dir = 1
        elif self.scanner_at == self.range - 1:
            self.scanner_dir = -1
        self.scanner_at += self.scanner_dir

    def severity(self):
        if self.scanner_at == 0:
            return self.depth * self.range
        else:
            return 0

    def scanner_location(self):
        return self.scanner_at

    def clear_at_time(self, time):
        return not (time % (2 * (self.range - 1)) == 0)


class Firewall:

    def __init__(self, filename):
        self.layers = defaultdict(EmptyLayer)
        self.time = 0
        self.packet_at = -1

        with open(filename) as f:
            for line in f:
                lhs, rhs = line.strip().split(': ')
                self.layers[int(lhs)] = Layer(int(lhs), int(rhs))

        self.exit_layer = max(depth for depth in self.layers) + 1

    def update_layers(self):
        for depth in self.layers:
            self.layers[depth].update()
        self.time += 1

    def advance_packet(self):
        self.packet_at += 1

    def trip_severity(self, delay=0):
        total_severity = 0
        while self.time < delay:
            self.update_layers()
        while self.packet_at < self.exit_layer:
            self.advance_packet()
            total_severity += self.layers[self.packet_at].severity()
            self.update_layers()
        return total_severity

    def packet_caught(self, delay=0):
        for layer in self.layers:
            time = delay + layer
            if not self.layers[layer].clear_at_time(time):
                return True
        return False


def part1():
    f = Firewall('input.txt')
    return f.trip_severity()


def part2():
    f = Firewall('input.txt')
    for delay in count(0):
        if not f.packet_caught(delay):
            return delay


if __name__ == '__main__':
    print(part1())  # 1476
    print(part2())  # 3937334
