if __name__ == "__main__":
    n,m = map(int, input().split())

    arr = [0]
    arr += list(map(int, input().split()))

    d = [0]*(n+1)
    d[0] = 1

    for i in range(1,m +1):
        for j in range(1,n +1):
            if j>= arr[i] and d[j - arr[i]] != 0: 
                d[j] += d[j - arr[i]]
    print(d[n])
