t = int(input())
for _ in range(t):
    n, x = map(int, input().split())

    a = list(map(int, input().split()))

    o = 0
    e = 0
    for i in a:
        if i % 2 == 1:
            o += 1
        else:
            e += 1

    if o % 2 == 0 and o > 0:
        o -= 1
    if x % 2 == 0 and e > 0:
        x -= 1
        e -= 1
    
    if x <= o:
        print('YES')
        continue
    elif x > o:
        x -= o
        if x <= e and o > 0:
            print('YES')
            continue
    
    print('NO')

    
