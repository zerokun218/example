import math

n = int(input())

a = [0] + list(map(int, input().split()))

f = [1]*(n+1)

for i in range(2, n+1):
    m = 0
    for j in range(1, i):
        if a[i] > a[j] and math.gcd(a[i], a[j]) == 1:
            m = max(m, f[j] + 1)
    f[i] = m

print(max(f))