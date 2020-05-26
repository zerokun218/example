n,m = map(int, input().split())

a = [0] + list(map(int, input().split()))
q = []
for i in range(0,m):
    q.append(int(input()))
f = [0]*(n+1)

s = set()

for i in range(n, 0, -1):
    s.add(a[i])
    f[i] = len(s)
for i in q:
    print(f[i])
