t = int(input())

f = [0]*(200+1)
f[1] = 1
f[2] = 2
for i in range(3, 201):
    f[i] = f[i-1] + f[i-2]
for i in range(0, t):
    n = int(input())
    print(f[n])