def convert2to16(a):
    res=0
    final=[]
    n=len(a)-1
    for i in range(0,len(a)-1):
        if (a[i] == '1' ):
            res += 2**n
        n -= 1
    while (res > 0):
        if (res % 16 == 10 ):
            final.append('A')
        if (res % 16 == 11 ):
            final.append('B')
        if (res % 16 == 12 ):
            final.append('C')
        if (res % 16 == 13 ):
            final.append('D')
        if (res % 16 == 14 ):
            final.append('E')
        if (res % 16 == 15 ):
            final.append('F')
        else:
            final.append(str(res % 16))
        res =int(res/16)
    print(''.join(final[::-1]))

if __name__ == "__main__":
    convert2to16('11111000101010010')
    