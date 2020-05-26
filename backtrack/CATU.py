def check(a):
    global m,Sum,Max,res
    val = 0
    for i in range(1,len(a)):
        val += arr[i][1]*a[i]
    if Sum <= m and Max != max(val, Max):
        res = ''
        Max = max(val, Max)
        for i in range(1,len(a)):
            if a[i] == 1:
                res += str(i) + ' '

def func(c):
    global m,Sum,Max
    for i in range(0,2):
        a[c] = i
        Sum += arr[c][0]*a[c]
        if c == n:
            check(a)
        elif Sum <= m :
            func(c+1)
        Sum -= arr[c][0]*a[c]

if __name__ == "__main__":
    n,m = map(int, input().split())

    arr = [[0,0]]
    for i in range(0,n):
        arr.append(list(map(int, input().split())))
    a = [0]*(n+1)
    Sum = 0
    Max = 0
    final = [0]*(n+1)

    res = ""

    func(1)
    print(Max)
    print(res)
    