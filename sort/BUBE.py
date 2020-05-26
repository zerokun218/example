if __name__ == "__main__":
    n, k = map(int, input().split())

    arr = [0]
    arr += list(map(int, input().split()))
    
    arr.sort()

    res = 0
    c = n
    for i in range(n,0,-1):
        if ( arr[i] + k <= arr[c]):
            c -= 1
        else: 
            res += arr[i]
    print(res)