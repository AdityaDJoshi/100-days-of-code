#     _       _ _ _                     _           _     _
#    / \   __| (_) |_ _   _  __ _      | | ___  ___| |__ (_)
#   / _ \ / _` | | __| | | |/ _` |  _  | |/ _ \/ __| '_ \| |
#  / ___ \ (_| | | |_| |_| | (_| | | |_| | (_) \__ \ | | | |
# /_/   \_\__,_|_|\__|\__, |\__,_|  \___/ \___/|___/_| |_|_|
#                     |___/
# https://www.hackerrank.com/challenges/chocolate-feast/problem
for _ in range(int(input())):
    n, c, m = map(int, input().split())
    tot = int(n/c)
    curr = tot

    while curr >= m:
        wrappers = int(curr / m)
        tot = tot + wrappers
        curr = wrappers + (curr % m)

    print(tot)
