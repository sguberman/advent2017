from itertools import filterfalse


def generator(start, multiply_by):
    """
    Lazily generate values as described by the challenge description.
    """
    value = start
    while True:
        value = (value * multiply_by) % 2147483647
        yield value


def last16(x):
    """
    Return the last 16 digits of x in binary as a string.
    """
    return '{:016b}'.format(x)[-16:]


def judge(a, b):
    """
    Compare the last 16 binary digits of a and b.
    """
    return last16(a) == last16(b)


def solution(part2=False):
    """
    Count the number of generator matches found by the judge
    after comparing limit generator pairs.
    """
    limit = 40000000
    genA, genB = generator(289, 16807), generator(629, 48271)

    if part2:
        limit = 5000000
        genA = filterfalse((lambda x: x % 4), genA)
        genB = filterfalse((lambda x: x % 8), genB)

    return sum(judge(a, b) for _, a, b in zip(range(limit), genA, genB))


if __name__ == '__main__':
    #print(solution())
    print(solution(part2=True))
