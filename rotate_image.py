#     _       _ _ _                     _           _     _
#    / \   __| (_) |_ _   _  __ _      | | ___  ___| |__ (_)
#   / _ \ / _` | | __| | | |/ _` |  _  | |/ _ \/ __| '_ \| |
#  / ___ \ (_| | | |_| |_| | (_| | | |_| | (_) \__ \ | | | |
# /_/   \_\__,_|_|\__|\__, |\__,_|  \___/ \___/|___/_| |_|_|
#                     |___/
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

for i in range(len(a)):
    for j in range(i+1):
        a[i][j], a[j][i] = a[j][i], a[i][j]


for i in range(len(a)):
    a[i] = a[i][::-1]

for i in a:
    print(i)