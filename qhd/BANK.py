temp = 0
ans = 0
def func(n, h):
    if n == 0:
        return 0
    else:
        if a[n][1] >= h:
            return max(a[n][0] + func(n-1, h+1), func(n-1, h))
        else:
            return func(n-1,h)
    
if __name__ == "__main__":
    n = int(input())

    a= [[0,0]]
    for i in range(0,n):
        x,y = map(int, input().split())
        a.append([x,y])
    a.sort(key = lambda x: x[1])
    f = [[0]*(10)]
    for i in range(0,n):
        f.append([0]*(10))
    res = 0
    # print(func(n, 0))
    for i in range(1,n +1):
        for j in range(0, a[i][1] +1):
            f[i][j] = max(a[i][0] + f[i-1][j-1], f[i-1][j])
            res = max(res, f[i][j])
    for i in f:
        print(i)

    print(res)