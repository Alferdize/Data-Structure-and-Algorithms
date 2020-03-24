def testcase():
    N, M = list(map(int, input().split()))
    cnt = 1 
    a = []
    b = []
    for i in range(1,N+M+1):
        a.append(int(input()))

        if i >= 4 and cnt != M:
            cnt +=1
            data = max(a[:i])
            index = a.index(data)
            a[index] = -1
            b.append(data)

        elif i  == M+N and cnt == M:
            data = max(a)
            index = a.index(data)
            a[index] = -1
            b.append(data)

    for i in b:
        print(i)


if __name__ == "__main__":
    testcase()