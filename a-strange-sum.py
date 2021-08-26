#     _       _ _ _                     _           _     _
#    / \   __| (_) |_ _   _  __ _      | | ___  ___| |__ (_)
#   / _ \ / _` | | __| | | |/ _` |  _  | |/ _ \/ __| '_ \| |
#  / ___ \ (_| | | |_| |_| | (_| | | |_| | (_) \__ \ | | | |
# /_/   \_\__,_|_|\__|\__, |\__,_|  \___/ \___/|___/_| |_|_|
#                     |___/
from math import sqrt


def fac(n):
    l = []
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            if n//i == i:
                l.append(i)
            else:
                l.append(i)

                l.append(n//i)

    return sorted(l)


MOD = pow(10, 9)+7
for _ in range(int(input())):
    # n, m = map(int, input().split())
    m = 10
    for n in range(1, 100):
        s = 0
        for i in range(1, n+1):
            t1 = pow(i, m)
            # s = ((s % MOD) + ((t1 * len(fac(i))) % MOD) % MOD)
            s = s+(t1*len(fac(i)))
        print(n, s)
