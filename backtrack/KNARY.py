def res(a):
    final.append("".join(a[1:]))
def func(c):
    global count
    for i in range(1,k+1):
        arr[c] = str(i)
        if c == n:
            count += 1
            res(arr)
        else:
            func(c+1)

if __name__ == "__main__":
    k,n = map(int, input().split())

    arr = [0]*(n+1)
    final = []
    count = 0

    func(1)

    print(count)
    for i in final:
        print(i)