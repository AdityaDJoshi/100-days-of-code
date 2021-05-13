#      *
#     * *
#    *   *
#   *  *  *  Author:Aditya Joshi
#  *       *
# *         *
n = int(input())
k = int(input())-1
l = []
for i in range(n):
    l.append(int(input()))
l.sort()
mis = 10**10
# print(l)
# print("pairs:")
for i in range(n-k):
    mis = min(mis, l[i+k]-l[i])
    # print(l[i+k], l[i])
# print(mis)
print("ans is %d" % mis)
