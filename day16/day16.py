from collections import deque
from itertools import count
from string import ascii_lowercase


class DancingPrograms:

    def __init__(self, programs, dance_moves=None, from_file=None):
        self.programs = deque(letter for letter in programs)
        self.dance_moves = dance_moves if dance_moves else []
        if from_file:
            with open(from_file) as f:
                self.dance_moves = f.read().strip().split(',')

        self.ops = {'s': self.spin,
                    'x': self.exchange,
                    'p': self.partner}

    def __str__(self):
        return ''.join(letter for letter in self.programs)

    def spin(self, x):
        self.programs.rotate(int(x))

    def exchange(self, i, j):
        i, j = int(i), int(j)
        a, b = self.programs[i], self.programs[j]
        self.programs[i] = b
        self.programs[j] = a

    def partner(self, a, b):
        i = self.programs.index(a)
        j = self.programs.index(b)
        self.exchange(i, j)

    def step(self, move):
        f, args = move[0], move[1:].split('/')
        self.ops[f](*args)

    def dance(self):
        for move in self.dance_moves:
            self.step(move)


def part1():
    d = DancingPrograms(ascii_lowercase[:16], from_file='input.txt')
    d.dance()
    return d


def part2():
    start = ascii_lowercase[:16]
    d = DancingPrograms(start, from_file='input.txt')
    
    for i in count(1):
        d.dance()
        if str(d) == start:
            cycle = i
            break
    
    times = 1000000000 % cycle
    d = DancingPrograms(start, from_file='input.txt')
    for _ in range(times):
        d.dance()
    return d


if __name__ == '__main__':
    print(part1())
    print(part2())
