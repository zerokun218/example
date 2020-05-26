q = []
while (True):
    x = input()
    if x == '0':
        break
    q.append(x)
res = []
for x in q:
    f = [0]*(len(x)+1)
    f[-1] = 1
    f[0] = 1
    for i in range(1, len(x)):
        if (x[i-1] + x[i] <= '26' and x[i] != '0') and f[i] == 0:
            f[i] = f[i-1] + f[i-2]
        elif x[i-1] + x[i] > '26':
            f[i] = f[i-1]
        if x[i] == '0':
            f[i] = f[i-2]
            f[i-1] = 0
            # print(f)
    # print(f)s
    res.append(f[len(x)-1])

for i in res:
    print(i)
