n = int(input())

a = [[0,0]]

for i in range(0, n):
    x, y = map(int, input().split())
    a.append([x,y])
# print(a)
a.sort(key = lambda x: x[0])
f = [0]*(n+1)

for i in range(1, n+1):
    m = 0
    for j in range(0, i):
        if a[j][1] < a[i][0]:
            m = max(m, f[j] + 1)
    f[i] = m

print(max(f))
