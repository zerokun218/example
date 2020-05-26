n, k = map(int, input().split())

kk = list(map(int, input().split()))

m = int(input())
a = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)

d = [0]*(n+1)

avail = [1]*(n+1)
q = [0]*(n+1)
def bfs():
    global d, avail
    front = 1
    rear = 0
    for i in kk:
        rear += 1
        q[rear] = i
        avail[i] = 0

    while True:
        if front > rear:
            return
        u = q[front]
        front += 1
        for i in a[u]:
            if avail[i] == 1:
                d[i] = d[u] + 1
                rear += 1
                q[rear] = i
                avail[i] = 0

bfs() 

for i in range(1, n+1):
    print(d[i], end =' ')
