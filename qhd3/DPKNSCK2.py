n, m = map(int, input().split())

a = [[0,0]]
for i in range(1, n+1):
    a.append(list(map(int, input().split())) + [i])
a.sort(key = lambda x: x[0], reverse = True)
a.sort(key = lambda x: x[1])
k = 0
res = 0
f = [[0]*(m+1) for _ in range(0, n+1)]
for i in range(1, n+1):
    for j in range(m, a[i][1]-1, -1):
        f[i][j] = max(f[i-1][j], f[i-1][j-a[i][1]] + a[i][0])
        if res != max(res, f[i][j]):
            res = f[i][j]
            k = i

# print(res)
# for i in f:
#     print(i)
ans = []
while m != 0:
    if f[k][m] == res and f[k][m-1] == res:
        m -= 1
    else:
        for i in range(k, 0, -1):
            if f[i][m] == res:
                k = i
        ans.append(str(a[k][2]))
        res -= a[k][0]
        m -= a[k][1]
        k -= 1
print(len(ans))
print(' '.join(ans[::-1]))
        