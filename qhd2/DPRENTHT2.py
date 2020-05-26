def BS(i):
    global res, a, t
    left = 1
    right = res
    while(left < right):
        mid = (left + right)//2
        if a[i][0] > a[t[mid]][1]:
            left = mid + 1
        else:
            right = mid
    return left

n = int(input())

a = [[0,0]]

for i in range(n):
    a.append(list(map(int, input().split())))

a.sort(key = lambda x: x[1])
a.sort(key = lambda x: x[0])
# print(a)

f = [1]*(n+1)
t = [0]*(n+1)

res = 0
for i in range(1, n+1):
    if a[i][0] > a[t[res]][1]:
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
print(res)