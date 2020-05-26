def func():
    pass

if __name__ == "__main__":
    n = int(input())
    m = int(input())

    arr = [0]*(n+1)

    for i in range(0,m):
        a,b = map(int, input().split())
        for j in range(a,b+1):
            arr[j] += 1
    q = int(input())

    res = []
    for i in range(1,q+1):
        x = int(input())
        a = 0
        for j in arr:
            if j >= x:
                a +=1
        res.append(a)

    for i in res:
        print(i)
