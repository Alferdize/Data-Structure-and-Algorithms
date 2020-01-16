import math 

EPS = 1e-9


def product(data):
    n = len(data)
    sum = 0
    output = [1] * n
    for i in range(n):
        sum += math.log10(data[i])

    for i in range(n):
        output[i] *= int((EPS + pow(10.00,sum - math.log10(data[i]))))

    return output



print(product([1, 2, 3, 4, 5]))