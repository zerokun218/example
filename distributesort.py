import random
# from collections import OrderedDict

def func(arr):
    dic = {}
    for i in range(min(arr),max(arr)+1):
        dic[i] = 0
    for i in arr:
        dic[i] += 1

    array = []
    for k in dic:
        if( dic[k] != 0):
            array += [k]*dic[k]
    
    print(arr)
    print(len(arr))
    print(dic)
    print(array)
    print(len(array))

if __name__ == "__main__":
    a=[]
    for i in range(0,100):
        a.append(random.randint(-15,15))
    random.shuffle(a)
    func(a)