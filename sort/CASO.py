if __name__ == "__main__":
    n = int(input())
    arr = []
    arr += list(map(int, input().split()))

    arr.sort()

    res = 0
    comp = 0
    count = 0
    for i in range(0,len(arr)):
        
        if (arr[i] != comp):
            comp = arr[i]
            res += int( (1/2)*count*(count-1) )
            count = 1
        else:
            count += 1
        
        if ( i == len(arr) - 1):
            res += int( (1/2)*count*(count-1) )
            break
    print(res)