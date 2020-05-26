n = 8
check = False
arr = [0]*(n+1) 
cot = [0]*(n+1)
cheochinh = [0]*(n*2+1)
cheophu = [0]*(n*2+1)
def check_func():
    global check
    check = True
    for i in range(1,9):
        for j in range(1,9):
            if arr[i] == j:
                print('w',end='')
            else:
                print('.',end='')
        print()
def func(k):
    global y,x
    if check == True:
        return
    else:
        for i in range(1,9):
            if cot[i] == 0 and cheochinh[k-i+8] == 0 and cheophu[k+i] == 0:
                if i != x and k !=y:
                    arr[k] = i
                    cot[i] = 1                
                    cheochinh[k-i+8] = 1
                    cheophu[k+i] = 1
                if k == 8 or (k == 7 and y == 8):
                    check_func()
                    return
                else:
                    func(k+1)
                if i != x and k !=y:    
                    cot[i] = 0
                    cheochinh[k-i+8] = 0
                    cheophu[k+i] = 0 
       
if __name__ == "__main__":
    y,x = map(int, input().split())

    cot[x] = 1
    cheochinh[y-x+8] = 1
    cheophu[y+x] = 1
    arr[y] = x

    
    func(1)
