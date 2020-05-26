s = 0
res = 0
def func(i):
    global s,res
    for k in range(0,2):
        f[i] = k
        s += arr[i]*f[i]
        if i == m:
            print(f)
            if s <= n:
                res = max(s,res)
        elif s <= n:
            func(i+1)
        s -= arr[i]*f[i]
    return res
    
# if __name__ == "__main__":
#     n,m = map(int, input().split())

#     arr = [0]
#     for i in range(0,m):
#         arr.append(int(input()))
#     f = [0]*(n+1)
#     f[0] = 1
#     for i in range(1,m +1):
#         for j in range(0, n +1):
#             if j >= arr[i]:
#                 f[j] = max(f[j], f[j-arr[i]])
#     for i in range(n,-1,-1):
#         if f[i] == 1:
#             print(i)
#             break

if __name__ == "__main__":
    n,m = map(int, input().split())

    arr = [0]
    for i in range(0,m):
        arr.append(int(input()))
    f = [0]*(m+1)
    print(func(1))
    # for i in range(1, m +1):
    #     for j in range(1, n+1):
    #         f[i][j] = f[i-1][j]
    #         if j >= arr[i]:
    #             f[i][j] = max(f[i-1][j-arr[i]] + arr[i], f[i][j])
    # print(f[m][n])
    # # for i in f:
    # #     print(i)
    # # while n > 0:
    # #     if f[n][m] != f[n-1][m]:
    # #         print(n, end = ' ' )
    # #         m = m - a[n]
    # #     n -=1

    print(n)
    