if __name__ == "__main__":
    n = int(input())

    arr = []
    arr += list(map(int, input().split()))

    res = [arr[0]]
    poi = []
    for i in range(1,n):
        for j in range(len(res)-1,0-1,-1):
            if (arr[i] >= res[j]):
                poi.append(j+1)
                res.insert(j+1,arr[i])
                break
            elif (j == 0):
                poi.append(0)
                res.insert(0, arr[i])
        
    for i in range(1,n):
        print(arr[i], end=' ')
        print(poi[i-1])

    