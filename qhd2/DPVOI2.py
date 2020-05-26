def BS(i):
    global count, a, t
    left = 1
    right = count
    while(left < right):
        mid = (left + right)//2
        if a[i][2] < a[t[mid]][2] and a[i][1] > a[t[mid]][1]:
            left = mid + 1
        else:
            right = mid
    return left

a = [[0,0,10**9]]
i = 0
while True:
    s = input()
    if s == '0' :
        break
    else:
        i += 1
        a.append([i] + list(map(int, s.split())))

a.sort(key = lambda x: x[2])
a.sort(key = lambda x: x[1])
t = [0]*(len(a))
f = [0]*(len(a))
res = 0
count = 0
for i in range(1, len(a)):
    if a[i][2] < a[t[count]][2] and a[i][1] > a[t[count]][1]:
        count += 1
        t[count] = i
        f[i] = count
    else:
        j = BS(i)
        # print(j ,end = ' ')
        # print(a[t[j]][2], end= ' ' )
        # print(a[i][2])
        if a[t[j]][2] < a[i][2]:
            t[j] = i
        f[i] = j
        
# print(t)
# print(f)
# for i in a:
#     print(i)
res = max(f)
ans = []
w, iq = 10**9, 0
for i in range(len(a)-1, 0, -1):
    if f[i] == res and a[i][1] < w and a[i][2] > iq:
        ans.append(str(a[i][0]))
        res -= 1
        w, iq = a[i][1], a[i][2] 
print(len(ans))
print(' '.join(ans[::-1]))