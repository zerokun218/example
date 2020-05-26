n,m,s = map(int, input().split())

a = [[] for _ in range(n+1)]

for i in range(1, m+1):
    x,y = map(int, input().split())
    a[x].append(y)

for i in range(1, n+1):
    a[i] = set(a[i])
    a[i] = list(a[i])

# print(a)

d = [10**9]*(n+1)
q = [0]*(n+1)
cnt = 0
res = [0]*(n+1)
avail = [1]*(n+1)

def dijkstra(s,f):
    d[s] = 0
    while True:
        u = 0
        for v in range(1, n+1):
            if avail[v] != 0 and d[v] < d[u]:
                u = v
        if u == 0 or u == f:
            break
        avail[u] = 0

        for i in range(0, len(a[u])):
            if d[a[u][i]] > d[u] + 1:
                d[a[u][i]] = d[u] + 1
                res[a[u][i]] = max(res[u], 1)
            elif d[a[u][i]] == d[u] + 1:
                res[a[u][i]] += res[u]
# avail2 = [1]*(n+1)
# q = [0]*(n+1)
# front = 1
# rear = 1
# q[1] = s
# avail2[s] = 0
# while front <= rear:
#     u = q[front]
#     front += 1
#     for i in range(0, len(a[u])):
#         if avail2[a[u][i]] == 1:
#             rear += 1
#             dijkstra(s, a[u][i])
#             q[rear] = a[u][i]
#             avail2[a[u][i]] = 0

for i in range(1, n+1):
    dijkstra(s, i)
# print(d)
# print(res)
ans = 0
for i in res:
    if i >= 2:
        ans += 1
print(ans)
    
