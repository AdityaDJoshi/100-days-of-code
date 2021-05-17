#     _       _ _ _                     _           _     _
#    / \   __| (_) |_ _   _  __ _      | | ___  ___| |__ (_)
#   / _ \ / _` | | __| | | |/ _` |  _  | |/ _ \/ __| '_ \| |
#  / ___ \ (_| | | |_| |_| | (_| | | |_| | (_) \__ \ | | | |
# /_/   \_\__,_|_|\__|\__, |\__,_|  \___/ \___/|___/_| |_|_|
#                     |___/
# https://www.hackerrank.com/challenges/luck-balance/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms
zeroes = []
ones = []
n, k = map(int, input().split())
for i in range(n):
    x, y = map(int, input().split())
    if y == 1:
        ones.append(x)
    else:
        zeroes.append(x)

ones.sort()
par = min(k, len(ones))
points = sum(zeroes)
points += sum(ones[(len(ones)-par):])
points -= sum(ones[:(len(ones)-par)])
print(points)
