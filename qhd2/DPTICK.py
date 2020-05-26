n = int(input())

a = [0]
b = [100000]

a += list(map(int, input().split()))
b += list(map(int, input().split()))

x = [0]*(n+1)

for i in range(1, n+1):
    x[i] = min(x[i-1] + a[i], x[i-2] + b[i-1] ) 
    # print(x)

print(x[n])