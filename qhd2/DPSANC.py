t = int(input())
res = []
for i in range(0, t):
    n = int(input())
    a = [[0,0,0]]
    for j in range(0,n):
        x,y,z = (list(map(int, input().split())))
        a.append([x,x+y,z])
    a.sort(key = lambda x: x[0])
    
    # print(a)
    f = [0]*(n+1)
    ans = 0
    for j in range(1, n+1):
        m = 0
        for k in range(0, j):
            if a[j][0] >= a[k][1]:
                m = max(m, f[k] + a[j][2])
        f[j] = m
        ans = max(ans, m)
    # print(f)
    res.append(ans)

for i in res:
    print(i)
