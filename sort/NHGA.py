def func(a):
    pass
if __name__ == "__main__":
    n = int(input())
    arr=[]
    arr += list(map(int, input().split()))
    arr.sort()
    a = [0]*(n-1)
    for i in range(1,n):
        a[i-1] = abs(arr[i] - arr[i-1])
    # del a[0]
    # a.remove(0)
    # print(a)
    print(min(a))
    