def BS(i):
    global res, a, f
    left = 1
    right = res
    while ( left < right):
        mid = (left + right)//2
        if a[i] > a[f[mid]]:
            left = mid + 1
        else:
            right = mid
    return left





n = int(input())

a = [-10**10] + list(map(int, input().split()))


f = [0]*(n+1)
l = [1]*(n+1)
res = 0
for i in range(1, n+1):
    if a[i] > a[f[res]]:
        res += 1
        f[res] = i
        l[i] = res
    else:
        j = BS(i)
        f[j] = i
        l[i] = j
# print(f)
# print(l)
print(max(l))
        