if __name__ == "__main__":
    n = int(input())

    res = []
    for i in range(0,n):
        h,k = map(int, input().split())
        arr = []
        arr += list(map(int, input().split()))

        arr.sort(reverse= True)
        j = 0
        count = 1
        for key in range(0,h-1):
            if (arr[j] - arr[key+1] > k ):
                count += 1
            j += 1
        
        res.append(count)
    
    for i in range(1,n+1):
        print("Case #{}: {}".format(i, res[i-1]))
