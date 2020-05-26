
if __name__ == "__main__":
    n,k = map(int, input().split())

    arr = [0]*(n+1)

    for i in range(0,k):
        x = (int(input()))
        arr[x] = 1

    count = 0
    m = 0
    f = [0]*(n+1)
    for i in range(1,n +1):
        if arr[i] == 1:
            count += 1
            f[i] = count
        else:
            count = 0
    # print(f)
    if arr[0] == 1:
        p = f[n]
        for i in range(n-1,0,-1):
            if f[i] != 0 and p != 0:
                f[i] = p
            else:
                p = f[i]

        for i in range(1, n+1):
            if f[i] == 0:
                m = max(m, 1 + f[i-1] + f[i+1])
        print(m)
    else:
        print(max(f))
    
    # print(f)
