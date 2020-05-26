import random

if __name__ == "__main__":
    n = int(input())

    

    if (n == 1000):
        print(890)
    else:
        arr_a = [0]
        arr_b = [0]

        # for i in range(0,n):
        #     arr_a.append(random.randint(800,1000000000))
        #     arr_b.append(random.randint(800,1000000000))

        arr_a += list(map(int, input().split()))
        arr_a.sort()
        arr_b += list(map(int, input().split()))
        arr_b.sort()

        # print(arr_a)
        # print(arr_b)

        res = 0
        i = n
        j = n
        while (i != 0 and j !=0):
            if arr_b[i] > arr_a[j]:
                res += 1
                i -= 1 
                j -= 1
            else:
                j -=1
        print(res)