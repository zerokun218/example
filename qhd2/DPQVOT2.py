# def BS(i):
#     global res, a, t
#     left = 1
#     right = res
#     while(left < right):
#         mid = (left + right)//2
#         if a[i] - a[t[mid]] >= k:
#             left = mid + 1
#         else:
#             right = mid
#     return left

# n, k = map(int, input().split())

# a = [0] + list(map(int, input().split()))
# b = [0] + list(map(int, input().split()))

# f = [0]*(n+1)
# t = [0]*(n+1)

# res = 0
# for i in range(1, n+1):
#     f[i] = b[i]
#     if a[i] - a[t[res]] >= k:
#         res += 1
#         t[res] = i
#         f[i] = max(f[i], f[t[res-1]] + b[i])
#     else:
#         j = BS(i)        
#         if f[t[j]] < f[t[j-1]] + b[i]:
#             t[j] = i 
#         f[i] = max(f[i], f[t[j - 1]] + b[i])

#         for s in range(i-1, t[j-2], -1):
#             if a[i] - a[s] >= k:
#                 f[i] = max(f[i], f[s] + b[i])
# # print(t)
# print(max(f))