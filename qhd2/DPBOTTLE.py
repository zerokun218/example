n = int(input())

a = [0]

a += list(map(int, input().split()))

f = [0]*(n+1)
t = [0]*(n+1)
for i in range(1, n+1):
    f[i] = max(f[i-1],max(f[i-2] + a[i], f[i-3] + a[i-1] + a[i]))
    if f[i-2] + a[i] >= f[i-3] + a[i-1] +a[i]:
        t[i] = t[i-2] + 1
    else:
        t[i] = t[i-3] + 2
    if f[i] == f[i-1]:
        t[i] = min(t[i],t[i - 1])

i = n
while(i >= 1):
    if f[i - 1] == f[n]:
        i -= 1
    else:
        break
print(t[i], end= ' ')
print(f[n])