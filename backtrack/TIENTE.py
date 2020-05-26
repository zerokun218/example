res = []
def check(a):
    global m,res
    Sum = 0
    for i in range(1,len(a)):
        Sum += a[i]*inp[i-1]
        if (Sum > m):
            return
    if Sum == m:
        s = ''
        for i in range(1,len(a)):
            if a[i] == 1:
                s += 'B '
            else:
                s+= 'A '
        res.append(s)

def func(k):
    for i in range(0,2):
        arr[k] = i
        if k == n:
            check(arr)
        else:
            func(k+1)

n =int(input())
inp = []
inp += list(map(int,input().split()))
m = (sum(inp)/2)
arr = [-1]*(n+1)

func(1)
if (len(res) != 0):  
    print(len(res))
    for i in res:
        print(i)
else:
    print('khong chia duoc')