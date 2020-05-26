t = int(input())
ans = []
for _ in range(t):
    n, k = map(int, input().split())
    a = [0] + list(map(int, input().split()))

    f = [[0]*(k+1) for x in range(0, n+1)]
    res = 0
    for i in range(1, n+1):
        for j in range(k, 0, -1):
            if j < a[i]:
                f[i][j] = f[i-1][j]
            else:
                f[i][j] = max(f[i-1][j], f[i-2][j-a[i]] + a[i])
            res = max(res, f[i][j])
    ans.append(str(res))

print(' '.join(ans))