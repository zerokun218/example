if __name__ == "__main__":
    a = int(input())
    res = 0
    if a == 1:
        res = 1
    for i in range(2, int(a**(1/2))+1):
        if a % i == 0:
            res = 1
            break
    if res == 1:
        print('NO')
    else:
        print("YES")