n,m,s,t = map(int, input().split())

tp = [[] for _ in range(0, n+1)]

for i in range(m):
    x,y,z = map(int, input().split())

    tp[x].append((y,z))
    tp[y].append((x,z))

# print(tp)

avail = [1]*(n+1)
d = [-1]*(n+1)
d[s] = 10**9

def dijkstra(s,t):
    while True:
        u = 0
        for v in range(1, n+1):
            if avail[v] != 0 and d[v] > d[u]:
                u = v
        if u == 0 or u == t:
            break
        avail[u] = 0
        for i in range(0, len(tp[u])):
            if d[tp[u][i][0]] <= min(d[u],tp[u][i][1]):
                d[tp[u][i][0]] = min(d[u], tp[u][i][1])
dijkstra(s,t)

print(d[t])
