def func():
    pass

if __name__ == "__main__":
    n = int(input())

    arr = []
    
    arr += list(map(int, input().split()))

    comp = arr[n-1]

    i=0
    j=0
    while ( i < n-1 and j < n-1):
        if ( arr[i] > comp ):
            i +=1
            continue
        else:
            arr[i],arr[j] = arr[j],arr[i]
            j += 1
            i = j
    arr[j],arr[n-1]=arr[n-1],arr[j]
    arr[j] = '['+str(arr[j])+']'

    for i in arr:
        print(i, end=' ')
    
