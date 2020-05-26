n = int(input())
MOD = 10**9
a = [0] + list(map(int, input().split())) + [0]
f = [0]*(n+2)
f[0] = 1
for i in range(1, n + 1 + 1):
    if a[i] == 0:
        if a[i-3] == 1:
            f[i] = (f[i-1] + f[i-2]) % MOD
        else:
            f[i] = (f[i-1] + f[i-2] + f[i-3]) % MOD      
    elif a[i] == 1:
        f[i] = f[i-1] % MOD
print(f[n+1])