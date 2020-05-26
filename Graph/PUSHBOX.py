n,m,k = map(int, input().split())

kk = list(map(int, input().split()))
t = [0]*(n+1)
for i in kk:
    t[i] = 1
# print(t)
a = [[] for i in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    a[y].append(x)


avail = [1]*(n+1)

res = 0
q = [0]*(n+1)
l = [0]*(n+1)
def bfs():
    global res
    front = 1
    rear = 1
    q[1] = 1
    avail[1] = 0
    while True:
        if front > rear:
            return
        u = q[front]
        front += 1
        for i in a[u]:
            if avail[i] == 1:
                l[i] = l[u] + 1
                rear += 1
                q[rear] = i
                avail[i] = 0
                if t[i] == 1:
                    res += l[i]

bfs()
print(res)

