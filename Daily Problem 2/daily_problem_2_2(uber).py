"""
daily_problem_2_2(uber).py
Second style of product
"""

def product_array(data_pro):
    num_ele = len(data_pro)
    left_data = [1]*num_ele
    temp_data = 1
    
    # Left product
    for i in range(1,num_ele):
        left_data[i] = left_data[i-1] * data_pro[i-1]

    # Right product 
    for i in range(num_ele-2,-1,-1):
        temp_data *= data_pro[i+1]
        left_data[i] *= temp_data

    return left_data


if __name__ == "__main__":
    DATA = [1, 2, 3, 4, 5]
    ARR = product_array(DATA)
    print(ARR)