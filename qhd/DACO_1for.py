def check(x, value):
    i = m[x]
    return value < arr[i]

def bs(l, r, value):
    print([l,r,value])
    global res
    if l > r:
        return
    mid = int((l+r)/2)
    print(mid)
    if check(mid, value):
        res = mid
        print(res)
        bs(mid+1, r, value)
    else:
        bs(l, mid-1, value)
    

if __name__ == "__main__":
    n = int(input())

    arr = [0]
    arr += list(map(int, input().split())) + [10**9 + 10]

    f = [0]*(len(arr))
    m = [0]*(len(arr))
    m[0] = n + 1 

    for k in range(n,-1,-1):
        bs(0, n - k + 1, arr[k])
        print(res)
        f[k] = res + 1
        if arr[k] > arr[m[res +1 ]]:
            m[res+1] = k 
        print(m)
        print(f)
    print(f[0] - 1)
    k = 0

    for i in range(1, n +1):
        if f[k] == f[i] + 1 and arr[k] < arr[i]:
            print(arr[i], end= ' ')
            k = i