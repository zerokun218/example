if __name__ == "__main__":
    n = int(input())

    arr = []
    for i in range(0,n):
        arr.append(tuple(map(int, input().split())))
    arr.sort(key = lambda x: x[1])

    day = 0
    count = 0
    for i,j in arr[:]:
        if (i > day):
            count += 1
            day = j

    print(count)
