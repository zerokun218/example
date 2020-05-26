def switch_string(s1,s2):
    a = []
    b = []
    s = ''
    if len(s1) != len(s2):
        return False
    for i in range(0,len(s1)):
        if s1[i] != s:
            a += [1]
            s = s1[i]
        else:
            a[-1] += 1
    s = ''
    for i in range(0,len(s2)):
        if s2[i] != s:
            b += [1]
            s = s2[i]
        else:
            b[-1] += 1
    i = len(a)-1
    j = len(b)-1
    print(a)
    print(b)
    while(i >= 0 and j >=0):
        print(a[i])
        print(b[j])
        if a[i] > b[j]:
            return False
        elif a[i] < b[j]:
            a[i-1] += a[i]
            a[i] = 0
            i -= 1
            
        else:
            i -= 1
            j -= 1

    return True

switch_string('cddb','abcc')