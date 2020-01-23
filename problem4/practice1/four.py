import random
import time
def swap(a, b):
    temp = a
    a = b
    b = temp


def segregate(data, n):
    j = 0
    for i in range(n):
        if data[i] < 0:
            swap(data[i], data[j])
            j += 1
    return j


def postiveminimum(data, n):
    for i in range(n):
        if abs(data[i]-1) < n and data[abs(data[i])-1] > 0:
            data[abs(data[i])-1] = - data[abs(data[i])-1]

    for i in range(n):
        if data[i] > 0:
            return i + 1
    return n + 1


def min_missing(data):
    n = len(data)
    shift = segregate(data, n)
    return postiveminimum(data, n - shift)


if __name__ == "__main__":
    start = time.time()
    data = [i for i in range(1,1000000)]
    data.remove(random.randint(1,1000000))
    print(min_missing(data))
    print(time.time() - start)
