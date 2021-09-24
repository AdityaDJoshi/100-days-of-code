#     _       _ _ _                     _           _     _
#    / \   __| (_) |_ _   _  __ _      | | ___  ___| |__ (_)
#   / _ \ / _` | | __| | | |/ _` |  _  | |/ _ \/ __| '_ \| |
#  / ___ \ (_| | | |_| |_| | (_| | | |_| | (_) \__ \ | | | |
# /_/   \_\__,_|_|\__|\__, |\__,_|  \___/ \___/|___/_| |_|_|
#                     |___/
import bisect


def twoSum(numbers, target):
    d = {}
    ans = []
    for i in set(numbers):
        d[i] = []
    for i in range(len(numbers)):
        d[numbers[i]].append(i)

    for i in range(len(numbers)):
        if numbers[bisect.bisect_left(numbers[i+1:], target-numbers[i])] == target-numbers[i]:
            return [i, bisect.bisect_left(numbers[i+1:], target-numbers[i])]


print(twoSum([0, 0, 3, 4], 0))
print(twoSum([2, 7, 11, 15], 9))
z = [2, 7, 11, 15]
l = bisect.bisect(z, 8)
print(l, z[l])
