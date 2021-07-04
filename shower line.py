#     _       _ _ _                     _           _     _
#    / \   __| (_) |_ _   _  __ _      | | ___  ___| |__ (_)
#   / _ \ / _` | | __| | | |/ _` |  _  | |/ _ \/ __| '_ \| |
#  / ___ \ (_| | | |_| |_| | (_| | | |_| | (_) \__ \ | | | |
# /_/   \_\__,_|_|\__|\__, |\__,_|  \___/ \___/|___/_| |_|_|
#                     |___/
# https://codeforces.com/problemset/problem/431/B
from itertools import permutations
gmatrix = []
for i in range(5):
    z = list(map(int, input().split()))
    gmatrix.append(z)
l = list(permutations([0, 1, 2, 3, 4], 5))
max_happiness = -1
for i in l:
    # hard coding the formula given in the problem
    happiness = gmatrix[i[0]][i[1]]+gmatrix[i[1]][i[0]] + (2 * gmatrix[i[2]][i[3]]) + (
        2 * gmatrix[i[3]][i[2]]) + gmatrix[i[1]][i[2]] + gmatrix[i[2]][i[1]] + (2 * gmatrix[i[3]][i[4]]) + (2 * gmatrix[i[4]][i[3]])
    max_happiness = max(max_happiness, happiness)
print(max_happiness)


# 2-0
# 3-1
# 1-2
# 5-3
# 4-4..
