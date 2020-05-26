n = int(input())

a = [[0,0]]
for i in range(0, n):
    a.append(list(map(int, input().split())))

a.sort(key = lambda x : x[1], reverse = True)
a.sort(key = lambda x : x[0])
# print(a)
f = [1]*(n+1)
for i in range(1, n+1):
    m = 0
    for j in range(0, i):
        if a[i][1] <= a[j][1] :
            m = max(m, f[j] + 1)
    f[i] = max(m,f[i])

print(max(f))