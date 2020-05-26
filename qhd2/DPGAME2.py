n,k = map(int, input().split())

a = [0]
a += list(map(int, input().split()))

f = [0]*(n+1)

res = -10**9 - 1
for i in range(1, n+1):
    m = -10**9 - 1
    for j in range(1, k+1):
        m = max(m, f[i-j])
    f[i] = m + a[i]
    res = max(res, f[i])

# print(f)
print(res)

####### LIMITED #######

    