"""
daily_problem_2_3(uber).py
Third way to find array data product
"""

import math

EPS = 1e-9


def product(data_pro):
    """Return array Product"""
    sum_data = 0
    num_data = len(data_pro)  # Number of elements
    output_data = []  # to store the resultant array
    # to hold all sum values
    for i in range(num_data):
        sum_data += math.log10(data_pro[i])
    # output array calculation
    for i in range(num_data):
        data = int((EPS + pow(10.00, sum_data - math.log10(data_pro[i]))))
        output_data.append(data)
    return output_data


if __name__ == "__main__":
    DATA = [1, 2, 3, 4, 5]
    ARR = product(DATA)
    print(ARR)
