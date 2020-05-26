if __name__ == '__main__':
    n = int(input())

    a = ['']
    f = [0]
    for i in range(1,n +1):
        a.append('0' + input())
        f.append([0]*(len(a[i])))

    res = [-1]*(n+1)

    for i in range(1, n+1):
        for j in range(1, len(a[i])):
            if a[i][j] == 'A':
                f[i][j] = f[i][j-1] + 1
            if f[i][j] > 1:
                f[i][j] = 1
            if a[i][j] == 'B':
                f[i][j] = f[i][j-1] - 1
            if f[i][j] < -1:
                res[i] = 0
        if res[i] == -1:
            if f[i][len(a[i]) - 1] <= -1:
                res[i] = 0
            else:
                res[i] = 1
    # for i in f:
    #     print(i)
    
    for i in range(1, n+1):
        if res[i] == 1:
            print("YES")
        else:
            print("NO")
