def func():
    pass

if __name__ == "__main__":
    n = int(input())

    arr = []
    temp = []
    for i in range(0,n):
        a = tuple(map(int, input().split()))
        arr.append(a)
    
    arr.sort( key = lambda x: x[1], reverse=True )
    
    b = 1
    a = 0
    x = tuple()
    
    for i,j in arr[:]:      
        if (j > 0 and n > 0):
            x = arr.pop(0)
            b = b - 1 + x[1]
            a += x[0]
            n -= 1
        if (b == 0 or n == 0):
            break

    arr.sort(key = lambda x: x[0], reverse=True)
    k=0
    while (b > 0 and n > 0):
        a += arr[k][0]
        k += 1
        n -=1
        b -=1
    print(a)
        