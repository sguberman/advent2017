def total_score(groups):
    score = 0
    level = 0
    garbage_count = 0
    canceled = False
    in_garbage = False
    for x in groups:
        if canceled:
            canceled = False
            continue
        elif in_garbage:
            if x == '!':
                canceled = True
            elif x == '>':
                in_garbage = False
            else:
                garbage_count += 1
        else:
            if x == '{':
                level += 1
                score += level
            elif x == '}':
                level -= 1
            elif x == '<':
                in_garbage = True
    return score, garbage_count


def read_input(filename):
    with open(filename) as f:
        return f.read().strip()


def solution():
    return total_score(read_input('input.txt'))


if __name__ == '__main__':
    print(solution())  # 9251, 4322
