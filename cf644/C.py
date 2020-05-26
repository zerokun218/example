t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    t = [0]*102
    m = 0
    k = 0
    for i in a:
        t[i] += 1
        if i % 2 == 0:
            k += 1
        else:
            m += 1
    check = 0
    if m % 2 == 0 or k % 2 == 0:
        print('YES')
        check = 1
    else:
        for i in a:
            if t[i-1] != 0 or t[i+1] != 0:
                print('YES')
                check = 1
                break
    if check == 0:
        print('NO')
# zero