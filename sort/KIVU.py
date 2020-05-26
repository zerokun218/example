if __name__ == "__main__":
    n,m = map(int, input().split())

    arr_a = [0]
    arr_b = [0]

    arr_a += list(map(int, input().split()))
    arr_a.sort()
    arr_b += list(map(int, input().split()))
    arr_b.sort()


    res = 0
    i = n
    j = m
    while (i != 0 and j !=0):
        if arr_a[i] > arr_b[j]:
            res += 1
            i -= 1 
            j -= 1
        else:
            j -=1

    print(res)