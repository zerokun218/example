if __name__ == "__main__":
    n = int(input())

    arr = []
    arr += list(map(int, input().split()))

    for i in range(0,len(arr)-1):
        vtmin = i
        j = i+1
        while (j < len(arr)):
            if ( arr[vtmin] > arr[j]):
                vtmin = j
                j += 1
            else:
                j += 1
        temp = arr[:]
        arr[i], arr[vtmin] =arr[vtmin],arr[i]
        if ( arr[i] == arr[vtmin] ):
            temp[i] = '[' + str(temp[i]) + ']'
        else:
            temp[i], temp[vtmin] = '[' + str(temp[vtmin]) + ']', '[' + str(temp[i]) + ']'
        for i in temp:
            print(i, end=' ')
        print()
