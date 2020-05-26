Min = '99999999999999999999999'
Max = '00000000000000000000000'

def func(i,j,s):
    global Min,Max
    if len(s) == k:
        print(s)
        Min = min(Min,s)
        Max = max(Max,s)
    if i < len(n):
        func(i+1,j, s+n[i])
    if j < len(m):
        func(i,j+1, s+m[j])
if __name__ == "__main__":
    n,m = map(str, input().split())

    k = len(n) + len(m)
    func(0,0,'')

    print(Min)
    print(Max)
