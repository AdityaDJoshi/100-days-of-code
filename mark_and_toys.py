#      *
#     * *
#    *   *
#   *  *  *  Author:Aditya Joshi
#  *       *
# *         *
# https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
n, k = map(int, input().split())
l = list(map(int, input().split()))
c = 0
l.sort()
for i in range(n):
    if (c+l[i]) > k:
        break
    c += l[i]
print(i)
