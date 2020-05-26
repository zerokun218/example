n,m,q = map(int, input().split())

a = [[] for _ in range(n+1)]

for i in range(1,m+1):
    x,y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)
# ques = list(map(int, input().split()))
ques = []
for i in range(q):
    ques.append(int(input()))

p = [0]*(n+1)
avail = [1]*(n+1)
l = [0]*(n+1)

t = [0]*(n+1)
def bfs(s):
    global avail

    front = 1
    rear = 1
    p[1] = s
    avail[s] = 0
    while(True):
        if front > rear:
            return
        u = p[front]
        front += 1

        for i in a[u]:
            if avail[i] == 1:
                rear += 1
                t[i] = u
                l[i] = l[u] + 1
                p[rear] = i
                avail[i] = 0


bfs(1)
# print(a)
# print(l)
for i in ques:
    print(l[i])


