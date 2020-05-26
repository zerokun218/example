if __name__ == "__main__":
    n = int(input())

    a = [0]

    a += list(map(int, input().split()))

    f = [0]*(n+1)

    f[3] = a[1] + a[2] + a[3]
    res = f[3]
    for i in range(4, n+1):
        f[i] = max( f[i-3] + a[i] + a[i-1] + a[i-2],  a[i] + a[i-1] + a[i-2])
        res = max(res, f[i])
    # print(f)
    print(res)
    