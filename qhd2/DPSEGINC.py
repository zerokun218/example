n = int(input())

a = [1] + list(map(int, input().split()))

f = [0]*(n+1)
m = 0
jmax = 0
for i in range(1, n+1):
    for j in range(i, 0, -1):
        if a[i] % a[j] == 0:
            f[i] = max(f[j] + 1, f[i])
            if m != max(m, f[i]):
                m = max(m, f[i])
                jmax = i
print(m)
t = []
for i in range(jmax, 0, -1):
    if  a[jmax] % a[i] == 0 and f[i] == m: 
        t.append(str(i))
        jmax = i
        m -= 1
print(' '.join(t[::-1]))