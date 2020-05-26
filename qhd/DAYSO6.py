if __name__ == "__main__":
    n = int(input())

    a = [0]

    a += list(map(int, input().split()))

    
    
    fi = [0]*(n+1)
    fj = [0]*(n+1)
    fk = [0]*(n+1)
    fi[0],fj[1],fk[2] = -10**9,-10**9,-10**9
    for i in range(1,n +1):
        fi[i] = max(fi[i-1],a[i])
    for i in range(2,n +1):
        fj[i] = max(fj[i-1], 2*a[i]+fi[i-1])
    for i in range(3, n+1):
        fk[i] = max(fk[i-1], 3*a[i] +fj[i-1])
    print(fk[n])
