def BS(i, a, t):
    global res
    left = 1
    right = res
    while(left < right):
        mid = (left + right)//2
        if a[i] > a[t[mid]]:
            left = mid + 1
        else:
            right = mid
    return left

n = int(input())
a = [-10**10] + list(map(int, input().split()))
b = [-10**10] + a[:0:-1]

t1 = [0]*(n+1)
f1 = [1]*(n+1)
res = 0
for i in range(1, n+1):
    if a[i] > a[t1[res]]:
        res += 1
        t1[res] = i
        f1[i] = res
    else:
        j = BS(i, a, t1)
        if a[t1[j]] > a[i]:
            t1[j] = i
        f1[i] = j

t2 = [0]*(n+1)
f2 = [1]*(n+1)
res = 0
for i in range(1, n+1):
    if b[i] > b[t2[res]]:
        res += 1
        t2[res] = i
        f2[i] = res
    else:
        j = BS(i, b, t2)
        if b[t2[j]] > b[i]:
            t2[j] = i
        f2[i] = j
# print(f1)
# print(f2)
ans = 1
for i in range(1, n+1):
    if f1[i] > 1 and f2[n-i + 1] > 1:
        ans = max(ans, f1[i] + f2[n-i+1] - 1)

print(ans)