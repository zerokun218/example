n,m,s = map(int, input().split())

a = [[] for _ in range(n+1)]

for i in range(1, m+1):
    x,y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)

avail = [1]*(n+1)
d = [10**9]*(n+1)

# def dijkstra(s,f):
#     d[s] = 0
#     while True:
#         u = 0
#         for v in range(1, n+1):
#             if avail[v] != 0 and d[v] < d[u]:
#                 u = v
#         if u == 0 or u == f:
#             break
#         avail[u] = 0

#         for i in range(0, len(a[u])):
#             if d[a[u][i]] > d[u] + 1:
#                 d[a[u][i]] = d[u] + 1
# res = []
# for i in range(1,n+1):
#     dijkstra(s, i)
#     if d[i] != 10**9:
#         res.append((i,d[i]))


q = [0]*(n+1)
def bfs(s):
    front = 1
    rear = 1
    q[1] = s
    avail[s] = 0
    d[s] = 0 
    while True:
        if front > rear:
            return
        u = q[front]
        front += 1

        for i in a[u]:
            if avail[i] == 1:
                d[i] = d[u] + 1
                avail[i] = 0
                rear += 1
                q[rear] = i

bfs(s)
res = []
for i in range(1, n+1):
    if d[i] != 10**9:
        res.append((i, d[i]))

res.sort(key = lambda x: x[0])
res.sort(key = lambda x: x[1])
for i in res:
    print(i[0], end=' ')
    print(i[1])

