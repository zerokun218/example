def prime(a):
    i=2
    dic={}
    k=a
    while a > 1:
        if (a % i == 0):
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
            a=int(a/i)
            continue
        i = i + 1

    print(dic)
    # dem so luong uoc cua a
    res=1
    for key in dic:
        res = int(res * (dic[key]+1) )
    print(res)

    # tong cac uoc
    result=1
    for key in dic:
        result = int(result * ((key**(dic[key]+1)-1)/(key-1)))
    print(result)

    # sang so nguyen to
    arr = (['0']*(k+1))
    for i in range(2,int(k**(1/2)+1)):
        if(arr[i] == '0' ):
            j=i*i
            while( j <= k):
                arr[j] = '1'
                j=j+i
    res_arr = [i for i in range(2,k) if arr[i] == '0' ]

    print(res_arr)

if __name__ == "__main__":
    prime(1000)
