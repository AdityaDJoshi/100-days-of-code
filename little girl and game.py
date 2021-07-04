#     _       _ _ _                     _           _     _
#    / \   __| (_) |_ _   _  __ _      | | ___  ___| |__ (_)
#   / _ \ / _` | | __| | | |/ _` |  _  | |/ _ \/ __| '_ \| |
#  / ___ \ (_| | | |_| |_| | (_| | | |_| | (_) \__ \ | | | |
# /_/   \_\__,_|_|\__|\__, |\__,_|  \___/ \___/|___/_| |_|_|
#                     |___/
# https://codeforces.com/problemset/problem/276/B
from collections import Counter
s = input()

d = Counter(s)
odd = []
for i in d:
    if d[i] % 2 == 1:
        odd.append(i)

if len(odd) == 0 or len(odd) == 1:
    print('First')
else:

    if (len(odd)-1) % 2 == 0:
        print('First')
    else:
        print('Second')
