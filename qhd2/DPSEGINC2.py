# def BS(i):
#     global res, a, t
#     left = 1
#     right = res
#     while(left < right):
#         mid = (left + right)//2
#         if a[i] % a[t[mid]] == 0:
#             left = mid + 1
#         else:
#             right = mid
#     return left

# n = int(input())

# a = [1] + list(map(int, input().split()))

# t = [0]*(n+1)
# f = [1]*(n+1)
# res = 0
# for i in range(1, n+1):
#     if a[i] % a[t[res]] == 0:
#         res += 1
#         t[res] = i
#         f[i] = res
#     else:
#         j = BS(i)
#         t[j] = i
#         f[i] = j
# print(t)
# print(f)