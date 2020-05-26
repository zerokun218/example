f = [1]*(10**6+1)
f[0] = 0
f[1] = 0
d = []

# print(f[:100])
# print(d[:100])
t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    bol = 1
    for i in range(2, int(n**(1/2)) +1):
        if n % i == 0:
            bol = 0
            tmp = i
            break
    if bol == 1:
        n += n
        n += 2*(k-1)
    else:
        n += tmp
        n += 2*(k-1)
    print(n)