n, m = map(int, input().split())

a = [[] for i in range(n+1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    a[x].append((y, z))
    a[y].append((x, z))

q = [0]*(n+1)
avail = [1]*(n+1)
d = [10**10]*(n+1)
t = [0]*(n+1)

def dijkstra(s, f):
    d[s] = 0
    while True:
        u = 0
        for i in range(1, n+1):
            if avail[i] == 1 and d[i] < d[u]:
                u = i
        if u == 0 or u == f:
            return
        avail[u] = 0
        for i in a[u]:
            if d[i[0]] > max(d[u], i[1]):
                d[i[0]] = max(d[u], i[1])

dijkstra(1,n)
print(d[n])
