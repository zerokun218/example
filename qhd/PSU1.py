if __name__ == "__main__":
    n,m = map(int, input().split())

    f = []
    for i in range(0,m +1):
        f.append([])
        for j in range(0,n +1):
            f[i].append(0)

    for i in range(1, n+1):
        f[1][i] = 1
    for i in range(2, m+1):
        for j in range(1, n+1):
            for k in range(j, n +1,j):
                f[i][k] = f[i][k] + f[i-1][j]
    
    s = 0
    for i in range(1, n +1):
        s += f[m][i]
    print(s)
    print(f)