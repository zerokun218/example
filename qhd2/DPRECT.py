n = int(input())

a = [0]
b = [0]

for i in range(0, n):
    x,y = map(int, input().split())

    a.append(x)
    b.append(y)

f = [0]*(n+1)
s = [0]*(n+1)
f[1] = a[1]
s[1] = b[1]
for i in range(2, n+1):
    f[i] = max(f[i-1] + a[i] + abs(b[i] - b[i-1]), s[i-1] + a[i] + abs(b[i] - a[i-1]))
    s[i] = max(f[i-1] + b[i] + abs(a[i] - b[i-1]), s[i-1] + b[i] + abs(a[i] - a[i-1]))

# print(f)
# print(s)
print(max(f[n], s[n]))