def func():
    pass

if __name__ == "__main__":
    n,c = map(int, input().split())

    arr = []

    for i in range(0,n):
        arr.append(tuple(map(int, input().split())))
    
    arr.sort(key = lambda x: x[0])

    res = 0
    for i,j in arr:
        if c >= i:
            res += 1
            c += j
        else:
            break
    
    print(res)