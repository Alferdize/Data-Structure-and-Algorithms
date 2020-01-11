"""
two.py
"""


# calculating product
def product(data_func):
    """Return Product """
    n_data = len(data_func)  # no. of elements
    left_data, right_data = [1]*n_data, [1]*n_data

    # left multiplication
    for i in range(1, n_data):
        left_data[i] = left_data[i-1] * data_func[i-1]

    # right multiplication
    for i in range(n_data-2, -1, -1):
        right_data[i] = right_data[i+1] * data_func[i+1]

    # final product
    for i in range(n_data):
        left_data[i] = left_data[i] * right_data[i]

    return left_data


if __name__ == "__main__":
    DATA = [1, 2, 3, 4, 5]
    ARR = product(DATA)
    print(ARR)
