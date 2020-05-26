n = int(input())

a = [0] + list(map(int, input().split()))
res = 0
for  k in range(1, 51):
    f = [1]*(n+1)
    for i in range(1, n+1):
        m = 0
        for j in range(1, i):
            if a[i] - a[j] == k:
                m = max(m, f[j] + 1)
        f[i] = max(m, f[i])
        res = max(res, f[i])

print(res)