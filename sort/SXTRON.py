if __name__ == "__main__":
    n,m = map(int, input().split())

    arr_b = []
    arr_c = []

    arr_b += list(map(int, input().split()))
    arr_c += list(map(int, input().split()))

    for i in range(1, len(arr_b)+1):
        arr_b[i-1] = (arr_b[i-1],'b' + str(i))
    
    for i in range(1, len(arr_c)+1):
        arr_c[i-1] = (arr_c[i-1],'c' + str(i))

    
    arr_a= []
    arr_a += arr_b + arr_c
    arr_a.sort(key = lambda x: x[0])

    for i in arr_a:
        print(i[1], end=' ')