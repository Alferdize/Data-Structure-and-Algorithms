import math

EPS = 1e-9


def product(data):
    n = len(data)
    output = [1] * n
    sum = 0
    for i in range(n):
        sum += math.log10(data[i])

    for i in range(n):
        output[i] *= int((EPS + pow(10.00,(sum - math.log10(data[i])))))

    return output


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    Arr = product(data)
    print(Arr)