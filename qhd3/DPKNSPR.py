p = [1]*(1121)
p[0], p[1] = 0, 0
for i in range(2, 1121):
    if p[i] == 1:
        for j in range(i*i, 1121, i):
            p[j] = 0

res = 0
a = [0]
for i in range(1, 1121):
    if p[i] == 1:
        a.append(i)


def func(x, n, k):
    global res, p
    # print(n, k)
    if n < 0 or n == 1 or (k ==0 and n != 0):
        return
    if n == 0 and k ==0:
        res += 1
        # print(1)
        return
    while x >= 2:
        if p[x] == 1:
            func(min(x-1, n-x),n-x, k-1)
        x -= 1

# print(p)
func(279,279,7)
print(res)

k = 7
n = 279

# print(a)
 
f = [[[0 for _ in range(k+1)] for _ in range(n+1)] for _ in range(len(a))]
for i in range(len(a)):
    f[i][0][0] = 1
    for j in range(n, 0, -1):
        for c in range(1,k+1):
            if a[i] <= j:
                f[i][j][c] = f[i-1][j-a[i]][c-1] + f[i-1][j][c]
            else:
                f[i][j][c] = f[i-1][j][c]
print(f[len(a)-1][279][7])
