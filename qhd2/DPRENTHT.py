n = int(input())

a = [[0,0]]
for i in range(0, n):
    a.append(list(map(int, input().split())))

a.sort(key = lambda x : x[0])

f = [0]*(n+1)

for i in range(1, n+1):
    m = 0
    f[i] = a[i][1] - a[i][0] + 1
    for j in range(1, i):
        if a[i][0] > a[j][1]:
            m = max(m, f[j] + a[i][1] - a[i][0] + 1)
    f[i] = max(m, f[i])

print(max(f))
