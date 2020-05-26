n = int(input())

import math
from functools import reduce
from itertools import combinations

s = []
def lcm(i):
    for x in i:
        s.append((x[0]*x[1])//(math.gcd(x[1],x[0])))
    # return (x*y)//(math.gcd(x,y))
a = list(map(int, input().split()))

# x = list(combinations(a,2))


res = 1
# res = reduce(lcm, a)

lcm(list(combinations(a,2)))
res = reduce(math.gcd,s)
# print(s)
# print(x)
print(res)