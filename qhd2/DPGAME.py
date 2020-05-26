MOD = 25071987

n,k = map(int, input().split())

b = []
b += list(map(int, input().split()))
a = [0]*(n+1)
for i in b:
    a[i] = 1

f = [0]*(n+1)
f[1] = 1
for i in range(2, n+1):
    if a[i] == 0:
        f[i] = (f[i-1] + f[i-2]) % MOD
    else:
        f[i] = 0

print(f[n])
