
def out(a):
    for i in range(1,len(a)):
        print(a[i], end = "")
    print()

def func(k):
    for i in range(0,2):
        res[k] = i
        if k == n:
            out(res)
        else:
            func(k+1)


if __name__ == "__main__":
    n = int(input())
    res = [-1]*(n+1)

    func(1)
