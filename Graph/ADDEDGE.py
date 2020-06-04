m, s, f = map(int, input().split())

a = [[] for _ in range(m)]
d = dict()
r = []
for _ in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    d['{}-{}'.format(x,y)] = 0
    r.append([x,y])

q = [0]*(10**6 + 1)
avail = [1]*(10**6+1)
t = [0]*(10**6+1)
c = 1

def bfs():
    global c
    front = 1
    rear = 1
    q[1] = s
    avail[s] = 0
    while True:
        if front > rear:
            return
        u = q[front]
        front += 1
        for i in a[u]:
            if avail[i] == 1:
                avail[i] = 0
                rear += 1
                q[rear] = i
                t[i] = u
            if i == f:
                c = 0
                return
bfs()

count = 0
while t[f] != 0:
    count += 1
    d['{}-{}'.format(t[f],f)] = 1
    f = t[f]
if c == 0:
    cnt = 0
    for i in r:
        cnt += 1
        if d['{}-{}'.format(i[0],i[1])] == 1:
            count -= 1
            if count == 0:
                print(cnt)
                break
else:
    print(0)

