# def BS(i, k):
#     pass


# n = int(input())

# a = [-10**11] + list(map(int, input().split()))

# t = [[0]*(n+1) for x in range(50)]
# f = [[1]*(n+1) for x in range(50)]

# res = 0
# for k in range(1, 51):
#     res = 0
#     for i in range(1, n+1):
#         if a[i] - a[t[k][res]] == k:
#             res += 1
#             t[k][res] = i
#             f[k][i] = res
#         else:
#             j = BS(i, k)
#             t[k][j] = i
#             f[k][i] = j