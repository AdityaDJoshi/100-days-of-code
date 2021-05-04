#      *
#     * *
#    *   *
#   *  *  *  Author:Aditya Joshi
#  *       *
# *         *
# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
q=[2,1,5,3,4]
q = [2, 5, 1, 3, 4]
q=[1, 2, 5, 3, 7, 8, 6, 4]

fl=False
ctr=0
for i in range(len(q)):
    if q[i]-(i+1)>2:
        fl=True
    for j in range(max(0,(q[i]-2)),i):
        if(q[j]>q[i]):
            ctr+=1
if fl:
    print("Too chaotic")
else:
    print(ctr)