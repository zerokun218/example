n = int(input())
MOD = 10**9 +7
f = [0]*(n+1)

f[0] = 1
f[-1] = 1
for i in range(1, n+1):
    f[i] = (f[i-1]*2 + f[i-2]) % MOD

print(f[n])