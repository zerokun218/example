t = int(input())
for _ in range(t):
    n,m,a,b = map(int, input().split())

    sa = [0]*(n+1)
    sb = [0]*(m+1)

    res = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if sa[i] < a and sb[j] < b:
                res[i][j] = 1
                sa[i] += 1
                sb[j] += 1
    f = max(sa)
    g = max(sb)
    
    if f != a or g != b or sa[n] != a or sb[m] != b:
        print('NO')
    else:
        print('YES')
        for i in res[1:]:
            for j in i[1:]:
                print(j,end='')
            print()