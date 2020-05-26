def func(a):
    dic = {}
    for i in range (-len(a),len(a)+1):
        dic[i] = 0

    dic[0] = 1
    sum = 0
    count = 0
    for i in a:
        if ( i.upper() == 'A' ):
            sum = sum - 1
            count = count + dic[sum]
            dic[sum] += 1
        else:
            sum = sum + 1
            count = count + dic[sum]
            dic[sum] += 1
    print(count)

if __name__ == "__main__":
    func('ababaabb')
    func('aabbaa')
    func('aababababbbbabab')