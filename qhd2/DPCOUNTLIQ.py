n = int(input())

MOD = 1000000007

a = [-10**10] + list(map(int, input().split()))

f = [1]*(n+1)
s = [0]*(n+1)
res = 0
for i in range(1, n+1):
    m = 0
    c = 0
    for j in range(1, i):
        if a[i] > a[j]:
            m = max(m, f[j] + 1)
    f[i] = max(m, f[i])
    for j in range(i-1, 0, -1):
        if a[i] > a[j] and f[j] == f[i] - 1:
            s[i] = (s[i] + max(s[j], 1)) % MOD
    res = max(res, f[i])
# print(f)
# print(s)
count = 0
for i in range(n, 0, -1):
    if f[i] == res:
        count = (count + s[i]) % MOD
print(count)
