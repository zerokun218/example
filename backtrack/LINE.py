def func(y,x):
    global ok, dy, dx
    arr[y][x] = 1
    if y == dy-1 and x == dx-1:
        ok = True
        return
    if y - 1 >= 0 and arr[y-1][x] == 0:
        func(y-1,x)
    if y + 1 <= n-1 and arr[y+1][x] == 0:
        func(y+1,x)
    if x - 1 >= 0 and arr[y][x-1] == 0:
        func(y,x-1)
    if x + 1 <= n-1 and arr[y][x+1] == 0:
        func(y,x+1)

if __name__ == "__main__":
    n, sy, sx, dy, dx = map(int, input().split())
    ok = False
    arr = []
    for i in range(0,n):
        arr.append(list(map(int, input().split())))

    func(sy-1, sx-1)
    if ok == True:
        print("YES")
    else:
        print("NO")
