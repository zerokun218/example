n, m = map(int, input().split())

a = [[0,0]]
for i in range(n):
    a.append(list(map(int, input().split())))

a.sort(key = lambda x: x[1])

f = [0]*(m+1)
for i in range(1, n+1):
    for j in range(1, m+1):
        if j >= a[i][1]:
            f[j] = max(f[j], f[j-a[i][1]] + a[i][0])
print(max(f))