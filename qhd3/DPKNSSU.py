n, m, k = map(int, input().split())

a = [0] + list(map(int, input().split()))

f = [0]*(m+1)
f[0] = 1

for i in range(1, n+1):
    for j in range(m, a[i]-1, -1):
        f[j] += f[j-a[i]]
        if f[j] > 100:
            f[j] = 105
if f[m] >= k:
    print('ENOUGH')
else:
    print(f[m])