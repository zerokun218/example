# t = int(input())
# for _ in range(t):
#     n, m = map(int, input().split())

#     a = []
#     for i in range(n):
#         a.append(input())
    
#     t = [0]*(m+1)
#     for i in range(0,m):
#         a.sort(key = lambda x: x[i])
#         for j in range(1, n):
#             if a[i][j] != a[i][j-1]:
#                 t[i] += 1
    
#     if sum(t) > 2:
#         print(-1)
#     else:
#         for i in range(0, m):
#             if t[i] == 0:
#                 t[i] = a[0][i]
            
