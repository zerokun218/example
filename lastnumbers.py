def last_number(k,m,n):
    res = 1
    print(m**n)
    for _ in range(1,n+1):
        print(_)
        res = int(res*m)%(10**k)

    print(res)


if __name__ == "__main__":
    k,m,n=map(int, input().split())
    last_number(k,m,n)