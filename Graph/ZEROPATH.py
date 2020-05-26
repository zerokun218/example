n = int(input())
res = [0]
avail = [1]*(n+1)
avail[0] = 0
def dfs(u):
    l = 1
    r = u
    while( True):
        if l > r:
            break
        if u % l == 0:
            l = l
            r = u//l
            # print(l, end = ' ' )
            # print(r)
            v = (l-1)*(r+1)
            # print(v)
            if avail[v] == 1:
                res.append(v)
                avail[v] = 0
                dfs(v)
        l += 1
        r = u/l

dfs(n)
# print(res)
res.sort()
res = list(map(str, res))
print(len(res))
print(' '.join(res))
