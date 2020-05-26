# import itertools

# x = input()
# a = list(itertools.permutations(x))
# a = set([''.join(x) for x in a])
# b = [x for x in a]
# b.sort()

# print(len(b))
# for i in b:
#     print(i)
def res(a):
    final.append(''.join(a))
def func(i):
    global check,arr
    for j in range(0,len(x)):
        if check[j] == 0:
            arr[i] = x[j]
            check[j] = 1
            if i == len(x)-1:
                res(arr)
            else:
                func(i+1)
            check[j] = 0
final = []
x = input()
check = [0]*(len(x))
arr = [0]*(len(x))
func(0)
print(final)
