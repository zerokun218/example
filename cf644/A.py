t = int(input())
for _ in range(t):
    a, b = map(int, input().split())

    a, b = min(a, b), max(a, b)

    s = a*2

    s = max(s, b)

    print(s*s)
# zero  