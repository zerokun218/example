if __name__ == "__main__":
    n = int(input())

    # 1    1 1
    # 1    1 0 
    f = [0]*(n+1)
    f[0] = 1
    f[n] = 1
    for i in range(1, n+1):
        f[i] = (f[i-1] + f[i-2] + f[i-1]) % 10**8
    # print(f)
    print(f[n] % 10**8)
