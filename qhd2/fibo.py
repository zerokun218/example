MOD = 10**9 + 7

n = int(input())


fibo = [0] * (10**6 +1)
fibo[1] = 1
fibo[2] = 1
for i in range(3, 10**6 +1):
    fibo[i] = (fibo[i-1] + fibo[i-2]) % MOD
# for i in range(0, n):
#     print(fibo[i+1], end =' ' )
# print()
print(fibo[n])