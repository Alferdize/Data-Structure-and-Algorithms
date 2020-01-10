def product(data):
    n = len(data)
    left ,  right  = [1]*n,[1]*n
    for i in range(1, n):
        left[i] = left[i-1] * data[i-1]
    for i in range(n-2,-1,-1):
        right[i] = right[i+1] * data[i+1]
    for i in range(n):
        left[i] = left[i] * right[i]
    return left













if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    arr = product(data)
    print(arr)