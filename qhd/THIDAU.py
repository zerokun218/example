res = 0
Sum = 0
if __name__ == "__main__":
    n,k = map(int, input().split())

    a = [0]
    b = [0]

    a += list(map(int, input().split()))
    b += list(map(int, input().split()))


    # f = [0]*(a[n]+1)
    # f[1] = b[1]
    # for i in range(2,n +1):
    #     f[i] = b[i]
    #     for j in range(0, i):
    #         if a[i] - a[j] >= k:
    #             f[i] = max(f[j] + b[i], f[i])

    # print(max(f))