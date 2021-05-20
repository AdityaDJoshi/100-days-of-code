#     _       _ _ _                     _           _     _
#    / \   __| (_) |_ _   _  __ _      | | ___  ___| |__ (_)
#   / _ \ / _` | | __| | | |/ _` |  _  | |/ _ \/ __| '_ \| |
#  / ___ \ (_| | | |_| |_| | (_| | | |_| | (_) \__ \ | | | |
# /_/   \_\__,_|_|\__|\__, |\__,_|  \___/ \___/|___/_| |_|_|
#                     |___/
# https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/filling-stones-078c792f/

# proof by examples, after n=3 mark there is always a way to get 'n' numbers out of 1...2n to give a zero total
# n=1
# [1][2] =2
# n=2
# [1,2][3,4]=1
# n=3
# [1,3,2][4,5,6]=0
# n=4
# [1,2,4,3][5,6,7,8]=0


n = int(input())
if n == 1:
    print(2)
elif n == 2:
    print(1)
else:
    print(0)
