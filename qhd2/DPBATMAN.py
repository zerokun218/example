t = int(input())
res = []
for x in range(0, t):
    n, m = map(int, input().split())
    a = [10**19] + list(map(int, input().split()))
    f = [1]*(n+1)
    for i in range(1, n+1):
        s = 0
        for j in range(1, i):
            if a[i] < a[j] or j == m:
                s = max(s, f[j] + 1)
        f[i] = max(s, f[i])
    res.append(max(f))

for i in res:
    print(i)