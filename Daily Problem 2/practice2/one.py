"""
one.py
"""


import math

EPS = 1e-9


def product(data_func):
    sum_data = 0
    num_data = len(data_func)
    output_data = []

    for i in range(num_data):
        sum_data += math.log10(data_func[i])

    for i in range(num_data):
        output_data.append(
            int((EPS + pow(10.00, sum_data - math.log10(data_func[i])))))

    return output_data


if __name__ == "__main__":
    DATA = [1, 2, 3, 4, 5]
    ARR = product(DATA)
    print(ARR)
