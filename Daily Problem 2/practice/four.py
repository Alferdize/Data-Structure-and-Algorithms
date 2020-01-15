"""
four.py
"""
def product(data):
    n = len(data)
    left = [1] * n
    temp = 1
    for i in range(1, n):
        left[i] = data[i-1] * left[i-1]


    for i in range(n-2,-1,-1):
        temp = temp * data[i+1]
        left[i] *= temp

    return left


if __name__ == "__main__":
    print(product([1, 2,3 , 4, 5]))