t = int(input())

for i in range(0, t):
    
    n = int(input())

    a = [0] + list(map(int, input().split()))

    f = [0]*(n+1 + 3)
    f[n] = a[n]
    f[n-1] =  a[n] + a[n-1]
    f[n-2] = f[n-1] + a[n-2]
    for i in range(n-3, 0, -1):
        f[i] = max(f[i+2] + a[i], f[i+4] + a[i] + a[i+1], f[i+6] + a[i] + a[i+1] + a[i+2])

    print(f[1])
