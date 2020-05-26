if __name__ == '__main__':
    t = int(input())
    a= [0]
    for i in range(0, t):
        a.append(int(input()))

    f = [0]*(1001)
    f[0] = 1
    for i in range(2, 1000 +1):
        for j in range(i, 1000 +1):
            f[j] = (f[j] + f[j-i]) % (10000000007)

    for i in range(1, t+1):
        print(f[a[i]] % (1000000000))