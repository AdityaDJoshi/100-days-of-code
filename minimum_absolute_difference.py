#     _       _ _ _                     _           _     _
#    / \   __| (_) |_ _   _  __ _      | | ___  ___| |__ (_)
#   / _ \ / _` | | __| | | |/ _` |  _  | |/ _ \/ __| '_ \| |
#  / ___ \ (_| | | |_| |_| | (_| | | |_| | (_) \__ \ | | | |
# /_/   \_\__,_|_|\__|\__, |\__,_|  \___/ \___/|___/_| |_|_|
#                     |___/
# https://leetcode.com/problems/minimum-absolute-difference/

arr = [3, 8, -10, 23, 19, -4, -14, 27]
arr.sort()

min_diff = 2*(10**6)
for i in range(len(arr)-1):
    min_diff = min(min_diff, arr[i+1]-arr[i])
z = []
for i in range(len(arr)-1):
    if arr[i+1]-arr[i] == min_diff:
        z.append([arr[i], arr[i+1]])
print(z)
