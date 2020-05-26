if __name__ == "__main__":
    n,m = map(int, input().split())

    arr = []
    arr += list(map(int, input().split()))

    arr.sort(reverse=True)

    res = 0
    if (m == 1 ):
        m = 0
    else:
        for i in arr:
            if i >= m:
                res += 1
                m = m - i
                break
            else:
                m = m - (i-1)
                res += 1
    if ( m > 0):
        print(-1)
    else:
        print(res)
