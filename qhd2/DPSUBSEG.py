t = int(input())
res = []
for i in range(0, t):
    n = int(input())
    a = [0] + list(map(int, input().split()))
    # a = [-1 if x < 0 else (0 if x == 0 else 1) for x in a]
    for j in range(1, n+1):
        if a[j] > 0:
            a[j] = 1
        elif a[j] < 0:
            a[j] = -1
    # print(a)
    f = [1]*(n+1)
    m = 1
    for j in range(n-1, 0, -1):
        if a[j]*a[j+1] < 0:
            f[j] = f[j+1] + 1
    # print(f)
    for j in range(1, n+1):
        print(f[j], end=' ')
    print()

# for i in res:
#     for j in i[1:]:
#         print(j,end = ' ')
#     print()
        
