k = int(input())
for _ in range(k):
    n,m = map(int, input().split())

    res = 0
    if n % 2 == 0:
        res = (n//2) * m 
    else:
        res = (n//2) * m
        if m % 2 == 0:
            res += m//2
        else:
            res += m//2 + 1
        
    print(res)
    # zero