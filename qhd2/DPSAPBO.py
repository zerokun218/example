n, k = map(int, input().split())

f = [0]*(n+1)

for i in range(1, n + 1):
    if i <= k + 1:
        f[i] = i + 1
    else:
        f[i] = (f[i-1] + f[i-k-1]) %  10**6 
# print(f)
print(f[n])