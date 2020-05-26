n = int(input())

a = [-10**9 + 1] + list(map(int, input().split()))
b = [-10**9 + 1] + a[n:0:-1]
s = [0]*(n+1)
f = [0]*(n+1)
# print(b)
for i in range(1, n+1):
    m = 0
    k = 0
    for j in range(0, i):
        if a[i] > a[j]:
            m = max(m, s[j] + 1)
        if b[i] > b[j]:
            k = max(k, f[j] + 1)
    s[i] = m
    f[i] = k

print(s)
print(f)
res = 1
for i in range(1, n + 1):
    m = 0
    if s[i] > 1:
        for j in range(1, n - i + 1):
            if f[j] >= 1 and a[i] > a[n - j + 1]:
                m = max(m, s[i] + f[j])
        res = max(res, m)

print(res)