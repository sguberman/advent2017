import pytest

from day09 import total_score, solution


testdata = [
    ('{}', 1),
    ('{{{}}}', 6),
    ('{{},{}}', 5),
    ('{{{},{},{{}}}}', 16),
    ('{<a>,<a>,<a>,<a>}', 1),
    ('{{<ab>},{<ab>},{<ab>},{<ab>}}', 9),
    ('{{<!!>},{<!!>},{<!!>},{<!!>}}', 9),
    ('{{<a!>},{<a!>},{<a!>},{<ab>}}', 3),
]


@pytest.mark.parametrize('groups,expected', testdata)
def test_total_score(groups, expected):
    assert total_score(groups)[0] == expected


def test_solution():
    assert solution() == (9251, 4322)


if __name__ == '__main__':
    pytest.main(['-v'])
