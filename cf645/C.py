t = int(input())
for _ in range(t):
    a1,a2, b1,b2 = map(int, input().split())

    
    print((b2-a2)*(b1-a1) + 1)