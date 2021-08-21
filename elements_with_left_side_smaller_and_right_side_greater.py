#     _       _ _ _                     _           _     _
#    / \   __| (_) |_ _   _  __ _      | | ___  ___| |__ (_)
#   / _ \ / _` | | __| | | |/ _` |  _  | |/ _ \/ __| '_ \| |
#  / ___ \ (_| | | |_| |_| | (_| | | |_| | (_) \__ \ | | | |
# /_/   \_\__,_|_|\__|\__, |\__,_|  \___/ \___/|___/_| |_|_|
#                     |___/
# https://practice.geeksforgeeks.org/problems/unsorted-array/0
mins = []
maxs = []
mi = arr[0]
ma = arr[-1]
for i in range(1, n - 1):
    mi = min(arr[i - 1], mi)
    mins.append(mi)
for i in range(n - 2, 0, -1):
    ma = max(ma, arr[i - 1])
    maxs.append(ma)
# print(mins)
# print(maxs)
temp = arr[1:n]
fl = True
for i in range(len(mins)):
    if temp[i] >= mins[i] and temp[i] <= maxs[i]:
        print(temp[i])
        fl = False
        break
if fl:
    print(-1)
# n = 4
# l = [4, 2, 5, 7]
# n = 3
# arr = [11, 9, 12]

# 14
# 5 6 4 1 7 12 9 1 4 1 11 5 7 1
