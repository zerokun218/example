t = int(input())
for _ in range(t):
    n,m,k = map(int, input().split())

    a = n//k

    ma = 10**9
    ma = min(ma, m, a)
    m -= ma

    pl = m//(k-1)
    m = m%(k-1)

    if m != 0:
        print(ma - pl -1)
    else:
        print(ma - pl)
# zero