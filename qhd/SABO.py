if __name__ == "__main__":
    n,k = map(int, input().split())


    res = [0]*(n+k+1)
    res[0] = 1
    for i in range(1,k+1 +1):
        res[i] = res[i-1] + 1
        res[i] = res[i] % 10**6

    for i in range(k+2,n+1):
        res[i] = res[i-1] + res[i-k-1]
        res[i] = res[i] % 10**6

    print(res[n] % 10**6) 