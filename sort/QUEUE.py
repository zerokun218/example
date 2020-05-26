import random

def func(l,r):
    i = l
    j = r     
    # x = arr[int((l+r)/2)]
    x = arr[random.randint(i+1, j)]
    
    while (i<=j):
        while (arr[i] < x ): 
            i+=1 
        while (arr[j] > x ):
            j-=1 
        if (i <= j):
            if (i!=j):
                print(i+1, end = ' ')
                print(j+1)
                arr[i], arr[j] = arr[j], arr[i]
            i +=1 
            j -=1 
    if l < j:
        func(l,j) 
    if r > i:
        func(i,r) 
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    
    func(0,n-1)
        

