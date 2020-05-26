n, m = map(int, input().split())
a = [[0,0]]
for i in range(n):
    a.append(list(map(int, input().split())))

f = [0]*(m+1)
f[0] = 0

for i in range(1, n+1):
    for j in range(m, a[i][1]-1, -1):
        f[j] = max(f[j-a[i][1]] + a[i][0], f[j])
print(max(f))