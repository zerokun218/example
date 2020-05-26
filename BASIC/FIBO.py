def func(n):
    if n == 1 or n == 2:
        return 1
    return func(n-1) + func(n-2)

if __name__ == "__main__":
    n = int(input())

    print(func(n))
    # f = [0]*(n+1)
    # f[1] = 1
    # f[2] = 1

    # for i in range(3,n+1):
    #     f[i] = f[i-1] + f[i-2]
    
    # for i in range(1,n+1):
    #     print(f[i], end = ' ')