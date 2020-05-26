if __name__ == "__main__":
    n = int(input())

    arr = []

    for i in range (0,n):
        a=tuple(map(int, input().split()))
        arr.append(a)
    
    arr.sort(key = lambda x: x[0] )

    min = -1
    res = 0
    for i in arr:
        if (i[0] >= min):
            min = i[1]
            res += i[1] - i[0]
        # if i[0] < min
        else:
            if (i[1] > min):
                res += i[1] - min
                min = i[1]

    print(res)