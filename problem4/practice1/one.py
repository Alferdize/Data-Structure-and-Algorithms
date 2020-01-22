def swap(a, b):
    temp = a
    a = b
    b = temp


def findmissingPostive(data, n):
    print(data,n)
    for i in range(n):
        # print((abs(data[i])-1),data[abs(data[i])-1],n)
        if(abs(data[i])-1) < n and data[abs(data[i])-1] > 0:
            data[abs(data[i])-1] = - data[abs(data[i]) - 1]
    for i in range(n):
        if data[i] > 0:
            return i + 1
    return n + 1


def segregate(data, n):
    j = 0
    for i in range(n):
        if data[i] <= 0:
            swap(data[i], data[j])
            j += 1
    return j


def findmissing(data):
    n = len(data)
    shift = segregate(data, n)
    return findmissingPostive(data, n - shift)


print(findmissing([2, 4, 8, 1, 8, 4, -9, 4, 3, 6]))
