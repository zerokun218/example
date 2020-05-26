count = 0
res = []


def check(a):
    global count, res
    sum = 0
    for i in range(1,len(a)):
        if a[i] == 1:
            sum += 1
        else:
            sum -= 1
        if sum < 0:
            break
    if sum == 0 :
        count += 1
        for i in range(1,len(a)):
            if a[i] == 1:
                print("(",end="")
            else:
                print(")",end="")
        print()


def func(k):
    for i in range(1,-1,-1):
        arr[k] = i
        if k == n :
            check(arr)
        else:
            func(k+1)

if __name__ == "__main__":
    n = int(input())
    arr = [-1]*(n+1) 
    func(1)

    print(count)