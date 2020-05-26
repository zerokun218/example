if __name__ == "__main__":
    x,n = map(int, input().split())

    print(((x % 10000) ** (n % 10000))%10000)
    