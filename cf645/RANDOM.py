import itertools
from random import randrange

a = [x for x in range(0, 11)]

f = [1]*(11)
t = 0
r = 0
while t <= 100:
    r = randrange(0,10)
    print(r)
    t+= 1
