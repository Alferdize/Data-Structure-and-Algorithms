"""
four.py
"""
import math

EPS = 1e-9

def product(data):
    n = len(data)
    sum = 0
    output_data = [1]*n
    for i in range(n):
        sum += math.log10(data[i])

    for i in range(n):
        # print(sum)
        # print(math.log10(data[i]))
        # print(sum - math.log10(data[i]))
        # print(EPS)
        # print(pow(10.00 , sum - math.log10(data[i])))
        output_data[i] *= int((EPS + pow(10.00 , sum - math.log10(data[i]))))

    return output_data


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    print(product(data))