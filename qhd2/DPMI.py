while True:
    s = int(input())
    if s != -1:
        n = s
        a = [[0,0]]
        for i in range(0, n):
            a.append(list(map(int, input().split())))
        a.sort(key = lambda x: x[1])
        a.sort(key = lambda x: x[0])

        f = [1]*(n+1)
        f[0] = 0
        for i in range(1, n+1):
            for j in range(1, i):
                if a[i][0] >= a[j][1]:
                    f[i] += f[j]
        res = ['0']*(8)
        ans = 0
        for i in f:
            ans = (ans + i)% 10**8
        ans = str(ans)
        j = 0
        for i in ans[::-1]:
            j -= 1
            res[j] = i
        print(''.join(res))
    else:
        break