n, s = map(int, input().split())

a = [[] for _ in range(0, n+1)]
# print(a)
avail = [1]*(n+1)
mark = 0

for i in range(1, n+1):
    t = list(map(int, input().split()))
    a[i] += t[1:]

# print(a)
# for i in head:
#     print(i, end=' ')

res = [str(s)]
def dfs(u):
    global avail, a
    avail[u] = 0
    for i in range(0, len(a[u]) ):
        # print(a, end=' ')
        # print(i)
        if avail[a[u][i]] == 1:
            res.append(str(a[u][i]))
            dfs(a[u][i])
# print(head)
ans = []
q = [0]*(n+1)
def bfs():
    front = 1
    rear = 1
    q[1] = s
    avail[s] = 0
    while( True ):
        if front > rear:
            return
        u = q[front]
        front += 1
        ans.append(u)
        for i in range(0, len(a[u])):
            if avail[a[u][i]] == 1:
                rear += 1
                q[rear] = a[u][i]
                avail[a[u][i]] = 0
        

# dfs(s)
# res.sort()
# print(len(res))
# print(' '.join(res))
bfs()
ans.sort()
print(len(ans))
for i in ans:
    print(i, end = ' ')
