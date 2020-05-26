t = int(input())
for i in range(t):
    n = int(input())
    a = [0] + list(map(int, input().split()))

    s = sum(a)

    f = [0]*(s + 1)
    f[0] = 1
    for i in range(1, n+1):
        for j in range(s, a[i]-1, -1):
            if f[j-a[i]] == 1:
                f[j] = 1
    for i in range(0, s + 1):
        if f[i] == 1:
            print(i, end =' ')
    print()

