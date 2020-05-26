if __name__ == "__main__":
    k,n = map(int, input().split())

    a = [[0]*(n+1)]
    f = [[0]*(n+1)]
    for i in range(0, k):
        a.append([0] + list(map(int, input().split())))
        f.append([0]*(n+1))
    # for ii in a:
    #     print(ii)
    # for ii in f:
    #     print(ii)
    f[1][1] = a[1][1]
    for i in range(1, k +1):
        for j in range(i, n +1 ):
            f[i][j] = max(f[i][j-1], f[i-1][j-1] + a[i][j])
    
    # for i in f:
    #     print(i)

    print(f[k][n])
