def func(x,y):
    global ok, dx, dy,res,final
    arr[x][y] = 1
    res.append([x+1,y+1])

    if x == dx-1 and y == dy-1:
        ok = True
        final = res[:]
    else:
        if x - 1 >= 0 and arr[x-1][y] == 0:
            func(x-1,y)
        if x + 1 <= n-1 and arr[x+1][y] == 0:
            func(x+1,y)
        if y - 1 >= 0 and arr[x][y-1] == 0:
            func(x,y-1)
        if y + 1 <= n-1 and arr[x][y+1] == 0:
            func(x,y+1)

        arr[x][y] = 0
        res.pop()
if __name__ == "__main__":
    n, sx, sy, dx, dy =map(int, input().split())
    ok = False
    res = []
    arr = []
    final = []
    for i in range(0,n):
        arr.append(list(map(int, input().split())))

    func(sx-1,sy-1)
    if ok == True:
        print(len(final))
        for i,j in final:
            print(str(i) + ' ' + str(j))
    else:
        print(0)