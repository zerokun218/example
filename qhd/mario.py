if __name__ == "__main__":
    n = int(input())

    arr = [0]

    arr+= (list(map(int, input().split()))) + [0]
    # print(arr)
    res = [0]*(n+2)
    res[0] = 1
    for i in range(1,n+2):
        if arr[i] == 2:
            res[i] = 0
        elif arr[i] == 1:
            res[i] = res[i-1]
        else:
            if i == 1:
                res[i] += res[i-1]
            elif i > 2:
                if arr[i-3] == 1:
                    res[i] += res[i-1] + res[i-2]
                else:
                    res[i] += res[i-1] + res[i-2] + res[i-3]
            else:
                res[i] += res[i-1] + res[i-2]
        # print(res)
        res[i] = res[i] % 10**9
    
    print(res[n+1]% 10**9)