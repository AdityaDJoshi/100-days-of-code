#      *
#     * *
#    *   *
#   *  *  *  Author:Aditya Joshi
#  *       *
# *         *
# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search
for _ in range(int(input())):
    money = int(input())
    n = int(input())
    cost = list(map(int, input().split()))
    s = set(sorted(cost))
    d = {}
    for i in range(n):
        if cost[i] in d:
            d[cost[i]].append(i)
        else:
            d[cost[i]] = [i]
    for i in s:
        a = d[i][0]+1
        d[i] = d[i][1:]
        if money-i in d:
            if d[money-i]:
                b = d[money-i][0]+1
                print(min(a, b), max(a, b))
                break
