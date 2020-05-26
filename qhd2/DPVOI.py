a = [[0,0,10**9]]
i = 0
while True:
    s = input()
    if s == '0' :
        break
    else:
        i += 1
        a.append([i] + list(map(int, s.split())))

a.sort(key = lambda x: x[1])
f = [0]*(len(a))
res = 0
for i in range(1, len(a)):
    m = 0
    for j in range(0, i):
        if a[i][2] < a[j][2] and a[i][1] > a[j][1]:
            m = max(m, f[j] + 1)
    f[i] = m
    res = max(res, m)
ans = []
w, iq = 10**9, 0
for i in range(len(a)-1, 0, -1):
    if f[i] == res and a[i][1] < w and a[i][2] > iq:
        ans.append(str(a[i][0]))
        res -= 1
        w, iq = a[i][1], a[i][2] 
print(len(ans))
print(' '.join(ans[::-1]))