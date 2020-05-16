def search(arr, n, k):
    for i in range(n):
        if arr[i] == k:
            return i+1
    return -1


if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    k = 10
    n = len(arr)
    result = search(arr, n, k)
    if result == -1:
        print("The data is not present in the List")
    else:
        print("The data is not present at %d location in arr" % result)
