def func(x,y,k):
    global ok,m,n,final,res,temp
    s = 0
    s = arr[x][y]
    arr[x][y] = -1

    if k == n + m - 1:
        if x == n-1 and y == m-1 and len(temp) > 1:
            ok = True
            final = res[:]
            return
    
    if y + 1 <= m-1 and arr[x][y+1] >= 0:
        if arr[x][y+1] != 0:
                temp.add(arr[x][y+1])
        res[k] = [x+1,y+1+1]
        func(x,y+1,k+1)
    if x + 1 <= n-1 and arr[x+1][y] >= 0:
        if arr[x+1][y] != 0:
            temp.add(arr[x+1][y])
        res[k] = [x+1+1,y+1]
        func(x+1,y,k+1)      
        
    arr[x][y] = s
if __name__ == "__main__":
    n,m = map(int, input().split())
    ok = False
    temp = []
    temp = set(temp)
    arr = []
    for i in range(0,n):
        arr.append(list(map(int, input().split())))
    
    final = []
    res = [[0,0]]*(n+m-1)
    res[0] = [1,1]
    func(0,0,1)
    if ok == True and len(temp) > 1:
        for i,j in final:
            print(str(i) + ' ' + str(j))
    else:
        print(-1)