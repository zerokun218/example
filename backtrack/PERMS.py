def res(a):
    final.append("".join(a[1:]))
def func(k ):
    global count
    for i in range(1,n+1):
        if check[i] == 0:
            arr[k] = str(i)
            check[i] = 1
            if k == n:
                count += 1
                res(arr)
            else:
                func(k+1)
            check[i] = 0
            


if __name__ == "__main__":
    n = int(input())
    count = 0
    arr = [0]*(n+1)
    final = []
    check = [0]*(n+1)

    func(1)
    print(count)
    for i in final:
        print(i)