#     _       _ _ _                     _           _     _
#    / \   __| (_) |_ _   _  __ _      | | ___  ___| |__ (_)
#   / _ \ / _` | | __| | | |/ _` |  _  | |/ _ \/ __| '_ \| |
#  / ___ \ (_| | | |_| |_| | (_| | | |_| | (_) \__ \ | | | |
# /_/   \_\__,_|_|\__|\__, |\__,_|  \___/ \___/|___/_| |_|_|
#                     |___/
from math import ceil
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = [a[0]]
    for i in range(1, len(a)):
        if a[i] == 1:
            b.append(b[-1])
        else:
            b.append(ceil(b[-1] / a[i]) * a[i])
    print(b)
