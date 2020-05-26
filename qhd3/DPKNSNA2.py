m, n = map(int, input().split())

a = [[0,0]]
for _ in range(n):
    a.append(list(map(int, input().split())))

f = [0]*(m+1)

for i in range(1, n+1):
    for j in range(a[i][1],m+1):
        f[j] = max(f[j], f[j-a[i][1]] + a[i][0])
print(max(f))