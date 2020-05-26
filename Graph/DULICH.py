# n,m = map(int, input().split())


# tp = [(0,10**18) for _ in range(n+1)]
# # print(tp)
# for i in range(1, m+1):
#     a,b,c = map(int, input().split())
#     tp[a].append((b,c))
#     tp[b].append((a,c))

# print(tp)
 
# d = [10**9]*(n+1)

# def dijkstra(s, f):
#     d = [10**9]*(n+1)
#     avail = [1]*(n+1)
#     d[s] = 0
#     while True:
#         u = 0
#         for v in range(1, n+1):
#             if avail[v] != 0 and d[v] < d[u]:
#                 u = v
#         if u == 0 or u == t:
#             break
#         avail[u] = 0

#         for i in range(0, len(tp[u])):
#             if d[tp[i][0]] > d[u] + tp[i][1]:
#                 d[tp[i][0]] = d[u] + tp[i][1]
# ans = 10**18 + 99
# for i in range(1, n+1):
#     for j in range(i+1, n+1):
#         dijkstra(i,j)
#         for k in range(j+1, n+1):
#             ans = min(ans, a[i][j] + a[i][k] )