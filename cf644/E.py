t = int(input())
for _ in range(t):
    n = int(input())
    a = [[1]*(n+1)]
    for i in range(n):
        t = input()
        tmp = [int(x) for x in t]
        a.append([1] + tmp + [1])
    a.append([1]*(n+2))
    # print(a)
    c = 1
    for i in range(n, 0, -1):
        for j in range(n, 0, -1):
            if a[i][j] == 1:
                if a[i+1][j] != 1 and a[i][j+1] != 1:
                    c = 0
                    break
        if c == 0:
            break
    if c == 1:
        print('YES')
    else:
        print('NO')

# zero