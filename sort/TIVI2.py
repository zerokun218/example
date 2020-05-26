if __name__ == "__main__":
    
    n = int(input())

    arr = []
    f = [0]*(100010)
    for i in range(0,n):
        a = tuple(map(int, input().split()))
        arr.append(a)
        f[a[1]] += 1
    
    arr.sort(key = lambda x: x[1])
    for i in range(1,len(f)):
        f[i] += f[i-1]

    res = 0
    k = 0
    for i,j in arr[:]:
        sub = 0
        if (f[j] - f[j-1] > 1 and j != k):
            x = f[j] - f[j-1]
            sub = (1/2)*x*(x-1)
            k = j
            
        res += f[j-1] - f[i] + sub
    print(int(res))