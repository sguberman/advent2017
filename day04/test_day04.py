import pytest

from day04 import part1, part2

def test_part1():
    assert part1() == 455


def test_part2():
    assert part2() == 186


if __name__ == '__main__':
    pytest.main()
