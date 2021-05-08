#      *
#     * *
#    *   *
#   *  *  *  Author:Aditya Joshi
#  *       *
# *         *
# https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
def checkMagazine(magazine, note):
    Mag = {}
    Note = {}
    f = True
    for i in set(magazine).union(set(note)):
        Mag[i] = 0
        Note[i] = 0
    for i in magazine:
        Mag[i] += 1
    for i in note:
        Note[i] += 1
    for i in Note:
        if Mag[i] < Note[i]:
            f = False
            break

    print("Yes" if f else "No")


mag = "two times three is not four".split()
note = "two times two is four".split()
checkMagazine(mag, note)
