if __name__ == "__main__":
    n = int(input())

    arr_M = []
    arr_M += list(map(int, input().split()))

    arr_F = []
    arr_F += list(map(int, input().split()))

    arr_M1 = [] # Nam muon nhay voi Nu cao
    arr_M2 = [] # muon nhay voi Nu thap
    for i in arr_M:
        if i > 0:
            arr_M1.append(i)
        else:
            arr_M2.append(i*(-1))

    arr_F1 = [] # Nu muon nhay voi Nam cao
    arr_F2 = [] # muon nhay voi Nam thap
    for i in arr_F:
        if i > 0:
            arr_F1.append(i)
        else:
            arr_F2.append(i*(-1))

    arr_M1.sort(reverse=True) # nam muon nhay voi nu cao
    arr_F2.sort(reverse=True) # nu muon nhap voi nam thap

    count = 0
    i = 0
    j = 0

    while(i != len(arr_F2) and j != len(arr_M1)):
        if arr_F2[i] > arr_M1[j]:
            count += 1
            i += 1
            j += 1
        else:
            j += 1

    arr_F1.sort(reverse=True) # nu muon nhay voi nam cao
    arr_M2.sort(reverse=True) # nam muon nhap voi nu thap

    i = 0
    j = 0
    while(i != len(arr_M2) and j != len(arr_F1)):
        if arr_M2[i] > arr_F1[j]:
            count += 1
            i += 1
            j += 1
        else:
            j += 1
   
                    

    print(count)