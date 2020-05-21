def search(arr, x):
    n = len(arr)
    low = 0
    high = n-1
    while low < high:
        mid = (low+high)//2
        if arr[mid] == x:
            return mid
        if arr[mid] < x:
            low = mid+1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 20
    print(search(arr, x))
