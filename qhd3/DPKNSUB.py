t = int(input())
for i in range(t):
    n = int(input())
    a = [0] + list(map(int, input().split()))

    s = sum(a)

    if s//2 != s/2:
        print('NO')
    else:
        f = [0]*(s//2 + 1)
        f[0] = 1
        for i in range(1, n+1):
            for j in range(s//2, a[i]-1, -1):
                if f[j-a[i]] == 1:
                    f[j] = 1
        if f[-1] == 1:
            print('YES') 
        else:
            print('NO')
