def func(k,s):
    if len(s) == n:
        if s not in res:
            res.append(s)
    if k < n:
        func(k+1, s+a[k])
        func(k+1, s+b[k])

if __name__ == "__main__":
    n = int(input())

    a = ''
    b = ''
    res = []
    a = input()
    b = input() 
    func(0,'')
    res.sort()
    print(len(res))
    for i in res:
        print(i)
