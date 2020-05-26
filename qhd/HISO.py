min_i = -10**9
temp = -10**9
def func(i ):
    global min_i, temp
    print(temp)
    if i <= n:
        if i == 2:
            min_i = arr[i-1]
            temp = arr[i] - min_i
            return max(temp,func(i+1))
        else:
            if min_i > arr[i-1]:
                min_i = arr[i-1]
            temp = max(arr[i] - min_i, func(i+1))
            return temp
    
    print(temp)
    return temp

if __name__ == "__main__":
    n = int(input())

    arr = [0]
    arr += list(map(int, input().split()))

    # Min = [0]*(n+1)
    # Min[1] = arr[1]
    # res = -10**9
    # for i in range(2, n +1):
    #     res = max(res, arr[i] - Min[i-1])
    #     Min[i] = min(Min[i-1], arr[i])

    print(func(2))
