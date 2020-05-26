n,k = map(int, input().split())

a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))

f = [0]*(n+1)

for i in range(1, n+1):
    m = 0
    f[i] = b[i]
    for j in range(0, i):
        if a[i] - a[j] >= k:
            m = max(m, f[j] + b[i])
    f[i] = max(m, f[i])

print(max(f))