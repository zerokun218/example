def function(n,k):
    res = 1
    for i in range(1,k+1):
        res = int(res*(1/i)*n*n)
        n = n - 1
    print(res)

function(5,1)