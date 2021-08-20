#     _       _ _ _                     _           _     _
#    / \   __| (_) |_ _   _  __ _      | | ___  ___| |__ (_)
#   / _ \ / _` | | __| | | |/ _` |  _  | |/ _ \/ __| '_ \| |
#  / ___ \ (_| | | |_| |_| | (_| | | |_| | (_) \__ \ | | | |
# /_/   \_\__,_|_|\__|\__, |\__,_|  \___/ \___/|___/_| |_|_|
#                     |___/
# https://practice.geeksforgeeks.org/problems/-rearrange-array-alternately-1587115620/1#
n = 6
arr = [1, 2, 3, 4, 5, 6]
n = 11
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
final = []
curr = 0
while True:
    if arr[-curr-1] == -1:
        break
    else:
        final.append(arr[-curr - 1])
        arr[-curr - 1] = -1

    if arr[curr] == -1:
        break
    else:
        final.append(arr[curr])
        arr[curr] = -1
    curr += 1
print(final)
