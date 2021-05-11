#      *
#     * *
#    *   *
#   *  *  *  Author:Aditya Joshi
#  *       *
# *         *
# https://www.codechef.com/START3B/problems/HIRETEST
from collections import Counter
for _ in range(int(input())):
    l = []
    n, m = map(int, input().split())
    x, y = map(int, input().split())
    for i in range(n):
        temp = list(input())
        d = Counter(temp)
        if 'U' not in d:
            d['U'] = 0
        if 'F' not in d:
            d['F'] = 0
        if 'P' not in d:
            d['P'] = 0
        if d['F'] >= x or ((d['F'] == (x-1)) and (d['P'] >= y)):
            l.append('1')
        else:
            l.append('0')

    print(''.join(l))
