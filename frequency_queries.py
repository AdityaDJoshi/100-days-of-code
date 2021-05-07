from collections import defaultdict


q = [(1, 1), (2, 2), (3, 2), (1, 1), (1, 1), (2, 1), (3, 2)]
q = [(3, 4), (2, 1003), (1, 16), (3, 1)]

n = int(input())

d = defaultdict(int)  # regular dictionary
e = defaultdict(int)  # dictionary of the values of the dictionary

# for i,j in q:
for tc in range(n):
    i, j = map(int, input().strip().split())

    if i == 1:
        # insert
        e[d[j]] -= 1
        d[j] += 1
        e[d[j]] += 1

    elif i == 2:
        if j in d:
            e[d[j]] -= 1
            d[j] -= 1
            e[d[j]] += 1

        d[j] = 0 if d[j] < 0 else d[j]

    else:
        print('1' if j in e and e[j] > 0 else '0')
