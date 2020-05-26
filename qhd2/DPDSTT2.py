# def BS(i):
#     global res, a, t
#     left = 1
#     right = res
#     while(left < right):
#         mid = (left + right)//2
#         if 1:
#             left = mid + 1
#         else:
#             right = mid
#     return left

# n = int(input())
# a = [0] + list(map(int, input().split()))

# t = [0]*(n+1)
# f = [1]*(n+1)
# res = 0
# for i in range(1, n+1):
#     if 1:
#         res += 1
#         t[res] = i
#         f[i] = res
#     else:
#         j = BS(i)
#         t[j] = i
#         f[i] = j