#      *
#     * *
#    *   *
#   *  *  *  Author:Aditya Joshi
#  *       *
# *         *
# https://www.codechef.com/START3B/problems/TANDP
for _ in range(int(input())):
    n, m = map(int, input().split())
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    police_dist = max((n-a), (m-b))
    thief_dist = (n-x)+(m-y)
    # print(police_dist, thief_dist)
    if thief_dist <= police_dist:
        print("YES")
    else:
        print("NO")
