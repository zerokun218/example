if __name__ == "__main__":
    a = int(input())
    res = 1
    for i in range(2, int(a**(1/2))+1):
        if a % i == 0:
            res += i + a/i
    
    if res == a:
        print("YES")
    else:
        print("NO")