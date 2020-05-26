t = int(input())
for i in range(0, t):
    n = int(input())

    a = [0] + list(map(int, input().split()))
    f = [0]*(n+1)
    for j in range(1, n+1):
        f[j] = max(f[j-1], f[j-2] + a[j])
    print(f[n])