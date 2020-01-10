def product(data):
    n = len(data)
    left = [1] * n
    right = [1] * n
    for i in range(1,len(left)):
        left[i] = left[i-1] * data[i-1]
    for i in range(len(left)-2,-1,-1):
        right[i] = right[i+1] * data[i+1]
    for i in range(len(left)-2,0,-1):
        right[i] = left[i] * right[i]
    return right












if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    arr = product(data)
    print(arr)