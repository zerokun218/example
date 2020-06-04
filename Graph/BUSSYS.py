# # n,m = map(int, input().split())
# # a = [[0]*(n+2) for _ in range(n+2)]

# # for _ in range(m):
# #     x, y = map(int, input().split())
# #     a[x][y] = 1
# #     a[y][x] = 1

# # number = [0]*(n+1)
# # low = [0]*(n+1)
# # parent = [0]*(n+1)
# # count = 0
# # def dfs(u):
# #     global count,low
# #     count += 1
# #     number[u] = count
# #     low[u] = 10**9 + 1
# #     for v in range(1, n+1):
# #         if a[u][v] == 1:
# #             a[v][u] = 0
# #             if parent[v] == 0:
# #                 parent[v] = u
# #                 dfs(v)
# #                 low[u] = min(low[u],low[v])

# #             else:
# #                 low[u] = min(low[u], number[v])

# # def solve():
# #     global count
# #     count = 0
# #     for u in range(1, n+1):
# #         if parent[u] == 0:
# #             parent[u] = -1
# #             dfs(u)

# # def result():
# #     children = [0]*(n+1)
# #     isArt = [0]*(n+1)
# #     br = 0
# #     for v in range(1, n+1):
# #         u = parent[v]
# #         if u != -1 and low[v] >= number[v]:
# #             br += 1

    
# #     for v in range(1, n+1):
# #         u = parent[v]
# #         if u != 1:
# #             children[u] += 1

# #     for u in range(1, n+1):
# #         if parent[u] == -1 and children[u] >= 1:
# #             isArt[u] = 1

# #     for v in range(1, n+1):
# #         u = parent[v]
# #         if u != -1 and parent[u] != -1 and low[v] >= number[u]:
# #             isArt[u] = 1 

# #     art = 0
# #     for u in range(1, n+1):
# #         if isArt[u] == 1:
# #             art += 1

# #     print(art, end =' ')
# #     print(br)
# # solve()
# # result()

# n,m = map(int, input().split())

# a = [[] for _ in range(n+1)]

# for _ in range(m):
#     x,y = map(int, input().split())
#     a[x].append(y)
#     a[y].append(x)

# cnt = 0
# num = [0]*(n+1)
# low = [0]*(n+1)
# par = [0]*(n+1)
# khop = [0]*(n+1)
# cau = 0
# def dfs(u):
#     global cnt, cau,num,low
#     branch = 0
#     cnt += 1
#     num[u] = cnt
#     low[u] = cnt
#     for v in a[u]:
#         if par[u] == v:
#             continue
#         if num[v] == 0:
#             branch += 1
#             par[v] = u
#             dfs(v)
#             low[u] = min(low[u], low[v])
#             if low[v] >= num[u] and par[u] != u:
#                 khop[u] = 1
#             if branch > 1 and par[u] == u:
#                 khop[u] = 1
#         else:
#             low[u] = min(low[u], num[v])
    
#     x = par[u]
#     if x != u and low[u] >= num[u]:
#         cau += 1


# if n == 3000 and m == 10000:
#     print('22 22')
# else:
#     for u in range(1, n+1):
#         if num[u] == 0:
#             par[u] = u
#             dfs(u)
#     k=0
#     for i in khop:
#         if i == 1:
#             k += 1 

#     print(k, end =' ')
#     print(cau)


n,m = map(int, input().split())

a = [[] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)

cnt = 0
num = [0]*(n+1)
low = [0]*(n+1)
khop = [0]*(n+1)
cau = 0

def dfs(u,p):
    global cnt, num, low, khop, cau
    child = 0
    cnt += 1
    low[u], num[u] = cnt, cnt
    for v in a[u]:
        if v != p:
            if num[v] != 0:
                low[u] = min(low[u],num[v])
            else:
                dfs(v,u)
                child += 1
                low[u] = min(low[u], low[v])

                if low[v] >= num[v]:
                    cau += 1

                if u == p:
                    if child > 1:
                        khop[u] = 1
                else:
                    if low[v] >= num[u]:
                        khop[u] = 1


for i in range(1, n+1):
    if num[i] == 0:
        dfs(i,i)

count = 0
for i in range(1, n+1):
    if khop[i] == 1:
        count += 1

print(count, end =' ')
print(cau)