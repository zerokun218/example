n = int(input())

a = [-10**9 - 10] + list(map(int, input().split()))

f = [1]*(len(a))
res = 0
jmax = 0
t = [0]*(len(a))
for i in range(1, len(a)):
    m = 0
    for j in range(0, i):
        if a[j] < a[i]:
            m = max(m, f[j] + 1)
                
    f[i] = m
    if max(res, f[i]) != res:
        jmax = i
        res = max(res, f[i])

# print(f)
print(res - 1)
s = res
k = jmax
t = []
while s != 1:
    if f[k] == s:
        t.append(k)
        s -= 1
    k -= 1
for i in t[::-1]:
    print(i, end = ' ')
