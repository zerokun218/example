n = int(input())

t = [0] + list(map(int, input().split()))
r = [100000] + list(map(int, input().split()))

f = [0]*(n+1)
tr = [0]*(n+1)

for i in range(1, n+1):
    f[i] = min(f[i-1] + t[i], f[i-2] + r[i-1])
s = f[n]
for i in range(n, 0, -1):
    if f[i-1] + t[i] == s:
        tr[i] = 1
        s -= t[i]
    elif f[i-2] + r[i-1] == s:
        tr[i-1] = 1
        s -= r[i-1]
     
# print(f)
count = 0
for i in tr:
    if i == 1:
        count+= 1
print(count)
for i in range(1, n+1):
    if tr[i] == 1:
        print(i, end = ' ')
