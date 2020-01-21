import math 

EPS = 1e-9


def product(a):
    n = len(a)
    output_data = [1] * n
    sum = 0
    for i in range(n):
        sum += math.log10(a[i])

    for i in range(n):
        output_data[i] *= int(EPS + pow(10.00,sum - math.log10(a[i])))

    print(output_data)


if __name__ == "__main__":
    product([1,2,3,4,5])