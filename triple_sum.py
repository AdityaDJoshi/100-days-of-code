# https://www.hackerrank.com/challenges/triple-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search
from bisect import bisect_left, bisect_right

la, lb, lc = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a = sorted(list(set(a)))
b = sorted(list(set(b)))
c = sorted(list(set(c)))
ctr = 0

for i in b:
    t1 = bisect_right(a, i)
    t2 = bisect_right(c, i)
    t3 = bisect_left(a, i)
    t4 = bisect_left(c, i)
    ctr += (max(t1, t3)*max(t2, t4))
# the max of these has to be taken as the built-in functions bisect_left
# and bisect_right both do not account for equality cases
print(ctr)
