if __name__ == "__main__":
    n = int(input())

    arr_a = []
    arr_a += list(map(int, input().split()))

    arr_b = []
    arr_b += list(map(int, input().split()))

    arr = []
    for i in range(0,n):
        arr.append(arr_a[i] + arr_b[i])
    
    
    arr_a.sort()
    arr.sort()

    # for i in range(0,n):
    #     arr.append(arr_a[i], arr_b[i])

    # arr.sort(key = lambda x: x[0])

    # f = [arr[0][0] + arr[0][1]]
    # count = 1
    # for i in range(1,len(arr)):
    #     val = f[0]
    #     print(val)
    #     if (arr[i][0] >= val ):
    #         f.pop(0)
    #     else:
    #         count +=1
    #     f.append(arr[i][0] + arr[i][1])
    #     f.sort()
    
    count = 0
    k = 0
    for i in range(0, n):
        if (arr_a[i] < arr[k]):
            count += 1
        else:
            k += 1
  
    print(count)