from collections import deque
from functools import reduce
from itertools import islice
from operator import xor


def twist(lst, pos, skip, length):
    d1 = deque(lst)
    d1.rotate(-pos)  # lst[pos] now at index 0
    to_reverse = deque(islice(d1, length))  # d1[:length]
    leftover = deque(islice(d1, length, None))  # d1[length:]
    to_reverse.reverse()
    d2 = to_reverse + leftover
    d2.rotate(pos)  # lst[pos] now back at index pos
    pos = (pos + length + skip) % len(lst)  # wraps around
    skip += 1
    return tuple(d2), pos, skip


def hash(lst, lengths, pos=0, skip=0):
    for length in lengths:
        lst, pos, skip = twist(lst, pos, skip, length)
    return lst, pos, skip


def part1():
    lst = tuple(range(256))
    with open('input.txt') as f:
        lengths = [int(x) for x in f.read().strip().split(',')]
    lst, *_ = hash(lst, lengths)
    return lst[0] * lst[1]


def input_to_ascii(inp):
    return tuple(ord(x) for x in inp)


def sparse_to_dense(sparse, n=16):
    chunks = (sparse[i:i+n] for i in range(0, len(sparse), n))
    return tuple(reduce(xor, chunk) for chunk in chunks)


def dense_to_hex(dense):
    return ''.join('{:02x}'.format(x) for x in dense)


def multihash(lst, lengths, rounds=64):
    pos = 0
    skip = 0
    for round in range(rounds):
        lst, pos, skip = hash(lst, lengths, pos, skip)
    return lst


def knot_hash(inp):
    lst = tuple(range(256))
    lengths = input_to_ascii(inp) + (17, 31, 73, 47, 23)
    sparse = multihash(lst, lengths)
    dense = sparse_to_dense(sparse)
    hexstr = dense_to_hex(dense)
    return hexstr


def part2():
    with open('input.txt') as f:
        inp = f.read().strip()
    return knot_hash(inp)


if __name__ == '__main__':
    print(part1())  # 1935
    print(part2())  # dc7e7dee710d4c7201ce42713e6b8359
