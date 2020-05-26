# cnt = 0

# def longestDominoChain(tiles):
#     global cnt
#     dic = dict()
#     for i in tiles:
#         x,y = i[0], i[1]
#         if x not in dic:
#             cnt += 1
#             dic[x] = cnt
#         if y not in dic:
#             cnt += 1
#             dic[y] = cnt
#     # print(dic)
#     global check
#     check = dict()
#     global a
#     a = [[] for _ in range(cnt + 1)]
#     for i in tiles:
#         x,y = i[0], i[1]
#         x,y = min(x,y), max(x,y)
#         a[dic[x]].append(dic[y])
#         a[dic[y]].append(dic[x])
#         if '{}-{}'.format(dic[x],dic[y]) not in check:
#             check['{}-{}'.format(dic[x],dic[y])] = 1
#         else:
#             check['{}-{}'.format(dic[x],dic[y])] += 1
#     # print(dic)



# def dfs(u):
#     global avail1,m, ma
#     if avail1[u] < 1:
#         return
#     avail1[u] -= 1
    
#     for i in a[u]:
#         if avail1[i] > 0:
#             avail1[i] -= 1
#             m[i] = m[u] + 1
#             ma = max(ma, m[i])
#             dfs(i)
            

# tiles = [[2,4], [5,4], [1,3], [3,6], [9,6]]
# longestDominoChain(tiles)
# avail = [0]*(cnt+1)
# for i in a:
#     for j in i:
#         avail[j] += 1
# l = [0]*(cnt+1)
# ma = 0

# for i in range(cnt+1):
#     avail1 = avail[:]
#     m = l[:]
#     dfs(i)

# print(ma)



# 
ma = 0
def dfs(u,avail1,m,ma):
    if avail1[u] < 1:
        return
    avail1[u] -= 1
    
    for i in a[u]:
        if avail1[i] > 0:
            avail1[i] -= 1
            m[i] = m[u] + 1
            dfs(i,avail1,m,ma)
            
def longestDominoChain(tiles):
    cnt = 0
    dic = dict()
    for i in tiles:
        x,y = i[0], i[1]
        if x not in dic:
            cnt += 1
            dic[x] = cnt
        if y not in dic:
            cnt += 1
            dic[y] = cnt
    # print(dic)
    global check
    check = dict()
    global a
    a = [[] for _ in range(cnt + 1)]
    for i in tiles:
        x,y = i[0], i[1]
        x,y = min(x,y), max(x,y)
        a[dic[x]].append(dic[y])
        a[dic[y]].append(dic[x])
        if '{}-{}'.format(dic[x],dic[y]) not in check:
            check['{}-{}'.format(dic[x],dic[y])] = 1
        else:
            check['{}-{}'.format(dic[x],dic[y])] += 1

    avail = [0]*(cnt+1)
    for i in a:
        for j in i:
            avail[j] += 1
    l = [0]*(cnt+1)
    global ma
    for i in range(cnt+1):    
        avail1 = avail[:]
        m = l[:]
        dfs(i,avail1,m,ma)
        ma = max(ma,max(m))

    return ma
    
tiles = [[2, 3], [2, 3], [3, 4], [3, 4], [4, 5], [4, 5], [5, 6], [5, 6], [6, 7], [6, 7], [7, 8], [7, 8], [8, 9], [8, 9], [9, 10], [9, 10], [10, 11], [10, 11], [11, 12], [11, 12], [12, 13], [12, 13], [13, 14], [13, 14], [14, 15], [14, 15], [15, 16], [15, 16], [16, 17], [16, 17], [17, 18], [17, 18], [18, 19], [18, 19], [19, 20], [19, 20], [20, 21], [20, 21], [21, 2], [21, 2], [2, 22], [2, 23], [2, 24], [2, 25], [22, 23], [22, 24], [22, 25], [23, 24], [23, 25], [24, 25], [3, 26], [3, 27], [3, 28], [3, 29], [26, 27], [26, 28], [26, 29], [27, 28], [27, 29], [28, 29], [4, 30], [4, 31], [4, 32], [4, 33], [30, 31], [30, 32], [30, 33], [31, 32], [31, 33], [32, 33], [5, 34], [5, 35], [5, 36], [5, 37], [34, 35], [34, 36], [34, 37], [35, 36], [35, 37], [36, 37], [6, 38], [6, 39], [6, 40], [6, 41], [38, 39], [38, 40], [38, 41], [39, 40], [39, 41], [40, 41], [7, 42], [7, 43], [7, 44], [7, 45], [42, 43], [42, 44], [42, 45], [43, 44], [43, 45], [44, 45], [8, 46], [8, 47], [8, 48], [8, 49], [46, 47], [46, 48], [46, 49], [47, 48], [47, 49], [48, 49], [9, 50], [9, 51], [9, 52], [9, 53], [50, 51], [50, 52], [50, 53], [51, 52], [51, 53], [52, 53], [10, 54], [10, 55], [10, 56], [10, 57], [54, 55], [54, 56], [54, 57], [55, 56], [55, 57], [56, 57], [11, 58], [11, 59], [11, 60], [11, 61], [58, 59], [58, 60], [58, 61], [59, 60], [59, 61], [60, 61], [12, 62], [12, 63], [12, 64], [12, 65], [62, 63], [62, 64], [62, 65], [63, 64], [63, 65], [64, 65], [13, 66], [13, 67], [13, 68], [13, 69], [66, 67], [66, 68], [66, 69], [67, 68], [67, 69], [68, 69], [14, 70], [14, 71], [14, 72], [14, 73], [70, 71], [70, 72], [70, 73], [71, 72], [71, 73], [72, 73], [15, 74], [15, 75], [15, 76], [15, 77], [74, 75], [74, 76], [74, 77], [75, 76], [75, 77], [76, 77], [16, 78], [16, 79], [16, 80], [16, 81], [78, 79], [78, 80], [78, 81], [79, 80], [79, 81], [80, 81], [17, 82], [17, 83], [17, 84], [17, 85], [82, 83], [82, 84], [82, 85], [83, 84], [83, 85], [84, 85], [18, 86], [18, 87], [18, 88], [18, 89], [86, 87], [86, 88], [86, 89], [87, 88], [87, 89], [88, 89], [19, 90], [19, 91], [19, 92], [19, 93], [90, 91], [90, 92], [90, 93], [91, 92], [91, 93], [92, 93], [20, 94], [20, 95], [20, 96], [20, 97], [94, 95], [94, 96], [94, 97], [95, 96], [95, 97], [96, 97], [21, 98], [21, 99], [21, 100], [21, 101], [98, 99], [98, 100], [98, 101], [99, 100], [99, 101], [100, 101], [19, 102], [102, 103], [103, 104], [104, 105], [105, 106], [106, 107], [107, 108], [108, 109], [109, 110], [110, 111], [21, 112], [112, 113], [113, 114], [114, 115], [115, 116], [116, 117], [117, 118], [118, 119], [20, 120], [120, 121], [121, 122], [122, 123], [123, 124], [124, 122]]

print(longestDominoChain(tiles))