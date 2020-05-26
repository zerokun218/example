if __name__ == "__main__":
    a = int(input())

    n = 0
    m = 0
    n = int(a/7)
    m = a % 7
    if n % 2 == 0:
        print(7-m,end = ' ' )
        print(m)
    else:
        print(m,end=' ')
        print(7-m)