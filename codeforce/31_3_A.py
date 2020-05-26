if __name__ == "__main__":
    t = int(input())

    first = []
    second = []

    for i in range(0, t):
        first.append(list(map(int, input().split())))
        second.append(list(map(int, input().split())))
    
    res = []
    for i in range(0, t):
        l = first[i][0]
        r = first[i][1]
        d = first[i][2]
        u = first[i][3]

        lr = l - r 
        du = d - u 


        space = abs(second[i][2] - second[i][4])
        high = abs(second[i][3] - second[i][5]) 

        x,y = (second[i][0], second[i][1])

        left = abs(x - second[i][2])
        down = abs(y - second[i][3])
        
        if (left - lr >=0 and left - lr <= space) and (down - du >= 0 and down - du <= high):
            res.append('Yes')
        else:
            res.append('No')
        if (x - min(1,l) < second[i][2] and x + min(1,r) > second[i][4]):
            res[i] = 'No'
        if y - min(1,d) < second[i][3] and y + min(1,u) > second[i][5]:
            res[i] = 'No'
        
    
    for i in res:
        print(i)
