#      *
#     * *
#    *   *
#   *  *  *  Author:Aditya Joshi
#  *       *
# *         *
# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
s = 'kkkk'
# s = 'abba'
# s = 'abcd'
# s = 'ifailuhkqq'
# s = 'cdcd'
l = list(s)
d = {}
ctr = 0
for i in range(len(l)):
    for j in range(i, len(l)):
        x = ''.join(sorted(l[i:j+1]))
        if x in d:
            d[x] += 1
        else:
            d[x] = 1

for i in d:
    x = d[i]
# easier way to perform nC2
    ctr += (x*(x-1))/2
print(int(ctr))
