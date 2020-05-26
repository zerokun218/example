if __name__ == "__main__":
    n = int(input())

    arr = [0]
    arr += list(map(int, input().split()))

    f = [0]*(n+1)
    s = [0]*(n+1)

    for i in range(2, n+1):
        f[i] = s[i-1] + arr[i-1] - 1
        s[i] = max(f[i-1] + arr[i] - 1, s[i-1] + abs(arr[i] - arr[i-1]))
        # print(f)
        # print(s)

    print(max(f[n], s[n]))