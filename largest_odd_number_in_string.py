#     _       _ _ _                     _           _     _
#    / \   __| (_) |_ _   _  __ _      | | ___  ___| |__ (_)
#   / _ \ / _` | | __| | | |/ _` |  _  | |/ _ \/ __| '_ \| |
#  / ___ \ (_| | | |_| |_| | (_| | | |_| | (_) \__ \ | | | |
# /_/   \_\__,_|_|\__|\__, |\__,_|  \___/ \___/|___/_| |_|_|
#                     |___/
# https://leetcode.com/contest/weekly-contest-246/problems/largest-odd-number-in-string/
num = input()
ctr = 0
ind = -1
for i in range(len(num)):
    if int(num[i]) % 2 == 1:
        ctr += 1
        ind = i
if ctr == 0:
    print('\"\"')
else:
    print(num[:ind+1])
