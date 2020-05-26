if __name__ == "__main__":
    n,m,k = map(int, input().split())
    
    arr = [0]
    for i in range(1,n+1):
        for j in range(1,m+1):
            arr.append(int(i*j))
    arr.sort()

    print(arr[k])