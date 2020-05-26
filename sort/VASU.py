if __name__ == "__main__":
    n = int(input())
    arr = []
    arr += list(map(int, input().split()))

    arr.sort(reverse=True)
    res = 0
    count=0
    for i in arr:
        if (i - count > 0):
            res += i - count
            count += 1
        else: break
    
    print(res)
