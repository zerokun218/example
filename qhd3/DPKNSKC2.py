n, m = map(int, input().split())

a = [[0,0]]
for i in range(n):
    a.append(list(map(int, input().split())))
# a.sort(key = lambda x: x[0], reverse= True)
# a.sort(key = lambda x: x[1])
k = 0
f = [[0]*(m+1) for _ in range(0, n+1)]
t = [0]*(n+1)
res = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if j < a[i][1]:
            f[i][j] = f[i-1][j]
        else:
            f[i][j] = max(f[i-1][j], f[i][j-a[i][1]] + a[i][0])
            if res != max(res, f[i][j]):
                res = f[i][j]
                k = i
# for i in f:
#     print(i)
print(res)

while m != 0:
    if f[k][m] == res and f[k][m-1] == res:
        m -= 1
    else:
        for i in range(k, 0, -1):
            if f[i][m] == res:
                k = i
        t[k] += 1
        res -= a[k][0]
        m -= a[k][1]

for i in t[1:]:
    print(i, end=' ')

        