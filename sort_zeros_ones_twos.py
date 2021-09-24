#     _       _ _ _                     _           _     _
#    / \   __| (_) |_ _   _  __ _      | | ___  ___| |__ (_)
#   / _ \ / _` | | __| | | |/ _` |  _  | |/ _ \/ __| '_ \| |
#  / ___ \ (_| | | |_| |_| | (_| | | |_| | (_) \__ \ | | | |
# /_/   \_\__,_|_|\__|\__, |\__,_|  \___/ \___/|___/_| |_|_|
#                     |___/
# https: // leetcode.com/problems/sort-colors/
# line 22 makes one of the biggest differences i have seen. To what i can understand fromt the given example is that it causes a movement of 2 (1 forward and 1 backward therefore skipping numbers in some cases)
# ..
def sort012(l, n):
    lo = 0
    it = 0
    hi = n-1
    while it <= hi:
        if(l[it] == 0):
            l[lo], l[it] = l[it], l[lo]
            lo += 1
            it += 1
        elif l[it] == 1:
            it += 1
        else:
            l[hi], l[it] = l[it], l[hi]
            hi -= 1
            # it += 1

    print(l)

    # return l
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
arr_size = len(arr)
sort012(arr, arr_size)
# print("Array after segregation :\n", arr)
