import pytest

from day10 import twist, hash, part1, input_to_ascii, sparse_to_dense, \
    dense_to_hex, knot_hash, part2


testdata = [
    (((0, 1, 2, 3, 4), 0, 0, 3), ((2, 1, 0, 3, 4), 3, 1)),
    (((2, 1, 0, 3, 4), 3, 1, 4), ((4, 3, 0, 1, 2), 3, 2)),
    (((4, 3, 0, 1, 2), 3, 2, 1), ((4, 3, 0, 1, 2), 1, 3)),
    (((4, 3, 0, 1, 2), 1, 3, 5), ((3, 4, 2, 1, 0), 4, 4))
]


@pytest.mark.parametrize('inp,exp', testdata)
def test_twist(inp, exp):
    lst1, pos1, skip1, length = inp
    lst2, pos2, skip2 = exp
    assert twist(lst1, pos1, skip1, length) == (lst2, pos2, skip2)


def test_hash():
    lst = (0, 1, 2, 3, 4)
    lengths = (3, 4, 1, 5)
    assert hash(lst, lengths)[0] == (3, 4, 2, 1, 0)


def test_part1():
    assert part1() == 1935


def test_input_to_ascii():
    assert input_to_ascii('1,2,3') == (49, 44, 50, 44, 51)


def test_sparse_to_dense():
    sparse = (65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22)
    assert sparse_to_dense(sparse) == (64,)


def test_dense_to_hex():
    dense = (64, 7, 255)
    assert dense_to_hex(dense) == '4007ff'


testdata = [
    ('', 'a2582a3a0e66e6e86e3812dcb672a272'),
    ('AoC 2017', '33efeb34ea91902bb2f59c9920caa6cd'),
    ('1,2,3', '3efbe78a8d82f29979031a4aa0b16a9d'),
    ('1,2,4', '63960835bcdc130f0b66d7ff4f6a5a8e')
]


@pytest.mark.parametrize('inp,exp', testdata)
def test_knot_hash(inp, exp):
    assert knot_hash(inp) == exp


def test_part2():
    assert part2() == 'dc7e7dee710d4c7201ce42713e6b8359'


if __name__ == '__main__':
    pytest.main(['-v'])
