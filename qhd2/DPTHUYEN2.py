def BS(i):
    global res, a, t
    l = 1
    r = res
    while (l < r):
        m = (l + r)//2
        if a[i][1] >= a[t[m]][1]:
            l = m + 1
        else:
            r = m
    return l

n = int(input())

a = [[0,0]]
for i in range(n):
    a.append(list(map(int, input().split())))

a.sort(key = lambda x: x[1])
a.sort(key = lambda x: x[0])

t = [0]*(n+1)
f = [1]*(n+1)

res = 0
for i in range(1, n+1):
    if a[i][1] >= a[t[res]][1]:
        res += 1
        t[res] = i
        f[i] = res
    else:
        j = BS(i)
        if a[t[j]][1] > a[i][1]:
            t[j] = i
        f[i] = j

# print(t)
# print(f)
print(n - max(f))