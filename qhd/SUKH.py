if __name__ == "__main__":
    n,m,k = map(int, input().split())

    arr = [0]
    
    arr += (list(map(int, input().split())))
#     f = []
#     # for i in range(0, n+1):
#     #     f.append([0]*(m+1))
#     # ok = False
#     # f[0][0] = 1
#     # for i in range(1, n +1):
#     #     f[i][0] = 1
#     #     for j in range(1, m +1):
#     #         if j >= arr[i]:
#     #             f[i][j] = f[i-1][j-arr[i]] + f[i-1][j]
#     #         else:
#     #             f[i][j] = f[i-1][j]
#     #         if f[i][j] >= 100:
#     #             f[i][j] = 105
                
#     # if f[n][m] >= k:
#     #     print('ENOUGH')
#     # else:
#     #     print(f[n][m])

    f = [0]*(m+1)
    f[0]=1
    for i in range(1, n+1):
        for j in range(m, arr[i]-1,-1):
            f[j] += f[j-arr[i]]
            if f[j] > 100:
                f[j] = 105
    
    if f[m] >= k:
        print("ENOUGH")
    else:
        print(f[m])
    