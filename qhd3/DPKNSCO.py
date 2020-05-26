t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    a = [0] + list(map(int, input().split()))

    a.sort()

    # f = [[0]*(m+1) for _ in range(0, n+1)]

    # for i in range(0, m+1):
    #     f[0][i] = 10**10

    # for i in range(1, n+1):
    #     for j in range(1, m+1):
    #         if j < a[i]:
    #             f[i][j] = f[i-1][j]
    #         else:
    #             f[i][j] = min(f[i-1][j],f[i][j-a[i]] + 1)
    # for i in range(1, n+1):
    #     print(f[i][m], end=' ')
    # print()
    # print(f)
    # if f[n][m] == 10**10:
    #     print(-1)
    # else:
    #     print(f[n][m])

    f = [10**10]*(m+1)
    f[0] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if j >= a[i]:
                f[j] = min(f[j], f[j-a[i]] + 1)
    if f[m] == 10**10:
        print(-1)
    else:
        print(f[m])

