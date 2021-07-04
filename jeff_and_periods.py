#     _       _ _ _                     _           _     _
#    / \   __| (_) |_ _   _  __ _      | | ___  ___| |__ (_)
#   / _ \ / _` | | __| | | |/ _` |  _  | |/ _ \/ __| '_ \| |
#  / ___ \ (_| | | |_| |_| | (_| | | |_| | (_) \__ \ | | | |
# /_/   \_\__,_|_|\__|\__, |\__,_|  \___/ \___/|___/_| |_|_|
#                     |___/
# https://codeforces.com/problemset/problem/352/B
from collections import defaultdict
n = int(input())
l = list(map(int, input().split()))

d = defaultdict(list)
for i in range(n):
    d[l[i]].append(i)
# print(d)
z = []
for i in d:
    if len(d[i]) == 1:
        # print(i, 0)
        z.append([i, 0])
    else:
        common_diff = (max(d[i]) - min(d[i]))//(len(d[i])-1)
        fl = True
        for j in range(len(d[i])-1):
            if d[i][j + 1] - d[i][j] != common_diff:
                fl = False
                break
        if fl:
            # print(i, common_diff)
            z.append([i, common_diff])
print(len(z))
for i in sorted(z):
    print(*i)
