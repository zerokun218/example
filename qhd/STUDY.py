s = 0
res = 0

f = []
# def check():
#     global res,m,f
#     temp = 0
#     print(t)
#     c = sum(t)
#     for i in range(1,n+1 ):
#         temp += a[i][ t[i] ]
#     if c == m and res != max(res, temp):
#         res = max(res, temp)
#         f = t[:]
# def func(i):
#     global n,m,s,res,t
#     for k in range(0,m+1):
#         s += k
#         t[i] = k
#         if i == n:
#             check()
#         elif s <= m:
#             func(i+1)
#         s -= k

def func( ai, b):
    if ai == 0:
        return 0
    c, d = 0, 0
    for i in range(1, m+1):
        if i <= b:
            c = func(ai-1, b-i) + a[ai][i]
        d = max(c,d)
    return max(d, func(ai -1, b )) 
            
    

if __name__ == "__main__":
    n,m = map(int, input().split())
    t = [0]*(n+1)
    a = [[0]*(m+1)]

    for i in range(0, n):
        a.append([0]+list(map(int, input().split())))
    
    print(func(n,m))