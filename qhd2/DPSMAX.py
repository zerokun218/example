n = int(input())
a = [0] + list(map(int, input().split()))

f = [0]*(n+1)
res = 0

for i in range(1, n+1):
    m = 0
    for j in range(0, i):
        if a[j] <= a[i]:
            m = max(m, f[j] + a[i])

    f[i] = m
    res = max(res, f[i])

print(res)