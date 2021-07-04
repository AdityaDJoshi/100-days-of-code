#     _       _ _ _                     _           _     _
#    / \   __| (_) |_ _   _  __ _      | | ___  ___| |__ (_)
#   / _ \ / _` | | __| | | |/ _` |  _  | |/ _ \/ __| '_ \| |
#  / ___ \ (_| | | |_| |_| | (_| | | |_| | (_) \__ \ | | | |
# /_/   \_\__,_|_|\__|\__, |\__,_|  \___/ \___/|___/_| |_|_|
#                     |___/
# https://codeforces.com/problemset/problem/459/B
from collections import Counter

n = int(input())
l = list(map(int, input().split()))
maxdif = max(l)-min(l)
d = Counter(l)
ans = 0
if maxdif != 0:
    for i in sorted(d.keys()):
        # print(i, d[i], d[i + maxdif])
        ans += d[i] * d[i + maxdif]
else:
    # There has to be only one type of element as,
    # if there are any two different elements their absolute difference has to be greater than 0
    temp = d[l[0]]
    ans = ((temp*(temp-1))//2)
print(maxdif, ans)
