from collections import Counter


def no_repeats(passphrase):
    return all(count < 2 for count in Counter(passphrase).values())


def count_valid_passphrases(filename, is_valid=no_repeats):
    with open(filename, 'r') as f:
        return sum(is_valid(line.strip().split()) for line in f)


def part1():
    return count_valid_passphrases('input.txt')


def no_anagrams(passphrase):
    return all(Counter(a) != Counter(b)
               for i, a in enumerate(passphrase)
                   for b in passphrase[:i] + passphrase[i + 1:])


def part2():
    return count_valid_passphrases('input.txt', no_anagrams)


if __name__ == '__main__':
    print(part1())  # 455
    print(part2())  # 186
