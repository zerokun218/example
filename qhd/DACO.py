if __name__ == "__main__":
    n = int(input())

    arr = [0]
    arr += list(map(int, input().split())) + [10**9 + 10]

    t = [0]*(len(arr))
    l = [1]*(len(arr))
    jmax = 0

    for i in range(n+1,-1,-1):
        jmax = n + 1
        for j in range(i+1,n+1 +1):
            if arr[j] > arr[i] and l[j] > l[jmax]:
                jmax = j
            l[i] = l[jmax] + 1
            t[i] = jmax
    #     print(t)
    # print(l)
    print(l[0] - 2)
    i = t[0]
    while i != n + 1:
        print(arr[i], end= ' ' )
        i = t[i]

