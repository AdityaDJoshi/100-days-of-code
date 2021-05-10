#      *
#     * *
#    *   *
#   *  *  *  Author:Aditya Joshi
#  *       *
# *         *

from collections import defaultdict


def countTriplets(arr, r):

    d = defaultdict(int)
    e = defaultdict(int)
    ctr = 0

    for i in range(len(arr)):
        ctr += d[arr[i]]
        d[arr[i]*r] += e[arr[i]]
        e[arr[i]*r] += 1
    print(d, e)
    print(ctr)


if __name__ == "__main__":
    n, r = map(int, input().split())
    arr = list(map(int, input().split()))
    print(countTriplets(arr, r))
