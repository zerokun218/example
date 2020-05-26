def func(a,k,h):
    dic = {0:0, 1:0, 2:0, 3:0}
    arr = []
    arr.append(list(dic.values()))
    for i in a:
        dic[i] +=1
        arr.append(list(dic.values()))
    print(arr)

    print(str(arr[h][1]-arr[k-1][1]) + " " 
        + str(arr[h][2]-arr[k-1][2]) + " "
        + str(arr[h][3]-arr[k-1][3]))

if __name__ == "__main__":
    n,m=map(int, input().split())
    arr =[]
    for i in range(1,n+1):
        arr.append(int(input()))

    query = []
    for i in range(1,m+1):
        query.append(map(int, input().split()))

    for i,j in query:
        func(arr,i,j) 
