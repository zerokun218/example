n = int(input())

a = [0] + list(map(int, input().split()))

b = [0]*(10**5 + 2)
m = 0
for i in range(1, n+1):
    b[a[i]] += 1
    m = max(m, a[i])
# print(b)
f = [0]*(m+1)
for i in range(1, m + 1 ):
    f[i] = max(f[i - 1], f[i - 2] + i*b[i])

print(f[m])

# 1 6 6 9 10 10 7