n = int(input())

a = [-1] + list(map(int, input().split()))

f = [1]*(n+1)
s = [1]*(n+1)

res = 0
for i in range(n, 0, -1):
    m = 0
    k = 0
    for j in range(i, n+1):
        if a[i] < a[j]:
            m = max(m, f[j] + 1)
        if a[i] > a[j]:
            k = max(k, s[j] + 1)
    f[i] = max(m, f[i])
    s[i] = max(k, s[i])
# print(s)
# print(f)
for i in range(1, n+1):
    res = max(res, s[i] + f[i] -1)

print(res)