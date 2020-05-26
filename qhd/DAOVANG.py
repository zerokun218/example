if __name__ == "__main__":
    n,k = map(int, input().split())

    arr = [[0]*(n+1)]
    # print(arr)
    for i in range(1,n+1):
        arr.append([0] + (list(map(int,input().split()))))
    # print(arr)

    for i in range(1,n+1):
        for j in range(1,n+1):
            arr[i][j] += arr[i][j-1] + arr[i-1][j] - arr[i-1][j-1]

    # for i in arr:
    #     print(i)
    Max = arr[k][k]
    for i in range(k,n+1):
        for j in range(k,n+1):
            Max = max(Max,arr[i][j] - arr[i-k][j] - arr[i][j-k] + arr[i-k][j-k]) 
    
    print(Max)