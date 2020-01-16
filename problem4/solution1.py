def swap(a, b):
    temp = a
    a = b
    b = temp


def segregate(data):
    j = 0
    for i in range(len(data)):
        if data[i] <= 0:
            swap(data[i], data[j])
            j += 1
    return j


def findmissingPostive(data, n):
    for i in range(n):
        if (abs(data[i]) - 1) < n and data[abs(data[i]) - 1] > 0:
            data[abs(data[i]) - 1] = - data[abs(data[i]) - 1]

    for i in range(n):
        if data[i] > 0:
            return i + 1
    return n + 1


def findmissing(data):
    n = len(data)
    shift = segregate(data)
    return findmissingPostive(data, n - shift)


print(findmissing([2, 4, 8, 1, 8, 4, -9, 4, 3, 6]))
