if __name__ == "__main__":
    m, n = map(int, input().split())

    a = [[0]*(n+1)]

    for i in range(0,m):
        a.append([0] + list(map(int, input().split())))
    
    f = [[0]*(n+1)]
    for i in range(0,m):
        f.append([0]*(n+1))
    
    g = [[0]*(n+1)]
    for i in range(0,m):
        g.append([0]*(n+1))
    
    f[0][1] = 1
    g[0][1] = 1
    if n > 1:
        g[1][2] = 1
    if m > 1:
        g[2][1] = 1
    for i in range(1, m +1):
        for j in range(1, n +1):
            if a[i][j] != -1:
                f[i][j] = (f[i-1][j] + f[i][j-1]) % 10**7
                if a[i][j] == a[i-1][j] or a[i][j] == 0:
                    g[i][j] += g[i-1][j] % 10**7
                if a[i][j] == a[i][j-1] or a[i][j] == 0:
                    g[i][j] += g[i][j-1] % 10**7
    # for i in f:
    #     print(i)
    # for i in g:
    #     print(i)
    print((f[m][n] - g[m][n]) % 10**7)




    