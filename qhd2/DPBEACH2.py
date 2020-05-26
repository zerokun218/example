def BS(i, t):
    global res, a
    l = 1
    r = res
    while (l < r):
        m = (l + r)//2
        if a[i] > a[t[m]]:
            l = m + 1
        else:
            r = m
    return l

def BS2(i, t):
    global res, a
    l = 1
    r = res
    while (l < r):
        m = (l + r)//2
        if a[i] < a[t[m]]:
            l = m + 1
        else:
            r = m
    return l

n = int(input())

a = [0] + list(map(int, input().split())) + [0]
a = a[::-1]
t1 = [0]*(n+1)
f1 = [1]*(n+1)
res = 0
for i in range(1, n+1):
    if a[i] > a[t1[res]]:
        res += 1
        t1[res] = i
        f1[i] = res
    else:
        j = BS(i, t1)
        if a[t1[j]] > a[i]:
            t1[j] = i
        f1[i] = j
# print(a)
a[0] = 10**18
t2 = [0]*(n+1)
f2 = [1]*(n+1)
res = 0
for i in range (1, n+1):
    if a[i] < a[t2[res]]:
        res += 1
        t2[res] = i
        f2[i] = res
    else:
        j = BS2(i, t2)
        if a[t2[j]] < a[i]:
            t2[j] = i
        f2[i] = j

# print(t1)
# print(f1)
# print(t2)
# print(f2)

ans = 0
for i in range(1, n+1):
    ans = max(ans,f1[i] + f2[i] - 1)

print(ans)