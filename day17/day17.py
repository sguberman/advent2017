from collections import deque


s = deque([0])
for x in range(1, 2018):
    s.rotate(-337)
    s.append(x)

print(s[0])  # part1

s = deque([0])
for x in range(1, 50000001):
    s.rotate(-337)
    s.append(x)

print(s[0])  # part2
