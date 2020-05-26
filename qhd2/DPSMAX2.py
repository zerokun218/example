# def BS(i):
#     global res, a, t
#     left = 1
#     right = res
#     while(left < right):
#         mid = (left + right)//2
#         if a[i] >= a[t[mid]]:
#             left = mid + 1
#         else:
#             right = mid
#     return left

# n = int(input())

# a = [1] + list(map(int, input().split()))

# t = [0]*(n+1)
# f = [0]*(n+1)
# m = [[0]*(n+1) for x in range(n+1)]
# res = 0
# for i in range(1, n+1):
#     if a[i] >= a[t[res]]:
#         res += 1
#         t[res] = i
#         m[res].append(i)
#         for j in m[res - 1]:
#             if a[i] >= a[j]:
#                 f[i] = max(f[i], f[j] + a[i])
#     else:
#         j = BS(i)
#         t[j] = i
#         m[j].append(i)
#         for k in m[j-1]:
#             if a[i] >= a[k]:
#                 f[i] = max(f[i], f[k] + a[i])
# print(t)
# print(f)