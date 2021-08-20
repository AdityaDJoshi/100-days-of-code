#     _       _ _ _                     _           _     _
#    / \   __| (_) |_ _   _  __ _      | | ___  ___| |__ (_)
#   / _ \ / _` | | __| | | |/ _` |  _  | |/ _ \/ __| '_ \| |
#  / ___ \ (_| | | |_| |_| | (_| | | |_| | (_) \__ \ | | | |
# /_/   \_\__,_|_|\__|\__, |\__,_|  \___/ \___/|___/_| |_|_|
#                     |___/
# https://leetcode.com/problems/product-of-array-except-self/
nums = [-1, 1, 0, -3, 3]
l = [1]
r = [1]
n = len(nums)
revnum = nums[::-1]
for i in range(1, n):
    l.append(l[-1] * nums[i - 1])
# print(l)
for i in range(1, n):
    r.append(r[-1] * revnum[i - 1])
# print(r[::-1])
r = r[::-1]
ans = []
for i in range(n):
    ans.append(l[i] * r[i])
print(ans)
