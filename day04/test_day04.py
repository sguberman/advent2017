import pytest

from day04 import part1, part2, no_repeats, no_anagrams


def test_part1():
    assert part1() == 455


def test_part2():
    assert part2() == 186


testdata = [('aa bb cc dd ee', True),
            ('aa bb cc dd aa', False),
            ('aa bb cc dd aaa', True)]


@pytest.mark.parametrize('phrase,expected', testdata)
def test_no_repeats(phrase, expected):
    assert no_repeats(phrase.split()) == expected


testdata = [('abcde fghij', True),
            ('abcde xyz ecdab', False),
            ('a ab abc abd abf abj', True),
            ('iiii oiii ooii oooi oooo', True),
            ('oiii ioii iioi iiio', False)]


@pytest.mark.parametrize('phrase,expected', testdata)
def test_no_anagrams(phrase, expected):
    assert no_anagrams(phrase.split()) == expected

if __name__ == '__main__':
    pytest.main(['-v'])
