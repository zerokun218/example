if __name__ == "__main__":
    n,m = map(int, input().split())

    a = [0]
    b = [0]

    for i in range(0, n):
        x,y = (map(int, input().split()))
        a.append(x)
        b.append(y)
    f = []
    for i in range(0, n+1):
        f.append([0]*(m+1))
    for i in range(1, n +1):
        for j in range(1, m+1):
            f[i][j] = f[i-1][j]
            
            if j >= a[i]:
                f[i][j] = max(f[i-1][j-a[i]] + b[i], f[i][j])
    print(f[n][m])
    while n > 0:
        if f[n][m] != f[n-1][m]:
            print(n, end = ' ' )
            m = m - a[n]
        n -=1
    


