def func(a,i,j):
    return a[j]-a[i-1]

if __name__ == "__main__":
    n=int(input())
    arr=[0]
    for i in range(1,n+1):
        arr.append(int(input())+arr[i-1])
    print(arr)
    max=arr[0]
    for h in range(1,n+1):
        for k in range(h, n+1):
            if (max < func(arr,h,k)):
                max = func(arr,h,k)
                max_i = h
                max_j = k
    
    print(max)
    print(max_i)
    print(max_j)