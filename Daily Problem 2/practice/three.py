"""
three.py
Product of elements in array
"""


def product_of_elements(data_pro):
    """Return  product of other elements"""
    num_ele = len(data_pro)
    left_data, right_data = [1]*num_ele, [1]*num_ele
    # Left product data
    for i in range(1, num_ele):
        left_data[i] = left_data[i-1] * data_pro[i-1]

    # Right product
    for i in range(num_ele-2, -1, -1):
        right_data[i] = right_data[i+1] * data_pro[i+1]

    # final product
    for i in range(num_ele):
        left_data[i] = right_data[i] * left_data[i]

    return left_data


if __name__ == "__main__":
    DATA = [1, 2, 3, 4, 5]
    ARR = product_of_elements(DATA)
    print(ARR)
