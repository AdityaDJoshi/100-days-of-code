#      *
#     * *
#    *   *
#   *  *  *  Author:Aditya Joshi
#  *       *
# *         *
# https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
arr = [2, 3, 4, 1, 5]
# arr = [1, 3, 5, 2, 4, 6, 7]
# arr = [4, 3, 1, 2]

swaps = 0
d = {}

for i, in range(len(arr)):
    d[arr[i]] = i

for i in range(len(arr)):

    if arr[i] != i+1:
        swaps += 1
        t = arr[i]
        arr[i], arr[d[i+1]] = i+1, arr[i]
        d[t] = d[i+1]
# print(d, swaps)
