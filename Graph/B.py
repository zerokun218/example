t = int(input())
for _ in range(t):
    n = int(input())
    
    a = [1] + list(map(int, input().split()))
    f = [1]*(n+1)
    res = 1
    for i in range(2, n+1):
        ma = 1
        for j in range(i-1,0, -1):
            if i % j == 0 and a[i] > a[j]:
                f[i] = f[j] + 1
                res = max(res, f[i])
                ma = max(ma, f[i])
        f[i] = ma
    # ma = 1
    # res = 1
    # if n == 1:
    #     print(1)
    # else:
    #     for i in range(2, n+1):
    #         if a[i] > a[1]:
    #             res += 1
    #         c = i
    #         b = i
    #         c += c
    #         while(c <= n):
    #             if a[c] > a[b]:
    #                 res += 1
    #                 b = c
    #                 c += c       
    #             else:
    #                 c += b
    #         ma = max(res, ma)
    #         res = 1
    #     print(ma)
    print(res)
