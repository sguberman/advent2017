from collections import Counter


def no_repeats(passphrase):
    c = Counter(passphrase)
    return all(count < 2 for count in c.values())


def count_valid_passphrases(filename, is_valid=no_repeats):
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            passphrase = line.strip().split()
            if is_valid(passphrase):
                count += 1
    return count


def part1():
    return count_valid_passphrases('input.txt')


def no_anagrams(passphrase):
    raise NotImplementedError


def part2():
    raise NotImplementedError


if __name__ == '__main__':
    print(part1())

