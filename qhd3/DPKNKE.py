t = int(input())
for i in range(t):
    n = int(input())
    a = [0] + list(map(int, input().split()))

    s = sum(a)

    f = [0]*(s//2 + 1)
    f[0] = 1
    for i in range(1, n+1):
        for j in range(s//2, a[i]-1, -1):
            if f[j-a[i]] == 1:
                f[j] = 1
    for i in range(s//2, 0, -1):
        if f[i] == 1:
            print(s - 2*i)
            break
