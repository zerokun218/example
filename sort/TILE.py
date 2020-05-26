if __name__ == "__main__":
    n = int(input())

    arr = []
    arr += list(map(int, input().split()))

    arr.sort(reverse=True)

    dur = arr[0]
    count=0
    for i in arr:
        count += 1
        if (dur == 0):
            break
        if (dur > i):
            dur = i
        dur -= 1
    print(count)
